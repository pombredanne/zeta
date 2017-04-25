# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Form component that implements form request and submit handlers using
design pattern ideas.

VForm class implements the `form-visit` pattern.
Example,
    vf = Vform( compmgr )
    vf.process( request, c, **kwargs )

vf.process() call will have the following parameters that are significant
request,
    The request object.
c, 
    The context object.
defer,
    Keyword argument, to implement post processing on `close` event.
formnames,
    Keyword argument, specifying the list of formnames to handle.
errhandler,
    Keyword argument, providing the call back on `ZetaFormError`

Every form is handled in a form handler `Component` class, which has, the
following signigicant attributes,
formname,
    either a string or list of formnames
getparams, 
    double list of form field elements from Query, one for request another for
    submit
getparamsall, 
    double list of form field elements from Query, one for request another for
    submit
postparams,
    double list of form field elements from POST data, one for request another
    for submit
postparamsall,
    double list of form field elements from POST data, one for request another
    for submit

When a new Form component needs to implemented, use the following example,

    class FormSomeform( Component ) :

        forname = [...]
        getparams = ( [...], [...] )
        getparamsall = ( [...], [...] )
        postparams = ( [...], [...] )
        postparamsall = ( [...], [...] )

        def requestform( self, request, c, **kwargs ) :
            ...

        def submitform( self, request, c, **kwargs ) :
            ...
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   Every form that is provided to the client will contain the following
#   hidden fields, as much as possible.
#       user_id     - authenticated user who requested the form.
#       license_id  - license id to which the form is applicable.
#       project_id  - project id to which the form is applicable.
#       ticket_id   - ticket id to which the form is applicable.
#       review_id   - review id to which the form is applicable.
#       wiki id     - wiki id to which the form is applicable.
#   * `user_id` will accompany all the forms, except the user registration form.
#   * if `project_id` accompanies `ticket`, `review` and `wiki` forms that the
#     form fields are entered in the context of that project.
#   * for attachment forms, instead of assuming the `user_id` as the
#     uploader, as explicit argument `user` is expected in the `submitform()`
#     interface.
# Todo    : None
#   1. `createtck`, also does ticket configuration. Update the unit-test
#      accordingly.
#   2. User-Relation feature is yet to changed to `Organisation` feature.
#   3. 'rmlic' Form Component seems to provide two ways of removing a license.
#      Document it !


from   __future__                         import with_statement
from   pytz                               import all_timezones, timezone
import datetime                           as dt
from   os.path                            import join

from   paste.deploy.converters            import asbool

from   zeta.ccore                         import Component, formcomponent
from   zeta.model                         import meta
from   zeta.model.tables                  import User, Wiki, WikiType, WikiTable_Map, \
                                                 WikiComment, wikipage_factory
from   zeta.lib.error                     import ZetaFormError
import zeta.lib.helpers                   as h
from   zeta.lib.constants                 import *
from   zeta.lib.captcha                   import Captcha, sessioncaptcha
from   zeta.lib.mailclient                import inviteuser

# In-module cache
gcache_formcomps = {}

class VForm( Component ) :
    """Component implementing the Vistor pattern for forms. Any body who wants
    to do forms processing, can call,
        VForm( comp_manager ).process( visitor, **kwargs ).
    where, 
        visitor is the Form component implementing the,
            `request()` and `submit()` api.
        kwargs will be directly passed to the `request()` and `submit()` api.

    defer,
        If set to True, form processing function will be packaged into
        callable object and returned to the caller. Caller can later call the
        object to complete the form processing.
    errhandler,
        call back for ZetaFormError
    """

    def _getparams( self, params, fields ) :
        res = []
        for f in fields :
            res.append( params.get(f[0], f[1]) ) \
                if isinstance(f, tuple) else res.append( params.get(f, None) )
        return res

    def _getparamsall( self, params, fields ) :
        return [ params.getall(k) for k in fields ]

    def _postparams( self, post, fields ) :
        res = []
        for f in fields :
            res.append( post.get(f[0], f[1]) ) \
                if isinstance(f, tuple) else res.append( post.get(f, None) )
        return res

    def _postparamsall( self, post, fields ) :
        return [ post.getall(k) for k in fields ]

    def _getargs( self, params, post, v, off ) :
        args = []
        hasattr(v, 'getparams') and \
            args.extend( self._getparams(params, v.getparams[off]) )
        hasattr(v, 'getparamsall') and \
            args.extend( self._getparamsall(params, v.getparamsall[off]) )
        hasattr(v, 'postparams') and \
            args.extend( self._postparams(post, v.postparams[off]) )
        hasattr(v, 'postparamsall') and \
            args.extend( self._postparamsall(post, v.postparamsall[off]) )
        return args

    def process( self, request, c, errhandler=None, defer=False, **kwargs ) :
        """Process the form"""
        global gcache_formcomps

        form = kwargs.pop( 'form', request.params.get('form', '') )
        formnames = kwargs.pop('formnames', request.params.getall('formname'))

        # Collect the form components to invoke.
        visitors = []
        for formname in formnames :
            v = gcache_formcomps.get( formname, None )
            formcls = formcomponent(formname)
            if not v :
                v = gcache_formcomps.setdefault(formname, formcls(self.compmgr))
            visitors.append( v )
        #if visitors == [] :
        #    raise ZetaFormError( 'Unknown formnames (`%s`)' % formnames )

        # This is where the forms are actually handled. Entry point to all
        # form form component methods in this file.
        handlers = []
        kwargs['defer'] = defer
        off = 0 if form=='request' else (1 if form=='submit' else None)

        try :
            if form == 'submit' and request.method != 'POST' :
                raise ZetaFormError(
                        'Forms submission can happen only via POST method' )

            if off == 0 :               # request
                for v in visitors :
                    args = self._getargs( request.params, request.POST, v, off )
                    handlers.append(v.requestform(request, c, *args, **kwargs))

            elif off == 1 :              # submit
                for v in visitors :
                    args = self._getargs( request.params, request.POST, v, off )
                    handlers.append( v.submitform(request, c, *args, **kwargs) )

            #else :
            #    raise ZetaFormError( 'Unexpected visit for form processing !!' )

        except ZetaFormError, (errmsg,) :
            if errhandler :
                errhandler( errmsg )
            else :
                raise

        finally :
            handlers = filter(None, handlers)
            h.onclose(c, handlers)

# This is an example form dont derive from this !!
class SampleForm( Component ) :
    def requestform( self ) :
        pass
    def submitform( self ) :
        pass

def parse_tags( tagnames ) :
    """tagnames is a comma seperated string,
    return a list of tagnames"""
    return [ t for t in [ t.strip(' ') for t in tagnames.split( ',' ) ] if t ]

# ------------------ System Froms ------------------------------

class FormSystem( Component ) :
    """Form Component to create/delete system table entries"""
    formname = 'system'
    postparams = (
        [],
        [ 'user_id', 'userrel_types', 'projteamtypes', 'tickettypes', 'ticketstatus',
          'ticketseverity', 'reviewnatures', 'reviewactions', 'wikitypes',
          'vcstypes', 'ticketresolv', 'specialtags', 'def_wikitype',
          'googlemaps', 'strictauth', 'welcomestring', 'userpanes',
          'regrbyinvite', 'invitebyall',
        ]
    )

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for system form"""

    def submitform( self, request, c,
                    user_id, userrel_types, projteamtypes, tickettypes,
                    ticketstatus, ticketseverity, reviewnatures, reviewactions,
                    wikitypes, vcstypes, ticketresolv, specialtags,
                    def_wikitype, googlemaps, strictauth, welcomestring,
                    userpanes, regrbyinvite, invitebyall,
                    defer=False, **kwargs
                  ) :
        """Create / delete system entries"""
        from zeta.config.environment import \
                userscomp, syscomp, projcomp, tckcomp, revcomp, vcscomp, wikicomp, tagcomp

        userrel_types = userrel_types != None and set(h.parse_csv(userrel_types))
        projteamtypes = projteamtypes != None and set(h.parse_csv(projteamtypes))
        tickettypes = tickettypes != None and set(h.parse_csv(tickettypes))
        ticketstatus = ticketstatus != None and set(h.parse_csv(ticketstatus))
        ticketseverity= ticketseverity != None and set(h.parse_csv(ticketseverity))
        reviewnatures = reviewnatures != None and set(h.parse_csv(reviewnatures))
        reviewactions = reviewactions != None and set(h.parse_csv(reviewactions))
        wikitypes = wikitypes != None and set(h.parse_csv(wikitypes))
        vcstypes = vcstypes != None and set(h.parse_csv(vcstypes))
        ticketresolv = ticketresolv != None and set(h.parse_csv(ticketresolv))
        specialtags = specialtags != None and set(h.parse_csv(specialtags))

        reltypes         = set(userscomp.reltypes)
        teams            = set(projcomp.teams)
        tcktypenames     = set(tckcomp.tcktypenames)
        tckstatusnames   = set(tckcomp.tckstatusnames)
        tckseveritynames = set(tckcomp.tckseveritynames)
        naturenames      = set(revcomp.naturenames)
        actionnames      = set(revcomp.actionnames)
        vcstypenames     = set(vcscomp.vcstypenames )
        typenames        = set(wikicomp.typenames)
        tagnames         = set(tagcomp.tagnames)

        addrel_types      = list( userrel_types.difference(reltypes) )
        addteams          = list( projteamtypes.difference(teams) )
        addtickettypes    = list( tickettypes.difference(tcktypenames) )
        addticketstatus   = list( ticketstatus.difference(tckstatusnames) )
        addticketseverity = list( ticketseverity.difference(tckseveritynames) )
        addreviewnatures  = list( reviewnatures.difference(naturenames) )
        addreviewactions  = list( reviewactions.difference(actionnames) )
        addwikitype       = list( wikitypes.difference(typenames) )
        addvcstypes       = list( vcstypes.difference( vcstypenames ))
        addspecialtags    = list( specialtags.difference( tagnames ) )

        if user_id :
            addrel_types and userscomp.userreltype_create( addrel_types )
            addteams and projcomp.create_projteamtype( addteams )
            addtickettypes and tckcomp.create_tcktype( addtickettypes )
            addticketstatus and tckcomp.create_tckstatus( addticketstatus )
            addticketseverity and tckcomp.create_tckseverity(addticketseverity)
            addreviewnatures and revcomp.create_reviewnature( addreviewnatures )
            addreviewactions and revcomp.create_reviewaction( addreviewactions )
            addwikitype and wikicomp.create_wikitype( addwikitype )
            addvcstypes and vcscomp.create_vcstype( addvcstypes )
            addspecialtags and [ tagcomp.create_tag(t) for t in addspecialtags ]

        se = {}
        userrel_types and   \
            se.update({ 'userrel_types' : ', '.join(userscomp.reltypes) })
        projteamtypes and   \
            se.update({ 'projteamtypes' : ', '.join(projcomp.teams) })
        tickettypes and     \
            se.update({ 'tickettypes' : ', '.join(tckcomp.tcktypenames) })
        ticketstatus and    \
            se.update({ 'ticketstatus' : ', '.join(tckcomp.tckstatusnames) })
        ticketseverity and  \
            se.update({ 'ticketseverity' : ', '.join(tckcomp.tckseveritynames) })
        reviewnatures and   \
            se.update({ 'reviewnatures' : ', '.join(revcomp.naturenames) })
        reviewactions and   \
            se.update({ 'reviewactions' : ', '.join(revcomp.actionnames) })
        vcstypes and        \
            se.update({ 'vcstypes' : ', '.join(vcscomp.vcstypenames) })
        wikitypes and       \
            se.update({ 'wikitypes' : ', '.join(wikicomp.typenames) })
        ticketresolv and    \
            se.update({ 'ticketresolv' : ', '.join(ticketresolv) })
        specialtags and     \
            se.update({ 'specialtags' : ', '.join(specialtags) })
        def_wikitype and    \
            se.update({ 'def_wikitype' : def_wikitype })
        googlemaps != None and      \
            se.update({ 'googlemaps' : googlemaps })
        strictauth and      \
            se.update({ 'strictauth' : strictauth })
        welcomestring != None and   \
            se.update({ 'welcomestring' : welcomestring })
        userpanes and       \
            se.update({ 'userpanes' : u', '.join(set(h.parse_csv( userpanes )))
                     })
        regrbyinvite and      \
            se.update({ 'regrbyinvite' : regrbyinvite })
        invitebyall and      \
            se.update({ 'invitebyall' : invitebyall })

        c.sysentries.update( se )

        syscomp.set_sysentry( c.sysentries, c=c, defer=defer, byuser=c.authuser)

# TODO : Defer this form handling.
class FormSiteLogo( Component ) :
    """Form Component to upload site logo"""
    formname = 'sitelogo'
    postparams = (
        [], [ 'user_id', ('sitelogofile', '') ]
    )

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for system form"""
        pass

    def submitform( self, request, c, user_id, sitelogo,
                    defer=False, **kwargs ) :
        """Create / delete system entries"""
        envpath   = self.compmgr.config.get( 'zeta.envpath' )

        if c.sitelogo and sitelogo != '' :
            open( join( envpath, 'public', c.sitelogo.lstrip(' /') ), 'w'
                ).write( sitelogo.file.read() )


