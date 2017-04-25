# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294317210.608582
_template_filename=u'/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/component/forms.html'
_template_uri=u'/component/forms.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['form_attachssummary', 'form_createrev', 'form_tckparent', 'form_updatetcmt', 'form_addattachs', 'form_tcksummary', 'form_systeminfo', 'form_delsw_h', 'form_tckpromptuser', 'form_addparts', 'form_configticket', 'form_revwfav', 'form_del_userpermissions', 'form_rmver', 'form_addtckfilter', 'input_text', 'form_revwauthor', 'input_password', 'form_vcsfile2wiki', 'form_updatever', 'form_editsw', 'input_checkbox', 'form_createwcmt', 'input_hidden', 'form_createpcomp', 'form_project_disable', 'form_updaterset', 'multiselect', 'select_revwnature', 'form_deltckfilter', 'form_rmmstn', 'form_delteamperms', 'form_wikifav', 'form_addtorset', 'form_deletemount_e', 'form_addprjperms', 'form_selectticket', 'form_configsw', 'form_rmpcomp', 'form_configtst', 'form_wikitype', 'label', 'form_creatercmt', 'form_configvcs', 'form_updatemount', 'form_updatepcomp', 'form_tckversion', 'input_radio', 'form_updatepg', 'form_selectsavfilter', 'form_approve_userrelations', 'input_button', 'form_wikicontent', 'form_addprjteam', 'form_user_disable', 'form_deletemount', 'form_createproject', 'form_wikisummary', 'form_inviteuser', 'form_delprjperms', 'form_selectwikipage', 'fieldhelp', 'form_selectfilerevision', 'form_sitelogo', 'form_updatemstn', 'form_createmstn', 'form_project_enable', 'select', 'input_submit', 'form_wikisourceurl', 'form_tckblockedby', 'form_tckseverity', 'form_updatelicense', 'form_projfav', 'form_projectinfo', 'form_tckblocking', 'form_selectwikiversion', 'form_updatewcmt', 'form_selectrevw', 'form_createpg', 'form_removelic_h', 'form_configrev', 'form_createmount_e', 'form_selectrset', 'form_createticket', 'form_selectvcs', 'form_licenselist', 'form_addteamperms', 'textarea', 'form_attachstags', 'form_votewiki', 'form_tckdescription', 'form_searchbox', 'form_delparts', 'form_edittck', 'form_userreg', 'form_tckcomponent', 'form_user_enable', 'form_delprjteam', 'form_systemconfig', 'form_tckfav', 'form_createlicense', 'form_tcktype', 'form_updtpass', 'form_tckmilestone', 'form_search', 'form_forgotpass', 'form_createrset', 'form_createtcmt', 'form_integratevcs', 'form_delfromrset', 'form_createver', 'form_closerev', 'form_configwiki', 'form_del_userrelations', 'form_votetck', 'input_file', 'form_wikidiff', 'form_createmount', 'form_replyrcmt', 'form_revwmoderator', 'form_replywcmt', 'form_replytcmt', 'form_resetpass', 'form_changetckst', 'input_image', 'form_configwiki_h', 'form_add_userrelations', 'select_revwaction', 'form_accountinfo', 'form_processrcmt', 'input_reset', 'form_deletevcs', 'form_add_userpermissions']


# SOURCE LINE 17

restrict_kwargs = lambda kwargs, allowed_keys : \
                        [ kwargs.pop( k ) for k in kwargs.keys() if k not in allowed_keys ]
make_attrs      = lambda kwargs : ' '.join([ k + '="'+kwargs[k]+'"' for k in kwargs ])
general_attrs     = [ 'name', 'value', 'id', 'class', 'title', 'style' ]
inputtext_attrs   = general_attrs + [ 'disabled', 'maxlength', 'readonly', 'size' ]
inputpass_attrs   = general_attrs + [ 'disabled', 'maxlength', 'size' ]
inputchkbox_attrs = general_attrs + [ 'checked', 'disabled' ]
inputradio_attrs  = general_attrs + [ 'checked', 'disabled' ]
inputfile_attrs   = general_attrs + [ 'disabled', 'size' ]
inputbutton_attrs = general_attrs
inputhidden_attrs = general_attrs
inputimage_attrs  = general_attrs + [ 'alt', 'disabled', 'src', 'value' ]
textarea_attrs    = general_attrs + [ 'rows', 'cols', 'disabled', 'readonly', 'tatype' ]
select_attrs      = general_attrs + [ 'multiple', 'size', 'disabled' ]
multiselect_attrs = general_attrs + [ 'size', 'disabled' ]

label_attrs       = [ 'for' ]

# System tables entry fields classified into `info` or `config`
infofields = [ 'product_name', 'product_version','database_version',
               'envpath', 
               'sitename', 'siteadmin', 'timezone', 'unicode_encoding'
             ]
