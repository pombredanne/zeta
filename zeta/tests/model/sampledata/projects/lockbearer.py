lockbearer_description = \
u"""
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most
straightforward and flexible models available, while also maintaining close
ties to Python calling and scoping semantics.

Mako is used by the python.org website as the basis for their site build
system (README), as well as by reddit.com for their newly launched beta site.
It is the default template language included with the Pylons web framework.
"""

lockbearer_compdesc    = \
[
u"""
Template exceptions can occur in two distinct places. One is when you lookup,
parse and compile the template, the other is when you run the template. Within
the running of a template, exceptions are thrown normally from whatever Python
code originated the issue. Mako has its own set of exception classes which
mostly apply to the lookup and lexer/compiler stages of template construction.
Mako provides some library routines that can be used to help provide
Mako-specific information about any exception's stack trace, as well as
formatting the exception within textual or HTML format. In all cases, the main
value of these handlers is that of converting Python filenames, line numbers,
and code samples into Mako template filenames, line numbers, and code samples.
All lines within a stack trace which correspond to a Mako template module will
be converted to be against the originating template file.
""",
u"""
The standard plugin methodology used by Turbogears as well as Pylons is
included in the module mako.ext.turbogears, using the TGPlugin class. This is
also a setuptools entrypoint under the heading python.templating.engines with
the name mako.
""",
u"""
A sample WSGI application is included in the distrubution in the file
examples/wsgi/run_wsgi.py. This runner is set up to pull files from a
templates as well as an htdocs directory and includes a rudimental two-file
layout. The WSGI runner acts as a fully functional standalone web server,
using wsgiutils to run itself, and propagates GET and POST arguments from the
request into the Context, can serve images, css files and other kinds of
files, and also displays errors using Mako's included exception-handling
utilities.
""",
u"""
A Pygments-compatible syntax highlighting module is included under
mako.ext.pygmentplugin. This module is used in the generation of Mako
documentation and also contains various setuptools entry points under the
heading pygments.lexers, including mako, html+mako, xml+mako (see the setup.py
file for all the entry points).
""",
]

lockbearer_mstndesc    = \
[
u"""
# inlined the "write" function of Context into a local template variable. This affords a 12-30% speedup in template render time. (idea courtesy same anonymous guest) [ticket:76]
# added "attr" accessor to namespaces. Returns attributes configured as module level attributes, i.e.  within <%! %> sections.  [ticket:62] i.e.: 
# cache_key argument can now render arguments passed directly to the %page or %def, i.e. <%def name="foo(x)" cached="True" cache_key="${x}"/> [ticket:78]
# some functions on Context are now private: _push_buffer(), _pop_buffer(), caller_stack._push_frame(), caller_stack._pop_frame().
# added a runner script "mako-render" which renders standard input as a template to stdout [ticket:81] [ticket:56]
""",
u"""
# can now use most names from __builtins__ as variable names without explicit declaration (i.e. 'id', 'exception', 'range', etc.) [ticket:83] [ticket:84]
# can also use builtin names as local variable names (i.e. dict, locals) (came from fix for [ticket:84])
# fixed bug in python generation when variable names are used with identifiers like "else", "finally", etc.  inside them [ticket:68]
# fixed codegen bug which occured when using <%page> level caching, combined with an expression-based cache_key, combined with the usage of <%namespace import="*"/> - fixed lexer exceptions not cleaning up temporary files, which could lead to a maximum number of file descriptors used in the process [ticket:69] 
# fixed issue with inline format_exceptions that was producing blank exception pages when an inheriting template is present [ticket:71] 
# format_exceptions will apply the encoding options of html_error_template() to the buffered output
# rewrote the "whitespace adjuster" function to work with more elaborate combinations of quotes and comments [ticket:75]
""",
u"""
# fixed propagation of 'caller' such that nested %def calls within a <%call> tag's argument list propigates 'caller' to the %call function itself (propigates to the inner calls too, this is a slight side effect which previously existed anyway)
# fixed bug where local.get_namespace() could put an incorrect "self" in the current context
# fixed another namespace bug where the namespace functions did not have access to the correct context containing their 'self' and 'parent'
# filters.Decode filter can also accept a non-basestring object and will call str() + unicode() on it [ticket:47]
# comments can be placed at the end of control lines, i.e. if foo: # a comment, [ticket:53], thanks to Paul Colomiets
# fixed expressions and page tag arguments and with embedded newlines in CRLF templates, follow up to [ticket:16], thanks Eric Woroshow
# added an IOError catch for source file not found in RichTraceback exception reporter [ticket:51]
""",
u"""
# variable names declared in render methods by internal codegen prefixed by "__M_" to prevent name collisions with user code
# added a Babel (http://babel.edgewall.org/) extractor entry point, allowing extraction of gettext messages directly from mako templates via Babel [ticket:45]
# fix to turbogears plugin to work with dot-separated names (i.e. load_template('foo.bar')).  also takes file extension as a keyword argument (default is 'mak').
# more tg fix:  fixed [ticket:35], allowing string-based templates with tgplugin even if non-compatible args were sent
# one small fix to the unit tests to support python 2.3
# a slight hack to how cache.py detects Beaker's memcached, works around unexplained import behavior observed on some python 2.3 installations
""",
u"""
# caching is now supplied directly by Beaker, which has all of MyghtyUtils merged into it now.  The latest Beaker (0.7.1) also fixes a bug related to how Mako was using the cache API.
# fix to module_directory path generation when the path is "./" [ticket:34]
# TGPlugin passes options to string-based templates [ticket:35]
# added an explicit stack frame step to template runtime, which allows much simpler and hopefully bug-free tracking of 'caller', fixes #28
# if plain Python defs are used with <%call>, a decorator @runtime.supports_callable exists to ensure that the "caller" stack is properly handled for the def.
# fix to RichTraceback and exception reporting to get template source code as a unicode object #37
""",
]