class FormStaticWiki( Component ) :
    """Form Component to edit / delete static wiki page"""
    formname = [ 'editsw', 'delsw' ]
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'pathurl', 'text', 'wiki_typename', 'sourceurl' ]
    )

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for system form"""
        pass

    def submitform( self, request, c, formname,
                    user_id, pathurl, text, wiki_typename, sourceurl,
                    defer=False, **kwargs
                  ) :
        """Edit / delete static wiki page"""
        from zeta.config.environment import syscomp

        pathurl = pathurl or kwargs.get('pathurl', None)
        text = u'' if text == None else text

        if formname == 'editsw' and pathurl :
            h.validate_fields( request )
            syscomp.set_staticwiki(
                    pathurl, text, swtype=wiki_typename, sourceurl=sourceurl,
                    c=c, defer=defer, byuser=c.authuser
            )

        elif formname == 'delsw' and pathurl :
            syscomp.remove_staticwiki(
                    pathurl, c=c, defer=defer, byuser=c.authuser )


# ------------------ Permission Froms ------------------------------

class FormPermissions( Component ) :
    """Form component to create and map permission groups"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for permission groups"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete entries in permission_group, permission_name
        and permission_maps tables"""
        pass

class FormPermgroup( FormPermissions ) :
    """Form Component to create permission group and permission names"""
    formname = [ 'createpg', 'updatepg', 'addpntopg', 'delpnfrompg' ]

    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'perm_group_id', 'perm_group' ] )
    postparamsall = ( [], [ 'perm_name' ] )

    def submitform( self, request, c, formname,
                    perm_group_id, perm_group, perm_names,
                    defer=False, **kwargs
                  ) :
        """create perm_group and group perm_names under it"""
        from zeta.config.environment import userscomp

        if formname in [ 'createpg', 'updatepg' ] and not perm_group :
            raise ZetaFormError( 'perm_group cannot be empty !!' )

        elif formname in [ 'addpntopg', 'delpnfrompg' ] and not perm_names :
            raise ZetaFormError( 'perm_group cannot be empty !!' )

        h.validate_fields( request )

        if formname == 'createpg' :
            pg = userscomp.get_permgroup( perm_group )
            if not pg :
                pg = userscomp.create_permgroup( perm_group, c=c, defer=defer )
                userscomp.add_permnames_togroup( pg, perm_names, c=c, defer=defer )

        elif formname == 'updatepg' :
            pg = userscomp.get_permgroup( int(perm_group_id) )
            if pg.perm_group != perm_group :
                userscomp.change_permgroup( pg, perm_group, c=c, defer=defer )

        elif formname == 'addpntopg' :
            pg = userscomp.get_permgroup( int(perm_group_id) )
            userscomp.add_permnames_togroup( pg, perm_names, c=c, defer=defer )

        elif formname == 'delpnfrompg' :
            pg = userscomp.get_permgroup( int(perm_group_id) )
            userscomp.remove_permnames_fromgroup( pg, perm_names, c=c, defer=defer )


class FormDeletePermgroup( FormPermissions ) :
    """Form Component to delete permission group and permission names"""
    formname = 'delpg'
    postparamsall = ( [], ['perm_group'] )

    def submitform( self, request, c, perm_groups, defer=False, **kwargs ) :
        """delete perm_group"""
        from zeta.config.environment import userscomp

        perm_groups and userscomp.remove_permgroup( perm_groups, c=c, defer=defer )
        
# ------------------ User Forms ---------------------------------

class FormUsers( Component ) :
    """Form component to process user entries"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for users"""
        c.all_timezones = all_timezones

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete user entries"""
        pass

class FormCreateUser( FormUsers ) :
    """Form Component to create user entries"""
    formname = [ 'createuser', 'updateuser' ]
    postparams = (
        [],
        [ 'user_id', 'username', 'emailid', 'password', 'confpass', 'timezone',
          'firstname', ( 'middlename', '' ), 'lastname', 'addressline1',
          'addressline2', 'city', 'pincode', 'state', 'country', 'userpanes',
          'captcha'
        ]
    )

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for users"""
        c.captcha = Captcha()
        c.captcha_urlpath = c.captcha.urlpath

    def submitform( self, request, c,
                    user_id, username, emailid, password, confpass, timezone,
                    firstname, middlename, lastname, addressline1, addressline2,
                    city, pincode, state, country, userpanes, captcha,
                    defer=False, **kwargs ) :
        """create / update user entry"""
        from zeta.config.environment import userscomp

        errmsg       = ''
        errmsg       += ( not username and 'username, ' ) or ''
        errmsg       += ( not emailid and 'emailid, ' )  or ''
        errmsg       += ( not user_id and \
                          ( not password or password != confpass ) and \
                          'password, '
                        ) or ''
        errmsg       += ( not timezone and  'timezone, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )

        h.validate_fields( request )

        user  = ( unicode(username), unicode(emailid), password, timezone )
        uinfo = ( firstname, middlename, lastname, addressline1,
                  addressline2, city, pincode, state, country, userpanes )
        if user_id :
            userscomp.user_create( user, uinfo, update=True, c=c, defer=defer )

        elif userscomp.user_exists( username ) :
            raise ZetaFormError( "Username %s already exists" % username )

        elif captcha and sessioncaptcha().match( captcha.upper() ) :
            userscomp.user_create( user, uinfo, c=c, defer=defer )
            sessioncaptcha().destroy()

        elif kwargs.get( 'test', None ) :   # To get the unit test case going
            userscomp.user_create( user, uinfo, c=c, defer=defer )

        else :
            raise ZetaFormError( "Captcha mismatch" )

        return None


class FormUpdatePassword( FormUsers ) :
    """Form Component to update user password"""
    formname = 'updtpass'
    postparams = (
        [], [ 'user_id', 'password', 'confpass' ]
    )

    def submitform( self, request, c, user_id, password, confpass,
                    defer=False, **kwargs ) :
        """create / update user entry"""
        from zeta.config.environment import userscomp

        if password != confpass :
            raise ZetaFormError( 'Mismatch in the re-entering the password !!' )

        if user_id and password :
            user = userscomp.get_user( int(user_id) )
            user = ( user.username, user.emailid, password, user.timezone )
            userscomp.user_create( user, update=True, c=c, defer=defer )

        else :
            raise ZetaFormError( 'In-sufficient, detail user-id' )

class FormUserPhoto( FormUsers ) :
    """Form Component to update user photo attachment"""
    formname = [ 'userphoto', 'deluserphoto' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'attachfile' ])

    def submitform( self, request, c, formname, user_id, attachfile,
                    defer=False, **kwargs ) :
        """update user photo"""
        from zeta.config.environment import userscomp, attcomp

        user = kwargs.get( 'user', None )

        if attachfile != None and user_id and user :
            photo = attcomp.create_attach( attachfile.filename, 
                                           fdfile=attachfile.file, 
                                           uploader=user
                                         )
            userscomp.user_set_photo( int(user_id), photo, c=c, defer=defer )

        elif formname == 'deluserphoto' and user_id :
            userscomp.user_set_photo(int(user_id), photo=None, c=c, defer=defer)

        else :
            raise ZetaFormError( 'In-sufficient detail, user-id and attachfile')

class FormUserIcon( FormUsers ) :
    """Form Component to update user icon attachment"""
    formname = [ 'usericon', 'delusericon' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'attachfile' ])

    def submitform( self, request, c, formname, user_id, attachfile,
                    defer=False, **kwargs ) :
        """update user icon"""
        from zeta.config.environment import userscomp, attcomp

        user = kwargs.get( 'user', None )

        if attachfile != None and user_id and user :
            icon = attcomp.create_attach( attachfile.filename, 
                                          fdfile=attachfile.file, 
                                          uploader=user
                                        )
            userscomp.user_set_icon( int(user_id), icon, c=c, defer=defer )

        elif formname == 'delusericon' and user_id :
            userscomp.user_set_icon( int(user_id), icon=None, c=c, defer=defer )

        else :
            raise ZetaFormError( 'In-sufficient detail, user-id and attachfile')

class FormUserDisable( FormUsers ) :
    """Form Component to update user disable status"""
    formname = [ 'userdis', 'userenb' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], ['user_id'] )
    postparamsall = ( [], [ 'disable_user', 'enable_user' ] )

    def submitform( self, request, c, formname, user_id, disable_users, enable_users,
                    defer=False, **kwargs ) :
        """update user disable status"""
        from zeta.config.environment import userscomp

        userscomp.user_disable( disable_users, c=c, defer=defer
        ) if formname == 'userdis' else None
        userscomp.user_disable( enable_users, disable=False, c=c, defer=defer
        ) if formname == 'userenb' else None

class FormUserPermissions( FormUsers ) :
    """Form Component to update user permissions"""
    formname = [ 'adduserperms', 'deluserperms' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'username' ])
    postparamsall = ( [], [ 'perm_group' ] )

    def submitform( self, request, c, formname, user_id, username, perm_groups,
                    defer=False, **kwargs ) :
        """update user permissions"""
        from zeta.config.environment import userscomp

        if user_id and username :
            if formname == 'deluserperms' :
                userscomp.user_remove_permgroup(
                        username, perm_groups, c=c, defer=defer )
            else :
                userscomp.user_add_permgroup(
                        username, perm_groups, c=c, defer=defer )

        else :
            raise ZetaFormError( 'In-sufficient detail, user-id' )

class FormUserRelations( FormUsers ) :
    """Form Component to update user relations"""
    formname = [ 'adduserrels', 'approveuserrels', 'deluserrels' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'userrel_type', 'userfrom' ] )
    postparamsall = ( [], [ 'user_relation_id', 'userto' ] )

    def submitform( self, request, c, formname, user_id, userrel_type, userfrom,
                    user_relation_ids, tousers,
                    defer=False, **kwargs ) :
        """update user relations"""
        from zeta.config.environment import userscomp

        user_relation_ids = map( lambda x : int(x), user_relation_ids )

        if not user_id :
            raise ZetaFormError( 'In-sufficient detail, user_id' )

        if formname == 'approveuserrels' and user_relation_ids :
            userscomp.user_approve_relation( user_relation_ids, approve=True )

        elif formname == 'deluserrels' and user_relation_ids :
            userscomp.user_remove_relation( user_relation_ids )

        else :
            if userrel_type and userfrom and tousers :
                [ userscomp.user_add_relation( userfrom, userto, userrel_type )
                  for userto in tousers ]

            else :
                errmsg = 'In-sufficient detail for creating user relation'
                raise ZetaFormError( errmsg )


