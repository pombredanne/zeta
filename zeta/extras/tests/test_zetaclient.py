from   hashlib      import sha1
import sys
from   os.path      import split, join, abspath
from   random       import randint, choice
from   pprint       import pprint

zetaroot = split( split( split( abspath( __file__ ))[0] )[0] )[0]
ipath    = join( zetaroot, 'extras', 'xrclients' )
sys.path.insert( 0, ipath )

import zetaclient   as zc

randomword = lambda : ''.join([ choice('abcdefghijk132') for i in range(5) ])

def parse_csv( line ) :
    """Parse a line of comma seperated values, discarding duplicate values and
    empty values, while stripping away the leading and trailing white spaces
    for valid values"""
    vals = line and line.split( ',' ) or []
    vals = filter( None, [ v.strip(' \t') for v in vals ] )
    return vals

def test_project( c ) :

    print "Testing project apis ..."

    # myprojects
    projobjs = c.myprojects()
    projects = sorted([ p.projectname for p in projobjs ])
    ref = sorted([ 'denethor', 'dernhelm', 'dwalin', 'elendil', 'greyhame',
                   'legolas', 'lockbearer', 'orald', 'treebeard' ])
    assert projects == ref

    # project details
    for p in projobjs :
        dets = p.fetch()

def test_staticwiki( c ) :

    print "Testing static wiki apis ..."

    swlist = []
    for sw in c.liststaticwikis() :
        sw.fetch()
        swlist.append( (sw.path, sw.text) )

    samppath = u'some/static/path/%s' % randomword()
    newlist  = []
    for i in range(10) :
        path = '%s%s' % ( samppath, i )
        sampcont = u'content for static path, %s' % path
        cont = sampcont[ : randint(1,len(sampcont)) ]
        sw   = c.newstaticwiki( path, cont )
        # Optionally update
        if choice([ 0, 1 ]) :
            cont = cont + 'Updated'
            sw.publish( cont )
        newlist.append( (path, cont) )
    db  = []
    for sw in c.liststaticwikis() :
        sw.fetch()
        db.append( (sw.path, sw.text) )
    ref = sorted( swlist + newlist, key=lambda t : t[0] )
    db  = sorted( db,  key=lambda t : t[0] )
    assert db==ref


def test_ticket( c, types, severities, statuses ) :
    
    print "Testing ticket apis ..."

    p         = choice( c.myprojects() )
    origtids  = [ t.id for t in p.fetchtickets() ]

    p.fetch()
    compids   = [ tup[0] for tup in p.components ]
    mstnids   = [ tup[0] for tup in p.milestones ]
    verids    = [ tup[0] for tup in p.versions ]

    newtids  = []
    for i in range(10) :
        summary  = u'summry for new ticket %s' % i
        type     = choice( types )
        severity = choice( severities )
        values_new = { 'description' : u'Description for ticket %s' % unicode(i),
                       'components'  : choice([ compids and [choice( compids)] or None, None ]),
                       'milestones'  : choice([ mstnids and [choice( mstnids)] or None, None ]),
                       'versions'    : choice([ verids and [choice( verids  )] or None, None ]),
                       'blocking'    : choice([ origtids and [choice( origtids)] or None, None ]),
                       'blockedby'   : choice([ origtids and [choice( origtids)] or None, None ]),
                       'parent'      : choice(origtids),
                     }
        kwargs = dict([ (a, values_new[a]) for a in values_new if choice([ True, False ]) ])
        t = p.newticket( summary, type, severity, **kwargs )
        kwargs = dict([ (k, kwargs[k]) for k in kwargs if kwargs[k] != None ])

        # Optionally config the ticket
        duedates   = [ ( '1.1.2012',   '01/01/2012' ),
                       ( '10/01/2012', '10/01/2012' ),
                       ( '10-1-2012',  '10/01/2012' ) ]
        values_cnf = { 'summary'     : u'updated summary for ticket %s' % i,
                       'type'        : choice([ choice( types ), None ]),
                       'severity'    : choice([ choice( severities ), None ]),
                       'description' : u'updated Description for ticket %s' % i,
                       'promptuser'  : choice([ p.projectusers and choice( p.projectusers ) or None, None ]),
                       'components'  : choice([ compids and [choice( compids)] or None, None ]),
                       'milestones'  : choice([ mstnids and [choice( mstnids)] or None, None ]),
                       'versions'    : choice([ verids and [choice( verids  )] or None, None ]),
                       'blocking'    : choice([ origtids and [choice( origtids)] or None, None ]),
                       'blockedby'   : choice([ origtids and [choice( origtids)] or None, None ]),
                       'parent'      : choice( origtids ),
                     }
        if choice([0,1]) :
            ckwargs = dict([ (a, values_cnf[a]) for a in values_cnf if choice([True, False ])  ])
            duedate = choice( duedates )
            ckwargs.update({ 'status'      : choice( statuses ),
                             'due_date'    : duedate[0],
                          })
            t.config( **ckwargs )
            [ kwargs.update({ k : ckwargs[k] }) for k in ckwargs if ckwargs[k] != None ]
            kwargs['due_date'] = duedate[1]

        newtids.append( t.id )
        t1  = t.fetch()
        t1.components = t1.compid and [ t1.compid ] or None
        t1.milestones = t1.mstnid and [ t1.mstnid ] or None
        t1.versions   = t1.verid and [ t1.verid ] or None
        db  = dict([ ( k, getattr(t1, k) ) for k in kwargs ])
        assert db == kwargs

        t.comment( u'Some comment on ticket' )
        t.addtags( [ u'hello', u'world' ] )
        t.deltags( [ u'hello', u'world' ] )
        t.vote( 'up' )
        t.vote( 'down' )
        t.favorite( True )
        t.favorite( False )

    assert sorted( origtids + newtids ) == sorted([ t.id for t in p.fetchtickets() ])

