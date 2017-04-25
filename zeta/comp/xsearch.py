# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to index and search database using Xapian"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : 
#   1. Delete documents (especially attachments that are removed)


from   __future__              import with_statement

import xapian                  as xap
from   os.path                 import basename

from   zeta.ccore              import Component
import zeta.lib.helpers        as h


DOCTYPE     = 0
ID          = 1
PROJECTNAME = 2

DEFAULT_SEARCH_FLAGS = (
    xap.QueryParser.FLAG_BOOLEAN  |
    xap.QueryParser.FLAG_PHRASE   |
    xap.QueryParser.FLAG_LOVEHATE |
    xap.QueryParser.FLAG_BOOLEAN_ANY_CASE
)

stemmer = xap.Stem('english')
qp      = xap.QueryParser()
qp.set_stemmer( stemmer )
qp.set_stemming_strategy( xap.QueryParser.STEM_SOME )

qp.add_prefix( 'id',      'XID:' )
qp.add_prefix( 'class',   'XCLASS:' )
qp.add_prefix( 'user',    'XUSER:' )
qp.add_prefix( 'email',   'XEMAIL:' )
qp.add_prefix( 'tzone',   'XTZONE:' )
qp.add_prefix( 'city',    'XCITY:' )
qp.add_prefix( 'state',   'XSTATE:' )
qp.add_prefix( 'country', 'XCOUNTRY:' )
qp.add_prefix( 'pincode', 'XPINCODE:' )
qp.add_prefix( 'file',    'XFILE:' )
qp.add_prefix( 'tag',     'XTAG:' )
qp.add_prefix( 'license', 'XLICENSE:' )
qp.add_prefix( 'project', 'XPROJECT:' )

xdb_r     = None
dburl     = None
def do_onetime( config ) :
    global xdb_r, userscomp, attcomp, liccomp, syscomp, projcomp, \
           tckcomp, revcomp, wikicomp, dburl

    if xdb_r == None :
        dburl = config['xapian.storepath']
        xdb_w = xap.WritableDatabase( dburl, xap.DB_CREATE_OR_OPEN )
        xdb_r = xap.Database( dburl )
        qp.set_database( xdb_r )

    else :
        xdb_r.reopen()