class FormInviteUser( FormUsers ) :
    """Form Component to invite user"""
    formname = 'inviteuser'
    postparams = ( [], [ 'user_id', 'emailid' ] )

    def submitform(self, request, c, user_id, emailid, defer=False, **kwargs) :
        """invite user"""
        from zeta.config.environment import userscomp
        from zeta.lib.base           import BaseController

        cntlr = BaseController()
        environ = kwargs.get( 'environ' )

        if user_id and emailid :
            user = userscomp.get_user( int(user_id) )
            environ = request.environ
            digest = userscomp.inviteuser( user, emailid )
            fullurl = h.fullurl( environ['HTTP_HOST'], environ['SCRIPT_NAME'],
                                 cntlr.url_userreg( digest ) )
            inviteuser( self.compmgr.config, emailid, fullurl, user,
                        c.sysentries['sitename'] )


class FormResetPass( FormUsers ) :
    """Form Component to reset user password"""
    formname = 'resetpass'
    postparams = ( [], [ 'password', 'confpass' ] )

    def submitform( self, request, c, password, confpass, defer=False, **kwargs ) :
        """Reset user password"""
        from zeta.config.environment import userscomp

        emailid = kwargs.get( 'emailid', None )
        user = emailid and userscomp.userbyemailid( unicode(emailid) )

        if user and password and ( password == confpass ) :
            user = ( user.username, user.emailid, password, user.timezone )
            userscomp.user_create( user, update=True, c=c, defer=defer )
        else :
            raise ZetaFormError( 'Failed to match requirements' )


# ------------------ License Forms ---------------------------------

class FormLicense( Component ) :
    """Form component to process license"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for license"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete user entries"""
        pass

class FormCreateLicense( FormLicense ) :
    """Form component to create / update license entry"""
    formname = [ 'createlic', 'updatelic' ]
    postparams = (
        [],
        [ 'user_id', 'license_id', 'licensename', 'summary', 'text', 'source',
          ( 'tags', '' ) ]
    )
    postparamsall = ( [], [ 'attachfile' ] )

    def submitform( self, request, c, user_id, license_id, licensename,
                    summary, text, source, tagnames, attachfile,
                    defer=False, **kwargs ) :
        """create / update license entry"""
        from zeta.config.environment import liccomp, attcomp

        license_id = license_id and int(license_id)
        tagnames = list(set(h.parse_csv( tagnames )))
        user = kwargs.get( 'user', None )

        errmsg       = ''
        errmsg       += ( not licensename and 'licensename, ' ) or ''
        errmsg       += ( not summary and 'summary, ' )  or ''
        errmsg       += ( not text and 'text, ' )  or ''
        errmsg       += ( not source and  'source, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )

        h.validate_fields( request )
            
        licensedet   = [ license_id, licensename, summary, text, source ]

        if license_id :
            liccomp.create_license( licensedet, update=True, c=c, defer=defer )

        elif liccomp.license_exists( licensename ) :
            raise ZetaFormError( "Licensename %s already exists" % licensename )

        else :
            l = liccomp.create_license( licensedet, c=c, defer=defer )
            tagnames and liccomp.add_tags( l, tagnames, c=c, defer=defer )
            if user :
                for attachfile in  attachfiles :
                    a = attcomp.create_attach( attachfile.filename, 
                                               fdfile=attachfile.file, 
                                               uploader=user
                                             )
                    liccomp.add_attach( l, a, c=c, defer=defer )

class FormRemoveLicense( FormLicense ) : # licensename
    """Form component to remove license entry"""
    formname = 'rmlic'
    postparams = ( [], [ 'user_id' ] )
    postparamsall = ( [], [ 'licensename' ] )

    def submitform( self, request, c, user_id, licensename, defer=False, **kwargs ) :
        """remove license entry"""
        from zeta.config.environment import liccomp

        licid = kwargs.get( 'licid', None )

        [ liccomp.remove_license( licensename, c=c, defer=defer )
          for licensename in licensename ]

        if isinstance( licid, (int,long) ) :
            liccomp.remove_license( licid, c=c, defer=defer )

class FormLicenseTags( FormLicense ) :
    """Form component to add / remove license tags"""
    formname = [ 'addlictags', 'dellictags' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'license_id', ('tags', '') ] )

    def submitform( self, request, c, formname, user_id, license_id, tagnames,
                    defer=False, **kwargs ) :
        """add / remove license tags"""
        from zeta.config.environment import liccomp

        tagnames = list(set(h.parse_csv( tagnames )))

        if license_id and formname == 'addlictags' :
            license_id = int( license_id )
            liccomp.add_tags( license_id, tagnames, c=c, defer=defer )

        if license_id and formname == 'dellictags' :
            license_id = int( license_id )
            liccomp.remove_tags( license_id, tagnames, c=c, defer=defer )

class FormLicenseAttachs( FormLicense ) :
    """Form component to add / remove license attachments"""
    formname = [ 'addlicattachs', 'dellicattachs' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'license_id' ] )
    postparamsall = ( [], [ 'attach_id', 'attachfile' ] )

    def submitform( self, request, c,
                    formname, user_id, license_id, attach_id, attachfiles,
                    defer=False, **kwargs
                  ) :
        """add / remove license attachments"""
        from zeta.config.environment import liccomp, attcomp

        user = kwargs.get( 'user', None )

        if license_id and formname == 'dellicattachs' :
            [ liccomp.remove_attach(
                    int(license_id), int(attach_id), c=c, defer=defer
              ) for attach_id in attach_id ]

        elif license_id and formname == 'addlicattachs'  and user :
            for attachfile in attachfiles :
                a = attcomp.create_attach( attachfile.filename, 
                                           fdfile=attachfile.file, 
                                           uploader=user
                                         )
                liccomp.add_attach( int(license_id), a, c=c, defer=defer )

# ------------------------ Attachment Forms ---------------------------

class FormAttachs( Component ) :
    """Form component to process attachments"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for attachment"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """create / update / delete attachment table entries"""
        pass

class FormAddAttachs( FormAttachs ) : # attachfile
    """Form component to remove attachment"""
    formname = 'addattachs'
    postparams = ( [], [ 'user_id', 'summary' ] )
    postparamsall = ( [], [ 'attachfile' ] )

    def submitform( self, request, c, user_id, summary, attachfiles,
                    defer=False, **kwargs ) :
        """add new attachment"""
        from zeta.config.environment import attcomp

        attachfiles = [ a for a in attachfiles if a != '' ]
        [ attcomp.create_attach(
                    attachfile.filename, 
                    fdfile=attachfile.file, 
                    uploader=int(user_id),
                    summary=summary,
                    log=True, c=c, defer=defer
          ) for attachfile in attachfiles ]

class FormRemoveAttach( FormAttachs ) :
    """Form component to remove attachment"""

    formname = 'rmattachs'

    postparams = ( [], [ 'user_id' ] )
    postparamsall = ( [], [ 'attach_id' ] )

    def submitform( self, request, c, user_id, attach_ids,
                    defer=False, **kwargs ) :
        """remove attachment"""
        from zeta.config.environment import attcomp

        [ attcomp.remove_attach( int(attach_id), log=True, c=c, defer=defer )
          for attach_id in attach_ids ]

class FormAttachsUpdate( FormAttachs ) :
    """Form component to update attachment summary and tags"""

    formname = [ 'attachssummary', 'attachstags' ]

    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'attachment_id', 'summary', ('tags', '') ] )

    def submitform( self, request, c, formname,
                    user_id, attachment_id, summary, tagnames,
                    defer=False, **kwargs ) :
        """update attachment entry"""
        from zeta.config.environment import attcomp

        tagnames = list(set( h.parse_csv(tagnames) ))

        if user_id and attachment_id and formname == 'attachssummary' :
            attcomp.edit_summary( int(attachment_id), summary=summary,
                                  c=c, defer=defer )

        if user_id and attachment_id and formname == 'attachstags' :
            attach  = attcomp.get_attach(
                            int(attachment_id), attrload=[ 'tags' ] )
            currtags= set([ tag.tagname for tag in attach.tags ])
            rmtags  = list( currtags.difference(tagnames) )
            addtags = list( set(tagnames).difference(currtags) )
            rmtags and attcomp.remove_tags(attach, tags=rmtags, c=c, defer=defer)
            addtags and attcomp.add_tags(attach, tags=addtags, c=c, defer=defer)
        

# --------------------------- Project Forms ----------------------------

class FormProjects( Component ) :
    """Form Component to process project fields"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for project"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """create / update / delete project table entries"""
        pass

class FormCreateProject( FormProjects ) :
    """Form component to create / update project entry"""
    formname = [ 'createprj', 'updateprj' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'projectname', 'summary', 'admin_email',
          'description', 'licensename', 'admin', ]
    )

    def submitform( self, request, c, user_id, project_id, projectname, summary,
                    admin_email, description, licensename, admin,
                    defer=False, **kwargs ) :
        """create / update project entry"""
        from zeta.config.environment import projcomp, wikicomp, syscomp
        from zeta.lib.base           import BaseController

        cntlr = BaseController()
        p = kwargs.get( 'project', None )        # Optimization

        errmsg = ''
        errmsg += ( not licensename and 'licensename, ' ) or ''
        errmsg += ( not summary and 'summary, ' )  or ''
        errmsg += ( not admin_email and 'admin_email, ' )  or ''
        errmsg += ( not description and  'description, ' ) or ''
        errmsg += ( not admin and  'admin, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )

        project = None
        if project_id :
            project_id = int(project_id)
            project = (p and (p.id == project_id) and p) or project_id

        h.validate_fields( request )
        prjdetail= [ None, projectname, summary, admin_email, licensename,
                     admin ]
        prjidetail = [ description ]

        if project :
            prjdetail[0] = project
            projcomp.create_project( prjdetail, prjidetail, update=True,
                                     c=c, defer=defer )

        elif projcomp.project_exists( projectname ) :
            raise ZetaFormError( "Projectname %s already exists" % projectname )

        else :
            # This is the place where the project gets created.
            p = projcomp.create_project( prjdetail, prjidetail, c=c, defer=defer )
            if p :
                # On successfull project creation, create the default 'homepage'
                w = wikicomp.create_wiki(
                        unicode( cntlr.url_wikiurl( p.projectname, PROJHOMEPAGE )),
                        wtype=c.sysentries.get( 'def_wikitype', None ),
                        creator=c.authuser, c=c, defer=defer
                    )
                # Before creating content associate the page with the project
                wikicomp.config_wiki( w, project=p, c=c, defer=defer )
                wikicomp.create_content(
                    w.id, c.authuser,
                    syscomp.get_staticwiki( u'p_homepage' ).text
                )

class FormProjectLicense( FormProjects ) :
    """Form component to update / remove project license"""
    formname = 'prjlic'
    postparams = ( [], [ 'user_id', 'project_id', 'licensename' ] )

    def submitform( self, request, c, user_id, project_id, licensename,
                    defer=False, **kwargs ) :
        """update / remove project license"""
        from zeta.config.environment import projcomp

        if not licensename :
            raise ZetaFormError( 'Check licensename !!' )

        if project_id :
            projcomp.config_project( int(project_id), license=licensename,
                                     c=c, defer=defer )

class FormProjectAdmin( FormProjects ) :
    """Form component to update project admin"""
    formname = 'prjadmin'
    postparams = ( [], [ 'user_id', 'project_id', 'adminname' ] )

    def submitform( self, request, c, user_id, project_id, adminname,
                    defer=False, **kwargs ) :
        """update project admin"""
        from zeta.config.environment import projcomp

        if not adminname :
            raise ZetaFormError( 'Check adminname !!' )

        if project_id :
            projcomp.config_project( int(project_id), admin=adminname,
                                     c=c, defer=defer )

class FormProjectFavorite( FormProjects ) :
    """Form component to add or remove a project being a user's favourite"""
    formname = 'projfav'
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'addfavuser', 'delfavuser' ] )

    def submitform( self, request, c, formname, user_id, project_id,
                    addfavuser, delfavuser, defer=False, **kwargs ) :
        """add / remove project favourite""" 
        from zeta.config.environment import projcomp

        if addfavuser and project_id :
            projcomp.addfavorites( int(project_id), addfavuser, c=c, defer=defer)
        elif delfavuser and project_id :
            projcomp.delfavorites( int(project_id), delfavuser, c=c, defer=defer)