cnffields  = [ 'welcomestring', 'specialtags', 'projteamtypes',
               'tickettypes', 'ticketseverity', 'ticketstatus', 'ticketresolv', 
               'wikitypes', 'def_wikitype', 'reviewactions', 'reviewnatures',
               'vcstypes',  'googlemaps', 'strictauth',
               'regrbyinvite', 'invitebyall', 'interzeta', 'userrel_types', 
             ]


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 15
    ns = runtime.Namespace(u'elements', context._clean_inheritance_tokens(), templateuri=u'/component/elements.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'elements')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 13
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 61
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 78
        __M_writer(u'\n')
        # SOURCE LINE 86
        __M_writer(u'\n')
        # SOURCE LINE 93
        __M_writer(u'\n')
        # SOURCE LINE 100
        __M_writer(u'\n')
        # SOURCE LINE 107
        __M_writer(u'\n')
        # SOURCE LINE 114
        __M_writer(u'\n')
        # SOURCE LINE 121
        __M_writer(u'\n')
        # SOURCE LINE 128
        __M_writer(u'\n\n')
        # SOURCE LINE 137
        __M_writer(u'\n\n')
        # SOURCE LINE 161
        __M_writer(u'\n\n')
        # SOURCE LINE 187
        __M_writer(u'\n\n')
        # SOURCE LINE 191
        __M_writer(u'\n\n')
        # SOURCE LINE 195
        __M_writer(u'\n\n')
        # SOURCE LINE 198
        __M_writer(u'\n')
        # SOURCE LINE 233
        __M_writer(u'\n\n')
        # SOURCE LINE 344
        __M_writer(u'\n\n')
        # SOURCE LINE 426
        __M_writer(u'\n\n')
        # SOURCE LINE 442
        __M_writer(u'\n\n')
        # SOURCE LINE 473
        __M_writer(u'\n\n')
        # SOURCE LINE 476
        __M_writer(u'\n')
        # SOURCE LINE 521
        __M_writer(u'\n\n')
        # SOURCE LINE 607
        __M_writer(u'\n\n')
        # SOURCE LINE 610
        __M_writer(u'\n')
        # SOURCE LINE 714
        __M_writer(u'\n\n')
        # SOURCE LINE 819
        __M_writer(u'\n\n')
        # SOURCE LINE 875
        __M_writer(u'\n\n')
        # SOURCE LINE 900
        __M_writer(u'\n\n')
        # SOURCE LINE 911
        __M_writer(u'\n\n')
        # SOURCE LINE 935
        __M_writer(u'\n\n')
        # SOURCE LINE 968
        __M_writer(u'\n\n')
        # SOURCE LINE 1001
        __M_writer(u'\n\n')
        # SOURCE LINE 1033
        __M_writer(u'\n\n')
        # SOURCE LINE 1065
        __M_writer(u'\n\n')
        # SOURCE LINE 1110
        __M_writer(u'\n\n')
        # SOURCE LINE 1155
        __M_writer(u'\n\n')
        # SOURCE LINE 1168
        __M_writer(u'\n\n')
        # SOURCE LINE 1185
        __M_writer(u'\n\n')
        # SOURCE LINE 1242
        __M_writer(u'\n\n\n')
        # SOURCE LINE 1246
        __M_writer(u'\n')
        # SOURCE LINE 1255
        __M_writer(u'\n\n')
        # SOURCE LINE 1328
        __M_writer(u'\n\n')
        # SOURCE LINE 1407
        __M_writer(u'\n\n')
        # SOURCE LINE 1437
        __M_writer(u'\n\n')
        # SOURCE LINE 1440
        __M_writer(u'\n')
        # SOURCE LINE 1539
        __M_writer(u'\n\n')
        # SOURCE LINE 1658
        __M_writer(u'\n\n')
        # SOURCE LINE 1728
        __M_writer(u'\n\n')
        # SOURCE LINE 1804
        __M_writer(u'\n\n')
        # SOURCE LINE 1839
        __M_writer(u'\n\n')
        # SOURCE LINE 1905
        __M_writer(u'\n\n')
        # SOURCE LINE 2000
        __M_writer(u'\n\n')
        # SOURCE LINE 2035
        __M_writer(u'\n\n')
        # SOURCE LINE 2094
        __M_writer(u'\n\n')
        # SOURCE LINE 2158
        __M_writer(u'\n\n')
        # SOURCE LINE 2193
        __M_writer(u'\n\n')
        # SOURCE LINE 2239
        __M_writer(u'\n\n')
        # SOURCE LINE 2285
        __M_writer(u'\n\n')
        # SOURCE LINE 2328
        __M_writer(u'\n\n')
        # SOURCE LINE 2371
        __M_writer(u'\n\n')
        # SOURCE LINE 2418
        __M_writer(u'\n\n')
        # SOURCE LINE 2465
        __M_writer(u'\n\n')
        # SOURCE LINE 2485
        __M_writer(u'\n\n')
        # SOURCE LINE 2488
        __M_writer(u'\n')
        # SOURCE LINE 2498
        __M_writer(u'\n\n')
        # SOURCE LINE 2642
        __M_writer(u'\n\n')
        # SOURCE LINE 2757
        __M_writer(u'\n\n')
        # SOURCE LINE 2772
        __M_writer(u'\n\n')
        # SOURCE LINE 2781
        __M_writer(u'\n\n')
        # SOURCE LINE 2790
        __M_writer(u'\n\n')
        # SOURCE LINE 2799
        __M_writer(u'\n\n')
        # SOURCE LINE 2808
        __M_writer(u'\n\n')
        # SOURCE LINE 2817
        __M_writer(u'\n\n')
        # SOURCE LINE 2826
        __M_writer(u'\n\n')
        # SOURCE LINE 2835
        __M_writer(u'\n\n')
        # SOURCE LINE 2844
        __M_writer(u'\n\n')
        # SOURCE LINE 2853
        __M_writer(u'\n\n')
        # SOURCE LINE 2862
        __M_writer(u'\n\n')
        # SOURCE LINE 2873
        __M_writer(u'\n\n')
        # SOURCE LINE 2909
        __M_writer(u'\n\n')
        # SOURCE LINE 2921
        __M_writer(u'\n\n')
        # SOURCE LINE 2937
        __M_writer(u'\n\n')
        # SOURCE LINE 2954
        __M_writer(u'\n\n')
        # SOURCE LINE 2971
        __M_writer(u'\n\n')
        # SOURCE LINE 2992
        __M_writer(u'\n\n')
        # SOURCE LINE 3016
        __M_writer(u'\n\n')
        # SOURCE LINE 3051
        __M_writer(u'\n\n')
        # SOURCE LINE 3069
        __M_writer(u'\n\n')
        # SOURCE LINE 3080
        __M_writer(u'\n\n')
        # SOURCE LINE 3086
        __M_writer(u'\n\n')
        # SOURCE LINE 3091
        __M_writer(u'\n\n')
        # SOURCE LINE 3102
        __M_writer(u'\n\n')
        # SOURCE LINE 3113
        __M_writer(u'\n\n')
        # SOURCE LINE 3214
        __M_writer(u'\n\n\n')
        # SOURCE LINE 3227
        __M_writer(u'\n\n')
        # SOURCE LINE 3259
        __M_writer(u'\n\n')
        # SOURCE LINE 3292
        __M_writer(u'\n\n')
        # SOURCE LINE 3323
        __M_writer(u'\n\n')
        # SOURCE LINE 3356
        __M_writer(u'\n\n')
        # SOURCE LINE 3379
        __M_writer(u'\n\n')
        # SOURCE LINE 3402
        __M_writer(u'\n\n')
        # SOURCE LINE 3457
        __M_writer(u'\n\n')
        # SOURCE LINE 3492
        __M_writer(u'\n\n')
        # SOURCE LINE 3504
        __M_writer(u'\n\n')
        # SOURCE LINE 3535
        __M_writer(u'\n\n')
        # SOURCE LINE 3567
        __M_writer(u'\n\n')
        # SOURCE LINE 3598
        __M_writer(u'\n\n')
        # SOURCE LINE 3629
        __M_writer(u'\n\n')
        # SOURCE LINE 3641
        __M_writer(u'\n\n')
        # SOURCE LINE 3649
        __M_writer(u'\n\n')
        # SOURCE LINE 3692
        __M_writer(u'\n\n')
        # SOURCE LINE 3703
        __M_writer(u'\n\n')
        # SOURCE LINE 3711
        __M_writer(u'\n\n')
        # SOURCE LINE 3741
        __M_writer(u'\n\n')
        # SOURCE LINE 3774
        __M_writer(u'\n\n')
        # SOURCE LINE 3786
        __M_writer(u'\n\n')
        # SOURCE LINE 3821
        __M_writer(u'\n\n')
        # SOURCE LINE 3834
        __M_writer(u'\n\n')
        # SOURCE LINE 3883
        __M_writer(u'\n\n')
        # SOURCE LINE 3886
        __M_writer(u'\n')
        # SOURCE LINE 3897
        __M_writer(u'\n\n')
        # SOURCE LINE 3904
        __M_writer(u'\n\n\n')
        # SOURCE LINE 3920
        __M_writer(u'\n\n')
        # SOURCE LINE 3937
        __M_writer(u'\n\n')
        # SOURCE LINE 3954
        __M_writer(u'\n\n')
        # SOURCE LINE 4002
        __M_writer(u'\n\n')
        # SOURCE LINE 4029
        __M_writer(u'\n\n')
        # SOURCE LINE 4096
        __M_writer(u'\n\n')
        # SOURCE LINE 4112
        __M_writer(u'\n\n')
        # SOURCE LINE 4129
        __M_writer(u'\n\n')
        # SOURCE LINE 4146
        __M_writer(u'\n\n')
        # SOURCE LINE 4180
        __M_writer(u'\n\n')
        # SOURCE LINE 4202
        __M_writer(u'\n\n')
        # SOURCE LINE 4226
        __M_writer(u'\n\n')
        # SOURCE LINE 4229
        __M_writer(u'\n')
        # SOURCE LINE 4240
        __M_writer(u'\n\n')
        # SOURCE LINE 4287
        __M_writer(u'\n\n\n')
        # SOURCE LINE 4291
        __M_writer(u'\n')
        # SOURCE LINE 4314
        __M_writer(u'\n\n')
        # SOURCE LINE 4322
        __M_writer(u'\n\n')
        # SOURCE LINE 4330
        __M_writer(u'\n\n')
        # SOURCE LINE 4348
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_attachssummary(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4316
        __M_writer(u'\n    <form id="attachssummary" action="')
        # SOURCE LINE 4317
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4318
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4319
        __M_writer(escape(input_hidden( name='attachment_id' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4320
        __M_writer(escape(input_hidden( name='summary' )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createrev(context,u,p,rsets,action,projusers,usernames,forsrc=[],forversion=None):
    context.caller_stack._push_frame()
    try:
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3116
        __M_writer(u'\n    ')
        # SOURCE LINE 3117

        ru_help = 'enter the resource url to be reviewed. ' + \
                  '<a href="/help/review#Specifying%20resource">Learn more</a>'
        rv_help = 'version to review'
        ra_help = 'author should take action on review comments'
        rsets   = [ [ '', '--Select-ReviewSet--' ] ] + rsets
            
        
        # SOURCE LINE 3123
        __M_writer(u'\n\n    <form id="createrev" action="')
        # SOURCE LINE 3125
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3126
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3127
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3128
        __M_writer(escape(input_hidden( name='moderator', value=str(u.username))))
        __M_writer(u'\n    <div class="form">\n        <div class="field">\n            <div class="label" style="width : 12em;">Review Set :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 3133
        __M_writer(escape(select( name='rset_id', id='rset_id', options=rsets )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Resource Url :</div>\n')
        # SOURCE LINE 3138
        if forsrc == [] :
            # SOURCE LINE 3139
            __M_writer(u'                <div class="ftbox" required="true">\n                    ')
            # SOURCE LINE 3140
            __M_writer(escape(input_text( name='resource_url', id='resource_url',
                                  style='width : 30em;' )))
            # SOURCE LINE 3141
            __M_writer(u'\n                    <br/>\n                    ')
            # SOURCE LINE 3143
            __M_writer(escape(fieldhelp( ru_help )))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 3146
        for rurl in forsrc :
            # SOURCE LINE 3147
            __M_writer(u'                <div>\n                ')
            # SOURCE LINE 3148
            __M_writer(escape(input_text( name='resource_url', value=rurl,
                              readonly='readonly', size='40' )))
            # SOURCE LINE 3149
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 3152
        __M_writer(u'        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Version :</div>\n')
        # SOURCE LINE 3155
        if forversion != None :
            # SOURCE LINE 3156
            __M_writer(u'                ')
            __M_writer(escape(input_text( name='version', value=str(forversion), readonly='readonly' )))
            __M_writer(u'\n')
            # SOURCE LINE 3157
        else :
            # SOURCE LINE 3158
            __M_writer(u'                <div class="ftbox" regExp="[0-9]*" required="true">\n                    ')
            # SOURCE LINE 3159
            __M_writer(escape(input_text( name='version', id='version' )))
            __M_writer(u'\n                    <br/>\n                    ')
            # SOURCE LINE 3161
            __M_writer(escape(fieldhelp( rv_help )))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 3164
        __M_writer(u'        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Author :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 3168
        __M_writer(escape(select( name='author', id='author', options=projusers,
                          opt_selected=u.username )))
        # SOURCE LINE 3169
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 3171
        __M_writer(escape(fieldhelp( ra_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Participants :</div>\n            <div class="fselect vtop">\n                ')
        # SOURCE LINE 3177
        __M_writer(escape(multiselect( name='participant', id='participant', options=usernames,
                               size="7" )))
        # SOURCE LINE 3178
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 3184
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 3185
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_createrev() {\n            function createrev_onsubmit( e ) {\n                var msg       = \'\';\n                if ( dijit.byId(\'createrev\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'author\' ), \'value\' )) {\n                        msg       = \'Provide review author !!\'\n                    }\n                    if (msg) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                        dojo.stopEvent( e );\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                    dojo.stopEvent( e );\n                }\n            }\n            new zeta.Form({ onsubmit : createrev_onsubmit, formid: \'createrev\' })\n\n            var n_rurl = dijit.byId( \'resource_url\' );\n            n_rurl ? n_rurl.focus() : null;\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckparent(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2828
        __M_writer(u'\n    <form id="tckparent" action="')
        # SOURCE LINE 2829
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2830
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2831
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2832
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2833
        __M_writer(escape(input_hidden( name='parent_id')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatetcmt(context,u,p,t,action,tcmt=None):
    context.caller_stack._push_frame()
    try:
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2956
        __M_writer(u'\n    <form id=\'updatetcmt\' action="')
        # SOURCE LINE 2957
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2958
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2959
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2960
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2961
        __M_writer(escape(input_hidden( name='ticket_comment_id', value=tcmt and str(tcmt.id) or '' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2962
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="w80">\n            ')
        # SOURCE LINE 2965
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose ticket comment.' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 2966
        __M_writer(escape(textarea( name='text', id='upcmt_text', text=tcmt and tcmt.text or '' )))
        __M_writer(u'\n        </div>\n        <div>')
        # SOURCE LINE 2968
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addattachs(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_file(**kwargs):
            return render_input_file(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4292
        __M_writer(u'\n    <form id="addattachs" enctype="multipart/form-data" action="')
        # SOURCE LINE 4293
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4294
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 8em;">File :</div>\n            <div class="ffile">\n                ')
        # SOURCE LINE 4299
        __M_writer(escape(input_file( name='attachfile', id='attachfile', style='width: 20em;' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 8em;">Summary :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 4305
        __M_writer(escape(input_text( name='summary', id="summary", style='width: 20em;' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 8em;"></div>\n            <div class="fsubmit">')
        # SOURCE LINE 4310
        __M_writer(escape(input_submit( value='Add' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tcksummary(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2855
        __M_writer(u'\n    <form id="tcksummary" action="')
        # SOURCE LINE 2856
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2857
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2858
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2859
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2860
        __M_writer(escape(input_hidden( name='summary')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_systeminfo(context,u,entries,action):
    context.caller_stack._push_frame()
    try:
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        __M_writer = context.writer()
        # SOURCE LINE 199
        __M_writer(u'\n    ')
        # SOURCE LINE 200

        help       = {
            'product_name'     : '',
            'envpath'          : '<em>Can be changed only in the .ini file</em>',
            'product_version'  : '',
            'database_version' : '',
            'sitename'         : '',
            'siteadmin'        : '',
            'timezone'         : '',
            'unicode_encoding' : '<em>-- This feature is in development --</em>',
        }
        import zwiki
            
        
        # SOURCE LINE 212
        __M_writer(u'\n\n    <div class="disptable w60 ml50" style="border-collapse: separate; border-spacing: 10px">\n')
        # SOURCE LINE 215
        for field in infofields :
            # SOURCE LINE 216
            __M_writer(u'        <div class="disptrow">\n            <div class="disptcell p3 fggray fntbold">')
            # SOURCE LINE 217
            __M_writer(escape(field))
            __M_writer(u'</div>\n            <div class="disptcell p3 fggray">\n                ')
            # SOURCE LINE 219
            __M_writer(escape(entries[field]))
            __M_writer(u'\n')
            # SOURCE LINE 220
            if help[field] : 
                # SOURCE LINE 221
                __M_writer(u'                    - ')
                __M_writer(escape(fieldhelp( help[field])))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 223
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 226
        __M_writer(u'        <div class="disptrow">\n            <div class="disptcell p3 fggray fntbold">zwiki_version</div>\n            <div class="disptcell p3 fggray">\n                ')
        # SOURCE LINE 229
        __M_writer(escape(zwiki.VERSION))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_delsw_h(context,u):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 444
        __M_writer(u'\n\n    <form id="delsw" action="" method="post">\n    ')
        # SOURCE LINE 447
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 448
        __M_writer(escape(input_hidden( name='pathurl',  id='pathurl')))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_delsw() {\n            function deletesw( n_del, n_li, e ) {\n                var i_pathurl = dojo.query( \'input#pathurl\' )[0];\n                var n_ul = n_li.parentNode;\n                i_pathurl.value = dojo.attr( n_li, \'pathurl\' );\n                dojo.attr(form_delsw, \'action\', dojo.attr( n_li, \'suburldel\' ));\n                submitform( form_delsw, e );\n                n_ul.removeChild( n_li );\n            }\n            dojo.query( \'span[name=delsw]\' ).forEach(\n                function( n ) {\n                    dojo.connect(\n                        n, \'onclick\', \n                        dojo.partial( deletesw, n, n.parentNode )\n                    );\n              }\n            );\n            new zeta.Form({ onsubmit : null, formid : \'delsw\' });\n        }\n        dojo.addOnLoad( initform_delsw );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckpromptuser(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2792
        __M_writer(u'\n    <form id="tckpromptuser" action="')
        # SOURCE LINE 2793
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2794
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2795
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2796
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2797
        __M_writer(escape(input_hidden( name='promptuser')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addparts(context,u,p,r,action,usernames):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3325
        __M_writer(u'\n    ')
        # SOURCE LINE 3326

        usernames = [ '--Add--' ] + usernames 
        default   = '--Add--'
            
        
        # SOURCE LINE 3329
        __M_writer(u'\n    <form id="addparts" action="')
        # SOURCE LINE 3330
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3331
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3332
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3333
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3334
        __M_writer(escape(select( name='participant', id='participant', options=usernames, opt_selected=default )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_addparts() {\n            new zeta.Form({ formid: \'addparts\' });\n            var n_select = dojo.query( \'select[name=participant]\', form_addparts )[0];\n            // Submit the form on selecting a user.\n            dojo.connect(\n                n_select, \'onchange\',\n                function( e ) {\n                    var n_select = e.currentTarget;\n                    var sr_str = \'select[name=participant] option[value=\'+n_select.value+\']\';\n                    var n_opt  = dojo.query( sr_str, form_addparts )[0];\n                    submitform( form_addparts, e );\n                    dojo.stopEvent( e );\n                    dojo.publish( \'insertparticipant\', [ n_select.value ] );\n                    n_select.removeChild( n_opt );\n                }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configticket(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2759
        __M_writer(u'\n    <form id="configtck" action="')
        # SOURCE LINE 2760
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2761
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2762
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2763
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2764
        __M_writer(escape(input_hidden( name='tck_typename')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2765
        __M_writer(escape(input_hidden( name='tck_severityname')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2766
        __M_writer(escape(input_hidden( name='promptuser')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2767
        __M_writer(escape(input_hidden( name='component_id')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2768
        __M_writer(escape(input_hidden( name='milestone_id')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2769
        __M_writer(escape(input_hidden( name='version_id')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2770
        __M_writer(escape(input_hidden( name='summary')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_revwfav(context,u,p,r,action,name):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3381
        __M_writer(u'\n    <form id=\'revwfav\' class="dispnone" action="')
        # SOURCE LINE 3382
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3383
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3384
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3385
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3386
        __M_writer(escape(input_hidden( name=name, value=str(u.username))))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        /* Setup favorite review for user */\n        function initform_revwfav() {\n            var n_span  = dojo.query( "span[name=favrevw]" )[0];\n            var w_form  = new zeta.Form({ normalsub: true, formid: \'revwfav\' });\n            var n_field = dojo.query( "input[name=')
        # SOURCE LINE 3394
        __M_writer(escape(name))
        __M_writer(u']", form_revwfav )[0];\n            if( n_span && n_field ) {\n                new ZFavorite( n_span, form_revwfav, n_field );\n            }\n        }\n        dojo.addOnLoad( initform_revwfav );\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_del_userpermissions(context,u,usernames,action,defuser,pgroups):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1112
        __M_writer(u'\n    <form id="deluserperms" action="')
        # SOURCE LINE 1113
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1114
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 1118
        __M_writer(escape(elements.iconize( 'User :', 'user' )))
        __M_writer(u'</div>\n            <div class="fselect vtop"  required="true">\n                ')
        # SOURCE LINE 1120
        __M_writer(escape(select( name='username', id='delfromuser', options=usernames, \
                          opt_selected=defuser, style='width : 15em' )))
        # SOURCE LINE 1121
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 7em;">Permissions :</div>\n            <div class="fselect vtop"  required="true">\n                ')
        # SOURCE LINE 1127
        __M_writer(escape(multiselect( name='perm_group', id='del_perm_group', options=pgroups, \
                               size="7", style='width : 15em' )))
        # SOURCE LINE 1128
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 1129
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Initialise deluserperms form */\n        function initform_deluserperms( e ) {\n            seluser_delpg  = dojo.query( \'form#deluserperms select#delfromuser\' )[0];\n            selpg_fromuser = dojo.query( \'form#deluserperms select#del_perm_group\' )[0];\n            new ZSelect( seluser_delpg, null, function( e ) { refresh_userperms() } );\n            new ZSelect( selpg_fromuser, \'deluserpg\', null );\n\n            function deluserperms_onsubmit( e ) {\n                submitform( form_deluserperms, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                userperms.store.close();\n                userperms.fetch({\n                    onComplete : userperms_oncomplete,\n                    sort       : [{ attribute : \'username\' }]\n                });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : deluserperms_onsubmit, formid : \'deluserperms\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_rmver(context,u,p,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2160
        __M_writer(u'\n    <form id="rmver" action="')
        # SOURCE LINE 2161
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2162
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2163
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;"></div>\n            <div class="ftarea">\n                ')
        # SOURCE LINE 2168
        __M_writer(escape(multiselect( name='version_id',  id='version_id', options=[],
                               size='4', style='width : 20em;' )))
        # SOURCE LINE 2169
        __M_writer(u'\n                <div>')
        # SOURCE LINE 2170
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Setup version removal */\n        function initform_rmver() {\n            var selver_rmver= dojo.query( \'form#rmver select#version_id\' )[0];\n            new ZSelect( selver_rmver, \'rmver\', null )\n            function rmver_onsubmit( e ) {\n                submitform( form_rmver, e );\n                verlist.store.close();\n                verlist.fetch({\n                    onComplete : verlist_oncomplete,\n                    sort : [ { attribute : \'version_name\' } ]\n                });\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: rmver_onsubmit, formid : \'rmver\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addtckfilter(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3018
        __M_writer(u'\n    <form id="addtckfilter" action="')
        # SOURCE LINE 3019
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3020
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3021
        __M_writer(escape(input_hidden( id='filterbyjson', name='filterbyjson' )))
        __M_writer(u'\n    <div class="pt10">\n        ')
        # SOURCE LINE 3023
        __M_writer(escape(input_text( id='filtername', name='name',
                      style='width: 10em; color: #D6D6D6;', value='Save-This-Filter' )))
        # SOURCE LINE 3024
        __M_writer(u'\n    </div>\n    </form>\n    <script type="text/javascript">\n        function addtckfilter_onsubmit( e ) {\n            var name    = dojo.attr( dojo.byId( \'filtername\' ), \'value\' );\n            var n_fjson = dojo.byId( \'filterbyjson\' );\n            var valpatt = /^[a-zA-Z]+[a-zA-Z0-9]*$/;\n            dojo.attr( n_fjson, \'value\', dojo.toJson(customquery()) );\n            if( name && n_fjson && valpatt.test( name ) ) {\n                submitform( form_addtckfilter, e );\n            } else {\n                dojo.publish( \'flash\', [ \'error\', "Invalid name", 2000 ]);\n            }\n            dojo.stopEvent( e );\n        }\n        function initform_addtckfilter() {\n            new zeta.Form({ onsubmit: addtckfilter_onsubmit,\n                            formid: \'addtckfilter\' })\n            dojo.connect( dojo.byId( \'filtername\' ), \'onfocus\',\n                function(e) {\n                    dojo.attr( e.target, \'value\', \'\' );\n                    dojo.style( e.target, { color : \'black\' });\n                }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_text(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n    ')
        # SOURCE LINE 50

        classes = kwargs.pop( 'classes', '' )
        text = kwargs.pop( 'text', '' )
        restrict_kwargs( kwargs, inputtext_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 56
        if text :
            # SOURCE LINE 57
            __M_writer(u'        <input type="text" class="')
            __M_writer(escape(classes))
            __M_writer(u'" ')
            __M_writer(attrs )
            __M_writer(u'>')
            __M_writer(escape(text))
            __M_writer(u'</input>\n')
            # SOURCE LINE 58
        else :
            # SOURCE LINE 59
            __M_writer(u'        <input type="text" class="')
            __M_writer(escape(classes))
            __M_writer(u'" ')
            __M_writer(attrs )
            __M_writer(u'/>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_revwauthor(context,u,p,r,action,projusers):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3229
        __M_writer(u'\n    ')
        # SOURCE LINE 3230

        projusers = [ [ '', '--Select-Author--' ] ] + projusers
        if not r.author :
            default   = '--Select-Author--'
        elif r.author.username not in projusers :
            default   = '--Select-Author--'
        else :
            default   = r.author.username
            
        
        # SOURCE LINE 3238
        __M_writer(u'\n    <form class="dispnone" id="revwauthor" action="')
        # SOURCE LINE 3239
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3240
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3241
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3242
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3243
        __M_writer(escape(select( name='author', id='author', options=projusers, opt_selected=default )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_revwauthor() {\n            new zeta.Form({ formid: \'revwauthor\' });\n            var n_select = dojo.query( \'select[name=author]\', form_revwauthor )[0];\n            // Submit the form on selecting the author\n            dojo.connect( n_select, \'onchange\',\n                          function( e ) {\n                              submitform( form_revwauthor, e );\n                              dojo.stopEvent( e );\n                          }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_password(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\n    ')
        # SOURCE LINE 64

        restrict_kwargs( kwargs, inputpass_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 67
        __M_writer(u'\n    <input type="password" ')
        # SOURCE LINE 68
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_vcsfile2wiki(context,u,p,sourceurl,action):
    context.caller_stack._push_frame()
    try:
        def input_radio(**kwargs):
            return render_input_radio(context,**kwargs)
        h = context.get('h', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3836
        __M_writer(u'\n    <form id="vcsfile2wiki" action="')
        # SOURCE LINE 3837
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3838
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3839
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3840
        __M_writer(escape(input_hidden( name='sourceurl', id='sourceurl', value=str(p.id) )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="ftbox"  required="true">\n                <span class="fntbold fggray">Wiki pagename :</span>\n                ')
        # SOURCE LINE 3845
        __M_writer(escape(input_text( name='pagename', id='pagename', value='' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="fradio dispinln">\n                ')
        # SOURCE LINE 3850
        __M_writer(escape(input_radio( name='status', id='cntstatus1',
                               value=h.WIKITYPE_HTML, text=h.WIKITYPE_HTML )))
        # SOURCE LINE 3851
        __M_writer(u'\n                ')
        # SOURCE LINE 3852
        __M_writer(escape(input_radio( name='status', id='cntstatus2',
                               value=h.WIKITYPE_ZWIKI, text=h.WIKITYPE_ZWIKI )))
        # SOURCE LINE 3853
        __M_writer(u'\n                ')
        # SOURCE LINE 3854
        __M_writer(escape(input_radio( name='status', id='cntstatus3',
                               value=h.WIKITYPE_TEXT, text=h.WIKITYPE_TEXT )))
        # SOURCE LINE 3855
        __M_writer(u'\n            </div>\n            <span class="ml10">')
        # SOURCE LINE 3857
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</span>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function vf2wiki_onsubmit( e ) {\n            var cnttype = \'')
        # SOURCE LINE 3864
        __M_writer(h.WIKITYPE_TEXT )
        __M_writer(u"';\n            var i_srcurl = dojo.byId('sourceurl');\n            var i_pgname = dojo.byId('pagename');\n            dojo.stopEvent( e );\n            if(! i_pgname.value ) {\n                dojo.publish( 'flash', [ 'error', 'Provide wiki pagename', 2000 ]);\n            }\n            if( dijit.byId( 'cntstatus1' ).checked ) {\n                cnttype = '")
        # SOURCE LINE 3872
        __M_writer(h.WIKITYPE_HTML )
        __M_writer(u"';\n            } else if( dijit.byId( 'cntstatus2' ).checked ) {\n                cnttype = '")
        # SOURCE LINE 3874
        __M_writer(h.WIKITYPE_ZWIKI )
        __M_writer(u"';\n            }\n            i_srcurl.value = '")
        # SOURCE LINE 3876
        __M_writer(sourceurl )
        __M_writer(u"' + '&cnttype=' + cnttype;\n            submitform( form_vcsfile2wiki, e );\n        }\n        function initform_vcsfile2wiki() {\n            new zeta.Form({ formid: 'vcsfile2wiki', onsubmit: vf2wiki_onsubmit });\n        }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatever(context,u,p,verlist,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2096
        __M_writer(u'\n    ')
        # SOURCE LINE 2097

        vn_help = 'version name must be unique'
            
        
        # SOURCE LINE 2099
        __M_writer(u'\n\n    <div class="w100 mb10">\n        ')
        # SOURCE LINE 2102
        __M_writer(escape(select( name='updtver', id='updtver', options=verlist )))
        __M_writer(u'\n        <hr/>\n    </div>\n    <form id="updatever" action="')
        # SOURCE LINE 2105
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2106
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2107
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2108
        __M_writer(escape(input_hidden( name='version_id', value='' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Version name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 2113
        __M_writer(escape(input_text( name='version_name', id='updtvername' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2115
        __M_writer(escape(fieldhelp( vn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 2121
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose version description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 2122
        __M_writer(escape(textarea( name='description', id='updtverdesc', cols='50',
                            style='width : 25em' )))
        # SOURCE LINE 2123
        __M_writer(u'\n                <div>')
        # SOURCE LINE 2124
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_updatever() {\n            /* Setup version detail update */\n            function updatever_onsubmit( e ) {\n                var msg = \'\'\n                if ( dijit.byId(\'updatever\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'updtverdesc\' ), \'value\' )) {\n                        msg = \'Provide version description !!\'\n                    }\n\n                    if ( msg ) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                    } else {\n                        submitform( form_updatever, e);\n                        verlist.store.close();\n                        verlist.fetch({\n                            onComplete : verlist_oncomplete,\n                            sort : [ { attribute : \'version_name\' } ]\n                        });\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                }\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: updatever_onsubmit, formid : \'updatever\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_editsw(context,u,sw,typenames,action,url_swpage):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        h = context.get('h', UNDEFINED)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        def input_button(**kwargs):
            return render_input_button(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 346
        __M_writer(u'\n    ')
        # SOURCE LINE 347

        swtype = sw.type.wiki_typename
        sourceurl = sw.sourceurl or ''
        
        
        # SOURCE LINE 350
        __M_writer(u'\n    <form id=\'editsw\' action="')
        # SOURCE LINE 351
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 352
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 353
        __M_writer(escape(input_hidden( name='pathurl', value=sw.path )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="">Source url :</div>\n            <div class="ftbox" style="">\n                ')
        # SOURCE LINE 358
        __M_writer(escape(input_text( name='sourceurl', id='sourceurl', value=sourceurl,
                              style='width: 30em;')))
        # SOURCE LINE 359
        __M_writer(u'\n            </div>\n        </div>\n\n        <div class="field">\n            <div class="label" style="">Type :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 366
        __M_writer(escape(select( name='wiki_typename', id='wiki_typename', options=typenames,
                          opt_selected=swtype, style='width : 10em' )))
        # SOURCE LINE 367
        __M_writer(u'\n            </div>\n        </div>\n\n        <div class="field">\n            <div class="label" style=""></div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 374
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose guest wiki page.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 375
        __M_writer(escape(textarea( name='text', tatype="simpletextarea", id='swtext',
                            text=sw.text, cols='90', rows='30' )))
        # SOURCE LINE 376
        __M_writer(u'\n            </div>\n        </div>\n\n        <div class="field">\n            <div class="label" style=""></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 383
        __M_writer(escape(input_submit( value='Save & Continue' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 384
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 385
        __M_writer(escape(input_button( id='preview', value='Preview' )))
        __M_writer(u'\n                <a href="')
        # SOURCE LINE 386
        __M_writer(escape(url_swpage))
        __M_writer(u'">Goto-page</a>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function onpreview( x_form, e ) {\n            var div_wp  = dojo.query( \'.swpreview\' )[0];\n            var ta_wcnt = dijit.byId( \'swtext\' )\n            if ( e.type == \'keyup\' && e.keyCode != dojo.keys.ENTER ) {\n                return;\n            }\n            if ( div_wp && ta_wcnt ) {\n                div_wp.innerHTML = \'\'\n                xhrpost_obj( \'')
        # SOURCE LINE 401
        __M_writer(h.url_swpreview )
        __M_writer(u"',\n                             { 'text' : ta_wcnt.attr( 'value' ) },\n                             'text',\n                             false,\n                             null,\n                             function( resp ) {\n                                    dojo.toggleClass( div_wp.parentNode.parentNode, 'dispnone', false );\n                                    div_wp.innerHTML = resp;\n                             },\n                             null\n                          );\n                dojo.stopEvent( e );\n            }\n        }\n        function initform_editsw() {\n            new zeta.Form({ normalsub: true, formid: 'editsw' });\n            dijit.byId( 'swtext' ).focus();\n\n            // Show preview\n            var x_form = dijit.byId( 'editsw' );\n            var butt_preview = dojo.query( '#preview', x_form.domNode )[0];\n            dojo.connect( butt_preview, 'onclick', dojo.hitch( null, onpreview, x_form ));\n            dojo.connect( butt_preview, 'onkeyup', dojo.hitch( null, onpreview, x_form ));\n        }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_checkbox(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n    ')
        # SOURCE LINE 72

        text = kwargs.pop( 'text', '' )
        restrict_kwargs( kwargs, inputchkbox_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 76
        __M_writer(u'\n    <input type="checkbox" ')
        # SOURCE LINE 77
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createwcmt(context,u,w,action):
    context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4098
        __M_writer(u'\n    <form id=\'createwcmt\' action="')
        # SOURCE LINE 4099
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4100
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4101
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4102
        __M_writer(escape(input_hidden( name='version_id', value=str(w.latest_version) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4103
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="w80">\n            ')
        # SOURCE LINE 4106
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose wiki comment.' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 4107
        __M_writer(escape(textarea( name='text', id='crwcmt_text' )))
        __M_writer(u'\n        </div>\n        <div>')
        # SOURCE LINE 4109
        __M_writer(escape(input_submit( value='Add' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_hidden(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 115
        __M_writer(u'\n    ')
        # SOURCE LINE 116

        restrict_kwargs( kwargs, inputhidden_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 119
        __M_writer(u'\n    <input type="hidden" ')
        # SOURCE LINE 120
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createpcomp(context,u,p,pusers,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1660
        __M_writer(u'\n    ')
        # SOURCE LINE 1661

        cn_help = 'Component name must be unique'
            
        
        # SOURCE LINE 1663
        __M_writer(u'\n\n    <form id="createpcomp" action="')
        # SOURCE LINE 1665
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1666
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1667
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Component name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1672
        __M_writer(escape(input_text( name='componentname', id='crcompname' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1674
        __M_writer(escape(fieldhelp( cn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Owner :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 1680
        __M_writer(escape(select( name='owner',  id='crowner', options=pusers )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1686
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose component description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1687
        __M_writer(escape(textarea( name='description', id='crcompdesc', rows='1', cols='50',
                            style='width : 25em' )))
        # SOURCE LINE 1688
        __M_writer(u'\n                <div>')
        # SOURCE LINE 1689
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_createpcomp() {\n            var select_puser = dojo.query( \'form#createpcomp select#crowner\' )[0];\n            new ZSelect( select_puser, \'projusers\', null );\n\n            function createpcomp_onsubmit( e ) {\n                var msg = \'\'\n                if ( dijit.byId(\'createpcomp\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'crowner\' ), \'value\' )) {\n                        msg = \'Provide component owner !!\'\n                    }\n                    if (! dojo.attr( dojo.byId( \'crcompdesc\' ), \'value\' )) {\n                        msg = \'Provide component description !!\'\n                    }\n\n                    if ( msg ) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                    } else {\n                        submitform( form_createpcomp, e);\n                        pcomplist.store.close();\n                        pcomplist.fetch({\n                            onComplete : pcomplist_oncomplete,\n                            sort : [ { attribute : \'componentname\' } ]\n                        })\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                }\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: createpcomp_onsubmit, formid : \'createpcomp\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_project_disable(context,u,action,eprojects):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1035
        __M_writer(u'\n    <form id="prjdis" action="')
        # SOURCE LINE 1036
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1037
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 1041
        __M_writer(escape(elements.iconize( 'Projects :', 'projects' )))
        __M_writer(u'</div>\n            <div class="fselect vtop" style="width : 20em;">\n                ')
        # SOURCE LINE 1043
        __M_writer(escape(multiselect( name='disable_project', id='disable_project', options=eprojects,
                               size='7', style='width : 10em;' )))
        # SOURCE LINE 1044
        __M_writer(u'</div>\n            <div class="fsubmit ml10">')
        # SOURCE LINE 1045
        __M_writer(escape(input_submit( value='Disable' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Initialise prjdis form */\n        function initform_prjdis() {\n            selproj_dis = dojo.query( \'select#disable_project\' )[0];\n            new ZSelect( selproj_dis, \'disable_project\', null );\n            function prjdis_onsubmit( e ) {\n                submitform( form_prjdis, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ]);\n                projectstatus.store.close();\n                projectstatus.fetch( { onComplete : projectstatus_oncomplete } );\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : prjdis_onsubmit, formid : \'prjdis\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updaterset(context,u,p,rs,action,reload):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3537
        __M_writer(u'\n    <form id=\'updaterset\' action="')
        # SOURCE LINE 3538
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3539
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3540
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3541
        __M_writer(escape(input_hidden( name='rset_id', value=str(rs.id))))
        __M_writer(u'\n    <div class="form">\n        <div class="field">\n            <div class="label" style="">Update ReviewSet :</div>\n            <div class="ftbox" required=True>\n                ')
        # SOURCE LINE 3546
        __M_writer(escape(input_text( name='name', id='name', value=rs.name )))
        __M_writer(u'\n            </div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 3549
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function updaterset_onsubmit(e) {\n            var reloadurl = "')
        # SOURCE LINE 3557
        __M_writer(reload )
        __M_writer(u'";\n            submitform( form_updaterset, e );\n            dojo.stopEvent(e);\n            if( reloadurl ) { window.location = reloadurl; }\n        }\n        function initform_updaterset() {\n            new zeta.Form({ onsubmit: updaterset_onsubmit, \n                            formid: \'updaterset\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_multiselect(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        unicode = context.get('unicode', UNDEFINED)
        range = context.get('range', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        str = context.get('str', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 163
        __M_writer(u'\n    ')
        # SOURCE LINE 164

        selected      = kwargs.get( 'opt_selected', '' )
        options       = kwargs.get( 'options', [] )
        opts_disabled = kwargs.get( 'opts_disabled', '' )
        restrict_kwargs( kwargs, multiselect_attrs )
        attrs         = make_attrs( kwargs )
        options       = options[:]
        for i in range(len(options)) :
            if isinstance( options[i], (str,unicode) ) :
                options[i] = ( options[i], options[i] )
            
        
        # SOURCE LINE 174
        __M_writer(u'\n    <select multiple="multiple" ')
        # SOURCE LINE 175
        __M_writer(attrs )
        __M_writer(u'>\n')
        # SOURCE LINE 176
        for val, txt in options :
            # SOURCE LINE 177
            __M_writer(u'            <option value=')
            __M_writer(escape(val))
            __M_writer(u'\n')
            # SOURCE LINE 178
            if selected == txt :
                # SOURCE LINE 179
                __M_writer(u'                selected="selected"\n')
                pass
            # SOURCE LINE 181
            if txt in opts_disabled :
                # SOURCE LINE 182
                __M_writer(u'                disabled="disabled"\n')
                pass
            # SOURCE LINE 184
            __M_writer(u'            >')
            __M_writer(escape(txt))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 186
        __M_writer(u'    </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_select_revwnature(context,naturenames):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3083
        __M_writer(u'\n    ')
        # SOURCE LINE 3084
        naturenames = [ [ '', '--Select-Nature--' ] ] + naturenames 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 3085
        __M_writer(escape(select( name='reviewnature', options=naturenames )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_deltckfilter(context,u,savfilterid,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3053
        __M_writer(u'\n    <form id="deltckfilter" action="')
        # SOURCE LINE 3054
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3055
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3056
        __M_writer(escape(input_hidden( name='tf_id', value=str(savfilterid) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3057
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'\n    </form>\n    <script type="text/javascript">\n        function deltckfilter_onsubmit( e ) {\n            submitform( form_deltckfilter, e );\n            dojo.stopEvent( e );\n        }\n        function initform_deltckfilter() {\n            new zeta.Form({ onsubmit: deltckfilter_onsubmit,\n                            formid: \'deltckfilter\' })\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_rmmstn(context,u,p,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2002
        __M_writer(u'\n    <form id="rmmstn" action="')
        # SOURCE LINE 2003
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2004
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2005
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;"></div>\n            <div class="ftarea">\n                ')
        # SOURCE LINE 2010
        __M_writer(escape(multiselect( name='milestone_id',  id='milestone_id', options=[],
                               size='4', style='width : 20em;' )))
        # SOURCE LINE 2011
        __M_writer(u'\n                <div>')
        # SOURCE LINE 2012
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Setup milestone removal */\n        function initform_rmmstn() {\n            var selmstn_rmmstn = dojo.query( \'form#rmmstn select#milestone_id\' )[0];\n            new ZSelect( selmstn_rmmstn, \'rmmstn\', null )\n            function rmmstn_onsubmit( e ) {\n                submitform( form_rmmstn, e );\n                mstnlist.store.close();\n                mstnlist.fetch({\n                    onComplete : mstnlist_oncomplete,\n                    sort : [ { attribute : \'milestone_name\' } ]\n                });\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: rmmstn_onsubmit, formid : \'rmmstn\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_delteamperms(context,u,p,teamtypes,deftt,teampgroups,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2330
        __M_writer(u'\n    <form id=\'delteamperms\' action="')
        # SOURCE LINE 2331
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2332
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2333
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">\n                ')
        # SOURCE LINE 2337
        __M_writer(escape(elements.iconize( 'Team :', 'team' )))
        __M_writer(u'</div>\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 2339
        __M_writer(escape(select( name='team_type', id='team_type', options=teamtypes,
                          opt_selected=deftt, style='width : 10em' )))
        # SOURCE LINE 2340
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Permissions :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2346
        __M_writer(escape(multiselect( name='projectteam_perm_id', id='projectteam_perm_id',
                               options=teampgroups, size="7", style='width : 15em' )))
        # SOURCE LINE 2347
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 2348
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n    <script type="text/javascript">\n        /* Setup permission removals to project team */\n        function initform_delteamperms() {\n            var dselect_tt     = dojo.query( \'form#delteamperms select[name=team_type]\'\n                                           )[0];\n            var select_delperm = dojo.query( \'form#delteamperms select#projectteam_perm_id\'\n                                           )[0];\n            new ZSelect( select_delperm, \'delpgfromteam\', null );\n            new ZSelect( dselect_tt, null, function( e ) { refresh_teamperms( \'todel\' ) } );\n            function delteamperms_onsubmit( e ) {\n                submitform( form_delteamperms, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                teamperms.store.close();\n                teamperms.fetch({ onComplete : teamperms_oncomplete });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit: delteamperms_onsubmit, formid : \'delteamperms\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_wikifav(context,u,p,w,action,name):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4182
        __M_writer(u'\n\n    <form id=\'wikifav\' class="dispnone" action="')
        # SOURCE LINE 4184
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4185
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4186
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 4187
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 4188
        __M_writer(escape(input_hidden( name=name, value=str(u.username))))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        /* Setup favorite wiki for user */\n        function initform_wikifav() {\n            var n_span  = dojo.query( "span[name=favwiki]" )[0];\n            var w_form  = new zeta.Form({ normalsub: true, formid: \'wikifav\' });\n            var n_field = dojo.query( "input[name=')
        # SOURCE LINE 4196
        __M_writer(escape(name))
        __M_writer(u']", form_wikifav )[0];\n            if( n_span && n_field ) {\n                new ZFavorite( n_span, form_wikifav, n_field );\n            }\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addtorset(context,u,p,rs,action,revwlist,reload=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3569
        __M_writer(u'\n    ')
        # SOURCE LINE 3570

        revwlist = [ [ '', '--Add Review to Set--' ] ] + revwlist
            
        
        # SOURCE LINE 3572
        __M_writer(u'\n    <form id=\'addtorset\' action="')
        # SOURCE LINE 3573
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3574
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3575
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3576
        __M_writer(escape(input_hidden( name='rset_id', value=str(rs.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3577
        __M_writer(escape(select( name='review_id', id='add_review_id', options=revwlist )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_addtorset() {\n            var n_selrid = dojo.byId( \'add_review_id\' );\n\n            new zeta.Form({ formid: \'addtorset\' });\n\n            // Submit form on selecting review to add\n            dojo.connect(\n                n_selrid, \'onchange\',\n                function( e ) {\n                    var reloadurl = "')
        # SOURCE LINE 3590
        __M_writer(reload )
        __M_writer(u'";\n                    if( n_selrid.value ) { submitform( form_addtorset, e ); }\n                    dojo.stopEvent( e );\n                    if( reloadurl ) { window.location = reloadurl; }\n                }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_deletemount_e(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3823
        __M_writer(u'\n    <form id="deletemount_e" action="')
        # SOURCE LINE 3824
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3825
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3826
        __M_writer(escape(input_hidden( name='mount_id', id='mount_id' )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_deletemount_e() {\n            new zeta.Form({ formid: \'deletemount_e\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addprjperms(context,u,p,projusers,defuser,x_userpgroups,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2373
        __M_writer(u'\n    <form id=\'addprjperms\' action="')
        # SOURCE LINE 2374
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2375
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2376
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 2380
        __M_writer(escape(elements.iconize( 'User :', 'user' )))
        __M_writer(u'</div>\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 2382
        __M_writer(escape(select( name='projuser', options=projusers,
                          opt_selected=defuser, style='width : 10em' )))
        # SOURCE LINE 2383
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 7em;">Permissions :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2389
        __M_writer(escape(multiselect( name='perm_group', id='perm_group', options=x_userpgroups, \
                               size="7", style='width : 15em' )))
        # SOURCE LINE 2390
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 2391
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Setup permission additions to project user */\n        function initform_addprjperms() {\n            var aselect_user   = dojo.query( \'form#addprjperms select[name=projuser]\'\n                                           )[0];\n            var select_addperm = dojo.query( \'form#addprjperms select[name=perm_group]\'\n                                           )[0];\n            new ZSelect( select_addperm, \'addppgtouser\', null );\n            new ZSelect( aselect_user, \'projusers\', function( e ) { refresh_prjperms() } );\n            function addprjperms_onsubmit( e ) {\n                submitform( form_addprjperms, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                prjperms.store.close();\n                prjperms.fetch({ onComplete : prjperms_oncomplete,\n                                 sort       : [{ attribute : \'username\' }]\n                              });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit: addprjperms_onsubmit, formid : \'addprjperms\' });\n        }\n        dojo.addOnLoad( initform_addprjperms );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectticket(context,u,ticketlist,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2489
        __M_writer(u'\n    ')
        # SOURCE LINE 2490

        ticketlist = [ [ '', '--Select-Ticket--' ] ] + ticketlist 
        default    = default or '--Select-Ticket--'
            
        
        # SOURCE LINE 2493
        __M_writer(u'\n    <span class="ml5">\n        ')
        # SOURCE LINE 2495
        __M_writer(escape(select( name='selectticket', id='selectticket', options=ticketlist,
                  opt_selected=default )))
        # SOURCE LINE 2496
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configsw(context,u,p,action,w='',typenames=[]):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 428
        __M_writer(u'\n    <div class="form">\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_configwiki() {\n            function configwiki_onsubmit( e ) {\n                submitform( form_configwiki, e );\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit : configwiki_onsubmit, formid : \'configwiki\' });\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_rmpcomp(context,u,p,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1806
        __M_writer(u'\n    <form id="rmpcomp" action="')
        # SOURCE LINE 1807
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1808
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1809
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;"></div>\n            <div class="ftarea">\n                ')
        # SOURCE LINE 1814
        __M_writer(escape(multiselect( name='component_id',  id='component_id', options=[],
                               size='4', style='width : 20em;' )))
        # SOURCE LINE 1815
        __M_writer(u'\n                <div>')
        # SOURCE LINE 1816
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_rmpcomp() {\n            /* Setup component removal */\n            var selpcomp_rmpcomp = dojo.query( \'form#rmpcomp select#component_id\')[0];\n            function rmpcomp_onsubmit( e ) {\n                submitform( form_rmpcomp, e );\n                pcomplist.store.close();\n                pcomplist.fetch({\n                    onComplete : pcomplist_oncomplete,\n                    sort : [ { attribute : \'componentname\' } ]\n                })\n                dojo.stopEvent(e);\n            }\n            new ZSelect( selpcomp_rmpcomp, \'rmpcomp\', null )\n            new zeta.Form({ onsubmit: rmpcomp_onsubmit, formid : \'rmpcomp\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configtst(context,u,p,action,t=None,ts=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2911
        __M_writer(u'\n    <form id="configtstat" action="')
        # SOURCE LINE 2912
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2913
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2914
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2915
        __M_writer(escape(input_hidden( name='ticket_id', value=( t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2916
        __M_writer(escape(input_hidden( name='ticket_status_id', value=( ts and str(ts.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2917
        __M_writer(escape(input_hidden( name='owner', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2918
        __M_writer(escape(input_hidden( name='tck_statusname')))
        __M_writer(u'\n    ')
        # SOURCE LINE 2919
        __M_writer(escape(input_hidden( name='due_date')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_wikitype(context,u,w,wikitypenames,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3907
        __M_writer(u'\n    <form id=\'wikitype\' action="')
        # SOURCE LINE 3908
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3909
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3910
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 3914
        __M_writer(escape(select( name='wiki_typename', id='wiki_typename', options=wikitypenames,
                          opt_selected=w.type.wiki_typename, style='width : 10em' )))
        # SOURCE LINE 3915
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_label(context,labelfor='',text=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 189
        __M_writer(u'\n    <label for="')
        # SOURCE LINE 190
        __M_writer(escape(labelfor))
        __M_writer(u'" >')
        __M_writer(escape(text))
        __M_writer(u'</label>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_creatercmt(context,u,p,r,action,naturenames):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3404
        __M_writer(u'\n    ')
        # SOURCE LINE 3405
 
        naturenames = [ '--Select-Nature--' ] + naturenames[:]
        pos_help    = 'Line number'
            
        
        # SOURCE LINE 3408
        __M_writer(u'\n    <form id=\'creatercmt\' action="')
        # SOURCE LINE 3409
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3410
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3411
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3412
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3413
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    <div class="form">\n        <div class="field" style="width: inherit;">\n            <div class="label" style="width : 8em;">Position :</div>\n            <div class="ftbox" style="width : 3em;" required="true" regExp="[0-9]*">\n                ')
        # SOURCE LINE 3418
        __M_writer(escape(input_text( name='position', style='width: 3em;' )))
        __M_writer(u'\n                <em>')
        # SOURCE LINE 3419
        __M_writer(escape(fieldhelp( pos_help, fhstyle="color: red;" )))
        __M_writer(u'</em>\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 8em;">Nature :</div>\n            <div class="fselect vtop"  style="width : 10em;">\n                ')
        # SOURCE LINE 3425
        __M_writer(escape(select( name='reviewnature', options=naturenames,
                          opt_selected='--Select-Nature--' )))
        # SOURCE LINE 3426
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop"  style="width : 8em;">Comment:</div>\n            <div class="ftarea" style="width: 40em;"required="true">\n                ')
        # SOURCE LINE 3432
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose review comment.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 3433
        __M_writer(escape(textarea( name='text', tatype='simpletextarea', id='crrcmt_text',
                            cols='50', rows='2')))
        # SOURCE LINE 3434
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 8em;"></div>\n            <div class="fsubmit" style="width: 10em;">')
        # SOURCE LINE 3439
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n    <script type="text/javascript">\n        // Setup review comment creation form\n        function initform_creatercmt() {\n            function creatercmt_onsubmit( e ) {\n                var i_pos = dojo.query( \'input[name=position]\', form_creatercmt )[0];\n                submitform( form_creatercmt, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                dojo.publish( \'refreshrcomments\', [ \'creatercmt\', i_pos.value ] );\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: creatercmt_onsubmit, formid: \'creatercmt\' });\n        }\n        dojo.addOnLoad( initform_creatercmt );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configvcs(context,u,p,action,v=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        t = context.get('t', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3694
        __M_writer(u'\n    <form id="configvcs" action="')
        # SOURCE LINE 3695
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3696
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3697
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3698
        __M_writer(escape(input_hidden( name='vcs_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3699
        __M_writer(escape(input_hidden( name='name')))
        __M_writer(u'\n    ')
        # SOURCE LINE 3700
        __M_writer(escape(input_hidden( name='rooturl')))
        __M_writer(u'\n    ')
        # SOURCE LINE 3701
        __M_writer(escape(input_hidden( name='vcs_typename')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatemount(context,u,m,vcslist,contents,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3743
        __M_writer(u'\n    <form id="updatemount" action="')
        # SOURCE LINE 3744
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3745
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3746
        __M_writer(escape(input_hidden( name='mount_id', value=str(m.id) )))
        __M_writer(u'\n    <div class="form">\n        <div class="disptrow">\n            <div class="ftbox" required="true">\n                 <em>name</em>')
        # SOURCE LINE 3750
        __M_writer(escape(input_text( name='name', id='name', value=m.name )))
        __M_writer(u'\n            </div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 3753
        __M_writer(escape(select( name='content',  id='content', options=contents,
                          opt_selected=m.content )))
        # SOURCE LINE 3754
        __M_writer(u'\n            </div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 3757
        __M_writer(escape(select( name='vcs_id',  id='vcs_id', options=vcslist,
                          opt_selected=m.vcs.name )))
        # SOURCE LINE 3758
        __M_writer(u'\n            </div>\n            <div class="ftbox" required="true">\n                <em>path</em>')
        # SOURCE LINE 3761
        __M_writer(escape(input_text( name='repospath', value=m.repospath, )))
        __M_writer(u'\n            </div>\n            <div class="pl20 fsubmit">')
        # SOURCE LINE 3763
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_updatemount() {\n            new zeta.Form({ formid: \'updatemount\' });\n            dijit.byId( \'name\' ).focus();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatepcomp(context,u,p,pusers,pcomplist,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1730
        __M_writer(u'\n    ')
        # SOURCE LINE 1731

        cn_help = 'component name must be unique'
            
        
        # SOURCE LINE 1733
        __M_writer(u'\n\n    <div class="w100 mb10">\n        ')
        # SOURCE LINE 1736
        __M_writer(escape(select( name='updtpcomp', id='updtpcomp', options=pcomplist )))
        __M_writer(u'\n        <hr/>\n    </div>\n    <form id="updatepcomp" action="')
        # SOURCE LINE 1739
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1740
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1741
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1742
        __M_writer(escape(input_hidden( name='component_id', value='' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Component name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1747
        __M_writer(escape(input_text( name='componentname', id='updtcompname' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1749
        __M_writer(escape(fieldhelp( cn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Owner :</div>\n            <div class="ftbox">\n                <span class="fggray" name="ownername"></span>&ensp;&ensp;\n                <span>Pick new owner :</span>\n                ')
        # SOURCE LINE 1757
        __M_writer(escape(select( name='owner',  id='updtowner', options=pusers )))
        __M_writer(u'</div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1762
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose component description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1763
        __M_writer(escape(textarea( name='description', id='updtpcompdesc', cols='50',
                            style='width : 25em' )))
        # SOURCE LINE 1764
        __M_writer(u'\n                <div>')
        # SOURCE LINE 1765
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Setup component detail update */\n        function initform_updatepcomp() {\n            var selpcomp_owner = dojo.query( \'form#updatepcomp select#updtowner\')[0];\n            new ZSelect( selpcomp_owner, \'updtpcompowners\', null ); \n            function updatepcomp_onsubmit( e ) {\n                var msg = \'\'\n                if ( dijit.byId(\'updatepcomp\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'updtowner\' ), \'value\' )) {\n                        msg = \'Provide component owner !!\'\n                    }\n                    if (! dojo.attr( dojo.byId( \'updtpcompdesc\' ), \'value\' )) {\n                        msg = \'Provide component description !!\'\n                    }\n\n                    if ( msg ) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                    } else {\n                        submitform( form_updatepcomp, e);\n                        pcomplist.store.close();\n                        pcomplist.fetch({\n                            onComplete : pcomplist_oncomplete,\n                            sort : [ { attribute : \'componentname\' } ]\n                        })\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                }\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: updatepcomp_onsubmit, formid : \'updatepcomp\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckversion(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2819
        __M_writer(u'\n    <form id="tckversion" action="')
        # SOURCE LINE 2820
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2821
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2822
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2823
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2824
        __M_writer(escape(input_hidden( name='version_id')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_radio(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n    ')
        # SOURCE LINE 80

        text = kwargs.get('text', '')
        restrict_kwargs( kwargs, inputradio_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 84
        __M_writer(u'\n    <input type="radio" ')
        # SOURCE LINE 85
        __M_writer(attrs )
        __M_writer(u'>')
        __M_writer(escape(text))
        __M_writer(u'</input>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatepg(context,u,action_pg,action_addpn,action_delpn,pgroups=[],defpg='',perms=[],x_perms=[]):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 524
        __M_writer(u'\n    ')
        # SOURCE LINE 525

        pg_help = ( 'Minimum 3 characters to max %s characters.' + \
                    'With all characters in small case.' ) % h.LEN_NAME
            
        
        # SOURCE LINE 528
        __M_writer(u'\n\n    <div class="w100 form">\n        <div class="field">\n            <div class="ftbox" style="width : 20em;" required="true">\n                Select group -\n                ')
        # SOURCE LINE 534
        __M_writer(escape(select( name='pglist', id='pglist', options=pgroups, opt_selected=defpg )))
        __M_writer(u'\n                <hr/>\n            </div>\n        </div>\n    </div>\n    <form id="updatepg" action="')
        # SOURCE LINE 539
        __M_writer(escape(action_pg))
        __M_writer(u'" method="post">\n    <div class="w100 form">\n    ')
        # SOURCE LINE 541
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 542
        __M_writer(escape(input_hidden( name='perm_group_id', value='' )))
        __M_writer(u'\n        <div class="field">\n            <div class="label" style="width : 11em;">Permission group :</div>\n            <div class="ftbox" style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 546
        __M_writer(escape(input_text( name='perm_group', id='updt_perm_group' )))
        __M_writer(u'</div>\n            <div class="fsubmit"  style="width : 5em;">')
        # SOURCE LINE 547
        __M_writer(escape(input_submit( value='Change' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n    <form id="addpntopg" action="')
        # SOURCE LINE 551
        __M_writer(escape(action_addpn))
        __M_writer(u'" method="post">\n    <div class="w100 form">\n    ')
        # SOURCE LINE 553
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 554
        __M_writer(escape(input_hidden( name='perm_group_id', value='' )))
        __M_writer(u'\n        <div class="field">\n            <div class="label" style="width : 11em;">Add Permissions :</div>\n            <div class="fselect vtop" style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 558
        __M_writer(escape(multiselect( name='perm_name', id='add_perm_name', options=x_perms, \
                               size="7", style='width : 17em' )))
        # SOURCE LINE 559
        __M_writer(u'</div>\n            <div class="fsubmit" style="width : 5em;">')
        # SOURCE LINE 560
        __M_writer(escape(input_submit( value='Add' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n    <form id="delpnfrompg" action="')
        # SOURCE LINE 564
        __M_writer(escape(action_delpn))
        __M_writer(u'" method="post">\n    <div class="w100 form">\n    ')
        # SOURCE LINE 566
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 567
        __M_writer(escape(input_hidden( name='perm_group_id', value='' )))
        __M_writer(u'\n        <div class="field">\n            <div class="label" style="width : 11em;">Delete Permissions :</div>\n            <div class="fselect vtop" style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 571
        __M_writer(escape(multiselect( name='perm_name', id='del_perm_name', options=perms, \
                               size="7", style='width : 17em' )))
        # SOURCE LINE 572
        __M_writer(u'</div>\n            <div class="fsubmit" style="width : 5em;">')
        # SOURCE LINE 573
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_perms() {\n            var select_addpn = dojo.query( \'form#addpntopg select#add_perm_name\' )[0];\n            new ZSelect( select_addpn, \'addpntopg\', null );\n\n            var select_delpn = dojo.query( \'form#delpnfrompg select#del_perm_name\' )[0];\n            new ZSelect( select_delpn, \'delpnfrompg\', null );\n\n            var select_pglist= dojo.query( \'select#pglist\' )[0];\n            new ZSelect( select_pglist, \'pglist\', function( e ) { refresh_perms() });\n\n            function perms_onsubmit( formid, e ) {\n                submitform( dojo.getObject( \'form_\'+formid, e ));\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                pgmap.store.close() ;\n                pgmap.fetch({\n                    onComplete : dojo.partial( pgmap_oncomplete, (formid == \'updatepg\')),\n                    sort       : [{ attribute : \'perm_group\' }]\n                });\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit : dojo.partial( perms_onsubmit, \'updatepg\' ),\n                            formid : \'updatepg\' });\n            new zeta.Form({ onsubmit : dojo.partial( perms_onsubmit, \'addpntopg\' ),\n                            formid : \'addpntopg\' });\n            new zeta.Form({ onsubmit : dojo.partial( perms_onsubmit, \'delpnfrompg\' ),\n                            formid : \'delpnfrompg\' });\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectsavfilter(context,u,filterlist,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3071
        __M_writer(u'\n    ')
        # SOURCE LINE 3072
 
        filterlist = [ [ '', '--Select-Filter--' ] ] + filterlist
        default    = default or '--Select-Filter--'
            
        
        # SOURCE LINE 3075
        __M_writer(u'\n    <span class="ml3">\n        ')
        # SOURCE LINE 3077
        __M_writer(escape(select( name='selsavfilter', id='selsavfilter',
                  options=filterlist, opt_selected=default )))
        # SOURCE LINE 3078
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_approve_userrelations(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 902
        __M_writer(u'\n    <form id="approveuserrels" action="')
        # SOURCE LINE 903
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 904
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="fchkbox ml10" style="width : 27em;"><div id="aurels"></div></div>\n        <div class="fsubmit ml10">')
        # SOURCE LINE 907
        __M_writer(escape(input_submit( value='Approve' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n    <div style="margin-left : 100px;" id="nodata">None</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_button(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 108
        __M_writer(u'\n    ')
        # SOURCE LINE 109

        restrict_kwargs( kwargs, inputbutton_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 112
        __M_writer(u'\n    <input type="button" ')
        # SOURCE LINE 113
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_wikicontent(context,u,w,wcnt,action,pageurl):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        h = context.get('h', UNDEFINED)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        def input_button(**kwargs):
            return render_input_button(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4031
        __M_writer(u'\n    ')
        # SOURCE LINE 4032

        sm_help = 'Enter the page summary, max %s characters' % h.LEN_SUMMARY
        sourceurl = w.sourceurl or ''
            
        
        # SOURCE LINE 4035
        __M_writer(u'\n\n    <form id=\'wikicont\' action="')
        # SOURCE LINE 4037
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4038
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4039
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4040
        __M_writer(escape(input_hidden( name='author', value=u.username )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field ml20">\n            <div class="ftarea w80" required="true">\n                ')
        # SOURCE LINE 4044
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 4045
        __M_writer(escape(textarea( name='text', tatype="simpletextarea", id='wcnttext', text=wcnt and wcnt.text or '',
                            cols='80', rows='30' )))
        # SOURCE LINE 4046
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 4051
        __M_writer(escape(input_submit( value='Save & Continue' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 4052
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 4053
        __M_writer(escape(input_button( id='preview', value='Preview' )))
        __M_writer(u'\n                <a class="ml10" href="')
        # SOURCE LINE 4054
        __M_writer(escape(pageurl))
        __M_writer(u'">Goto-Page</a>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function onpreview( x_form, e ) {\n            var div_wp  = dojo.query( \'.wikipreview\' )[0];\n            var ta_wcnt = dijit.byId( \'wcnttext\' )\n            var n_wtype = dojo.byId( \'wiki_typename\' );\n            if ( e.type == \'keyup\' && e.keyCode != dojo.keys.ENTER ) {\n                return;\n            }\n            if ( div_wp && ta_wcnt ) {\n                div_wp.innerHTML = \'\'\n                var url = url_preview( \'')
        # SOURCE LINE 4070
        __M_writer(h.url_wikipreview )
        __M_writer(u"', n_wtype.value);\n                xhrpost_obj( url,\n                             { 'text' : ta_wcnt.attr( 'value' ) },\n                             'text',\n                             false,\n                             null,\n                             function( resp ) {\n                                 dojo.toggleClass( div_wp.parentNode.parentNode, 'dispnone', false );\n                                 div_wp.innerHTML = resp;\n                             },\n                             null\n                           );\n                dojo.stopEvent( e );\n            }\n        }\n        function initform_wikicont() {\n            new zeta.Form({ normalsub: true, formid: 'wikicont' });\n            dijit.byId( 'wcnttext' ).focus();\n\n            // Setup preview\n            var x_form = dijit.byId( 'wikicont' );\n            var butt_preview = dojo.query( '#preview', x_form.domNode )[0];\n            dojo.connect( butt_preview, 'onclick', dojo.hitch( null, onpreview, x_form ));\n            dojo.connect( butt_preview, 'onkeyup', dojo.hitch( null, onpreview, x_form ));\n        }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addprjteam(context,u,p,teamtypes,deftt,x_teamusers,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2195
        __M_writer(u'\n    <form id=\'addprjteam\' action="')
        # SOURCE LINE 2196
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2197
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2198
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">\n                ')
        # SOURCE LINE 2202
        __M_writer(escape(elements.iconize( 'Team :', 'team' )))
        __M_writer(u'</div>\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 2204
        __M_writer(escape(select( name='team_type', id='team_type', options=teamtypes,
                          opt_selected=deftt, style='width : 10em' )))
        # SOURCE LINE 2205
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">\n                ')
        # SOURCE LINE 2210
        __M_writer(escape(elements.iconize( 'Users :', 'users' )))
        __M_writer(u'</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2212
        __M_writer(escape(multiselect( name='projuser', options=x_teamusers, \
                               size="7", style='width : 10em' )))
        # SOURCE LINE 2213
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 2214
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Setup user additions to project team */\n        function initform_addprjteam() {\n            var aselect_tt     = dojo.query( \'form#addprjteam select[name=team_type]\' )[0];\n            var select_adduser = dojo.query( \'form#addprjteam select[name=projuser]\' )[0];\n\n            new ZSelect( aselect_tt, null, function( e ) { refresh_projuser( \'toadd\' ) } );\n            new ZSelect( select_adduser, \'addprojuser\', null );\n\n            function addprjteam_onsubmit( e ) {\n                submitform( form_addprjteam, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                // Fetch and update the project team member details.\n                projectteams.store.close();\n                projectteams.fetch({ onComplete : projectteams_oncomplete });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit: addprjteam_onsubmit, formid : \'addprjteam\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_user_disable(context,u,action,eusers):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 970
        __M_writer(u'\n\n    <form id="userdis" action="')
        # SOURCE LINE 972
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 973
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 977
        __M_writer(escape(elements.iconize( 'Users :', 'users' )))
        __M_writer(u'</div>\n            <div class="fselect vtop">\n                ')
        # SOURCE LINE 979
        __M_writer(escape(multiselect( name='disable_user', id='disable_user', options=eusers,
                               size='7', style='width : 15em;' )))
        # SOURCE LINE 980
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 981
        __M_writer(escape(input_submit( value='Disable' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Initialise userdis form */\n        function initform_userdis( e ) {\n            seluser_dis = dojo.query( \'select#disable_user\' )[0];\n            new ZSelect( seluser_dis, \'disable_user\', null );\n            function userdis_onsubmit( e ) {\n                submitform( form_userdis, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ]);\n                userstatus.store.close();\n                userstatus.fetch( { onComplete : userstatus_oncomplete } );\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : userdis_onsubmit, formid : \'userdis\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_deletemount(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3776
        __M_writer(u'\n    <form id="deletemount" action="')
        # SOURCE LINE 3777
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3778
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3779
        __M_writer(escape(input_hidden( name='mount_id', id='del_mountid' )))
        __M_writer(u'\n    </form>\n    <script type="text/javascript">\n        function initform_deletemount() {\n            new zeta.Form({ formid: \'deletemount\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createproject(context,u,licensenames,liceditable,projectnames,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        h = context.get('h', UNDEFINED)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1441
        __M_writer(u'\n    ')
        # SOURCE LINE 1442

        pn_help = '<b>"projectname" cannot be changed later</b>' 
        sm_help = 'one line summary'
            
        
        # SOURCE LINE 1445
        __M_writer(u'\n\n    <form id="createprj" action="')
        # SOURCE LINE 1447
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1448
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 1449
        __M_writer(escape(input_hidden( name='admin', value=u.username )))
        __M_writer(u'\n    <div class="form">\n        <div class="field">\n            <div class="label" style="width : 15%">Project name :</div>\n            <div class="ftbox" required="true" regExp="')
        # SOURCE LINE 1453
        __M_writer(escape(h.RE_PNAME))
        __M_writer(u'">\n                ')
        # SOURCE LINE 1454
        __M_writer(escape(input_text( name='projectname', id='projectname' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1456
        __M_writer(escape(fieldhelp( pn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15%;">Summary :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1462
        __M_writer(escape(input_text( name='summary', id='summary', size='64', style='width : 30em;' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1464
        __M_writer(escape(fieldhelp( sm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15%;">Admin E-mailid :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1470
        __M_writer(escape(input_text( name='admin_email', id='admin_email', value=u.emailid )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15%;">License :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 1476
        __M_writer(escape(select( name='licensename',  id='licensename', options=licensenames )))
        __M_writer(u'\n')
        # SOURCE LINE 1477
        if liceditable :
            # SOURCE LINE 1478
            __M_writer(u'                    <a class="ml10 fntitalic" href="')
            __M_writer(escape(h.url_crlic))
            __M_writer(u'"\n                       title="Create a new license for this project">create-license</a>\n')
            # SOURCE LINE 1480
        else :
            # SOURCE LINE 1481
            __M_writer(u'                    <em title="You don\'t have the permission" \n                        class="ml10 undrln fggray">create-license</em>\n')
            pass
        # SOURCE LINE 1484
        __M_writer(u'            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 15%;">Description :</div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1489
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose project description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1490
        __M_writer(escape(textarea( name='description', tatype='simpletextarea', id='description',
                            cols='90', rows='20', style='width : 100%' )))
        # SOURCE LINE 1491
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15%;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 1497
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1498
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_createproject() {\n            function createprj_onsubmit( e ) {\n                var rg_pname  = dijit.byId(\'projectname\').value;\n                var projnames = ')
        # SOURCE LINE 1508
        __M_writer(h.json.dumps( projectnames ) )
        __M_writer(u';\n                var stopevent = false;\n                var msg       = \'\';\n                if ( dijit.byId(\'createprj\').validate() ) {\n                    for ( i in projnames ) {\n                        if ( projnames[i] == rg_pname ) {\n                            stopevent = true;\n                            msg       = rg_pname+ \' already exists\'\n                        }\n                    }\n                    if (! dojo.attr( dojo.byId( \'licensename\' ), \'value\' )) {\n                        stopevent = true;\n                        msg       = \'Provide the license for project !!\'\n                    }\n                    if (! dojo.attr( dojo.byId( \'description\' ), \'value\' )) {\n                        stopevent = true;\n                        msg       = \'Project description is a must !!\'\n                    }\n                    if (stopevent) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                        dojo.stopEvent( e );\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                    dojo.stopEvent( e );\n                }\n            }\n            new zeta.Form({ onsubmit : createprj_onsubmit, formid : \'createprj\' });\n            dijit.byId( \'projectname\' ).focus();\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_wikisummary(context,u,w,action,summary=''):
    context.caller_stack._push_frame()
    try:
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        un_help = context.get('un_help', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3922
        __M_writer(u'\n    <form id=\'wikisummary\' action="')
        # SOURCE LINE 3923
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3924
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3925
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\'Summary :\'</div>\n            <div class="ftbox"  required="true">\n                ')
        # SOURCE LINE 3930
        __M_writer(escape(input_text( name='summary', id='summary', value=summary )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 3932
        __M_writer(escape(fieldhelp( un_help )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_inviteuser(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1157
        __M_writer(u'\n    <form id="inviteuser" action="')
        # SOURCE LINE 1158
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1159
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="form">\n        <div class="field">\n            <div class="ftbox" required="true">\n                <span class="fntbold">User email-id to invite : </span>\n                ')
        # SOURCE LINE 1164
        __M_writer(escape(input_text( name='emailid',  id='emailid', size='32', style='width : 15em;' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_delprjperms(context,u,p,projusers,defuser,userpgroups,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2420
        __M_writer(u'\n    <form id=\'delprjperms\' action="')
        # SOURCE LINE 2421
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2422
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2423
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 2427
        __M_writer(escape(elements.iconize( 'User :', 'user' )))
        __M_writer(u'</div>\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 2429
        __M_writer(escape(select( name='projuser', options=projusers,
                          opt_selected=defuser, style='width : 10em' )))
        # SOURCE LINE 2430
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 7em;">Permissions :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2436
        __M_writer(escape(multiselect( name='project_perm_id', id='project_perm_id', options=userpgroups,
                               size="7", style='width : 15em' )))
        # SOURCE LINE 2437
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 2438
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_delprjperms() {\n            /* Setup permission removals to project user */\n            var dselect_user   = dojo.query( \'form#delprjperms select[name=projuser]\'\n                                           )[0];\n            var select_delperm = dojo.query( \'form#delprjperms select#project_perm_id\'\n                                           )[0];\n            new ZSelect( select_delperm, \'delppgfromuser\', null );\n            new ZSelect( dselect_user, \'projusers\', function( e ) { refresh_prjperms() } );\n            function delprjperms_onsubmit( e ) {\n                submitform( form_delprjperms, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                prjperms.store.close();\n                prjperms.fetch({ onComplete : prjperms_oncomplete,\n                                 sort       : [{ attribute : \'username\' }]\n                              });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit: delprjperms_onsubmit, formid : \'delprjperms\' });\n        }\n        dojo.addOnLoad( initform_delprjperms );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectwikipage(context,u,wikipagenames,default=''):
    context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        x = context.get('x', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3887
        __M_writer(u'\n    ')
        # SOURCE LINE 3888
 
        wikipagenames = sorted( wikipagenames, key=lambda x : x[1] )
        wikipagenames = [ [ '', '--Select-Wikipage--' ] ] +  wikipagenames
        default       = default or '--Select-Wikipage--'
            
        
        # SOURCE LINE 3892
        __M_writer(u'\n    <span class="ml5">\n        ')
        # SOURCE LINE 3894
        __M_writer(escape(select( name='selectwikipage', id='selectwikipage', options=wikipagenames,
                  opt_selected=default )))
        # SOURCE LINE 3895
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_fieldhelp(context,help='',fhstyle=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 193
        __M_writer(u'\n    <span class="fhelp" style="')
        # SOURCE LINE 194
        __M_writer(escape(fhstyle))
        __M_writer(u'" >')
        __M_writer(help )
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectfilerevision(context,u,revlist,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3643
        __M_writer(u'\n    <span class="ml5">\n        <span style="font-size : small;">File Revision :</span>\n        ')
        # SOURCE LINE 3646
        __M_writer(escape(select( name='selectfrev', id='selectfrev', options=revlist,
                  opt_selected=default )))
        # SOURCE LINE 3647
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_sitelogo(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_file(**kwargs):
            return render_input_file(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4332
        __M_writer(u'\n    <form id="sitelogo" enctype="multipart/form-data" action="')
        # SOURCE LINE 4333
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4334
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 6em;">File :</div>\n            <div class="ffile">\n                ')
        # SOURCE LINE 4339
        __M_writer(escape(input_file( name='sitelogofile', id='sitelogofile' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 6em;"></div>\n            <div class="fsubmit">')
        # SOURCE LINE 4344
        __M_writer(escape(input_submit( value='Upload' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatemstn(context,u,p,mstnlist,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_radio(**kwargs):
            return render_input_radio(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1907
        __M_writer(u'\n    ')
        # SOURCE LINE 1908

        mn_help = 'milestone name must be unique'
            
        
        # SOURCE LINE 1910
        __M_writer(u'\n\n    <div class="w100 mb20">\n        ')
        # SOURCE LINE 1913
        __M_writer(escape(select( name='updtmstn', id='updtmstn', options=mstnlist )))
        __M_writer(u'\n        <hr/>\n    </div>\n    <form id="updatemstn" action="')
        # SOURCE LINE 1916
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1917
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1918
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1919
        __M_writer(escape(input_hidden( name='milestone_id', value='' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Mileston name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1924
        __M_writer(escape(input_text( name='milestone_name', id='updtmstnname' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1926
        __M_writer(escape(fieldhelp( mn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Due date :</div>\n            <div class="fdtbox">\n                ')
        # SOURCE LINE 1932
        __M_writer(escape(input_text( name='due_date', id='updtduedate' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1938
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose milestone description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1939
        __M_writer(escape(textarea( name='description', id='updtmstndesc', cols='50',
                            style='width : 25em' )))
        # SOURCE LINE 1940
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Mark as : </div>\n            <div class="fradio">\n                ')
        # SOURCE LINE 1946
        __M_writer(escape(input_radio( name='status', id='mstnstatus1', value='open',
                               text='open' )))
        # SOURCE LINE 1947
        __M_writer(u'\n                ')
        # SOURCE LINE 1948
        __M_writer(escape(input_radio( name='status', id='mstnstatus2', value='cancelled',
                               text='cancelled' )))
        # SOURCE LINE 1949
        __M_writer(u'\n                ')
        # SOURCE LINE 1950
        __M_writer(escape(input_radio( name='status', id='mstnstatus3', value='completed',
                               text='completed' )))
        # SOURCE LINE 1951
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Closing remark : </div>\n            <div class="ftarea">\n                ')
        # SOURCE LINE 1957
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose closing_remark.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1958
        __M_writer(escape(textarea( name='closing_remark', id='closing_remark', rows='4', cols='50',
                style='width : 25em' )))
        # SOURCE LINE 1959
        __M_writer(u'\n                <div>')
        # SOURCE LINE 1960
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* setup milestone update */\n        function initform_updatemstn() {\n            function updatemstn_onsubmit( e ) {\n                var msg = \'\'\n                dojo.stopEvent(e);\n                if ( dijit.byId(\'updatemstn\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'updtmstndesc\' ), \'value\' )) {\n                        msg = \'Provide milestone description !!\'\n                    }\n                    if ( dijit.byId( \'mstnstatus2\' ).checked || \n                         dijit.byId( \'mstnstatus3\' ).checked ) {\n                        if (! dojo.attr( dojo.byId( \'closing_remark\' ), \'value\' )) {\n                            msg = \'Provide closing remark !!\'\n                        }\n                    }\n\n                    if ( msg ) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                    } else {\n                        submitform( form_updatemstn, e);\n                        mstnlist.store.close();\n                        mstnlist.fetch({\n                            onComplete : mstnlist_oncomplete,\n                            sort : [ { attribute : \'milestone_name\' } ]\n                        });\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                }\n            }\n            new zeta.Form({ onsubmit: updatemstn_onsubmit, formid : \'updatemstn\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createmstn(context,u,p,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1841
        __M_writer(u'\n    ')
        # SOURCE LINE 1842

        mn_help = 'milestone name must be unique'
            
        
        # SOURCE LINE 1844
        __M_writer(u'\n\n    <form id="createmstn" action="')
        # SOURCE LINE 1846
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1847
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1848
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Milestone name :</div>\n            <div class="ftbox" required="true"> \n                ')
        # SOURCE LINE 1853
        __M_writer(escape(input_text( name='milestone_name', id='crmstnname' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1855
        __M_writer(escape(fieldhelp( mn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Due date :</div>\n            <div class="fdtbox">\n                ')
        # SOURCE LINE 1861
        __M_writer(escape(input_text( name='due_date', id='crduedate' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1867
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose milestone description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1868
        __M_writer(escape(textarea( name='description', id='crmstndesc', rows='1', cols='50',
                            style='width : 25em' )))
        # SOURCE LINE 1869
        __M_writer(u'\n                <br/>\n                <div>')
        # SOURCE LINE 1871
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n    \n    <script type="text/javascript">\n        /* setup milestone creation */\n        function initform_createmstn() {\n            function createmstn_onsubmit( e ) {\n                var msg     = \'\'\n                if ( dijit.byId(\'createmstn\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'crmstndesc\' ), \'value\' )) {\n                        msg = \'Provide milestone description !!\'\n                    }\n\n                    if ( msg ) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                    } else {\n                        submitform( form_createmstn, e);\n                        mstnlist.store.close();\n                        mstnlist.fetch({\n                            onComplete : mstnlist_oncomplete,\n                            sort : [ { attribute : \'milestone_name\' } ]\n                        });\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                }\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: createmstn_onsubmit, formid : \'createmstn\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_project_enable(context,u,action,dprojects):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1003
        __M_writer(u'\n    <form id="prjenb" action="')
        # SOURCE LINE 1004
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1005
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 1009
        __M_writer(escape(elements.iconize( 'Projects :', 'projects' )))
        __M_writer(u'</div>\n            <div class="fselect vtop" style="width : 20em;">\n                ')
        # SOURCE LINE 1011
        __M_writer(escape(multiselect( name='enable_project', id='enable_project', options=dprojects,
                               size='7', style='width : 10em;' )))
        # SOURCE LINE 1012
        __M_writer(u'</div>\n            <div class="fsubmit ml10">')
        # SOURCE LINE 1013
        __M_writer(escape(input_submit( value='Enable' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Initialise prjenb form */\n        function initform_prjenb() {\n            selproj_enb = dojo.query( \'select#enable_project\' )[0];\n            new ZSelect( selproj_enb, \'enable_project\', null );\n            function prjenb_onsubmit( e ) {\n                submitform( form_prjenb, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ]);\n                projectstatus.store.close();\n                projectstatus.fetch( { onComplete : projectstatus_oncomplete } );\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : prjenb_onsubmit, formid : \'prjenb\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_select(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        unicode = context.get('unicode', UNDEFINED)
        range = context.get('range', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        str = context.get('str', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 139
        __M_writer(u'\n    ')
        # SOURCE LINE 140

        selected      = kwargs.get( 'opt_selected', '' )
        options       = kwargs.get( 'options', [] )
        opts_disabled = kwargs.get( 'opts_disabled', '' )
        restrict_kwargs( kwargs, select_attrs )
        attrs         = make_attrs( kwargs )
        options       = options[:]
        for i in range(len(options)) :
            if isinstance( options[i], (str,unicode) ) :
                options[i] = ( options[i], options[i] )
            
        
        # SOURCE LINE 150
        __M_writer(u'\n    <select ')
        # SOURCE LINE 151
        __M_writer(attrs )
        __M_writer(u'>\n')
        # SOURCE LINE 152
        for val, txt in options :
            # SOURCE LINE 153
            __M_writer(u'            ')

            selattr = 'selected="selected"' if selected == txt else ""
            disattr = 'disabled="disabled"' if txt in  opts_disabled else ""
            
                        
            
            # SOURCE LINE 157
            __M_writer(u'\n            <option value="')
            # SOURCE LINE 158
            __M_writer(escape(val))
            __M_writer(u'" ')
            __M_writer(escape(selattr))
            __M_writer(u' ')
            __M_writer(escape(disattr))
            __M_writer(u'>')
            __M_writer(escape(txt))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 160
        __M_writer(u'    </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_submit(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer(u'\n    ')
        # SOURCE LINE 95

        restrict_kwargs( kwargs, inputbutton_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 98
        __M_writer(u'\n    <input type="submit" ')
        # SOURCE LINE 99
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_wikisourceurl(context,u,w,action,sourceurl=''):
    context.caller_stack._push_frame()
    try:
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        un_help = context.get('un_help', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3939
        __M_writer(u'\n    <form id=\'wikisourceurl\' action="')
        # SOURCE LINE 3940
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3941
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3942
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\'Sourceurl :\'</div>\n            <div class="ftbox"  required="true">\n                ')
        # SOURCE LINE 3947
        __M_writer(escape(input_text( name='sourceurl', id='sourceurl', value=sourceurl )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 3949
        __M_writer(escape(fieldhelp( un_help )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckblockedby(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2837
        __M_writer(u'\n    <form id="tckblockedby" action="')
        # SOURCE LINE 2838
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2839
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2840
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2841
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2842
        __M_writer(escape(input_hidden( name='blockedby_ids')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckseverity(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2783
        __M_writer(u'\n    <form id="tckseverity" action="')
        # SOURCE LINE 2784
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2785
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2786
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2787
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2788
        __M_writer(escape(input_hidden( name='tck_severityname', value=( t and t.severity.tck_severityname or '' ) )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatelicense(context,u,l,action):
    context.caller_stack._push_frame()
    try:
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1330
        __M_writer(u'\n    ')
        # SOURCE LINE 1331

        ln_help  = 'licensename must be unique'
        sm_help  = 'one line summary'
        src_help = 'license originator'
            
        
        # SOURCE LINE 1335
        __M_writer(u'\n\n    <form id="updatelic" action="')
        # SOURCE LINE 1337
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1338
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1339
        __M_writer(escape(input_hidden( name='license_id', value=str(l.id))))
        __M_writer(u'\n    <div class="form 40em">\n        <div class="field pt20">\n            <div class="label" style="width : 12%;">License name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1344
        __M_writer(escape(input_text( name='licensename',  id='licensename', 
                              value=l.licensename, size='32', style='width : 15em;' )))
        # SOURCE LINE 1345
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1347
        __M_writer(escape(fieldhelp( ln_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12%;">Summary :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1353
        __M_writer(escape(input_text( name='summary',  id='summary', 
                              value=l.summary, size='64', style='width : 30em;' )))
        # SOURCE LINE 1354
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1356
        __M_writer(escape(fieldhelp( sm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12%;">Source :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1362
        __M_writer(escape(input_text( name='source', id='source', size='64', 
                              value=l.source, style='width : 30em;' )))
        # SOURCE LINE 1363
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1365
        __M_writer(escape(fieldhelp( src_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 12%;">License Text :</div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1371
        __M_writer(escape(textarea( name='text', tatype='simpletextarea', id='text',
                            text=l.text, cols='50', rows='20', style='width : 100%' )))
        # SOURCE LINE 1372
        __M_writer(u'\n            </div>\n        </div>\n')
        # SOURCE LINE 1377
        __M_writer(u'        <div class="field">\n            <div class="label" style="width : 12%;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 1380
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1381
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function updatelic_onsubmit( e ) {\n            if ( dijit.byId( \'updatelic\' ).validate() ) {\n                var lictext = dojo.byId( \'text\' ).value\n                if(! lictext ) {\n                    dojo.publish(\n                        \'flash\', [ \'error\', "License text must be present", 2000 ]\n                    );\n                    dojo.stopEvent( e );\n                }\n            } else {\n                dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                dojo.stopEvent( e );\n            }\n        }\n        function initform_updatelic() {\n            new zeta.Form({ onsubmit : updatelic_onsubmit, formid :  \'updatelic\' });\n        }\n        dojo.addOnLoad( initform_updatelic );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_projfav(context,u,p,action,name):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2467
        __M_writer(u'\n    <form id=\'projfav\' class="dispnone" action="')
        # SOURCE LINE 2468
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2469
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2470
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2471
        __M_writer(escape(input_hidden( name=name, value=str(u.username))))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        /* Setup favorite project for user */\n        function initform_projfav() {\n            var n_span  = dojo.query( "span[name=favproj]" )[0];\n            var w_form  = new zeta.Form({ normalsub: true, formid: \'projfav\' });\n            var n_field = dojo.query( "input[name=')
        # SOURCE LINE 2479
        __M_writer(escape(name))
        __M_writer(u']", form_projfav )[0];\n            if( n_span && n_field ) {\n                new ZFavorite( n_span, form_projfav, n_field );\n            }\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_projectinfo(context,u,p,licensenames,usernames,licurl,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1541
        __M_writer(u'\n    ')
        # SOURCE LINE 1542

        sm_help = 'one line summary'
        em_help = 'if left empty, your registered email-id will be used.'
        ml_help = 'project mailing-list as comma separated values'
        ir_help = 'project irc-channels as comma separated values'
        
        pinfo        = p.project_info
        mailinglists = ', '.join([ m.mailing_list for m in p.mailinglists ])
        ircchannels  = ', '.join([ i.ircchannel for i in p.ircchannels ])
            
        
        # SOURCE LINE 1551
        __M_writer(u'\n\n    <form id="updateprj" action="')
        # SOURCE LINE 1553
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1554
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1555
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1556
        __M_writer(escape(input_hidden( name='projectname', value=str(p.projectname))))
        __M_writer(u'\n')
        # SOURCE LINE 1558
        __M_writer(u'    ')
        __M_writer(escape(input_hidden( name='expose_project', id='exposed', value=p.projectname )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10%;">Summary :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1563
        __M_writer(escape(input_text( name='summary', id='summary', size='64',
                              style='width : 30em;', value=p.summary )))
        # SOURCE LINE 1564
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1566
        __M_writer(escape(fieldhelp( sm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10%;">Admin E-mailid :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 1572
        __M_writer(escape(input_text( name='admin_email', id='admin_email', value=p.admin_email )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1574
        __M_writer(escape(fieldhelp( em_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10%;">Description :</div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1580
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose project description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1581
        __M_writer(escape(textarea( name='description', id='description',
                            text=p.project_info.description, style='width : 40em' )))
        # SOURCE LINE 1582
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10%;">Admin :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 1588
        __M_writer(escape(select( name='admin',  id='admin', options=usernames,
                opt_selected=p.admin.username )))
        # SOURCE LINE 1589
        __M_writer(u'\n                ')
        # SOURCE LINE 1590
        __M_writer(escape(fieldhelp( 
                    'if you are changing the administrator, be sure to refresh the page',
                    fhstyle="font-style: italic; color: red"
                )))
        # SOURCE LINE 1593
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10%;">License :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 1599
        __M_writer(escape(select( name='licensename',  id='licensename', options=licensenames,
                          opt_selected=p.license and p.license.licensename or '' )))
        # SOURCE LINE 1600
        __M_writer(u'\n                <a class="ml5" href="')
        # SOURCE LINE 1601
        __M_writer(escape(licurl))
        __M_writer(u'">view-all-license</a>\n            </div>\n        </div>\n')
        # SOURCE LINE 1605
        __M_writer(u'        <div class="field">\n            <div class="label" style="width : 10%;">Mailing-lists :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 1608
        __M_writer(escape(input_text( name='mailinglists', id='mailinglists', size='64',
                              value= mailinglists )))
        # SOURCE LINE 1609
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1611
        __M_writer(escape(fieldhelp( ml_help )))
        __M_writer(u'\n            </div>\n        </div>\n')
        # SOURCE LINE 1615
        __M_writer(u'        <div class="field">\n            <div class="label" style="width : 10%;">Irc-channels :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 1618
        __M_writer(escape(input_text( name='ircchannels', id='ircchannels', size='64',
                              value= ircchannels )))
        # SOURCE LINE 1619
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1621
        __M_writer(escape(fieldhelp( ir_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10%;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 1627
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1628
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function updateprj_onsubmit( e ) {\n            var msg       = \'\';\n            if ( dijit.byId(\'updateprj\').validate() ) {\n                if (! dojo.attr( dojo.byId( \'licensename\' ), \'value\' )) {\n                    msg       = \'Provide the license for project !!\'\n                }\n                if (! dojo.attr( dojo.byId( \'description\' ), \'value\' )) {\n                    msg       = \'Project description is a must !!\'\n                }\n            } else {\n                msg = "Invalid form fields"\n            }\n            if (msg) {\n                dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n            } else {\n                submitform( form_updateprj, e );\n            }\n            dojo.stopEvent( e );\n        }\n        function initform_projectinfo() {\n            new zeta.Form({ onsubmit : updateprj_onsubmit, formid : \'updateprj\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckblocking(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2846
        __M_writer(u'\n    <form id="tckblocking" action="')
        # SOURCE LINE 2847
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2848
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2849
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2850
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2851
        __M_writer(escape(input_hidden( name='blocking_ids')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectwikiversion(context,u,versions,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3899
        __M_writer(u'\n    <span class="ml5">\n        ')
        # SOURCE LINE 3901
        __M_writer(escape(select( name='selectwver', id='selectwver', options=versions,
                  opt_selected=default )))
        # SOURCE LINE 3902
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updatewcmt(context,u,w,action,wcmt=None):
    context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4131
        __M_writer(u'\n    <form id=\'updatewcmt\' action="')
        # SOURCE LINE 4132
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4133
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4134
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4135
        __M_writer(escape(input_hidden( name='wiki_comment_id', value=wcmt and str(wcmt.id) or '' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4136
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4137
        __M_writer(escape(input_hidden( name='version_id', value=wcmt and str(wcmt.version_id) or '' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="w80">\n            ')
        # SOURCE LINE 4140
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose wiki comment.' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 4141
        __M_writer(escape(textarea( name='text', id='upwcmt_text', text=wcmt and wcmt.text or '' )))
        __M_writer(u'\n        </div>\n        <div>')
        # SOURCE LINE 4143
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectrevw(context,u,revwlist,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3093
        __M_writer(u'\n    ')
        # SOURCE LINE 3094
 
        revwlist = [ [ '', '--Select-Review--' ] ] + revwlist
        default  = default or '--Select-Review--'
            
        
        # SOURCE LINE 3097
        __M_writer(u'\n    <span class="ml5">\n        ')
        # SOURCE LINE 3099
        __M_writer(escape(select( name='selectrevw', id='selectrevw', options=revwlist,
                  opt_selected=default )))
        # SOURCE LINE 3100
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createpg(context,u,permnames,action):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 477
        __M_writer(u'\n    ')
        # SOURCE LINE 478

        pg_help = 'small cased, 2 to max %s characters. ' % h.LEN_NAME
            
        
        # SOURCE LINE 480
        __M_writer(u'\n\n    <form id="createpg" action="')
        # SOURCE LINE 482
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 483
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 11em;">Permission group :</div>\n            <div class="ftbox" style="width : 25em;" required="true" regExp="[a-z0-9_.]{2,32}">\n                ')
        # SOURCE LINE 488
        __M_writer(escape(input_text( name='perm_group', id='cr_perm_group' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 490
        __M_writer(escape(fieldhelp( pg_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 11em;">Permission names :</div>\n            <div class="fselect vtop"  style="width : 25em;" required="true">\n                ')
        # SOURCE LINE 496
        __M_writer(escape(multiselect( name='perm_name', id='cr_perm_name', options=permnames, \
                               size="7", style='width : 17em' )))
        # SOURCE LINE 497
        __M_writer(u'</div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 11em;"></div>\n            <div class="fsubmit" style="width : 25em;">')
        # SOURCE LINE 501
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_createpg() {\n            function createpg_onsubmit( e ) {\n                submitform( form_createpg, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                pgmap.store.close() ;\n                pgmap.fetch({\n                    onComplete : dojo.partial( pgmap_oncomplete, true ),\n                    sort       : [{ attribute : \'perm_group\' }]\n                });\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit : createpg_onsubmit, formid : \'createpg\' });\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_removelic_h(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1409
        __M_writer(u'\n\n    <form id="rmlic" action="')
        # SOURCE LINE 1411
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1412
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 1413
        __M_writer(escape(input_hidden( name='licensename',  id='licensename')))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_rmlic() {\n            function removelic( n_remove, n_tr, e ) {\n                var i_licname = dojo.query( \'input#licensename\' )[0];\n                var n_table   = n_tr.parentNode;\n                i_licname.value = dojo.attr( n_tr, \'licensename\' );\n                submitform( form_rmlic, e );\n                n_table.removeChild( n_tr );\n            }\n            dojo.query( \'span[name=rmlic]\' ).forEach(\n                function( n ) {\n                    dojo.connect(\n                        n, \'onclick\', \n                        dojo.partial( removelic, n, n.parentNode.parentNode )\n                    );\n              }\n            );\n            new zeta.Form({ onsubmit : null, formid : \'rmlic\' });\n        }\n        dojo.addOnLoad( initform_rmlic );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configrev(context,u,p,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3217
        __M_writer(u'\n    <form class="dispnone" id="configrev" action="')
        # SOURCE LINE 3218
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3219
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3220
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3221
        __M_writer(escape(input_hidden( name='review_id', value='' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3222
        __M_writer(escape(input_hidden( name='resource_url', id='resource_url', value='' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3223
        __M_writer(escape(input_hidden( name='version', id='version', value='' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3224
        __M_writer(escape(input_hidden( name='author', id='author', value='' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3225
        __M_writer(escape(input_hidden( name='moderator', id='moderator', value='' )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createmount_e(context,u,v,contents,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3788
        __M_writer(u'\n    ')
        # SOURCE LINE 3789

        rp_help = 'relative path to repositories root url'
            
        
        # SOURCE LINE 3791
        __M_writer(u'\n    <div id="mountpopup" class="dispnone p5 bgaliceblue br4"\n         style="border: 1px solid LightSteelBlue">\n        <form id="createmount_e" action="')
        # SOURCE LINE 3794
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n            ')
        # SOURCE LINE 3795
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n            ')
        # SOURCE LINE 3796
        __M_writer(escape(input_hidden( name='vcs_id', value=str(v.id) )))
        __M_writer(u'\n            ')
        # SOURCE LINE 3797
        __M_writer(escape(input_hidden( name='repospath', id='repospath' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 3798
        __M_writer(escape(input_text( name='name', id='name' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 3799
        __M_writer(escape(select( name='content',  id='content', options=contents )))
        __M_writer(u'\n            ')
        # SOURCE LINE 3800
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'\n        </form>\n        <div name="close" class="fgblue pointer">close</div>\n    </div>\n\n    <script type="text/javascript">\n        function cme_onsubmit( e ) {\n            var i_name = dojo.byId( \'name\' );\n            var i_content = dojo.byId( \'content\' );\n            if( i_name.value && i_content.value ) {\n                submitform( form_createmount_e, e );\n                dojo.publish( \'mounted\', [] );\n            } else {\n                dojo.publish( \'flash\', [ \'error\', \'Complete the form\', 2000 ]);\n            }\n            dojo.stopEvent( e );\n        }\n        function initform_createmount_e() {\n            new zeta.Form({ formid: \'createmount_e\', onsubmit: cme_onsubmit });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectrset(context,u,rsetlist,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3104
        __M_writer(u'\n    ')
        # SOURCE LINE 3105
 
        rsetlist = [ [ '', '--Select-ReviewSet--' ] ] + rsetlist
        default  = default or '--Select-ReviewSet--'
            
        
        # SOURCE LINE 3108
        __M_writer(u'\n    <span class="ml5">\n        ')
        # SOURCE LINE 3110
        __M_writer(escape(select( name='selectrset', id='selectrset', options=rsetlist,
                  opt_selected=default )))
        # SOURCE LINE 3111
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createticket(context,u,p,action,tck_typenames,tck_severitynames,projusers,components,milestones,versions):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        x = context.get('x', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2501
        __M_writer(u'\n    ')
        # SOURCE LINE 2502

        sm_help    = 'one line summary'
        blkby_help = 'comma separated list of <b>ticket ids</b> that are blocking this ticket'
        blkng_help = 'comma separated list of <b>ticket ids</b> that are blockedby this ticket'
        pt_help    = 'parent <b>ticket id</b>'
        
        components = [ [ '', '--Select-Component--' ] ] + \
                        sorted( components, key=lambda x : x[1] )
        milestones = [ [ '', '--Select-Milestone--' ] ] + \
                        sorted( milestones, key=lambda x : x[1] )
        versions   = [ [ '', '--Select-Version--' ] ]   + \
                        sorted( versions, key=lambda x : x[1] )
        projusers  = sorted( projusers )
            
        
        # SOURCE LINE 2515
        __M_writer(u'\n\n    <form id="createtck" action="')
        # SOURCE LINE 2517
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2518
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2519
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100">\n      <div class="posr floatl" style="padding-left : 20px;">\n      <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 15%;">Summary :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 2526
        __M_writer(escape(input_text( name='summary', id='summary', size='40', style='width : 25em;' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2528
        __M_writer(escape(fieldhelp( sm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15%;">type :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2534
        __M_writer(escape(select( name='tck_typename',  id='tck_typename', options=tck_typenames )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15%;">severity :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2540
        __M_writer(escape(select( name='tck_severityname',  id='tck_severityname', 
                          options=tck_severitynames )))
        # SOURCE LINE 2541
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 20%;">prompt user :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2547
        __M_writer(escape(select( name='promptuser',  id='promptuser', options=projusers,
                          opt_selected=u.username )))
        # SOURCE LINE 2548
        __M_writer(u'\n            </div>\n        </div>\n      </div>\n      </div>\n      <div class="posr floatl" style="border-left : 3px solid #d6d6d6;">\n      <div class="w100 form mb10">\n        <div class="field w100">\n          <div class="fselect">\n              <div class="floatl m5">\n                  ')
        # SOURCE LINE 2558
        __M_writer(escape(select( name='component_id',  id='component', options=components,
                            opt_selected='--Select-Component--' )))
        # SOURCE LINE 2559
        __M_writer(u'\n              </div>\n              <div class="floatl m5">\n                  ')
        # SOURCE LINE 2562
        __M_writer(escape(select( name='milestone_id',  id='milestone', options=milestones,
                            opt_selected='--Select-Milestone--' )))
        # SOURCE LINE 2563
        __M_writer(u'\n              </div>\n              <div class="floatl m5">\n                  ')
        # SOURCE LINE 2566
        __M_writer(escape(select( name='version_id',  id='version', options=versions,
                            opt_selected='--Select-Version--' )))
        # SOURCE LINE 2567
        __M_writer(u'\n              </div>\n          </div>\n        </div>\n      </div>\n      <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 20%;">blocked by :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2576
        __M_writer(escape(input_text( name='blockedby_ids', id='blockedby_ids' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2578
        __M_writer(escape(fieldhelp( blkby_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 20%;">blocking :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2584
        __M_writer(escape(input_text( name='blocking_ids', id='blocking_ids' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2586
        __M_writer(escape(fieldhelp( blkng_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 20%;">parent ticket:</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2592
        __M_writer(escape(input_text( name='parent_id', id='parent_id' )))
        __M_writer(u'\n                ( ')
        # SOURCE LINE 2593
        __M_writer(escape(fieldhelp( pt_help )))
        __M_writer(u' )\n            </div>\n        </div>\n      </div>\n      </div>\n      <div class="w100 form bclear" style="padding-left : 20px;">\n        <div class="field">\n            <div class="label vtop" style="width : 7%;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 2602
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose ticket description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 2603
        __M_writer(escape(textarea( name='description', tatype='simpletextarea', id='description',
                            cols='60', rows='7' )))
        # SOURCE LINE 2604
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 7%;"></div>\n            <div class="fsubmit">')
        # SOURCE LINE 2609
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n        </div>\n      </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_createtck() {\n            function createtck_onsubmit( e ) {\n                var stopevent = false;\n                var msg       = \'\';\n                if ( dijit.byId(\'createtck\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'tck_typename\' ), \'value\' )) {\n                        stopevent = true;\n                        msg       = \'Provide ticket type !!\'\n                    }\n                    if (! dojo.attr( dojo.byId( \'tck_severityname\' ), \'value\' )) {\n                        stopevent = true;\n                        msg       = \'Project ticket severity !!\'\n                    }\n                    if (stopevent) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                        dojo.stopEvent( e );\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                    dojo.stopEvent( e );\n                }\n            }\n            new zeta.Form({ onsubmit : createtck_onsubmit, formid: \'createtck\' });\n            dijit.byId( \'summary\' ).focus();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_selectvcs(context,u,vcslist,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3632
        __M_writer(u'\n    ')
        # SOURCE LINE 3633

        vcslist = [ [ '', '--Select-Repository--' ] ] + vcslist
        default = default or '--Select-Repository--'
            
        
        # SOURCE LINE 3636
        __M_writer(u'\n    <span class="ml5">\n        ')
        # SOURCE LINE 3638
        __M_writer(escape(select( name='selectvcs', id='selectvcs', options=vcslist,
                  opt_selected=default )))
        # SOURCE LINE 3639
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_licenselist(context,lics,default=''):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1247
        __M_writer(u'\n    ')
        # SOURCE LINE 1248
 
        lics    = [ [ '', '--Select-License--' ] ] + lics
        default = default or '--Select-License--'
            
        
        # SOURCE LINE 1251
        __M_writer(u'\n    <span style="margin-left : 10px; font-weight: normal;">\n        ')
        # SOURCE LINE 1253
        __M_writer(escape(select( name='viewlicense', id='viewlicense', options=lics, opt_selected=default )))
        __M_writer(u'\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_addteamperms(context,u,p,teamtypes,deftt,x_teampgroups,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2287
        __M_writer(u'\n    <form id=\'addteamperms\' action="')
        # SOURCE LINE 2288
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2289
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2290
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">\n                ')
        # SOURCE LINE 2294
        __M_writer(escape(elements.iconize( 'Team :', 'team' )))
        __M_writer(u'</div>\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 2296
        __M_writer(escape(select( name='team_type', id='team_type', options=teamtypes,
                          opt_selected=deftt, style='width : 10em' )))
        # SOURCE LINE 2297
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Permissions :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2303
        __M_writer(escape(multiselect( name='perm_group', id='perm_group', options=x_teampgroups, \
                               size="7", style='width : 15em' )))
        # SOURCE LINE 2304
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 2305
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n    <script type="text/javascript">\n        /* Setup permission additions to project team */\n        function initform_addteamperms() {\n            var aselect_tt     = dojo.query( \'form#addteamperms select[name=team_type]\'\n                                           )[0];\n            var select_addperm = dojo.query( \'form#addteamperms select[name=perm_group]\'\n                                           )[0];\n            new ZSelect( aselect_tt, null, function( e ) { refresh_teamperms( \'toadd\' ) } );\n            new ZSelect( select_addperm, \'addpgtoteam\', null );\n            function addteamperms_onsubmit( e ) {\n                submitform( form_addteamperms, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                teamperms.store.close();\n                teamperms.fetch({ onComplete : teamperms_oncomplete });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit: addteamperms_onsubmit, formid : \'addteamperms\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_textarea(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 130
        __M_writer(u'\n    ')
        # SOURCE LINE 131

        text  = kwargs.pop( 'text', '' )
        restrict_kwargs( kwargs, textarea_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 135
        __M_writer(u'\n    <textarea ')
        # SOURCE LINE 136
        __M_writer(attrs )
        __M_writer(u'>')
        __M_writer(escape(text))
        __M_writer(u'</textarea>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_attachstags(context,u,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4324
        __M_writer(u'\n    <form id="attachstags" action="')
        # SOURCE LINE 4325
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4326
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4327
        __M_writer(escape(input_hidden( name='attachment_id' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4328
        __M_writer(escape(input_hidden( name='tags' )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_votewiki(context,u,p,w,action,upvotes,downvotes,currvote):
    context.caller_stack._push_frame()
    try:
        vote = context.get('vote', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4204
        __M_writer(u'\n    <form id=\'votewiki\' class="dispnone" action="')
        # SOURCE LINE 4205
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4206
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4207
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 4208
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 4209
        __M_writer(escape(input_hidden( name='votedas', value=(vote and vote.votedas or ''))))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        /* Setup wiki voting form */\n        function initform_votewiki() {\n            var n_span = dojo.query( "span[name=wikivote]" )[0];\n            if( n_span ) {\n                new zeta.Voting({\n                    upvotes: ')
        # SOURCE LINE 4218
        __M_writer(escape(upvotes))
        __M_writer(u',\n                    downvotes: ')
        # SOURCE LINE 4219
        __M_writer(escape(downvotes))
        __M_writer(u",\n                    currvote: '")
        # SOURCE LINE 4220
        __M_writer(escape(currvote))
        __M_writer(u"',\n                    formid: 'votewiki'\n                }, n_span );\n            }\n        }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckdescription(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2864
        __M_writer(u'\n    <form id="tckdescription" action="')
        # SOURCE LINE 2865
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2866
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2867
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2868
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2869
        __M_writer(escape(textarea( name='description', tatype='simpletextarea', id='description',
                text=t.description, rows='10', style='width : 100%' )))
        # SOURCE LINE 2870
        __M_writer(u'\n    ')
        # SOURCE LINE 2871
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_searchbox(context,u,id,valasbg,action,faces=[],style='',classes=''):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4231
        __M_writer(u'\n    <span name="searchbox" class="')
        # SOURCE LINE 4232
        __M_writer(escape(classes))
        __M_writer(u'" style="')
        __M_writer(escape(style))
        __M_writer(u'">\n        <form id=\'')
        # SOURCE LINE 4233
        __M_writer(escape(id))
        __M_writer(u'\' class="dispinln" action="')
        __M_writer(escape(action))
        __M_writer(u'" method="get">\n')
        # SOURCE LINE 4234
        for face, val in faces :
            # SOURCE LINE 4235
            __M_writer(u'                ')
            __M_writer(escape(input_hidden( name=face, value=val )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 4237
        __M_writer(u'            ')
        __M_writer(escape(input_text( name='querystring', value=valasbg )))
        __M_writer(u'\n        </form>\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_delparts(context,u,p,r,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3358
        __M_writer(u'\n    <form class="dispnone" id="delparts" action="')
        # SOURCE LINE 3359
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3360
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3361
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3362
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3363
        __M_writer(escape(input_hidden( name='participant' )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_delparts() {\n            new zeta.Form({ formid: \'delparts\' });\n            dojo.subscribe(\n                \'delparticipant\', \n                function( username ) {\n                    dojo.query( \'input[name=participant]\', form_delparts \n                              )[0].value = username;\n                    submitform( form_delparts );\n                }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_edittck(context,u,p,t,action,tck_typenames,tck_severitynames,projusers,components,milestones,versions):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        compnentname = context.get('compnentname', UNDEFINED)
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        h = context.get('h', UNDEFINED)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2645
        __M_writer(u'\n    ')
        # SOURCE LINE 2646

        blkby_help = 'Enter blocking ticket ids as comma separated integer values'
        blkng_help = 'Enter blockedby ticket ids as comma separated integer values'
        pt_help    = 'Parent ticket id as integer value'
        sm_help    = 'A one line summary'
        ds_help    = 'Mininum 6 characters to max %s characters.' % h.LEN_DESCRIBE
        
        componentname  = t.components and t.components[0].componentname
        milestone_name = t.milestones and t.milestones[0].milestone_name
        version_name   = t.versions   and t.versions[0].version_name
        
        blockedby  = ', '.join([ str(tby.id) for tby in t.blockedby ])
        blocking   = ', '.join([ str(tng.id) for tng in t.blocking ])
        parent     = t.parent and str(t.parent.id) or ''
            
        
        # SOURCE LINE 2660
        __M_writer(u'\n    <form id="configtck" action="')
        # SOURCE LINE 2661
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2662
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2663
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2664
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 12em;">type :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2669
        __M_writer(escape(select( name='tck_typename',  id='tck_typename',
                          options=tck_typenames, opt_selected=t.type.tck_typename )))
        # SOURCE LINE 2670
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">severity :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2676
        __M_writer(escape(select( name='tck_severityname',  id='tck_severityname',
                          options=tck_severitynames, opt_selected=t.severity.tck_severityname )))
        # SOURCE LINE 2677
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">prompt user :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2683
        __M_writer(escape(select( name='promptuser',  id='promptuser', options=projusers,
                          opt_selected=t.promptuser.username )))
        # SOURCE LINE 2684
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">component :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2690
        __M_writer(escape(select( name='component_id',  id='component', options=components,
                          opt_selected=compnentname )))
        # SOURCE LINE 2691
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">milestone :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2697
        __M_writer(escape(select( name='milestone_id',  id='milestone', options=milestones,
                          opt_selected=milestone_name )))
        # SOURCE LINE 2698
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">version :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 2704
        __M_writer(escape(select( name='version_id',  id='version', options=versions,
                          opt_selected=version_name )))
        # SOURCE LINE 2705
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">blocked by :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2711
        __M_writer(escape(input_text( name='blockedby_ids', id='blockedby_ids', value=blockedby )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2713
        __M_writer(escape(fieldhelp( blkby_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">blocking :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2719
        __M_writer(escape(input_text( name='blocking_ids', id='blocking_ids', value=blocking )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2721
        __M_writer(escape(fieldhelp( blkng_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">parent ticket:</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2727
        __M_writer(escape(input_text( name='parent_id', id='parent_id', value=parent )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2729
        __M_writer(escape(fieldhelp( pt_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Summary :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 2735
        __M_writer(escape(input_text( name='summary', id='summary', value=t.summary,
                              size='64', style='width : 30em;' )))
        # SOURCE LINE 2736
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2738
        __M_writer(escape(fieldhelp( sm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Description</div>\n            <div class="ftarea w50">\n                ')
        # SOURCE LINE 2744
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose ticket description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 2745
        __M_writer(escape(textarea( name='description', tatype='simpletextarea', id='description',
                            text=t.description, rows='20', style='width : 100%' )))
        # SOURCE LINE 2746
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2748
        __M_writer(escape(fieldhelp( ds_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;"></div>\n            <div class="fsubmit">')
        # SOURCE LINE 2753
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_userreg(context,action,url_captcha):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        h = context.get('h', UNDEFINED)
        def input_password(**kwargs):
            return render_input_password(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 611
        __M_writer(u'\n    ')
        # SOURCE LINE 612

        un_help = 'All small case, between 3 characters to %s characters.' % h.LEN_NAME
        em_help = 'Your communication email id.'
        pw_help = 'Use a password of minimum 4 characters.'
            
        
        # SOURCE LINE 616
        __M_writer(u'\n\n    <form id="userreg" action="')
        # SOURCE LINE 618
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 12em;">Username :</div>\n            <div class="ftbox" style="width : 40em;" required="true" regExp="')
        # SOURCE LINE 622
        __M_writer(escape(h.RE_UNAME))
        __M_writer(u'">\n                ')
        # SOURCE LINE 623
        __M_writer(escape(input_text( name='username', id='username' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 625
        __M_writer(escape(fieldhelp( un_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Email-id :</div>\n            <div class="ftbox" style="width : 40em;" required="true" regExp="')
        # SOURCE LINE 630
        __M_writer(escape(h.RE_EMAIL))
        __M_writer(u'">\n                ')
        # SOURCE LINE 631
        __M_writer(escape(input_text( name='emailid', id='emailid')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 633
        __M_writer(escape(fieldhelp( em_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Password :</div>\n            <div class="fpass" style="width : 40em;">\n                ')
        # SOURCE LINE 639
        __M_writer(escape(input_password( name='password', id='password')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 641
        __M_writer(escape(fieldhelp( pw_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Confirm password :</div>\n            <div class="fpass" style="width : 40em;">\n                ')
        # SOURCE LINE 647
        __M_writer(escape(input_password( name='confpass', id='confpass')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 649
        __M_writer(escape(fieldhelp( pw_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Timezone :</div>\n            <div class="fselect" style="width : 40em;">\n                ')
        # SOURCE LINE 655
        __M_writer(escape(select( name='timezone',  id='timezone', options=h.all_timezones, opt_selected='UTC' )))
        __M_writer(u'</div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;"></div>\n            <div class="fsubmit">\n                <div>\n                    <a target="_blank" href="')
        # SOURCE LINE 661
        __M_writer(escape(h.url_tos))
        __M_writer(u'">Terms of Service</a>\n                 </div>\n                <div class="pt5 fgcrimson">\n                    By submitting this form, it is implied that you are agreeing\n                    to Terms of Service\n                </div>\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vbottom" style="width : 12em;">Captcha :</div>\n            ')
        # SOURCE LINE 671
        __M_writer(escape(elements.captcha( url_captcha )))
        __M_writer(u'\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;"></div>\n            <div class="fsubmit" sytle="width : 40em;">\n                ')
        # SOURCE LINE 676
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 677
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_userreg() {\n            function userreg_onsubmit( e ) {\n                var rg_uname = dijit.byId(\'username\').value;\n                var rg_pass = dijit.byId(\'password\').value;\n                var rg_cpass = dijit.byId(\'confpass\').value;\n                if ( dijit.byId(\'userreg\').validate() ) {\n                    for ( i = 0; i < usernames.length; i++ ) {\n                        if ( usernames[i] == rg_uname ) {\n                            dojo.publish( \'flash\', [ \'error\', rg_uname+\' already exists\', 2000 ]);\n                            dojo.stopEvent( e );\n                         }\n                    }\n                    if(rg_pass && rg_cpass) {\n                        if(rg_pass != rg_cpass){\n                            dojo.publish( \'flash\', [ \'error\', \'Please enter matching password!!\', 2000 ]);\n                            dojo.stopEvent( e );\n                        }\n                    } else {\n                        dojo.publish( \'flash\', [ \'error\', \'Please provide password\', 2000 ]);\n                        dojo.stopEvent( e );\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                    dojo.stopEvent( e );\n                }\n            }\n            new zeta.Form({ onsubmit : userreg_onsubmit, formid : \'userreg\' });\n            dijit.byId( \'username\' ).focus();\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckcomponent(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2801
        __M_writer(u'\n    <form id="tckcomponent" action="')
        # SOURCE LINE 2802
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2803
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2804
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2805
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2806
        __M_writer(escape(input_hidden( name='component_id')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_user_enable(context,u,action,dusers):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 937
        __M_writer(u'\n\n    <form id="userenb" action="')
        # SOURCE LINE 939
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 940
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 944
        __M_writer(escape(elements.iconize( 'Users :', 'users' )))
        __M_writer(u'</div>\n            <div class="fselect vtop">\n                ')
        # SOURCE LINE 946
        __M_writer(escape(multiselect( name='enable_user', id='enable_user', options=dusers,
                               size='7', style='width : 15em;' )))
        # SOURCE LINE 947
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 948
        __M_writer(escape(input_submit( value='Enable' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Initialise userenb form */\n        function initform_userenb( e ) {\n            seluser_enb = dojo.query( \'select#enable_user\' )[0];\n            new ZSelect( seluser_enb, \'enable_user\', null );\n            function userenb_onsubmit( e ) {\n                submitform( form_userenb, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ]);\n                userstatus.store.close();\n                userstatus.fetch( { onComplete : userstatus_oncomplete } );\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : userenb_onsubmit, formid : \'userenb\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_delprjteam(context,u,p,teamtypes,deftt,teamusers,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2241
        __M_writer(u'\n    <form id=\'delprjteam\' action="')
        # SOURCE LINE 2242
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2243
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2244
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">\n                ')
        # SOURCE LINE 2248
        __M_writer(escape(elements.iconize( 'Team :', 'team' )))
        __M_writer(u'</div>\n            <div class="fselect"  required="true">\n                ')
        # SOURCE LINE 2250
        __M_writer(escape(select( name='team_type', id='team_type', options=teamtypes,
                          opt_selected=deftt, style='width : 10em' )))
        # SOURCE LINE 2251
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">\n                ')
        # SOURCE LINE 2256
        __M_writer(escape(elements.iconize( 'Users :', 'users' )))
        __M_writer(u'</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 2258
        __M_writer(escape(multiselect( name='project_team_id', id='project_team_id',
                               options=teamusers, size="7", style='width : 10em' )))
        # SOURCE LINE 2259
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 2260
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_delprjteam() {\n            /* Setup user removal from project team */\n            var dselect_tt     = dojo.query( \'form#delprjteam select[name=team_type]\' )[0];\n            var select_deluser = dojo.query( \'form#delprjteam select#project_team_id\' )[0];\n\n            new ZSelect( dselect_tt, null, function( e ) { refresh_projuser( \'todel\' ) } );\n            new ZSelect( select_deluser, \'delprojuser\', null );\n\n            function delprjteam_onsubmit( e ) {\n                submitform( form_delprjteam, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                // Fetch and update the project team member details.\n                projectteams.store.close();\n                projectteams.fetch({ onComplete : projectteams_oncomplete });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit: delprjteam_onsubmit, formid : \'delprjteam\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_systemconfig(context,u,entries,action):
    context.caller_stack._push_frame()
    try:
        Exception = context.get('Exception', UNDEFINED)
        set = context.get('set', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 235
        __M_writer(u'\n    ')
        # SOURCE LINE 236

        if set( infofields + cnffields ) != set( entries ) :
            raise Exception( 'Mismatch in system fields' )
        
        help = {
            'welcomestring' :
                    """This string will be displayed on the page bar of site's
                    homepage""",
            'specialtags'   :
                    """Some tags are special, in the sense that they will be
                    interpreted by the application""",
            'projteamtypes' :
                    """Registered users can be part of a project only via a
                    team. Add team types for all the projects hosted under
                    this site, <em>non-members</em> denote registered users
                    who are not part of the project""",
            'tickettypes'   :
                    """Tickets can have type, it gives an idea about the
                    ticket""",
            'ticketseverity':
                    """Ticket severity should indicate at what priority it
                    should be addressed. Note that, sometimes important
                    ticket need not be urgent""",
            'ticketstatus'  :
                    """And this is how a ticket is tracked, typically a ticket
                    begins its life as 'new', travels through one of
                    its different states, that is defined here and finally moves on
                    to a resolved state.""",
            'ticketresolv'  :
                    """Should be a sub-set of ticket-status list, and
                    indicates that a ticket is resolved upon moving to this
                    state.""",
            'wikitypes' :
                    """Documents can also can have types, define them here""",
            'def_wikitype'  :
                    """Should be present in the list of `wikitypes`. On creating
                    a wiki page, it is always marked with the default
                    type""",
            'reviewactions' :
                    """<em>Authors</em> must take actions on review comments,
                    define the type of actions here""",
            'reviewnatures' :
                    """Nature of review comment. Sometimes, marking a comment
                    as `cosmetic` can avoid lot of debate.""",
            'vcstypes'  :
                    """Supported list of version control systems, integratable
                    with your site.""",
            'googlemaps'    :
                    """
                    <a href="http://code.google.com/apis/maps/signup.html">sign-up</a>
                    google map key for your site and copy the key here. If
                    left empty, google-maps will not be enabled.""",
            'strictauth'    :
                    """Setting this to `True` will completely restrict
                    anonymous user. This feature is still evolving""",
            'regrbyinvite'  :
                    """By default anybody can register in the site. In case
                    this is not desirable, set `regrbyinvite` to `True`""",
            'invitebyall'   :
                    """If `regrbyinvite` is set to `True`, `invitebyall`
                    defines who can invite new users. By default, only site
                    administrator can invite, if set to `True` any registered
                    user under this site can invite new users""",
        }
            
        
        # SOURCE LINE 300
        __M_writer(u'\n\n    <div class="w100 calign fgred">\n        All the confguration fields here pertains to entire site,\n        applicable to all projects created in this site\n    </div>\n    <div class="disptable w100">\n    <div class="disptrow">\n        <div class="disptcell w60">\n        <form id="system" action="')
        # SOURCE LINE 309
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n        ')
        # SOURCE LINE 310
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n        <div class="disptable ml50" style="border-collapse: separate; border-spacing: 10px">\n')
        # SOURCE LINE 312
        for field in cnffields :
            # SOURCE LINE 313
            __M_writer(u'            ')
            helptext = help.get( field, '' ) 
            
            __M_writer(u'\n            <div class="disptrow">\n                <div class="disptcell fntbold pb20">')
            # SOURCE LINE 315
            __M_writer(escape(field))
            __M_writer(u'</div>\n                <div class="disptcell ftbox pb20">\n                    ')
            # SOURCE LINE 317
            __M_writer(escape(input_text( name=field, style='width: 30em;', id='sys_'+field, value=entries[field] )))
            __M_writer(u'\n                </div>\n                <div class="disptcell">\n                <div class="ml10">\n')
            # SOURCE LINE 321
            if helptext :
                # SOURCE LINE 322
                __M_writer(u'                        ')
                __M_writer(escape(elements.helpboard( helptext, styles='padding: 5px' )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 324
            __M_writer(u'                </div>\n                </div>\n            </div>\n')
            pass
        # SOURCE LINE 328
        __M_writer(u'            <div class="disptrow">\n                <div class="disptcell"></div>\n                <div class="disptcell">')
        # SOURCE LINE 330
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n        </form>\n        </div>\n    </div>\n    </div>\n\n    <script type="text/javascript">\n        /* Initialise system form */\n        function initform_system( e ) {\n            new zeta.Form({ normalsub : true, formid : \'system\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckfav(context,u,p,t,action,name):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2973
        __M_writer(u'\n    <form id=\'tckfav\' class="dispnone" action="')
        # SOURCE LINE 2974
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2975
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2976
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2977
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2978
        __M_writer(escape(input_hidden( name=name, value=str(u.username))))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        /* Setup favorite ticket for user */\n        function initform_tckfav() {\n            var n_span  = dojo.query( "span[name=favtck]" )[0];\n            var w_form  = new zeta.Form({ normalsub: true, formid: \'tckfav\' });\n            var n_field = dojo.query( "input[name=')
        # SOURCE LINE 2986
        __M_writer(escape(name))
        __M_writer(u']", form_tckfav )[0];\n            if( n_span && n_field ) {\n                new ZFavorite( n_span, form_tckfav, n_field );\n            }\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createlicense(context,u,action):
    context.caller_stack._push_frame()
    try:
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1257
        __M_writer(u'\n    ')
        # SOURCE LINE 1258

        ln_help  = 'licensename must be unique'
        sm_help  = 'one line summary'
        src_help = 'license originator'
            
        
        # SOURCE LINE 1262
        __M_writer(u'\n\n    <form id="createlic" action="')
        # SOURCE LINE 1264
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1265
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="form 40em">\n        <div class="field pt20">\n            <div class="label" style="width : 12%;">License name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1270
        __M_writer(escape(input_text( name='licensename',  id='licensename', size='32', style='width : 15em;' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1272
        __M_writer(escape(fieldhelp( ln_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12%;">Summary :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1278
        __M_writer(escape(input_text( name='summary',  id='summary', size='64', style='width : 30em;' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1280
        __M_writer(escape(fieldhelp( sm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12%;">Source :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 1286
        __M_writer(escape(input_text( name='source', id='source', size='64', style='width : 30em;' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1288
        __M_writer(escape(fieldhelp( src_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop"  style="width : 12%;">License Text :</div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 1294
        __M_writer(escape(textarea( name='text', tatype='simpletextarea', id='text',
                            cols='80', rows='20', style='width : 100%' )))
        # SOURCE LINE 1295
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12%;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 1301
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1302
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_liccreate() {\n            function createlic_onsubmit( e ) {\n                if ( dijit.byId( \'createlic\' ).validate() ) {\n                    var lictext = dojo.byId( \'text\' ).value\n                    if(! lictext ) {\n                        dojo.publish(\n                            \'flash\', [ \'error\', "License text must be present", 2000 ]\n                        );\n                        dojo.stopEvent( e );\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                    dojo.stopEvent( e );\n                }\n            }\n            new zeta.Form({ onsubmit : createlic_onsubmit, formid : \'createlic\' });\n            dijit.byId( \'licensename\' ).focus();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tcktype(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2774
        __M_writer(u'\n    <form id="tcktype" action="')
        # SOURCE LINE 2775
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2776
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2777
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2778
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2779
        __M_writer(escape(input_hidden( name='tck_typename', value=(t and t.type.tck_typename or '') )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_updtpass(context,u,action):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def input_password(**kwargs):
            return render_input_password(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 821
        __M_writer(u'\n    ')
        # SOURCE LINE 822

        pw_help = 'Should be a minimum of 4 character password.'
            
        
        # SOURCE LINE 824
        __M_writer(u'\n\n    <form id="updtpass" action="')
        # SOURCE LINE 826
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 827
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 15em;">Enter new password :</div>\n            <div class="fpass" required="true" regExp="')
        # SOURCE LINE 831
        __M_writer(escape(h.RE_PASSWD))
        __M_writer(u'">\n                ')
        # SOURCE LINE 832
        __M_writer(escape(input_password( name='password', id='password')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 834
        __M_writer(escape(fieldhelp( pw_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15em;">Confirm password :</div>\n            <div class="fpass" required="true">\n                ')
        # SOURCE LINE 840
        __M_writer(escape(input_password(name='confpass', id='confpass')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 842
        __M_writer(escape(fieldhelp(pw_help)))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15em;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 848
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 849
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_updtpass() {\n            function updtpass_onsubmit( e ) {\n                password = dijit.byId( \'password\' ).value;\n                confpass = dijit.byId( \'confpass\' ).value;\n                if ( password == \'\' ) {\n                    dojo.publish( \'flash\', [ \'error\', "Enter password", 2000 ] );\n                } else if ( password != confpass ) {\n                    dojo.publish( \'flash\', [ \'error\', "Re-type the exact password", 2000 ]\n                    );\n                } else {\n                    submitform( form_updtpass, e );\n                }\n                dijit.byId( \'password\' ).value = \'\';\n                dijit.byId( \'confpass\' ).value = \'\';\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : updtpass_onsubmit, formid : \'updtpass\' });\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_tckmilestone(context,u,p,action,t=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2810
        __M_writer(u'\n    <form id="tckmilestone" action="')
        # SOURCE LINE 2811
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2812
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2813
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2814
        __M_writer(escape(input_hidden( name='ticket_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2815
        __M_writer(escape(input_hidden( name='milestone_id')))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_search(context,querystring,u,action,allfaces,faces):
    context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        def input_checkbox(**kwargs):
            return render_input_checkbox(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4242
        __M_writer(u'\n    ')
        # SOURCE LINE 4243

        project = faces.get('project', '')
        faces   = faces.keys()
        filterby = { 'staticwiki': 'guest-wiki' }
            
        
        # SOURCE LINE 4247
        __M_writer(u'\n    <form id=\'searchadv\' action="')
        # SOURCE LINE 4248
        __M_writer(escape(action))
        __M_writer(u'" method="get">\n')
        # SOURCE LINE 4249
        if project :
            # SOURCE LINE 4250
            __M_writer(u'            ')
            __M_writer(escape(input_hidden( name='project', value=project )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 4252
        __M_writer(u'        <div class="">\n            <span class="ml20 fntbold fntitalic">Filter By : </span>\n')
        # SOURCE LINE 4254
        for face in sorted(allfaces.keys()) :
            # SOURCE LINE 4255
            __M_writer(u'                <span class="mr10">\n                    ')
            # SOURCE LINE 4256
            checked = face in faces 
            
            __M_writer(u'\n')
            # SOURCE LINE 4257
            if checked :
                # SOURCE LINE 4258
                __M_writer(u'                        ')
                __M_writer(escape(input_checkbox( name=face, value=allfaces[face], checked='checked' )))
                __M_writer(u'\n                        ')
                # SOURCE LINE 4259
                __M_writer(escape(filterby.get(face, face).upper()))
                __M_writer(u'\n')
                # SOURCE LINE 4260
            else :
                # SOURCE LINE 4261
                __M_writer(u'                        ')
                __M_writer(escape(input_checkbox( name=face, value=allfaces[face] )))
                __M_writer(u'\n                        ')
                # SOURCE LINE 4262
                __M_writer(escape(filterby.get(face, face).upper()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 4264
            __M_writer(u'                </span>\n')
            pass
        # SOURCE LINE 4266
        __M_writer(u'            <span class="mr10">\n                ')
        # SOURCE LINE 4267
        checked = 'all' in faces 
        
        __M_writer(u'\n')
        # SOURCE LINE 4268
        if checked :
            # SOURCE LINE 4269
            __M_writer(u'                    ')
            __M_writer(escape(input_checkbox( name='all', value='1', checked='checked' )))
            __M_writer(u' ALL\n')
            # SOURCE LINE 4270
        else :
            # SOURCE LINE 4271
            __M_writer(u'                    ')
            __M_writer(escape(input_checkbox( name='all', value='1' )))
            __M_writer(u' ALL\n')
            pass
        # SOURCE LINE 4273
        __M_writer(u'            </span>\n        </div>\n        <div class="mt10 ml50">\n            ')
        # SOURCE LINE 4276
        __M_writer(escape(input_text( id="facetedsr", name='querystring', value=querystring )))
        __M_writer(u'\n            ')
        # SOURCE LINE 4277
        __M_writer(escape(input_submit( value='Search' )))
        __M_writer(u'\n        </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_searchadv() {\n            n = dojo.byId( \'facetedsr\' );\n            n.focus();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_forgotpass(context,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1170
        __M_writer(u'\n    <form id="forgotpass" action="')
        # SOURCE LINE 1171
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    <div class="form w100">\n        <div class="field">\n            <div class="ftbox vmiddle" style="text-align: center;" required="true">\n                ')
        # SOURCE LINE 1175
        __M_writer(escape(input_text( name='emailid',  id='emailid', size='32', style='width : 15em;' )))
        __M_writer(u'\n                <div class="mt10">\n                ')
        # SOURCE LINE 1177
        __M_writer(escape(elements.helpboard("""
                    Enter the email id that you have registered with us.
                    Reset link will be sent to you as e-mail.
                """)))
        # SOURCE LINE 1180
        __M_writer(u'\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createrset(context,u,p,action,reload):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3506
        __M_writer(u'\n    <form id=\'createrset\' action="')
        # SOURCE LINE 3507
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3508
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3509
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="form">\n        <div class="field">\n            <div class="label" style="">Create ReviewSet :</div>\n            <div class="ftbox" required=True>\n                ')
        # SOURCE LINE 3514
        __M_writer(escape(input_text( name='name', id='name', style='width: 10em;' )))
        __M_writer(u'\n            </div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 3517
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function createrset_onsubmit(e) {\n            var reloadurl = "')
        # SOURCE LINE 3525
        __M_writer(reload )
        __M_writer(u'";\n            submitform( form_createrset, e );\n            dojo.stopEvent(e);\n            if( reloadurl) { window.location = reloadurl; }\n        }\n        function initform_createrset() {\n            new zeta.Form({ onsubmit: createrset_onsubmit, \n                            formid: \'createrset\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createtcmt(context,u,p,t,action):
    context.caller_stack._push_frame()
    try:
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2923
        __M_writer(u'\n    <form id=\'createtcmt\' action="')
        # SOURCE LINE 2924
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2925
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2926
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2927
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2928
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="w80">\n            ')
        # SOURCE LINE 2931
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose ticket comment.' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 2932
        __M_writer(escape(textarea( name='text', id='crtcmt_text' )))
        __M_writer(u'\n        </div>\n        <div>')
        # SOURCE LINE 2934
        __M_writer(escape(input_submit( value='Add' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_integratevcs(context,u,p,action,vcs_typenames):
    context.caller_stack._push_frame()
    try:
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3651
        __M_writer(u'\n    ')
        # SOURCE LINE 3652

        nm_help = 'repository name must be unique'
            
        
        # SOURCE LINE 3654
        __M_writer(u'\n    <form id="integratevcs" action="')
        # SOURCE LINE 3655
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3656
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3657
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 12em;">Name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 3662
        __M_writer(escape(input_text( name='name', id='name' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 3664
        __M_writer(escape(fieldhelp( nm_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Type :</div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 3670
        __M_writer(escape(select( name='vcs_typename',  id='vcs_typename', options=vcs_typenames )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;">Root-url :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 3676
        __M_writer(escape(input_text( name='rooturl', id='rooturl', size='64', style='width : 30em;' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 12em;"></div>\n            <div class="fsubmit">')
        # SOURCE LINE 3681
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_integratevcs() {\n            new zeta.Form({ formid: \'integratevcs\' });\n            dijit.byId( \'name\' ).focus();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_delfromrset(context,u,p,rs,action,revwlist,reload=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3600
        __M_writer(u'\n    ')
        # SOURCE LINE 3601

        revwlist = [ [ '', '--Remove Review from Set--' ] ] + revwlist
            
        
        # SOURCE LINE 3603
        __M_writer(u'\n    <form id=\'delfromrset\' action="')
        # SOURCE LINE 3604
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3605
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3606
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3607
        __M_writer(escape(input_hidden( name='rset_id', value=str(rs.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3608
        __M_writer(escape(select( name='review_id', id='del_review_id', options=revwlist )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_delfromrset() {\n            var n_selrid = dojo.byId( \'del_review_id\' );\n\n            new zeta.Form({ formid: \'delfromrset\' });\n\n            // Submit form on selecting review to remove\n            dojo.connect(\n                n_selrid, \'onchange\',\n                function( e ) {\n                    var reloadurl = "')
        # SOURCE LINE 3621
        __M_writer(reload )
        __M_writer(u'";\n                    if( n_selrid.value ) { submitform( form_delfromrset, e ); }\n                    dojo.stopEvent( e );\n                    if( reloadurl ) { window.location = reloadurl; }\n                }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createver(context,u,p,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2037
        __M_writer(u'\n    ')
        # SOURCE LINE 2038

        vn_help = 'version name must be unique'
            
        
        # SOURCE LINE 2040
        __M_writer(u'\n\n    <form id="createver" action="')
        # SOURCE LINE 2042
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2043
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2044
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Version name :</div>\n            <div class="ftbox" required="true">\n                ')
        # SOURCE LINE 2049
        __M_writer(escape(input_text( name='version_name', id='crvername' )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 2051
        __M_writer(escape(fieldhelp( vn_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label vtop" style="width : 10em;">Description : </div>\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 2057
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose version description.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 2058
        __M_writer(escape(textarea( name='description', id='crverdesc', rows='1', cols='50',
                            style='width : 25em' )))
        # SOURCE LINE 2059
        __M_writer(u'\n                <div>')
        # SOURCE LINE 2060
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* setup version creation */\n        function initform_createver() {\n            function createver_onsubmit( e ) {\n                var msg = \'\'\n                if ( dijit.byId(\'createver\').validate() ) {\n                    if (! dojo.attr( dojo.byId( \'crverdesc\' ), \'value\' )) {\n                        msg = \'Provide version description !!\'\n                    }\n\n                    if ( msg ) {\n                        dojo.publish( \'flash\', [ \'error\', msg, 2000 ]);\n                    } else {\n                        submitform( form_createver, e );\n                        verlist.store.close();\n                        verlist.fetch({\n                            onComplete : verlist_oncomplete,\n                            sort : [ { attribute : \'version_name\' } ]\n                        });\n                    }\n                } else {\n                    dojo.publish( \'flash\', [ \'error\', "Invalid form fields", 2000 ]);\n                }\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit: createver_onsubmit, formid : \'createver\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_closerev(context,u,p,r,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_radio(**kwargs):
            return render_input_radio(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3294
        __M_writer(u'\n    <form class="dispnone" id="closerev" action="')
        # SOURCE LINE 3295
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3296
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3297
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3298
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3299
        __M_writer(escape(input_hidden( name='command', value='' )))
        __M_writer(u'\n')
        # SOURCE LINE 3300
        if r.closed :
            # SOURCE LINE 3301
            __M_writer(u'        Open  : ')
            __M_writer(escape(input_radio( name='radiocommand', value='open' )))
            __M_writer(u'\n        Close : ')
            # SOURCE LINE 3302
            __M_writer(escape(input_radio( name='radiocommand', value='close', checked='checked' )))
            __M_writer(u'\n')
            # SOURCE LINE 3303
        else :
            # SOURCE LINE 3304
            __M_writer(u'        Open  : ')
            __M_writer(escape(input_radio( name='radiocommand', value='open', checked='checked' )))
            __M_writer(u'\n        Close : ')
            # SOURCE LINE 3305
            __M_writer(escape(input_radio( name='radiocommand', value='close' )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 3307
        __M_writer(u'    </form>\n\n    <script type="text/javascript">\n        function onchange_command( value, e ) {\n            var i_command = dojo.query( \'input[name=command]\', form_closerev )[0];\n            dojo.attr( i_command,\'value\', value );\n            submitform( form_closerev, e );\n            dojo.stopEvent( e );\n        }\n        function initform_closerev() {\n            new zeta.Form({ formid: \'closerev\' });\n            var radios = dojo.query( \'input[name=radiocommand]\' );\n            dojo.connect( radios[0], \'onchange\', dojo.partial( onchange_command, \'open\' ));\n            dojo.connect( radios[1], \'onchange\', dojo.partial( onchange_command, \'close\' ));\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configwiki(context,u,p,action,w='',typenames=[]):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3956
        __M_writer(u'\n    ')
        # SOURCE LINE 3957

        wid = w and str(w.id) or ''
        wtype = w and w.type.wiki_typename or ''
        summary = w and w.summary or u''
        sourceurl = w and w.sourceurl or u''
        
        
        # SOURCE LINE 3962
        __M_writer(u'\n    <form id=\'configwiki\' action="')
        # SOURCE LINE 3963
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3964
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3965
        __M_writer(escape(input_hidden( name='wiki_id', value=wid)))
        __M_writer(u'\n    ')
        # SOURCE LINE 3966
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="form">\n        <div class="disptrow">\n            <div class="disptcell ralign">Summary :</div>\n            <div class="disptcell">\n            ')
        # SOURCE LINE 3971
        __M_writer(escape(input_text( name='summary', id='summary', value=summary,
                          style='width: 30em;')))
        # SOURCE LINE 3972
        __M_writer(u'\n            </div>\n        </div>\n        <div class="disptrow">\n            <div class="disptcell ralign">Source url :</div>\n            <div class="disptcell">\n            ')
        # SOURCE LINE 3978
        __M_writer(escape(input_text( name='sourceurl', id='sourceurl', value=sourceurl,
                          style='width: 30em;')))
        # SOURCE LINE 3979
        __M_writer(u'\n            </div>\n            <div class="disptcell ralign">Type :</div>\n            <div class="disptcell">\n            ')
        # SOURCE LINE 3983
        __M_writer(escape(select( name='wiki_typename', id='wiki_typename', options=typenames,
                      opt_selected=wtype, style='width : 10em' )))
        # SOURCE LINE 3984
        __M_writer(u'\n            </div>\n            <div class="disptcell">\n            ')
        # SOURCE LINE 3987
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_configwiki() {\n            function configwiki_onsubmit( e ) {\n                submitform( form_configwiki, e );\n                dojo.stopEvent(e);\n            }\n            new zeta.Form({ onsubmit : configwiki_onsubmit, formid : \'configwiki\' });\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_del_userrelations(context,u,reltypes,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 913
        __M_writer(u'\n    <form id=\'deluserrels\' action="')
        # SOURCE LINE 914
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 915
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 919
        __M_writer(escape(elements.iconize( 'Relation :', 'relation' )))
        __M_writer(u'</div>\n            <div class="fselect"  style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 921
        __M_writer(escape(select( name='userrel_type', id='userrel_type', options=reltypes,
                          style='width : 10em' )))
        # SOURCE LINE 922
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 927
        __M_writer(escape(elements.iconize( 'Users :', 'users' )))
        __M_writer(u'</div>\n            <div class="fselect" style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 929
        __M_writer(escape(multiselect( name='user_relation_id', id='user_relation_id',
                               options=[], size="4", style='width : 10em' )))
        # SOURCE LINE 930
        __M_writer(u'</div>\n            <div class="fsubmit ml10">')
        # SOURCE LINE 931
        __M_writer(escape(input_submit( value='Delete' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_votetck(context,u,p,t,action,upvotes,downvotes,currvote):
    context.caller_stack._push_frame()
    try:
        vote = context.get('vote', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2994
        __M_writer(u'\n    <form id=\'votetck\' class="dispnone" action="')
        # SOURCE LINE 2995
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2996
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2997
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2998
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2999
        __M_writer(escape(input_hidden( name='votedas', value=(vote and vote.votedas or ''))))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        /* Setup ticket voting form */\n        function initform_votetck() {\n            var n_span = dojo.query( "span[name=tckvote]" )[0];\n            if( n_span ) {\n                new zeta.Voting({\n                    upvotes: ')
        # SOURCE LINE 3008
        __M_writer(escape(upvotes))
        __M_writer(u',\n                    downvotes: ')
        # SOURCE LINE 3009
        __M_writer(escape(downvotes))
        __M_writer(u",\n                    currvote: '")
        # SOURCE LINE 3010
        __M_writer(escape(currvote))
        __M_writer(u"',\n                    formid: 'votetck'\n                }, n_span );\n            }\n        }\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_file(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n    ')
        # SOURCE LINE 88

        restrict_kwargs( kwargs, inputfile_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 91
        __M_writer(u'\n    <input type="file" ')
        # SOURCE LINE 92
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_wikidiff(context,u,w,action,wikicontents):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_radio(**kwargs):
            return render_input_radio(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4148
        __M_writer(u'\n    ')
        # SOURCE LINE 4149
        wikicontents = wikicontents[:] ; wikicontents.reverse() 
        
        __M_writer(u'\n\n    <form id="wikidiff" action="')
        # SOURCE LINE 4151
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4152
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4153
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4154
        __M_writer(escape(input_submit( value='View changes' )))
        __M_writer(u'\n    <table class="zwhistory">\n        <thead><tr>\n        <th class="zwhcmp" colspan="2">O/N</th>\n        <th class="zwhver"> Version </th>\n        <th class="zwhdesc"> Description </th>\n        </tr></thead>\n')
        # SOURCE LINE 4161
        for wcnt in wikicontents :
            # SOURCE LINE 4162
            __M_writer(u'        <tr>\n        <td class="zwhcmp">')
            # SOURCE LINE 4163
            __M_writer(escape(input_radio( name='oldver', value=str(wcnt.id))))
            __M_writer(u'</td>\n        <td class="zwhcmp">')
            # SOURCE LINE 4164
            __M_writer(escape(input_radio( name='newver', value=str(wcnt.id) )))
            __M_writer(u'</td>\n        <td class="zwhver"> ')
            # SOURCE LINE 4165
            __M_writer(escape(wcnt.id))
            __M_writer(u' </td>\n        <td class="zwhdesc">\n            Authored by <a href="')
            # SOURCE LINE 4167
            __M_writer(escape(h.url_foruser(wcnt.author)))
            __M_writer(u'">')
            __M_writer(escape(wcnt.author))
            __M_writer(u'</a>,\n            on ')
            # SOURCE LINE 4168
            __M_writer(escape(h.utc_2_usertz( wcnt.created_on, u.timezone ).strftime('%b %d, %Y, %r')))
            __M_writer(u'\n        </td>\n        </tr>\n')
            pass
        # SOURCE LINE 4172
        __M_writer(u'    </table>\n    </form>\n\n    <script type="text/javascript">\n        function initform_wikidiff() {\n            new zeta.Form({ formid: \'wikidiff\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_createmount(context,u,vcslist,contents,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3713
        __M_writer(u'\n    <form id="createmount" action="')
        # SOURCE LINE 3714
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3715
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    <div class="form">\n        <div class="disptrow">\n            <div class="ftbox" required="true">\n                 <em>name</em>')
        # SOURCE LINE 3719
        __M_writer(escape(input_text( name='name', id='name' )))
        __M_writer(u'\n            </div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 3722
        __M_writer(escape(select( name='content',  id='content', options=contents )))
        __M_writer(u'\n            </div>\n            <div class="fselect" required="true">\n                ')
        # SOURCE LINE 3725
        __M_writer(escape(select( name='vcs_id',  id='vcs_id', options=vcslist )))
        __M_writer(u'\n            </div>\n            <div class="ftbox" required="true">\n                <em>relative-path</em>')
        # SOURCE LINE 3728
        __M_writer(escape(input_text( name='repospath', id='repospath' )))
        __M_writer(u'\n            </div>\n            <div class="pl20 fsubmit">')
        # SOURCE LINE 3730
        __M_writer(escape(input_submit( value='Create' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_createmount() {\n            new zeta.Form({ formid: \'createmount\' });\n            dijit.byId( \'name\' ).focus();\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_replyrcmt(context,u,p,r,action):
    context.caller_stack._push_frame()
    try:
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3459
        __M_writer(u'\n    <form id=\'replyrcmt\' action="')
        # SOURCE LINE 3460
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3461
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3462
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3463
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3464
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3465
        __M_writer(escape(input_hidden( name='replytocomment_id', value='' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="ftarea" required="true">\n                ')
        # SOURCE LINE 3469
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose review comment.' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 3470
        __M_writer(escape(textarea( name='text', tatype='simpletextarea', id='rprcmt_text',
                            cols='90', rows='2', style='width : 100%' )))
        # SOURCE LINE 3471
        __M_writer(u'\n                ')
        # SOURCE LINE 3472
        __M_writer(escape(input_submit( value='Reply' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        // Setup review comment reply form\n        function initform_replyrcmt() {\n            function replyrcmt_onsubmit( e ) {\n                var i_r2cmt = dojo.query( \'input[name=replytocomment_id]\', form_replyrcmt )[0];\n                submitform( form_replyrcmt, e );\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                dojo.stopEvent(e);\n                dojo.publish( \'refreshrcomments\', [ \'replyrcmt\', i_r2cmt.value ] );\n            }\n            new zeta.Form({ onsubmit: replyrcmt_onsubmit, formid: \'replyrcmt\' });\n        }\n        dojo.addOnLoad( initform_replyrcmt );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_revwmoderator(context,u,p,r,action,projusers):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3261
        __M_writer(u'\n    ')
        # SOURCE LINE 3262

        projusers = [ [ '', '--Select-Moderator--' ] ] + projusers
        default   = r.moderator and r.moderator.username or '--Select-Moderator--'
        if not r.moderator :
            default   = '--Select-Moderator--'
        elif r.moderator.username not in projusers :
            default   = '--Select-Moderator--'
        else :
            default   = r.moderator.username
            
        
        # SOURCE LINE 3271
        __M_writer(u'\n    <form class="dispnone" id="revwmoderator" action="')
        # SOURCE LINE 3272
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3273
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3274
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3275
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3276
        __M_writer(escape(select( name='moderator', options=projusers, opt_selected=default )))
        __M_writer(u'\n    </form>\n\n    <script type="text/javascript">\n        function initform_revwmoderator() {\n            new zeta.Form({ formid: \'revwmoderator\' });\n            var n_select = dojo.query( \'select[name=moderator]\', form_revwmoderator )[0];\n            // Submit the form on selecting the moderator\n            dojo.connect( n_select, \'onchange\',\n                          function( e ) {\n                              submitform( form_revwmoderator, e );\n                              dojo.stopEvent( e );\n                          }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_replywcmt(context,u,w,action,wcmt=None):
    context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4114
        __M_writer(u'\n    <form id=\'replywcmt\' action="')
        # SOURCE LINE 4115
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4116
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4117
        __M_writer(escape(input_hidden( name='wiki_id', value=str(w.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4118
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4119
        __M_writer(escape(input_hidden( name='version_id', value=str(w.latest_version) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4120
        __M_writer(escape(input_hidden( name='replytocomment_id', value=wcmt and str(wcmt.id) or '' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="w80">\n            ')
        # SOURCE LINE 4123
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose wiki comment.' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 4124
        __M_writer(escape(textarea( name='text', id='rpwcmt_text' )))
        __M_writer(u'\n        </div>\n        <div>')
        # SOURCE LINE 4126
        __M_writer(escape(input_submit( value='Reply' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_replytcmt(context,u,p,t,action,tcmt=None):
    context.caller_stack._push_frame()
    try:
        def textarea(**kwargs):
            return render_textarea(context,**kwargs)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        elements = _mako_get_namespace(context, 'elements')
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2939
        __M_writer(u'\n    <form id=\'replytcmt\' action="')
        # SOURCE LINE 2940
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2941
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2942
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2943
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2944
        __M_writer(escape(input_hidden( name='commentby', value=u.username )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2945
        __M_writer(escape(input_hidden( name='replytocomment_id', value=tcmt and str(tcmt.id) or '' )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="w80">\n            ')
        # SOURCE LINE 2948
        __M_writer(escape(elements.captiontextarea( 'Use wiki markup to compose ticket comment.' )))
        __M_writer(u'\n            ')
        # SOURCE LINE 2949
        __M_writer(escape(textarea( name='text', id='rptcmt_text' )))
        __M_writer(u'\n        </div>\n        <div>')
        # SOURCE LINE 2951
        __M_writer(escape(input_submit( value='Reply' )))
        __M_writer(u'</div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_resetpass(context,action):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def input_password(**kwargs):
            return render_input_password(context,**kwargs)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1187
        __M_writer(u'\n    ')
        # SOURCE LINE 1188

        pw_help = 'Should be a minimum of 4 character password.'
            
        
        # SOURCE LINE 1190
        __M_writer(u'\n\n    <form id="resetpass" action="')
        # SOURCE LINE 1192
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 15em;">Enter new password :</div>\n            <div class="fpass" required="true" regExp="')
        # SOURCE LINE 1196
        __M_writer(escape(h.RE_PASSWD))
        __M_writer(u'">\n                ')
        # SOURCE LINE 1197
        __M_writer(escape(input_password( name='password', id='password')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1199
        __M_writer(escape(fieldhelp( pw_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15em;">Confirm password :</div>\n            <div class="fpass" required="true">\n                ')
        # SOURCE LINE 1205
        __M_writer(escape(input_password( name='confpass', id='confpass')))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 1207
        __M_writer(escape(fieldhelp( pw_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 15em;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 1213
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 1214
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_resetpass() {\n            function resetpass_onsubmit( e ) {\n                var password = dijit.byId( \'password\' ).value;\n                var confpass = dijit.byId( \'confpass\' ).value;\n                var msg  = null;\n                if ( password == \'\' ) {\n                    msg = "Enter password";\n                } else if ( password != confpass ) {\n                    msg = "Re-type the exact password";\n                }\n                if( msg ) {\n                    dojo.publish( \'flash\', [ \'error\', msg, 2000 ] );\n                    dijit.byId( \'password\' ).value = \'\';\n                    dijit.byId( \'confpass\' ).value = \'\';\n                    dojo.stopEvent( e );\n                }\n            }\n            new zeta.Form({ onsubmit : resetpass_onsubmit, formid : \'resetpass\' });\n            dijit.byId( \'password\' ).focus();\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_changetckst(context,u,p,t,statusname,due_date,action,tck_statusnames):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 2875
        __M_writer(u'\n    ')
        # SOURCE LINE 2876

        neutral_style = "float : none; text-align : center; margin : 0px;"
            
        
        # SOURCE LINE 2878
        __M_writer(u'\n    <form id="createtstat" action="')
        # SOURCE LINE 2879
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 2880
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 2881
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2882
        __M_writer(escape(input_hidden( name='ticket_id', value=str(t.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 2883
        __M_writer(escape(input_hidden( name='owner', value=str(u.id) )))
        __M_writer(u'\n    <div style="display : table;">\n    <div style="display : table-row;">\n        <div class="p5" style="display : table-cell;">\n            <div class="dispinln">status :</div>\n        </div>\n        <div class="p5" style="display : table-cell;">\n            <div class="dispinln">\n                ')
        # SOURCE LINE 2891
        __M_writer(escape(select( name='tck_statusname',  id='tck_statusname',
                          options=tck_statusnames, opt_selected=statusname )))
        # SOURCE LINE 2892
        __M_writer(u'\n            </div>\n        </div>\n        <div class="p5" style="display : table-cell;">\n            <div class="dispinln" style="width : 12em;">due date :</div>\n        </div>\n        <div class="p5" style="display : table-cell;">\n            <div class="fdtbox dispinln" style="')
        # SOURCE LINE 2899
        __M_writer(escape(neutral_style))
        __M_writer(u'">\n                ')
        # SOURCE LINE 2900
        __M_writer(escape(input_text( name='due_date', value=due_date, id='tsduedate' )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="p5" style="display : table-cell;">\n            <div class="dispinln">')
        # SOURCE LINE 2904
        __M_writer(escape(input_submit( value='Change' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_image(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 122
        __M_writer(u'\n    ')
        # SOURCE LINE 123

        restrict_kwargs( kwargs, inputimage_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 126
        __M_writer(u'\n    <input type="image" ')
        # SOURCE LINE 127
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_configwiki_h(context,u,p,action,w=''):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 4004
        __M_writer(u'\n    ')
        # SOURCE LINE 4005

        wid = w and str(w.id) or ''
        wtype = w and w.type.wiki_typename or ''
        summary = w and w.summary or u''
        sourceurl = w and w.sourceurl or u''
        
        
        # SOURCE LINE 4010
        __M_writer(u'\n    <form id=\'configwiki\' action="')
        # SOURCE LINE 4011
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 4012
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 4013
        __M_writer(escape(input_hidden( name='wiki_id', value=wid)))
        __M_writer(u'\n    ')
        # SOURCE LINE 4014
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    <div class="w100 form">\n        ')
        # SOURCE LINE 4016
        __M_writer(escape(input_text( name='wiki_typename', id='wiki_typename', value=wtype )))
        __M_writer(u'\n        ')
        # SOURCE LINE 4017
        __M_writer(escape(input_text( name='summary', id='summary', value=summary )))
        __M_writer(u'\n        ')
        # SOURCE LINE 4018
        __M_writer(escape(input_text( name='sourceurl', id='sourceurl', value=sourceurl)))
        __M_writer(u'\n        ')
        # SOURCE LINE 4019
        __M_writer(escape(input_submit( value='Update' )))
        __M_writer(u'\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_configwiki() {\n            new zeta.Form({ normalsub: true, formid: \'configwiki\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_add_userrelations(context,u,reltypes,action):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 877
        __M_writer(u'\n    <form id=\'adduserrels\' action="')
        # SOURCE LINE 878
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 879
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 880
        __M_writer(escape(input_hidden( name='userfrom', value=u.username )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 884
        __M_writer(escape(elements.iconize( 'Relation :', 'relation' )))
        __M_writer(u'</div>\n            <div class="fselect"  style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 886
        __M_writer(escape(select( name='userrel_type', id='userrel_type', options=reltypes,
                          style='width : 10em' )))
        # SOURCE LINE 887
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 892
        __M_writer(escape(elements.iconize( 'Users :', 'users' )))
        __M_writer(u'</div>\n            <div class="fselect" style="width : 20em;" required="true">\n                ')
        # SOURCE LINE 894
        __M_writer(escape(multiselect( name='userto', id='userto', options=[], \
                               size="4", style='width : 10em' )))
        # SOURCE LINE 895
        __M_writer(u'</div>\n            <div class="fsubmit ml10">')
        # SOURCE LINE 896
        __M_writer(escape(input_submit( value='Add' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_select_revwaction(context,actionnames):
    context.caller_stack._push_frame()
    try:
        def select(**kwargs):
            return render_select(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 3088
        __M_writer(u'\n    ')
        # SOURCE LINE 3089
        actionnames = [ [ '', '--Select-Action--' ] ] + actionnames 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 3090
        __M_writer(escape(select( name='reviewaction', options=actionnames )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_accountinfo(context,u,action):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def fieldhelp(help='',fhstyle=''):
            return render_fieldhelp(context,help,fhstyle)
        def input_reset(**kwargs):
            return render_input_reset(context,**kwargs)
        str = context.get('str', UNDEFINED)
        x = context.get('x', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def input_text(**kwargs):
            return render_input_text(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 716
        __M_writer(u'\n    ')
        # SOURCE LINE 717

        uinfo     = u.userinfo
        fliparg   = lambda x : x and x or ''
        em_help   = 'Your communication email id.'
        up_help   = 'Comma separated list of user panes'
            
        
        # SOURCE LINE 722
        __M_writer(u'\n\n    <form id="accountinfo" action="')
        # SOURCE LINE 724
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 725
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 726
        __M_writer(escape(input_hidden( name='username', id='username', value=u.username )))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 10em;">Email-id :</div>\n            <div class="ftbox" required="true" regExp="')
        # SOURCE LINE 730
        __M_writer(escape(h.RE_EMAIL))
        __M_writer(u'">\n                ')
        # SOURCE LINE 731
        __M_writer(escape(input_text( name='emailid', id='emailid', value=u.emailid )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 733
        __M_writer(escape(fieldhelp( em_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Timezone :</div>\n            <div class="fselect">\n                ')
        # SOURCE LINE 739
        __M_writer(escape(select( name='timezone',  id='timezone', options=h.all_timezones, opt_selected=u.timezone )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">First Name :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 745
        __M_writer(escape(input_text( name='firstname', id='firstname', value=fliparg(uinfo.firstname) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Middle Name :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 751
        __M_writer(escape(input_text( name='middlename', id='middlename', value=fliparg(uinfo.middlename) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Last Name :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 757
        __M_writer(escape(input_text( name='lastname', id='lastname', value=fliparg(uinfo.lastname) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Address line 1 :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 763
        __M_writer(escape(input_text( name='addressline1', id='addressline1', value=fliparg(uinfo.addressline1) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Address line 2 :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 769
        __M_writer(escape(input_text( name='addressline2', id='addressline2', value=fliparg(uinfo.addressline2) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">City :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 775
        __M_writer(escape(input_text( name='city', id='city', value=fliparg(uinfo.city) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Pincode :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 781
        __M_writer(escape(input_text( name='pincode', id='pincode', value=fliparg(uinfo.pincode) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">State :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 787
        __M_writer(escape(input_text( name='state', id='state', value=fliparg(uinfo.state) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Country :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 793
        __M_writer(escape(input_text( name='country', id='country', value=fliparg(uinfo.country) )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;">Userpanes :</div>\n            <div class="ftbox">\n                ')
        # SOURCE LINE 799
        __M_writer(escape(input_text( name='userpanes', id='myuserpanes', value=fliparg(uinfo.userpanes) )))
        __M_writer(u'\n                <br/>\n                ')
        # SOURCE LINE 801
        __M_writer(escape(fieldhelp( up_help )))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 10em;"></div>\n            <div class="fsubmit">\n                ')
        # SOURCE LINE 807
        __M_writer(escape(input_submit( value='Submit' )))
        __M_writer(u'\n                ')
        # SOURCE LINE 808
        __M_writer(escape(input_reset( value='Reset' )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        function initform_accountinfo() {\n            new zeta.Form({ normalsub: true, formid : \'accountinfo\' });\n        } \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_processrcmt(context,u,p,r,action):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3494
        __M_writer(u'\n    <form id=\'processrcmt\' action="')
        # SOURCE LINE 3495
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3496
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3497
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3498
        __M_writer(escape(input_hidden( name='review_id', value=str(r.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3499
        __M_writer(escape(input_hidden( name='review_comment_id', value='' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3500
        __M_writer(escape(input_hidden( name='approve', value='empty' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3501
        __M_writer(escape(input_hidden( name='reviewnature', value='empty' )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3502
        __M_writer(escape(input_hidden( name='reviewaction', value='empty' )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_reset(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 101
        __M_writer(u'\n    ')
        # SOURCE LINE 102

        restrict_kwargs( kwargs, inputbutton_attrs )
        attrs = make_attrs( kwargs )
            
        
        # SOURCE LINE 105
        __M_writer(u'\n    <input type="reset" ')
        # SOURCE LINE 106
        __M_writer(attrs )
        __M_writer(u'/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_deletevcs(context,u,p,action,v=None):
    context.caller_stack._push_frame()
    try:
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        t = context.get('t', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3705
        __M_writer(u'\n    <form id="deletevcs" action="')
        # SOURCE LINE 3706
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 3707
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id) )))
        __M_writer(u'\n    ')
        # SOURCE LINE 3708
        __M_writer(escape(input_hidden( name='project_id', value=str(p.id))))
        __M_writer(u'\n    ')
        # SOURCE LINE 3709
        __M_writer(escape(input_hidden( name='vcs_id', value=(t and str(t.id) or '') )))
        __M_writer(u'\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form_add_userpermissions(context,u,usernames,action,defuser,x_pgroups):
    context.caller_stack._push_frame()
    try:
        elements = _mako_get_namespace(context, 'elements')
        def multiselect(**kwargs):
            return render_multiselect(context,**kwargs)
        str = context.get('str', UNDEFINED)
        def input_hidden(**kwargs):
            return render_input_hidden(context,**kwargs)
        def select(**kwargs):
            return render_select(context,**kwargs)
        def input_submit(**kwargs):
            return render_input_submit(context,**kwargs)
        __M_writer = context.writer()
        # SOURCE LINE 1067
        __M_writer(u'\n    <form id="adduserperms" action="')
        # SOURCE LINE 1068
        __M_writer(escape(action))
        __M_writer(u'" method="post">\n    ')
        # SOURCE LINE 1069
        __M_writer(escape(input_hidden( name='user_id', value=str(u.id))))
        __M_writer(u'\n    <div class="w100 form">\n        <div class="field">\n            <div class="label" style="width : 7em;">\n                ')
        # SOURCE LINE 1073
        __M_writer(escape(elements.iconize( 'User :', 'user' )))
        __M_writer(u'</div>\n            <div class="fselect vtop"  required="true">\n                ')
        # SOURCE LINE 1075
        __M_writer(escape(select( name='username', id='addtouser', options=usernames, \
                          opt_selected=defuser, style='width : 12em' )))
        # SOURCE LINE 1076
        __M_writer(u'\n            </div>\n        </div>\n        <div class="field">\n            <div class="label" style="width : 7em;">Permissions :</div>\n            <div class="fselect vtop"  required="true">\n                ')
        # SOURCE LINE 1082
        __M_writer(escape(multiselect( name='perm_group', id='add_perm_group', options=x_pgroups, \
                               size="7", style='width : 15em' )))
        # SOURCE LINE 1083
        __M_writer(u'</div>\n            <div class="fsubmit" style="margin-left : 50px">')
        # SOURCE LINE 1084
        __M_writer(escape(input_submit( value='Add' )))
        __M_writer(u'</div>\n        </div>\n    </div>\n    </form>\n\n    <script type="text/javascript">\n        /* Initialise adduserperms form */\n        function initform_adduserperms( e ) {\n            seluser_addpg  = dojo.query( \'form#adduserperms select#addtouser\' )[0];\n            selpg_touser   = dojo.query( \'form#adduserperms select#add_perm_group\' )[0];\n            new ZSelect( seluser_addpg, null, function( e ) { refresh_userperms() } );\n            new ZSelect( selpg_touser, \'adduserpg\', null );\n\n            function adduserperms_onsubmit( e ) {\n                submitform( form_adduserperms, e )\n                dojo.publish( \'flash\', [ \'message\', "Refreshing ..." ] );\n                userperms.store.close();\n                userperms.fetch({\n                    onComplete : userperms_oncomplete,\n                    sort       : [{ attribute : \'username\' }]\n                });\n                dojo.stopEvent( e );\n            }\n            new zeta.Form({ onsubmit : adduserperms_onsubmit, formid : \'adduserperms\' });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