lockbearer_verdesc     = \
[
u"""
* Added a "decorator" kw argument to <%def>, allows custom decoration functions to wrap rendering callables.  Mainly intended for custom caching algorithms, not sure what other uses there may be (but there may be).  Examples are in the "filtering" docs.
* When Mako creates subdirectories in which to store templates, it uses the more permissive mode of 0775 instead of 0750, helping out with certain multi-process scenarios. Note that the mode is always subject to the restrictions of the existing umask. [ticket:101]
* Fixed namespace.__getattr__() to raise AttributeError on attribute not found instead of RuntimeError.  [ticket:104] 
* Added last_modified accessor to Template, returns the time.time() when the module was created. [ticket:97]
* Fixed lexing support for whitespace around '=' sign in defs. [ticket:102]
* Removed errant "lower()" in the lexer which was causing tags to compile with case-insensitive names, thus messing up custom <%call> names. [ticket:108]
* Fixed compatibility with Jython 2.5b1.
""",
u"""
* the <%namespacename:defname> syntax described at http://techspot.zzzeek.org/?p=28 has now been added as a built in syntax, and is recommended as a more modern syntax versus <%call expr="expression">.  The %call tag itself will always remain, with <%namespacename:defname> presenting a more HTML-like alternative to calling defs, both plain and nested.  Many examples of the new syntax are in the "Calling a def with embedded content" section of the docs.
* added support for Jython 2.5.
* cache module now uses Beaker's CacheManager object directly, so that all cache types are included.  memcached is available as both "ext:memcached" and "memcached", the latter for backwards compatibility.
* added "cache" accessor to Template, Namespace.  e.g.  ${local.cache.get('somekey')} or template.cache.invalidate_body()
* added "cache_enabled=True" flag to Template, TemplateLookup.  Setting this to False causes cache operations to "pass through" and execute every time; this flag should be integrated in Pylons with its own cache_enabled configuration setting.
""",
u"""
* the Cache object now supports invalidate_def(name), invalidate_body(), invalidate_closure(name), invalidate(key), which will remove the given key from the cache, if it exists.  The cache arguments (i.e. storage type) are derived from whatever has been already persisted for that template.  [ticket:92]
* For cache changes to work fully, Beaker 1.1 is required.  1.0.1 and up will work as well with the exception of cache expiry.  Note that Beaker 1.1 is **required** for applications which use dynamically generated keys, since previous versions will permanently store state in memory for each individual key, thus consuming all available memory for an arbitrarily large number of distinct keys.
* fixed bug whereby an <%included> template with <%page> args named the same as a __builtin__ would not honor the default value specified in <%page> [ticket:93] 
* fixed the html_error_template not handling tracebacks from normal .py files with a magic encoding comment [ticket:88] 
* RichTraceback() now accepts an optional traceback object to be used in place of sys.exc_info()[2].  html_error_template() and text_error_template() accept an optional render()-time argument "traceback" which is passed to the RichTraceback object.  
""",
u"""
* added ModuleTemplate class, which allows the construction of a Template given a Python module generated by a previous Template.   This allows Python modules alone to be used as templates with no compilation step.   Source code and template source are optional but allow error reporting to work correctly.
* fixed Python 2.3 compat. in mako.pyparser [ticket:90]
* fix Babel 0.9.3 compatibility; stripping comment tags is now optional (and enabled by default).
* cached blocks now use the current context when rendering an expired section, instead of the original context passed in [ticket:87]
* fixed a critical issue regarding caching, whereby a cached block would raise an error when called within a cache-refresh operation that was initiated after the initiating template had completed rendering.
""",
u"""
* fixed bug where 'output_encoding' parameter would prevent render_unicode() from returning a unicode object.
* bumped magic number, which forces template recompile for this version (fixes incompatible compile symbols from 0.1 series).
* added a few docs for cache options, specifically those that help with memcached.
* Speed improvements (as though we needed them, but people contributed and there you go):
* added "bytestring passthru" mode, via `disable_unicode=True` argument passed to Template or TemplateLookup. All unicode-awareness and filtering is turned off, and template modules are generated with the appropriate magic encoding comment. In this mode, template expressions can only receive raw bytestrings or Unicode objects which represent straight ASCII, and render_unicode() may not be used if multibyte characters are present. When enabled, speed improvement around 10-20%. [ticket:77] (courtesy anonymous guest)
""",
]