class FormProjectDisable( FormProjects ) : # disable_project, enable_project
    """Form component to update project disable status"""
    formname = [ 'prjdis', 'prjenb' ]
    postparams = ( [], [ 'user_id' ] )
    postparamsall = ( [], [ 'disable_project', 'enable_project' ] )

    def submitform( self, request, c, user_id, disable_projects,
                    enable_projects, defer=False, **kwargs ) :
        """update project disable status"""
        from zeta.config.environment import projcomp

        [ projcomp.config_project( projectname, disable=True, c=c, defer=defer) 
          for projectname in disable_projects ]
        [ projcomp.config_project( projectname, disable=False, c=c, defer=defer)
          for projectname in enable_projects ]

class FormProjectExpose( FormProjects ) : # expose_project, private_project
    """Form component to update project expose status"""
    formname = [ 'prjexp', 'prjprv' ]
    postparams = ( [], [ 'user_id' ] )
    postparamsall = ( [], [ 'expose_project', 'private_project' ] )

    def submitform( self, request, c, user_id, expprojects, prvprojects,
                    defer=False, **kwargs ) :
        """update project expose status"""
        from zeta.config.environment import projcomp

        [ projcomp.config_project( projectname, expose=True, c=c, defer=defer) 
          for projectname in expprojects ]
        [ projcomp.config_project( projectname, expose=False, c=c, defer=defer) 
          for projectname in prvprojects ]

class FormProjectLogo( FormProjects ) :
    """Form component to update / remove project logo"""
    formname = [ 'addprjlogo', 'delprjlogo' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'attachfile' ] )

    def submitform( self, request, c, formname, user_id, project_id, attachfile,
                    defer=False, **kwargs ) :
        """update / remove project logo"""
        from zeta.config.environment import projcomp, attcomp

        user = kwargs.get( 'user', None )

        if attachfile != None and project_id and user :
            logo = attcomp.create_attach( attachfile.filename, 
                                          fdfile=attachfile.file, 
                                          uploader=user
                                        )
            projcomp.config_project( int(project_id), logo=logo, c=c, defer=defer)

        elif formname == 'delprjlogo'  and project_id :
            projcomp.config_project( int(project_id), logo=None, c=c, defer=defer)

        else :
            raise ZetaFormError( 'In-sufficient detail, project-id and attachfile')

class FormProjectIcon( FormProjects ) :
    """Form component to update / remove project icon"""
    formname = [ 'addprjicon', 'delprjicon' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'attachfile' ] )

    def submitform( self, request, c, formname, user_id, project_id, attachfile,
                    defer=False, **kwargs ) :
        """update / remove project icon"""
        from zeta.config.environment import projcomp, attcomp

        user = kwargs.get( 'user', None )

        if attachfile != None and project_id and user :
            icon = attcomp.create_attach( attachfile.filename, 
                                          fdfile=attachfile.file, 
                                          uploader=user
                                        )
            projcomp.config_project( int(project_id), icon=icon, c=c, defer=defer)

        elif formname =='delprjicon' and project_id :
            projcomp.config_project( int(project_id), icon=None, c=c, defer=defer)

        else :
            raise ZetaFormError( 'In-sufficient detail, project-id and attachfile')

class FormProjectMailinglist( FormProjects ) :
    """Form component to add / remove project mailinglist"""
    formname = 'prjml'
    postparams = ( [], [ 'user_id', 'project_id', ('mailinglists', '') ] )

    def submitform( self, request, c, user_id, project_id, mailinglists,
                    defer=False, **kwargs ) :
        """add / remove project mailinglist"""
        from zeta.config.environment import projcomp

        mailinglists = mailinglists and mailinglists.split(',')
        mailinglists = [ m for m in [ m.strip(' ') for m in mailinglists ] if m ]
        appendml = kwargs.get( 'appendml', False )
        p = kwargs.get( 'project', None )

        project = None
        if project_id :
            project_id = int(project_id)
            project = (p and (p.id == project_id) and p) or project_id

        if filter( lambda ml : bool(ml), mailinglists ) :
            projcomp.set_mailinglists( project, mailinglists, append=appendml,
                                       c=c, defer=defer )

        else :
            projcomp.set_mailinglists( project, mailinglists=None,
                                       c=c, defer=defer )

class FormProjectIRCchannels( FormProjects ) :
    """Form component to add / remove project IRCChannels"""
    formname = 'prjirc'
    postparams = ( [], [ 'user_id', 'project_id', ('ircchannels', '') ] )

    def submitform( self, request, c, user_id, project_id, ircchannels, 
                    defer=False, **kwargs ) :
        """add / remove project IRCChannels"""
        from zeta.config.environment import projcomp

        ircchannels = ircchannels and ircchannels.split(',')
        ircchannels = [ i for i in [ i.strip(' ') for i in ircchannels ] if i ]
        appendirc = kwargs.get( 'appendirc', False )
        p = kwargs.get( 'project', None )

        project = None
        if project_id :
            project_id = int(project_id)
            project = (p and (p.id == project_id) and p) or project_id

        if filter( lambda irc : bool(irc), ircchannels ) :
            projcomp.set_ircchannels( project, ircchannels, append=appendirc,
                                      c=c, defer=defer )
        else :
            projcomp.set_ircchannels( project, ircchannels=None,
                                      c=c, defer=defer )

class FormProjectCreateComponent( FormProjects ) :
    """Form component to create / update project components"""
    formname = [ 'createpcomp', 'updatepcomp' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'component_id', 'componentname',
          'description', 'owner' ]
    )

    def submitform( self, request, c, user_id, project_id, component_id, 
                    componentname, description, owner, defer=False, **kwargs ) :
        """create / update project components"""
        from zeta.config.environment import projcomp

        errmsg = ''
        errmsg += ( not componentname and 'componentname, ' ) or ''
        errmsg += ( not description and  'description, ' ) or ''
        errmsg += ( not owner and  'owner, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )

        h.validate_fields( request )

        compdetail = [ None, componentname, description, owner ]
        if component_id :
            compdetail[0] = int(component_id)
            projcomp.create_component(
                int(project_id), compdetail, update=True, c=c, defer=defer
            )

        else :
            c = projcomp.create_component(
                    int(project_id), compdetail, c=c, defer=defer
                )

class FormProjectComponentOwner( FormProjects ) :
    """Form component to update / remove component owner"""
    formname = 'pcompowner'
    postparams = ( [], [ 'user_id', 'project_id', 'component_id', 'owner' ] )

    def submitform( self, request, c, user_id, project_id, component_id, owner,
                    defer=False, **kwargs ) :
        """update /remove component owner"""
        from zeta.config.environment import projcomp

        comp = projcomp.get_component( int(component_id) )
        if comp and owner :
            compdetail = [ comp.id, comp.componentname, comp.description,
                           owner ]
            projcomp.create_component(
                    int(project_id), compdetail, update=True, c=c, defer=defer )

class FormProjectRemoveComponent( FormProjects ) : # component_id
    """Form component to remove project components"""
    formname = 'rmpcomp'
    postparams = ( [], [ 'user_id', 'project_id' ] )
    postparamsall = ( [], [ 'component_id' ] )

    def submitform( self, request, c, user_id, project_id, component_ids,
                    defer=False, **kwargs ) :
        """remove project components"""
        from zeta.config.environment import projcomp

        [ projcomp.remove_component(
                int(project_id), int(component_id), c=c, defer=defer
          ) for component_id in component_ids ]

class FormProjectCreateMilestone( FormProjects ) :
    """Form component to create / update project milestones"""
    formname = [ 'createmstn', 'updatemstn' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'milestone_id', 'milestone_name',
          'description', 'due_date' ]
    )

    def submitform( self, request, c, user_id, project_id, milestone_id,
                    milestone_name, description, due_date,
                    defer=False, **kwargs ) :
        """create / update project milestones,
        due_date is expect in UTC."""
        from zeta.config.environment import userscomp, projcomp

        errmsg = ''
        errmsg += ( not milestone_name and 'milestone_name, ' ) or ''
        errmsg += ( not description and  'description, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )

        h.validate_fields( request )

        if due_date :
            usertz = timezone( userscomp.get_user( int(user_id) ).timezone )
            due_date = h.usertz_2_utc(
                            dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                            usertz
                       )

        mstndetail = [ None, milestone_name, description, due_date ]
        if milestone_id :
            mstndetail[0] = int(milestone_id)
            projcomp.create_milestone(
                int(project_id), mstndetail, update=True, c=c, defer=defer
            )

        else :
            m = projcomp.create_milestone(
                    int(project_id), mstndetail, c=c, defer=defer )

class FormProjectMilestoneDuedate( FormProjects ) :
    """Form component to update milestone due_date
        due_date is expect in UTC."""
    formname = 'mstnduedate'
    postparams = ( [], [ 'user_id', 'project_id', 'milestone_id', 'due_date' ])

    def submitform( self, request, c, user_id, project_id, milestone_id,
                    due_date, defer=False, **kwargs ) :
        """update milestone duedate"""
        from zeta.config.environment import userscomp, projcomp

        m = projcomp.get_milestone( int(milestone_id) )
        if due_date :
            usertz   = timezone( userscomp.get_user( int(user_id) ).timezone )
            due_date = h.usertz_2_utc(
                            dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                            usertz
                       )

        if m and due_date :
            mstndetail = [ m.id, m.milestone_name, m.description, due_date ]
            projcomp.create_milestone(
                int(project_id), mstndetail, update=True, c=c, defer=defer )

class FormProjectCloseMilestone( FormProjects ) :
    """Form component to close milestone"""
    formname = 'mstnclose'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'milestone_id', 'closing_remark', 'status' ]
    )

    def submitform( self, request, c, user_id, project_id, milestone_id,
                    closing_remark, status, defer=False, **kwargs ) :
        """close milestone"""
        from zeta.config.environment import projcomp

        errmsg = ''
        errmsg += ( status not in ['open', 'completed', 'cancelled'] \
                    and status ) or ''
        errmsg += ( (status in ['completed', 'cancelled']) and \
                    (not closing_remark) and 'closing_remark, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )
        
        m = projcomp.get_milestone( int(milestone_id) )
        if m and (m.completed or m.cancelled) and (status == 'open') :
            projcomp.open_milestone(m, closing_remark, c=c, defer=defer)
        elif m and closing_remark and status :
            projcomp.close_milestone(
                m, closing_remark, status, c=c, defer=defer )
        
class FormProjectRemoveMilestone( FormProjects ) : # milestone_id
    """Form component to remove project milestones"""
    formname = 'rmmstn'
    postparams = ( [], [ 'user_id', 'project_id' ] )
    postparamsall = ( [], [ 'milestone_id' ] )

    def submitform( self, request, c, user_id, project_id, milestone_ids,
                    defer=False, **kwargs ) :
        """remove project milestones"""
        from zeta.config.environment import projcomp

        [ projcomp.remove_milestone(
                int(project_id), int(milestone_id), c=c, defer=defer
          ) for milestone_id in milestone_ids ]

class FormProjectCreateVersion( FormProjects ) :
    """Form component to create / update project versions"""
    formname = [ 'createver', 'updatever' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'version_id', 'version_name', 'description' ]
    )

    def submitform( self, request, c, user_id, project_id, version_id,
                    version_name, description, defer=False, **kwargs ) :
        """create / update project versions"""
        from zeta.config.environment import projcomp

        errmsg = ''
        errmsg += ( not version_name and 'version_name, ' ) or ''
        errmsg += ( not description and  'description, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        verdetail = [ None, version_name, description ]
        if version_id and project_id :
            verdetail[0] = int(version_id)
            projcomp.create_version(
                int(project_id), verdetail, update=True, c=c, defer=defer )

        elif project_id :
            v = projcomp.create_version(
                    int(project_id), verdetail, c=c, defer=defer )

class FormProjectRemoveVersion( FormProjects ) : # version_id
    """Form component to remove project versions"""
    formname = 'rmver'
    postparams = ( [], [ 'user_id', 'project_id' ])
    postparamsall = ( [], [ 'version_id' ] )

    def submitform( self, request, c, user_id, project_id, version_ids,
                    defer=False, **kwargs ) :
        """remove project versions"""
        from zeta.config.environment import projcomp

        [ projcomp.remove_version(
                int(project_id), int(version_id), c=c, defer=defer
          ) for version_id in version_ids ]

class FormProjectTags( FormProjects ) :
    """Form component to add / remove project tags"""
    formname = [ 'addprjtags', 'delprjtags' ]
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'project_id', 'component_id', 'milestone_id',
          'version_id', ('tags', '') ]
    )

    def submitform( self, request, c, formname, user_id, project_id, component_id,
            milestone_id, version_id, tags, defer=False, **kwargs ) :
        """add / remove project tags"""
        from zeta.config.environment import projcomp

        tagnames = list(set( h.parse_csv(tags) ))
         
        entity = ( component_id and 'component' ) or \
                 ( milestone_id and 'milestone' ) or \
                 ( version_id and 'version' ) or \
                 None
        id = component_id and int(component_id) or \
             milestone_id and int(milestone_id) or \
             version_id and int(version_id) or \
             int(project_id)

        if project_id and id and formname == 'addprjtags' :
            obj = (( entity == 'component' ) and projcomp.get_component( id )) or\
                  (( entity == 'milestone' ) and projcomp.get_milestone( id )) or\
                  (( entity == 'version' ) and projcomp.get_version( id )) or\
                  projcomp.get_project( id )
            projcomp.add_tags(
                    int(project_id), entity, id, tagnames, c=c, defer=defer )

        if project_id and id and formname == 'delprjtags' :
            obj = (( entity == 'component' ) and projcomp.get_component( id )) or\
                  (( entity == 'milestone' ) and projcomp.get_milestone( id )) or\
                  (( entity == 'version' ) and projcomp.get_version( id )) or\
                  projcomp.get_project( id )
            projcomp.remove_tags(
                    int(project_id), entity, id, tagnames, c=c, defer=defer )

