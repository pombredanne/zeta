# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294496354.628912
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/accounts/forgotpass.html'
_template_uri='/derived/accounts/forgotpass.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['hd_script', 'bd_script', 'bd_body']


# SOURCE LINE 9


page_tooltips = [
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
        # SOURCE LINE 14
        __M_writer(u'\n\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n    ')
        # SOURCE LINE 18
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
        # SOURCE LINE 40
        __M_writer(u'\n    ')
        # SOURCE LINE 41
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        forms = _mako_get_namespace(context, 'forms')
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n    <div id="bdy" class="mt50">\n    <div id="forgotpass" class="brtr10 brtl10">\n')
        # SOURCE LINE 24
        if c.errormsg :
            # SOURCE LINE 25
            __M_writer(u'            <div class="fgcrimson fntbold calign p20" style="font-size : 120%">\n                ')
            # SOURCE LINE 26
            __M_writer(escape(c.errormsg))
            __M_writer(u'\n            </div>\n')
            # SOURCE LINE 28
        elif c.form == 'request' :
            # SOURCE LINE 29
            __M_writer(u'            ')
            __M_writer(escape(forms.form_forgotpass( h.suburl_forgotpass )))
            __M_writer(u'\n')
            # SOURCE LINE 30
        elif c.form == 'submit' :
            # SOURCE LINE 31
            __M_writer(u'            <div class="fgblue fntbold calign p20" style="font-size : 120%">\n                Reset link sent to your emailid\n            </div>\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'    </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


