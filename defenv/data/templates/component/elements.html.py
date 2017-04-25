# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1294317210.9896059
_template_filename=u'/home/pratap/mybzr/pratap/dev/zeta/zeta/templates-dojo/component/elements.html'
_template_uri=u'/component/elements.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['attachments', 'diff_row', 'captiontextarea', 'captcha', 'delete_row', 'titleindex', 'helpboard', 'pagebar', 'maintabs', 'timeline_view', 'favoriteicon', 'showpeople', 'replace_row', 'timeline', 'mainnav', 'tag_spans', 'lictable1', 'attach_spans', 'flashmessages', 'equal_row', 'attachdownloads', 'insert_row', 'difftable', 'user_panes', 'iconize', 'contextnav', 'iconlink']


# SOURCE LINE 7

iconmap = {
    'addattach'   : '/zetaicons/add_attach.png',
    'addtag'      : '/zetaicons/tag_green_add.png',
    'attach'      : '/zetaicons/attach.png',
    'project'     : '/zetaicons/project.png',
    'projects'    : '/zetaicons/projects.png',
    'relation'    : '/zetaicons/user_link.png',
    'tag'         : '/zetaicons/tag_green.png',
    'team'        : '/zetaicons/group_link.png',
    'users'       : '/zetaicons/group.png',
    'user'        : '/zetaicons/user.png',
    'trash'       : '/zetaicons/bin.png',
    'refresh'     : '/zetaicons/arrow_refresh.png',
    'servergo'    : '/zetaicons/server_go.png',
    'plus_exp'    : '/zetaicons/plus_exp.gif',
    'arrow_right' : '/zetaicons/arrow_right.png',
    'timeline'    : '/zetaicons/time.png',
    'tooltips'    : '/zetaicons/tooltips.png',
    'barchart'    : '/zetaicons/chart_bar.png',
    'commentadd'  : '/zetaicons/comment_add.png',
}


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 5
    ns = runtime.Namespace(u'forms', context._clean_inheritance_tokens(), templateuri=u'/component/forms.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'forms')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 96
        __M_writer(u'\n\n')
        # SOURCE LINE 134
        __M_writer(u'\n\n')
        # SOURCE LINE 158
        __M_writer(u'\n\n')
        # SOURCE LINE 183
        __M_writer(u'\n\n')
        # SOURCE LINE 213
        __M_writer(u'\n\n')
        # SOURCE LINE 218
        __M_writer(u'\n\n')
        # SOURCE LINE 226
        __M_writer(u'\n\n')
        # SOURCE LINE 233
        __M_writer(u'\n\n')
        # SOURCE LINE 256
        __M_writer(u'\n\n')
        # SOURCE LINE 287
        __M_writer(u'\n\n')
        # SOURCE LINE 294
        __M_writer(u'\n\n')
        # SOURCE LINE 299
        __M_writer(u'\n\n')
        # SOURCE LINE 304
        __M_writer(u'\n\n')
        # SOURCE LINE 312
        __M_writer(u'\n\n')
        # SOURCE LINE 360
        __M_writer(u'\n\n')
        # SOURCE LINE 367
        __M_writer(u'\n\n')
        # SOURCE LINE 370
        __M_writer(u'\n')
        # SOURCE LINE 377
        __M_writer(u'\n\n')
        # SOURCE LINE 388
        __M_writer(u'\n\n')
        # SOURCE LINE 394
        __M_writer(u'\n\n')
        # SOURCE LINE 400
        __M_writer(u'\n\n')
        # SOURCE LINE 409
        __M_writer(u'\n\n')
        # SOURCE LINE 442
        __M_writer(u'\n\n')
        # SOURCE LINE 445
        __M_writer(u'\n')
        # SOURCE LINE 458
        __M_writer(u'\n\n')
        # SOURCE LINE 590
        __M_writer(u'\n\n')
        # SOURCE LINE 593
        __M_writer(u'\n')
        # SOURCE LINE 710
        __M_writer(u'\n\n')
        # SOURCE LINE 713
        __M_writer(u'\n')
        # SOURCE LINE 819
        __M_writer(u'\n\n')
        # SOURCE LINE 867
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_attachments(context,u,attachments,editable,attachassc=None,aa=None,ua=None,la=None,pa=None,ta=None,ra=None,wa=None):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 715
        __M_writer(u'\n    ')
        # SOURCE LINE 716
        keys = sorted( attachments.keys() ) 
        
        __M_writer(u'\n    <div id="attachments" class="br4 w100" style="border: 3px solid #B3CFB3;">\n    <table class="w100">\n        <tr class="bggrn2">\n            <td class="p3 fntbold" style="width: 2%;">id</td>\n            <td class="p3 fntbold" style="">filename</td>\n            <td class="p3 fntbold" style="">summary</td>\n            <td class="p3 fntbold" style="">tags</td>\n            <td class="p3 fntbold" style="width: 5%;">uploader</td>\n')
        # SOURCE LINE 725
        if attachassc :
            # SOURCE LINE 726
            __M_writer(u'            <td class="p3 fntbold calign" style="width: 10em;">attached-to</td>\n')
            pass
        # SOURCE LINE 728
        __M_writer(u'            <td class="p3 fntbold calign" style="width: 8%;">downloads</td>\n            <td class="p3 fntbold" style="width: 8%;">size</td>\n        </tr>\n')
        # SOURCE LINE 731
        for k in keys :
            # SOURCE LINE 732
            __M_writer(u'            ')
            count = 0 
            
            __M_writer(u'\n            <tr class="fntitalic bggray2"><td class="p3 fntbold" colspan="8">')
            # SOURCE LINE 733
            __M_writer(escape(k))
            __M_writer(u'</td></tr>\n')
            # SOURCE LINE 734
            for att in attachments[k] :
                # SOURCE LINE 735
                __M_writer(u'                ')
 
                count += 1
                bgrnd = (count%2 == 0) and 'bggray1' or ''
                if attachassc :
                    items = [ h.attachassc2link( item, aa, ua, la, pa, ta, ra, wa )
                              for item in attachassc.get( att[0], [] ) ]
                else :
                    items = []
                                
                
                # SOURCE LINE 743
                __M_writer(u'\n                <tr class="')
                # SOURCE LINE 744
                __M_writer(escape(bgrnd))
                __M_writer(u'">\n                    <td class="p3 fggray" style="width: 2%">\n                        <a href="')
                # SOURCE LINE 746
                __M_writer(escape(att[8]))
                __M_writer(u'">')
                __M_writer(escape(att[0]))
                __M_writer(u'</a>\n                    </td>\n                    <td class="p3 fggray" style="">')
                # SOURCE LINE 748
                __M_writer(escape(att[1]))
                __M_writer(u'</td>\n                    <td class="p3" style="">\n                        <span name="summary" attid="')
                # SOURCE LINE 750
                __M_writer(escape(att[0]))
                __M_writer(u'" class="inedit">')
                __M_writer(escape(att[3]))
                __M_writer(u'</span>\n                    </td>\n                    <td class="p3" style="">\n                        <span name="tags" attid="')
                # SOURCE LINE 753
                __M_writer(escape(att[0]))
                __M_writer(u'" class="inedit">')
                __M_writer(escape(att[7]))
                __M_writer(u'</span>\n                    </td>\n                    <td class="p3 fggray" style="width: 5%;">\n                        <a href="')
                # SOURCE LINE 756
                __M_writer(escape(h.url_foruser( att[6] )))
                __M_writer(u'">')
                __M_writer(escape(att[6]))
                __M_writer(u'</a>\n                    </td>\n')
                # SOURCE LINE 758
                if attachassc :
                    # SOURCE LINE 759
                    __M_writer(u'                    <td class="p3 fggray calign" style="width: 10em;">\n')
                    # SOURCE LINE 760
                    for text, href in items :
                        # SOURCE LINE 761
                        __M_writer(u'                            <div class=""><a href="')
                        __M_writer(escape(href))
                        __M_writer(u'">')
                        __M_writer(escape(text))
                        __M_writer(u'</a></div>\n')
                        pass
                    # SOURCE LINE 763
                    __M_writer(u'                    </td>\n')
                    pass
                # SOURCE LINE 765
                __M_writer(u'                    <td class="p3 fggray calign" style="width: 8%;">')
                __M_writer(escape(att[4]))
                __M_writer(u'</td>\n                    <td class="p3 fggray" style="width: 8%;">')
                # SOURCE LINE 766
                __M_writer(escape(h.displaysize(att[2])))
                __M_writer(u'</td>\n                </tr>\n')
                pass
            pass
        # SOURCE LINE 770
        __M_writer(u'    </table>\n    </div>\n\n    <script type="text/javascript">\n        function editable_attachments() {\n            // Setup forms\n            new zeta.Form({ normalsub: true, formid: \'attachssummary\' });\n            new zeta.Form({ normalsub: true, formid: \'attachstags\' });\n\n            var inlines = dojo.query( \'span.inedit\' );\n\n            function inline_onchange( attid, formnode, field, value ) {\n                dojo.query( \'input[name=\' + field + \']\', formnode \n                          )[0].value = value;\n                dojo.query( \'input[name=attachment_id]\', formnode )[0].value = attid;\n                submitform( formnode );\n            }\n            dojo.forEach(\n                inlines,\n                function(item) {\n                    var name  = dojo.attr( item, \'name\' );\n                    var attid = dojo.attr( item, \'attid\' )   \n                    if ( name == \'summary\' ) {\n                        new dijit.InlineEditBox({\n                            editor: "dijit.form.TextBox",\n                            onChange: dojo.partial(\n                                        inline_onchange, attid, form_attachssummary, \'summary\' \n                                      ),\n                        }, item )        \n                    } else if ( name == \'tags\' ) {\n                        new dijit.InlineEditBox({\n                            editor: "dijit.form.TextBox",\n                            onChange: dojo.partial(\n                                        inline_onchange, attid, form_attachstags, \'tags\'\n                                      )\n                        }, item )        \n                    }\n                }\n            );\n\n        }\n        function setup_attachments() {\n            var editable = ')
        # SOURCE LINE 812
        __M_writer((editable and 'true' or 'false') )
        __M_writer(u'\n            if( editable ) {\n                editable_attachments()\n            }\n        }\n        dojo.addOnLoad( setup_attachments );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_diff_row(context,col1,col2,col3,cls):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 371
        __M_writer(u'\n    <tr class="')
        # SOURCE LINE 372
        __M_writer(escape(cls))
        __M_writer(u'">\n        <td class="oldver ')
        # SOURCE LINE 373
        __M_writer(escape(cls))
        __M_writer(u'">')
        __M_writer(escape(col1))
        __M_writer(u'</td>\n        <td class="newver ')
        # SOURCE LINE 374
        __M_writer(escape(cls))
        __M_writer(u'">')
        __M_writer(escape(col2))
        __M_writer(u'</td>\n        <td class="verdiff ')
        # SOURCE LINE 375
        __M_writer(escape(cls))
        __M_writer(u'">')
        __M_writer(escape(col3))
        __M_writer(u'</td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_captiontextarea(context,text=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 289
        __M_writer(u'\n    <div class="w100 mb5 fntitalic fntbold fggray">\n        ')
        # SOURCE LINE 291
        __M_writer(escape(text))
        __M_writer(u'\n        <a href="/help/zwiki/ZWiki">Zwiki reference</a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_captcha(context,url):
    context.caller_stack._push_frame()
    try:
        forms = _mako_get_namespace(context, 'forms')
        __M_writer = context.writer()
        # SOURCE LINE 362
        __M_writer(u'\n    <div class="ftbox vbottom">\n        ')
        # SOURCE LINE 364
        __M_writer(escape(forms.input_text( name='captcha', id='captcha' )))
        __M_writer(u'\n        <img class="ml20 bgblack p5" src="')
        # SOURCE LINE 365
        __M_writer(escape(url))
        __M_writer(u'"/>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_delete_row(context,tup,flines,tlines):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        def diff_row(col1,col2,col3,cls):
            return render_diff_row(context,col1,col2,col3,cls)
        __M_writer = context.writer()
        # SOURCE LINE 390
        __M_writer(u'\n')
        # SOURCE LINE 391
        for ln in range(tup[1], tup[2]) :
            # SOURCE LINE 392
            __M_writer(u'        ')
            __M_writer(escape(diff_row( ln+1, '', flines[ln], 'diffdelete' )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_titleindex(context,items,url_for,snippets):
    context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        map = context.get('map', UNDEFINED)
        len = context.get('len', UNDEFINED)
        filter = context.get('filter', UNDEFINED)
        p = context.get('p', UNDEFINED)
        range = context.get('range', UNDEFINED)
        r = context.get('r', UNDEFINED)
        def iconlink(link,iconname,anchor_name='',classes='',styles='',title=''):
            return render_iconlink(context,link,iconname,anchor_name,classes,styles,title)
        __M_writer = context.writer()
        # SOURCE LINE 314
        __M_writer(u'\n    ')
        # SOURCE LINE 315
        curdir = [] 
        
        __M_writer(u'\n    <ul class="ml50">\n')
        # SOURCE LINE 317
        for item in items :
            # SOURCE LINE 318
            __M_writer(u'        ')

            if len(item) == 2 :
                wikiid, path, urledit, suburldel = item + ('', '')
            elif len(item) == 4 :
                wikiid, path, urledit, suburldel = item
            
            parts  = filter( None, path.split('/') )
            render = map( lambda r, p : None if r == p else p, curdir, parts )
            while render :
                if render[-1] == None :
                    render.pop(-1)
                else :
                    break
            curdir = parts
            ndirs  = render and (len(render)-1) or 0
            
            (hd, pr) = snippets.get( wikiid, ('', '') )
            hd_snip = '<span class="fntbold fggray">%s</span>' % hd
            pr_snip = '<div>%s</div>' % pr
            
            a_edit = urledit and '<a class="ml5" href="%s">edit</a>' % urledit or ''
            span_del = suburldel and \
                       capture( iconlink, suburldel, 'trash',
                                classes='ml10', title='Remove this page') or ''
                    
            
            # SOURCE LINE 342
            __M_writer(u'\n')
            # SOURCE LINE 343
            for i in range(ndirs) :
                # SOURCE LINE 344
                if render[i] :
                    # SOURCE LINE 345
                    __M_writer(u'                <li class="pb10" style="margin-left: ')
                    __M_writer(escape(i*20))
                    __M_writer(u'px">\n                    <b>')
                    # SOURCE LINE 346
                    __M_writer(escape(render[i]))
                    __M_writer(u'</b>\n                </li>\n')
                    pass
                pass
            # SOURCE LINE 350
            __M_writer(u'        <li class="pb10" style="margin-left: ')
            __M_writer(escape(ndirs*20))
            __M_writer(u'px"\n            pathurl="')
            # SOURCE LINE 351
            __M_writer(escape(path))
            __M_writer(u'" suburldel="')
            __M_writer(escape(suburldel))
            __M_writer(u'">\n            <b><a href="')
            # SOURCE LINE 352
            __M_writer(escape(url_for( path )))
            __M_writer(u'">')
            __M_writer(escape(render[-1]))
            __M_writer(u'</a></b>\n            ')
            # SOURCE LINE 353
            __M_writer(hd_snip )
            __M_writer(u'\n            ')
            # SOURCE LINE 354
            __M_writer(a_edit )
            __M_writer(u'\n            ')
            # SOURCE LINE 355
            __M_writer(span_del )
            __M_writer(u'\n            ')
            # SOURCE LINE 356
            __M_writer(pr_snip )
            __M_writer(u'\n        </li>\n')
            pass
        # SOURCE LINE 359
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_helpboard(context,help='',classes='',styles=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 306
        __M_writer(u'\n    <div class="helpbrd bgblue1 p10 ')
        # SOURCE LINE 307
        __M_writer(escape(classes))
        __M_writer(u' br10"\n         style="font-family: Helvetica, sans-serif;\n                ')
        # SOURCE LINE 309
        __M_writer(escape(styles))
        __M_writer(u'">\n        ')
        # SOURCE LINE 310
        __M_writer(help )
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagebar(context,text,spans=[],rspans=[],tooltips=[],div_spans=[]):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def iconize(spantext,iconname,span_name='',classes='',styles='',title=''):
            return render_iconize(context,spantext,iconname,span_name,classes,styles,title)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n    <div id="pbar" class="brtl10 brtr10">\n        <div class="disptable vmiddle fntbold w100 bggrn1 brtl10 brtr10">\n        <div class="disptrow">\n            <div class="disptcell vmiddle pl10" style="height: 30px;">\n                <div>\n                    <span class="mr50">')
        # SOURCE LINE 37
        __M_writer(text )
        __M_writer(u'</span>\n')
        # SOURCE LINE 38
        for span in spans :
            # SOURCE LINE 39
            __M_writer(u'                        ')
            __M_writer(span )
            __M_writer(u'\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\n')
        # SOURCE LINE 42
        if rspans :
            # SOURCE LINE 43
            __M_writer(u'                        <div class="floatr">\n')
            # SOURCE LINE 44
            for span in rspans :
                # SOURCE LINE 45
                __M_writer(u'                                ')
                __M_writer(span )
                __M_writer(u'\n')
                pass
            # SOURCE LINE 47
            __M_writer(u'                        </div>\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'\n')
        # SOURCE LINE 50
        if tooltips :
            # SOURCE LINE 51
            __M_writer(u'                        <span id=\'trgr_tooltips\' title="Tips on how to use this page" \n                             style="margin: 5px 5px 0px 10px;" class="fgblue pointer">\n                            ')
            # SOURCE LINE 53
            __M_writer(escape(iconize( '', 'tooltips', styles="height: 16px;" )))
            __M_writer(u'\n                        </span>\n')
            # SOURCE LINE 55
        else :
            # SOURCE LINE 56
            __M_writer(u'                        <span id=\'trgr_tooltips\' title="Tips on how to use this page" \n                             style="margin: 5px 5px 0px 10px;" class="fggray">\n                        </span>\n')
            pass
        # SOURCE LINE 60
        __M_writer(u'                </div>\n            </div>\n        </div>\n')
        # SOURCE LINE 63
        if div_spans :
            # SOURCE LINE 64
            __M_writer(u'        <div class="disptrow bgwhite">\n            <div class="disptcell vmiddle"\n                 style="height: 27px; border-bottom : 1px solid green;">\n')
            # SOURCE LINE 67
            for span in div_spans :
                # SOURCE LINE 68
                __M_writer(u'                    ')
                __M_writer(span )
                __M_writer(u'\n')
                pass
            # SOURCE LINE 70
            __M_writer(u'            </div>\n        </div>\n')
            pass
        # SOURCE LINE 73
        __M_writer(u'        <div class="disptrow bgwhite">\n            <div class="disptcell">\n')
        # SOURCE LINE 75
        if tooltips :
            # SOURCE LINE 76
            __M_writer(u'                <div id="cont_tooltips"></div>\n')
            pass
        # SOURCE LINE 78
        __M_writer(u'            </div>\n        </div>\n        </div>\n    </div>\n\n    <script type="text/javascript">\n        function pagebartooltip() {\n            var n_cont = dojo.byId( \'cont_tooltips\' );\n            var n_trgr = dojo.byId( \'trgr_tooltips\' );\n            if( n_cont ) {\n                new zeta.ToolTips({\n                    n_tooltip : n_trgr,\n                    tooltips: ')
        # SOURCE LINE 90
        __M_writer( h.json.dumps( tooltips ) )
        __M_writer(u'\n                }, n_cont )\n            }\n        };\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintabs(context,tabs,psearchbox):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 136
        __M_writer(u'\n    ')
        # SOURCE LINE 137
        t1 = tabs[0] 
        
        __M_writer(u'\n    <div class="disptable calign w100 brtl10 brtr10" class="fnt87">\n    <div class="disptrow">\n        <div class="maintab disptcell vmiddle brtl10 ')
        # SOURCE LINE 140
        __M_writer(escape(t1.tab))
        __M_writer(u'">\n            <div>\n                <a style="" class="fntitalic" href="')
        # SOURCE LINE 142
        __M_writer(escape(t1.href))
        __M_writer(u'"\n                   title="')
        # SOURCE LINE 143
        __M_writer(escape(t1.title))
        __M_writer(u'" >')
        __M_writer(escape(t1.text))
        __M_writer(u'</a>\n            </div>\n        </div>\n')
        # SOURCE LINE 146
        for t in tabs[1:] : 
            # SOURCE LINE 147
            __M_writer(u'        <div class="maintab disptcell vmiddle ')
            __M_writer(escape(t.tab))
            __M_writer(u'" style="width: 11%">\n            <div>\n                <a href="')
            # SOURCE LINE 149
            __M_writer(escape(t.href))
            __M_writer(u'" title="')
            __M_writer(escape(t.title))
            __M_writer(u'">')
            __M_writer(escape(t.text))
            __M_writer(u'</a>\n            </div>\n        </div>\n')
            pass
        # SOURCE LINE 153
        __M_writer(u'        <div class="maintab disptcell vmiddle brtr10" style="width: 15em;">\n            ')
        # SOURCE LINE 154
        __M_writer(psearchbox )
        __M_writer(u'\n        </div>\n    </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_timeline_view(context,logs,fromoff,tooff,links,chartid=''):
    context.caller_stack._push_frame()
    try:
        x = context.get('x', UNDEFINED)
        h = context.get('h', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def timeline(ondt,log):
            return render_timeline(context,ondt,log)
        __M_writer = context.writer()
        # SOURCE LINE 460
        __M_writer(u'\n    ')
        # SOURCE LINE 461

        if logs :
            lf = '<span class="fgred">%s</span>' % logs[0].created_on.strftime("%a, %b %d, %Y")
            lt = '<span class="fgred">%s</span>' % logs[-1].created_on.strftime("%a, %b %d, %Y")
            logwindow = "Till %s from %s" % ( lf, lt )
        else :
            logwindow = "No logs"
        slices  = h.timeslice( logs )
        slicedt = sorted( slices.keys(),
                          key=lambda x : h.dt.datetime.strptime(x, '%a, %b %d %Y' ),
                          reverse=True )
            
        
        # SOURCE LINE 472
        __M_writer(u'\n    <div class="timeline ml10 mr10">\n        <br/>\n        <div class="pb2" style="height : 1.5em; border-bottom : 2px solid gray;">\n            <div class="floatr">\n                <a class="rss" href="')
        # SOURCE LINE 477
        __M_writer(escape(h.url_rssfeed))
        __M_writer(u'" rel="nofollow">RSS</a>\n\n')
        # SOURCE LINE 479
        if links[0] :
            # SOURCE LINE 480
            __M_writer(u'                    <span class="fntlarge fntbold"><a href="')
            __M_writer(escape(links[0]))
            __M_writer(u'">&#171;</a></span>\n')
            pass
        # SOURCE LINE 482
        __M_writer(u'\n')
        # SOURCE LINE 483
        if links[1] :
            # SOURCE LINE 484
            __M_writer(u'                    <span class="fntlarge fntbold ml5"><a href="')
            __M_writer(escape(links[1]))
            __M_writer(u'">&#8249;</a></span>\n')
            pass
        # SOURCE LINE 486
        __M_writer(u'\n                <span class="ml5">')
        # SOURCE LINE 487
        __M_writer(escape(fromoff))
        __M_writer(u'-')
        __M_writer(escape(tooff))
        __M_writer(u'</span>\n\n')
        # SOURCE LINE 489
        if links[2] :
            # SOURCE LINE 490
            __M_writer(u'                    <span class="fntlarge fntbold ml5"><a href="')
            __M_writer(escape(links[2]))
            __M_writer(u'">&#8250;</a></span>\n')
            pass
        # SOURCE LINE 492
        __M_writer(u'\n            </div>\n            <span class="fntbold">')
        # SOURCE LINE 494
        __M_writer(logwindow )
        __M_writer(u'</span>\n            <span name="expand" class="ml10 fgblue pointer">Expand</span>\n        </div>\n        <div class="pl5 pr5">\n')
        # SOURCE LINE 498
        if chartid :
            # SOURCE LINE 499
            __M_writer(u'                <div class="floatr p5 bgwhite">\n                    <div class="chartcntnr">\n                        <div id="')
            # SOURCE LINE 501
            __M_writer(escape(chartid))
            __M_writer(u'" class="chart"\n                             style="width: 500px; height: 325px;">\n                        </div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 507
        for ondt in slicedt :
            # SOURCE LINE 508
            __M_writer(u'                <ul class="">\n')
            # SOURCE LINE 509
            for log in slices[ondt] :
                # SOURCE LINE 510
                __M_writer(u'                    ')
                __M_writer(escape(timeline(ondt, log )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 512
            __M_writer(u'                </ul>\n')
            pass
        # SOURCE LINE 514
        __M_writer(u'        </div>\n        <br/>\n        <div class="bclear pb2" style="height : 1.5em; border-bottom : 2px solid gray;">\n            <div class="floatr" style="right : 0px;">\n')
        # SOURCE LINE 518
        if links[0] :
            # SOURCE LINE 519
            __M_writer(u'                    <span class="fntlarge fntbold"><a href="')
            __M_writer(escape(links[0]))
            __M_writer(u'">&#171;</a></span>\n')
            pass
        # SOURCE LINE 521
        __M_writer(u'\n')
        # SOURCE LINE 522
        if links[1] :
            # SOURCE LINE 523
            __M_writer(u'                    <span class="fntlarge fntbold ml5"><a href="')
            __M_writer(escape(links[1]))
            __M_writer(u'">&#8249;</a></span>\n')
            pass
        # SOURCE LINE 525
        __M_writer(u'\n                <span class="ml5">')
        # SOURCE LINE 526
        __M_writer(escape(fromoff))
        __M_writer(u'-')
        __M_writer(escape(tooff))
        __M_writer(u'</span>\n\n')
        # SOURCE LINE 528
        if links[2] :
            # SOURCE LINE 529
            __M_writer(u'                    <span class="fntlarge fntbold ml5"><a href="')
            __M_writer(escape(links[2]))
            __M_writer(u'">&#8250;</a></span>\n')
            pass
        # SOURCE LINE 531
        __M_writer(u'            <span class="fntbold">&ensp;</span>\n            </div>\n        </div>\n    </div>\n\n    <script type="text/javascript">\n        function logmsg( n, what ) {\n            if( what == \'expand\' ) {\n                dojo.toggleClass( n, \'dispblk\', true );\n                dojo.toggleClass( n, \'ml50\', true );\n                dojo.toggleClass( n.parentNode, \'wsnowrap\', false );\n                dojo.toggleClass( n, \'wsprewrap\', true );\n            } else {\n                dojo.toggleClass( n, \'dispblk\', false );\n                dojo.toggleClass( n, \'ml50\', false );\n                dojo.toggleClass( n.parentNode, \'wsnowrap\', true );\n                dojo.toggleClass( n, \'wsprewrap\', false );\n            }\n        }\n\n        function pntr_onclick( n_logmsg, e ) {\n            dojo.hasClass( n_logmsg, \'dispblk\' ) ? \n                logmsg( n_logmsg, \'summary\' ) : logmsg( n_logmsg, \'expand\' ) ;\n            dojo.stopEvent(e);\n        }\n        function setup_timeline() {\n            dojo.setObject( \'span_expand\', dojo.query( \'span[name=expand]\' )[0] );\n            dojo.forEach(\n                dojo.query( \'.tlog\' ),\n                function( n ) {\n                    var n_pntr   = dojo.query( \'span[name=interface]\', n )[0]\n                    var n_logmsg = dojo.query( \'span[name=logmsg]\', n )[0]\n                    dojo.connect(\n                        n_pntr, \'onclick\',\n                        dojo.partial( pntr_onclick, n_logmsg )\n                    );\n                }\n            );\n            dojo.connect(\n                span_expand, \'onclick\', \n                function(e) {\n                    dojo.forEach(\n                        dojo.query( \'span[name=logmsg]\' ),\n                        function( n ) {\n                            if( span_expand.innerHTML == \'Summary\' ) {\n                                logmsg( n, \'summary\' ) \n                            } else {\n                                logmsg( n, \'expand\') ;\n                            }\n                        }\n                    );\n                    span_expand.innerHTML = span_expand.innerHTML == \'Expand\' ?\n                                                \'Summary\' : \'Expand\'\n                    dojo.stopEvent(e);\n                }\n            );\n        }\n        dojo.addOnLoad( setup_timeline );\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_favoriteicon(context,name,classes=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 215
        __M_writer(u'\n    <span name="')
        # SOURCE LINE 216
        __M_writer(escape(name))
        __M_writer(u'" title="add or delete as your favorite"\n        class="favdeselected pointer fntlarge ')
        # SOURCE LINE 217
        __M_writer(escape(classes))
        __M_writer(u'"></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_showpeople(context,u,p,r,projusers,usernames,revweditable):
    context.caller_stack._push_frame()
    try:
        forms = _mako_get_namespace(context, 'forms')
        h = context.get('h', UNDEFINED)
        set = context.get('set', UNDEFINED)
        list = context.get('list', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 594
        __M_writer(u'\n    ')
        # SOURCE LINE 595

        participants_ = [ u.username for u in r.participants ]
        x_participants = sorted(list(
                            set( usernames ).difference( set( participants_ ))
                         ))
        'admin' in x_participants and x_participants.remove('admin')
        'anonymous' in x_participants and x_participants.remove('anonymous')
            
        
        # SOURCE LINE 602
        __M_writer(u'\n    <div id="revwinfo">\n        <div class="fggray fntbold pt5 pb5 ml10"> Author </div>\n')
        # SOURCE LINE 605
        if revweditable :
            # SOURCE LINE 606
            __M_writer(u'            <div class="ml20">\n            ')
            # SOURCE LINE 607
            __M_writer(escape(forms.form_revwauthor(u, p, r, h.suburl_revwauthor, projusers)))
            __M_writer(u'\n            </div>\n')
            # SOURCE LINE 609
        else :
            # SOURCE LINE 610
            __M_writer(u'            ')
            authorname = r.author and r.author.username or '-' 
            
            __M_writer(u'\n            <div class="ml20">\n')
            # SOURCE LINE 612
            if r.author :
                # SOURCE LINE 613
                __M_writer(u'                <a href="')
                __M_writer(escape(h.url_foruser( authorname )))
                __M_writer(u'">')
                __M_writer(escape(authorname))
                __M_writer(u'</a>\n')
                # SOURCE LINE 614
            else :
                # SOURCE LINE 615
                __M_writer(u'                <span>')
                __M_writer(escape(authorname))
                __M_writer(u'</span>\n')
                pass
            # SOURCE LINE 617
            __M_writer(u'            </div>\n')
            pass
        # SOURCE LINE 619
        __M_writer(u'        <hr/>\n        <div class="fggray fntbold pt5 pb5 ml10"> Moderator </div>\n')
        # SOURCE LINE 621
        if revweditable :
            # SOURCE LINE 622
            __M_writer(u'            <div class="ml20">\n            ')
            # SOURCE LINE 623
            __M_writer(escape(forms.form_revwmoderator( u, p, r, h.suburl_revwmoderator, projusers )))
            __M_writer(u'\n            </div>\n')
            # SOURCE LINE 625
        else :
            # SOURCE LINE 626
            __M_writer(u'            ')
 
            moderatorname = r.moderator and r.moderator.username or '-'
                        
            
            # SOURCE LINE 628
            __M_writer(u'\n            <div class="ml20">\n')
            # SOURCE LINE 630
            if r.moderator :
                # SOURCE LINE 631
                __M_writer(u'                <a href="')
                __M_writer(escape(h.url_foruser( moderatorname )))
                __M_writer(u'">')
                __M_writer(escape(moderatorname))
                __M_writer(u'</a>\n')
                # SOURCE LINE 632
            else :
                # SOURCE LINE 633
                __M_writer(u'                <span>')
                __M_writer(escape(moderatorname))
                __M_writer(u'</span>\n')
                pass
            # SOURCE LINE 635
            __M_writer(u'            </div>\n')
            pass
        # SOURCE LINE 637
        if u == r.moderator :
            # SOURCE LINE 638
            __M_writer(u'            <div id="revwclosed" class="fgblue pointer ml20 mt10 mb10">\n                ')
            # SOURCE LINE 639
            __M_writer(escape(forms.form_closerev( u, p, r, h.suburl_closerev )))
            __M_writer(u'\n            </div>\n')
            pass
        # SOURCE LINE 642
        __M_writer(u'        <hr/>\n        <div class="fggray fntbold pt5 pb5 ml10"> Participants </div>\n')
        # SOURCE LINE 644
        if revweditable :
            # SOURCE LINE 645
            __M_writer(u'            <div class="ml20">\n                ')
            # SOURCE LINE 646
            __M_writer(escape(forms.form_addparts( u, p, r, h.suburl_addparts, x_participants )))
            __M_writer(u'\n            </div>\n')
            pass
        # SOURCE LINE 649
        __M_writer(u'        <div id="listparts" class="ml20 p5" >\n')
        # SOURCE LINE 650
        for username in sorted([ u.username for u in r.participants ]) :
            # SOURCE LINE 651
            __M_writer(u'        <div>\n')
            # SOURCE LINE 652
            if revweditable :
                # SOURCE LINE 653
                __M_writer(u'            <span username="')
                __M_writer(escape(username))
                __M_writer(u'"\n                  class="closeparticipant mr5 fgred pointer">x</span>\n')
                pass
            # SOURCE LINE 656
            __M_writer(u'            <a href="')
            __M_writer(escape(h.url_foruser( username )))
            __M_writer(u'">')
            __M_writer(escape(username))
            __M_writer(u'</a>\n        </div>\n')
            pass
        # SOURCE LINE 659
        __M_writer(u'        </div>\n        ')
        # SOURCE LINE 660
        __M_writer(escape(forms.form_delparts( u, p, r, h.suburl_delparts )))
        __M_writer(u'\n    </div>\n    <script type="text/javascript">\n        function publish_delpart( username, e ) {\n            dojo.publish( \'delparticipant\', [ username ] );\n            dojo.destroy(\n                dojo.query( \'span[username=\'+username+\']\', dojo.byId( \'listparts\' ) \n                          )[0].parentNode\n            );\n            dojo.stopEvent(e);\n        }\n        function setup_participants() {\n\n            dojoaddOnLoad( \'initform_revwauthor\' );\n            dojoaddOnLoad( \'initform_revwmoderator\' );\n            dojoaddOnLoad( \'initform_closerev\' );\n            dojoaddOnLoad( \'initform_addparts\' );\n            dojoaddOnLoad( \'initform_delparts\' );\n\n            var n_spans = dojo.query(\'div#revwinfo span.closeparticipant\');\n            dojo.forEach( n_spans,\n                function( n ) {\n                    dojo.connect(\n                        n, \'onclick\', \n                        dojo.partial( publish_delpart, dojo.attr( n, \'username\' ))\n                    );\n                }\n            );\n            dojo.subscribe( \n                \'insertparticipant\',\n                function( username ) {\n                    // Create the div\n                    var n_div = dojo.create( \'div\', {}, dojo.byId( \'listparts\' ), \'last\' );\n                    // interface to show and delete the participant.\n                    var n_x = dojo.create( \n                                \'span\', { username : username, innerHTML : \'x \',\n                                          class : "closeparticipant mr5 fgred pointer"\n                                        },\n                                n_div, \'last\'\n                              );\n                    dojo.connect( n_x, \'onclick\', \n                                  dojo.partial( publish_delpart, username ));\n                    dojo.create( \n                        \'a\', { href : url_foruser( username ), innerHTML : username },\n                        n_div, \'last\'\n                    );\n                }\n            );\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_replace_row(context,tup,flines,tlines):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        def diff_row(col1,col2,col3,cls):
            return render_diff_row(context,col1,col2,col3,cls)
        __M_writer = context.writer()
        # SOURCE LINE 402
        __M_writer(u'\n')
        # SOURCE LINE 403
        for ln in range(tup[1], tup[2]) :
            # SOURCE LINE 404
            __M_writer(u'        ')
            __M_writer(escape(diff_row( ln+1, '', flines[ln], 'diffreplace' )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 406
        for ln in range(tup[3], tup[4]) :
            # SOURCE LINE 407
            __M_writer(u'        ')
            __M_writer(escape(diff_row( '', ln+1, tlines[ln], 'diffreplace' )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_timeline(context,ondt,log):
    context.caller_stack._push_frame()
    try:
        def iconize(spantext,iconname,span_name='',classes='',styles='',title=''):
            return render_iconize(context,spantext,iconname,span_name,classes,styles,title)
        __M_writer = context.writer()
        # SOURCE LINE 446
        __M_writer(u'\n    <li class="tlog">\n        <div class="mt5 mb5 ml3 wsnowrap" style="overflow: hidden;">\n            <span class="hoverhighlight fntmono fntmedium">\n                ')
        # SOURCE LINE 450
        __M_writer(escape(iconize( ondt, 'plus_exp', span_name='interface', classes='pointer mr5',
                           title='%s'%log.created_on )))
        # SOURCE LINE 451
        __M_writer(u'\n            </span>\n            <span class="ml5">By ')
        # SOURCE LINE 453
        __M_writer(log.userhtml )
        __M_writer(u'</span>\n            <span>in ')
        # SOURCE LINE 454
        __M_writer(log.itemhtml )
        __M_writer(u'</span>\n            <span name="logmsg" class="ml10 fggray">')
        # SOURCE LINE 455
        __M_writer(escape(log.log))
        __M_writer(u'</span>\n        </div>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainnav(context,mnavtabs,psearchbox,spans=[],rspans=[],tooltips=[]):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def contextnav(spans=[],rspans=[],tooltips=[]):
            return render_contextnav(context,spans,rspans,tooltips)
        def maintabs(tabs,psearchbox):
            return render_maintabs(context,tabs,psearchbox)
        __M_writer = context.writer()
        # SOURCE LINE 98
        __M_writer(u'\n    <div class="brtl10 brtr10">\n    <div class="disptable w100 brtl10 brtr10">\n        <div class="disptrow">\n            <div id="mainnav" class="disptcell vmiddle brtl10 brtr10">\n                ')
        # SOURCE LINE 103
        __M_writer(escape(maintabs(mnavtabs, psearchbox)))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="disptrow">\n            <div id="ctxtnav" class="disptcell">\n                ')
        # SOURCE LINE 108
        __M_writer(escape(contextnav(spans=spans, rspans=rspans, tooltips=tooltips)))
        __M_writer(u'\n            </div>\n        </div>\n        <div class="disptrow">\n            <div class="disptcell">\n')
        # SOURCE LINE 113
        if tooltips :
            # SOURCE LINE 114
            __M_writer(u'                <div id="cont_tooltips"></div>\n')
            pass
        # SOURCE LINE 116
        __M_writer(u'            </div>\n        </div>\n    </div>\n    </div>\n\n    <script type="text/javascript">\n        function contexttooltip() {\n            var n_cont = dojo.byId( \'cont_tooltips\' );\n            var n_trgr = dojo.byId( \'trgr_tooltips\' );\n            if( n_cont && n_trgr ) {\n                new zeta.ToolTips({\n                    n_tooltip : n_trgr,\n                    tooltips: ')
        # SOURCE LINE 128
        __M_writer( h.json.dumps( tooltips ) )
        __M_writer(u'\n                }, n_cont )\n            }\n        };\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tag_spans(context,span_name,form_id,refreshurl):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 301
        __M_writer(u'\n    <span class="m2" name="')
        # SOURCE LINE 302
        __M_writer(escape(span_name))
        __M_writer(u'" form_id="')
        __M_writer(escape(form_id))
        __M_writer(u'" refreshurl="')
        __M_writer(escape(refreshurl))
        __M_writer(u'">\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_lictable1(context,license,editable):
    context.caller_stack._push_frame()
    try:
        def iconize(spantext,iconname,span_name='',classes='',styles='',title=''):
            return render_iconize(context,spantext,iconname,span_name,classes,styles,title)
        __M_writer = context.writer()
        # SOURCE LINE 258
        __M_writer(u'\n    <table class="w100" style="border-collapse : collapse;">\n        <tr>\n            <th class="calign">Id</th>\n            <th class="calign">License name</th>\n            <th class="calign">Projects</th>\n')
        # SOURCE LINE 264
        if editable :
            # SOURCE LINE 265
            __M_writer(u'                <th></th>\n')
            pass
        # SOURCE LINE 267
        __M_writer(u'        </tr>\n')
        # SOURCE LINE 268
        for l in license :
            # SOURCE LINE 269
            __M_writer(u'            ')
            id, licensename, licurl, editurl, rmurl = l[:5] 
            
            __M_writer(u'\n            <tr licensename="')
            # SOURCE LINE 270
            __M_writer(escape(licensename))
            __M_writer(u'">\n                <td class="calign">')
            # SOURCE LINE 271
            __M_writer(escape(id))
            __M_writer(u'</td>\n                <td class="calign"><a class="fntbold" href="')
            # SOURCE LINE 272
            __M_writer(escape(licurl))
            __M_writer(u'">')
            __M_writer(escape(licensename))
            __M_writer(u'</a></td>\n                <td class="calign">\n')
            # SOURCE LINE 274
            for p, href in l[5:] :
                # SOURCE LINE 275
                __M_writer(u'                    <div><a href="')
                __M_writer(escape(href))
                __M_writer(u'">')
                __M_writer(escape(p))
                __M_writer(u'</a></div>\n')
                pass
            # SOURCE LINE 277
            __M_writer(u'                </td>\n')
            # SOURCE LINE 278
            if editable :
                # SOURCE LINE 279
                __M_writer(u'                    <td class="calign">\n                        ')
                # SOURCE LINE 280
                __M_writer(escape(iconize( '', 'trash', span_name='rmlic', classes='fgblue pointer',
                                   title='Remove this license' )))
                # SOURCE LINE 281
                __M_writer(u'\n                    </td>\n')
                pass
            # SOURCE LINE 284
            __M_writer(u'            </tr>\n')
            pass
        # SOURCE LINE 286
        __M_writer(u'    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_attach_spans(context,span_name,form_id,refreshurl):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 296
        __M_writer(u'\n    <span class="m2" name="')
        # SOURCE LINE 297
        __M_writer(escape(span_name))
        __M_writer(u'" form_id="')
        __M_writer(escape(form_id))
        __M_writer(u'" refreshurl="')
        __M_writer(escape(refreshurl))
        __M_writer(u'">\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flashmessages(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 235
        __M_writer(u'\n    ')
        # SOURCE LINE 236
 
       
        allflash = [ ('%s'%m) for m in h.flash.pop_messages() ]
        errors   = [ m.strip( h.ERROR_FLASH ) for m in allflash if h.ERROR_FLASH in m ]
        messages = [ m.strip( h.MESSAGE_FLASH ) for m in allflash if h.MESSAGE_FLASH in m ]
        allflash = errors + messages
        flashcls = (errors and 'bgLSalmon') or (messages and 'bgyellow') or ''
        if allflash :
            style= ""
        else :
            style= "display: none;"
            
        
        # SOURCE LINE 247
        __M_writer(u'\n    <div id="flashblk" class="calign m10 fntsmall fwnormal z100 ')
        # SOURCE LINE 248
        __M_writer(escape(flashcls))
        __M_writer(u' br5"\n         style="')
        # SOURCE LINE 249
        __M_writer(escape(style))
        __M_writer(u'">\n        <div id="flashmsg" class="p2">\n')
        # SOURCE LINE 251
        for message in allflash:
            # SOURCE LINE 252
            __M_writer(u'                ')
            __M_writer(escape(message))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 254
        __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_equal_row(context,tup,flines,tlines):
    context.caller_stack._push_frame()
    try:
        Exception = context.get('Exception', UNDEFINED)
        def diff_row(col1,col2,col3,cls):
            return render_diff_row(context,col1,col2,col3,cls)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 379
        __M_writer(u'\n    ')
        # SOURCE LINE 380

        if tup[2] - tup[1] != tup[4] - tup[3] :
            raise Exception
        len = tup[2] - tup[1]
            
        
        # SOURCE LINE 384
        __M_writer(u'\n')
        # SOURCE LINE 385
        for ln in range(0, len) :
            # SOURCE LINE 386
            __M_writer(u'        ')
            __M_writer(escape( diff_row( tup[1]+ln+1, tup[3]+ln+1, flines[tup[1]+ln], 'diffequal' )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_attachdownloads(context,u,attachments):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 821
        __M_writer(u'\n    ')
        # SOURCE LINE 822
 
        count = 0
        values = [];
        [ values.extend( v ) for v in attachments.values() ]
            
        
        # SOURCE LINE 826
        __M_writer(u'\n    <div id="attachments w100" class="br4" style="border: 3px solid #B3CFB3;">\n    <table class="w100">\n        <tr class="bggrn2">\n            <td class="p3 fntbold" style="width: 21%;">filename</td>\n            <td class="p3 fntbold" style="">summary</td>\n            <td class="p3 fntbold" style="width: 7%;">uploader</td>\n            <td class="p3 fntbold" style="width: 10em;;">created-on</td>\n            <td class="p3 fntbold" style="width: 8%;">downloads</td>\n            <td class="p3 fntbold" style="width: 8%;">size</td>\n        </tr>\n')
        # SOURCE LINE 837
        for att in values :
            # SOURCE LINE 838
            __M_writer(u'            ')

            createdon = att[5] and h.utc_2_usertz( att[5], u.timezone ).strftime("%a, %b %d, %Y")
            count += 1
            bgrnd = (count%2 == 0) and 'bggray1' or ''
                        
            
            # SOURCE LINE 842
            __M_writer(u'\n            <tr class="')
            # SOURCE LINE 843
            __M_writer(escape(bgrnd))
            __M_writer(u'">\n                <td class="p5 fggray" style="width: 15%">\n                    <a href="')
            # SOURCE LINE 845
            __M_writer(escape(h.url_for( h.r_attachdownl, id=att[0] )))
            __M_writer(u'">')
            __M_writer(escape(att[1]))
            __M_writer(u'</a>\n                </td>\n                <td class="p5" style="">\n                    <span name="summary" attid="')
            # SOURCE LINE 848
            __M_writer(escape(att[0]))
            __M_writer(u'" class="inedit">')
            __M_writer(escape(att[3]))
            __M_writer(u'</span>\n                </td>\n                <td class="p5 fggray" style="width: 5%;">\n                    <a href="')
            # SOURCE LINE 851
            __M_writer(escape(h.url_foruser( att[6] )))
            __M_writer(u'">')
            __M_writer(escape(att[6]))
            __M_writer(u'</a>\n                </td>\n                <td class="p5 fggray" style="width: 10em;">')
            # SOURCE LINE 853
            __M_writer(escape(createdon))
            __M_writer(u'</td>\n                <td class="p5 fggray" style="width: 8%;">')
            # SOURCE LINE 854
            __M_writer(escape(att[4]))
            __M_writer(u'</td>\n                <td class="p5 fggray" style="width: 8%;">')
            # SOURCE LINE 855
            __M_writer(escape(att[2]/1024))
            __M_writer(u' KB</td>\n            </tr>\n')
            # SOURCE LINE 857
            if att[6] :
                # SOURCE LINE 858
                __M_writer(u'            <tr class="fntitalic ')
                __M_writer(escape(bgrnd))
                __M_writer(u'">\n                <td class="pl5 fntitalic fggreen" colspan="7">\n                    <span>( ')
                # SOURCE LINE 860
                __M_writer(escape(att[6]))
                __M_writer(u' )</span>\n                </td>\n            </tr>\n')
                pass
            pass
        # SOURCE LINE 865
        __M_writer(u'    </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_insert_row(context,tup,flines,tlines):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        def diff_row(col1,col2,col3,cls):
            return render_diff_row(context,col1,col2,col3,cls)
        __M_writer = context.writer()
        # SOURCE LINE 396
        __M_writer(u'\n')
        # SOURCE LINE 397
        for ln in range(tup[3], tup[4]) :
            # SOURCE LINE 398
            __M_writer(u'        ')
            __M_writer(escape(diff_row( '', ln+1, tlines[ln], 'diffinsert' )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_difftable(context,oldver,newver,flines,tlines):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def diff_row(col1,col2,col3,cls):
            return render_diff_row(context,col1,col2,col3,cls)
        def replace_row(tup,flines,tlines):
            return render_replace_row(context,tup,flines,tlines)
        def equal_row(tup,flines,tlines):
            return render_equal_row(context,tup,flines,tlines)
        def delete_row(tup,flines,tlines):
            return render_delete_row(context,tup,flines,tlines)
        def insert_row(tup,flines,tlines):
            return render_insert_row(context,tup,flines,tlines)
        __M_writer = context.writer()
        # SOURCE LINE 411
        __M_writer(u'\n    ')
        # SOURCE LINE 412
        m = h.SequenceMatcher( None, flines, tlines ) 
        
        __M_writer(u'\n    <div class="difflegend mt10">\n        <dl>\n            <dt class="unmod"></dt><dd class="ml5">Un-modified</dd>\n            <dt class="del"></dt><dd class="ml5">Deleted</dd>\n            <dt class="ins"></dt><dd class="ml5">Inserted</dd>\n            <dt class="rep"></dt><dd class="ml5">Replaced</dd>\n        </dl>\n    </div>\n    <table class="zwdiff">\n        <thead><tr>\n            <th class="oldver">v')
        # SOURCE LINE 423
        __M_writer(escape(oldver))
        __M_writer(u'</th>\n            <th class="newver">v')
        # SOURCE LINE 424
        __M_writer(escape(newver))
        __M_writer(u'</th>\n            <th class="verdiff">Difference</th>\n        </tr></thead>\n')
        # SOURCE LINE 427
        for cluster in m.get_grouped_opcodes() :
            # SOURCE LINE 428
            __M_writer(u'            ')
            __M_writer(escape(diff_row( '...', '...', '', 'skip' )))
            __M_writer(u'\n')
            # SOURCE LINE 429
            for tup in cluster :
                # SOURCE LINE 430
                if tup[0] == 'equal' :
                    # SOURCE LINE 431
                    __M_writer(u'                    ')
                    __M_writer(escape(equal_row( tup, flines, tlines )))
                    __M_writer(u'\n')
                    # SOURCE LINE 432
                elif tup[0] == 'delete' :
                    # SOURCE LINE 433
                    __M_writer(u'                    ')
                    __M_writer(escape(delete_row( tup, flines, tlines )))
                    __M_writer(u'\n')
                    # SOURCE LINE 434
                elif tup[0] == 'insert' :
                    # SOURCE LINE 435
                    __M_writer(u'                    ')
                    __M_writer(escape(insert_row( tup, flines, tlines )))
                    __M_writer(u'\n')
                    # SOURCE LINE 436
                elif tup[0] == 'replace' :
                    # SOURCE LINE 437
                    __M_writer(u'                    ')
                    __M_writer(escape(replace_row( tup, flines, tlines )))
                    __M_writer(u'\n')
                    pass
                pass
            pass
        # SOURCE LINE 441
        __M_writer(u'    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_panes(context,userpanes):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 185
        __M_writer(u'\n    <table class="w100"><tr>\n    <td id="collapseup" style="width : 7px;" class="pointer vmiddle inactive">\n        <div style="cursor : default; width : 7px; background-color : transparent;">&#187;<div>\n    </td>\n    <td id="coluserpane">\n        <div class="pt5 w100 pl1pc">\n            <div class="fntsmall w100 ralign">\n                <span id="uprefresh" class="fgblue pointer">refresh</span>\n                &ensp;\n                <span id="upcolexp" class="fgblue pointer">collapse</span>\n            </div>\n\n            <div style="border : thin dotted black; padding : 0px 3px 0 3px; margin : 3px 0px 3px 0;"\n                 class="fntsmall 100" id="adduserpanes">\n')
        # SOURCE LINE 200
        for up in userpanes :
            # SOURCE LINE 201
            __M_writer(u'                    <span class="fgblue pointer" title="')
            __M_writer(escape(up))
            __M_writer(u'">')
            __M_writer(escape(up))
            __M_writer(u'&ensp;</span>\n')
            pass
        # SOURCE LINE 203
        __M_writer(u'            </div>\n\n            <div id=\'userpanes\' class="w100">\n')
        # SOURCE LINE 206
        for up in userpanes :
            # SOURCE LINE 207
            __M_writer(u'                <div title="')
            __M_writer(escape(up))
            __M_writer(u'"></div>\n')
            pass
        # SOURCE LINE 209
        __M_writer(u'            </div>\n        </div>\n    </td>\n    </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_iconize(context,spantext,iconname,span_name='',classes='',styles='',title=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 220
        __M_writer(u'\n    ')
        # SOURCE LINE 221
        iconfile = iconmap.get( iconname, '' ) 
        
        __M_writer(u'\n    <span name="')
        # SOURCE LINE 222
        __M_writer(escape(span_name))
        __M_writer(u'" class="pl18 iconize ')
        __M_writer(escape(classes))
        __M_writer(u'" title="')
        __M_writer(escape(title))
        __M_writer(u'"\n          style="')
        # SOURCE LINE 223
        __M_writer(escape(styles))
        __M_writer(u'; background : transparent url(')
        __M_writer(escape(iconfile))
        __M_writer(u') no-repeat scroll 0;">\n        ')
        # SOURCE LINE 224
        __M_writer(spantext )
        __M_writer(u'&ensp;\n    </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contextnav(context,spans=[],rspans=[],tooltips=[]):
    context.caller_stack._push_frame()
    try:
        def iconize(spantext,iconname,span_name='',classes='',styles='',title=''):
            return render_iconize(context,spantext,iconname,span_name,classes,styles,title)
        __M_writer = context.writer()
        # SOURCE LINE 160
        __M_writer(u'\n')
        # SOURCE LINE 161
        for span in spans :
            # SOURCE LINE 162
            __M_writer(u'        ')
            __M_writer(span )
            __M_writer(u'\n')
            pass
        # SOURCE LINE 164
        __M_writer(u'\n')
        # SOURCE LINE 165
        if rspans :
            # SOURCE LINE 166
            __M_writer(u'        <div class="floatr">\n')
            # SOURCE LINE 167
            for span in rspans :
                # SOURCE LINE 168
                __M_writer(u'                ')
                __M_writer(span )
                __M_writer(u'\n')
                pass
            # SOURCE LINE 170
            __M_writer(u'        </div>\n')
            pass
        # SOURCE LINE 172
        __M_writer(u'\n')
        # SOURCE LINE 173
        if tooltips :
            # SOURCE LINE 174
            __M_writer(u'        <span id=\'trgr_tooltips\' title="Tips on how to use this page" \n             style="margin: 5px 5px 0px 10px;" class="fgblue pointer">\n            ')
            # SOURCE LINE 176
            __M_writer(escape(iconize( '', 'tooltips', styles="height: 16px;" )))
            __M_writer(u'\n        </span>\n')
            # SOURCE LINE 178
        else :
            # SOURCE LINE 179
            __M_writer(u'        <span id=\'trgr_tooltips\' title="Tips on how to use this page" \n             style="margin: 5px 5px 0px 10px;" class="fggray">\n        </span>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_iconlink(context,link,iconname,anchor_name='',classes='',styles='',title=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 228
        __M_writer(u'\n    ')
        # SOURCE LINE 229
        iconfile = iconmap.get( iconname, '' ) 
        
        __M_writer(u'\n    <a name="')
        # SOURCE LINE 230
        __M_writer(escape(anchor_name))
        __M_writer(u'" class="anchorlink ')
        __M_writer(escape(classes))
        __M_writer(u' br4" title="')
        __M_writer(escape(title))
        __M_writer(u'" \n       style="')
        # SOURCE LINE 231
        __M_writer(escape(styles))
        __M_writer(u';" href="')
        __M_writer(escape(link))
        __M_writer(u'"\n       ><img src="')
        # SOURCE LINE 232
        __M_writer(escape(iconfile))
        __M_writer(u'" class="vmiddle"/></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