class FormProjectAttachs( FormProjects ) : # attach_id, attachfile
    """Form component to add / remove project attachments"""
    formname = [ 'addprjattachs', 'delprjattachs' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id' ])
    postparamsall = ( [], [ 'attach_id', 'attachfile' ] )

    def submitform( self, request, c, formname, user_id, project_id,
                    attach_ids, attachfiles, defer=False, **kwargs ) :
        """add / remove project attachments"""
        from zeta.config.environment import projcomp, attcomp

        user = kwargs.get( 'user', None )

        if project_id and formname == 'delprjattachs' :
            [ projcomp.remove_attach(
                int(project_id), int(attach_id), c=c, defer=defer
              ) for attach_id in attach_ids ]

        elif project_id and formname == 'addprjattachs' and user :
            for attachfile in  attachfiles :
                a = attcomp.create_attach( attachfile.filename, 
                                           fdfile=attachfile.file, 
                                           uploader=user
                                         )
                projcomp.add_attach( int(project_id), a, c=c, defer=defer )

class FormProjectTeam( FormProjects ) : # project_team_id, projuser
    """Form component to add / remove project-teams"""
    formname = [ 'addprjteam', 'delprjteam' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'team_type' ])
    postparamsall = ( [], [ 'project_team_id', 'projuser' ] )

    def submitform( self, request, c, formname, user_id, project_id, team_type,
                    project_team_ids, projusers, defer=False, **kwargs ) :
        """add / remove project-teams"""
        from zeta.config.environment import projcomp

        if formname == 'delprjteam' :
            project_team_ids = [ int(id) for id in project_team_ids ]
            projcomp.remove_project_users(
                project_team_ids, c=c, defer=defer )

        else :
            projcomp.add_project_user(
                    int(project_id), team_type, projusers, c=c, defer=defer )
            # TODO : Should we approve the user addition ?

class FormProjectTeamPermissions( FormProjects ) : # projectteam_perm_id, perm_group
    """Form component to add /remove project-team permissions"""
    formname = [ 'addteamperms', 'delteamperms' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'team_type' ])
    postparamsall = ( [], [ 'projectteam_perm_id', 'perm_group' ] )

    def submitform( self, request, c, formname, user_id, project_id, team_type,
                    projectteam_perm_ids, perm_groups, defer=False, **kwargs ) :
        """add / remove project-team permissions"""
        from zeta.config.environment import projcomp

        if formname == 'delteamperms' :
            projectteam_perm_ids = [ int(id) for id in projectteam_perm_ids ]
            projcomp.remove_projectteam_perm(
                projectteam_perm_ids, c=c, defer=defer )

        else :
            projcomp.add_projectteam_perm(
                int(project_id), team_type, perm_groups, c=c, defer=defer )

class FormProjectPermission( FormProjects ) : # project_perm_id, perm_group
    """Form component to add /remove project-user permissions"""
    formname = [ 'addprjperms', 'delprjperms' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'projuser' ])
    postparamsall = ( [], [ 'project_perm_id', 'perm_group' ] )

    def submitform( self, request, c, formname, user_id, project_id, projuser,
                    project_perm_ids, perm_groups, defer=False, **kwargs ) :
        """add / remove project-user permissions"""
        from zeta.config.environment import projcomp

        if formname == 'delprjperms' :
            project_perm_ids = [ int(id) for id in project_perm_ids ]
            projcomp.remove_project_permission(
                    project_perm_ids, c=c, defer=defer )

        else :
            [ projcomp.add_project_permission(
                    int(project_id), projuser, perm_group, c=c, defer=defer
              ) for perm_group in perm_groups ]

# -------------------- Ticket Forms --------------------------------

class FormTickets( Component ) :
    """Form component to create / update / delete ticket tables"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for ticket forms"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete entries in ticket tables"""
        pass

class FormCreateTicket( FormTickets ) : # milestone_id, component_id, version_id
    """Form component to create / update tickets"""
    formname = 'createtck'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'ticket_id', 'summary', 'description',
          'tck_typename', 'tck_severityname', 'promptuser', 'parent_id',
          ('blocking_ids', ''), ('blockedby_ids', ''), ('tags', '') ]
    )
    postparamsall = ( [], [ 'component_id', 'milestone_id', 'version_id' ] )

    def submitform( self, request, c, user_id, project_id, ticket_id, summary,
                    description, tck_typename, tck_severityname, promptuser,
                    parent_id, blocking_ids, blockedby_ids, tags, component_ids,
                    milestone_ids, version_ids, defer=False, **kwargs ) :
        """create / update ticket table"""
        from zeta.config.environment import tckcomp

        component_ids = component_ids or None
        milestone_ids = milestone_ids or None
        version_ids = version_ids or None
        blocking_ids = blocking_ids and \
                       [ i.strip(' ') for i in blocking_ids.split(',') ]
        blocking_ids = filter(None, blocking_ids) if blocking_ids else []
        blockedby_ids = blockedby_ids and \
                        [ i.strip(' ') for i in blockedby_ids.split(',') ]
        blockedby_ids = filter(None, blockedby_ids) if blockedby_ids else []
        tagnames = list(set( h.parse_csv(tags) ))
        append = kwargs.get( 'append', False )

        errmsg = ''
        errmsg += ( not summary and 'summary, ' )  or ''
        errmsg += ( not tck_typename and  'tck_typename, ' ) or ''
        errmsg += ( not tck_severityname and  'tck_severityname, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        tckdetail        = [ None, summary, description, tck_typename,
                             tck_severityname ]
        promptuser       = promptuser or int(user_id)
        if ticket_id :
            ticket_id    = int(ticket_id)
            tckdetail[0] = ticket_id
            tckcomp.create_ticket( int(project_id), tckdetail, promptuser,
                                   update=True, c=c, defer=defer )

        else :
            owner = int(user_id)
            t = tckcomp.create_ticket(
                    int(project_id), tckdetail, promptuser, owner,
                    c=c, defer=defer, index=False
                )
            ticket_id = t.id
            if tagnames :
                tckcomp.add_tags( t, tagnames )

        tckcomp.config_ticket(
                ticket_id,
                parent=parent_id and int(parent_id) or None,
                components=component_ids and [ int(id) for id in component_ids if id ],
                milestones=milestone_ids and [ int(id) for id in milestone_ids if id ],
                versions=version_ids and [ int(id) for id in version_ids if id ],
                blocking=[ int(id) for id in blocking_ids if id ],
                blockedby=[ int(id) for id in blockedby_ids if id ],
                append=append, c=c, defer=defer
        )


class FormTicketConfig( FormTickets ) : # component_id, milestone_id, version_id
    """Form component to update ticket config"""
    formname = [ 'configtck', 'tcktype', 'tckseverity', 'tckpromptuser',
                 'tckcomponent', 'tckmilestone', 'tckversion', 'tckparent',
                 'tckblockedby', 'tckblocking', 'tcksummary', 'tckdescription' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'ticket_id', 'summary', 'description',
          'tck_typename', 'tck_severityname', 'promptuser', 'parent_id',
          'blocking_ids', 'blockedby_ids' ]
    )
    postparamsall = ( [], [ 'component_id', 'milestone_id', 'version_id' ] )

    def submitform( self, request, c, user_id, project_id, ticket_id, summary,
                    description, tck_typename, tck_severityname, promptuser,
                    parent_id, blocking_ids, blockedby_ids, component_ids,
                    milestone_ids, version_ids, defer=False, **kwargs ) :
        """update ticket config"""
        from zeta.config.environment import tckcomp

        append = kwargs.get( 'append', False )

        tck_typename = tck_typename or None
        tck_severityname = tck_severityname or None
        promptuser = promptuser or None
        component_ids = component_ids or None
        milestone_ids = milestone_ids or None
        version_ids = version_ids or None

        try : # To handle invalid blocking_ids string
            if isinstance( blocking_ids, (str, unicode) ) :
                ids          = blocking_ids.split(',')
                blocking_ids = [ int(id) for id in [ id.strip(' ') for id in ids ] if id ]
        except :
            blocking_ids = None

        try : # To handle invalid blockedby_ids string
            if isinstance( blockedby_ids, (str, unicode) ) :
                ids           = blockedby_ids.split(',')
                blockedby_ids = [ int(id) for id in [ id.strip(' ') for id in ids ] if id ]
        except :
            blockedby_ids = None

        try : # To handle invalid parent_id string
            parent_id = parent_id and int(parent_id)
        except :
            parent_id = None

        if ticket_id :
            tckcomp.config_ticket(
                int(ticket_id),
                type        = tck_typename,
                severity    = tck_severityname,
                promptuser  = promptuser,
                parent      = parent_id,
                components  = component_ids and \
                              [ int(id) for id in component_ids if id ],
                milestones  = milestone_ids and \
                              [ int(id) for id in milestone_ids if id ],
                versions    = version_ids and \
                              [ int(id) for id in version_ids if id ],
                blocking    = blocking_ids,
                blockedby   = blockedby_ids,
                append=append, c=c, defer=defer
            )

        if project_id and ticket_id and (summary !=None or description != None) :
            t          = tckcomp.get_ticket( int(ticket_id) )
            summary    = summary or t.summary
            ticket_id  = int( ticket_id )
            project_id = int( project_id )
            tckdetail  = [ t.id, summary, description, t.type, t.severity ]
            tckcomp.create_ticket( 
                    project_id, tckdetail, t.promptuser, c=c, defer=defer,
                    update=True
            )

