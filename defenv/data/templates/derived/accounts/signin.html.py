# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294319196.9356861
_template_filename='/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/derived/accounts/signin.html'
_template_uri='/derived/accounts/signin.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['bd_script', 'bd_body']


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
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_script(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n    ')
        # SOURCE LINE 46
        __M_writer(escape(parent.bd_script()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        dojo.addOnLoad(\n            function() { dojo.query( "input[name=username]" )[0].focus(); }\n        );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bd_body(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n    ')
        # SOURCE LINE 9

        flash = c.signinflash or ''
            
        
        # SOURCE LINE 11
        __M_writer(u'\n\n    <div id="bdy" class="mt50">\n    <div id="signin" class="brtr10 brtl10 p5">\n        <div class="p10 bgblue1 calign fntbold">\n            Sign in\n            <div class="fgred calign" style="margin-left: 50px;">')
        # SOURCE LINE 17
        __M_writer(escape(flash))
        __M_writer(u'</div>\n        </div>\n        <form action="%s" method="post">\n        <div class="w100 form">\n            <div class="field">\n                <div class="label" style="width : 8em;">Username :</div>\n                <div class="ftbox">\n                    <input name="username" type="text"/></div>\n            </div>\n            <div class="field">\n                <div class="label" style="width : 8em;">Password :</div>\n                <div class="ftbox">\n                    <input name="password" type="password"/></div>\n            </div>\n            <div class="field w100">\n                <div class="label" style="width : 8em;"></div>\n                <div class="fsubmit">\n                    <input name="authform" value="Sign In" type="submit"/>\n                    <a class="ml10" href="')
        # SOURCE LINE 35
        __M_writer(escape(h.url_forgotpass))
        __M_writer(u'">forgot-password</a>\n                </div>\n            </div>\n        </div>\n        </form>\n        <br/>\n    </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


