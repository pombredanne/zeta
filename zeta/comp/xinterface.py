# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component providing eXternal Inteface access to the server"""
import sys

from   sqlalchemy              import select

from   zeta.ccore              import Component
from   zeta.model.schema       import t_staticwiki
from   zeta.model              import meta
import zeta.lib.helpers        as h

class XInterfaceComponent( Component ) :
    """Component to interface with external applications"""

    def system( self ) :
        """Get the system table entries"""
        from zeta.config.environment import syscomp

        return (True, syscomp.get_sysentry(), '')

    def myprojects( self, user ) :
        """List of projects for `username`"""
        projnames = sorted( h.myprojects( user ))
        return ( True, (projnames or []), '' )

    def projectdetails( self, projectname ) :
        """Obtain project details like,
            components, milestones, versions, teams"""
        from zeta.config.environment import projcomp

        comps, mstns, vers, pusers = projcomp.projectdetails( projectname )
        comps = [ (k, comps[k]) for k in comps ]
        mstns = [ (k, mstns[k]) for k in mstns ]
        vers  = [ (k, vers[k]) for k in vers ]
        d = { 'components'   : comps,
              'milestones'   : mstns,
              'versions'     : vers,
              'projectusers' : pusers,
            }
        return ( True, d, '' )

    def list_sw( self ) :
        """List Static wiki pages"""
        q     = select( [ t_staticwiki.c.path ], bind=meta.engine )
        paths = sorted([ tup[0] for tup in q.execute().fetchall() if tup[0] ])
        return ( True, paths, '' )

    def create_sw( self, path, content=u'', swtype=None, sourceurl=None,
                   byuser=None ) :
        """Create a new static wiki page"""
        from zeta.config.environment import syscomp

        try :
            sw = syscomp.get_staticwiki( unicode(path) )
            if sw :
                rc, failmsg = False, ('%s, already exists' % path)
            else :
                sw  = syscomp.set_staticwiki( unicode(path), content,
                                              swtype=swtype, sourceurl=sourceurl,
                                              byuser=byuser )
                rc, failmsg = (sw and (True, '')) \
                             or (False, 'Unable to create %s' % path)
        except :
            rc, sw, failmsg = ( False, None,
                               "Type : %s, Value : %s" % sys.exc_info()[:2] )
        return ( rc, sw, failmsg )

    def read_sw( self, path ) :
        """Read static wiki specified by path"""
        from zeta.config.environment import syscomp

        sw      = syscomp.get_staticwiki( path )
        d       = sw and { 'path'     : sw.path,
                           'text'     : sw.text,
                           'texthtml' : sw.texthtml,
                         } \
                  or {}
        return ( bool(d), d, ('StaticWiki %s not found' % path) )

    def update_sw( self, path, content='', swtype=None, sourceurl=None,
                   byuser=None ) :
        """Update static wiki page specified by `path`, with `content`"""
        from zeta.config.environment import syscomp

        sw = syscomp.get_staticwiki( unicode(path) )
        sw = sw and syscomp.set_staticwiki( unicode(path), unicode(content),
                                            swtype=swtype, sourceurl=sourceurl,
                                            byuser=byuser 
                                          ) \
             or None
        return ( bool(sw), sw, ('Unable to update static wiki %s' % path) )

    def list_wiki( self, projectname ) :
        """List wiki urls for project `projectname`"""
        from zeta.config.environment import wikicomp

        wikipages = [ h.wiki_parseurl( wu )
                      for wid, wu in wikicomp.wikiurls( projectname ) ]

        return ( True, wikipages, '' )

    def create_wiki( self, projectname, wikiurl, wtype=None, summary=u'',
                     sourceurl=u'', byuser=None ) :
        """Create a wiki page for the project `projectname`"""
        from zeta.config.environment import wikicomp, projcomp

        wtype = wtype and unicode(wtype) \
               or unicode(c.sysentries['def_wikitype'])
        wiki = wikicomp.get_wiki( wikiurl )
        rc, wiki, failmsg = ( bool(wiki), wiki, 
                              ('wiki page, %s already exists' % wikiurl) )
        try :
            if not wiki :
                wiki = wikicomp.create_wiki( wikiurl, wtype, summary,
                                             sourceurl, creator=byuser )
                wiki and wikicomp.config_wiki(
                                wiki, project=projectname, byuser=byuser )
                rc, wiki, failmsg = ( bool(wiki), wiki,
                                      ('Unable to create wiki page %s'%wikiurl) )
        except :
            rc, wiki, failmsg = ( False, None, 
                                  "Type : %s, Value : %s" % sys.exc_info()[:2] )
        return (rc, wiki, failmsg)

    def read_wiki( self, projectname, wikiurl ) :
        """Read a wiki page for project `projectname`"""
        from zeta.config.environment import wikicomp

        wiki     = wikicomp.get_wiki( wikiurl )

        if wiki :
            wcnt = wikicomp.get_content( wiki )
            text = wcnt and wcnt.text or ''
            d={ 'type'      : wiki.type.wiki_typename,
                'summary'   : wiki.summary,
                'sourceurl' : wiki.sourceurl,
                'text'      : text
              }
            rc, failmsg = True, ''
        else :
            rc, d, failmsg = ( False, {},
                               ('Unable to read wiki page, %s' % wikiurl) )
        return ( rc, d, failmsg )

    def update_wiki( self, projectname, wikiurl, content, author ) :
        """Update a wiki page for project `projectname`"""
        from zeta.config.environment import wikicomp

        wiki     = wikicomp.get_wiki( wikiurl )
        try :
            if wiki :
                wpage = wikicomp.create_content( wiki, author, content )
                rc, wiki, failmsg = ( bool(wpage), wiki, 
                                      ('Unable to update wiki page, %s' % wikiurl)
                                    )
            else :
                rc, wiki, failmsg = ( False, None, 
                                      ('wiki page, %s does not exist' % wikiurl)
                                    )
        except :
            rc, wiki, failmsg = ( False, None,
                                  ("Type : %s, Value : %s" % sys.exc_info()[:2])
                                )
        return ( rc, wiki, failmsg )

    def config_wiki( self, projectname, wikiurl, wtype=None, summary=None,
                     sourceurl=None, byuser=None ) :
        """Config wiki page for project `projectname`"""
        from zeta.config.environment import wikicomp

        wiki = wikicomp.get_wiki( wikiurl )
        if wiki :
            wikicomp.config_wiki(wiki, wtype=wtype, summary=summary,
                                 sourceurl=sourceurl, byuser=byuser)
            rc, wiki, failmsg = True, wiki, ''

        else :
            rc, wiki, failmsg = ( False, None, ('Invalid wiki page, %s'%wikiurl) )
        return ( rc, wiki, failmsg )

    def comment_wiki( self, projectname, wikiurl, comment, commentor ) :
        """Comment on wiki page for project `projectname`"""
        from zeta.config.environment import wikicomp

        wiki     = wikicomp.get_wiki( wikiurl )

        if wiki and wiki.latest_version :
            wcmtdet = [ None, commentor, wiki.latest_version, comment ]
            wcmt    = wikicomp.create_wikicomment(
                            wiki, wcmtdet, byuser=commentor )
            rc, wcmt, failmsg = ( bool(wcmt), wcmt,
                                  ('Unable to create comment for wiki page %s' % \
                                              wikiurl)
                                )
        else :
            rc, wcmt, failmsg = ( False, None, ('Invalid wiki page, %s'%wikiurl) )
        return ( rc, wcmt, failmsg )

    def wiki_tags( self, projectname, wikiurl, addtags=None, deltags=None,
                   byuser=None ) :
        """Add or delete tags from wiki page"""
        from zeta.config.environment import wikicomp

        wiki     = wikicomp.get_wiki( wikiurl )
        if wiki :
            if addtags != None :
                wikicomp.add_tags( wiki, tags=addtags, byuser=byuser )
            if deltags != None :
                wikicomp.remove_tags( wiki, tags=deltags, byuser=byuser )
            rc, failmsg = True, ''

        else :
            rc, failmsg = True, ('Invalid wiki page, %s'%wikiurl)
        return (rc, wiki, failmsg )

    def wiki_vote( self, projectname, wikiurl, vote, user ) :
        """Upvote or Downvote a wiki page"""
        from zeta.config.environment import wikicomp

        wiki     = wikicomp.get_wiki( wikiurl )
        if wiki :
            ( vote == 'up' and wikicomp.voteup( wiki, user ) ) \
            or \
            ( vote == 'down' and wikicomp.votedown( wiki, user ) )
            rc, failmsg = True, ''

        else :
            rc, failmsg = False, ('Invalid wiki page, %s'%wikiurl)
        return (rc, wiki, failmsg)

    def wiki_fav( self, projectname, wikiurl, favorite, user ) :
        """Add or remove wiki page as favorite"""
        from zeta.config.environment import wikicomp

        wiki     = wikicomp.get_wiki( wikiurl )

        if wiki and favorite==True :
            wikicomp.addfavorites( wiki, [user], byuser=user )
            rc, failmsg = True, ''
            
        elif wiki and favorite==False :
            wikicomp.delfavorites( wiki, [user], byuser=user )
            rc, failmsg = True, ''

        else :
            rc, failmsg = False, ('Invalid wiki page, %s' % wikiurl)
        return (rc, wiki, failmsg )

    def list_ticket( self, projectname ) :
        """List all tickets under the project `projectname`"""
        from zeta.config.environment import tckcomp

        tickets = dict([ (str(t[0]), t[1:]) 
                         for t in tckcomp.ticketsummary( projectname ) ])

        if tickets :
            rc, d, failmsg = True, { 'tickets' : tickets }, ''
        else :
            failmsg = 'Project %s does not have any tickets' % projectname
            rc, d   = False, {},

        return (rc, d, failmsg)

    def create_ticket( self, projectname, summary, type, severity, owner,
                       description=u'', components=None, milestones=None,
                       versions=None, blocking=None, blockedby=None,
                       parent=None
                     ) :
        """Create a ticket for the project `projectname`"""
        from zeta.config.environment import tckcomp, projcomp

        project  = projcomp.get_project( projectname )

        try :
            if project :

                tckdet = [ None, summary, description, type, severity ]
                tck    = tckcomp.create_ticket(
                                    project, tckdet, owner=owner, byuser=owner
                         )
                tckcomp.config_ticket(
                      tck,
                      components= components and [ int(id) for id in components if id ],
                      milestones= milestones and [ int(id) for id in milestones if id ],
                      versions  = versions and [ int(id) for id in versions if id ],
                      blocking  = blocking and [ int(id) for id in blocking if id ],
                      blockedby = blockedby and [ int(id) for id in blockedby if id ] ,
                      parent    = parent and int(parent),
                      byuser    = owner,
                      append    = False,
                )
                rc, d, failmsg = True, { 'id' : tck.id }, ''

            else :
                rc, d, failmsg = False, {}, ('Invalid project, %s'%projectname)

        except :
            rc, d, failmsg = ( False, {},
                               ("Type : %s, Value : %s" % sys.exc_info()[:2])
                             )

        return (rc, d, failmsg)

    def read_ticket( self, projectname, ticket ) :
        """Read a ticket for project `projectname`"""
        from zeta.config.environment import tckcomp

        t       = tckcomp.get_ticket( ticket )
        if t :
            d = tckcomp.ticketdetails( t )
            d.update(dict([ (k, '') for k in [ 'compid', 'compname', 'mstnid',
                                               'mstnname', 'verid', 'vername',
                                               'parent' ]
                                    if d[k] == None
                         ])
                    )
            d.update({
                'blockedby': tckcomp.blockersof( t ),
                'blocking' : tckcomp.blockingfor( t ),
                'children' : tckcomp.childrenfor( t )
            })
            rc, failmsg = True, ''

        else :
            rc, d, failmsg = False, {}, ('Invalid ticket, %s' % ticket)
        return (rc, d, failmsg)

    def config_ticket( self, projectname, ticket, owner, summary=None, type=None,
                       severity=None, description=None, promptuser=None,
                       components=None, milestones=None, versions=None,
                       blocking=None, blockedby=None, parent=None,
                       status=None, due_date=None, byuser=None
                     ) :

        """Config ticket"""
        from zeta.config.environment import tckcomp

        t = tckcomp.get_ticket( ticket )
        projectname = unicode(projectname)

        try :
            if t :
                ts = tckcomp.get_ticket_status( t.tsh_id, attrload=['status'] )
                tckcomp.config_ticket(
                  t,
                  type      = type,
                  severity  = severity,
                  promptuser= promptuser,
                  components= components and [ int(id) for id in components if id ],
                  milestones= milestones and [ int(id) for id in milestones if id ],
                  versions  = versions and [ int(id) for id in versions if id ],
                  blocking  = blocking and [ int(id) for id in blocking if id ],
                  blockedby = blockedby and [ int(id) for id in blockedby if id ] ,
                  parent    = parent and int(parent),
                  append    = False,
                  byuser    = byuser
                )

                if (summary != None) or (description != None) :
                    tckdet = [ t.id, summary, description, t.type, t.severity ]
                    tckcomp.create_ticket( projectname, tckdet, t.promptuser,
                                           update=True, byuser=byuser )

                if ( status == ts.status.tck_statusname and (due_date != None))\
                   or \
                   ( (status == None) and (due_date != None) ) :
                    # Just change the  due_date for current tsh
                    tstatdet = [ ts.id, ts.status, due_date ]
                    tckcomp.create_ticket_status( t, tstatdet, owner,
                                                  update=True, byuser=byuser )
                elif status :
                    # New status
                    tstatdet = [ None, status, due_date ]
                    tckcomp.create_ticket_status( t, tstatdet, owner, byuser=byuser )

                rc, failmsg = True, ''

            else :
                rc, failmsg = False, ('Invalid ticket %s'%t)

        except :
            rc, failmsg = False, (" Type : %s, Value : %s" % sys.exc_info()[:2])

        return (rc, t, failmsg)

    def comment_ticket( self, projectname, ticket, comment, commentor ) :
        """Comment on ticket for project `projectname`"""
        from zeta.config.environment import tckcomp

        t = tckcomp.get_ticket( ticket )
        try :
            if t :
                tcmtdet = [ None, comment, commentor ]
                tcmt    = tckcomp.create_ticket_comment(
                                            t, tcmtdet, byuser=commentor )
                rc, failmsg = ( bool(tcmt),
                                ('Unable to create comment for ticket %s' % t.id)
                              )

            else :
                rc, tcmt, failmsg = False, None, ('Invalid ticket, %s' % ticket)

        except :
            rc, tcmt, failmsg = ( False, None,
                                  (" Type : %s, Value : %s" % sys.exc_info()[:2])
                                )
        return (rc, tcmt, failmsg)

    def ticket_tags( self, projectname, ticket, addtags=None, deltags=None,
                     byuser=None ) :
        """Add or delete tags from ticket"""
        from zeta.config.environment import tckcomp

        t = tckcomp.get_ticket( ticket )
        if t :
            if addtags != None :
                tckcomp.add_tags( t, tags=addtags, byuser=byuser )
            if deltags != None :
                tckcomp.remove_tags( t, tags=deltags, byuser=byuser )
            rc, failmsg = True, ''

        else :
            rc, failmsg = False, ('Invalid ticket, %s' % ticket)

        return (rc, t, failmsg)

    def ticket_vote( self, projectname, ticket, vote, user ) :
        """Upvote or Downvote a ticket"""
        from zeta.config.environment import tckcomp

        t = tckcomp.get_ticket( ticket )
        if t :
            ( vote == 'up' and tckcomp.voteup( t, user ) ) \
            or \
            ( vote == 'down' and tckcomp.votedown( t, user ) )
            rc, failmsg = True, ''

        else :
            
            rc, failmsg = False, ('Invalid ticket, %s' % ticket)

        return rc, t, failmsg

    def ticket_fav( self, projectname, ticket, favorite, user ) :
        """Add or remove ticket as favorite"""
        from zeta.config.environment import tckcomp

        t = tckcomp.get_ticket( ticket )

        if t and favorite==True :
            tckcomp.addfavorites( t, [user], byuser=user )
            rc, failmsg = True, ''
            
        elif t and favorite==False :
            tckcomp.delfavorites( t, [user], byuser=user )
            rc, failmsg = True, ''

        else :
            rc, failmsg = False, ('Invalid ticket, %s' % ticket)

        return (rc, t, failmsg)