class FormTicketFavorite( FormTickets ) :
    """Form component to add or remove a ticket being a user's favourite"""
    formname = 'tckfav'
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'project_id', 'ticket_id', 'addfavuser', 'delfavuser' ]
    )

    def submitform( self, request, c, formname, user_id, project_id, ticket_id,
                    addfavuser, delfavuser, defer=False, **kwargs ) :
        """add / remove ticket favourite"""
        from zeta.config.environment import tckcomp

        if addfavuser and ticket_id :
            tckcomp.addfavorites( int(ticket_id), addfavuser, c=c, defer=defer )
        if delfavuser and ticket_id :
            tckcomp.delfavorites( int(ticket_id), delfavuser, c=c, defer=defer )

class FormTicketVote( FormTickets ) :
    """Form component to vote for/against ticket"""
    formname = 'votetck'
    postparams = ( [], [ 'user_id', 'project_id', 'ticket_id', 'votedas' ] )
    
    def submitform( self, request, c, user_id, project_id, ticket_id, votedas,
                    defer=False, **kwargs ) :
        """vote ticket"""
        from zeta.config.environment import tckcomp

        if votedas == 'up' :
            tckcomp.voteup( int(ticket_id), int(user_id), c=c, defer=defer )
        elif votedas == 'down' :
            tckcomp.votedown( int(ticket_id), int(user_id), c=c, defer=defer )


class FormCreateTicketStatus( FormTickets ) :
    """Form component to create / update ticket status"""
    formname = 'createtstat'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'ticket_id', 'ticket_status_id',
          'tck_statusname', 'due_date', 'owner' ]
    )
    
    def submitform( self, request, c, user_id, project_id, ticket_id,
                    ticket_status_id, tck_statusname, due_date, owner,
                    defer=False, **kwargs ) :
        """create / update ticket status"""
        from zeta.config.environment import userscomp, tckcomp

        errmsg = ''
        errmsg += ( not tck_statusname and 'tck_statusname, ' )  or ''
        errmsg += ( not owner and 'owner, ' )  or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        if due_date :
            usertz   = timezone( userscomp.get_user( int(user_id) ).timezone )
            due_date = h.usertz_2_utc(
                            dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                            usertz
                       )

        tckstatdetail = [ None, tck_statusname, due_date ]
        ticket_id     = int( ticket_id )
        if ticket_id :
            owner = int(owner)
            t     = tckcomp.get_ticket( ticket_id )
            ts    = tckcomp.get_ticket_status( t.tsh_id, attrload=['status'] )

            if ticket_status_id :
                # Update the status and due_date for current tsh
                tckstatdetail[0] = int(ticket_status_id)
                tckcomp.create_ticket_status(
                        ticket_id, tckstatdetail, owner,
                       update=True, c=c, defer=defer
                )

            elif (ts.status.tck_statusname == tck_statusname) and due_date !=None :
                # Just change the due_date for current tsh
                tckstatdetail[0] = ts.id
                tckcomp.create_ticket_status(
                        ticket_id, tckstatdetail, owner,
                        update=True, c=c, defer=defer
                )

            elif tck_statusname :
                # New status
                ts = tckcomp.create_ticket_status(
                        ticket_id, tckstatdetail, owner, c=c, defer=defer )

class FormTicketStatusConfig( FormTickets ) :
    """Form component to update ticket-status config"""
    formname = [ 'configtstat', 'tststatus', 'tstduedate' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'ticket_id', 'ticket_status_id',
          'tck_statusname', 'due_date', 'owner' ]
    )
    
    def submitform( self, request, c, user_id, project_id, ticket_id,
                    ticket_status_id, tck_statusname, due_date, owner,
                    defer=False, **kwargs ) :
        """update ticket-status config"""
        from zeta.config.environment import userscomp, tckcomp

        tck_statusname = tck_statusname or None
        owner = owner and int(owner)
        
        if due_date :
            usertz   = timezone( userscomp.get_user( int(user_id) ).timezone )
            due_date = h.usertz_2_utc( 
                            dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                            usertz
                       )

        if ticket_id and ticket_status_id :
            ts = tckcomp.get_ticket_status( int(ticket_status_id) )
            tckstatdetail = [ ts.id, tck_statusname or ts.status, due_date ]
            tckcomp.create_ticket_status(
                    int(ticket_id), tckstatdetail, owner or ts.owner, 
                    update=True, c=c, defer=defer
            )

class FormCreateTicketComment( FormTickets ) :
    """Form component to create / update ticket-comment"""
    formname = [ 'createtcmt', 'replytcmt', 'updatetcmt' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'ticket_id', 'ticket_comment_id', 'text',
          'commentby', 'replytocomment_id' ]
    )
    
    def submitform( self, request, c, user_id, project_id, ticket_id,
                    ticket_comment_id, text, commentby, replytocomment_id,
                    defer=False, **kwargs ) :
        """create / update ticket-comment"""
        from zeta.config.environment import tckcomp

        errmsg = ''
        errmsg += ( not text and 'text, ' )  or ''
        errmsg += ( not commentby and 'commentby, ' )  or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        tckcomment = [ None, text, commentby ]
        if ticket_id and ticket_comment_id :
            ticket_comment_id = int(ticket_comment_id)
            tckcomment[0] = ticket_comment_id
            tckcomp.create_ticket_comment(
                    int(ticket_id), tckcomment, update=True, c=c, defer=defer
            )

        elif ticket_id :
            tc = tckcomp.create_ticket_comment(
                    int(ticket_id), tckcomment, c=c, defer=defer
            )
            ticket_comment_id = tc.id

        replytocomment_id = replytocomment_id and int(replytocomment_id)
        if ticket_comment_id and replytocomment_id :
            tckcomp.comment_reply( ticket_comment_id, replytocomment_id )

class FormTicketFilter( FormTickets ) :
    """Form component to add /remove ticket filters"""
    formname = [ 'addtckfilter', 'deltckfilter' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'name', 'filterbyjson', 'tf_id' ])
    
    def submitform( self, request, c, formname, user_id, name, filterbyjson,
                    tf_id, defer=False, **kwargs ) :
        """add / remove ticket filters"""
        from zeta.config.environment import tckcomp

        userid = int(user_id)
        if name and filterbyjson and (formname == 'addtckfilter') :
            tckcomp.create_ticketfilter(
                    name=name, filterbyjson=filterbyjson,
                    foruser=userid, c=c, defer=defer, byuser=userid
            )

        if formname == 'deltckfilter' :
            tckcomp.del_ticketfilter(
                    tfs=[ int(tf_id) ], c=c, defer=defer, byuser=userid
            )

class FormTicketTags( FormTickets ) :
    """Form component to add / remove tags"""
    formname = [ 'addtcktags', 'deltcktags' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'ticket_id', ('tags', '') ])
    
    def submitform( self, request, c, formname, user_id, project_id, ticket_id,
                    tags, defer=False, **kwargs ) :
        """add / remove ticket tags"""
        from zeta.config.environment import tckcomp

        tagnames = list(set( h.parse_csv(tags) ))

        if ticket_id and formname == 'addtcktags' :
            t = tckcomp.get_ticket( int(ticket_id) )
            tckcomp.add_tags( t, tagnames, c=c, defer=defer )

        if ticket_id and formname == 'deltcktags' :
            t = tckcomp.get_ticket( int(ticket_id) )
            tckcomp.remove_tags( t, tagnames, c=c, defer=defer  )

class FormTicketAttachs( FormTickets ) : # attach_id, attachfile
    """Form component to add / remove attachments"""
    formname = [ 'addtckattachs', 'deltckattachs' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'ticket_id' ])
    postparamsall = ( [], [ 'attach_id', 'attachfile' ] )
    
    def submitform( self, request, c, formname, user_id, project_id, ticket_id,
                    attach_ids, attachfiles, defer=False, **kwargs ) :
        """add / remove ticket attachments"""
        from zeta.config.environment import tckcomp, attcomp

        user = kwargs.get( 'user', None )

        if ticket_id and formname == 'deltckattachs' :
            [ tckcomp.remove_attach(
                    int(ticket_id), int(attach_id), c=c, defer=defer
              ) for attach_id in attach_ids ]

        elif ticket_id and formname == 'addtckattachs' and user :
            for attachfile in  attachfiles :
                a = attcomp.create_attach( attachfile.filename, 
                                           fdfile=attachfile.file, 
                                           uploader=user
                                         )
                tckcomp.add_attach( int(ticket_id), a, c=c, defer=defer )


# --------------------- Review Forms -------------------------------

class FormReviews( Component ) :
    """Form component to create / update / delete review tables"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for review forms"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete entries in review tables"""
        pass

class FormReviewSet( FormReviews ) : # review_id
    """Form component to create / update review set"""
    formname = [ 'createrset', 'updaterset', 'addtorset', 'delfromrset' ]
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'project_id', 'rset_id', 'name' ]
    )
    postparamsall = ( [], [ 'review_id' ] )

    def submitform( self, request, c, formname, user_id, project_id,
                    rset_id, name, review_id, defer=False, **kwargs ) :
        """create / update review sets. Add / remove review in review set"""
        from zeta.config.environment import revcomp, projcomp

        if formname in [ 'createrset', 'updaterset' ] :
            if name and rset_id :
                rset = revcomp.get_reviewset( int(rset_id) )
                rset and revcomp.update_reviewset(rset, name, c=c, defer=defer)

            elif name and project_id :
                proj = projcomp.get_project( int(project_id) )
                proj and revcomp.create_reviewset(proj, name, c=c, defer=defer)

        elif formname == 'addtorset' and review_id and rset_id :
            review = revcomp.get_review( int(review_id[0]) )
            rset   = revcomp.get_reviewset( int(rset_id) )
            revcomp.add_reviewtoset( rset, review, c=c, defer=defer )

        elif formname == 'delfromrset' and review_id and rset_id :
            review = revcomp.get_review( int(review_id[0]) )
            rset   = revcomp.get_reviewset( int(rset_id) )
            review.reviewset == rset and revcomp.remove_reviewfromset(
                                            review, c=c, defer=defer )

