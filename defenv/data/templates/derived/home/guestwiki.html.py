# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294493252.0422001
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/home/guestwiki.html'
_template_uri='/derived/home/guestwiki.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['hd_script', 'swiki_edit', 'swiki_page', 'bd_body', 'bd_script']


# SOURCE LINE 9


page_tooltips = [

[ 'Help',
"""
<div>While navigating to a page, use this <b>Tool-Tip</b> widget to get a
quick help on how to interact with the page.
<a href="help/">Detailed help</a></div>
"""
],
[ 'Project',
"""Instantiate projects under this site, where every instance of a project
will have its own wiki, ticketing, review, and version control.
"""
],
[ 'Metanav',
"""The top-most tool bar, available in all pages."""
],
[ 'Header',
"""
Each page's header has a <b>site-logo</b> (configurable in site-admin) on the left
and <b>project-logo</b> (if the page is under a project's context) on the right.
"""
],
[ 'Page-Layout',
"""Apart from <b>meta-nav</b> tool bar, a page has the following layout -
<b>header</b>, <b>bread crumbs</b>, <b>main-nav</b> tab bar, <b>context-nav</b>
tool bar and <b>footer</b>. Only project-pages have <b>main-nav</b> and
<b>context-nav</b> elements. For non project pages, they are replaced with a
<b>page-bar</b>, like the one in this page.
"""
],
[ 'Guest Wiki',
"""Guest wiki, is non version controlled wiki documents that are independant
of any project, like for example the <a href="/help/">help</a> pages. If the url
does not map to an application function, it is freely available to create
a guest wiki page. <a href="/help/GuestWiki">Learn more</a>
<div class="calign w100 fntbold">
    To create a new guest wiki page, enter the url in the address bar and ENTER
</div>
"""
],

]



def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 7
    ns = runtime.Namespace(u'forms', context._clean_inheritance_tokens(), templateuri=u'/component/forms.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'forms')] = ns

    # SOURCE LINE 6
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
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 68
        __M_writer(u'\n\n')
        # SOURCE LINE 89
        __M_writer(u'\n\n')
        # SOURCE LINE 148
        __M_writer(u'\n\n\n')
        # SOURCE LINE 161
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n    ')
        # SOURCE LINE 59
        __M_writer(escape(parent.hd_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_swiki_edit(context):
    context.caller_stack._push_frame()
    try:
        forms = _mako_get_namespace(context, 'forms')
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 70
        __M_writer(u'\n<div class="zeditsw mr5">\n    <div class="pb2 posr ralign" style="border-bottom : 1px solid gray">\n        <span><a href="')
        # SOURCE LINE 73
        __M_writer(escape(h.url_swpage))
        __M_writer(u'">Back-to-Page</a></span>\n    </div>\n    <div class="dispnone mt10 ml10 mr10">\n        <fieldset style="background: #F4F4F4 url(/preview_bg.png) repeat scroll 0">\n            <legend>Preview( <a href="#edit">edit</a> )</legend>\n            <div class="ml10 mr10 swpreview"></div>\n        </fieldset>\n        <br/>\n        <hr/>\n    </div>\n    <div class="mt10">\n        <a name="edit"></a>\n        ')
        # SOURCE LINE 85
        __M_writer(escape(forms.form_editsw( c.authuser, c.swiki, c.wikitypenames,
                             h.suburl_editsw, h.url_swpage )))
        # SOURCE LINE 86
        __M_writer(u'\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_swiki_page(context,swtype,sourceurl,pagehtml):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\n')
        # SOURCE LINE 63
        if swtype == h.WIKITYPE_IFRAME :
            # SOURCE LINE 64
            __M_writer(u'    <div>')
            __M_writer(pagehtml )
            __M_writer(u'</div>\n')
            # SOURCE LINE 65
        else :
            # SOURCE LINE 66
            __M_writer(u'    <div>')
            __M_writer(pagehtml )
            __M_writer(u'</div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        c = context.get('c', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def swiki_edit():
            return render_swiki_edit(context)
        h = context.get('h', UNDEFINED)
        forms = _mako_get_namespace(context, 'forms')
        def swiki_page(swtype,sourceurl,pagehtml):
            return render_swiki_page(context,swtype,sourceurl,pagehtml)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 91
        __M_writer(u'\n    ')
        # SOURCE LINE 92

        pagebartext = c.swurl and str(c.swurl) or str(c.welcomestring) 
        
        if c.sweditable and not c.urldir :
            editsw = '<span name="editsw" class="ml10 fwnormal fntsmall">' +\
                     ( '<a href="%s" title="Edit this page">edit</a></span' % \
                       h.url_editsw )
            delsw = capture( elements.iconlink, h.suburl_delsw, 'trash',
                             classes="ml10",
                             title='Delete this guest wiki page' )
        else :
            editsw = '<span></span>'
            delsw  = '<span></span>'
        
        swtype = ''
        sourceurl = ''
        if c.swiki :
            swtype = c.swiki and c.swiki.type.wiki_typename or ''
            sourceurl = c.swiki.sourceurl
        if swtype == h.WIKITYPE_IFRAME :
            iframesrc = '&ensp;<span class="fntitalic fntxsmall">(from '+\
                           '<span class="fggreen">' + sourceurl + '</span>)'
        else :
            iframesrc = ''
        
        refr = ''
        if c.swhtml :
            refr = capture(
                    elements.iconlink, h.url_refreshsw,
                    'refresh', classes="ml20",
                    title='Fresh translation of this guest-wiki page'
                  )
        searchbox = capture(
                        forms.form_searchbox,
                        c.authuser, 'searchswiki', 'Search-GuestWiki-pages',
                        h.suburl_search, c.searchfaces
                    )
            
        
        # SOURCE LINE 129
        __M_writer(u'\n    <div id="page">\n        ')
        # SOURCE LINE 131
        __M_writer(escape(elements.pagebar(
            pagebartext, spans=[ searchbox, editsw, delsw, iframesrc, refr ],
            tooltips=page_tooltips
        )))
        # SOURCE LINE 134
        __M_writer(u'\n        <div id="bdy">\n            <div class="p5">\n')
        # SOURCE LINE 137
        if c.swikis :
            # SOURCE LINE 138
            __M_writer(u'                ')
            __M_writer(escape(elements.titleindex( c.swikis, h.url_forswiki, c.swsnippets )))
            __M_writer(u'\n                ')
            # SOURCE LINE 139
            __M_writer(escape(forms.form_delsw_h(c.authuser)))
            __M_writer(u'\n')
            # SOURCE LINE 140
        elif c.swhtml :
            # SOURCE LINE 141
            __M_writer(u'                ')
            __M_writer(escape(swiki_page(swtype, sourceurl, c.swhtml)))
            __M_writer(u'\n')
            # SOURCE LINE 142
        elif c.editsw and not c.urldir :
            # SOURCE LINE 143
            __M_writer(u'                ')
            __M_writer(escape(swiki_edit()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 145
        __M_writer(u'            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 151
        __M_writer(u'\n    ')
        # SOURCE LINE 152
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n\n        dojoaddOnLoad( \'initform_editsw\' );\n\n        dojo.addOnLoad( setup_userpanes );\n        dojo.addOnLoad( adjust_upheight );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


