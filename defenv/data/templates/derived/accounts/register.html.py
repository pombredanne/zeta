# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294493333.216748
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/accounts/register.html'
_template_uri='/derived/accounts/register.html'
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
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 62
        __M_writer(u'\n\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n')
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
        # SOURCE LINE 17
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(escape(parent.hd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        usernames = ')
        # SOURCE LINE 21
        __M_writer( h.json.dumps( c.usernames ) )
        __M_writer(u';\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\n    ')
        # SOURCE LINE 66
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        dojo.addOnLoad( initform_userreg );\n    </script>\n')
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
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n    <div id="page" class="p5">\n        <div class="p10 bgblue1 calign fntbold">\n            Registration form\n        </div>\n        <div id="bdy" class="mt20 w100" style="padding : 0 20% 0 0">\n')
        # SOURCE LINE 31
        if c.authorized :
            # SOURCE LINE 32
            __M_writer(u'                <div class="disptable" style="margin: 0 auto;">\n                <div class="disptrow">\n                    <div class="disptcell">\n                        ')
            # SOURCE LINE 35
            __M_writer(escape(forms.form_userreg( h.suburl_userreg, c.captcha_urlpath )))
            __M_writer(u'\n                    </div>\n                    <div class="disptcell">\n                    <div style="width : 25em;">\n                        ')
            # SOURCE LINE 39
            __M_writer(escape(elements.helpboard("""
                            <span class="fgred">All fields are mandatory.</span>
                            <dl>
                            <dt>username</dt>
                                <dd>Pick a proper username, you may not be able to
                                change it later.</dd>
                            <dt>Terms of Service</dt>
                                <dd>If `Terms of Service (tos)` it empty, prompt your
                                site-administrator to add a valid TOS content at
                                <a href="/tos">tos</a></dd>
                            </dl>
                        """)))
            # SOURCE LINE 50
            __M_writer(u'\n                    </div>\n                    </div>\n                </div>\n                </div>\n')
            # SOURCE LINE 55
        else :
            # SOURCE LINE 56
            __M_writer(u'            <div class="fgcrimson m20" style="font-size: 120%">\n                Registration is allowed only by invitation\n            </div>\n')
            pass
        # SOURCE LINE 60
        __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