class FormCreateReview( FormReviews ) : # review_id, resource_url, participant
    """Form component to create / update review"""
    formname = [ 'createrev', 'configrev', 'revwauthor', 'revwmoderator' ]
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'project_id', 'version', 'author', 'moderator', 'rset_id' ]
    )
    postparamsall = ( [], [ 'review_id', 'resource_url', 'participant' ] )

    def submitform( self, request, c, formname, user_id, project_id, version,
                    author, moderator, rset_id, review_ids, resource_urls,
                    participants, defer=False, **kwargs ) :
        """create / update review"""
        from zeta.config.environment import revcomp, projcomp

        version = int(version) if version != None else None
        append = kwargs.get( 'append', True )

        if formname == 'createrev' :
            errmsg       = ''
            errmsg       += ( not resource_urls and 'resource_url, ' )  or ''
            errmsg       += ( (version == None) and  'version, ' ) or ''
            errmsg       += ( not author and 'author, ' )  or ''
            errmsg       += ( not moderator and  'moderator, ' ) or ''
            if errmsg : 
                errmsg = 'Check ' + errmsg  + '!!'
                raise ZetaFormError( errmsg )
            h.validate_fields( request )

        rset = rset_id and revcomp.get_reviewset( int(rset_id) )

        if project_id and len(review_ids) == 1 and len(resource_urls) == 1 :
            p = projcomp.get_project( int(project_id) )
            revdetail = [ int(review_ids[0]), resource_urls[0], version, author,
                          moderator ]
            r = revcomp.create_review(p, revdetail, update=True, c=c, defer=defer)
            participants and revcomp.set_participants(
                                    int(review_ids[0]), participants,
                                    append=append, c=c, defer=defer
                             )
            r and rset and revcomp.add_reviewtoset( rset, r, c=c, defer=defer )
            
        elif project_id and review_ids :
            p = projcomp.get_project( int(project_id) )
            for rid in review_ids :
                revdetail = [ int(rid), None, version, author, moderator ]
                r = revcomp.create_review( p, revdetail,
                                           update=True, c=c, defer=defer )
                participants and revcomp.set_participants(
                                    int(rid), participants,
                                    append=append, c=c, defer=defer
                                 )
                r and rset and revcomp.add_reviewtoset(
                                    rset, r, c=c, defer=defer )

        elif project_id and resource_urls :
            p = projcomp.get_project( int(project_id) )
            for rurl in resource_urls :
                revdetail = [ None, rurl, version, author, moderator ]
                r = revcomp.create_review( p, revdetail, c=c, defer=defer )
                participants and revcomp.set_participants(
                                    r, participants,
                                    append=append, c=c, defer=defer
                                 )
                r and rset and revcomp.add_reviewtoset(
                                rset, r, c=c, defer=defer )

class FormReviewParticipants( FormReviews ) : # participant
    """Form component to update review"""
    formname = [ 'addparts', 'delparts' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'review_id' ] )
    postparamsall = ( [], [ 'participant' ] )

    def submitform( self, request, c, formname, user_id, project_id, review_id,
                    participants, defer=False, **kwargs ) :
        """update review"""
        from zeta.config.environment import revcomp

        append = kwargs.get( 'append', True )

        if review_id and participants :
            if formname == 'addparts' :
                revcomp.set_participants(
                        int(review_id), participants, append=append,
                        c=c, defer=defer
                )
            elif formname == 'delparts' :
                revcomp.set_participants(
                        int(review_id), participants,
                        remove=True, c=c, defer=defer
                )

class FormCloseReview( FormReviews ) :
    """Form component to close review"""
    formname = 'closerev'
    postparams = ( [], [ 'user_id', 'project_id', 'review_id', 'command' ] )

    def submitform( self, request, c, user_id, project_id, review_id, command,
                    defer=False, **kwargs ) :
        """close review"""
        from zeta.config.environment import revcomp

        if command == 'open' :
            close = False
            rc    = revcomp.close_review(
                            int(review_id), close=close, c=c, defer=defer )

        elif command == 'close' :
            close = True
            rc    = revcomp.close_review(
                            int(review_id), close=close, c=c, defer=defer )

        else :
            raise ZetaFormError( "Unknow 'closerev' command" )

        if rc != close :
            raise ZetaFormError( 'Cannot close review, check whether ' + \
                                 'all review comments are approved' )


class FormCreateReviewComment( FormReviews ) :
    """Form component to create / update review"""
    formname = [ 'creatercmt', 'replyrcmt' ]
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'project_id', 'review_id', 'review_comment_id',
          'position', 'text', 'reviewnature', 'commentby', 'replytocomment_id' ]
    )

    def submitform( self, request, c, formname, user_id, project_id, review_id,
                    review_comment_id, position, text, nature, commentby,
                    replytocomment_id, defer=False, **kwargs ) :
        """create / update review"""
        from zeta.config.environment import revcomp

        errmsg = ''
        errmsg += ( not text and 'text, ' )  or ''
        errmsg += ( not commentby and  'commentby, ' ) or ''
        errmsg += ( (formname == 'creatercmt') and not position and 'position, ') or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        revcomment = [ None, position, text, commentby, nature, None ]
        if review_id and review_comment_id :
            revcomment[0] = int(review_comment_id)
            revcomp.create_reviewcomment(
                    int(review_id), revcomment, update=True, c=c, defer=defer )

        elif review_id :
            rc = revcomp.create_reviewcomment(
                    int(review_id), revcomment, c=c, defer=defer )
            review_comment_id = rc.id

        replytocomment_id = replytocomment_id and int(replytocomment_id)
        if review_comment_id and replytocomment_id :
            revcomp.comment_reply( review_comment_id, replytocomment_id )

class FormProcessReviewComment( FormReviews ) :
    """Form component to approve review comment"""
    formname = 'processrcmt'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'review_id', 'review_comment_id', 'approve',
          'reviewnature', 'reviewaction' ]
    )

    def submitform( self, request, c, user_id, project_id, review_id,
                    review_comment_id, approve, reviewnature, reviewaction,
                    defer=False, **kwargs ) :
        """process (action/approve) review comment"""
        from zeta.config.environment import revcomp

        approve = asbool(approve)
        if review_comment_id :
            revcomp.process_reviewcomment( 
                        int(review_comment_id), reviewnature=reviewnature,
                        reviewaction=reviewaction, approve=approve,
                        c=c, defer=defer
            )

class FormReviewFavorite( FormReviews ) :
    """Form component to add or remove a review being a user's favourite"""
    formname = 'revwfav'
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [], [ 'user_id', 'project_id', 'review_id', 'addfavuser', 'delfavuser' ]
    )

    def submitform( self, request, c, formname, user_id, project_id,
                    review_id, addfavuser, delfavuser, defer=False, **kwargs ) :
        """add / remove review favourite"""
        from zeta.config.environment import revcomp

        if addfavuser and review_id :
            revcomp.addfavorites( int(review_id), addfavuser, c=c, defer=defer )
        if delfavuser and review_id :
            revcomp.delfavorites( int(review_id), delfavuser, c=c, defer=defer )

class FormReviewTags( FormReviews ) :
    """Form component to add / remove Review tags"""
    formname = [ 'addrevtags', 'delrevtags' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'review_id', ('tags', '') ] )

    def submitform( self, request, c, formname, user_id, review_id, tags, defer=False, **kwargs ) :
        """add / remove review tags"""
        from zeta.config.environment import revcomp

        tagnames   = list(set( h.parse_csv(tags) ))
        if review_id and formname == 'addrevtags' :
            revcomp.add_tags( int(review_id), tagnames, c=c, defer=defer )
        if review_id and formname == 'delrevtags' :
            revcomp.remove_tags( int(review_id), tagnames, c=c, defer=defer )

class FormReviewAttachs( FormReviews ) : # attach_id, attachfile
    """Form component to add / remove review attachments"""
    formname = [ 'addrevattachs', 'delrevattachs' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'review_id' ] )
    postparamsall = ( [], [ 'attach_id', 'attachfile' ] )

    def submitform( self, request, c, formname, user_id, review_id, 
                    attach_ids, attachfiles, defer=False, **kwargs ) :
        """add / remove review attachments"""
        from zeta.config.environment import revcomp, attcomp

        user = kwargs.get( 'user', None )

        if review_id and formname == 'delrevattachs' :
            [ revcomp.remove_attach(
                    int(review_id), int(attach_id), c=c, defer=defer
              ) for attach_id in attach_ids ]

        elif review_id and formname == 'addrevattachs'  and user :
            for attachfile in  attachfiles :
                a = attcomp.create_attach( attachfile.filename, 
                                           fdfile=attachfile.file, 
                                           uploader=user
                                         )
                revcomp.add_attach( int(review_id), a, c=c, defer=defer )


# --------------------- Vcs Forms -------------------------------

class FormVcs( Component ) :
    """Form component to create / update / delete vcs tables"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for vcs forms"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete entries in vcs tables"""
        pass

class FormIntegrateVcs( FormVcs ) :
    """Form component to integrate / update / delete vcs"""
    formname = 'integratevcs'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'vcs_typename', 'name', 'rooturl',
          'loginname', 'password' ]
    )

    def submitform( self, request, c, user_id, project_id, vcs_typename, name,
                    rooturl, loginname, password, defer=False, **kwargs ) :
        """integrate vcs"""
        from zeta.config.environment import vcscomp
        errmsg = ''
        errmsg += ( not name and  'repository name, ' ) or ''
        errmsg += ( not vcs_typename and 'repository type, ' )  or ''
        errmsg += ( not rooturl and 'root url, ' )  or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        if project_id :
            vcsdetail = ( vcs_typename, name, rooturl, loginname, password )
            v = vcscomp.integrate_vcs(
                    int(project_id), vcsdetail, c=c, defer=defer )

        else :
            raise ZetaFormError( 'Project not defined' )

class FormConfigVcs( FormVcs ) :
    """Form component to configure existing vcs entry"""
    formname = 'configvcs'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'vcs_id', 'vcs_typename', 'name', 'rooturl',
          'loginname', 'password' ]
    )

    def submitform( self, request, c, user_id, project_id, vcs_id,
                    vcs_typename, name, rooturl, loginname, password,
                    defer=False, **kwargs ) :
        """config vcs"""
        from zeta.config.environment import vcscomp

        if vcs_id :
            vcscomp.config_vcs(
                    int(vcs_id), name=name, type=vcs_typename, rooturl=rooturl,
                    loginname=loginname, password=password,
                    c=c, defer=defer
            )

class FormDeleteVcs( FormVcs ) :
    """Form component to delete vcs"""
    formname = [ 'deletevcs' ]
    postparams = ( [], [ 'user_id', 'project_id', 'vcs_id' ] )

    def submitform( self, request, c, user_id, project_id, vcs_id,
                    defer=False, **kwargs ) :
        """delete vcs"""
        from zeta.config.environment import vcscomp
        if project_id and vcs_id :
            vcscomp.delete_vcs( int( vcs_id ), c=c, defer=defer )


class FormCreateVcsmount( FormVcs ) :
    """Form component to create a repository mount"""
    formname = [ 'createmount' ]
    postparams = ( [], [ 'user_id', 'vcs_id', 'name', 'repospath', 'content' ] )

    def submitform( self, request, c, user_id, vcs_id, name, repospath, content,
                    defer=False, **kwargs ) :
        """Create repository mount"""
        from zeta.config.environment import vcscomp

        errmsg = ''
        errmsg += ( not vcs_id and  'vcs_id, ' ) or ''
        errmsg += ( not name and 'name, ' )  or ''
        errmsg += ( not repospath and 'repospath, ' )  or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )

        vcs_id = int(vcs_id)
        if user_id and vcs_id and name and repospath :
            if content :
                m = vcscomp.create_mount(
                            vcs_id, name, repospath, content, c=c, defer=defer )
            else :
                m = vcscomp.create_mount(
                            vcs_id, name, repospath, c=c, defer=defer )

class FormUpdateVcsmount( FormVcs ) :
    """Form component to update repository mount"""
    formname = [ 'updatemount' ]
    postparams = ( [], [ 'user_id', 'mount_id', 'name', 'repospath', 'content' ] )

    def submitform( self, request, c, user_id, mount_id, name, repospath, content,
                    defer=False, **kwargs ) :
        """Update repository mount"""
        from zeta.config.environment import vcscomp

        m = mount_id and vcscomp.get_mount( int(mount_id) )    
        kwargs = { 'c': c, 'defer': defer }
        name and kwargs.setdefault( 'name', name )
        repospath and kwargs.setdefault( 'repospath', repospath )
        content and kwargs.setdefault( 'content', content )
        m and vcscomp.update_mount( m, **kwargs )

