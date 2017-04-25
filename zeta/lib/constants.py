# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Avoid using magic numbers. Instead use contants."""

# -*- coding: utf-8 -*-

# Gotchas : None
#   1. When changing the following regular expression string(s), make sure to
#      change the regular expressions encoded in the form template(s).
# Notes   : None
# Todo    :
#   1. Most of the Contants define the limitations of the product. Document
#      them somewhere.

LEN_SYSFIELD       = 64
LEN_SYSVALUE       = 256

LEN_NAME           = 32
LEN_NAME1          = 64
LEN_SUMMARY        = 128
LEN_256            = 256
LEN_DESCRIBE       = 65536

LEN_EMAILID        = 64
LEN_TZ             = 32
LEN_ADDRLINE       = 64
LEN_PINCODE        = 8

LEN_TAGNAME        = 256
LEN_RESOURCEURL    = 512
LEN_LICENSENAME    = 64
LEN_LICENSESOURCE  = 128

LEN_QUERYSTRING    = 1024
LEN_1K             = 1024

LEN_ATTACHSIZE     = 1024*1024*10  # 10 MB Maximum attachment size.

DUMMY_EMAIL        = u'email.id@host.name'
DUMMY_PASSWORD     = 'admin123'
ADMIN_EMAIL        = u'admin.email@host.name'
ADMIN_PASSWORD     = 'admin123'
ANONYMOUS_EMAIL    = u'anonymous.id@host.name'
ANONYMOUS_PASSWORD = 'anonymous123'
DEFAULT_TIMEZONE   = 'UTC'

ATTACH_DIR         = 'fileattach'
DIR_STATICWIKI     = 'staticfiles'
PROJHOMEPAGE       = 'homepage'

ACCOUNTS_ACTIONS   = [ 'newaccount', 'signin', 'signout', 'forgotpass' ]

ERROR_FLASH        = 'error ::'
MESSAGE_FLASH      = 'message ::'

MAX_BREADCRUMBS    = 6

IFRAME_RET         = '<html> <body> <textarea>{ result : "OK" }</textarea> </body> </html>'

# When changing the following regular expression string(s), make sure to change
# the regular expressions encoded in the form template(s).
RE_UNAME           = r'^[a-z0-9_]{3,32}$'       # `username` restrictions
RE_EMAIL           = r'^.*@.*$'
RE_PASSWD          = r'^.{4,64}$'
RE_PNAME           = r'^[A-Za-z0-9_.]{1,32}$'   # `projectname` restrictions
RE_TNAME           = r'^[A-Za-z0-9_.!]{1,256}$' # `tagname` restrictions

TLCOUNT            = 100
MAIL_STARTCOUNT    = 1

# Wiki types and content types
WIKITYPES          = [ u'html', u'text', u'iframe', u'redirect', u'zwiki' ]
EMPTYWIKITYPES     = [ u'redirect' ]
WIKITYPE_HTML      = u'html' 
WIKITYPE_TEXT      = u'text'
WIKITYPE_ZWIKI     = u'zwiki'
WIKITYPE_IFRAME    = u'iframe' 
WIKITYPE_REDIRECT  = u'redirect'

MNT_CONTENTTYPES   = [ u'html', u'text', u'zwiki' ]
MNT_HTMLCONTENT    = u'html'
MNT_TEXTCONTENT    = u'text'
MNT_ZWIKICONTENT   = u'zwiki'

CNTTYPE2WIKITYPE   = {
    u'html'  : u'html',
    u'text'  : u'text',
    u'zwiki' : u'zwiki',
}

MAX2SWITCH_ALPHAINDEX = 100