lockbearer_comments    = \
[
u"""
Removed errant "lower()" in the lexer which
  was causing tags to compile with 
  case-insensitive names, thus messing up
  custom <%call> names. [ticket:108]


""",
u"""
When Mako creates subdirectories in which
  to store templates, it uses the more
  permissive mode of 0775 instead of 0750,
  helping out with certain multi-process 
  scenarios. Note that the mode is always
  subject to the restrictions of the existing
  umask. [ticket:101]


""",
u"""
Fixed namespace.__getattr__() to raise 
  AttributeError on attribute not found 
  instead of RuntimeError.  [ticket:104]


""",
u"""
Added a "decorator" kw argument to <%def>,
  allows custom decoration functions to wrap
  rendering callables.  Mainly intended for
  custom caching algorithms, not sure what
  other uses there may be (but there may be).
  Examples are in the "filtering" docs.


""",
u"""
Fixed lexing support for whitespace
  around '=' sign in defs. [ticket:102]


""",
u"""
doc corrections
fixes #100

""",
u"""
Added last_modified accessor to Template,
  returns the time.time() when the module
  was created. [ticket:97]


""",
u"""
whitespace
""",
u"""
reapply the _fields check, it's needed for CPython 2.5
""",
u"""
fixed compat. with the upcoming Jython 2.5b1 by removing all the Jython
workarounds; its AST matches CPython's pretty closely

""",
u"""
don't assume dict ordering
""",
u"""
bump to 0.2.4dev
""",
u"""
beaker 1.1

""",
u"""
use __builtin__, __builtins__ is an implementation detail
""",
u"""
fixed bug whereby an <%included> template with 
  <%page> args named the same as a __builtin__ would not
  honor the default value specified in <%page> [ticket:93]


""",
u"""
put parenthesis around expressions from ${} blocks inside of attributes to 
better support grouping

""",
u"""
support blank tag attributes

""",
u"""
RichTraceback() now accepts an optional traceback object
  to be used in place of sys.exc_info()[2].  html_error_template() 
  and text_error_template() accept an optional
  render()-time argument "traceback" which is passed to the
  RichTraceback object.
lexer tests now rely upon an always-sorted dict repr()

""",
u"""
the <%namespacename:defname> syntax described at
  http://techspot.zzzeek.org/?p=28 has now 
  been added as a built in syntax, and is recommended
  as a more modern syntax versus <%call expr="expression">.
  The %call tag itself will always remain, 
  with <%namespacename:defname> presenting a more HTML-like
  alternative to calling defs, both plain and 
  nested.  Many examples of the new syntax are in the
  "Calling a def with embedded content" section
  of the docs.


""",
u"""
don't assume dict ordering
""",
u"""
whitespace
""",
u"""
we don't have to split('.') either on Jython now
""",
u"""
beaker bump
added "cache_enabled=True" flag to Template, 
  TemplateLookup.  Setting this to False causes cache
  operations to "pass through" and execute every time;
  this flag should be integrated in Pylons with its own
  cache_enabled configuration setting.


""",
u"""
Beaker 1.0.4 isn't out yet, require dev for now
""",
u"""
caching now uses beaker.cache_manager directly.  For best results
use Beaker 1.0.4, just checked in.   This version of Beaker stores
no persistent state in memory for each key, allowing dynamically
generated keys to work without using up available memory.

""",
u"""
cache sends in a "defname" parameter so that the cache can map settings to that name, instead of the key.
eliminates the need to store all Value objects which will use up RAM in a dynamic-key scenario.

""",
u"""
update to latest Jython AST class name mappings
""",
u"""
bump to 0.2.3dev
""",
u"""
added "cache" accessor to Template, Namespace.
  e.g.  ${local.cache.get('somekey')} or
  template.cache.invalidate_body()

the Cache object now supports invalidate_def(name),
  invalidate_body(), invalidate_closure(name), 
  invalidate(key), which will remove the given key 
  from the cache, if it exists.  The cache arguments
  (i.e. storage type) are derived from whatever has
  been already persisted for that template.
  [ticket:92]


""",
u"""
doc fixes including [ticket:89]

""",
u"""
o fix compatibility with babel 0.9.3: stripping comment tags is now optional
and babel is responisble for stripping them when necessary
o remove the no longer needed Unicode/Str ast hack for Jython

""",
u"""
merge trunk@400:branches/jython@400 to trunk
adds support for Jython 2.5

""",
u"""
fix Python 2.3 compat
fixes #90
""",
u"""
added docs for self.attr, template.get_def()

""",
u"""
correction

""",
u"""
fixed cache code to work with Beaker 1.0.1, which is now the required version of Beaker.
removed unnecessary attributes from DefTemplate.
added ModuleTemplate class, which allows the construction
of a Template given a Python module generated by a previous
Template.   This allows Python modules alone to be used
as templates with no compilation step.   Source code
and template source are optional but allow error reporting
to work correctly.


""",
u"""
cache module now uses Beaker's clsmap to get at 
container classes, so cache types such as 
"ext:google", "ext:sqla", etc. are available.  
memcached is available as both "ext:memcached" and
"memcached", the latter for backwards compatibility.


""",
u"""
fix the html_error_template not handling tracebacks from normal .py files with
a magic encoding comment

""",
u"""
<%include> accepts args !

""",
u"""
cached blocks now use the current context when rendering
an expired section, instead of the original context
passed in [ticket:87]


""",
u"""
fixed a critical issue regarding caching, whereby 
a cached block would raise an error when called within a
cache-refresh operation that was initiated after the 
initiating template had completed rendering.


""",
u"""
bumped genhtml version #

""",
u"""
bumped magic number, which forces template recompile for 
this version (fixes incompatible compile symbols from 0.1 
series).
added a few docs for cache options, specifically those that
help with memcached.


""",
u"""
fixed bug where 'output_encoding' parameter would prevent 
render_unicode() from returning a unicode object


""",
u"""
bump version number
""",
u"""
added a runner script "mako-render" which renders 
standard input as a template to stdout [ticket:81] 
[ticket:56]


""",
u"""
dict/locals placed in mako-private namespace, [ticket:84]

""",
u"""
  - can now use most names from __builtins__ as variable
    names without explicit declaration (i.e. 'id', 
    'exception', 'range', etc.) [ticket:83]


""",
u"""
merge r360 from branches/jython
""",
u"""
some refinements to FastEncodingBuffer re: unicode
fixed buffering when disable_unicode is used

""",
u"""
footnote to [ticket:76] - inlined FastEncodingBuffer's write() method

""",
u"""
CHANGES cleanup
some functions on Context are now private:
_push_buffer(), _pop_buffer(),
caller_stack._push_frame(), caller_stack._pop_frame().
implemented [ticket:76] inlining of context.write()


""",
u"""
remove erroneous extra line of declares

""",
u"""
little more concise syntax
""",
u"""
add a section about how to return early using return
from Mike Orr
""",
u"""
use 2.5 elementtree if available
""",
u"""
oops, wrong branch. merge r363 from brnaches/jython
""",
u"""
small cleanup
""",
u"""
use os.path.exists instead of os.access F_OK, which is currently broken on google app engine
""",
u"""
merged r351 from branches/jython
""",
u"""
merge r349 from branches/jython

""",
u"""
merge branches/_ast r340:HEAD, minus r344, to trunk. adds support for parsing
python via _ast and google app engine

""",
u"""
cleanup
""",
u"""
added "bytestring passthru" mode, via `disable_unicode=True`
  argument passed to Template or TemplateLookup.  All
  unicode-awareness and filtering is turned off, and template 
  modules are generated with the appropriate magic encoding
  comment.  In this mode, template expressions can only
  receive raw bytestrings or Unicode objects which represent
  straight ASCII, and render_unicode() may not be used. 
  [ticket:77]  (courtesy anonymous guest)


""",
u"""
typo fix

""",
u"""
cache_key argument can now render arguments passed 
  directly to the %page or %def, i.e.
  <%def name="foo(x)" cached="True" cache_key="${x}"/>
  [ticket:78]

""",
u"""
rewrote the "whitespace adjuster" function to work with
  more elaborate combinations of quotes and comments
  [ticket:75]


""",
u"""
self.attr is also assignable....

""",
u"""
added "attr" accessor to namespaces.  Returns attributes
  configured as module level attributes, i.e. within 
  <%! %> sections [ticket:62]
removed reliance upon KeyError/AttributeError in namespace.__getattr__

""",
u"""
fix indentation for [ticket:70]

""",
u"""
format_exceptions will apply the encoding options
  of html_error_template() to the buffered output


""",
u"""
fixed issue with inline format_exceptions that was producing
  blank exception pages when an inheriting template is 
  present [ticket:71]


""",
u"""
copyright !

""",
u"""
fixed codegen bug which occured when using <%page> level
  caching, combined with an expression-based cache_key, 
  combined with the usage of <%namespace import="*"/>


""",
u"""
defer temp file creation until after any potential lexer exceptions
fixes #69
""",
u"""
rename this misspelt test
""",
u"""
fixed bug in python generation when variable names are used
  with identifiers like "else", "finally", etc. inside them
  [ticket:68]


""",
u"""
fixed typo per [ticket:64]

""",
u"""
0.1.10

""",
u"""
fixed another namespace bug where the namespace functions
  did not have access to the correct context containing
  their 'self' and 'parent'


""",
u"""
fixed bug where local.get_namespace() could put an 
  incorrect "self" in the current context


""",
u"""
fixed propagation of 'caller' such that nested %def calls
  within a <%call> tag's argument list propigates 'caller'
  to the %call function itself (propigates to the inner
  calls too, this is a slight side effect which previously
  existed anyway)


""",
u"""
version #

""",
u"""
documented 'n' filter [ticket:58]

""",
u"""
added an IOError catch for source file not found in RichTraceback
exception reporter [ticket:51]


""",
u"""
fixed expressions and page tag arguments and with embedded
newlines in CRLF templates. follow up to #16.
thanks Eric Woroshow
""",
u"""
o move the babel plugin test template to test_htdocs
o update the babelplugin test for babel 0.9
""",
u"""
fix the babel example; the script was renamed to pybabel for 0.8.1
fixes #48
""",
u"""
comments can be placed at the end of control lines,
i.e. if foo: # a comment, [ticket:53], thanks to 
Paul Colomiets

""",
u"""
filters.Decode filter can also accept a non-basestring
object and will call str() + unicode() on it [ticket:47]


""",
u"""
spelling errors

""",
u"""
more tg fix:  fixed [ticket:35], allowing string-based
templates with tgplugin even if non-compatible args were sent


""",
u"""
fix to turbogears plugin to work with dot-separated names
(i.e. load_template('foo.bar')).  also takes file extension
as a keyword argument (default is 'mak').


""",
u"""
-> 0.1.8

""",
u"""
fixed import="*" with <%defs> embedded directly in <%namespace>

""",
u"""
added missing files from [ticket:45] checkin

""",
u"""
added a Babel (http://babel.edgewall.org/) extractor entry
point, allowing extraction of gettext messages directly from
mako templates via Babel [ticket:45]

""",
u"""
variable names declared in render methods by internal 
codegen prefixed by "__M_" to prevent name collisions
with user code


""",
u"""
changelog

""",
u"""
0.1.7

""",
u"""
Adding Python 2.3 hack for Beaker import to work properly without memcached.
""",
u"""
fix for 2.3

""",
u"""
0.1.6 prep

""",
u"""
added exceptions unit test, changed myghtyutils to beaker in docs

""",
u"""
html_error_template includes options "full=True", "css=True"
  which control generation of HTML tags, CSS [ticket:39]


""",
u"""
caching is now supplied directly by Beaker, which has 
  all of MyghtyUtils merged into it now

""",
u"""
leading utf-8 BOM in template files is honored according to pep-0263


""",
u"""
fixed codegen bug when defining <%def> within <%call> within <%call>

""",
u"""
control lines, i.e. % lines, support backslashes to continue long
  lines (#32)
fixed single "#" comments in docs

""",
u"""
added the 'encoding_errors' parameter to Template/TemplateLookup
  for specifying the error handler associated with encoding to
  'output_encoding' [ticket:40]
the Template returned by html_error_template now defaults to
  output_encoding=sys.getdefaultencoding(),
  encoding_errors='htmlentityreplace' [ticket:37]


""",
u"""
fixed comment syntax

""",
u"""
correction/edits

""",
u"""
added a doc for inheritable namespace

""",
u"""
Lexer/Compile exceptions propigate throughout lexer/parsetree/ast
using a more portable **exception_kwargs collection
added "source" member to the dict propigated to Lexer/Compile exceptions
RichTraceback can access original template source as a unicode object
using either 'source' memebr on Lexer/Compile exception, or 'source' 
property on ModuleInfo, fixes #37
unit tests for #37

""",
u"""
the <%call> test bumps up magic number

""",
u"""
added an explicit stack frame step to template runtime, which
  allows much simpler and hopefully bug-free tracking of 'caller',
  fixes #28
if plain Python defs are used with <%call>, a decorator
  @runtime.supports_callable exists to ensure that the "caller"
  stack is properly handled for the def.


""",
u"""
0.1.6 dev upcoming

""",
u"""
disclaimers for formatted whitespace

""",
u"""
typos

""",
u"""
TGPlugin passes options to string-based templates [ticket:35]

""",
u"""
fix to module_directory path generation when the path is "./"
  [ticket:34]


""",
u"""
README file

""",
u"""
adding some 0.1.5 versions

""",
u"""
adjustments to the buffer_filters arg so it works right with cached/buffered

""",
u"""
added "n" filter, disables *all* filters normally applied to an expression
via <%page> or default_filters (but not those within the filter)
added buffer_filters argument, defines filters applied to the return value
of buffered/cached/filtered %defs, after all filters defined with the %def
itself have been applied.  allows the creation of default expression filters
that let the output of return-valued %defs "opt out" of that filtering
via passing special attributes or objects.
added support for "class" structures in ast parsing (i.e. class-level
data members wont get added to the "declared" list)

""",
u"""
filtered out throwaway func name when getting <%include> kwargs

""",
u"""
fix to context-arguments inside of <%include> tag which broke 
during 0.1.4 [ticket:29]

""",
u"""
fix to lexing of <%docs> tag nested in other tags


""",
u"""
cache_url attribute on page tag

""",
u"""
added cache_url to API level

""",
u"""
added "cache_url" argument passthru for memcached

""",
u"""
AST parsing, properly detects imports of the form "import foo.bar"
  [ticket:27]


""",
u"""
- AST expression generation - added in just about everything 
  expression-wise from the AST module  [ticket:26]


""",
u"""
0.1.4 prep

""",
u"""
- <%include> plus arguments is also programmatically available via
self.include_file(<filename>, **kwargs)

""",
u"""
- further escaping added for multibyte expressions in %def, %call attributes
[ticket:24]


""",
u"""
correction for line=None [ticket:25]

""",
u"""
- <%include> has an "args" attribute that can pass arguments to the called
template (keyword arguments only, must be declared in that page's <%page> tag.)


""",
u"""
added docs about traceback formatting

""",
u"""
- fixed/improved "caller" semantics so that undefined caller is "UNDEFINED",
propigates __nonzero__ method so it evaulates to False if not present, 
True otherwise.  this way you can say % if caller:\n ${caller.body()}\n% endif


""",
u"""
- added a path normalization step to lookup so URIs like "/foo/bar/../etc/../foo"
pre-process the ".." tokens before checking the filesystem


""",
u"""
further fix to previous ast enhancement; dont log identifiers as "declared" once we're traversing inside functions since they are local to the function.

""",
u"""
- fix to variable scoping for identifiers only referenced within functions


""",
u"""
- fixes to code parsing/whitespace adjusting where plain python 
comments may contain quote characters [ticket:23]


""",
u"""
- got defs-within-defs to be cacheable


""",
u"""
- added "preprocessor" argument to Template, TemplateLookup - is a single
  callable or list of callables which will be applied to the template text
  before lexing.  given the text as an argument, returns the new text.
- added mako.ext.preprocessors package, contains one preprocessor so far:
  'convert_comments', which will convert single # comments to the new ##
  format


""",
u"""
fixed comment to new style

""",
u"""
- added lexer error for unclosed control-line (%) line


""",
u"""
multiline comment syntax now <%doc>

""",
u"""
- improvement to scoping of "caller" variable when using <%call> tag


""",
u"""
- fix to text parsing to not yank "#" on the first col of the line
- doc adjustments, changeset adjustments, modified unicode tests to
use ## instead of # for magic encoding comment.  # will still work for now.
- unsure whether we are going with #* *# or <%doc> for multiline comments,
looking like <%doc>.

""",
u"""
got the multiline comments to highlight

""",
u"""
comments moved to "##" "#* *#" syntax.  still have to get pygment plugin to work.

""",
u"""
- UNDEFINED evaluates to False

""",
u"""
Fixing conditional to properly check templatename.
""",
u"""
0.1.2

""",
u"""
- got "top level" def calls to work, i.e. template.get_def("somedef").render()

""",
u"""
updates

""",
u"""
changed around filtering so you can just say "decode.utf8" or "decode.<whatever>" for generic expression decoding

""",
u"""
docs, added the unicode chapter

""",
u"""
- all template lexing converts the template to unicode first, to
  immediately catch any encoding issues and ensure internal unicode
  representation.

""",
u"""
- support for CRLF templates...whoops ! welcome to all the windows users.
  [ticket:16]
- cleanup in unit tests

""",
u"""
fixed typo

""",
u"""
- small fix to local variable propigation for locals that are conditionally declared

""",
u"""
some expression generator things missing, fixes [ticket:18]

""",
u"""
xtra test

""",
u"""
- "expression_filter" argument in <%page> applies only to expressions
- added "default_filters" argument to Template, TemplateLookup.  applies only to expressions,
gets prepended to "expression_filter" arg from <%page>.  defaults to ["unicode"], so that
all expressions get stringified into u'' by default (this is what Mako already does).
By setting to [], expressions are passed through raw.
- added "imports" argument to Template, TemplateLookup.  so you can predefine a list of
import statements at the top of the template.  can be used in conjunction with
default_filters.


""",
u"""
unit tests for input_encoding, non double-decode of unicode object

""",
u"""
- added optional input_encoding flag to Template, to allow sending a unicode() object with no
magic encoding comment

""",
u"""
platform independent path fixies

""",
u"""
added getattr/hasattr test

""",
u"""
- added module_filename argument to Template to allow specification of a specific module
file
- added modulename_callable to TemplateLookup to allow a function to determine module filenames
(takes filename, uri arguments).  used for [ticket:14]

""",
u"""
- fix to parsing of code/expression blocks to insure that non-ascii characters, combined
with a template that indicates a non-standard encoding, are expanded into backslash-escaped 
glyphs before being AST parsed [ticket:11]


""",
u"""
0.1.1

""",
u"""
- buffet plugin supports string-based templates, allows ToscaWidgets to work [ticket:8]

""",
u"""
- "directories" can be passed to TemplateLookup as a scalar in which case it gets
converted to a list [ticket:9]

""",
u"""
added unit test to insure that <%page> args can override names from __builtins__

""",
u"""
added a unit test for ben involving calling next.body() from a <%call> tag

""",
u"""
copyright update

""",
u"""
added development config file

""",
u"""
- fix to code generation to correctly track multiple defs with the same name.
this is implemented by changing the "topleveldefs" and "closuredefs" collections
from a Set to a dictionary.  a unit test was added with alternate set-ordering
as the original issue only appeared on linux to start.
- "backslash" -> "slash" in syntax doc

""",
u"""
added the "check for last" step back to the tests - illustrates how the different systems handle such a step

""",
u"""
- implemented "module" attribute for namespace [ticket:7]

""",
u"""
removed escaping, extra condfitional

""",
u"""
correction

""",
u"""
added some notes about frameworks

""",
u"""
- better error message when a lookup is attempted with a template that has no lookup

""",
u"""
- fix to expression filters so that string conversion (actually unicode) properly 
occurs before filtering
- removed encoding() filter - it conflicts with the fact that unicode conversion has to
occur on the value first before being sent to the filter.  recommended way for encoded
strings is to just say unicode(x, encoding='whatever')

""",
u"""
der, expiretime, not timeout

""",
u"""
- fix so that "cache_timeout" parameter is propigated

""",
u"""
- svn trunk in setup.py
- "cache='true'" -> "cached='True'"

""",
u"""
update

""",
u"""
removed "prune contrib" - have moved textmate tmbundle stuff out of trunk

""",
u"""
moving textmate out of trunk to external contrib folder

""",
u"""
removed "/" from prune for [ticket:5]

""",
u"""
added argument to %call tag example

""",
u"""
- added "encoding()" filter; this allows a filter expression to specify the encoding and error
handling for the given expression.
usage is like:  ${data | encoding('utf-8', errors='strict')}


""",
u"""
fix to encoding for file-read-from-a-template test

""",
u"""
further try/except AST fixes, cleanup of filter unit tests, made __locals propigation in codegen slightly simpler/faster

""",
u"""
Adding unicode doc reading in template test.
""",
u"""
- AST parsing fixes: fixed TryExcept identifier parsing

""",
u"""
etc

""",
u"""
css tweak

""",
u"""
release related stuff

""",
u"""
escaping back on

""",
u"""
fixes

""",
u"""
fix

""",
u"""
edits

""",
u"""
fix

""",
u"""
fixes, lots of new docs

""",
u"""
more highlighting tweaks

""",
u"""
css file

""",
u"""
tweaks to pygment highlighting, integrated with docs

""",
u"""
Added <%text> and # comment line highlighting to TM bundle.
""",
u"""
Added missing highlighting of <% %> blocks.
""",
u"""
Fixed pygments plugin to support all current Mako syntax.
""",
u"""
Properly highlights all Mako syntax, except for ${} inside HTML tags.
""",
u"""
Adding include highlighting for TM bundle.
""",
u"""
More pygments highlighting updates, almost properly highlights a <%def> now.
""",
u"""
Adding proper pygment highligher, and setup.py entry points for pygments.
""",
u"""
Moving pygments plugin to avoid name clashes.
""",
u"""
Initial commit of Pygments highlighting plugin.
""",
u"""
Adding command for {} substitution.
""",
u"""
Fixed highlighting of end char in a name under <%def>.
""",
u"""
Adding contrib directory with TextMate bundle.
""",
u"""
This entry-point namespace is only used for turbogears, removing -tg postfix as its unnecessary.
""",
u"""
filter docs, filtering functions

""",
u"""
edits

""",
u"""
edit

""",
u"""
py2.3 tweaks

""",
u"""
some lexer fixes
more doc construction

""",
u"""
ok the default "catchall" at the page level is now **pageargs, useable
by the template but otherwise not affected

""",
u"""
took out the whole "auto-propigation of **kwargs" thing, 
implemented "args" for <%page> tag.  still has a default 
"**_extra_pageargs" catchall for now...

""",
u"""
wow, really cant have any characters in an anchor tag

""",
u"""
esacping...

""",
u"""
dev

""",
u"""
escaping for section names

""",
u"""
fixes

""",
u"""
requestattr

""",
u"""
docs etc

""",
u"""
- fixes and tests involving exceptions propigating from buffered/ccall sections
- more docs

""",
u"""
default 'extension' argument

""",
u"""
formatting

""",
u"""
formatting

""",
u"""
basic usage doc; lookup sets filesystem checks to true by default

""",
u"""
magic number support

""",
u"""
some tweaking around with the render method, template lookups, getting direct def calls to work

""",
u"""
fixed def's

""",
u"""
added one-page docs

""",
u"""
<%def> tag now requires () in the name, i.e. <%def name="foo()">

""",
u"""
adjust plugin to be part of ext/, adjust plugin name

""",
u"""
cache file args, can be supplied on TemplateLookup, Template, <%page> tag, <%def> tag

""",
u"""
some refinements to the **kwargs sent to the main render() method

""",
u"""
propigate main body **kwargs to top-level defs
more docs

""",
u"""
caching layer for ns...

""",
u"""
added get_namespace function, more docs

""",
u"""
css stuff

""",
u"""
cleanup

""",
u"""
converted templates to base filesystem operations on their original uri; module writing
occurs in a directory hierarchy resembling uri scheme

""",
u"""
some simplifications

""",
u"""
big overhaul to variable scoping in code generation

""",
u"""
a little touch-and-go with def call with content....needs more work

""",
u"""
description->uri

""",
u"""
cache

""",
u"""
docs, runtime, exceptions

""",
u"""
docs, caching

""",
u"""
lexer picks up on magic encoding comment

""",
u"""
make dictionaryy operation more explicit

""",
u"""
Made plugin options more tolerant so mako. prefix isn't required.
""",
u"""
Prefixing template with / was unnecessary.
""",
u"""
Adding Mako TurboGears plugin support.
""",
u"""
Adding setup.py file for packaging.
""",
u"""
caching work, some doc content

""",
u"""
cleaning up exception formatting

""",
u"""
wsgi example rearrangement/update
cache function optional

""",
u"""
docs, capturing, etc

""",
u"""
comments

""",
u"""
some basic (memory only so far) caching

""",
u"""
trying to make autohandler extension look better.  theyre going to want a tag....

""",
u"""
autohandler extension

""",
u"""
path stuff, autohandler ext not quite working, etc

""",
u"""
dynamic inheritance

""",
u"""
various dev on lookup

""",
u"""
added "import='x, y'" / "import='*'" to namespace tag, will cut down on dots
added filename-relative lookup to TemplateLookup

""",
u"""
dont need lookup for exception reporting

""",
u"""
dev

""",
u"""
wsgi, exception handling

""",
u"""
localized exception 

""",
u"""
added wsgi example, working on lookup/exception reporting

""",
u"""
screwing around with the exception formatting a bit

""",
u"""
fixed [ticket:1] ! w00p

""",
u"""
more lru

""",
u"""
added a threading test for lru....

""",
u"""
cleanup etc

""",
u"""
traceback formatting

""",
u"""
unit test cleanup, lru test, switched lru to be fuzzy

""",
u"""
took out extra mutex thing

""",
u"""
basic module file generation/loading 

""",
u"""
starting to put in the module loading crap...

""",
u"""
we have liftoff (finally....)

""",
u"""
scoping wackiness regarding component calls with content

""",
u"""
namespace model moved around to be more module-level, called from a variety of 
codepaths into the module (main render, inherit only, def call only)

""",
u"""
doc system, working on namespace scoping/declarations, ast parsing, etc

""",
u"""
porting doc system from SA over to mako

""",
u"""
text tag, adding "inheritable" flag to namespace

""",
u"""
changed %component to %def

""",
u"""
unit tests....

""",
u"""
filters mostly complete for now...

""",
u"""
starting to add filter functionality

""",
u"""
assertion conditions for unit tests, fix to namespace generation

""",
u"""
more inheritance tests and turning on attribute-embedded expressions

""",
u"""
inheritance works for namespaces pulled in via <%namespace> 

""",
u"""
further inheritance stuff...

""",
u"""
more syntax checks

""",
u"""
cleanup

""",
u"""
inheritance/ccall with content coming together now

""",
u"""
some semblance of inheritance, needs cleanup

""",
u"""
speed adjustments...the cheetah test setting the bar pretty high....

""",
u"""
adjustments to context to support 'args'

""",
u"""
docs

""",
u"""
more pythonlike about scope:  variable assignment now follows python conventions (i.e., you lose access to the enclosing scope version when you assign locally)

""",
u"""
changing around scope to be more consistent

""",
u"""
took out 2.4 generator...

""",
u"""
some thought given to unicode...

""",
u"""
added lookup module

""",
u"""
copyright etc

""",
u"""
unittests

""",
u"""
switched context from a "context = context.update()" model to a regular push()/pop() model

""",
u"""
component calls with content....

""",
u"""
doc, etc

""",
u"""
cstringio, template lookup

""",
u"""
benchmarks....beating cheetah so far ! woop

""",
u"""
various cleanup, more scoping tweaks, ast tweaks

""",
u"""
some stuff with args

""",
u"""
namespaces....namespace idea needs clarification

""",
u"""
this version seems to do it all...

""",
u"""
still trying to get nested components up.  not happening in this version.

""",
u"""
nested components, codegen arch, lexer fixes

""",
u"""
unit tests, error handling, interface, etc

""",
u"""
runtime, exceptions etc

""",
u"""
got something running

""",
u"""
dev

""",
u"""
codegen dev...

""",
u"""
dev on codegen...

""",
u"""
adding TemplateNode as lead parsetree value

""",
u"""
more logic for control lines, ternaries

""",
u"""
lexer completed

""",
u"""
adjustments

""",
u"""
lexer, basic parse tree structure, exception classes

""",
u"""
working out some expression parsing/return stuff, which will allow us
to add arguments to function signatures
"""
]