def test_wiki( c, types ) :

    print "Testing wiki apis ..."

    p           = choice( c.myprojects() )
    origwikis   = [ w.pagename for w in p.fetchwikis() ]

    for i in range(10) :
        pagename= u'some/Page/%s%s' % ( randomword(), i )
        type    = choice( types )
        summary = choice([ (u'Some summary for wiki %s'% i), u'', None ])
        w       = p.newwiki( pagename, type=type, summary=summary )
        text    = u'Some wiki content'
        w.publish( text )

        # Optionally configure wiki
        if choice([ 0, 1 ]) :
            chngtype = choice( types + ([None]*2) )
            chngsummary = choice([ (u'Updated summary for wiki %s'% i), u'', None ])
            w.config( type=chngtype, summary=chngsummary )
            if chngtype != None :
                type = chngtype
            if chngsummary != None :
                summary = chngsummary

        chkattrs = [ 'pagename', 'type', 'summary', 'text' ]
        w1  = w.fetch()
        db  = dict([ (k, getattr(w1, k)) for k in chkattrs ]) 
        ref = { 'pagename' : pagename,
                'type' : type,
                'summary' : summary,
                'text' : text,
              }
        assert db == ref

        w.comment( u'Some comment on wiki' )
        w.addtags([ u'hello', u'world' ])
        w.deltags([ u'hello', u'world' ])
        w.vote( 'up' )
        w.vote( 'down' )
        w.favorite( True )
        w.favorite( False )

if __name__ == '__main__' :
    passw = sha1( 'admin123' ).hexdigest()
    url = 'http://192.168.0.101:5000/xmlrpc?username=admin&password=%s' % passw
    c = zc.Client( url )

    sysentries  = c.systementries()
    tcktypes    = [ unicode(v) for v in parse_csv( sysentries['tickettypes'] ) ]
    tckseverity = [ unicode(v) for v in parse_csv( sysentries['ticketseverity'] ) ]
    tckstatus   = [ unicode(v) for v in parse_csv( sysentries['ticketstatus']) ]
    wikitypes   = [ unicode(v) for v in parse_csv( sysentries['wikitypes'] ) ]

    test_project( c )
    test_staticwiki( c )
    test_ticket( c, tcktypes, tckseverity, tckstatus )
    test_wiki( c, wikitypes )

