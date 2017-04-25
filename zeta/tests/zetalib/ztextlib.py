from   random               import choice, randint, shuffle, seed

from   zeta.lib.ztext       import EMAIL_ENDMARKER, Swiki, Attachment, \
                                   Ticket, Wiki, Review

def emptyline( chars=[' ', '\t'], maxlen=3 ) :
    """Construct empty line, optionally with chars"""
    return ''.join([ choice(chars) for i in range(1,maxlen) ])

def genattr( attr, val ) :
    """Generate attribute : value pair"""
    leadingchars  = emptyline()
    trailingchars = emptyline()
    colon         = choice([ ' : ', ':', ': ', ' :',
                             '\t: ', ':\t', ':\t ', ' :\t' ])
    if attr[0] == '>' :                             # Reply text
        line = attr 
    elif attr.strip( ' \t' ) == EMAIL_ENDMARKER :   # Email end marker
        line = attr 
    else :
        line = u"%s%s%s%s%s" % ( leadingchars, attr, colon, val, trailingchars )
    return line

def leadingemptylines( lines ) :
    """Add empty lines to the beginning of "lines" """
    leading = []
    [ leading.append( emptyline() ) for i in range( 1, randint(1,3)) ]
    return leading+lines

def trailingemptylines( lines ) :
    """Add empty lines to the end of "lines" """
    trailing = []
    [ trailing.append( emptyline() ) for i in range( 1, randint(1,3)) ]
    return lines+trailing

def prefixtextlines( textlines, hbdelimiters ) :
    """Prefix text lines with hbdelimiters and/or emptylines"""
    lines = []
    [ lines.append( emptyline() ) for i in range( 1, randint(1,3)) ]
    hbdelimiters and lines.append( choice(hbdelimiters) + choice(['', ':']) )
    [ lines.append( emptyline() ) for i in range( 1, randint(1,3)) ]
    lines.extend( textlines )
    [ lines.append( emptyline() ) for i in range( 1, randint(1,3)) ]
    return lines


text_a = \
"""During the last weeks, Kenn and I worked together to support EMF generated
editors running on RAP. I'm always mesmerized by how effective such synergies
can be used when people from different teams work together for a bigger goal.
Kudos to Kenn for his great work in EMF by refactoring the EMF UI bundles
(namely o.e.emf.ui.common and o.e.emf.ui.edit) in order to single-source them.
But what does that mean for the community?"""

replytext = \
"""
>Go out, grab EMF & RAP M6 from Helios, get your model ready, fire up
>properties view and switch "Rich Ajax Platform" to true. Hit the magic
>>"Generate All" button and you're done - an EMF backed RAP application."""

text_b = \
"""For the details, please refer to the EMF/RAP integration wiki page.
In case you want to see what else is going on in the RAP space right now, I'll
be giving a RAP 1.3 N&N talk tomorrow at EclipseCon. Hope to see you there!"""


#-------------------- Test cases for static wiki text block -----------------