class FormDeleteVcsmount( FormVcs ) :
    """Form component to delete repository mount"""
    formname = [ 'deletemount' ]
    postparams = ( [], [ 'user_id', 'mount_id' ] )

    def submitform( self, request, c, user_id, mount_id,
                    defer=False, **kwargs ) :
        """Delete repository mount"""
        from zeta.config.environment import vcscomp

        mount_id and vcscomp.delete_mount( int(mount_id), c=c, defer=defer )

# --------------------- Wiki Forms -------------------------------

class FormWikis( Component ) :
    """Form component to create / update / delete wiki tables"""

    def requestform( self, request, c, defer=False, **kwargs ) :
        """Populate context for wiki forms"""
        pass

    def submitform( self, request, c, defer=False, **kwargs ) :
        """Create / Update / Delete entries in wiki tables"""
        pass

class FormCreateWiki( FormWikis ) :
    """Form component to create wiki"""
    formname = 'createwiki'
    postparams = (
        [],
        [ 'user_id', 'project_id', 'wikiurl', 'wiki_typename', 'sourceurl',
          'creator' ]
    )

    def submitform( self, request, c, user_id, project_id, wikiurl,
                    wiki_typename, sourceurl, creator, defer=False, **kwargs ) :
        """create wiki"""
        from zeta.config.environment import wikicomp

        errmsg = ''
        errmsg += ( not wikiurl and  'wikiurl, ' ) or ''
        errmsg += ( not wiki_typename and 'wiki_typename, ' )  or ''
        errmsg += ( not creator and 'creator, ' )  or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        if wikicomp.get_wiki( wikiurl ) :
            raise ZetaFormError( 'wiki page with url `%s` already exists !!' )

        w = wikicomp.create_wiki(
                wikiurl, wiki_typename, sourceurl=sourceurl, creator=creator,
                c=c, defer=defer
            )
        project_id and wikicomp.config_wiki(
                                w, project=int(project_id), c=c, defer=defer )

class FormConfigWiki( FormWikis ) :
    """Form component to configure a wiki page"""
    formname = [ 'configwiki', 'wikitype', 'wikisummary', 'wikisourceurl' ]
    postparams = (
        [],
        [ 'user_id', 'project_id', 'wiki_id', 'wiki_typename', 'summary',
          'sourceurl' ]
    )

    def submitform( self, request, c, user_id, project_id, wiki_id,
                    wiki_typename, summary, sourceurl, defer=False, **kwargs ) :
        """configure a wiki page"""
        from zeta.config.environment import wikicomp

        append = kwargs.get( 'append', False )

        wiki_id = int(wiki_id)
        try :
            project_id = project_id and int(project_id)
        except :
            project_id = None

        wikicomp.config_wiki(
                wiki_id, project=project_id, wtype=wiki_typename,
                summary=summary, sourceurl=sourceurl, c=c, defer=defer
        )

class FormWikiFavorite( FormWikis ) :
    """Form component to add or remove a wiki being a user's favourite"""
    formname = 'wikifav'
    getparams = ( [], [ 'formname' ] )
    postparams = (
        [],
        [ 'user_id', 'project_id', 'wiki_id', 'addfavuser', 'delfavuser' ]
    )

    def submitform( self, request, c, formname, user_id, project_id, wiki_id,
                    addfavuser, delfavuser, defer=False, **kwargs ) :
        """add / remove wiki favourite"""
        from zeta.config.environment import wikicomp

        if addfavuser and wiki_id :
            wikicomp.addfavorites( int(wiki_id), addfavuser, c=c, defer=defer )
        if delfavuser and wiki_id :
            wikicomp.delfavorites( int(wiki_id), delfavuser, c=c, defer=defer )

class FormWikiVote( FormWikis ) :
    """Form component to vote for/against wiki"""
    formname = 'votewiki'
    postparams = ( [], [ 'user_id', 'project_id', 'wiki_id', 'votedas' ] )
    
    def submitform( self, request, c, user_id, project_id, wiki_id, votedas,
                    defer=False, **kwargs ) :
        """vote wiki"""
        from zeta.config.environment import wikicomp
        if votedas == 'up' :
            wikicomp.voteup( int(wiki_id), int(user_id), c=c, defer=defer )
        elif votedas == 'down' :
            wikicomp.votedown( int(wiki_id), int(user_id), c=c, defer=defer )

class FormWikiContent( FormWikis ) :
    """Form component to create / update wiki page content"""
    formname = 'wikicont'
    postparams = (
        [], [ 'user_id', 'wiki_id', 'text', 'author', 'version_id' ]
    )

    def submitform( self, request, c, user_id, wiki_id, text, author,
                    version_id, defer=False, **kwargs ) :
        """create / update wiki page content"""
        from zeta.config.environment import wikicomp

        errmsg = ''
        errmsg += ( not author and 'author, ' )  or ''
        if errmsg :
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        version_id  = version_id and int(version_id)
        if wiki_id :
            wikicomp.create_content(
                    int(wiki_id), author, text, version_id, c=c, defer=defer )

class FormRemoveWikiContent( FormWikis ) :
    """Form component to remove a wiki page version"""
    formname = 'rmwikicont'
    postparams = ( [], [ 'user_id', 'project_id', 'wiki_id', 'version_id' ] )

    def submitform( self, request, c, user_id, project_id, wiki_id, version_id,
                    defer=False, **kwargs ) :
        """remove a wiki page content"""
        from zeta.config.environment import wikicomp

        errmsg = ''
        errmsg += ( not version_id and  'version_id, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        if wiki_id :
            wikicomp.remove_content(
                    int(wiki_id), int(version_id), c=c, defer=defer )

class FormWikiRedirect( FormWikis ) :
    """Form component to redirect wiki page"""
    formname = 'wikiredir'
    postparams = ( [], [ 'user_id', 'project_id', 'wiki_id', 'wiki_target' ] )

    def submitform( self, request, c, user_id, project_id, wiki_id, wiki_target,
                    defer=False, **kwargs ) :
        """redirect wiki page"""
        from zeta.config.environment import wikicomp

        if wiki_id and wiki_target :
            wikicomp.wiki_redirect( int(wiki_id), int(wiki_target) )

class FormCreateWikiComment( FormWikis ) :
    """Form component to create / update wiki-comment"""
    formname = [ 'createwcmt', 'updatewcmt', 'replywcmt' ]
    postparams = (
        [],
        [ 'user_id', 'wiki_id', 'wiki_comment_id', 'version_id', 'text',
          'commentby', 'replytocomment_id' ]
    )
    
    def submitform( self, request, c, user_id, wiki_id, wiki_comment_id,
                    version_id, text, commentby, replytocomment_id,
                    defer=False, **kwargs ) :
        """create / update wiki-comment"""
        from zeta.config.environment import wikicomp

        errmsg = ''
        errmsg += ( not text and 'text, ' )  or ''
        errmsg += ( not commentby and 'commentby, ' )  or ''
        errmsg += ( not version_id and  'version_id, ' ) or ''
        if errmsg : 
            errmsg = 'Check ' + errmsg  + '!!'
            raise ZetaFormError( errmsg )
        h.validate_fields( request )

        wcmtdetail = [ None, commentby, int(version_id), text ]
        if wiki_id and wiki_comment_id :
            wiki_comment_id = int(wiki_comment_id)
            wcmtdetail[0]   = wiki_comment_id
            wikicomp.create_wikicomment(
                    int(wiki_id), wcmtdetail, update=True, c=c, defer=defer
            )

        elif wiki_id :
            wc = wikicomp.create_wikicomment(
                    int(wiki_id), wcmtdetail, c=c, defer=defer
            )
            wiki_comment_id = wc.id

        replytocomment_id = replytocomment_id and int(replytocomment_id)
        if wiki_comment_id and replytocomment_id :
            wikicomp.comment_reply( wiki_comment_id, replytocomment_id )

class FormWikiTags( FormWikis ) :
    """Form component to add / remove wiki tags"""
    formname = [ 'addwikitags', 'delwikitags' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'wiki_id', ('tags', '') ] )

    def submitform( self, request, c, formname, user_id, project_id, wiki_id,
                    tags, defer=False, **kwargs ) :
        """add / remove wiki tags"""
        from zeta.config.environment import wikicomp

        tagnames   = list(set( h.parse_csv( tags ) ))
        if wiki_id and formname == 'addwikitags' :
            w = wikicomp.get_wiki( int(wiki_id) )
            wikicomp.add_tags( w, tagnames, c=c, defer=defer )

        if wiki_id and formname == 'delwikitags' :
            w = wikicomp.get_wiki( int(wiki_id) )
            wikicomp.remove_tags( w, tagnames, c=c, defer=defer )

class FormWikiAttachs( FormWikis ) : # attach_id, attachfile
    """Form component to add / remove wiki attachments"""
    formname = [ 'addwikiattachs', 'delwikiattachs' ]
    getparams = ( [], [ 'formname' ] )
    postparams = ( [], [ 'user_id', 'project_id', 'wiki_id' ] )
    postparamsall = ( [], [ 'attach_id', 'attachfile' ] )
    
    def submitform( self, request, c, formname, user_id, project_id, wiki_id, 
                    attach_ids, attachfiles, defer=False, **kwargs ) :
        """add / remove wiki attachments"""
        from zeta.config.environment import wikicomp, attcomp

        user = kwargs.get( 'user', None )

        if wiki_id and formname == 'delwikiattachs' :
            [ wikicomp.remove_attach(
                    int(wiki_id), int(attach_id), c=c, defer=defer
              ) for attach_id in attach_ids ]

        elif wiki_id and formname == 'addwikiattachs' and user :
            for attachfile in  attachfiles :
                a = attcomp.create_attach( attachfile.filename, 
                                           fdfile=attachfile.file, 
                                           uploader=user
                                         )
                wikicomp.add_attach( int(wiki_id), a, c=c, defer=defer )

class FormWikiDiff( FormWikis ) :
    """Form component to generate the difference between wiki versions.
    This component does not commit anything to the database."""
    formname = 'wikidiff'
    postparams = ( [], [ 'user_id', 'wiki_id', 'oldver', 'newver' ] )
    
    def submitform( self, request, c, user_id, wiki_id, oldver, newver,
                    defer=False, **kwargs ) :
        """Generate the difference between wiki versions"""
        c.oldver = oldver and int(oldver)
        c.newver = newver and int(newver)

class FormVcsfile2Wiki( FormWikis ) :
    """Form component to map a file in a project's repository as project wiki
    page."""
    formname = 'vcsfile2wiki'
    postparams = ( [], [ 'user_id', 'project_id', 'sourceurl', 'pagename' ] )
    
    def submitform( self, request, c, user_id, project_id, sourceurl, pagename,
                    defer=False, **kwargs ) :
        """Map a file in repostiory as wiki page"""
        from zeta.config.environment import wikicomp, projcomp
        from zeta.lib.base           import BaseController

        cntlr = BaseController()
        try :
            project_id = int(project_id)
        except :
            errmsg = 'Check project id !!'
            raise ZetaFormError( errmsg )

        if sourceurl and pagename :
            p = projcomp.get_project(int(project_id))
            wikiurl = cntlr.url_wikiurl( p.projectname, pagename
                      ) if pagename[0] != '/' else pagename 
            w = wikicomp.create_wiki(
                    unicode(wikiurl), wtype=unicode(WIKITYPE_IFRAME),
                    sourceurl=unicode(sourceurl), creator=c.authuser,
                    c=c, defer=defer
                )
            wikicomp.config_wiki( w, project=p, c=c, defer=defer )
            wikicomp.create_content( w.id, c.authuser, '' )
        else :
            errmsg = 'Please provide wiki pagename !!'
            raise ZetaFormError( errmsg )
