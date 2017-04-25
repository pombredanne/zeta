# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294317214.39311
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/home/titleindex.html'
_template_uri='/derived/home/titleindex.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['hd_script', 'bd_script', 'bd_body']


# SOURCE LINE 9


page_tooltips = [

[ 'Help',
"""Complete list of guest wiki pages that are published under this site.
"""
],
[ 'Guest-wiki',
"""Guest wiki, is non version controlled wiki documents that are expected to
be common to all projects, like for example the <a href="/help/">help</a> pages.
If you have the permission you can edit guest wiki documents.
<a href="/help/GuestWiki">Learn more</a>.
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
        # SOURCE LINE 27
        __M_writer(u'\n\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    ')
        # SOURCE LINE 31
        __M_writer(escape(parent.hd_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n    ')
        # SOURCE LINE 58
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        dojo.addOnLoad( setup_userpanes );\n        dojo.addOnLoad( adjust_upheight );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        forms = _mako_get_namespace(context, 'forms')
        capture = context.get('capture', UNDEFINED)
        c = context.get('c', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n    ')
        # SOURCE LINE 35

        pagebartext = 'TitleIndex'
        searchbox   = capture(
                        forms.form_searchbox,
                        c.authuser, 'searchswiki', 'Search-staticwikipages',
                        h.suburl_search, c.searchfaces
                      )
            
        
        # SOURCE LINE 42
        __M_writer(u'\n    <div id="page">\n        ')
        # SOURCE LINE 44
        __M_writer(escape(elements.pagebar(
            pagebartext, spans=[ searchbox ], tooltips=page_tooltips
        )))
        # SOURCE LINE 46
        __M_writer(u'\n        <div id="bdy">\n            <div>\n                ')
        # SOURCE LINE 49
        __M_writer(escape(elements.titleindex( c.swikis, h.url_forswiki, c.swsnippets )))
        __M_writer(u'\n                ')
        # SOURCE LINE 50
        __M_writer(escape(forms.form_delsw_h(c.authuser)))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