def sw_testcase_1(swtype) :
    """create static wiki page"""
    attrs     = [ ( choice( Swiki.attributes['path'] ), u'sw/path/url' ),
                  ( choice( Swiki.attributes['type'] ), swtype.wiki_typename),
                  ( choice(Wiki.attributes['sourceurl']),
                    "http://discoverzeta.com/zwiki" ) ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = []
    [ hbdelimit.extend(v) for v in Swiki.hbdelimiter.values() ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def sw_verify_1( syscomp, swtype ) :
    sw = syscomp.get_staticwiki( u'sw/path/url' )
    return sw.text == text_a and \
           sw.type.wiki_typename == swtype.wiki_typename and \
           sw.sourceurl == "http://discoverzeta.com/zwiki"

def sw_testcase_2() :
    """update wiki page"""
    attrs     = [ ( choice( Swiki.attributes['path'] ), u'sw/path/url' ) ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = []
    [ hbdelimit.extend(v) for v in Swiki.hbdelimiter.values() ]
    textlines = attrlines + prefixtextlines( text_b.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def sw_verify_2( syscomp ) :
    sw = syscomp.get_staticwiki( u'sw/path/url' )
    return sw.text == text_b

def sw_testcase_3() :
    """with path, without hbdelimiter, without text"""
    attrs     = [ ( choice( Swiki.attributes['path'] ), u'sw/path/url' ) ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines
    textlines = leadingemptylines( textlines )
    return '\n'.join( textlines )

def sw_testcase_4() :
    """with path, without hbdelimiter, without text"""
    attrs     = [ ( choice( Swiki.attributes['path'] ), u'sw/path/url' ) ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = []
    [ hbdelimit.extend(v) for v in Swiki.hbdelimiter.values() ]
    hbdelimit.remove( '' )
    textlines = attrlines + [ choice( hbdelimit ) ]
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def sw_verify_4( syscomp ) :
    sw = syscomp.get_staticwiki( u'sw/path/url' )
    return sw.text == ''

#-------------------- Test cases for attachment text block -----------------

def att_testcase_1() :
    """Create an attachment, summary and optional
    text"""
    attrs = [( choice(Attachment.attributes['id']), 'New' ),
             ( choice(Attachment.attributes['summary']), 'Ztext Attachment summary' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def att_verify_1( attcomp ) :
    attachs = attcomp.get_attach()
    return attachs[-1].summary == 'Ztext Attachment summary'

def att_testcase_2( p ) :
    """Create an attachment, summary and optional
    text"""
    attrs = [( choice(Attachment.attributes['id']), 'New' ),
             ( choice(Attachment.attributes['projectname']), p.projectname ),
             ( choice(Attachment.attributes['summary']), 'Ztext1 Attachment summary' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def att_verify_2( attcomp, p ) :
    a = attcomp.get_attach()[-1]
    return a in p.attachments and (a.summary == 'Ztext1 Attachment summary')

def att_testcase_3( attach ) :
    """Update an attachment, tags, and optional text"""
    attrs = [( choice(Attachment.attributes['id']), str(attach.id) ),
             ( choice(Attachment.attributes['tags']), 'Ztext,tags' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join(textlines)

def att_verify_3( attcomp ) :
    attachs  = attcomp.get_attach()
    tagnames = [ t.tagname for t in attachs[-1].tags ]
    return 'Ztext' in tagnames and 'tags' in tagnames

def att_testcase_4() :
    """Create an attachment, with invalid data"""
    attrs = [ ( choice(Attachment.attributes['summary']), 'Ztext Attachment summary' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

#-------------------- Test cases for attachment text block -----------------

def wiki_testcase_1( p, type ) :
    """Create a new wiki page for `project`, using wikiurl, with type"""
    wikiurl = u'/p/%s/wiki/test/wiki1' % p.projectname
    attrs = [( choice(Wiki.attributes['wikiurl']), wikiurl ),
             ( choice(Wiki.attributes['type']), type.wiki_typename ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['text']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def wiki_verify_1( wikicomp, p, type ) :
    wikiurl = u'/p/%s/wiki/test/wiki1' % p.projectname
    w    = wikicomp.get_wiki(wikiurl)
    wcnt = wikicomp.get_content(w)
    return (w.type.wiki_typename == type.wiki_typename) and \
           (wcnt.text == text_a)

def wiki_testcase_2( p, type, summary ) :
    """Create a new wiki page for `project`, using projectname, pagename, with
    summary"""
    attrs = [( choice(Wiki.attributes['projectname']), p.projectname ),
             ( choice(Wiki.attributes['pagename']), u'test/wiki2' ),
             ( choice(Wiki.attributes['type']), type.wiki_typename ),
             ( choice(Wiki.attributes['summary']), summary ),
             ( choice(Wiki.attributes['sourceurl']),
               "http://discoverzeta.com/zwiki" ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['text']
    textlines = attrlines + prefixtextlines( text_b.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def wiki_verify_2( wikicomp, p, type, summary ) :
    wikiurl = u'/p/%s/wiki/test/wiki2' % p.projectname
    w    = wikicomp.get_wiki(wikiurl)
    wcnt = wikicomp.get_content(w)
    return (w.type.wiki_typename == type.wiki_typename) and \
           (w.summary == summary) and \
           (w.sourceurl == "http://discoverzeta.com/zwiki" ) and \
           (wcnt.text == text_b)

def wiki_testcase_3( wikicomp, p ) :
    """Update a new wiki page for `project`, using wikiid, with tags"""
    wikiurl   = u'/p/%s/wiki/test/wiki2' % p.projectname
    w         = wikicomp.get_wiki( wikiurl )
    attrs     = [( choice(Wiki.attributes['wikiid']), str(w.id) ),
                 ( choice(Wiki.attributes['tags']), 'Ztext,tags' ),
                ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['comment']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def wiki_verify_3( wikicomp, p ) :
    wikiurl  = u'/p/%s/wiki/test/wiki2' % p.projectname
    w        = wikicomp.get_wiki( wikiurl )
    wcmts    = wikicomp.get_wikicomment()
    tagnames = [ t.tagname for t in w.tags ]
    return (wcmts[-1].text == text_a) and 'Ztext' in tagnames and 'tags' in tagnames

def wiki_testcase_4( pid, user ) :
    """Update a new wiki page for `project`, using projectid, pagename, with
    favorite and upvote"""
    attrs = [( choice(Wiki.attributes['projectid']), pid ),
             ( choice(Wiki.attributes['pagename']), u'test/wiki2' ),
             ( choice(Wiki.attributes['favorite']), choice(['true','True']) ),
             ( choice(Wiki.attributes['vote']), choice(['up','Up']) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['text']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def wiki_verify_4( wikicomp, p, user ) :
    wikiurl  = u'/p/%s/wiki/test/wiki2' % p.projectname
    w        = wikicomp.get_wiki(wikiurl)
    wcnt     = wikicomp.get_content(w)
    return (wcnt.text == text_a) and (user in w.favoriteof) and \
           (w.votes[0].votedas == 'up')

def wiki_testcase_5( wikicomp, p ) :
    """UnMark favorite and downvote wiki page"""
    wikiurl  = u'/p/%s/wiki/test/wiki2' % p.projectname
    attrs = [( choice(Wiki.attributes['wikiurl']), wikiurl ),
             ( choice(Wiki.attributes['favorite']), choice(['false','False']) ),
             ( choice(Wiki.attributes['vote']), choice(['down','Down']) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['text']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def wiki_verify_5( wikicomp, p, user ) :
    wikiurl  = u'/p/%s/wiki/test/wiki2' % p.projectname
    w        = wikicomp.get_wiki(wikiurl)
    return user not in w.favoriteof and w.votes[0].votedas == 'down'

def wiki_testcase_6() :
    """Mark favorite for invalid wiki page"""
    attrs = []
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['text']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def wiki_testcase_7() :
    """Mark favorite for invalid wiki page"""
    attrs = [( choice(Wiki.attributes['wikiid']), '10000' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Wiki.hbdelimiter['text']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

#-------------------- Test cases for ticket text block -----------------

def tck_testcase_1( p, type, severity, promptuser, components ) :
    """Create a ticket with projectname, type, severity, summary, promptuser,
    components"""
    comps   = ', '.join([ str(comp.id) for comp in components ])
    summary = 'Some ticket summary ...'
    attrs = [( choice(Ticket.attributes['projectname']), p.projectname ),
             ( choice(Ticket.attributes['type']), type.tck_typename ),
             ( choice(Ticket.attributes['severity']), severity.tck_severityname ),
             ( choice(Ticket.attributes['summary']), summary ),
             ( choice(Ticket.attributes['promptuser']), promptuser.username ),
             ( choice(Ticket.attributes['components']), comps ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def tck_verify_1( tckcomp, type, severity, promptuser, components ) :
    t = tckcomp.get_ticket()[-1]
    return (t.type == type) and (t.severity == severity) and \
           (t.summary == 'Some ticket summary ...') and \
           (t.promptuser == promptuser) and (t.components == components)

def tck_testcase_2( p, type, severity, milestones, versions ) :
    """Create a ticket with projectid, type, severity, summary, milestones,
    versions"""
    mstns   = ', '.join([ str(m.id) for m in milestones ])
    vers    = ', '.join([ str(v.id) for v in versions ])
    summary = 'Some ticket summary another ...'
    attrs = [( choice(Ticket.attributes['projectname']), p.projectname ),
             ( choice(Ticket.attributes['type']), type.tck_typename ),
             ( choice(Ticket.attributes['severity']), severity.tck_severityname ),
             ( choice(Ticket.attributes['summary']), summary ),
             ( choice(Ticket.attributes['milestones']), mstns ),
             ( choice(Ticket.attributes['versions']), vers ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Ticket.hbdelimiter['description']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def tck_verify_2( tckcomp, type, severity, milestones, versions ) :
    t = tckcomp.get_ticket()[-1]
    return (t.type == type) and (t.severity == severity) and \
           (t.summary == 'Some ticket summary another ...') and \
           (t.milestones == milestones) and (t.versions == versions) and \
           (t.description == text_a)

def tck_testcase_3( t, type, severity, blockedby, blocking ) :
    """Update a ticket with type, severity, summary, blockedby, blocking"""
    bby   = ', '.join([ str(tck.id) for tck in blockedby ])
    bking = ', '.join([ str(tck.id) for tck in blocking ])
    attrs = [( choice(Ticket.attributes['ticket']), str(t.id) ),
             ( choice(Ticket.attributes['type']), type.tck_typename ),
             ( choice(Ticket.attributes['severity']), severity.tck_severityname ),
             ( choice(Ticket.attributes['blockedby']), bby ),
             ( choice(Ticket.attributes['blocking']), bking ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Ticket.hbdelimiter['description']
    textlines = attrlines + prefixtextlines( text_b.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def tck_verify_3( t, type, severity, blockedby, blocking ) :
    return (t.type == type) and (t.severity == severity) and \
           (sorted(t.blockedby) == sorted(blockedby)) and \
           (sorted(t.blocking) == sorted(blocking)) and \
           (t.description == text_b)

def tck_testcase_4( t, type, parent, user ) :
    """Update a ticket with type, parent, tags, favorite, upvote"""
    attrs = [( choice(Ticket.attributes['ticket']), str(t.id) ),
             ( choice(Ticket.attributes['type']), type.tck_typename ),
             ( choice(Ticket.attributes['parent']), str(parent.id) ),
             ( choice(Ticket.attributes['tags']), 'Ztext,tags' ),
             ( choice(Ticket.attributes['favorite']), choice(['true','True']) ),
             ( choice(Ticket.attributes['vote']), choice(['up','Up']) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Ticket.hbdelimiter['comment']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def tck_verify_4( t, type, parent, user ) :
    tcmt     = t.comments[0]
    tagnames = [ tag.tagname for tag in t.tags ]
    return (t.type == type) and (t.parent == parent) and \
           (user in t.favoriteof) and (t.votes[0].votedas == 'up' ) and \
           ('Ztext' in tagnames) and ('tags' in tagnames) and \
           (tcmt.text == text_a)

def tck_testcase_5( t ) :
    """Update a ticket with no-favorite, downvote, attachments"""
    attrs = [( choice(Ticket.attributes['ticket']), str(t.id) ),
             ( choice(Ticket.attributes['favorite']), choice(['false','False']) ),
             ( choice(Ticket.attributes['vote']), choice(['down','Down']) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def tck_verify_5( t, user ) :
    return user not in t.favoriteof and t.votes[0].votedas == 'down'

def tck_testcase_6() :
    """Insufficient data"""
    attrs = []
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Ticket.hbdelimiter['description']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def tck_testcase_7() :
    """Invalid ticket"""
    attrs = [( choice(Ticket.attributes['ticket']), '10000' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Ticket.hbdelimiter['description']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

#-------------------- Test cases for review text block -----------------

def revw_testcase_1( r, nature ) :
    """Comment on review with nature and position, tags"""
    position = 5 
    attrs = [( choice(Review.attributes['reviewid']), str(r.id) ),
             ( choice(Review.attributes['nature']), nature.naturename ),
             ( choice(Review.attributes['position']), position ),
             ( choice(Review.attributes['tags']), 'Ztext,tags' ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Review.hbdelimiter['comment']
    textlines = attrlines + prefixtextlines( text_a.split('\n'), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def revw_verify_1( revcomp, r, nature ) :
    rcmt = revcomp.get_reviewcomment()[-1]
    r    = revcomp.get_review( r.id )
    tagnames = [ tag.tagname for tag in r.tags ]
    return (rcmt.nature == nature) and (rcmt.position == 5) and \
           (rcmt.text == text_a) and ('Ztext' in tagnames) and \
           ('tags' in tagnames)

def revw_testcase_2( r ) :
    """Comment on review with position, favorite, attachments"""
    position = 10
    attrs = [( choice(Review.attributes['reviewid']), str(r.id) ),
             ( choice(Review.attributes['position']), position ),
             ( choice(Review.attributes['favorite']), choice(['true','True']) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Review.hbdelimiter['comment']
    textlines = attrlines + prefixtextlines( text_b.split( '\n' ), hbdelimit )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def revw_verify_2( revcomp, r, user ) :
    rcmt = revcomp.get_reviewcomment()[-1]
    r    = revcomp.get_review( r.id )
    return (rcmt.position == 10) and (rcmt.text == text_b) and \
           (user in r.favoriteof)

def revw_testcase_3( revcomp, r, action, nature, approved ) :
    """update review comment with action , nature, approved, un-favorite"""
    rcmt = revcomp.get_reviewcomment()[-1]
    approved= choice(['true','True']) if approved else choice(['false','False'])
    attrs = [( choice(Review.attributes['rcmtid']), str(rcmt.id) ),
             ( choice(Review.attributes['reviewid']), str(r.id) ),
             ( choice(Review.attributes['nature']), nature.naturename ),
             ( choice(Review.attributes['action']), action.actionname ),
             ( choice(Review.attributes['approved']), approved ),
             ( choice(Review.attributes['favorite']), choice(['false','False']) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    textlines = attrlines
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )
    pass

def revw_verify_3( revcomp, r, user, action, nature, approved ) :
    rcmt = revcomp.get_reviewcomment()[-1]
    return (rcmt.nature == nature) and (rcmt.action == action) and \
           (rcmt.approved == approved) and (user not in r.favoriteof)

def revw_testcase_4( r ) :
    """Comment on review without position"""
    attrs = [( choice(Review.attributes['reviewid']), str(r.id) ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Review.hbdelimiter['comment']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )

def revw_testcase_5() :
    """Comment on invalid review"""
    attrs = [( choice(Review.attributes['reviewid']), str(10000) ),
             ( choice(Review.attributes['position']), 2 ),
            ]
    attrlines = [ genattr( a, v ) for a, v in attrs ]
    hbdelimit = Review.hbdelimiter['comment']
    textlines = attrlines + prefixtextlines( text_a.split( '\n' ), [] )
    textlines = trailingemptylines( leadingemptylines( textlines ))
    return '\n'.join( textlines )
