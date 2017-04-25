# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""
=== Paster admin commands to manage the application via command line

> [<PRE paster request CONFIG_FILE URL [OPTIONS/ARGUMENTS] >]

where,
:CONFIG_FILE :: The .ini file that sets-up the application
:URL         :: Command url
:OPTIONS     :: Options as //key=value// pairs

"""


# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None
#   1. Version consistency is not checked when using paster admin command ...
#      brainstrom whether it okay to leave it that way.


import logging
import cgi
import os
from   os.path                 import abspath, join, dirname, isdir, isfile
from   pprint                  import pprint

from   pylons                  import config
from   pylons                  import request, response, session, tmpl_context as c

from   zeta.config.environment import dbversion, pkg_path, zetaversion
from   zeta.lib.base           import BaseController
import zeta.lib.helpers        as h
import zeta.lib.genwikidoc     as genwikidoc
import zeta.lib.vcsadaptor     as va
from   zeta.lib.mailclient     import MailDB, fetchconfig, projectemail, \
                                      SMTPconn, POPconn
from   zeta.lib.ztext          import parse, Context

log   = logging.getLogger( __name__ )
pjoin = os.path.join

def cmd_parse_request() :
    return dict([ item for item in
                      cgi.parse_qsl(request.environ['QUERY_STRING']) ])

class PasteradminController( BaseController ) :

    def __before__( self, environ ) :
        # TODO : Should the following line remain commented ?
        # self.beforecontrollers()
        from zeta.config.environment import userscomp, syscomp

        c.sysentries = syscomp.get_sysentry()
        if not request.environ['paste.command_request'] :
            raise Exception( 'Invoke these request via command' )

    def genwikidoc( self, environ ) :
        r"""
        ==== Generate application documentation

        Generate documentation from source code.

        > [<PRE paster request <.ini file> /pasteradmin/genwikidoc [docs=docs] >]

        where,
        :docs ::
            comma separated list of one or more of the following values, \\ 
              [<PRE schema vim zwhtml zwmacros zwextensions xmlrpc pasteradmin pygments >]
            If left empty will generate documentation for all the above
            components.
        """
        from zeta.model  import meta

        alldocs = [ 'schema', 'zwhtml', 'zwmacros', 'zwextensions', 'xmlrpc',
                    'pasteradmin', 'pygments', 'vim' ]
        args    = cmd_parse_request()
        docs    = args.get( 'docs', None )
        docs    = h.parse_csv( docs )
        if ('all' in docs) or (docs == []) :
            docs = alldocs

        helpdocsdir = pjoin( abspath( os.curdir ), 'defenv/staticfiles/help' )
        zwikdocsdir = pjoin( abspath( os.curdir ), 'defenv/staticfiles/help/zwiki' )
        if not isdir( helpdocsdir ) :
            print "Please run the command from root of source tree !!"
            return

        srcdocsdir  = pjoin( abspath( os.curdir ), 'docs' )
        if not isdir( srcdocsdir ) :
            print "Please run the command from root of source tree !!"
            return

        if 'schema' in docs :
            print "Generating schema doc ..."
            tables  = [ t for t in meta.metadata.sorted_tables ]
            genwikidoc.schemadoc( srcdocsdir, tables )

        if 'zwhtml' in docs :
            print "Generating doc for ZWiki HTML Templated Tags ..."
            genwikidoc.zwhtml( zwikdocsdir )

        if 'zwmacros' in docs :
            print "Generating doc for ZWiki macros ..."
            genwikidoc.zwmacros( zwikdocsdir )

        if 'zwextensions' in docs :
            print "Generating doc for ZWiki extensions..."
            genwikidoc.zwextensions( zwikdocsdir )

        if 'xmlrpc' in docs :
            print "Generating XMLRPC doc ..."
            genwikidoc.xmlrpc( helpdocsdir )

        if 'pasteradmin' in docs :
            print "Generating PasterAdmin doc ..."
            genwikidoc.pasteradmin( helpdocsdir )

        if 'pygments' in docs :
            print "Generating Pygments doc ..."
            genwikidoc.pygments( helpdocsdir )

        if 'vim' in docs :
            print "Generating vim doc ..."
            genwikidoc.vimdoc( helpdocsdir )



    def staticwiki( self, environ, do=None, dir=None, path=None ) :
        r"""
        ==== Guest wiki pages

        Push a directory tree of wiki documents as guest wiki pages, or pull guest
        wiki pages from database into a directory tree.

        > [<PRE paster request <.ini file> /pasteradmin/staticwiki <do> [dir] [path] >]

        where,
        :do ::
          can be, \\ 
          //push//, to push directory tree of wiki pages from <dir> into the 
                    database \\ 
          //pull//, to pull static wiki pages from database into <dir> \\ 
          //deleteall//, to delete all static-wiki pages in the database \\ 
          //delete//, to delete static-wiki page specified by <path>
        """
        from zeta.config.environment  import syscomp

        args = cmd_parse_request()
        do   = args.get( 'do', None )
        dir  = args.get( 'dir', None )
        path = args.get( 'path', None )

        dir     = dir and abspath( dir )

        if do == 'push' and dir :
            print "Pushing static wiki pages from %s ... " % dir
            files, skipped = syscomp.push_staticwiki( dir, byuser=u'admin' )
            for f in files :
                print "    ", f
            print "Skipped files ..."
            for f in skipped :
                print "    ", f

        elif do == 'pull' and dir :
            print "Pulling static wiki pages to %s ... " % dir
            files = syscomp.pull_staticwiki( dir )
            for f in files :
                print "    ", f

        elif do == 'deleteall' :
            print "Removing all static wiki entries ... "
            syscomp.remove_staticwiki( byuser=u'admin')

        elif do == 'delete' and path :
            # path is the swiki path that needs to be deleted
            print "Removing static wiki entry, '%s' ... " % path
            syscomp.remove_staticwiki( path, byuser=u'admin' )

        else :
            response.status_int = 400
            print "Invalid request ... \n"


    def phomepage( self, environ, do=None, file=None, project=None ) :
        r"""
        ==== Project home-page

        Update project homepage.

        > [<PRE paster request <.ini file> /pasteradmin/phomepage <do> <file> [project] >]

        where,
        :do ::
          can be, \\ 
          //push//, to push the <file> as project home-page for [project] \\ 
          //pull//, to pull <project> homepage from database and save it in <file> \\ 

        if [project] is not specified (for //push//), the operation will be
        done on all hosted projects.
        """
        from zeta.config.environment    import syscomp, projcomp, wikicomp

        if environ['paste.command_request'] :
            args = cmd_parse_request()
            do   = args.get( 'do', None )
            file = args.get( 'file', None )
            proj = args.get( 'project', None )

        file     = file and abspath( file )
        project  = projcomp.get_project( unicode(proj) )

        if project :
            projects = [ project ]
        else :
            projects = projcomp.get_project()

        if do == 'push' and file :
            for p in projects :
                print "Pushing homepage %s for project %s ... " % (
                      file, p.projectname )
                c.project = p
                w    = wikicomp.get_wiki(
                            unicode( self.url_wikiurl( p.projectname, 'homepage' ))
                       )
                if not w :
                    w = wikicomp.create_wiki(
                            unicode(self.url_wikiurl( p.projectname, 'homepage')),
                            type=c.sysentries.get( 'def_wikitype', None ),
                            creator=u'admin'
                        )
                    wikicomp.config_wiki( w, project=p )

                text = open( file ).read()
                wcnt = wikicomp.create_content( w.id, u'admin', unicode(text) )

        elif do == 'pull' and file and project :
            print "Pulling homepage for project %s to %s ... " % (
                  p.projectname, file )
            w    = wikicomp.get_wiki( 
                        unicode( self.url_wikiurl( p.projectname, 'homepage' ))
                   )
            wcnt = w and wikicomp.get_content( w.id )
            wcnt and open( file, 'w' ).write( wcnt.text )

        else :
            response.status_int = 400
            print "Invalid request ... \n"


    def search( self, environ ) :
        r"""
        ==== Xapian search indexing

        Build search index table for database content.

        > [<PRE paster request <.ini file> /pasteradmin/search <do> [doctypes] [replace=1] [querystring] [xid] >]

        where,
        :do :: 
          can be, \\ 
          //index//, to index all documents from tables mentioned in [doctypes] \\ 
          //queryterms//, convert the <querystring> and display the query terms \\ 
          //query//, results for <querystring> \\ 
          //clear//, remove the document identified by //xid//
        :doctypes ::
          Documents for which to build search index, can be a comma separated
          value of,
          [<PRE user, attach, license, staticwiki, project, ticket, review, wiki. >]
          If not specified, index will be built for all documents
        :replace ::
          Overwrite the existing index with new one. If not specified, replace
          will be False
        :querystring ::
          simple query string
        :xid ::
          document id, only for administrators who know what they are doing.
        """
        from zeta.config.environment    import srchcomp

        if environ['paste.command_request'] :
            args     = cmd_parse_request()
            do       = args.get( 'do', None )
            replace  = args.get( 'replace', None )
            doctypes = args.get( 'doctypes', '' )
            q        = args.get( 'q', None )
            xid      = args.get( 'xid', None )

            doctypes = h.parse_csv( doctypes )

        if do == 'index' and not doctypes :
            print "Indexing Users ...."
            srchcomp.indexuser( replace=replace, flush=False )
            print "Indexing Attachments ...."
            srchcomp.indexattach( replace=replace, flush=False )
            print "Indexing Licenses ...."
            srchcomp.indexlicense( replace=replace, flush=False )
            print "Indexing StaticWikis ...."
            srchcomp.indexstaticwiki( replace=replace, flush=False )
            print "Indexing Projects ...."
            srchcomp.indexproject( replace=replace, flush=False )
            print "Indexing Tickets ...."
            srchcomp.indexticket( replace=replace, flush=False )
            print "Indexing Reviews ...."
            srchcomp.indexreview( replace=replace, flush=False )
            print "Indexing Wikis ...."
            srchcomp.indexwiki( replace=replace, flush=False )
            srchcomp.close()

        elif do == 'index' :
            'user'       in doctypes and srchcomp.indexuser( replace=replace, flush=False)
            'attach'     in doctypes and srchcomp.indexattach( replace=replace, flush=False )
            'license'    in doctypes and srchcomp.indexlicense( replace=replace, flush=False )
            'staticwiki' in doctypes and srchcomp.indexstaticwiki( replace=replace, flush=False )
            'project'    in doctypes and srchcomp.indexproject( replace=replace, flush=False )
            'ticket'     in doctypes and srchcomp.indexticket( replace=replace, flush=False )
            'review'     in doctypes and srchcomp.indexreview( replace=replace, flush=False )
            'wiki'       in doctypes and srchcomp.indexwiki( replace=replace, flush=False)
            srchcomp.close()

        elif do == 'queryterms' and q :
            print srchcomp.queryterms(q)

        elif do == 'query' and q :
            matches = srchcomp.query( q )
            for m in matches :
                print "--------------------------"
                print "Percent : %s  Rank : %s  Weight : %s " % \
                      ( m.percent, m.rank, m.weight )
                print m.document.get_data()[:100]

        elif do == 'clear' and xid :
            srchcomp.clear( xid )


    def upgradewiki( self, environ, do=None ) :
        r"""
        ==== Upgrade wiki

        Most of the text content in the database support wiki markup. When a
        newer version of ZWiki library is used, upgrade pre-translated
        wiki pages using the latest version.

        > [<PRE paster request <.ini file> /pasteradmin/upgradewiki [what] >]

        where,
        :what ::
          Is comma separated list of tables to upgrade, which can be,
          [<PRE staticwiki, project, ticket, review, wiki >]
        """
        from zeta.config.environment import
                syscomp, projcomp, tckcomp, revcomp, wikicomp

        args = cmd_parse_request()
        do   = args.get( 'do', None )
        what = args.get( 'what', [ 'staticwiki', 'project', 'ticket', 'review',
                                   'wiki' ])
        
        appenv   = config['zeta.envpath']

        print "Removing yacctabs ..."""
        if isfile( './yacctab.py' ) :
            os.remove( './yacctab.py' )
        if isfile( './yacctab.pyc' ) :
            os.remove( './yacctab.pyc' )
        if isfile( join( appenv, 'data/yacctab.py' )) :
            os.remove( join( appenv, 'data/yacctab.py' ))
        if isfile( join( appenv, 'data/yacctab.pyc' )) :
            os.remove( join( appenv, 'data/yacctab.pyc' ))

        if 'staticwiki' in what :
            count = syscomp.upgradewiki( byuser=u'admin' )
            print "Upgraded %s static wiki pages ... ok" % count

        if 'project' in what :
            cnt_proj, cnt_comp, cnt_mstn, cnt_ver = \
                    projcomp.upgradewiki( byuser=u'admin')
            print "Upgraded %s projects, %s components, %s milestones, %s versions... ok" % \
                  ( cnt_proj, cnt_comp, cnt_mstn, cnt_ver )

        if 'ticket' in what :
            cnt_ticket, cnt_tcmt = tckcomp.upgradewiki()
            print "Upgraded %s tickets and %s ticket comments ... ok" % \
                  ( cnt_ticket, cnt_tcmt )

        if 'review' in what :
            cnt_rcmt = revcomp.upgradewiki()
            print "Upgraded %s review comments ... ok" % cnt_rcmt

        if 'wiki' in what :
            cnt_wcnt, cnt_wcmt = wikicomp.upgradewiki()
            print "Upgraded %s wiki contents and %s wiki comments ... ok" % \
                  ( cnt_wcnt, cnt_wcmt )

        return ''


    def upgradedb( self, environ ) :
        r"""
        ==== Upgrade database

        When ever a deployed version of application is upgraded with a new
        version, database //might// get outdated. To bring the database in
        consistence with the application, use this command.

        > [<PRE paster request <.ini file> /pasteradmin/upgradedb >]
        """
        from  zeta.model.upgrade      import upgradedb
        from zeta.config.environment  import syscomp

        dbver_db  = syscomp.get_sysentry( u'database_version' )
        dbver_app = dbversion
        defenv    = join( pkg_path, 'defenv' )

        print "Current database version : %s" % dbver_db
        print "Application compatible version : %s" % dbver_app

        print "Upgrading the database from, %s to %s ..." % (dbver_db, dbver_app)
        upgradedb( dbver_db, dbver_app, defenv, config['zeta.envpath'] )

        syscomp.set_sysentry(
            { u'database_version' : unicode(dbver_app) },
            byuser=u'admin'
        )
        print "Database set to latest DB version %s" % dbver_app
    

    def upgradeenv( self, environ ) :
        r"""
        ==== Upgrade environment directory

        When ever a deployed version of application is upgraded with the new
        version, environment directory //might// get outdated. To bring the
        environment in consistence with application, use this command.

        > [<PRE paster request <.ini file> /pasteradmin/upgradeenv  >]
        """
        import zeta.lib.upgradeenv
        from zeta.config.environment    import syscomp

        appver_db = syscomp.get_sysentry( u'product_version' )
        defenv    = join( pkg_path, 'defenv' )
        zeta.lib.upgradeenv.upgradeenv( appver_db, defenv, config['zeta.envpath'] )
        syscomp.set_sysentry(
            { u'product_version' : unicode(zetaversion) },
            byuser=u'admin'
        )


    def maildb( self, environ ) :
        r"""
        ==== Manage mail server's SQL database

        The mail server should be configured to support virtual domains and
        virtual users. Use this command list/add/del virtual domains and
        virtual users.

        > [<PRE paster request <.ini file> /pasteradmin/maildb  \
                [ domain=action ] [ user=action ] [ name=name ] [ email=email ]
                [ password=password ] >]

        where,
        : do       :: specify the actions ''clean'' or ''setup'' or ''adddom'' or
                      ''deldom'' or ''listdom'' or ''adduser'' or ''deluser'' or
                      ''listuser''
        : name     :: for domain action. Will be interpreted as ''domainname''
        : email    :: for user action. Will be interpreted as ''email''
        : password :: for user action. Will be interpreted as email's password.

        Note that //domain// and //user// parameters are mutually exclusive
        """
        from zeta.config.environment    import projcomp, mailcomp

        if environ['paste.command_request'] :
            args     = cmd_parse_request()
            do       = args.get( 'do', '' )
            name     = args.get( 'name', None )
            email    = args.get( 'email', '' )
            password = args.get( 'password', None )

        server, login, loginpass  = fetchconfig( config )
        mdb = MailDB( config )

        if server and login and loginpass and mdb.Session :

            if do == 'setup' :
                domains, users = mailcomp.setupaccounts()
                for dn in domains :
                    print "Created virtual domain `%s`..." % dn
                for u in users :
                    print "Created virtual user `%s` ..." % u
        
            elif do == 'clean' :
                domains, users = mailcomp.cleanaccounts()
                for dn in domains :
                    print "Deleted virtual domain `%s`..." % dn
                for u in users :
                    print "Deleted virtual user `%s` ..." % u

            elif do == 'listdom' :
                for dn in mailcomp.virtualdomains : print dn

            elif do == 'adddom' and name :
                for dn in mailcomp.adddomains( name ) :
                    print "Created virtual domain  %s ..." % dn

            elif do == 'deldom' and name :
                for dn in mailcomp.deldomains( name ) :
                    print "Deleting virtual domain `%s` ..." % dn

            elif do == 'listuser' :
                for e, p in mailcomp.virtualusers : print "%s, %s ..." % (v,p)

            elif do == 'adduser' and email and password :
                for em in mailcomp.adduser( config, email, password ) :
                    print "Created user-email `%s` ..." % em

            elif do == 'deluser' and email :
                for em in mailcomp.delusers( email ) :
                    print "Deleted user-email `%s` ..." % em

            else :
                print 'Unknown maildb command'

        else :
            print "Insufficient information %s" % \
                                [ server, login, password, mdb.Session ]


    def mailcmd( self, environ ) :
        r"""
        ==== Manage mails with command line

        Fetch / Delete mails from mail server, using this commands line tool

        > [<PRE paster request <.ini file> /pasteradmin/mailcmd \
                [ do=delete ] [ project=projectname ] [ mails=mails ] >]

        where,
        : do      :: specify the action ''stat'' or ''fetch'' or ''delete''
        : project :: specify the project to `do` mail actions
        : mails   :: specify the mail numbers to fetch or delete.
        """
        from zeta.config.environment    import projcomp, mailcomp

        if environ['paste.command_request'] :
            args    = cmd_parse_request()
            do      = args.get( 'do', '' )
            project = args.get( 'project', '' )
            mails   = args.get( 'mails', '' )

        server, login, password = fetchconfig( config )
        if project :
            login = projectemail(config, project)
        sconn  = SMTPconn( config, server, login, password )
        pconn  = POPconn( config, server, login, password )

        fromto = mails.split( '..', 1 )
        if len(fromto) == 1 :
            mails = [ int(fromto) ]
        else :
            mails = range( fromto[0], fromto[1]+1 )

        if do == 'stat' :
            print "Statistics for %s : %s" % ( login, pconn.stat() )

        if do == 'fetch' :
            for i in mails : 
                print "Fetching mail %s ..." % i
                pprint( pconn.retr( i ))

        elif do == 'delete' :
            for i in mails :
                print "Deleting mail %s ..." % i
                pconn.dele( i )


    def mailprocess( self, environ ) :
        r"""
        ==== Process e-mails

        Fetch / Delete mails from mail server

        > [<PRE paster request <.ini file> /pasteradmin/mailprocess \
                [ ip=<server-ip> ] [ user=<login> ] [ passwd=<password> ]
                [ do=delete ] [ mails=mails ] >]

        where,
        : project :: specify the project to process the mail. If the value is
                     `_all_` all projects will be processed.
        : delete  :: True or False, to delete the mails after processing it.
        """
        from zeta.config.environment    import projcomp, mailcomp

        if environ['paste.command_request'] :
            args    = cmd_parse_request()
            project = args.get( 'project', '' )
            mails   = args.get( 'mails', '' )
            delete  = eval( args.get( 'delete', 'False' ))

        server, login, password = fetchconfig( config )
        if project == '_all_' :
            logins = [ projectemail(config, p) for p in projcomp.projectnames ]
        elif project :
            logins = [ projectemail(config, project) ]
        #sconn  = SMTPconn( config, server, login, password )
        #pconn  = POPconn( config, server, login, password )

        for login in logins :
            print "Fetching mail for %s ..." % login
            inmails = mailcomp.pullmails( login=login, loginpass=password,
                                          delete=True )
            ctxts   = mailcomp.processmails( inmails, login )
            valctxts= [ isinstance( ctxt, Context ) for ctxt in ctxts ]
            print "  Total mails pulled, %s" % inmails
            print "  Valid mails, %s " % len([ ctxt for ctxt in valctxts if ctxt ])
            print "  InValid mails, %s " % len([ ctxt for ctxt in valctxts if not ctxt ])


    def replogprocess( self, environ ) :
        r"""
        ==== Process repository logs

        Fetch repository logs, interpret the log message and update the
        database.

        > [<PRE paster request <.ini file> /pasteradmin/replogprocess \
                [ id=<repid> ] [ project=<projectname> ] [ name=<rep-name> ] >]

        where,
        : id      :: VCS id.
        : project :: Optional projectname
        : name    :: Optional repository name, which will be confirmed with
                     //id//
        """
        from zeta.config.environment import vcscomp, syscomp

        args    = cmd_parse_request()
        vcsid   = args.get( 'id', None )
        project = args.get( 'project', None )
        name    = args.get( 'name', None )

        vcs     = vcsid and vcscomp.get_vcs( int(vcsid) )
        namechk = name and vcs.name == name or True

        # Fetch the revision number from which messages had to be processed
        d_offs  = syscomp.get_sysentry( 'replogs', None )
        d_offs  = {} if d_offs == None else eval(d_offs)
        replogs = []

        if vcs and namechk :
            print "Processing repository logs for %s" % vcs.name
            print "---------------------------------"
            print "vcs-id   : %s" % vcs.id
            print "vcs-name : %s" % vcs.name
            print "vcs-type : %s" % vcs.type.vcs_typename
            print "project  : %s" % vcs.project.projectname
            fromrev = d_offs.get( vcs.id, 1 )
            vrep    = va.open_repository( vcs )
            replogs = vrep.logs( vcs.rooturl, revstart=fromrev )
        for r in replogs :
            ctxt = parse( r[0] )
            if isinstance( ctxt, Context ) :
                ctxt.commit( config, u'admin' )
                print "%s," % r[1]
        if replogs :
            d_offs[ vcs.id ] = replogs[-1][1]
            print "\nProcessed from %s to %s\n" % (replogs[0][1], replogs[-1][1])

        
    def analytics( self, environ ) :
        r"""
        ==== Analytics

        Project analysis, site analysis and repository analysis

        > [<PRE paster request <.ini file> /pasteradmin/analytics [anal=anals] >]

        where,
        :anals ::
            comma separated list of one or more of the following values, \\ 
            [<PRE tags attachs users license projects tickets reviews wiki timeline >]
            If left empty will compute all analytics
        """
        import zeta.lib.analytics as ca

        allanal = [ 'tags',  'attachs', 'staticwiki', 'users', 'license',
                    'projects', 'tickets', 'reviews', 'wiki', 'timeline' ]
        args    = cmd_parse_request()
        anals   = args.get( 'anal', None )
        anals   = h.parse_csv( anals )
        if ('all' in anals) or (anals == []) :
            anals = allanal

        if 'tags' in anals :
            print "Computing analytics for tags ..."
            ta = ca.get_analyticobj( 'tags' )
            ta.analyse()
            ta.cacheme()

        if 'attachs' in anals :
            print "Computing analytics for attachments ..."
            aa = ca.get_analyticobj( 'attachs' )
            aa.analyse()
            aa.cacheme()

        if 'staticwiki' in anals :
            print "Computing analytics for static-wiki ..."
            swa = ca.get_analyticobj( 'staticwiki' )
            swa.analyse()
            swa.cacheme()

        if 'users' in anals :
            print "Computing analytics for users ..."
            aa = ca.get_analyticobj( 'users' )
            aa.analyse()
            aa.cacheme()

        if 'license' in anals :
            print "Computing analytics for license ..."
            la = ca.get_analyticobj( 'license' )
            la.analyse()
            la.cacheme()

        if 'projects' in anals :
            print "Computing analytics for project ..."
            pa = ca.get_analyticobj( 'projects' )
            pa.analyse()
            pa.cacheme()

        if 'tickets' in anals :
            print "Computing analytics for tickets ..."
            ta = ca.get_analyticobj( 'tickets' )
            ta.analyse()
            ta.cacheme()

        if 'reviews' in anals :
            print "Computing analytics for reviews ..."
            ra = ca.get_analyticobj( 'reviews' )
            ra.analyse()
            ra.cacheme()

        if 'wiki' in anals :
            print "Computing analytics for wiki ..."
            wa = ca.get_analyticobj( 'wiki' )
            wa.analyse()
            wa.cacheme()

        if 'timeline' in anals :
            print "Computing analytics for timeline ..."
            tla = ca.get_analyticobj( 'timeline' )
            tla.analyse()
            tla.cacheme()
