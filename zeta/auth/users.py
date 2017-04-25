# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""User component"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   1. There is no point in providing the `userreltype_remove()`, since the
#      relation that is removed might already be referenced (via foreign key
#      constraints) elsewhere.
#   2. post-processing function can be subscribed to onclose event and can
#      thus be delayed until the request is completed.
#   3. `pylons.config` is initialized as late as possible from 0.10rc1 and 1.0
#      versions, so methods that will be invoked via create_models() pass the
#      config parameter explicitly.
# Todo    :
#   1. Unit testing for create_permname(), create_apppermissions() methods.
#   2. Test cases for 'sitepgroups' and 'projpgroups'

from   __future__               import with_statement

from   hashlib                  import sha1

from   sqlalchemy               import *
from   sqlalchemy.orm           import *
from   paste.util.import_string import eval_import
from   pylons                   import config

from   zeta.ccore               import Component
from   zeta.auth.perm           import permissions
import zeta.auth.perm           as permmod
from   zeta.model               import meta
from   zeta.model.schema        import t_project, t_project_team, t_user, \
                                       t_permission_group, at_user_permissions, \
                                       at_project_admins, at_permission_maps, \
                                       t_permission_name, t_user_info
from   zeta.model.tables        import System, User, UserInfo, UserRelation_Type, \
                                       UserRelation, UserInvitation, \
                                       PermissionName, PermissionGroup, Attachment
from   zeta.lib.error           import ZetaUserError, ZetaAuthorizationError, \
                                       ZetaAuthenticationError
import zeta.lib.helpers         as h
import zeta.lib.cache           as cache

# In-module caching
gcache_permnames      = []
gcache_proj_permnames = []
gcache_site_permnames = []

builtin_all = all
builtin_any = any

