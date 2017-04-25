# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294494465.484143
_template_filename=u'/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/base/basic1.html'
_template_uri=u'/base/basic1.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['bd_breadcrumbs', 'hd_meta', 'hd_title', 'bd_metanav', 'hd_links', 'hd_script', 'bd_body', 'bd_header', 'hd_styles', 'bd_footer', 'item_metanav', 'bd_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 9
    ns = runtime.Namespace(u'forms', context._clean_inheritance_tokens(), templateuri=u'/component/forms.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'forms')] = ns

    # SOURCE LINE 8
    ns = runtime.Namespace(u'elements', context._clean_inheritance_tokens(), templateuri=u'/component/elements.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'elements')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n\n<html>\n    <head>\n        ')
        # SOURCE LINE 15
        __M_writer(escape(self.hd_title()))
        __M_writer(u'\n        ')
        # SOURCE LINE 16
        __M_writer(escape(self.hd_meta()))
        __M_writer(u'\n        ')
        # SOURCE LINE 17
        __M_writer(escape(self.hd_links()))
        __M_writer(u'\n        ')
        # SOURCE LINE 18
        __M_writer(escape(self.hd_styles()))
        __M_writer(u'\n        ')
        # SOURCE LINE 19
        __M_writer(escape(self.hd_script()))
        __M_writer(u'\n    </head>\n    <body class="tundra">\n        ')
        # SOURCE LINE 22
        __M_writer(escape(self.bd_header()))
        __M_writer(u'\n        ')
        # SOURCE LINE 23
        __M_writer(escape(self.bd_breadcrumbs()))
        __M_writer(u'\n        ')
        # SOURCE LINE 24
        __M_writer(escape(self.bd_body()))
        __M_writer(u'\n        ')
        # SOURCE LINE 25
        __M_writer(escape(self.bd_footer()))
        __M_writer(u'\n        ')
        # SOURCE LINE 26
        __M_writer(escape(self.bd_script()))
        __M_writer(u'\n    </body>\n</html>\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n\n')
        # SOURCE LINE 80
        __M_writer(u'\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n\n')
        # SOURCE LINE 145
        __M_writer(u'\n\n')
        # SOURCE LINE 173
        __M_writer(u'\n\n')
        # SOURCE LINE 175
        __M_writer(u'\n\n')
        # SOURCE LINE 220
        __M_writer(u'\n\n')
        # SOURCE LINE 345
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        session = context.get('session', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 147
        __M_writer(u'\n    ')
        # SOURCE LINE 148

        e  = request.environ
        bd = session.get( 'breadcrumbs', [] )
        hrefs = h.urlpathcrumbs( e['PATH_INFO'], e['HTTP_HOST'], e['SCRIPT_NAME'] )
        node = lambda text, ref : '<a class="mr10 fgred nodec" href="%s">%s</a>' % (
                                   ref, text )
            
        
        # SOURCE LINE 154
        __M_writer(u'\n    <div class="ralign fntsmall mt5 mb10" style="">\n')
        # SOURCE LINE 156
        if c.authorized :
            # SOURCE LINE 157
            __M_writer(u'        <span id="urlbreadcrumb">\n')
            # SOURCE LINE 158
            for text, ref in hrefs[:-1] :
                # SOURCE LINE 159
                __M_writer(u'            ')
                __M_writer(escape(elements.iconize( node(text,ref), 'arrow_right', classes='floatl',
                                styles="padding-left: 8px" )))
                # SOURCE LINE 160
                __M_writer(u'\n')
                pass
            # SOURCE LINE 162
            if hrefs :
                # SOURCE LINE 163
                __M_writer(u'            ')
                __M_writer(escape(elements.iconize( hrefs[-1][0], 'arrow_right', classes='floatl fggray',
                                styles="padding-left: 8px" )))
                # SOURCE LINE 164
                __M_writer(u'\n')
                pass
            # SOURCE LINE 166
            __M_writer(u'        </span>\n')
            # SOURCE LINE 167
            for title, href in bd :
                # SOURCE LINE 168
                __M_writer(u'            <a class="ml10" href="')
                __M_writer(escape(href))
                __M_writer(u'">')
                __M_writer(escape(title))
                __M_writer(u'</a>\n')
                pass
            # SOURCE LINE 170
            __M_writer(u'        &ensp;\n')
            pass
        # SOURCE LINE 172
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_meta(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n    <title>')
        # SOURCE LINE 32
        __M_writer(escape(c.title))
        __M_writer(u'</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_metanav(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        def item_metanav(m,cls):
            return render_item_metanav(context,m,cls)
        __M_writer = context.writer()
        # SOURCE LINE 82
        __M_writer(u'\n    <div id="metanav" class="fntsmall">\n')
        # SOURCE LINE 85
        __M_writer(u'        <table class="br5"><tr>\n            <td class="mtiblck"> ')
        # SOURCE LINE 86
        __M_writer(escape(c.authusername))
        __M_writer(u' </td>\n')
        # SOURCE LINE 87
        for m in c.metanavs[:-1] :
            # SOURCE LINE 88
            __M_writer(u'                ')
            __M_writer(escape(item_metanav(m, "mtiblck mtiwht")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 90
        __M_writer(u'            ')
        __M_writer(escape(item_metanav(c.metanavs[-1], "mtiwht")))
        __M_writer(u'\n        </tr></table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_links(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n    <link href="/zdojo/release/dojo/resources/dojo.css" rel="stylesheet" type="text/css"/>\n    <link href="/zdojo/ztundra.css" rel="stylesheet" type="text/css"/>\n    <link href="/zdojo/zdojo.css" rel="stylesheet" type="text/css"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_script(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n    <script src="/zdojo/release/dojo/dojo.js" type="text/javascript"></script>\n    <script type="text/javascript">\n        // TODO : This function graciously fails handler subscription. Eventually this\n        //        should be removed ...\n        function dojoaddOnLoad( fnstr ) {\n            //try {\n            //    dojo.addOnLoad( fn );\n            //} catch( err ) { console.log( err )}\n            fn = dojo.getObject( fnstr )\n            if( typeof fn == \'function\' ) {\n                dojo.addOnLoad( fn );\n            }\n        };\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_header(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        forms = _mako_get_namespace(context, 'forms')
        getattr = context.get('getattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n    ')
        # SOURCE LINE 97

        url_prj =  getattr( h, 'url_prj', None )
        if c.project and url_prj :
            url_hdrlogo = url_prj
            imgsrc = c.prjlogo
        else :
            url_hdrlogo = h.url_sitehome
            imgsrc = c.sitelogo
        
        if c.project :
            title = c.projectname
            titlesummary = c.projsummary
        else :
            title = h.fromconfig('zeta.sitename', '?')
            titlesummary = h.fromconfig('zeta.welcomestring', '')
            
        
        # SOURCE LINE 112
        __M_writer(u'\n    <div id="lthead">\n        <div class="disptable w100">\n        <div class="disptrow w100">\n            <div class="disptcell p3" style="width: 100px;">\n                <div id="hdrlogo">\n                    <a class="nodec fggray fntcaption" href="')
        # SOURCE LINE 118
        __M_writer(escape(url_hdrlogo))
        __M_writer(u'"\n                       ><img alt="logo" src="')
        # SOURCE LINE 119
        __M_writer(escape(imgsrc))
        __M_writer(u'"/></a>\n                </div>\n            </div>\n            <div class="disptcell vtop">\n                ')
        # SOURCE LINE 123
        __M_writer(escape(elements.flashmessages()))
        __M_writer(u'\n                ')
        # SOURCE LINE 124
        __M_writer(escape(forms.form_searchbox(
                    c.authuser, 'searchzeta', 'Search-Site', h.suburl_searchzeta,
                    style='padding-left: 7px;'
                )))
        # SOURCE LINE 127
        __M_writer(u'\n                ')
        # SOURCE LINE 128
        __M_writer(escape(self.bd_metanav()))
        __M_writer(u'\n                <div id="sitetitle">\n                <dl style="padding: 10px 0px 0px 10px">\n                    <dt class="fntxlarge fntitalic">')
        # SOURCE LINE 131
        __M_writer(escape(title))
        __M_writer(u'</dt>\n                    <dd class="fntlarge">')
        # SOURCE LINE 132
        __M_writer(escape(titlesummary))
        __M_writer(u'</dd>\n                </dl>\n                </div>\n')
        # SOURCE LINE 141
        __M_writer(u'            </div>\n        </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_styles(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_footer(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 177
        __M_writer(u'\n    <div class="bclear" id="footer">\n        <hr style="margin-bottom: 0px"/>\n        <a class="floatl" href="')
        # SOURCE LINE 180
        __M_writer(escape(c.zetalink))
        __M_writer(u'"\n           ><img width="110" height="45" src="')
        # SOURCE LINE 181
        __M_writer(escape(c.zetalogo))
        __M_writer(u'"/></a>\n        <div class="floatl" style="font-size: 11px; height : 45px">\n            <div class="ml5 calign" style="height : 22px; border-bottom : 4px solid Gainsboro">\n                <span style="vertical-align : -6px;">version : </span>\n                <span class="fntbold" style="vertical-align : -6px;">')
        # SOURCE LINE 185
        __M_writer(escape(c.zetaversion))
        __M_writer(u'</span>\n            </div>\n            <div class="ml5 pt2" style="height : 22px;">\n                <span class="fntbold" style="color: skyblue">SKR</span>\n                <span class="fntbold" style="color: black">Farms (P) Ltd</span>\n            </div>\n        </div>\n        <div class="floatr fntbold bgblue1 brbl5 brbr5">\n        <table><tr>\n            <td class="p5 calign vmiddle">\n                <div>Z Links</div>\n            </td>\n            <td class="p5" style="border-left: 1px solid gray;">\n                <div><a target="_blank" class="fgcrimson"\n                        title="Track Zeta development activities"\n                        href="http://dev.discoverzeta.com"\n                        >zeta-development</a></div>\n                <div><a target="_blank" class="fgcrimson"\n                        title="Discuss with us"\n                        href="http://groups.google.com/group/zeta-discuss"\n                        >zeta-mailinglist</a>\n            </td>\n            <td class="p5">\n                <div><a target="_blank" class="fgcrimson"\n                        title="Mail to us for support"\n                        href="mailto:support@discoverzeta.com"\n                        >Support</a></div>\n                <div><a target="_blank" class="fgcrimson"\n                        title="Download it now !!"\n                        href="http://discoverzeta.com/download"\n                        >Download</a></div>\n            </td>\n        </tr></table>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_item_metanav(context,m,cls):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n')
        # SOURCE LINE 70
        if m.type == 'link' :
            # SOURCE LINE 71
            __M_writer(u'        <td class="')
            __M_writer(escape(cls))
            __M_writer(u'">\n            <a style="margin: 0;" title="')
            # SOURCE LINE 72
            __M_writer(escape(m.title))
            __M_writer(u'" href="')
            __M_writer(escape(m.href))
            __M_writer(u'"\n               >')
            # SOURCE LINE 73
            __M_writer(escape(m.text))
            __M_writer(u'</a></td>\n')
            # SOURCE LINE 74
        elif m.type == 'pointer' :
            # SOURCE LINE 75
            __M_writer(u'        <td class="')
            __M_writer(escape(cls))
            __M_writer(u'">\n            <span name="')
            # SOURCE LINE 76
            __M_writer(escape(m.text))
            __M_writer(u'" class="fntsmall pointer fgblue">\n                ')
            # SOURCE LINE 77
            __M_writer(escape(m.text))
            __M_writer(u'<span class="fntxsmall vmiddle"> &#9660;</span>\n            </span></td>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 222
        __M_writer(u'\n    <script src="/zdojo/release/dijit/dijit.js" type="text/javascript"></script>\n    <script src="/zdojo/release/dojox/grid/DataGrid.js" type="text/javascript"></script>\n\n    <script src="/zdojo/zlib.js" type="text/javascript"></script>\n    <script src="/zdojo/zwidgets.js" type="text/javascript"></script>\n\n')
        # SOURCE LINE 230
        __M_writer(u'    <script src="/jquery-1.4.2.min.js" type="text/javascript"></script>\n    <script src="/highcharts/highcharts.js" type="text/javascript"></script>\n    <script src="/highcharts/scripts.js" type="text/javascript"></script>\n    <script src="/zhighcharts.js" type="text/javascript"></script>\n')
        # SOURCE LINE 237
        __M_writer(u'\n')
        # SOURCE LINE 240
        if h.webanalytics and not getattr( c, 'skipga', False ) :
            # SOURCE LINE 241
            __M_writer(u'        ')
            __M_writer(h.webanalytics )
            __M_writer(u'\n')
            pass
        # SOURCE LINE 243
        __M_writer(u'\n    <script type="text/javascript">\n        // Common initialization routine\n        function init_zeta() {\n            dojo.subscribe( \'flash\', null, flashmsghandler );\n        }\n\n        // Initialize quick-links\n        function qlinks_menu() {\n            var qlMenu;\n            var tgtnodes = dojo.query( \'div#metanav span[name=quick-links]\' )[0];\n            var quicklinks = ')
        # SOURCE LINE 254
        __M_writer(h.json.dumps( h.quicklinks ) )
        __M_writer(u';\n            var quicklinks_s = ')
        # SOURCE LINE 255
        __M_writer(h.json.dumps( h.quicklinks_special ) )
        __M_writer(u';\n\n            if ( tgtnodes ) {\n                pMenu = new zeta.Menu({\n                                targetNodes   :[ tgtnodes ],\n                                style: { zIndex: 50, fontSize: \'small\', width: \'7em\',\n                                         color: \'blue\' }\n                        });\n                dojo.forEach( quicklinks,\n                    function( ql ) {\n                        purl = \'<a href="\' + ql[1] + \'">\' + ql[0] + \'</a>\'\n                        pMenu.addChild( new zeta.MenuItem(\n                                            { content: purl, class: \'fntbold hoverhighlight\' }\n                                      ));\n                    }\n                );\n                pMenu.addChild( new zeta.MenuItem({ content: \'<hr/>\' }));\n                dojo.forEach( quicklinks_s,\n                    function( ql ) {\n                        purl = \'<a href="\' + ql[1] + \'">\' + ql[0] + \'</a>\'\n                        pMenu.addChild( new zeta.MenuItem(\n                                            { content: purl, class: \'fntbold hoverhighlight\' }\n                                      ));\n                    }\n                );\n            }\n        }\n\n        // Initialize project menu\n        function project_menu() {\n            var pMenu;\n            var tgtnodes = dojo.query( \'div#metanav span[name=myprojects]\' )[0];\n            var myprojects = ')
        # SOURCE LINE 287
        __M_writer(h.json.dumps( h.projectlinks ) )
        __M_writer(u';\n\n            if ( tgtnodes ) {\n                pMenu = new zeta.Menu({\n                                targetNodes   :[ tgtnodes ],\n                                style: { zIndex: 50, fontSize: \'small\', width: \'8em\',\n                                         color: \'blue\', maxHeight: \'500px\' }\n                        });\n                pMenu.addChild(\n                    new zeta.MenuItem(\n                        { content: \'<a href="')
        # SOURCE LINE 297
        __M_writer(escape(h.url_createprj))
        __M_writer(u'">New-project</a>\',\n                          class: \'hoverhighlight\' }\n                    )\n                );\n                pMenu.addChild( new zeta.MenuItem({ content: \'<hr/>\' }));\n                dojo.forEach( myprojects,\n                    function( p ) {\n                        purl = \'<a href="\' + p[1] + \'">\' + p[0] + \'</a>\'\n                        pMenu.addChild( new zeta.MenuItem(\n                                            { content: purl, class: \'fntbold hoverhighlight\' }\n                                      ));\n                    }\n                );\n            }\n        }\n\n        dojo.addOnLoad( init_zeta );\n        dojo.addOnLoad( qlinks_menu );\n        dojo.addOnLoad( project_menu );\n        dojo.addOnLoad( tablesorter );\n        dojo.addOnLoad(togglezwbox);\n\n        // Handlers for other elements in derived files.\n        dojoaddOnLoad( \'pagebartooltip\' );\n        dojoaddOnLoad( \'contexttooltip\' );\n\n        // Handler for search box.\n        dojo.addOnLoad( function() {\n            dojo.forEach( dojo.query( "span[name=searchbox] input[type=text]" ),\n                function( n ) {\n                    dojo.toggleClass( n, \'fggray2\', true );\n                    dojo.connect( n, \'onfocus\',\n                                  function( e ) {\n                                      dojo.attr( n, \'helpstr\', n.value );\n                                      n.value = \'\';\n                                      dojo.toggleClass( n, \'fggray2\', false );\n                                  }\n                                );\n                    dojo.connect( n, \'onblur\',\n                                  function( e ) {\n                                      n.value = dojo.attr( n, \'helpstr\' );\n                                      dojo.toggleClass( n, \'fggray2\', true );\n                                  }\n                                );\n                }\n            );\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