class XSearchComponent( Component ) :
    """Xapian search"""

    def index( self, document, replace, flush=True ) :
        """Index the document, which is a list of,
            [ metadata, attributes, contents],

        The first item of 'attributes' {key:value} paid must be XID

        replace,    if True, replace the existing index for id with new data.
        """
        do_onetime( self.compmgr.config )
        metadata, attributes, contents = document

        xdb_w   = xap.WritableDatabase( dburl, xap.DB_CREATE_OR_OPEN )
        indexer = xap.TermGenerator()
        doc     = xap.Document()

        indexer.set_stemmer(stemmer)
        indexer.set_document( doc )

        if replace :
            # Identify the document and its docid
            eq = xap.Enquire( xdb_r )
            eq.set_query( xap.Query( 'XID%s' % attributes[0][4:] ))
            matches = eq.get_mset( 0, 10 )
        else :
            matches = []

        # Metadata for documents
        doc.add_value( DOCTYPE, metadata['doctype'] )
        doc.add_value( ID,      str(metadata['id']) )
        'projectname' in metadata and \
                doc.add_value( PROJECTNAME, metadata['projectname'] )

        # Prefixed terms
        for attr in attributes :
            prefix, term = attr.split( ':' )
            indexer.index_text( term.encode('utf8'), 10, prefix )

        # Index the content
        doc.set_data(' ;;; '.join([ content for content in contents ]))
        for i in range(len(contents)) :
            content = contents[i]
            indexer.index_text( content.encode('utf8'), i+1 )
        if replace and len(matches) >= 1  :
            xdb_w.replace_document( matches[0].docid, doc )
            flush and xdb_w.flush()
        else :
            xdb_w.add_document( doc )
            flush and xdb_w.flush()
        return

    def clear( self, xid, flush=True ) :
        """Delete the document 'xid'"""
        do_onetime( self.compmgr.config )
        xdb_w   = xap.WritableDatabase( dburl, xap.DB_CREATE_OR_OPEN )
        matches = self.query( 'id:%s' % xid )
        len(matches) == 1 and xdb_w.delete_document( matches[0].docid )
        flush and xdb_w.flush()
        return

    def indexuser( self, users=[], clear=False, replace=False, flush=True ) :
        """Index all the users passed as argument, or index all the users in
        the database if 'users' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of users from index
        If replace == True,
            then replace the list of users with new data"""
        from zeta.config.environment import userscomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            users = users or userscomp.get_user()
            if clear :
                [ self.clear( 'id:user_%s' % u.id, flush=flush ) for u in user ]
            else :
                [ self.index( userscomp.documentof( u ), replace, flush=flush )
                  for u in users ]
        return

    def indexlicense( self, license=[], clear=False, replace=False, flush=True ) :
        """Index all the license passed as argument, or index all the license in
        the database if 'license' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of license from index
        If replace == True,
            then replace the list of license with new data"""
        from zeta.config.environment import liccomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            license = license or liccomp.get_license()
            if clear :
                [ self.clear( 'id:license_%s' % l.id, flush=flush )
                  for l in license ]
            else :
                [ self.index( liccomp.documentof( l ), replace, flush=flush )
                  for l in license ]
        return

    def indexattach( self, attachs=[], clear=False, replace=False, flush=True ) :
        """Index all the attachs passed as argument, or index all the attachs in
        the database if 'attachs' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of attachs from index
        If replace == True,
            then replace the list of attachs with new data"""
        from zeta.config.environment import attcomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            attachs = attachs or attcomp.get_attach()
            if clear :
                [ self.clear( 'id:attach_%s' % a.id, flush=flush ) for a in attachs ]
            else :
                [ self.index( attcomp.documentof( a ), replace, flush=flush )
                  for a in attachs ]
        return

    def indexstaticwiki( self, staticwikis=[], clear=False, replace=False, 
                         flush=True ) :
        """Index all the staticwikis passed as argument, or index all the 
        staticwikis in the database if 'staticwikis' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of staticwikis from index
        If replace == True,
            then replace the list of staticwikis with new data"""
        from zeta.config.environment import syscomp

        config = self.compmgr.config
        yessearch = config[ 'zeta.xapiansearch' ]
        if yessearch :
            do_onetime( config )
            staticwikis = staticwikis or syscomp.get_staticwiki()
            if clear :
                [ self.clear( 'id:staticwiki_%s' % swiki.path, flush=flush )
                  for swiki in staticwikis ]
            else :
                [ self.index(syscomp.documentof( swiki ), replace, flush=flush)
                  for swiki in staticwikis ]
        return

    def indexproject( self, projects=[], clear=False, replace=False,
                      flush=True ) :
        """Index all the projects passed as argument, or index all the
        projects in the database if 'projects' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of projects from index
        If replace == True,
            then replace the list of projects with new data"""
        from zeta.config.environment import projcomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            projects = projects or projcomp.get_project()
            if clear :
                [ self.clear( 'id:project_%s' % p.id, flush=flush )
                  for p in projects ]
            else :
                [ self.index( projcomp.documentof(p), replace, flush=flush )
                  for p in projects ]
        return

    def indexticket( self, tickets=[], clear=False, replace=False, flush=True ) :
        """Index all the tickets passed as argument, or index all the tickets in
        the database if 'tickets' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of tickets from index
        If replace == True,
            then replace the list of tickets with new data"""
        from zeta.config.environment import tckcomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            tickets = tickets or tckcomp.get_ticket()
            if clear :
                [ self.clear( 'id:ticket_%s' % t.id, flush=flush )
                  for t in tickets ]
            else :
                [ self.index( tckcomp.documentof( t ), replace, flush=flush )
                  for t in tickets ]
        return

    def indexreview( self, reviews=[], clear=False, replace=False, flush=True ) :
        """Index all the reviews passed as argument, or index all the reviews in
        the database if 'reviews' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of reviews from index
        If replace == True,
            then replace the list of reviews with new data"""
        from zeta.config.environment import revcomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            reviews = reviews or revcomp.get_review()
            if clear :
                [ self.clear( 'id:review_%s' % r.id, flush=flush ) for r in reviews ]
            else :
                [ self.index( revcomp.documentof( r ), replace, flush=flush )
                  for r in reviews ]
        return

    def indexwiki( self, wikis=[], clear=False, replace=False, flush=True ) :
        """Index all the wikis passed as argument, or index all the wikis in
        the database if 'wikis' is empty.
        If clear == True,
            then do the reverse, (i.e) clear the list of wikis from index
        If replace == True,
            then replace the list of wikis with new data"""
        from zeta.config.environment import wikicomp

        config = self.compmgr.config
        if config['zeta.xapiansearch'] :
            do_onetime( config )
            wikis = wikis or wikicomp.get_wiki()
            if clear :
                [ self.clear( 'id:wiki_%s' % w.id, flush=flush ) for w in wikis]
            else :
                [ self.index( wikicomp.documentof( w ), replace, flush=flush )
                  for w in wikis ]
        return

    def queryterms( self, querystring ) :
        """Find the terms that are found in the query string"""

        do_onetime( self.compmgr.config )
        query = qp.parse_query( querystring.encode('utf8'), DEFAULT_SEARCH_FLAGS )
        terms = []
        k     = query.get_terms_begin()
        end   = query.get_terms_end ()
        while k != end :
            term = k.get_term()
            term = term[0] == 'Z' and term[1:] or term
            term and terms.append( term )
            k.next()
        return terms


    def _queryprefixes( self, prefxquer ) :
        """Convert prefix list into query objects"""
        or_queries  = [ xap.Query(prefix)
                        for op, prefix in prefxquer if op == xap.Query.OP_OR ]
        and_queries = [ xap.Query(prefix)
                        for op, prefix in prefxquer if op == xap.Query.OP_AND ]
        or_query    = None
        if len(or_queries) > 1 :
            or_query  = reduce(
                          lambda q1, q2 : xap.Query( xap.Query.OP_OR, q1, q2 ),
                          or_queries
                        )
        elif len(or_queries) == 1 :
            or_query  = or_queries[0]

        and_query   = None
        if len(and_queries) > 1 :
            and_query = reduce(
                          lambda q1, q2 : xap.Query( xap.Query.OP_AND, q1, q2 ),
                          and_queries
                        )
        elif len(and_queries) == 1 :
            and_query = and_queries[0]
        
        if and_query and or_query :
            query = xap.Query( xap.Query.OP_AND, or_query, and_query )
        else :
            query = and_query or or_query or None
        return query

    def query( self, querystring, prefxquer=[], frommatch=0, maxitems=None ) :
        """Parse the query string, Enquire index, find matching set"""
        from zeta.config.environment import userscomp

        do_onetime( self.compmgr.config )
        maxitems   = maxitems or (xdb_r.get_doccount()-frommatch)
        query      = qp.parse_query( querystring.encode('utf8'), DEFAULT_SEARCH_FLAGS )
        eq         = xap.Enquire( xdb_r )

        # Combine queries
        prefquery  = self._queryprefixes( prefxquer )
        query      = prefquery and \
                           xap.Query( xap.Query.OP_AND, query, prefquery ) \
                     or query

        # Fetch
        eq.set_query( query )
        return eq.get_mset( frommatch, maxitems )


    def close( self ) :
        global xdb_r
        do_onetime( self.compmgr.config )
        del xdb_r

    def urlfor_match( self, m, urlconstructor ) :
        """Construct url for the matching document"""
        from zeta.config.environment import \
                    userscomp, attcomp, liccomp, syscomp, projcomp, tckcomp, \
                    revcomp, wikicomp

        do_onetime( self.compmgr.config )
        doc     = m.document
        doctype = doc.get_value( DOCTYPE )
        id      = doc.get_value( ID )
        if doctype == 'user' :
            user    = userscomp.get_user( int(id ))
            text    = 'User : %s' % user.username
            url     = urlconstructor['user']( int(id)  )
        elif doctype == 'attach' :
            attach  = attcomp.get_attach( int(id ))
            # Attachments can be deleted
            if attach :
                text = 'Attachment : %s' % attach.filename
                url  = urlconstructor['attach']( int(id) )
            else :
                text = '-- Missing attachment. May be deleted'
                url  = ''
        elif doctype == 'license' :
            license = liccomp.get_license( int(id ))
            # License can be deleted
            if license :
                text = 'License : %s' % license.licensename
                url  = urlconstructor['license']( int(id) )
            else :
                text = '-- Missing License. May be deleted'
                url  = ''
        elif doctype == 'staticwiki' :  # id is 'path'
            swiki = syscomp.get_staticwiki( unicode(id) )
            text = 'Guest Wiki : %s' % swiki.path
            url = urlconstructor['staticwiki']( id )
        elif doctype == 'project' :
            project = projcomp.get_project( int(id) )
            text = 'Project : %s' % project.projectname
            url = urlconstructor['project']( int(id) )
        elif doctype == 'ticket' :
            projectname = doc.get_value( PROJECTNAME )
            ticket = tckcomp.get_ticket( int(id) )
            text = '(%s) Ticket : %s' % (projectname, ticket.summary)
            url = urlconstructor['ticket']( projectname, int(id) )
        elif doctype == 'review' :
            projectname = doc.get_value( PROJECTNAME )
            review  = revcomp.get_review( int(id) )
            text    = '(%s) Review : %s' % (projectname, review.id)
            url = urlconstructor['review']( projectname, int(id) )
        elif doctype == 'wiki' :
            projectname = doc.get_value( PROJECTNAME )
            wiki    = wikicomp.get_wiki( int(id) )
            text    = '(%s) Wiki : %s' % \
                            (projectname, os.path.basename(wiki.wikiurl))
            url = urlconstructor['wiki']( projectname, int(id) )
        else :
            text = ''
            url  = ''

        return text, url

    searchfaces = { 
                    'user'        : '1',
                    'attach'      : '1',
                    'license'     : '1',
                    'staticwiki'  : '1',
                    'project'     : '1',
                    'ticket'      : '1',
                    'review'      : '1',
                    'wiki'        : '1'
                  }

    projectfaces = {
                    'attach'      : '1',
                    'project'     : '1',
                    'ticket'      : '1',
                    'review'      : '1',
                    'wiki'        : '1'
                   }