class UserComponent( Component ) :
    """Manage User authentication using database defined by zeta.model"""

    def _queryattrs( self, q, attrload_all, attrload ) :
        if attrload_all :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
        if attrload :
            q = q.options( *[ eagerload( e ) for e in attrload ] )
        return q

    def _md5( self, password, secret='' ) :
        result = md5(password)
        secret and result.update(secret)
        result = result.hexdigest()
        return result

    def _sha1( self, password, secret='' ) :
        result = sha1(password)
        secret and result.update(secret)
        result = result.hexdigest()
        return result

    def doencrypt( self, password, enctype='sha1' ) :
        if enctype == 'md5' :
            return self._md5( password )
        if enctype == 'sha1' :
            return self._sha1( password )
    
    # Existence Methods
    def user_exists( self, user ) :
        """Returns ``True`` if a user exists with the given username, 
        ``False`` otherwise. Usernames are case insensitive."""
        return (self.get_user( user ) and True) or False
        
    def user_has_password( self, user, password ) :
        """Returns ``True`` if the user has the password specified, ``False`` 
        otherwise. Passwords are case sensitive. Raises an exception if the
        user doesn't exist."""
        user = self.get_user( user )
        if not user :
            return False
        elif user.disabled :
            return False
        elif unicode( user.password ) == self.doencrypt( password ) :
            return True
        else :
            return False

    def user_has_permnames( self, user, permnames, checkall=False ) :
        """Returns ``True`` if the user has all the permnames
        (when checkall=True) or when the user has any of the permnames
        (when checkall=False)
        ``False`` otherwise. Raises an exception if the user doesn't exist.
        """
        if isinstance( permnames, (str, unicode) ) :
            permnames = [ permnames ]

        upn     = self.user_permnames( user )
        granted = map( lambda p : p in upn, permnames )
        return builtin_all( granted ) if checkall else builtin_any( granted )

    def user_has_permgroups( self, user, permgroups, all=False ) :
        """Returns ``True`` if the user has all the permgroups (when all=True)
        or when the user has any of the permgroups (when all=False). ``False``
        otherwise. Raises an exception if the user doesn't exist.
        """
        if isinstance( permgroups, (str, unicode) ) :
            permgroups = [ permgroups ]

        upg     = self.user_permgroups( user )
        granted = map( lambda pg : pg in upg, permgroups )
        if all :
            return builtin_all( granted )
        else :
            return builtin_any( granted )
        
    # List Methods
    def list_users( self ) :
        """Returns a lowercase list of all usernames ordered alphabetically."""
        return self._usernames()

    def list_emailids( self ) :
        """Returns a list of all user emailids in sorted order."""
        stmt = select( [ t_user.c.emailid ],
                       order_by=[asc(t_user.c.emailid)],
                       bind=meta.engine
                     )
        return [ tup[0] for tup in stmt.execute().fetchall() if tup[0] ]

    # User Methods
    def user( self, username ) :
        """Returns a dictionary in the following format:

        .. code-block :: Python
        
            {
                'username': username,
                'group':    None,
                'password': password,
                'roles':    []
            }

        The role names are ordered alphabetically
        Raises an exception if the user doesn't exist."""
        msession = meta.Session()
        username = unicode(username)
        user = msession.query( User ).filter_by( username=username ).first()
        if user :
            return { 'username': user.username,
                     'group':    None,
                     'password': user.password,
                     'roles':    []
                   }
        else :
            raise ZetaAuthenticationError( "No such user %r"%username )

    def get_userrel_type( self, relationtype=None ) :
        """Get user relation type identified by,
        `relationtype`, which can be,
            `id` or `userrel_type` or `UserRelation_Type` instance.
        if relationtype==None,
            then return a list of all UserRelation_Type instances.
            
        Return,
            A list UserRelation_Type instances, or
            UserRelation_Type instance."""
        msession = meta.Session()

        if isinstance( relationtype, (int, long) ) :
            relationtype = msession.query( UserRelation_Type 
                           ).filter_by( id=relationtype ).first()

        elif isinstance( relationtype, (str,unicode) ) :
            relationtype = msession.query( UserRelation_Type 
                           ).filter_by( userrel_type=relationtype ).first()
            
        elif relationtype == None :
            relationtype = msession.query( UserRelation_Type ).all()

        elif isinstance( relationtype, UserRelation_Type ) :
            pass

        else :
            relationtype = None

        return relationtype

    def get_user( self, user=None, attrload_all=[], attrload=[] ) :
        """Get user entry identified by,
        `user` which can be,
            `id` or `username` or `User` instance.
        if user=None,
            Then all the registered users will be returned.

        Always eager load, 'userinfo' attribute as well.

        Return,
            A list of User instances, or
            User instance."""

        if isinstance( user, User ) and attrload_all==[] and attrload==[] :
            return user

        msession = meta.Session()

        # Compose query based on `user` type
        if isinstance( user, (int,long) ) :
            q = msession.query( User ).filter_by( id=user )
        elif isinstance( user, (str, unicode) ) :
            q = msession.query( User ).filter_by( username=unicode(user) )
        elif isinstance( user, User ) :
            q = msession.query( User ).filter_by( id=user.id )
        else :
            q = None

        # Compose eager-loading options
        if q :
            q = self._queryattrs( q, attrload_all, attrload )
            user = q.first()

        elif user == None :
            q = msession.query( User )
            q = self._queryattrs( q, attrload_all, attrload )
            user = q.all()

        else :
            user = None

        # Gotcha : Dont know why userinfo is expired here
        # if isinstance( user, User ) :
        #     msession.expire( user.userinfo )
        return user

    def get_userrel( self, userrelation=None, userfrom=None, userto=None,
                     reltype=None ) :
        """Get the user relation entry identified by,
        `userrelation` which can be,
            `id` or `UserRelation` instance.
        if userrelation == None,
            then the UserRelation entries are filtered by `userfrom`, `userto`
            and `reltype` object.

        Return,
            Lists of all UserRelation instances or
            UserRelation instance."""
        userfrom = userfrom and self.get_user( userfrom )
        userto   = userto and self.get_user( userto )
        reltype  = reltype and self.get_userrel_type( reltype )
        msession = meta.Session()

        if isinstance( userrelation, (int, long) ) :
            userrelations = msession.query( UserRelation 
                            ).filter_by( id=userrelation ).first()

        elif isinstance( userrelation, UserRelation ) :
            userrelations = userrelation

        elif userfrom or userto or reltype :
            q = msession.query( UserRelation )
            if userfrom :
                q = q.filter_by( userfrom_id=userfrom.id )
            if userto :
                q = q.filter_by( userto_id=userto.id )
            if reltype :
                q = q.filter_by( userreltype_id=reltype.id )
            userrelations = q.all()

        else :
            userrelations = msession.query( UserRelation ).all()

        return userrelations

    def user_password( self, user ) :
        """Returns the password associated with the user or ``None`` if no
        password exists. Raises an exception is the user doesn't exist."""
        user = self.get_user( user )
        return user and user.password or None

    def user_permnames( self, user ) :
        """Returns a list of all the permission names for the given user 
        ordered alphabetically. Raises an exception if the user doesn't exist."""
        oj = t_user.outerjoin( at_user_permissions,
                  ).outerjoin(
                        t_permission_group,
                        at_user_permissions.c.groupid == t_permission_group.c.id
                  ).outerjoin(
                        at_permission_maps,
                        t_permission_group.c.id == at_permission_maps.c.groupid 
                  ).outerjoin(
                        t_permission_name,
                        at_permission_maps.c.permid == t_permission_name.c.id
                  )
        q = select( [ t_permission_name.c.perm_name ],
                    order_by=[asc(t_permission_name.c.perm_name)],
                    bind=meta.engine
                  ).select_from( oj )
        if isinstance(user, (int, long)) :
            q = q.where( t_user.c.id == user )
        elif isinstance(user, User) :
            q = q.where( t_user.c.id == user.id )
        elif isinstance(user, (str, unicode)) :
            q = q.where( t_user.c.username == user )
        else :
            raise ZetaUserError( "No such user %s" % user )

        entries = list( set([ x[0] for x in q.execute().fetchall() if x[0] ]))
        return entries


    def user_permgroups( self, user ) :
        """Returns a list of all the permission groups for the given user 
        ordered alphabetically. Raises an exception if the user doesn't exist."""
        oj = t_user.outerjoin( at_user_permissions,
                  ).outerjoin(
                        t_permission_group,
                        at_user_permissions.c.groupid == t_permission_group.c.id
                  )
        q  = select( [ t_permission_group.c.perm_group ],
                     order_by=[asc(t_permission_group.c.perm_group)],
                     bind=meta.engine
                   ).select_from( oj )
        if isinstance(user, (int, long)) :
            q = q.where( t_user.c.id == user )
        elif isinstance(user, User) :
            q = q.where( t_user.c.id == user.id )
        elif isinstance(user, (str, unicode)) :
            q = q.where( t_user.c.username == user )
        else :
            raise ZetaUserError( "No such user %s" % user )

        entries = list( set([ x[0] for x in q.execute().fetchall() if x[0] ]))
        return entries

    # User Creation, modification and deletion.
    def userreltype_create( self, userrel_types, byuser=None ) :
        """Create user relation entries for the relations specified by,
        `userrel_type`
            which can be, a string specifying the relation name or a list of
            such strings"""
        from zeta.config.environment import tlcomp

        if isinstance( userrel_types, (str,unicode) ) :
            userrel_types = [ userrel_types ]

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ msession.add( UserRelation_Type( unicode(r) )) 
              for r in userrel_types ]

        # Database Post processing
        tlcomp.log(
            byuser, 'added user relation types, `%s`' % ', '.join(userrel_types)
        )

    @h.postproc()
    def user_create( self, user, userinfo=None, update=False, doclose=None ) :
        """Before creating the user validate the user information.
        `user`     tuple of user account info.
                   (username, emailid, password, timezone)
        `userinfo` tuple of user personal info
                   (fname,   mname, lname, addr1, addr2, city, pcode, state,
                    country, userpanes)
        if update=True,
            An existing user details will be updated.
            In which case `userinfo` can be None . But `user` should
            follow the tuple format.

        Return,
            User instance."""
        from zeta.config.environment import tlcomp, srchcomp

        user = list(user)
        user[0] = user[0].lower()
        q  = select([ t_user.c.id ], bind=meta.engine 
                   ).where( t_user.c.username == user[0] )
        uid = [ tup[0] for tup in q.execute().fetchall() if tup[0] ]
        uid = uid and uid[0]

        # Convert the password into digest.
        user[2] = user[2] and sha1( user[2] ).hexdigest()

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if ( update and uid ) or uid :  # Update user
                kwargs = {}
                kwargs.setdefault( 'username', user[0] )
                user[1] != None and kwargs.setdefault( 'emailid', user[1] )
                user[2] != None and kwargs.setdefault( 'password', user[2] )
                user[3] != None and kwargs.setdefault( 'timezone', user[3] )
                stmt = t_user.update().where( t_user.c.username == user[0]
                                            ).values( **kwargs )
                res = msession.connection().execute(stmt)

                if userinfo :
                    kwargs = {}
                    uiattrs = [ 'firstname', 'middlename', 'lastname',
                                'addressline1', 'addressline2', 'city',
                                'pincode', 'state', 'country', 'userpanes' ]
                    [ kwargs.setdefault( uiattrs[i], userinfo[i] )
                            for i in range(10) if userinfo[i] != None ]
                    stmt = t_user_info.update().where(
                                t_user_info.c.user_id == uid
                           ).values( **kwargs )
                    res = msession.connection().execute(stmt)

                log = 'updated user preference'
                idxreplace = True

            else :                      # Create new user
                kwargs = dict( zip(
                            ['username', 'emailid', 'password', 'timezone' ],
                            list(user)
                         ))
                stmt = t_user.insert().values( **kwargs )
                res = msession.connection().execute(stmt)
                uid = res.inserted_primary_key[0]

                kwargs = dict( filter( 
                            lambda x : x[1] != None,
                            zip(
                               [ 'user_id', 'firstname', 'middlename',
                                 'lastname', 'addressline1', 'addressline2',
                                 'city', 'pincode', 'state', 'country',
                                 'userpanes' ],
                               [ uid ] + list(userinfo)
                            )
                         ))
                kwargs.setdefault( 'userpanes', u'siteuserpanes' )
                stmt = t_user_info.insert().values( **kwargs )
                res = msession.connection().execute(stmt)

                log = 'registered new user'
                idxreplace = False

        u = self.get_user( uid )

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_usersite )

        def onclose(tlcomp, srchcomp, uid, log, idxreplace) :
            tlcomp.log( uid, log )
            if idxreplace == False :
                self.user_add_permgroup( uid, permmod.default_siteperms,
                                         byuser=uid )
            srchcomp.indexuser( [uid], replace=idxreplace )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, uid, log, idxreplace ))
        return u


    def user_remove( self, user, byuser=None ) :
        """Remove the user identified by,
        `user` which can be,
            `id` or `username` or `User` instance.
        
        Note : Removing the user could orphan the following items,
                attachment
                project administration
                project components
                tickets prompting the user
                ticket status
                ticket comments
                review author
                review moderator
                review comments
                wiki creator
                wiki author
                wiki comments.
                and much more ....."""
        from zeta.config.environment import tlcomp, srchcomp

        user     = self.get_user( user ) 
        # Make sure to remove the user attachments before removing the user.
        self.user_set_photo( user )
        self.user_set_icon( user )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            msession.delete( user )

        # Post processing
        tlcomp.log( byuser, 'removed user `%s`' % user.username )


    @h.postproc()
    def user_set_photo( self, user, photo=None, doclose=None ) :
        """Attachment object (entry) to be assiociated as user photo for
        `user`. If a photo attachment is already associated with the user,
        then the old attachment is removed and replaced with new photo
        attachment.
        if photo==None,
            then remove the photo attachment."""
        from zeta.config.environment import attcomp, tlcomp

        log = ''
        user = self.get_user( user )
        msession = meta.Session()

        with msession.begin( subtransactions=True ) :
            if user :
                if isinstance( user.photofile, Attachment ) :   # Remove
                    attcomp.remove_attach( user.photofile, byuser=user )
                    log = 'removed user photo'
                if photo :                                      # Add
                    user.photofile = attcomp.get_attach( photo )
                    photo.uploader = user
                    log = 'uploaded user photo, `%s`' % photo.filename

        # Post processing, optional deferred handling
        def onclose(tlcomp, user, log) :
            log and tlcomp.log( user, log )
        doclose( h.hitchfn( onclose, tlcomp, user, log ))
        return None

    @h.postproc()
    def user_set_icon( self, user, icon=None, doclose=None ) :
        """Attachment object (entry) to be assiociated as user icon for
        `user`. If an icon attachment is already associated with the user,
        then the old attachment is removed and replaced with new icon
        attachment.
        if icon==None,
            then remove the icon attachment."""
        from zeta.config.environment import attcomp, tlcomp, srchcomp

        log      = ''
        user     = self.get_user( user )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if user :
                if isinstance( user.iconfile, Attachment ) :    # Remove
                    attcomp.remove_attach( user.iconfile, byuser=user )
                    log = 'removed user icon'
                if icon :                                       # Add
                    user.iconfile = attcomp.get_attach( icon )
                    icon.uploader = user
                    log = 'uploaded user icon, `%s`' % icon.filename

        # Post processing, optional deferred handling
        def onclose(tlcomp, user, log) :
            log and tlcomp.log( user, log )
        doclose( h.hitchfn( onclose, tlcomp, user, log ))
        return None

    @h.postproc()
    def user_add_permgroup( self, user, perm_groups, doclose=None,
                            byuser=None, ) :
        """Add the permission group `perm_groups` for user identified by
        `user`. perm_groups must have already been created.
        `perm_groups` must be a list of permission group identified by,
            `perm_group` or PermissionGroup instance
        """
        from zeta.config.environment import tlcomp, srchcomp

        # convert the perm_groups list into homogenous list of 
        # de-normalized permission group names
        if not isinstance( perm_groups, list ) :
            perm_groups = [ perm_groups ]
        perm_groups = [ isinstance(pg, PermissionGroup) and pg.perm_group or pg
                        for pg in perm_groups if pg ]
        denormalize = lambda pg : [ pg, 'defgrp_'+pg.lower() ][ pg.isupper() ]
        perm_groups_ = perm_groups
        perm_groups = map( denormalize, perm_groups )

        _pglist  = []
        [ _pglist.extend([ (pg.perm_group, pg), (pg.id, pg) ])
          for pg in self.get_permgroup() ]
        pgdict = dict( _pglist )
        perm_groups = filter( None,
                              map( lambda pg : pgdict.get( pg, None ),
                                   perm_groups )
                            )

        user = self.get_user( user, attrload=[ 'permgroups' ] )
        u_pgs = [ pg.perm_group for pg in user.permgroups ]
        uid = user.id
        log = ''
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if user :
                for pg in perm_groups : 
                    if pg.perm_group not in u_pgs :
                        stmt = at_user_permissions.insert().values(
                                    userid=uid, groupid=pg.id )
                        msession.connection().execute(stmt)
                if perm_groups :
                    log = '%s, added permission groups, `%s`' % (
                              user.username, ', '.join( perm_groups_ )
                          )

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_usersite )
        def onclose(tlcomp, byuser, log) :
            log and tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return user

    @h.postproc()
    def user_remove_permgroup( self, user, perm_groups, doclose=None,
                               byuser=None ) :
        """Add the permission group `perm_groups` for user identified by
        `user`."""
        from zeta.config.environment import tlcomp, srchcomp

        # convert the perm_groups list into homogenous list of 
        # de-normalized permission group names
        if not isinstance( perm_groups, list ) :
            perm_groups = [ perm_groups ]
        perm_groups = [ isinstance(pg, PermissionGroup) and pg.perm_group or pg
                         for pg in perm_groups ]
        denormalize = lambda pg : [ pg, 'defgrp_'+pg.lower() ][ pg.isupper() ]
        perm_groups_ = perm_groups
        perm_groups = map( denormalize, perm_groups )

        _pglist  = []
        [ _pglist.extend([ (pg.perm_group, pg), (pg.id, pg) ])
          for pg in self.get_permgroup() ]
        pgdict = dict( _pglist )
        user = self.get_user( user, attrload=[ 'permgroups' ] )
        log = ''
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if user :
                [ user.permgroups.remove( pgdict[pg] ) for pg in perm_groups ]

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_usersite )
        if perm_groups and user :
            log = '%s, deleted permission groups, `%s`' % (
                     user.username, ', '.join( perm_groups_ )
                  )

        def onclose(tlcomp, byuser, log) :
            log and tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return user

    def user_add_relation( self, user, relateduser, relationtype, byuser=None ) :
        """Relate user `user` and user `relateduser` as `relationtype`.
        `user` can be,
            `id` or `username` or `User` instance.
        `relateduser` can be,
            `id` or `username` or `User` instance.
        `relationtype` can be,
            `id` or `userrel_type` or `UserRelation` instance."""
        from zeta.config.environment import tlcomp, srchcomp

        user         = self.get_user( user )
        relateduser  = self.get_user( relateduser )
        relationtype = self.get_userrel_type( relationtype )
        ur           = self.get_userrel( userfrom=user, userto=relateduser,
                                         reltype=relationtype )             
        msession     = meta.Session() 
        if ur :
            ur  = ur[0]
            log = ''
        else :
            with msession.begin( subtransactions=True ) :
                ur             = UserRelation()
                ur.userreltype = relationtype
                ur.userfrom    = user
                ur.userto      = relateduser
                msession.add( ur )
                log = 'Proposed a relation `%s` to user `%s`' % \
                            ( relationtype.userrel_type, user.username )

        # Post processing
        log and tlcomp.log( byuser, log )

        return ur


    def user_approve_relation( self, userrelations, approve=True, byuser=None ) :
        """Approve the userrelations identified by 
        `userrelations` which can be,
            `id` or `UserRelation` instance or
            list of `id` and `UserRelation` instances."""
        from zeta.config.environment import tlcomp, srchcomp

        if not isinstance( userrelations, list ) :
            userrelations = [ userrelations ]
        userrelations = [ self.get_userrel( ur ) for ur in userrelations ]
        logs          = []
        msession      = meta.Session() 
        with msession.begin( subtransactions=True ) :
            for ur in userrelations :
                if not ur :
                    continue
                ur.approved = approve
                logs.append(
                    'approved relation `%s` from user `%s`' % \
                        ( ur.userreltype.userrel_type, ur.userfrom.username )
                )

        # Post processing
        [ tlcomp.log( byuser, log ) for log in logs ]
        

    def user_remove_relation( self, userrelations, byuser=None ) :
        """Remove the userrelations identified by 
        `userrelations` which can be,
            `id` or `UserRelation` instance or
            list of `id` and `UserRelation` instances."""
        from zeta.config.environment import tlcomp, srchcomp
        
        if not isinstance( userrelations, list ) :
            userrelations = [ userrelations ]
        userrelations = [ self.get_userrel( ur ) for ur in userrelations ]
        logs          = []
        msession      = meta.Session()
        with msession.begin( subtransactions=True ) :
            for ur in userrelations :
                if not ur :
                    continue 
                logs.append(
                    'deleted user %s with relation `%s`' % \
                        ( ur.userto.username, ur.userreltype.userrel_type)
                )
                msession.delete( ur )

        # Post processing
        [ tlcomp.log( byuser, log ) for log in logs ]


    @h.postproc()
    def user_disable( self, users, disable=True, doclose=None, byuser=None ) :
        """Disable the user identified by,
        `user`, which can be,
            `id` or `username` or `User` instance.
        """
        from zeta.config.environment import tlcomp, srchcomp

        log = ''
        users = users if isinstance(users, list) else [users]
        users_ = []
        msession = meta.Session()
        for user in users :
            stmt = t_user.update()
            if isinstance(user, (int, long)) :
                stmt = stmt.where( t_user.c.id == user ).values( disabled=disable )
            elif isinstance(user, (str, unicode)) :
                stmt = stmt.where( t_user.c.username == user ).values( disabled=disable )
            elif isinstance(user, User) :
                stmt = stmt.where( t_user.c.id == user.id ).values( disabled=disable )
                user = user.username
            users_.append(user)

            with msession.begin( subtransactions=True ) :
                res = msession.connection().execute(stmt)

        # Post processing, optional deferred handling
        def onclose(tlcomp, disable, byuser, users_) :
            if disable :
                tlcomp.log(
                    byuser, 'disabled users, `%s`' % ', '.join(users_) )
            else :
                tlcomp.log(
                    byuser, 'enabled users, `%s`' % ', '.join(users_) )
        doclose( h.hitchfn( onclose, tlcomp, disable, byuser, users_ ))
        return users

    def inviteuser( self, user, emailid ) :
        """For `emailid` generate a digest and store it in database"""
        from zeta.config.environment import tlcomp, srchcomp

        digest   = sha1( user.username + emailid + 'erode' ).hexdigest()
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            uinv = UserInvitation( emailid, digest )
            uinv.byuser = user
            msession.add( uinv )
        tlcomp.log( user, 'Invited user, `%s`' % emailid )
        return digest

    def get_invitation( self, uinv=None ) :
        """Get `userinvitation` entries"""
        msession = meta.Session()
        if isinstance( uinv, (int, long) ) :
            uinvs = msession.query( UserInvitation ).filter_by( id=uinv).first()
        else :
            uinvs = msession.query( UserInvitation ).all()
        return uinvs

    def invbydigest( self, digest ) :
        """Fetch the invitation entry for `digest`"""
        msession = meta.Session()
        uinv = msession.query( UserInvitation ).filter_by( digest=digest ).first()
        return uinv

    def acceptedby( self, user, uinv ) :
        """`user` has accepted the invitation"""
        user     = self.get_user( user )
        msession = meta.Session()
        if isinstance( uinv, (int, long) ) :
            uinv = msession.query( UserInvitation ).filter_by( id=uinv ).first()
        with msession.begin( subtransactions=True ) :
            uinv.acceptedby = user.username

    def userbyemailid( self, emailid ) :
        """Fetch the User object matching `emailid`"""
        msession = meta.Session()
        user = msession.query( User ).filter_by( emailid=emailid ).first()
        return user

    # Data Crunching methods on user tables.

    def get_connections( self, user ) :
        """Process `userconnections` and `connectedusers` for the user identified by,
        `user` which can be,
            `id` or `username` or `User` instance.

        Return a tuple of three dictionaries ( touserrels, fromuserrels, potrels )
        with each dictionary element is a `userrel_type` to list mapping.
            The list mapped in touserrels is a tuple of,
                (user.username, user.id, approved)
            The list mapped in fromuserrels is a tuple of,
                (user.username, user.id, approved)
            The list mapped in potrels is a sequence of username."""
        allusers = [ u.username for u in self.get_user() ]
        user     = self.get_user(
                            user,
                            attrload_all=[ 'userconnections.userreltype',
                                           'userconnections.userto',
                                           'connectedusers.userreltype',
                                           'connectedusers.userfrom' 
                                         ]
                   )
        reltypes = [ rt.userrel_type for rt in self.get_userrel_type() ]

        touserrels   = dict([ (rt, []) for rt in reltypes ])
        fromuserrels = dict([ (rt, []) for rt in reltypes ])
        potrels      = dict([ (rt, allusers[:]) for rt in reltypes ])

        for ur in user.userconnections :
            touserrels[ ur.userreltype.userrel_type ].append(
                    ( ur.userto.username, ur.id, ur.approved )
            )
            if ur.userto.username in potrels[ ur.userreltype.userrel_type ] :
                potrels[ ur.userreltype.userrel_type ].remove(
                        ur.userto.username
                )

        for ur in user.connectedusers :
            fromuserrels[ ur.userreltype.userrel_type ].append(
                    (ur.userfrom.username, ur.id, ur.approved )
            )

        return touserrels, fromuserrels, potrels

    def projectnames( self, user ) :
        """Generate a list of projects that the `user` is associated with,
        if `user` is User object, it is assumed that `projecteams.project` and
        `adminprojects` attributes are -- eagerloaded.
        """
        if isinstance( user, User ) :
            names = [ pt.project.projectname for pt in user.projectteams ] + \
                    [ p.projectname for p in user.adminprojects ]

        elif isinstance( user, (int, long)) :
            oj = t_project.outerjoin( t_project_team 
                         ).outerjoin(
                            at_project_admins,
                            at_project_admins.c.projectid == t_project.c.id
                         )

            q  = select([ t_project.c.projectname ], bind=meta.engine 
                       ).select_from( oj
                       ).where( or_( t_project_team.c.user_id == user,
                                     at_project_admins.c.adminid == user
                                   )
                       )
            names = [ tup[0] for tup in q.execute().fetchall() if tup[0] ]

        elif isinstance( user, (str, unicode)) :
            tbl_auser = t_user.alias( 'adminuser' )
            oj = t_project.outerjoin( t_project_team
                         ).outerjoin(
                            t_user,
                            t_project_team.c.user_id == t_user.c.id
                         ).outerjoin(
                            at_project_admins,
                            at_project_admins.c.projectid == t_project.c.id
                         ).outerjoin(
                            tbl_auser,
                            at_project_admins.c.adminid == tbl_auser.c.id
                         )
            q  = select([ t_project.c.projectname], bind=meta.engine 
                       ).select_from( oj
                       ).where( or_( t_user.c.username == user,
                                     tbl_auser.c.username == user
                                   )
                       )
            names = [ tup[0] for tup in q.execute().fetchall() if tup[0] ]

        return list(set(names))

    def ustatus( self, users ) :
        """Alternate API to crunch userstatus by passing a prefetched list of
        users from DB"""
        return self._userstatus( users=users )

    def siteadmin( self ) :
        """Fetch data from database and crunch them for user, site-level
        administration
            Return, 
                ( usernames, userpermissionmap, userstatus )
        """
        allperms  = self.site_permnames
        status    = { 'enabled' : [], 'disabled' : [] }
        x_users   = [ 'admin', 'anonymous' ]
        lookup    = [ 'enabled', 'disabled' ]
        userperms = {}
        permmap   = {}
        usernames = []

        # Query Database
        oj       = t_user.outerjoin( at_user_permissions 
                                   ).outerjoin( t_permission_group )

        stmt     = select( [ t_user.c.username, t_user.c.disabled,
                             t_permission_group.c.perm_group
                           ],
                           bind=meta.engine
                         ).select_from( oj )

        # Loop through the result and format data.
        for tup in stmt.execute().fetchall() :
            if tup[0] in x_users : continue
            userperms.setdefault( tup[0], [] 
                                ).append( self.normalize_perms( tup[2] ))
            status[ lookup[ tup[1] ] ].append( tup[0] )
            usernames.append( tup[0] )

        # Compose the list of denied permission list as well.
        permmap   = dict([ 
                       ( u,
                         [ sorted( filter( None, userperms[u] )),
                           sorted(list(
                               set(allperms).difference( userperms[u] )
                           ))
                         ]
                       ) for u in userperms
                     ])

        # Prune redundant usernames
        usernames          = list(set( usernames ))
        status['enabled']  = list(set( status['enabled'] ))
        status['disabled'] = list(set( status['disabled'] ))

        return sorted(usernames), permmap, status


    def _usernames( self ) :
        """list of registered `username`"""
        stmt = select( [ t_user.c.username ],
                       order_by=[asc(t_user.c.username)],
                       bind=meta.engine
                     )
        return [ tup[0] for tup in stmt.execute().fetchall() if tup[0] ]

    def _reltypes( self ) :
        """Sorted list of `userrel_type`"""
        msession = meta.Session()
        rels     = msession.query( UserRelation_Type).order_by( 
                                            UserRelation_Type.userrel_type )
        return [ r.userrel_type for r in rels ]

    def _userstatus( self, users=[] ) :
        """UnSorted dictionary of disabled and enabled `usernames`"""
        d       = { 'enabled' : [], 'disabled' : [] }
        x_users = [ 'admin', 'anonymous' ]
        lookup  = [ 'enabled', 'disabled' ]

        if users :
            [ d[ lookup[ u.disabled ] ].append( u.username )
              for u in [ u for u in users if u.username not in x_users ] ]

        else :
            stmt   = select( [ t_user.c.username, t_user.c.disabled ],
                             bind=meta.engine
                           )
            [ d[ lookup[ tup[1] ] ].append( tup[0] )
              for tup in stmt.execute().fetchall() if tup[0] not in x_users ]

        return d

    # PermissionName Creation, PermissionGroup creation and deletion.
    def permname_exists( self, perm_name ) :
        """Returns ``True`` if the PermissionName with perm_name exists,
        ``False`` otherwise. Permission Names are all in upper case."""
        p = self.get_permname( perm_name )
        return bool( p )

    def permgroup_exists( self, perm_group ) :
        """Returns ``True`` if the PermissionGroup with perm_group exists,
        ``False`` otherwise. Permission Groups are all in lower case."""
        pg = self.get_permgroup( perm_group )
        return bool( pg )
        
    def list_permnames( self ) :
        """Returns a uppercase list of all PermissionNames ordered
        alphabetically."""
        global gcache_permnames
        if not gcache_permnames :
            msession = meta.Session()
            q = msession.query(PermissionName).order_by(PermissionName.perm_name)
            gcache_permnames = [ p.perm_name for p in q.all() ]
        return gcache_permnames

    def list_permgroups( self ) :
        """Returns a lowercase list of all PermissionGroups ordered
        alphabetically."""
        msession = meta.Session()
        q = msession.query(PermissionGroup).order_by(PermissionGroup.perm_group)
        return [ pg.perm_group for pg in q.all() ]

    def get_permname( self, perm_name=None ) :
        """Get the PermissionName instance identified by,
        `perm_name` which can be,
            `id` or `perm_name` or `PermissionName` instance.
        if perm_name=None,
            PermissionName instance. or
            List of PermissionName instances
        """
        msession = meta.Session()
        if isinstance( perm_name, (int, long) ) :
            perm_name = msession.query( PermissionName ).filter_by( id=perm_name ).first()
        elif isinstance( perm_name, (str, unicode) ) :
            perm_name = msession.query( PermissionName ).filter_by( perm_name=perm_name ).first()
        elif perm_name == None :
            perm_name = msession.query( PermissionName ).all()
        elif isinstance( perm_name, PermissionName ) :
            pass
        else :
            perm_name = None
        return perm_name

    def get_permgroup( self, perm_group=None, attrload=[], attrload_all=[] ) :
        """Get the PermissionGroup instance identified by,
        `perm_group` which can be,
            `id` or `perm_group` or `PermissionGroup` instance.
        if perm_group=None,
            PermissionGroup instance. or
            List of PermissionGroup instances"""
        if isinstance( perm_group, PermissionGroup ) and attrload==[] and \
                attrload_all==[] :
            return perm_group

        msession = meta.Session()

        # Compose query based on `perm_group` type
        if isinstance( perm_group, (int,long) ) :
            q = msession.query( PermissionGroup ).filter_by( id=perm_group )
        elif isinstance( perm_group, (str, unicode) ) :
            perm_group = perm_group.isupper() and ('defgrp_' + perm_group.lower()) \
                         or perm_group
            q = msession.query( PermissionGroup ).filter_by(
                perm_group=unicode(perm_group) )
        elif isinstance( perm_group, PermissionGroup ) :
            q = msession.query( PermissionGroup ).filter_by( id=perm_group.id )
        else :
            q = None

        # Compose eager-loading options
        if q :
            q = self._queryattrs( q, attrload_all, attrload )
            perm_group = q.first()
        elif perm_group == None :
            q = msession.query( PermissionGroup )
            q = self._queryattrs( q, attrload_all, attrload )
            perm_group = q.all()
        else :
            perm_group = None

        return perm_group

    def create_permname( self, perm_name, byuser=None ) :
        """Add entries for perm_name in permission_name table. Check before
        adding and add the corresponding 'defgrp_...' permission group as
        well."""
        from zeta.config.environment import tlcomp, srchcomp

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            perm_name = perm_name.upper()
            if not self.get_permname( perm_name ) :
                p  = PermissionName( perm_name )
                pg = PermissionGroup( 'defgrp_'+perm_name.lower() )
                msession.add( p )
                msession.add( pg )
                pg.perm_names = [ p ]

        # Database Post processing
        tlcomp.log( byuser, 'created new permission name `%s`' % perm_name )

        return p, pg

    def change_permname( self, perm_name, new_name, byuser=None ) :
        """Change `perm_name` name."""
        from zeta.config.environment import tlcomp, srchcomp

        pn       = self.get_permname( perm_name )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            pn.perm_name = new_name

        # Database Post processing
        tlcomp.log( byuser, 'changed permission name name to `%s`' % new_name )

        return pn

    def create_apppermissions( self, permissions, byuser=None ) :
        """Create all the permission names implemented by the application."""
        [ self.create_permname( aperm.perm_name, byuser=byuser )
          for compname in permissions.keys() for aperm in permissions[compname]]

    @h.postproc()
    def create_permgroup( self, perm_group, doclose=None, byuser=None ) :
        """Add an entry for perm_group in permission_group table."""
        from zeta.config.environment import tlcomp, srchcomp

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            pg = PermissionGroup( perm_group.lower() )
            msession.add( pg )

        # Post processing, optional deferred handling
        def onclose(tlcomp, byuser, perm_group) :
            tlcomp.log( byuser, 'created new permission group `%s`' % perm_group )
        doclose( h.hitchfn( onclose, tlcomp, byuser, perm_group ))
        return pg

    @h.postproc()
    def change_permgroup(self, perm_group, new_name, doclose=None, byuser=None):
        """Change the perm_group name."""
        from zeta.config.environment import tlcomp, srchcomp

        pg       = self.get_permgroup( perm_group )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            pg.perm_group = new_name

        # Post processing, optional deferred handling
        def onclose(tlcomp, byuser, new_name) :
            tlcomp.log( byuser, 'changed permission group name to `%s`' % new_name )
        doclose( h.hitchfn( onclose, tlcomp, byuser, new_name ))
        return pg

    @h.postproc()
    def add_permnames_togroup( self, perm_group, perm_names, append=True,
                               doclose=None, byuser=None ) :
        """Add the specified list of permission names `perm_names` to already
        created `perm_group`."""
        from zeta.config.environment import projcomp, tlcomp, srchcomp

        perm_group = self.get_permgroup( perm_group, attrload=['perm_names'] )

        # convert the perm_names list into homogenous list of 
        # de-normalized permission names
        if not isinstance( perm_names, list ) :
            perm_names = [ perm_names ]
        perm_names = [ isinstance( pn, PermissionName ) and pn.perm_name or pn
                       for pn in perm_names if pn ]
        
        log = ''
        _pnlist  = []
        [ _pnlist.extend([ (pn.perm_name, pn), (pn.id, pn) ])
          for pn in self.get_permname() ]
        pndict = dict( _pnlist )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if append :
                perm_group.perm_names.extend([ pndict[pn] for pn in perm_names ])
            else :
                perm_group.perm_names = [ pndict[pn] for pn in perm_names ]

        log = 'added permnames to permgroup %s,\n%s' % (
                    perm_group.perm_group,
                    ', '.join([ pndict[pn].perm_name for pn in perm_names ]),
              ) if perm_names else ''

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_usersite )
        cache.invalidate( projcomp.mapfor_teamperms )
        def onclose( tlcomp, byuser, log ) :
            log and tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return perm_group

    @h.postproc()
    def remove_permnames_fromgroup( self, perm_group, perm_names, doclose=None,
                                    byuser=None ) :
        """Remove the specified list of permission names `perm_names` from already
        created `perm_group`."""
        from zeta.config.environment import projcomp, tlcomp, srchcomp

        perm_group = self.get_permgroup( perm_group )

        # convert the perm_names list into homogenous list of 
        # de-normalized permission names
        if not isinstance( perm_names, list ) :
            perm_names = [ perm_names ]
        perm_names = [ isinstance( pn, PermissionName ) and pn.perm_name or pn
                       for pn in perm_names if pn ]

        _pnlist  = []
        [ _pnlist.extend([ (pn.perm_name, pn), (pn.id, pn) ])
          for pn in self.get_permname() ]
        pndict = dict( _pnlist )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ perm_group.perm_names.remove( pndict[pn] ) for pn in perm_names ]

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_usersite )
        cache.invalidate( projcomp.mapfor_teamperms )
        log = 'deleted permnames from permgroup %s,\n%s' % \
                    ( perm_group.perm_group,
                      ', '.join([ pndict[pn].perm_name for pn in perm_names ]),
                    ) if perm_names else ''
        def onclose(tlcomp, byuser, log ) :
            log and tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return perm_group

    @h.postproc()
    def remove_permgroup( self, perm_groups, doclose=None, byuser=None ) :
        """Remove permission group identified by,
        `perm_groups` which can be,
            `id` or `perm_group` or `PermissionGroup` instance.
            list of id` or `perm_group` or `PermissionGroup` instance."""
        from zeta.config.environment import tlcomp, srchcomp

        if not isinstance( perm_groups, list ) :
            perm_groups = [ perm_groups ]

        pgroups   = []
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            for pg in perm_groups :
                pg = self.get_permgroup( pg )
                if pg :
                    pgroups.append( pg.perm_group )
                    # Remove Project-User permission
                    [ msession.delete( projectperm )    
                            for projectperm in pg.projectperms ]
                    # Remove the Project-Team permission
                    [ msession.delete( projteamperm )  
                            for projteamperm in pg.projteamperms ]
                    # Since User permissions are entered in association
                    # tables, they are automatically removed.
                    msession.delete( pg )

        # Post processing, optional deferred handling
        log = 'deleted permission groups,\n`%s`' % ', '.join(pgroups)
        def onclose(tlcomp, byuser, log ) :
            tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return None

    # Data Crunching methods on permission database.

    def normalize_perms( self, perms ) :
        """Since the permission names are mapped to 'defgrp_' permission
        groups, this function differentiates the permission names from
        permission groups and returns the normalised version of permission
        list.
        `perms` is a list of permission groups / permission names as strings. 
        """
        if isinstance( perms, list ) :
            normalizedperms = []
            for p in perms :
                if p[:7] == 'defgrp_' :
                    normalizedperms.append( p[7:].upper() )
                else :
                    normalizedperms.append( p )
            return sorted(normalizedperms)
        elif isinstance( perms, (str, unicode) ) :
            return [ perms, perms[7:].upper() ][ perms[:7] == 'defgrp_' ]

    def userpermission_map( self, usernames=[], allusers=[] ) :
        """Return a dictionary of
            { username : [ [ perm_groups ... ], [ ^ perm_groups ... ] ]
              ...
            }
        Only site permissions (for each user) are covered by this function.
        """
        allperms  = self.site_permnames

        #users     = allusers or self.get_user( attrload=[ 'permgroups' ] )
        #userperms = [ ( u.username,
        #                self.normalize_perms(
        #                    [ pg.perm_group for pg in u.permgroups ] )
        #              ) for u in users
        #            ]

        #permmap   = dict([ ( u,
        #                     [ perms,
        #                       sorted(list(set(allperms).difference(perms))) ]
        #                   ) for u, perms in userperms ])

        oj   = t_user.outerjoin( at_user_permissions 
                               ).outerjoin( t_permission_group )

        stmt = select( [ t_user.c.username, t_permission_group.c.perm_group ],
                        bind=meta.engine
                     ).select_from( oj )

        userperms = {}
        [ userperms.setdefault( tup[0], [] ).append(
            self.normalize_perms( tup[1] )
          ) for tup in stmt.execute().fetchall() if tup[0] ]

        permmap   = dict([ 
                       ( u,
                         [ sorted( filter( None, userperms[u] )),
                           sorted(list(
                               set(allperms).difference( userperms[u] )
                           ))
                         ]
                       ) for u in userperms
                     ])

        if usernames :
            [ permmap.pop( u ) for u in permmap.keys() if u not in usernames ]

        return permmap

    @cache.cache( 'mapfor_usersite', useargs=False )
    def mapfor_usersite( self ) :
        """Generate the permission map for site users"""
        maps      = {}
        skipusers = [ 'admin', 'anonymous' ]
        users     = self.get_user( attrload_all=[ 'permgroups.perm_names' ] )
        for u in users :
            if u.username in skipusers :
                continue
            maps[u.username] = [ pn.perm_name 
                                 for pg in u.permgroups for pn in pg.perm_names]
        return maps

    def _perm_names( self ) :
        """Sorted list of all permission names in the database."""
        global gcache_permnames
        if not gcache_permnames :
            msession = meta.Session()
            gcache_permnames = [ 
                p.perm_name 
                for p in msession.query( PermissionName 
                                       ).order_by( PermissionName.perm_name )
            ]
        return gcache_permnames

    def _proj_permnames( self ) :
        """Sorted list of all permission names that have project context"""
        global gcache_proj_permnames
        if not gcache_proj_permnames :
            permnames             = self._perm_names()
            gcache_proj_permnames = [
                a.perm_name for comp in permissions for a in permissions[comp]
                            if a.project and a.perm_name in permnames
            ]
        return gcache_proj_permnames

    def _site_permnames( self ) :
        """Sorted list of all permission names that only have site context"""
        global gcache_site_permnames
        if not gcache_site_permnames :
            permnames             = self._perm_names()
            gcache_site_permnames = [
                a.perm_name for comp in permissions for a in permissions[comp]
                            if not a.project and a.perm_name in permnames 
            ]
        return gcache_site_permnames

    def _perm_groups( self ) :
        """Sorted list of all permission groups in the database"""
        msession = meta.Session()
        return [ pg.perm_group 
                 for pg in msession.query( PermissionGroup 
                                         ).order_by(PermissionGroup.perm_group)
               ]

    def _mappedpgroups( self ) :
        """unsorted list of permission groups that are one-to-one mapped to
        permission groups"""
        return [ pg.perm_group for pg in self.get_permgroup()
                               if pg.perm_group[:7] == 'defgrp_' ]

    def _custompgroups( self ) :
        """unsorted list of permission groups that are created by users"""
        return [ pg.perm_group for pg in self.get_permgroup()
                               if pg.perm_group[:7] != 'defgrp_' ]

    def _pgmap( self ) :
        """unsorted dictionary of permission maps
            { perm_group : [ [ perm_name, perm_name ...],
                             [ x_perm_name, x_perm_name ... ]
                           ],
              ...
            }
        """
        allpermnames = self.perm_names

        pgmap        = {}
        msession     = meta.Session()
        permgroups   = self.get_permgroup( attrload=[ 'perm_names' ] )
        for pg in permgroups :
            if pg.perm_group[:7] == 'defgrp_' :
                continue
            permnames   = [ p.perm_name for p in pg.perm_names ]
            x_permnames = list(set(allpermnames).difference( set(permnames) ))
            pgmap.setdefault( pg.id, 
                              [ pg.perm_group, permnames, x_permnames ]
                            )

        return pgmap

    def _pgroupsbytype( self ) :
        """mapped permission groups and custom permission groups as a
        dictionary of,
            { 'mapped' : [ sorted list of permission group names ],
              'custom' : [ sorted list of permission group names ]
            }
        names"""
        d = { 'mapped' : [], 'custom' : [] }
        for pgroup in self._perm_groups() :
            if pgroup[:7] == 'defgrp_' :
                d['mapped'].append( pgroup )
            else :
                d['custom'].append( pgroup )
        d['mapped'].sort()
        d['custom'].sort()
        return d

    def _sitepgroups( self, permgroups=None ) :
        """Prune all the permission groups that contain project-level permission
        names and return those that have only site-level permission names"""
        permgroups = permgroups == None and \
                            self.get_permgroup( attrload=[ 'perm_names' ] ) \
                     or permgroups
        projpnames = self.proj_permnames
        for pg in permgroups[:] :
            for pn in pg.perm_names :
                if pn.perm_name in projpnames :
                    permgroups.remove( pg )
                    break;
        return permgroups

    def _projpgroups( self, permgroups=None ) :
        """Prune all the permission groups that contain site-level permission
        names and return those that have only project-level permission
        names"""
        permgroups = permgroups == None and \
                            self.get_permgroup( attrload=[ 'perm_names' ] ) \
                     or permgroups
        sitepnames = self.site_permnames
        for pg in permgroups[:] :
            for pn in pg.perm_names :
                if pn.perm_name in sitepnames :
                    permgroups.remove( pg )
                    break;
        return permgroups

    # Doc - metadata for 'user' table entries
    def documentof( self, user, search='xapian' ) :
        """Make a document for 'user' entry to create a searchable index
            [ metadata, attributes, document ], where

            metadata   : { key, value } pairs to be associated with document
            attributes : searchable { key, value } pairs to be associated with
                         document
            document   : [ list , of, ... ] document string, with increasing
                         weightage
        """
        user  = self.get_user( user, attrload=[ 'userinfo' ] )
        uinfo = user.userinfo

        metadata = \
            { 'doctype' : 'user', 'id' : user.id }
           
        attributes = \
            search == 'xapian' and \
                [ 'XID:user_%s'   % user.id,                # id
                  'XCLASS:site', 'XCLASS:user',             # class
                  'XUSER:%s'      % user.username,          # user
                  'XEMAIL:%s'     % user.emailid,           # email
                  'XTZONE:%s'     % user.timezone,          # tzone
                  'XCITY:%s'      % uinfo.city,             # city
                  'XSTATE:%s'     % uinfo.state,            # state
                  'XCOUNTRY:%s'   % uinfo.country,          # country
                  'XPINCODE:%s'   % uinfo.pincode,          # pincode
                ] \
            or \
                []

        attrs = ' '.join([ getattr( user, a )
                           for a in [ 'username', 'emailid', 'timezone' ] ])
        cont1 = attrs + ' ' + \
                ' '.join(
                    [ getattr( uinfo, a ) or ''
                      for a in [ 'firstname', 'middlename', 'lastname',
                                 'addressline1', 'addressline2', 'city',
                                 'state', 'country', 'pincode' ]
                    ]
                )
        cont2 = attrs + ' ' + \
                ' '.join([ getattr( uinfo, a ) or ''
                           for a in [ 'city', 'state', 'country', 'pincode' ]
                        ])
        document = [ cont1, cont2 ]

        return [ metadata, attributes, document ]

    # User properties
    reltypes   = property( _reltypes )
    usernames  = property( _usernames )
    userstatus = property( _userstatus )

    # Permission properties
    perm_names    = property( _perm_names )
    proj_permnames= property( _proj_permnames )
    site_permnames= property( _site_permnames )
    perm_groups   = property( _perm_groups )
    mappedpgroups = property( _mappedpgroups )
    custompgroups = property( _custompgroups )
    mixedpnames   = property(
                        lambda self : self._perm_names() + self._custompgroups()
                    )
    pgmap         = property( _pgmap )
    sitepgroups   = property( _sitepgroups )
    projpgroups   = property( _projpgroups )
