# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294332929.7395761
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/siteadmin/tline.html'
_template_uri='/derived/siteadmin/tline.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['hd_script', 'bd_script', 'bd_body']


# SOURCE LINE 8


page_tooltips = [
]


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
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
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n\n\n')
        # SOURCE LINE 52
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_script(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(escape(parent.hd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n    function setup_charts() {\n        var datatline = ')
        # SOURCE LINE 19
        __M_writer( h.json.dumps(c.datatline) )
        __M_writer(u'\n        timelinechart( datatline, Date.UTC( ')
        # SOURCE LINE 20
        __M_writer(escape(','.join(c.startdt)))
        __M_writer(u" ),\n                       'chart_tline', 'Site Activity' );\n    }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n    ')
        # SOURCE LINE 44
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        dojo.addOnLoad( setup_charts );\n\n        dojo.addOnLoad( setup_userpanes );\n        dojo.addOnLoad( adjust_upheight );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        c = context.get('c', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n    ')
        # SOURCE LINE 27
 
        pagebartext = "Site Timeline"
        charts      = capture( elements.iconlink, h.url_sitecharts,
                               'barchart', title="Site Analytics" )
            
        
        # SOURCE LINE 31
        __M_writer(u'\n    <div id="page">\n        ')
        # SOURCE LINE 33
        __M_writer(escape(elements.pagebar( pagebartext, tooltips=page_tooltips )))
        __M_writer(u'\n        <div id="bdy" class="">\n            ')
        # SOURCE LINE 35
        __M_writer(escape(elements.timeline_view( c.logs, c.fromoff, c.tooff, c.links,
                                      chartid='chart_tline')))
        # SOURCE LINE 36
        __M_writer(u'\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


