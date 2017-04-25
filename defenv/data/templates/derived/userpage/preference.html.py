# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294498249.1837151
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/userpage/preference.html'
_template_uri='/derived/userpage/preference.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['hd_script', 'bd_script', 'bd_body']


# SOURCE LINE 10


page_tooltips = [

[ 'Help',
"""Update your description and preferences"""
],
[ 'User Home',
"""Snatpshot of your activity along with statistics"""
],
[ 'Users',
"""List of registered users"""
],
[ 'GoogleMap',
"""If enable in site-admin -> site-config, watch yourself and your friends in
googlemap"""
],
[ 'MyTickets',
"""All tickets that are assigned to you across projects"""
],
[ 'Timeline',
"""Timeline of your activity"""
],

]



def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 8
    ns = runtime.Namespace(u'forms', context._clean_inheritance_tokens(), templateuri=u'/component/forms.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'forms')] = ns

    # SOURCE LINE 7
    ns = runtime.Namespace(u'elements', context._clean_inheritance_tokens(), templateuri=u'/component/elements.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'elements')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/basic1.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 132
        __M_writer(u'\n\n\n\n')
        # SOURCE LINE 168
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_script(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        str = context.get('str', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n    ')
        # SOURCE LINE 39
        __M_writer(escape(parent.hd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        function preference_forms() {\n            var div_accinfo = dojo.byId( "accinfo" );\n\n            /* User photo attachment */\n            new zeta.Attachments(\n                { user: [ \'')
        # SOURCE LINE 47
        __M_writer(escape(str(c.authuser.id)))
        __M_writer(u"', '")
        __M_writer(escape(c.authuser.username))
        __M_writer(u"' ],\n                  id: 'photoattachblk',\n                  addform: [ 'userphoto', '")
        # SOURCE LINE 49
        __M_writer(h.suburl_adduserphoto )
        __M_writer(u"' ],\n                  delform: [ 'deluserphoto', '")
        # SOURCE LINE 50
        __M_writer(h.suburl_deluserphoto )
        __M_writer(u"' ],\n                  editable: ")
        # SOURCE LINE 51
        __M_writer(escape([0,1][c.photo_editable == True]))
        __M_writer(u",\n                  url: '")
        # SOURCE LINE 52
        __M_writer(h.url_userprefresh )
        __M_writer(u"',\n                  label: 'Upload Photo',\n                  attachs: ")
        # SOURCE LINE 54
        __M_writer( h.json.dumps(c.photoattach) )
        __M_writer(u"\n                }, div_accinfo.childNodes[1]\n            );\n\n            /* User icon attachment */\n            new zeta.Attachments(\n                { user: [ '")
        # SOURCE LINE 60
        __M_writer(escape(str(c.authuser.id)))
        __M_writer(u"', '")
        __M_writer(escape(c.authuser.username))
        __M_writer(u"' ],\n                  id: 'iconattachblk',\n                  addform: [ 'usericon', '")
        # SOURCE LINE 62
        __M_writer(h.suburl_addusericon )
        __M_writer(u"' ],\n                  delform: [ 'delusericon', '")
        # SOURCE LINE 63
        __M_writer(h.suburl_delusericon )
        __M_writer(u"' ],\n                  editable: ")
        # SOURCE LINE 64
        __M_writer(escape([0,1][c.icon_editable == True]))
        __M_writer(u",\n                  url: '")
        # SOURCE LINE 65
        __M_writer(h.url_userirefresh )
        __M_writer(u"',\n                  label: 'Upload Icon',\n                  attachs: ")
        # SOURCE LINE 67
        __M_writer( h.json.dumps(c.iconattach) )
        __M_writer(u'\n                }, div_accinfo.childNodes[3]\n            );\n\n            new zeta.ConfigTabs({\n                id: "preftabs",\n                tabs: dojo.query( "div[name=preftab]" )\n                }, dojo.query( "div[name=preftabs]" )[0]\n            );\n\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 136
        __M_writer(u'\n    ')
        # SOURCE LINE 137
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n\n')
        # SOURCE LINE 139
        if c.googlemaps :
            # SOURCE LINE 140
            __M_writer(u'    <script\n        src="http://maps.google.com/maps?file=api&amp;v=2.x&amp;key=')
            # SOURCE LINE 141
            __M_writer(escape(c.googlemaps))
            __M_writer(u'"\n        type="text/javascript">\n    </script>\n\n    <script type="text/javascript">\n        var map         = null;\n        var geocoder    = null;\n        var fulladdress = "')
            # SOURCE LINE 148
            __M_writer(escape(c.fulladdress))
            __M_writer(u'"\n        var username    = "')
            # SOURCE LINE 149
            __M_writer(escape(c.authusername))
            __M_writer(u'"\n        function init_gmap() {\n            rc = creategmap( "useringmap", 400, 400 )\n            map      = rc[0];\n            geocoder = rc[1];\n            marker = showAddress( username, fulladdress, fulladdress );\n        }\n    </script>\n')
            pass
        # SOURCE LINE 158
        __M_writer(u'\n    <script type="text/javascript">\n        dojo.addOnLoad( preference_forms );\n        dojo.addOnLoad( initform_accountinfo );\n        dojo.addOnLoad( initform_updtpass );\n        dojoaddOnLoad( \'init_gmap\' );\n\n        dojo.addOnLoad( setup_userpanes );\n        dojo.addOnLoad( adjust_upheight );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        forms = _mako_get_namespace(context, 'forms')
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        capture = context.get('capture', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n    ')
        # SOURCE LINE 82
 
        pagebartext = "User preference (%s)" % c.authusername
        
        users = '<span class="ml10 fwnormal fntsmall">' +\
                ( '<a href="%s">Users</a></span>' % h.url_usershome )
        uhome = '<span class="ml10 fwnormal fntsmall">' +\
                ( '<a href="%s">Homepage</a></span>' % h.url_userhome )
        usersgmap = '<span class="ml10 fwnormal fntsmall">' +\
                    ( '<a href="%s">OnGooglemap</a></span>' % h.url_usersgmap )
        mytickets = '<span class="ml10 fwnormal fntsmall">' +\
                    ( '<a href="%s">MyTickets</a></span>' % h.url_mytickets )
        
        charts = capture( elements.iconlink, h.url_usercharts,
                          'barchart', title="Analytics for %s" % c.username,
                          classes="ml20"
                        )
        tline  = capture( elements.iconlink, h.url_usertline,
                          'timeline', title="Timeline", classes="ml10" )
            
        
        # SOURCE LINE 100
        __M_writer(u'\n    <div id="page">\n        ')
        # SOURCE LINE 102
        __M_writer(escape(elements.pagebar( pagebartext,
                            [ uhome, users, usersgmap, mytickets, charts, tline ],
                            tooltips=page_tooltips )))
        # SOURCE LINE 104
        __M_writer(u'\n        <div id="bdy" class="m10">\n        <div name="preftabs">\n            <div id="accinfo" class="dispnone" name="preftab" title="AccountInfo"\n                 selected="true">\n                <div name="photoattachs"></div>\n                <div name="iconattachs"></div>\n                <div class="disptable bclear pt20 ml50">\n                <div class="disptrow">\n                    <div class="disptcell w50 vtop">\n                    ')
        # SOURCE LINE 114
        __M_writer(escape(forms.form_accountinfo( c.authuser, h.suburl_accountinfo )))
        __M_writer(u'\n                    </div>\n                    <div class="disptcell" style="padding-left: 50px;">\n                        <div id="useringmap" class="fggray2 p5"\n                             style="border: 2px solid gray; width: 400px; height: 400px;">\n                             Want to see you on google map ? Enable `googlemaps` in\n                             site-admin->siteConfig\n                        </div>\n                    </div>\n                </div>\n                </div>\n            </div>\n            <div id="chpass" class="dispnone" name="preftab" title="ChangePassword">\n                ')
        # SOURCE LINE 127
        __M_writer(escape(forms.form_updtpass( c.authuser, h.suburl_updtpass )))
        __M_writer(u'\n            </div>\n        </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


