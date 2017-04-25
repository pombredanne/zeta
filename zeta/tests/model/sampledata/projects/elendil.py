elendil_description = \
u"""
Python is a general-purpose, high-level programming language.[2] Its design
philosophy emphasizes programmer productivity and code readability.[3]
Python's core syntax and semantics are minimalistic, while the standard
library is large and comprehensive. Its use of whitespace as block delimiters
is unusual among popular programming languages.

Python supports multiple programming paradigms (primarily object oriented,
imperative, and functional) and features a fully dynamic type system and
automatic memory management, similar to Perl, Ruby, Scheme, and Tcl. Like
other dynamic languages, Python is often used as a scripting language.

Python was first released by Guido van Rossum in 1991.[4] The language has an
open, community-based development model managed by the non-profit Python
Software Foundation, which also maintains the de facto standard definition of
the language in CPython, the reference implementation.
"""

elendil_compdesc    = \
[
u"""
The mainstream Python implementation, known as CPython, is written in C
meeting the C89 standard,[36]. CPython compiles the Python program into
intermediate bytecode,[37] which is then executed by the virtual machine.[38]
It is distributed with a large standard library written in a mixture of C and
Python. CPython ships in versions for many platforms, including Microsoft
Windows and most modern Unix-like systems. CPython was intended from almost
its very conception to be cross-platform; its use and development on esoteric
platforms such as Amoeba, alongside more conventional ones like Unix and Mac
OS, has greatly helped in this regard.
""",
u"""
Stackless Python is a significant fork of CPython that implements
microthreads; it does not use the C memory stack. CPython uses a GIL to allow
only one thread to execute at a time while the Stackless Python threads are
independent of the OS and can run concurrently. Stackless Python is better
suited to scalable tasks and for use on microcontrollers or other limited
resource platforms due to the thread's light weight. It can be expected to run
on approximately the same platforms that CPython runs on.
""",
u"""
Jython compiles the Python program into Java byte code, which can then be
executed by every Java Virtual Machine implementation. This also enables the
utilization of Java class library functions from the Python program.
IronPython follows a similar approach in order to run Python programs on the
.NET Common Language Runtime. PyPy is an experimental self-hosting
implementation of Python, written in Python, that can output several types of
bytecode, object code and intermediate languages. There also exist compilers
to high-level object languages, with either unrestricted Python, a restricted
subset of Python, or a language similar to Python as the source language. PyPy
is of this type, compiling RPython to several languages; other examples
include Pyjamas compiling to Javascript; Shed Skin compiling to C++; and
Cython & Pyrex compiling to C.
""",
u"""
In 2005 Nokia released a Python interpreter for the Series 60 mobile phones
called PyS60. It includes many of the modules from the CPython implementations
and some additional modules for integration with the Symbian operating system.
This project has been kept up to date to run on all variants of the S60
platform and there are several third party modules available. There is also a
Python interpreter for Windows CE devices (including Pocket PC). It is called
PythonCE. There are additional tools available for easy application and GUI
development.
""",
u"""
ChinesePython is a Python programming language using Chinese language
lexicon. Besides reserved words and variable names, most data type operations
can be coded in Chinese as well.
""",
]

elendil_mstndesc    = \
[
u"""
Python is a multi-paradigm programming language. Rather than forcing
programmers to adopt a particular style of programming, it permits several
styles: object-oriented programming and structured programming are fully
supported, and there are a number of language features which support
functional programming and aspect-oriented programming (including by
metaprogramming[11] and by magic methods).[12] Many other paradigms are
supported using extensions, such as pyDBC and Contracts for Python which allow
Design by Contract.
""",
u"""
Python uses dynamic typing and a combination of reference counting and a
cycle-detecting garbage collector for memory management. An important feature
of Python is dynamic name resolution (late binding), which binds method and
variable names during program execution.
""",
u"""
Rather than requiring all desired functionality to be built into the
language's core, Python was designed to be highly extensible. New built-in
modules can be easily written in C or C++. Python can also be used as an
extension language for existing modules and applications that need a
programmable interface. This design of a small core language with a large
standard library and an easily extensible interpreter was intended by Van
Rossum from the very start because of his frustrations with ABC (which
espoused the opposite mindset).[5]
""",
u"""
The design of Python offers only limited support for functional programming in
the Lisp tradition. However, Python's design philosophy exhibits significant
similarities to those of minimalist Lisp-family languages, such as Scheme. The
library has two modules (itertools and functools) that implement proven
functional tools borrowed from Haskell and Standard ML.[13]
""",
u"""
While offering choice in coding methodology, the Python philosophy rejects
exuberant syntax, such as in Perl, in favor of a sparser, less-cluttered
grammar. As with Perl, Python's developers expressly promote a particular
"culture" or ideology based on what they want the language to be, favoring
language forms they see as "beautiful", "explicit" and "simple". As Alex
Martelli put it in his Python Cookbook (2nd ed., p.230): "To describe
something as clever is NOT considered a compliment in the Python culture."
Python's philosophy rejects the Perl "there is more than one way to do it"
approach to language design in favor of "there should be one and preferably
only one obvious way to do it".
""",
]

elendil_verdesc     = \
[
u"""
A common neologism in the Python community is pythonic, which can have
a wide range of meanings related to program style. To say that a piece
of code is pythonic is to say that it uses Python idioms well, that it
is natural or shows fluency in the language. Likewise, to say of an
interface or language feature that it is pythonic is to say that it
works well with Python idioms, that its use meshes well with the rest
of the language.
""",
u"""
In contrast, a mark of unpythonic code is that it attempts to "write C++ (or
Lisp, Perl, or Java) code in Python"that is, provides a rough transcription
rather than an idiomatic translation of forms from another language. The
concept of pythonicity is tightly bound to Python's minimalist philosophy of
readability and avoiding the "there's more than one way to do it" approach.
Unreadable code or incomprehensible idioms are unpythonic.
""",
u"""
Python is often used as a scripting language for web applications, e.g. via
mod_python for the Apache web server. With Web Server Gateway Interface a
standard API has been developed to facilitate these applications. Web
application frameworks or application servers like web2py, Zope, and Django
support developers in the design and maintenance of complex applications.
""",
u"""
Python has seen extensive use in the information security industry, including
in exploit development.[20] Python has been successfully embedded in a number
of software products as a scripting language, including in finite element
method software such as Abaqus, 3D animation packages such as Maya, Softimage
XSI, and Blender, and 2D imaging programs like GIMP, Inkscape, Scribus, and
Paint Shop Pro.[21] ESRI is now promoting Python as the best choice for
writing scripts in ArcGIS.[22] It has even been used in several
videogames.[23]
""",
u"""
For many operating systems, Python is a standard component; it ships with most
Linux distributions, with NetBSD, and OpenBSD, and with Mac OS X. Red Hat
Linux and Fedora both use the pythonic Anaconda installer. Gentoo Linux uses
Python in its package management system, Portage, and the standard tool to
access it, emerge. Pardus uses it for administration and during system
boot.[24]
"""
]

elendil_comments    = \
[
u"""
further hint to where the open docs really are

""",
u"""
explicitly close the file, merged from py3k

""",
u"""
switch library reference and language reference
""",
u"""
fix by stripping spaces from the argument in the 'help'
function.


""",
u"""
plug ref leak
""",
u"""
correctly handle descrs with __missing__
""",
u"""
Fix field name conflicts for named tuples.


""",
u"""
teach the peepholer about SETUP_WITH
""",
u"""
#6112: list.remove raises ValueError, not RuntimeError.
""",
u"""
fix cPickle's unpickling of recursive tuples.
""",
u"""
Allow multiple context managers in one with statement, as proposed
in http://codereview.appspot.com/53094 and accepted by Guido.

The construct is transformed into multiple With AST nodes so that
there should be no problems with the semantics.

""",
u"""
Make assertSequenceEqual error messages less cryptic, particularly for nested sequences.
""",
u"""
fix error handling
""",
u"""
take into account the fact that SETUP_WITH pushes a finally block
""",
u"""
add a SETUP_WITH opcode

It speeds up the with statement and correctly looks up the special
methods involved.

""",
u"""
special-case pickling of dicts. This nearly doubles the performance of dict pickling in cPickle.

""",
u"""
handle errors from _PyObject_LookupSpecial when __get__ fails
""",
u"""
make class skipping decorators the same as skipping every test of the class

This removes ClassTestSuite and a good bit of hacks.

""",
u"""
stop using Py_FindMethod
""",
u"""
Add Misc/python.pc to the list of ignored files


""",
u"""
Add pkg-config support.

It creates a python-2.7.pc file and a python.pc symlink in the
$(LIBDIR)/pkgconfig directory. Patch by Clinton Roy.


""",
u"""
Don't fail extracting a directory from a zipfile if the directory already exists.

""",
u"""
Do not try to build a version-independent
installer if the package has extension modules.

Also add NEWS entry for #5311.

""",
u"""
add a versionadded tag for set_tunnel

""",
u"""
fcntl now converts its third arguments to a C `long` rather
than an int, which makes some operations possible under 64-bit Linux (e.g.
DN_MULTISHOT with F_NOTIFY).



""",
u"""
Fix build under Windows


""",
u"""
Fixed Issue1424152, urllib2 fails with HTTPS over Proxy. 


""",
u"""

lnotab-based tracing is very complicated and isn't documented very well.  There
were at least 3 comment blocks purporting to document co_lnotab, and none did a
very good job. This patch unifies them into Objects/lnotab_notes.txt which
tries to completely capture the current state of affairs.

I also discovered that we've attached 2 layers of patches to the basic tracing
scheme. The first layer avoids jumping to instructions that don't start a line,
to avoid problems in if statements and while loops.  The second layer
discovered that jumps backward do need to trace at instructions that don't
start a line, so it added extra lnotab entries for 'while' and 'for' loops, and
added a special case for backward jumps within the same line. I replaced these
patches by just treating forward and backward jumps differently.

""",
u"""
Add smtplib test from 

""",
u"""
remove mention of old ctypes version
""",
u"""
reorder name
""",
u"""
support building with subversion 1.7 #6094
""",
u"""
skip a test_fileio subtest on all BSDs, not only FreeBSD


""",
u"""
Some pid_t-expecting or producing functions were forgotten in r72852.


""",
u"""
Fix functions taking or returning a process identifier to use
the dedicated C type `pid_t` instead of a C `int`. Some platforms have
a process identifier type wider than the standard C integer type.


""",
u"""
str.format raises SystemError.
""",
u"""
Fix spelling left over from testing.

""",
u"""
Don't be so wordy in requires('network') in case other tests
are added later, and skip the existing test if SSL is not available.

""",
u"""
Fix smtplib.SMTP_SSL._get_socket now correctly returns
the socket.  Patch by Farhan Ahmad, test by Marcin Bachry.


""",
u"""
#6078: _warnings is a builtin module and has no standard init_warnings function.
""",
u"""
#6086: fix spelling and use a better exception to catch.
""",
u"""
Correction in softspace behavior description.
""",
u"""
s/use/call/
""",
u"""
Fix confusing wording.
""",
u"""
Fix references to file-related functions and methods (os.* vs file.*).
""",
u"""
fixed encoding
""",
u"""
#6084: fix example.
""",
u"""
Use raise X(y).
""",
u"""
don't use subprocess.call with PIPEs as the child can fill the pipe buf and
deadlock. add a warning to subprocess docs about this, similar to Popen.wait's.
refs http://bugs.jython.org/issue1351

""",
u"""
Fix-up moving average example.
""",
u"""
Rename TestCase._result to _resultForDoCleanups to avoid potential clashes in TestCase subclasses. 
""",
u"""
don't raise OverflowError for complex('1e500').  Backport of r72803.
""",
u"""
#6051: refer to email examples for better way to construct email messages.
""",
u"""
#6055: refer to "sqlite3" consistently.
""",
u"""
Update bug tracker URL.
""",
u"""
Fix by teaching frame_setlineno how to jump to the first line of
a code object.

""",
u"""
typos in ctypes Module
""",
u"""
POP_MARK was not in pickle protocol 0.
""",
u"""
Remove some old MacPython files that are no longer relevant.

""",
u"""
Remove some traces of 'MacPython'

""",
u"""
This patch ensures that the pydoc_data package gets installed. This is needed
to make it possible to use pydoc to get access to the language reference.

That is, without this patch the folllowing won't work:

   >>> help('if')


""",
u"""
Note that ordered dictionaries work with reversed().
""",
u"""
fixed the 'package' option of build_ext
""",
u"""
fix refleaks in test_urllib2_localnet.
""",
u"""
While I was modifying test_trace, it threw an exception when I accidentally
made it try to set the line number from the trace callback for a 'call' event.
This patch makes the error message a little more helpful in that case, and
makes it a little less likely that a future editor will make the same mistake
in test_trace.

""",
u"""
MutableSequence.__iadd__ should return self.
""",
u"""
Fixed #6053 - win32 fixes for distutils tests
""",
u"""
working with relative paths to avoid tar warnings on absolute paths
""",
u"""
Fixed the library extension when distutils build_ext is used inplace
""",
u"""
chop off slash
""",
u"""
fixed the test name
""",
u"""
ignore .rst files in sphinx its self
""",
u"""
pep8-fied distutils.archive_util + added minimum test coverage
""",
u"""
pep8-fied distutils.dir_util
""",
u"""
removed sys.platform == 'mac' usage in distutils.dir_util
""",
u"""
removed sys.platform == 'mac' support in distutils.dist.parse_command_line and improved test coverage
""",
u"""
remove confusing wording from complex -> integer and
complex -> float conversion error messages.


""",
u"""
not running this test with MSVC6
""",
u"""
#5935: mention that BROWSER is looked for in PATH.
""",
u"""
#5942: Copy over flag table from dbm.rst which is clearer.
""",
u"""
#6017: better document behavior of dictiterators when the dict is changed.
""",
u"""
part of #4144: fix exception message in console session.
""",
u"""
Added NEWS for r72698.
""",
u"""
Removed Py_WIN_WIDE_FILENAMES which is not used any more.
""",
u"""
typo
""",
u"""
update
""",
u"""
completely ignore old-style stuff for type checking overloading
""",
u"""
deal with old-style classes in issubclass and isinstance
""",
u"""
properly lookup __instancecheck__ and __subclasscheck__
""",
u"""
use skipTest()
""",
u"""
pep8-fied distutils.dist module
""",
u"""
#6041: sdist and register now use the check command. No more duplicate code for metadata checking
""",
u"""
Fix about and bugs pages to match real workflow.
""",
u"""
#2856: document 2.x os.listdir() behavior for undecodable filenames.
""",
u"""
#6009: undocument default argument of Option as deprecated. 
""",
u"""
#6025: fix signature of parse().
""",
u"""
#6034: clarify __reversed__ doc.
""",
u"""
Fix bootstrapping by removing uses of the copy module in distutils


""",
u"""
Weak references and weak dictionaries now support copy()ing and deepcopy()ing.


""",
u"""
Make imaplib IPv6-capable. Patch by Derek Morr.


""",
u"""
Fix example output for doctest-like demos.
""",
u"""
make regrtest.py promote refleaks to test failures.
""",
u"""
a useful decorator for cleaning up threads
""",
u"""
prevent refleaks from threads
""",
u"""
Fix a crash in the parser module.

Patch by Amaury.



""",
u"""
Make nntplib IPv6-capable. Patch by Derek Morr.

(Unfortunately, nntplib doesn't have a test suite)


""",
u"""
#6022 fixed test_get_outputs so it doesn't leaves a test file in the cwd
""",
u"""
Fix test failure on Windows, and add skip check if even unicodedata
turns out not to be an external module on some other platform.

""",
u"""
pep8-fied distutils.command.sdist + more tests
""",
u"""
more test coverage for distutils sdist command
""",
u"""
importlib.import_module is better these days
""",
u"""
adding void to the c function
""",
u"""
added an inifoo in the C file, to avoid a warning by the MSVC9 linker
""",
u"""
inspect.findsource/getsource now raise an IOError if the 'source'
file is a binary.  Patch by Brodie Rao, test by Daniel Diniz.

""",
u"""
Move news item to correct section, remove spurious 'see below'
from docstring.

""",
u"""
add docstrings to marshal.

""",
u"""
the compiler attribute is used in setup.py; can't rename
""",
u"""
fixed #5977: distutils build_ext.get_outputs was not using the inplace option
""",
u"""
Better fix for modules using unittest.main(). Fixes regression caused by commit for Michael Foord
""",
u"""
Fix to restore command line behaviour for test modules using unittest.main(). Regression caused by Michael
""",
u"""
removing the assert statement so the code works when Python is run with -O
""",
u"""
Make it clear up front that shelve only records changes
when objects are assigned back to it when writeback is False.

""",
u"""
Add missing # to NEWS
""",
u"""
Adds a verbosity keyword argument to unittest.main plus a minor fix allowing you to specify test modules / classes
from the command line.

Closes 

Michael Foord

""",
u"""
Fix some float.fromhex bugs related to inf and nan handling.

""",
u"""
distutils.test_build_clib added a new line at the end of the file, to avoid a warning with some compilers
""",
u"""
sys.setdefaultencoding() strikes me as a bad example
""",
u"""
fixed test_build_ext for win32
""",
u"""
use isinstance
""",
u"""
fixed test for all platforms
""",
u"""
now using EnvironGuard everywhere
""",
u"""
refactored test_sysconfig so it uses test.test_support.EnvironmentVarGuard
""",
u"""
Added tests form install_lib and pep8-fied the module
""",
u"""
fixed #5984 and improved test coverage
""",
u"""
make sure files are closed using the with statement
""",
u"""
close file explicitly
""",
u"""
clear error state properly
""",
u"""
don't ignore exceptions from _PyObject_LengthHint
""",
u"""
ignore AttributeErrors for classic classes
""",
u"""
*sigh* deal with instances correctly
""",
u"""
can't handle classic classes here
""",
u"""
ignore classic classes
""",
u"""
convert some more special methods to use _PyObject_LookupSpecial
""",
u"""
StreamHandler.handleError now swallows IOErrors which occur when trying to print a traceback.
""",
u"""
#5976: fixed distutils test_check_environ
""",
u"""
Fixed distutils.command.build_ext - Ensure RUNPATH is added to extension modules with RPATH if GNU ld is used
""",
u"""
lookup __reversed__ correctly as a special method
""",
u"""
Merged revisions 72491-72493 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r72491 | benjamin.peterson | 2009-05-08 19:33:27 -0500 (Fri, 08 May 2009) | 7 lines
  
  make 2to3 use unicode internally on 2.x
  
  This started out as a fix for #2660, but became this large refactoring
  when I realized the dire state this was in. 2to3 now uses
  tokenize.detect_encoding to decode the files correctly into unicode.
........
  r72492 | benjamin.peterson | 2009-05-08 19:35:38 -0500 (Fri, 08 May 2009) | 1 line
  
  remove compat code
........
  r72493 | benjamin.peterson | 2009-05-08 19:54:15 -0500 (Fri, 08 May 2009) | 1 line
  
  add a test for \r\n newlines
........

""",
u"""
Fix an off by one error on negative indexs to __getitem__
http://code.google.com/p/ipaddr-py/issues/detail?id=15

""",
u"""
PyFrame_GetLineNumber:
Most uses of PyCode_Addr2Line
(http://www.google.com/codesearch?q=PyCode_Addr2Line) are just trying to get
the line number of a specified frame, but there's no way to do that directly.
Forcing people to go through the code object makes them know more about the
guts of the interpreter than they should need.

The remaining uses of PyCode_Addr2Line seem to be getting the line from a
traceback (for example,
http://www.google.com/codesearch/p?hl=en#u_9_nDrchrw/pygame-1.7.1release/src/base.c&q=PyCode_Addr2Line),
which is replaced by the tb_lineno field.  So we may be able to deprecate
PyCode_Addr2Line entirely for external use.

""",
u"""
PyCode_NewEmpty:
Most uses of PyCode_New found by http://www.google.com/codesearch?q=PyCode_New
are trying to build an empty code object, usually to put it in a dummy frame
object. This patch adds a PyCode_NewEmpty wrapper which lets the user specify
just the filename, function name, and first line number, instead of also
requiring lots of code internals.

""",
u"""
Fix gcc -Wextra compiler warnings (and remove some
trailing whitespace).

""",
u"""
Add a file that contains diffs between offical libffi files and the
files in this repository.  Should make it easier to merge new libffi
versions.

""",
u"""
fix this test
""",
u"""
Update the Windows locale mapping with the ones introduced with Vista.

""",
u"""
Add ISO-8859-16.

""",
u"""
Fix name.
""",
u"""
this is now a bound method
""",
u"""
add _PyObject_LookupSpecial to handle fetching special method lookup
""",
u"""
#4351: more appropriate DeprecationWarning stacklevels

""",
u"""
fixed AR/ARFLAGS values in test_sysconfig
""",
u"""
run autoconf (step forgotten in r72445)
""",
u"""
Fixed #5941: added ARFLAGS for the archiver command.
""",
u"""
removed remaining spaces
""",
u"""
Fixed wording for formatting integers: precision is not allowed.
""",
u"""
Pre-opened test file needs to be opened in binary mode.

""",
u"""
News item for Issue5955.


""",
u"""
Issue5955: aifc's close method did not close the file it wrapped,
now it does.  This also means getfp method now returns the real fp.

""",
u"""
actually close files instead of leaving it to the gc #5955
""",
u"""
Revert inappropriate doc change.

""",
u"""
Document how to pass a 'decode' argument to get_payload when
is_multipart is False.

""",
u"""
Remove two dead links
""",
u"""
Add NEWS entry about 

""",
u"""
The unicode-internal encoder now reports the number of *characters*
consumed like any other encoder (instead of the number of bytes).

""",
u"""
Be more explicit about the error we are catching.

Requested by: Antoine Pitrou

""",
u"""
removed string.split usage
""",
u"""
more build_clib cleanup + test coverage
""",
u"""
pep8-fied build_clib module : it is now similar to the one in 3.x
""",
u"""
Added a test and cleaned check_library_list to be ready to fix #5940
""",
u"""
Wrap getpreferredencoding()'s use of setlocale in a try/except to prevent
us from raising an exception when the locale is invalid.



""",
u"""
Merged revisions 68503,68507,68694,69054,69673,69679-69681,70991,70999,71003,71695 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r68503 | benjamin.peterson | 2009-01-10 14:14:49 -0600 (Sat, 10 Jan 2009) | 1 line
  
  use variable
........
  r68507 | benjamin.peterson | 2009-01-10 15:13:16 -0600 (Sat, 10 Jan 2009) | 1 line
  
  rewrap
........
  r68694 | benjamin.peterson | 2009-01-17 17:55:59 -0600 (Sat, 17 Jan 2009) | 1 line
  
  test for specific node type
........
  r69054 | guilherme.polo | 2009-01-28 10:01:54 -0600 (Wed, 28 Jan 2009) | 2 lines
  
  Added mapping for the ttk module.
........
  r69673 | benjamin.peterson | 2009-02-16 09:38:22 -0600 (Mon, 16 Feb 2009) | 1 line
  
  fix handling of as imports #5279
........
  r69679 | benjamin.peterson | 2009-02-16 11:36:06 -0600 (Mon, 16 Feb 2009) | 1 line
  
  make Base.get_next_sibling() and Base.get_prev_sibling() properties
........
  r69680 | benjamin.peterson | 2009-02-16 11:41:48 -0600 (Mon, 16 Feb 2009) | 1 line
  
  normalize docstrings in pytree according to PEP 11
........
  r69681 | benjamin.peterson | 2009-02-16 11:43:09 -0600 (Mon, 16 Feb 2009) | 1 line
  
  use a set
........
  r70991 | benjamin.peterson | 2009-04-01 15:54:50 -0500 (Wed, 01 Apr 2009) | 1 line
  
  map urllib.urlopen to urllib.request.open #5637
........
  r70999 | benjamin.peterson | 2009-04-01 17:36:47 -0500 (Wed, 01 Apr 2009) | 1 line
  
  add very alpha support to 2to3 for running concurrently with multiprocessing
........
  r71003 | benjamin.peterson | 2009-04-01 18:10:43 -0500 (Wed, 01 Apr 2009) | 1 line
  
  fix when multiprocessing is not available or used
........
  r71695 | benjamin.peterson | 2009-04-17 22:21:29 -0500 (Fri, 17 Apr 2009) | 1 line
  
  refactor multiprocessing support, so it's less hacky to employ and only loads mp when needed
........

""",
u"""
tabify :(
""",
u"""
don't package Lib/test/README anymore.

""",
u"""
fix running test_capi with -R ::

Also, fix a refleak in the test that was preventing running. :)

""",
u"""
Fix find_library can return directories instead of files
(on win32)

""",
u"""
Changed format.__float__ and complex.__float__ to use a precision of 12 when using the empty presentation type. This more closely matches str()'s behavior and reduces surprises when adding alignment flags to an empty format string. Patch by Mark Dickinson.
""",
u"""
Fix some gcc -Wextra warnings.  Thanks Victor Stinner for
the patch.

""",
u"""
Fixing issue5861 - test_urllib fails on windows. Agree to comment to have ':' in pathname2url as windows recognizes it. test_urllib passes now.
""",
u"""
Remove -n switch on "Edit with IDLE" menu item.

""",
u"""
Remove unused variable.
""",
u"""
#5929: fix signedness warning.
""",
u"""
Fix overlong lines.
""",
u"""
#5142: add module skipping feature to pdb.
""",
u"""
Add a news entry for r72319.
""",
u"""
#1309567: fix linecache behavior of stripping subdirectories from paths when looking for relative filename matches. Also add a linecache test suite.
""",
u"""
#5932: fix error return in _convertPyInt_AsSsize_t() conversion function.
""",
u"""
Update bdist_msi so that the generated MSIs for pure Python modules can install to any version of Python, like the generated EXEs from bdist_wininst. (Previously, you had to create a new MSI for each version of Python.)
""",
u"""
using sys._getframe(x), where x > 0 doesnt' work on IronPython
""",
u"""
Fix (property subclass shadows __doc__ string) by inserting
the __doc__ into the subclass instance __dict__.  The fix refactors
property_copy to call property_init in such a way that the __doc__
logic is re-executed correctly when getter_doc is 1, thus simplifying
property_copy.


""",
u"""
In :class:`zipfile.Zipfile`, fix wrong path calculation when extracting a file to the root directory.


""",
u"""
#5916, 5917: small socket doc improvements.
""",
u"""
#5927, 5928: typos.
""",
u"""
#5925: fix highlighting of keyword table.
""",
u"""
Add Nick Barnes to ACKS.


""",
u"""
The UTF-7 decoder was too strict and didn't accept some legal sequences. 
Patch by Nick Barnes and Victor Stinner.


""",
u"""
Fix typos.

""",
u"""
os.listdir() should fail for empty path on windows.
""",
u"""
cleanup applied patch to match style that is already in py3k branch.

""",
u"""
For hashlib algorithms provided by OpenSSL, the Python
GIL is now released during computation on data lengths >= 2048 bytes.

""",
u"""
There's no %A in Python 2.x!

""",
u"""
Handle %s like %S and %R in PyUnicode_FromFormatV(): Call
PyUnicode_DecodeUTF8() once, remember the result and output it in a second
step. This avoids problems with counting UTF-8 bytes that ignores the effect
of using the replace error handler in PyUnicode_DecodeUTF8().

                                    """,
            u"""
Don't use PyOS_strnicmp for NaN and Inf detection: it's locale-aware.

""",
u"""
Eliminate some locale-dependent calls to isspace and tolower.

""",
u"""
Remove unnecessary uses of context in PyGetSetDef.  See 

""",
u"""
docstring update.

""",
u"""
Optimization: move RFC defined network constant construction out of
the is_*() methods and into module private instances.

""",
u"""
- applies patch supplied by philipp hagemeister to fix
many problems with the ancient mcast.py demo code.

""",
u"""
Further development of issue5559, handle Windows files
which not only have embedded spaces, but leading spaces.
""",
u"""
idle.py modified and simplified to better support
developing experimental versions of IDLE which are
not installed in the standard location.
""",
u"""

""",
u"""
Isue #5084: unpickling now interns the attribute names of pickled objects,
saving memory and avoiding growth in size of subsequent pickles. Proposal
and original patch by Jake McGuire.


""",
u"""
add myself
""",
u"""
Add addCleanup and doCleanups to unittest.TestCase.

Closes 

Michael Foord



""",
u"""
#1607951: Make mailbox.Maildir re-read the directories less frequently.
This is done by recording the current time -1sec, and not re-reading unless
the directory mod. times are >= the recorded time.
""",
u"""
Convert test method names to PEP8 style.

""",
u"""
Remove unnecessary use of context for long getters.
(Related to 

""",
u"""
revert unrelated change
""",
u"""
remove py3k compat code
""",
u"""
Add items
""",
u"""
don't let sys.argv be used in the tests
""",
u"""
Adds an exit parameter to unittest.main(). If False main no longer
calls sys.exit.

Closes 

Michael Foord
 


""",
u"""
Keep py3k and trunk code in sync.
""",
u"""
Fix directive name.
""",
u"""
Review ipaddr docs and add them in the TOC under "Internet protocols".

""",
u"""
Make Modules/ld_so_aix return the actual exit code of the linker, rather than always exit successfully.
Patch by Floris Bruynooghe.


""",
u"""
`shutil.copyfile()` and `shutil.copytree()` now raise an
error when a named pipe is encountered, rather than blocking infinitely.


""",
u"""
Adds the ipaddr module to the standard library.  
Based off of subversion r69 from http://code.google.com/p/ipaddr-py/

This code is 2to3 safe, I'll merge it into py3k later this afternoon.

""",
u"""
Make test.test_support.EnvironmentVarGuard behave like a dictionary.

All changes are mirrored to the underlying os.environ dict, but rolled back
on exit from the with block.

""",
u"""
#5889: remove comma at the end of a list that some C compilers don't like.

""",
u"""
Fix for Issue1648102, based on the MSDN spec: If this parameter specifies the
"<local>" macro as the only entry, this function bypasses any host name that
does not contain a period.

""",
u"""
Make the turtle.rst doctests pass.  I have a feeling there should be
more cleanup, but I don't know now to kill turtles.  Especially
unexpected ones... ;)

""",
u"""
Add complex.__format__.
""",
u"""
prevent ref cycles by removing bound method on close()
""",
u"""
make sure to close file
""",
u"""
make sure mode is removable while cleaning up test droppings
""",
u"""
#5878: fix repr of re object.
""",
u"""
fix test_shutil on ZFS #5676
""",
u"""
Backport some of the float formatting tests from py3k.

""",
u"""
Remove format_float and use _PyOS_double_to_string instead.

""",
u"""
format(1234.5, '.4') gives misleading result
(Backport of r72109 from py3k.)

""",
u"""
run autoconf
""",
u"""
More aifc tests.

""",
u"""
- configure.in: Don't error, when no --with-dbmliborder option is present

""",
u"""
- Add configure option --with-dbmliborder=db1:db2:... to specify 
  the order that backends for the dbm extension are checked. 

""",
u"""
- Add configure option --with-dbmliborder=db1:db2:... to specify 
  the order that backends for the dbm extension are checked. 

""",
u"""
Now that we've got a test_aifc, add a few tests.

""",
u"""
Fix aifc now skips any chunk type it doesn't actually
process instead of throwing errors for anything not in an explicit
skip list.  This is per this spec: http://www.cnpbagwell.com/aiff-c.txt.
Spec reference and test sound file provided by Santiago Pereson, fix
based on patch by Hiroaki Kawai.


""",
u"""
Fixed #5874 : distutils.tests.test_config_cmd is not locale-sensitive anymore
""",
u"""
Make the doctests in the docs pass, except for those in the turtle module.
""",
u"""
ctypes fails to build on mipsel-linux-gnu (detects mips
instead of mipsel)

""",
u"""
Remove spurious 'u'.

""",
u"""
Various small fixups to the multiprocessing docs, mostly fixing and
enabling doctests that Sphinx can run, and fixing and disabling tests that
Sphinx can't run.  I hand checked every test not now marked as a doctest,
and all except the two that have open bug reports against them now work,
at least on Linux/trunk. (I did not look at the last example at all since
there was already an open bug).  I did not read the whole document with
an editor's eye, but I did fix a few things I noticed while working on
the tests.


""",
u"""
Silence warning on Windows.
""",
u"""
Massively speedup `unicodedata.normalize()` when the
string is already in normalized form, by performing a quick check beforehand.
Original patch by Rauli Ruohonen.


""",
u"""
Add example to the seealso section.
""",
u"""
Update spec version number.
""",
u"""
calling a function of the mimetypes module from several threads
at once could hit the recursion limit if the mimetypes database hadn't been
initialized before.


""",
u"""
rationalize isdigit / isalpha / tolower, etc. Will port to py3k. Should fix Windows buildbot errors.
""",
u"""
Make sys.xxx variable references into links, note that print_last only
works when an exception gets to the interactive prompt, and update the
examples after testing.  The last one is now a valid Sphinx doctest,
but of the preceding two one can't be made a doctest and the other one
I'm postponing to 3.x because sphinx handles doctests as Unicode strings
and that makes the 2.x output confusing.


""",
u"""
#5840: dont claim we dont support TLS.
""",
u"""
#5848: small unittest doc patch.
""",
u"""
Demote warnings to notices, part 2: stuff that is 2.x-only.

""",
u"""
Demote warnings to notices where appropriate, following the goal that as few "red box" warnings
should clutter the docs as possible.  Part 1: stuff that gets merged to Py3k.

""",
u"""
Remove ".. warning::" markup that doesnt contain warnings for users, rather todo items.
""",
u"""
#5856: fix typo s in traceback example.
""",
u"""
Updated __all__ to include some missing names and remove some names which should not be exported.
""",
u"""
Right click 'go to file/line' not working if spaces
in path.  Bug 5559.
""",
u"""
Use test.test_support.EnvironmentVarGuard where tests change environment vars.

""",
u"""
Fix typo in function name

""",
u"""
Fix typo.

""",
u"""
Backport r71967 changes from py3k to trunk.
(Internal plumbing changes for float parsing.)

""",
u"""
Reset errno before both calls to PyOS_ascii_strtod, not just one.

""",
u"""
Note that the caller is resposible for freeing the result of PyOS_double_to_string.
""",
u"""
Update pydoc topics.

""",
u"""
Move pydoc_topics module to its own subdirectory, so that no generated code is in Lib/.
""",
u"""
Another file where the versions need to be up to date.

""",
u"""
Remove outdated TODO file.
""",
u"""
Note that the versions are also in README.txt.

""",
u"""
Update versions in instructions for manual set-up.
""",
u"""
Mostly formatting nits, and "and-ed together" -> "or-ed together" flags.
""",
u"""
Fix titlecase for characters that are their own
titlecase, but not their own uppercase.

""",
u"""
deprecate PyOS_ascii_formatd.

If anyone wants to clean up the documentation, feel free. It's my first documentation foray, and it's not that great.

Will port to py3k with a different strategy.
""",
u"""
document int -> Py_ssize_t changes.

""",
u"""
field changed from int to Py_ssize_t.

""",
u"""
more int -> Py_ssize_t documentation.

""",
u"""
more int -> Py_ssize_t documentation.

""",
u"""
int -> Py_ssize_t documentation.

""",
u"""
int -> Py_ssize_t documentation.

""",
u"""
Reformat prior to editing.

""",
u"""
int -> Py_ssize_t documentation.

""",
u"""
Reformat prior to editing.

""",
u"""
Since it's a macro, actually refer to it as such instead of function.

""",
u"""
Add a versionchanged notice for a few forgotten entries.

""",
u"""
Reformat, since I've been busy here anyway.

""",
u"""
Documentation notes for int -> Py_ssize_t changes.

""",
u"""
More documentation pointers about int -> Py_ssize_t.
Also fix up the documentation for PyObject_GC_Resize(). It seems that since
it first got documented, the documentation was actually for
_PyObject_GC_Resize().

""",
u"""
Reformat prior to editing.

""",
u"""
Since I edited this file, reformat for future edits.

""",
u"""
Reference to an int type, whereas it's a Py_ssize_t as the synopsis states.

""",
u"""
Reformat prior to editing.

""",
u"""
Document more int -> Py_ssize_t changes.

""",
u"""
Reformat prior to editing.

""",
u"""
Belatedly document which C API functions had their argument(s) or
return type changed from int or int * to Py_ssize_t or Py_ssize_t * as this
might cause problems on 64-bit platforms.

""",
u"""
Avoid redundant call to FormatError()
""",
u"""
#5841: add deprecation py3k warning and notice in the docs for commands module.
""",
u"""
#5821: add some capabilities of TarFile's file-like object.
""",
u"""
#5834: use "failure" instead of "error" because the two have different meanings in unittest context.
""",
u"""
#3320: fix spelling.
""",
u"""
Reformat paragraph.

""",
u"""
The type for ppos has been Py_ssize_t since 2.5, reflect this in the
documentation.

""",
u"""
Reformat prior to editing.

""",
u"""
(Invalid behavior of unicode.lower): Fixed bogus logic in
makeunicodedata.py and regenerated the Unicode database (This fixes
).

    """,
u"""
Reformat file prior to editing.

""",
u"""
Rewrite a sentence to be more in line with the rest of the documentation with
regard to person and audience.

""",
u"""
#5810: Fixed Distutils test_build_scripts
""",
u"""
adjust email examples not to use connect() and terminate with
quit() and not close().

""",
u"""
Fixed failure in test_httpservers
""",
u"""
Certain sequences of calls to set() and unset() for
support.EnvironmentVarGuard objects restored the environment variables
incorrectly on __exit__.

Fix this by recording the initial value of each environment variable on the
first access in set() or unset().

""",
u"""
First attempt to document PyObject_HEAD_INIT and PyVarObject_HEAD_INIT.

""",
u"""
Reformat prior to expanding.

""",
u"""
Fix typo in complex parsing code;  expand tests.

""",
u"""
fix a segfault when setting __class__ in __del__ #5283
""",
u"""
All global symbols that the _ctypes extension defines are
now prefixed with 'Py' or '_ctypes'.

""",
u"""
ctypes unwilling to allow pickling wide character.

""",
u"""
wrong paths for ctypes cleanup when Python is built in a
directory other than the source directory.

""",
u"""
Remove unnecessary double negative

""",
u"""
Use more robust test for double-rounding in test_fsum.
While we're at it, use new unittest.skipUnless decorator to
implement skipping for that test.

""",
u"""
The two-argument form of the Fraction constructor
now accepts arbitrary Rational instances.

""",
u"""
Fix missing 'return NULL'

""",
u"""

 - simplify parsing and printing of complex numbers
 - make complex(repr(z)) round-tripping work for complex
   numbers involving nans, infs, or negative zeros
 - don't accept some of the stranger complex strings
   that were previously allowed---e.g., complex('1..1j')

""",
u"""
Add link to PEP 236.
""",
u"""
#5813: add a reference to the "future statements" section.
""",
u"""
Fix rewrapping accident.
""",
u"""
#5820: fix bug in usage of getreader().
""",
u"""
Produce correct version string to access the .chm
docs on Windows.  Patch 5783 gpolo.  Will port.
""",
u"""
make Fraction('1e-6') valid.  Backport of r71806.

""",
u"""
Fixed formatting with commas didn't work if no specifier type code was given.
""",
u"""
Change API for import_fresh_module() to better support test_warnings use case (also fixes some bugs in the original implementation)
""",
u"""
Backport of some of the work in r71665 to trunk. This reworks much of
int, long, and float __format__(), and it keeps their implementation
in sync with py3k.

Also added PyOS_double_to_string. This is the "fallback" version
that's also available in trunk, and should be kept in sync with that
code. I'll add an issue to document PyOS_double_to_string in the C
API.

There are many internal cleanups. Externally visible changes include:

- Implement PEP 378, Format Specifier for Thousands Separator, for
  floats, ints, and longs.

- 'n' formatting for ints, longs, and floats handles
  leading zero formatting poorly.

- For float.__format__, don't add a trailing ".0" if
  we're using no type code and we have an exponent.

""",
u"""
Fixed regression caused when fixing #5768.

""",
u"""
Documentation for auto-numbered format fields. Contributed by Terry J. Reedy.
""",
u"""
#5751: fix escaping of \\n.
""",
u"""
#5757: fix copy-paste error in notify().
""",
u"""
Restore skips of posix and pty tests on Windows by calling the
test_support.import_module on the appropriate modules
before any other imports.

""",
u"""
Fix for the Issue918368 - urllib doesn't correct server returned urls


""",
u"""
Nit: integer division should use //, not /

""",
u"""
Make long -> float (and int -> float) conversions
correctly rounded, using round-half-to-even.  This ensures that the
value of float(n) doesn't depend on whether we're using 15-bit digits
or 30-bit digits for Python longs.

""",
u"""
Fix typo
""",
u"""
adding a NEWS note for #5795 (previously checked via the buildbot)
""",
u"""
making BuildWinInstTestCase silent in case bdist_wininst is not run under win32
""",
u"""
#5795 sysconfig._config_vars was shadowed in tearDown
""",
u"""
Automatic conversion of floats to integers for struct.pack integer codes
is deprecated.  Use an explicit int() instead.

""",
u"""
Fix for issue5657.

""",
u"""
fix typo
""",
u"""
make errors consistent
""",
u"""
initialize weakref some weakref types
""",
u"""
many more types to initialize (I had to expose some of them)
""",
u"""
move test to a more appropiate one
""",
u"""
initalize -> initialize
""",
u"""
try to initalize all builtin types with PyType_Ready to avoid problems like #5787
""",
u"""
fix a few nits in unittest.py #5771
""",
u"""
rename internal bytes_ functions to bytearray
""",
u"""
Fix a couple of minor round() issues.

""",
u"""
Backport r71704 (add configure check for C99 round function) to trunk.

""",
u"""
copysign shouldn't be declared as static in pymath.c

""",
u"""
"not subscriptable" should be a bit more understandable than "unsubscriptable".
""",
u"""
DistutilsSetupError was not raised when one single warning occured
""",
u"""
Change to Unicode output logic and test case for same.
""",
u"""
Change to Unicode output logic and test case for same.
""",
u"""
Clarify the behavior of any() and all() with an empty iterable.
""",
u"""
Less red ink (warning->note) and add link to def of side-by-side assembly.

""",
u"""
Remove duplicated function declaration.
Make _pagesize static.
""",
u"""
Remove unneeded code.
""",
u"""
Fix for issue3440: add warning to subprocess discussion of
env parameter that on Windows SystemRoot is required in order
to run side-by-side assemblies.

""",
u"""
call __float__ on str subclasses #5759

tests by R. David Murray

""",
u"""
tupel -> tuple
""",
u"""
pep8-fied
""",
u"""
improved test coverage for distutils.cmd
""",
u"""
Add missing NEWS item for issue1161031 fix.

""",
u"""
#5745: more linking for identifiers in email docs.
""",
u"""
deactivate test_search_cpp under win32
""",
u"""
#5741 followup: should also allow %%(blah)s.
""",
u"""
Simplify markup.
""",
u"""
Fixed #5607: Distutils test_get_platform was failing fo Mac OS X fat binaries.
""",
u"""
Fixed another typos. (email.Utils => email.utils)
""",
u"""
Fixed typo. (email.Utils => email.utils)
""",
u"""
Adjust test_asyncore to account for intentional asyncore behavior change
introduced by r70934 that was causing a test failure when run under -O.

""",
u"""
Fixed incorrect object passed into format_float_internal(). This was resulting in a conversion being done twice.
""",
u"""
fix missing quote
""",
u"""
fix extra parenthesis #5774
""",
u"""
#5719: add short usage example to optparse docstring.
""",
u"""
remove useless import
""",
u"""
#5741: dont disallow double percent signs in SafeConfigParser.set() keys.
""",
u"""
removed string usage and added a test for _clean
""",
u"""
added a test for finalize_options
""",
u"""
added a simple test for search_cpp
""",
u"""
pep8-fied the module before adding tests
""",
u"""
removed the print statements and added a test
""",
u"""
#5704: let python -3 imply -t as well.
""",
u"""
Take credit for my patch for 
""",
u"""
fix markup
""",
u"""
ignore py3_test_grammar when compiling the library
""",
u"""
Take credit for a patch of mine.
""",
u"""
Make test_asyncore tests match code changes introduced by the
fix to Issue1161031, refactoring the test to simplify it in
the process.

""",
u"""
Re-word
""",
u"""
Add various items
""",
u"""
testing a full check case
""",
u"""
#5732: added the check command into Distutils
""",
u"""
fixed link
""",
u"""
Provide a standardised testing mechanism for doing fresh imports of modules, including the ability to block extension modules in order to test the pure Python fallbacks
""",
u"""
remove unpleasant exec

""",
u"""
Add examples.
""",
u"""
#5698: Fix casing of !DOCTYPE to conform to W3C specs.
""",
u"""
Let "lambda" point to the correct heading.
""",
u"""
Fix the count of datatypes.
""",
u"""
Clarify the table entries for combinatorics.
""",
u"""
IE needs the border-left:0 for some reason.
""",
u"""
More table clean-up
""",
u"""
Center table headings.
""",
u"""
More table formatting.
""",
u"""
Add note on using keyword arguments with OrderedDict.
""",
u"""
refactored xml.dom.minidom.normalize, increasing both
its clarity and its speed.

""",
u"""
Fixed #5731: Distutils bdist_wininst no longer worked on non-Windows platforms
""",
u"""
Add a custom stylesheet with better table formatting.
""",
u"""
add more pickling tests.

- Add tests for the module-level load() and dump() functions.
- Add tests for cPickle's internal data structures, stressing workloads
with many gets/puts.
- Add tests for the Pickler and Unpickler classes, in particular the
memo attribute.
- test_xpickle is extended to test backwards compatibility with Python
2.4, 2.5 and 2.6 by round-tripping pickled objects through a worker
process. This is guarded with a regrtest -u xpickle resource.

""",
u"""
Typo fixes
""",
u"""
Add items
""",
u"""
Update ignore file for suspicious builder.
""",
u"""
Remove redundant backtick.
""",
u"""
fix syntax
""",
u"""
these must be installed to correctly run tests
""",
u"""
Minor factoring.
""",
u"""
Add docstrings.
""",
u"""
- Make timing assertions very generous (a la test_timeout.py)
- Break the gc cycle in negotiation tests
- test the different guarantees of read_lazy and read_very_lazy

""",
u"""
Fix make.bat to match makefile changes
""",
u"""
eliminate more race conditions in telnetlib tests
""",
u"""
Minor tweak to improve the code as suggested by Brett Cannon and as implemented in the Py3K branch.
""",
u"""
revert unrelated change to test_telnetlib
""",
u"""
fix since difference formating of SyntaxErrors
""",
u"""
fix syntax tests after formatting change
""",
u"""
see if this helps the doc builds
""",
u"""
add create_connection to __all__ #5711
""",
u"""
- Fix CGIHTTPServer information disclosure.  Relative paths are
  now collapsed within the url properly before looking in cgi_directories.

""",
u"""
test the telnetlib.Telnet interface more thoroughly
""",
u"""
news entry for r71299.

""",
u"""
Fixes issue5705: os.setuid() and friends did not accept the same range of
values that pwd.getpwnam() returns.

""",
u"""
pep8-fied method names
""",
u"""
Fixed #5095: msi missing from Distutils bdist formats
""",
u"""
added a simplest test to distutils.spawn._nt_quote_args
""",
u"""
Fixed #1491431: distutils.filelist.glob_to_re was broken for some edge cases (detailed in the test
""",
u"""
Py_XINCREF, Py_DECREF, Py_XDECREF: Add `do { ... } while (0)'
to avoid compiler warnings.

""",
u"""
- SimpleXMLRPCDispatcher.__init__: Provide default values for
  new arguments introduced in 2.5.

""",
u"""
Normalize issue referencing style.
""",
u"""
Adding assertIs and assertIsNot methods to unittest.TestCase



""",
u"""
#602893: add indicator for current line in cgitb that doesnt rely on styling alone.
""",
u"""
Fixed 5694: removed spurious test output in Distutils
""",
u"""
#5298: clarify docs about GIL by using more consistent wording.
""",
u"""
#5444: adapt make.bat to new htmlhelp output file name.
""",
u"""
#5432: make plistlib docstring a raw string, since it contains examples with backslash escapes.
""",
u"""
#5471: fix expanduser() for $HOME set to "/".
""",
u"""
#5370: doc update about unpickling objects with custom __getattr__ etc. methods.
""",
u"""
Add NEWS entry for r71237.
""",
u"""
#1326077: fix traceback formatting of SyntaxErrors.  This fixes two differences with formatting coming from Python: a) the reproduction of location details in the error message if no line text is given, b) the prefixing of the last line by one space.
""",
u"""
Whitespace normalization.
""",
u"""
- Py_DECREF: Add `do { ... } while (0)' to avoid compiler warnings.
  (avoiding brown paper typo this time)

""",
u"""
#5580: no need to use parentheses when converterr() argument is actually a type description.
""",
u"""
#5615: make it possible to configure --without-threads again.
""",
u"""
Moved logging.captureWarnings() call inside with statement in WarningsTest.test_warnings.
""",
u"""
#1726172: dont raise an unexpected IndexError if a voidresp() call has an empty response.
""",
u"""
#1718017: document the relation of os.path and the posixpath, ntpath etc. modules better.
""",
u"""
Avoid sure signs of a diseased mind.
""",
u"""
Normalize spelling of Mac OS X.
""",
u"""
#1742837: expand HTTP server docs, and fix SocketServer ones to document methods as methods, not functions.
""",
u"""
Include tkinter.h only after including tk.h (or the equivalent for another platform).
""",
u"""
Change the way unittest.TestSuite use their tests to always access them through iteration. Non behavior changing, this allows you to create custom subclasses that override __iter__.



""",
u"""
compare types with is
""",
u"""
note how using iter* are unsafe while mutating and document iter(dict)
""",
u"""
Package zipdir.zip.

""",
u"""
No behavior change.
""",
u"""
revert r71159 since it broke the build
""",
u"""
- Py_DECREF: Add `do { ... } while (0)' to avoid compiler warnings.

""",
u"""
- In PyRun_SimpleFileExFlags avoid invalid memory access with
  short file names.

""",
u"""
#5601: clarify that webbrowser is not meant for file names.
""",
u"""
#5642: clarify map() compatibility to the builtin.
""",
u"""
Replace the localized min/max calls with normal if/else
""",
u"""
Allow multiple IDLE GUI/subprocess pairs to exist
simultaneously. Thanks to David Scherer for suggesting
the use of an ephemeral port for the GUI.
Patch 1529142 Weeble.

""",
u"""
Fix error in description of 'oct' (

""",
u"""
Add helpful link.
""",
u"""
Clarified warning about logging use from asynchronous signal handlers.
""",
u"""
Fix 'the the' duplication
""",
u"""
Fix 'the the'; grammar fix
""",
u"""
Add some items
""",
u"""
Added warning about logging use from asynchronous signal handlers.
""",
u"""
Fixed compile error on windows.
""",
u"""
Localize the function lookup in timeit.



""",
u"""
Update docs for namedtuple's renaming change.
""",
u"""
Have namedtuple's field renamer assign names that
are consistent with the corresponding tuple index.


""",
u"""
backport the memoryview object.


""",
u"""
sys.long_info attributes should be ints, not longs

""",
u"""
PyErr_NormalizeException may not set an error, so convert the PyErr_SetObject
call on hitting the recursion limit into just assigning it to the arguments provided.

""",
u"""
Actually the displayhook should print the repr.

""",
u"""
Add missing iteritems() call to the for loop in mailbox.MH.get_message().

Fixes issue2625.

""",
u"""
Store the functions in the _type_equality_funcs as wrapped objects that are deep copyable.

This allows for the deep copying of TestCase instances.




""",
u"""
Add custom initializer argument to multiprocess.Manager*, courtesy of lekma
""",
u"""
Clarify that datetime strftime does not produce leap seconds and datetime
strptime does not accept it in the strftime behavior section of the
datetime docs.

Closes 

""",
u"""
Raise ValueError if the size causes ERROR_NO_SYSTEM_RESOURCES
""",
u"""
Fix two issues introduced by by changing the signature of
PyImport_AppendInittab() to take a const char *.

""",
u"""
Better exception messages for unittest assert methods.

- unittest.assertNotEqual() now uses the inequality operator (!=) instead 
  of the equality operator.
  
- Default assertTrue and assertFalse messages are now useful. 

- TestCase has a longMessage attribute. This defaults to False, but if set to True 
  useful error messages are shown in addition to explicit messages passed to assert methods.




""",
u"""
PyImport_AppendInittab() took a char * as a first argument even though that
string was stored beyond the life of the call. Changed the signature to be
const char * to help make this point.

Closes 

""",
u"""
Fixing the issue4860. Escaping embedded '"' character in js_output() method of Morsel.


""",
u"""
fix error handling
""",
u"""
In PyErr_GivenExceptionMatches, temporarily bump the recursion
limit, so that in the most common case PyObject_IsSubclass will
not raise a recursion error we have to ignore anyway.

""",
u"""
Remove port spec from run.py and fix bug where
subprocess fails to extract port from command line
when warnings are present.
""",
u"""
Additional protection for SEM_VALUE_MAX on platforms, thanks to Martin Loewis
""",
u"""
Fix test_doctest, missed two assignments to curframe.
""",
u"""
handle SEEK_ constants in test_io
""",
u"""
this should be :noindex:
""",
u"""
fix markup
""",
u"""
issue5545: Switch to Autoconf for multiprocessing; special thanks to Martin Lowis for help
""",
u"""
Typo fix
""",
u"""
Cache the f_locals dict of the current frame, since every access to frame.f_locals overrides its contents with the real locals which undoes modifications made by the debugging user.
""",
u"""
remove double underscores
""",
u"""
Add my initials to Misc/developers.txt. Names are now sorted by number of
characters in the person's name.

""",
u"""
In Pdb, stop assigning values to __builtin__._ which interferes with the one commonly installed by gettext.
""",
u"""
Add tests checking the CSV module's ability to handle
embedded newlines in quoted field values.

""",
u"""
add seek constants to __all__
""",
u"""
Revert accidental checkin.
""",
u"""
Add NEWS item.
""",
u"""
#4572: add SEEK_* values as constants in io.py.
""",
u"""
Add link to an alternative generator with a long-period.
""",
u"""
Fix for issue5040. Adding test for Content-Length


""",
u"""
bounds check arguments to mmap.move().  All of them.  Really.
fixes crasher on OS X 10.5

""",
u"""
test_warnings ironically had a single test that was not protecting the warnings
filter and was resetting it.

""",
u"""
test_logging was blindly clearing the warnings filter. This caused
PendingDeprecationWarnings to be spewed all over by unittest.failIf*(). Fix
moves over to using warnings.catch_warning to protect the warnings filter.

""",
u"""
MutableSet.__iand__() no longer mutates self during iteration.
""",
u"""
Adding Wing project file
""",
u"""
_warnings was importing itself to get an attribute. That's bad if warnings gets
called in a thread that was spawned by an import itself.

Last part to close #1665206.

""",
u"""
Paul Kippes was given commit privileges to work on 3to2.

""",
u"""
#5655: fix docstring oversight.
""",
u"""
Ron DuPlain was given commit privileges at PyCon 2009 to work on 3to2.

""",
u"""
document Listener address restrictions on windows
""",
u"""
http://bugs.python.org/issue5623
Dynamically discoverd the size of the ioinfo struct used by the crt for its file descriptors.  This should work across all flavors of the CRT.  Thanks to Amaury Forgeot d'Arc
Needs porting to 3.1
""",
u"""
The cgitb module had imports in its functions. This can cause deadlock with the
import lock if called from within a thread that was triggered by an import.

Partially fixes 

""",
u"""
Fix test_xmlrpc and make the CGI handler work with no CONTENT_LENGTH.
""",
u"""
Fixed compile error on windows.
""",
u"""
Add Maksim, who worked on several issues at the sprint.
""",
u"""
#5631: add upload to list of possible commands, which is presented in --help-commands.
""",
u"""
The SimpleXMLRPCServer's CGI handler now runs like a pony.

""",
u"""
Fix multiprocessing.event to match the new threading.Event API
""",
u"""
Fix locale.format now checks that it is passed
exactly one pattern, which avoids mysterious errors where it
had seemed to fail to do localization.

""",
u"""
Fix for failing asyncore tests.

""",
u"""
Fix running test_sys with tracing enabled.

""",
u"""
#5228: add pickle support to functools.partial
""",
u"""
Fix Windows test skip error revealed by buildbot.  Also a comment spelling
correction in a previously fixed test.

""",
u"""
Dont shout to users.
""",
u"""
fixed the test for win32 CompileError
""",
u"""
catching msvc9compiler error as well
""",
u"""
Improve examples for collections.deque()
""",
u"""
#5018: remove confusing paragraph.
""",
u"""
#5617: add a handy function to print a unicode string to gdbinit.
""",
u"""
#5583 Added optional Extensions in Distutils
""",
u"""
Pass MS CRT debug flags into subprocesses
""",
u"""
#3427: document correct return type for urlopen().info().
""",
u"""
#1651995: fix _convert_ref for non-ASCII characters.
""",
u"""
#5563: more documentation for bdist_msi.
""",
u"""
Made handle_expt_event() be called last, so that we don't accidentally read
after closing the socket.

""",
u"""
#1676135: remove trailing slashes from --prefix argument.
""",
u"""
#1675026: add a note about a strange Windows problem, and remove notes about AtheOS.
""",
u"""
Remove warning about pending Win9x support removal.

""",
u"""
fix Thread.ident when it is the main thread or a dummy thread #5632
""",
u"""
#5598: document DocFileSuite *args argument.
""",
u"""
take the usual lock precautions around _active_limbo_lock
""",
u"""
#1530012: move TQS section before raw strings.
""",
u"""
making sdist and config test silents
""",
u"""
added tests to the install_headers command
""",
u"""
added test to the install_data command
""",
u"""
more tests for the upload command
""",
u"""
more tests for the register command
""",
u"""
added tests for the clean command
""",
u"""
using log.warn for sys.stderr
""",
u"""
#1674032: return value of flag from Event.wait(). OKed by Guido.
""",
u"""
Fixed mmap.move crash by integer overflow. (take2)
""",
u"""
Issue an actual PendingDeprecationWarning for the TestCase.fail* methods.
Document the deprecation.

""",
u"""
Add NEWS entry for regrtest change.

""",
u"""
Remove the regrtest check that turns any ImportError into a skipped test.
Hopefully all modules whose imports legitimately result in a skipped
test have been properly wrapped by the previous commits.

""",
u"""
Improve test_support.import_module docstring, remove
deprecated flag from get_attribute since it isn't likely
to do anything useful.


""",
u"""
This resolves Tests pass.

""",
u"""
Delete out-of-date and little-known README from the test
directory by consensus of devs at pycon sprint.

""",
u"""
#5618: fix typo.
""",
u"""
#4411: document mro() and __mro__. (I hope I got it right.)
""",
u"""
Fix-up unwanted change.
""",
u"""
#5190: export make_option in __all__.
""",
u"""
#1096310: document usage of sys.__std*__ a bit better.
""",
u"""
#4882: document named group behavior a bit better.
""",
u"""
Rename the actual method definitions to the official assertFoo names.

Adds unittests to make sure the old fail* names continue to work now
and adds a comment that they are pending deprecation.

Also adds a test to confirm that the plural Equals method variants
continue to exist even though we're unlikely to deprecate those.

http://bugs.python.org/issue2578

""",
u"""
#5241: document missing U in regex howto.
""",
u"""
#5227: note that Py_Main doesnt return on SystemExit.
""",
u"""
A few more test skips via import_module, and change import_module to                                                                                                                                                
return the error message produced by importlib, so that if an import                                                                                                                                                
in the package whose import is being wrapped is what failed the skip                                                                                                                                                
message will contain the name of that module instead of the name of the                                                                                                                                             
wrapped module.  Also fixed formatting of some previous comments.                                                                                                                                                   


""",
u"""
#5245: note that PyRun_SimpleString doesnt return on SystemExit.
""",
u"""
missed the news/acks for netbsd patch
""",
u"""
#837577: note cryptic return value of spawn*e on invalid env dicts.
""",
u"""
Apply patch for netbsd multiprocessing support
""",
u"""
Per the language summit, the optional fastpath imports should use from-import-star.
""",
u"""
#970783: document PyObject_Generic[GS]etAttr.
""",
u"""
#992207: document that the parser only accepts \\n newlines.
""",
u"""
The unittest.TestCase.assertEqual() now displays the differences in lists,
tuples, dicts and sets on failure.

Many new handy type and comparison specific assert* methods have been added
that fail with error messages actually useful for debugging.  Contributed in
by Google and completed with help from mfoord and GvR at PyCon 2009 sprints.

Discussion lives in http://bugs.python.org/issue2578.

""",
u"""
#5417: replace references to undocumented functions by ones to documented functions.
""",
u"""
#1386675: specify WindowsError as the exception, because it has a winerror attribute that EnvironmentError doesnt have.
""",
u"""
#5529: backport new docs of import semantics written by Brett to 2.x.
""",
u"""
#5581: fget argument of abstractproperty is optional as well.
""",
u"""
#5566: fix versionadded from PyLong ssize_t functions.
""",
u"""
#5519: remove reference to Kodos, which seems dead.
""",
u"""
Add check for PyDict_Update() error.

""",
u"""
Global statements from one function leaked into parallel functions.

Re http://bugs.python.org/issue4315

The symbol table used the same name dictionaries to recursively
analyze each of its child blocks, even though the dictionaries are
modified during analysis.  The fix is to create new temporary
dictionaries via the analyze_child_block().  The only information that
needs to propagate back up is the names of the free variables.

Add more comments and break out a helper function.  This code doesn't
get any easier to understand when you only look at it once a year.


""",
u"""
Update quicktest to match Python 3 branch

""",
u"""
Minor update to OSX build-installer script, needed
to ensure that the build will succeed in a clean
checkout and with a non-default deployment target.

""",
u"""
Add is_declared_global() which distinguishes between implicit and
explicit global variables.

""",
u"""
Fixed mmap.move crash by integer overflow.
""",
u"""
add JoinableQueue to __all__
""",
u"""
Fix a wrong struct field assignment (docstring as closure).
""",
u"""
Add various items
""",
u"""
merge in patch from tim golden to fix contextmanager support for mp.Lock()
""",
u"""
Actually suppress warnings in test_at_least_import_untested_modules
inside the catch_warnings context manager.

""",
u"""
Fix add /Library/Python/2.7/site-packages to
sys.path on OSX, to make it easier to share (some) installed 
packages between the system install and a user install.

""",
u"""
Add more items
""",
u"""
typo fix
""",
u"""
Change more tests to use import_module for the modules that
should cause tests to be skipped.  Also rename import_function
to the more descriptive get_attribute and add a docstring.

""",
u"""
#5039: make it clear that the impl. note refers to CPython.
""",
u"""
A fix for inspired by the patch from Andi Albrecht (aalbrecht),
though with some changes by me.  This patch should not be back ported or
forward ported.  It's a bit too risky for 2.6 and 3.x does things fairly
differently.

""",
u"""
Many edits
""",
u"""
Add several items and placeholders
""",
u"""
Remove comment
""",
u"""
Typo fixes
""",
u"""
#5199: make warning about vars() assignment more visible.
""",
u"""
Add several VM developers.

""",
u"""
finalize the queue prior to shutdown
""",
u"""
Fix for bugs: Issue4675 and Issue4962.


""",
u"""
Remove references to test_socket_ssl which was deleted in trunk
in r64392 and py3k in r59038.

""",
u"""
Fix for 

""",
u"""
Fixes 

""",
u"""
* Set a custom icon on the Python installer DMG
* Remove last traces of "MacPython" 
* Add options to build different flavors of the installer
  (still defaulting to a 2-way universal build that 
  runs on OSX 10.3)

""",
u"""
Remove usage of the deprecated '-cString' and '+stringWithCString:' API's
in PythonLauncher, replacing them with the correct counterparts.

""",
u"""
Add import_function method to test.test_support, and modify a number of
tests that expect to be skipped if imports fail or functions don't
exist to use import_function and import_module.  The ultimate goal is
to change regrtest to not skip automatically on ImportError.  Checking
in now to make sure the buldbots don't show any errors on platforms
I can't direct test on.

""",
u"""
Fix issue where 'make altinstall' or 'make install' would install everything 
that needs to be installed on OSX (depending on the configure flags)

""",
u"""
* Updates installed dependencies to latest releaases (bzip, zlib, ...)
* Changes code for updating folder icons from Python code
  that uses the deprecated Carbon module to a much simpler
  Cocoa program in Objective-C

""",
u"""
Tk 8.5 Text widget requires 'wordprocessor' tabstyle attr to handle mixed space/tab properly. patch by Guilherme Polo.
""",
u"""
Fix for (some Carbon modules aren't present in the documentation)

""",
u"""
use socket.SO_REUSEADDR on multiprocessing SocketManager sockets
""",
u"""
Revert incorrect change.

""",
u"""
Add an entry to developers.txt.
""",
u"""
This patch fixes (wrong argument type conversion in Carbon.Qt)

""",
u"""
don't rely on the order dict repr #5605
""",
u"""
Convert import try/except to use test_support.import_module().

""",
u"""
add missing import
""",
u"""
there's actually three methods here #5600
""",
u"""
fix import
""",
u"""
fix regression in pure python code path, fix a decoder bug for unicode float literals outside of a container
""",
u"""
add missing import
""",
u"""
use the awesome new status iterator
""",
u"""
thanks to guido's bytecode verifier, this is fixed
""",
u"""
this has been fixed since 2.6 (I love removing these)
""",
u"""
Make life easier for non-CPython implementations.
""",
u"""
Apply floatformat changes to unicodeobject.c
as well as stringobject.c.

""",
u"""
Add paranoid check to avoid potential buffer overflow
on systems with sizeof(int) > 4.

""",
u"""
Replace confusing fabs(x)/1e25 >= 1e25 test
with fabs(x) >= 1e50, and fix documentation.

""",
u"""
Typo fix.
""",
u"""
Add the ability to control the random seed used by regrtest.py -r.

This adds a --randseed option, and makes regrtest.py -r indicate what random seed it's using so that that value can later be fed back to --randseed. This option is useful for tracking down test order-related issues found by make buildbottest, for example.

""",
u"""
fix consistency
""",
u"""
stop the versionchanged directive from hiding the docs
""",
u"""
a more realistic example
""",
u"""
Add section numbering to some of the larger subdocuments.

""",
u"""
Switch to fixed Sphinx version.
""",
u"""
Add a script to fixup rst files if the pre-commit hook rejects them.

""",
u"""
Fix a typo and be more specific


""",
u"""
Typo fix
""",
u"""
give os.symlink and os.link() better parameter names #5564
""",
u"""
#5324: document __subclasses__().
""",
u"""
Publicize the GC untracking optimization


""",
u"""
Fix typo.
""",
u"""
Adjusted _tkinter to compile without warnings when WITH_THREAD is not
defined (part of 

""",
u"""
fix another name
""",
u"""
update email tests to use SkipTest
""",
u"""
** is required here
""",
u"""
add missing import
""",
u"""
must pass argument to get expected behavior ;)
""",
u"""
fix incorrect auto-translation of TestSkipped -> unittest.SkipTest
""",
u"""
fix naming
""",
u"""
remove test_support.TestSkipped and just use unittest.SkipTest
""",
u"""
apply the second part of #4242's patch; classify all the implementation details in test_descr
""",
u"""
rename TestCase.skip() to skipTest() because it causes annoying problems with trial #5571
""",
u"""
add some useful utilities for skipping tests with unittest's new skipping ability

most significantly apply a modified portion of the patch from #4242 with
patches for skipping implementation details

""",
u"""
add support for PyPy
""",
u"""
roll old test in with new one
""",
u"""
more and more implementations now support sys.subversion
""",
u"""
add much better tests for python version information parsing
""",
u"""
remove uneeded function
""",
u"""
Separate initialization from clearing.
""",
u"""
this can be slightly less ugly
""",
u"""
add shorthands for expected failures and unexpected success
""",
u"""
News item for the platform.py fix (r70594).


""",
u"""
Remove the sys.version_info shortcut, since they cause the APIs
to return different information than the _sys_version() output
used in previous Python versions.

This also fixes issue5561: platform.python_version_tuple returns tuple of ints, should be strings

Added more tests for the various platform functions.


""",
u"""
clarify the type of data returned
""",
u"""
another style nit
""",
u"""
fix newline issue in test summary
""",
u"""
this is better written using assertRaises
""",
u"""
fix typo
""",
u"""
add new skipping things to __all__
""",
u"""
update docstring
""",
u"""
remove special metadata
""",
u"""
some cleanup and modernization
""",
u"""
Add links to related resources.
""",
u"""
update from CVS
""",
u"""
forgot to document that setUp can be skipped (silly me...)
""",
u"""
refactor unittest docs
""",
u"""
comply with the evilJavaNamingScheme for attribute names

It seems my love of PEP 8 overrode the need for consistentcy

""",
u"""
implement test skipping and expected failures

patch by myself #1034053

""",
u"""
complain when there's no last exception
""",
u"""
revert r70552; wrong fix
""",
u"""
fix very old names for exception terms #5543
""",
u"""
The tracking statistics were actually too pessimistic


""",
u"""
Add a heuristic so that tuples and dicts containing only
untrackable objects are not tracked by the garbage collector. This can
reduce the size of collections and therefore the garbage collection overhead
on long-running programs, depending on their particular use of datatypes.

(trivia: this makes the "binary_trees" benchmark from the Computer Language
Shootout 40% faster)


""",
u"""
Make imported name private and wrap long-line.
""",
u"""
speed up the long division algorithm for Python longs.
The basic algorithm remains the same; the most significant speedups
come from the following three changes:

  (1) normalize by shifting instead of multiplying and dividing
  (2) the old algorithm usually did an unnecessary extra iteration of
      the outer loop; remove this.  As a special case, this means that
      long divisions with a single-digit result run twice as fast as
      before.
  (3) make inner loop much tighter.

Various benchmarks show speedups of between 50% and 150% for long
integer divisions and modulo operations.

""",
u"""
Move initialization of root link to __init__.
""",
u"""
Add more comments.  Improve variable names.
Make links clearer by using a Link object
instead of a list.  Use proxy links to avoid
circular references.


""",
u"""
AttributeError can be thrown during recursion errors
""",
u"""
Fixed the tarfile._BZ2Proxy.read() method that would loop
forever on incomplete input. That caused tarfile.open() to hang when used
with mode 'r' or 'r:bz2' and a fileobj argument that contained no data or
partial bzip2 compressed data.

""",
u"""
close the file even if an exception occurs #5536
""",
u"""
- Fix comment macro in python.man

""",
u"""
There is no macro named SIZEOF_SSIZE_T. Should use SIZEOF_SIZE_T instead.
""",
u"""
Rewrite Py_ARITHMETIC_RIGHT_SHIFT so that it's valid for all signed
integer types T, not just those for which "unsigned T" is legal.


""",
u"""
Add MutableSet example.
""",
u"""
Use 30-bit digits for Python longs, on 64-bit platforms.
Backport of r70459.

""",
u"""
Fix typo
""",
u"""
* Add implementation notes.
* Re-order methods so that those touching the underlying data
  structure come first and the derived methods come last.



""",
u"""
* Add clearer comment to initialization code.
* Add optional argument to popitem() -- modeled
  after Anthon van der Neut's C version.
* Fix method markup in docs.


""",
u"""
Silence a compiler warning.
""",
u"""
Add object_pairs_hook to the json module.


""",
u"""
Improve implementation with better underlying data structure
for O(1) deletions.  Big-Oh performance now the same as regular
dictionaries.  Uses a doubly-linked list instead of a list/seq
to track insertion order.


""",
u"""
close files after comparing them
""",
u"""
Use mixin methods where possible. (2.7 only -- these don't all exist in 3.0)
""",
u"""
a much better example
""",
u"""
fix strange errors when setting attributes on tracebacks #4034
""",
u"""
Attempt to fix Solaris buildbot failure on test_locale


""",
u"""
On platforms with sizeof(wchar_t) == 4 and
sizeof(Py_UNICODE) == 2, PyUnicode_FromWideChar now converts
each character outside the BMP to the appropriate surrogate pair.

Thanks Victor Stinner for the patch.

(backport of r70452 from py3k to trunk)


""",
u"""
Updated openssl support on VC6. (openssl-0.9.6g is old, cannot compile with _ssl.c)
If you use http://svn.python.org/projects/external/openssl-0.9.8g, Perl is not needed.
This scheme was ported from PCBuild.
""",
u"""
Fix bug in _insert_thousands_sep: too much zero padding could be
added for 'n' formats with non-repeating thousands-separator.

""",
u"""
merge json library with simplejson 2.0.9 (
""",
u"""
Add support for thousands separator and 'n' format specifier
to Decimal __format__ method.

""",
u"""
I thought this was begging for an example
""",
u"""
Fix bug in Decimal __format__ method that swapped left and right
alignment.

""",
u"""
Add token markup.
""",
u"""
Added skip for old MSVC.
""",
u"""
Move the previously local import of threading to module level.

This is cleaner and avoids lockups in obscure cases where a Queue
is instantiated while the import lock is already held by another thread.

OKed by Tim Peters.

""",
u"""
Fix markup in re docs and give a mail address in regex howto, so that
the recommendation to send suggestions to the author can be followed.

""",
u"""
#5469: add with statement to list of name-binding constructs.
""",
u"""
#5276: document IDLESTARTUP and .Idle.py.
""",
u"""
#5478: fix copy-paste oversight in function signature.
""",
u"""
#5488: add missing struct member.
""",
u"""
#5491: clarify nested() semantics.
""",
u"""
Fix a small nit in the error message if bool() falls back on __len__ and it returns the wrong type: it would tell the user that __nonzero__ should return bool or int.
""",
u"""
#5493: clarify __nonzero__ docs.
""",
u"""
#5496: fix docstring of lookup().
""",
u"""
fix tuple.index() error message #5495
""",
u"""
Make marshalling errors a little more informative as to what went wrong
""",
u"""
Unicode format tests weren't actually testing unicode. This was probably due to the original backport from py3k.
""",
u"""
Allow auto-numbered replacement fields in str.format() strings.

For simple uses for str.format(), this makes the typing easier. Hopfully this
will help in the adoption of str.format().

For example:
'The {} is {}'.format('sky', 'blue')

You can mix and matcth auto-numbering and named replacement fields:
'The {} is {color}'.format('sky', color='blue')

But you can't mix and match auto-numbering and specified numbering:
'The {0} is {}'.format('sky', 'blue')
ValueError: cannot switch from manual field specification to automatic field numbering

Will port to 3.1.

""",
u"""
locale.format() bug when the thousands separator is a space character.


""",
u"""
#5486: typos.
""",
u"""
Fix buglet in the itertools documentation.
""",
u"""
Add reference to solution for a commonly asked question.
""",
u"""
Fixed distutils.test_util tear down
""",
u"""
Require implementations for warnings.showwarning() support the 'line' argument.
Was a DeprecationWarning for not supporting it since Python 2.6.

Closes 

""",
u"""
Fix typo.
""",
u"""
For collections.deque() objects, expose the maxlen parameter as a read-only attribute.
""",
u"""
Small optimization for corner case where maxlen==0.
""",
u"""
Update the decimal FAQ for the from_float() classmethod and improve the recipe for remove_exponent() to make it cut and pasteable.
""",
u"""
Add a version tag to the decimal module.
""",
u"""
Clarify the meaning of normal and subnormal.
""",
u"""
Update url for the spec.
""",
u"""
Fix markup.
""",
u"""
gzip and bz2 are context managers
""",
u"""
Add missing space.

""",
u"""
#5458: add a note when we started to raise RuntimeErrors.

""",
u"""
Add cross-reference to the collections docs.
""",
u"""
Add consume() recipe to itertools docs.
""",
u"""
Fix typo.
""",
u"""
Add Chris Withers.

""",
u"""
fix funky indentation
""",
u"""
Fixed Show a window constructed with tkSimpleDialog.Dialog only 
after it is has been populated and properly configured in order to prevent 
window flashing.

""",
u"""
Fixed Prevent a segfault in _tkinter by using the
guaranteed to be safe interp argument given to the PythonCmd in place
of the Tcl interpreter taken from a PythonCmd_ClientData.

""",
u"""
Fixed Guarantee that Tkinter.Text.search returns a string.
""",
u"""
removed > 2.3 syntax from distutils.msvc9compiler
""",
u"""
Minor bsddb documentation glitch
""",
u"""
mmap.resize for anonymous map is not working yet, so changed to real file mapping...
""",
u"""
Fixed mmap crash after resize failure on windows.

Now uses NULL instead of INVALID_HANDLE_VALUE as invalid map handle
because CreateFileMapping returns NULL when error occurs.
""",
u"""
Fixed memory leak on failure.
""",
u"""
add example
""",
u"""
Fix for 

""",
u"""
Fixes issues 3883 and 5194

""",
u"""
Change framework search order when looking for Tcl/Tk on OSX.

This is needed because the system linker looks in /Library/Framework before
it looks in /System/Library frameworks. Without this patch _tkinter will
be unusable when it is compiled on a system that has Tk 8.5 installed in
/Library/Frameworks (and the Apple 8.4 install in /System/Library/Frameworks)

""",
u"""
Fixed a typo.


""",
u"""
Fix for 

""",
u"""
Fix 

""",
u"""
Remove obsolete stuff from string module docs.

""",
u"""
Fix some more bugs caused by the backport from 3.x for importlib.
Do a more exact copy of the final 3.x code to resolve bugs and add
appropriate tests.

""",
u"""
Backport 70140, 70141, 70143, and 70144.
Adds tests, switches from list to deque, fixes __reduce__
which was unnecessarily copying __keys.


""",
u"""
making the writing more formal
""",
u"""
Fixed subprocess handle leak on failure on windows.
""",
u"""
Fixed memory leak.
""",
u"""
Minor simplification.
""",
u"""
Make the underlying data structure more private.
""",
u"""
Beef-up tests.
""",
u"""
Fix markup.
""",
u"""
Backport 70111: Let configparser use ordered dicts by default.


""",
u"""
Backport 70106: Add OrderedDict support to collections.namedtuple().


""",
u"""
Backport PEP 372: OrderedDict()
""",
u"""
Fix SHA_new and MD5_new, that would crash if not given initial data
""",
u"""
give httplib.IncompleteRead a more sane repr #4308
""",
u"""
removing the force-optimized option as discussed in #1533164
""",
u"""
Adds an optional flags argument to re.split, re.sub and re.subn to be
consistent with the other re module functions.

""",
u"""
The note about caching of regular expression objects was incorrect ReST and 
thus invisible in the compiled documentation.  Fixed.  Also I cleaned up the
wording.

""",
u"""
fix a silly problem of caching gone wrong #5401
""",
u"""
Fix docs for ConfigParser.
""",
u"""
Fix 3k-style metaclass syntax in docstrings.

""",
u"""
Backport r69961 to trunk, replacing JUMP_IF_{TRUE,FALSE} with
POP_JUMP_IF_{TRUE,FALSE} and JUMP_IF_{TRUE,FALSE}_OR_POP. This avoids executing
a POP_TOP on each conditional and sometimes allows the peephole optimizer to
skip a JUMP_ABSOLUTE entirely. It speeds up list comprehensions significantly.

""",
u"""
typo in cmath.cos and cmath.cosh docstring

""",
u"""
Binary flag is needed on windows.
""",
u"""
Fixed mmap crash in accessing elements of second map object
with same tagname but larger size than first map. (Windows)
""",
u"""
mmap.write_byte didn't check map size, so it could cause buffer
overrun.
""",
u"""
Issues #1533164 and #5378: Added quiet and force-optimize options to Distutils bdist_rpm command
""",
u"""
#5365: add quick look conversion table for different time representations.
""",
u"""
#5344: fix punctuation.
""",
u"""
#5363: fix cmpfiles() docs. Another instance where a prose description is twice as long as the code.
""",
u"""
#5361: fix typo.
""",
u"""
make Distutils compatible with 2.3 again.
""",
u"""
Give mapping views a usable repr.
""",
u"""
Fix a bug where code was trying to index an int. Left over from the situation
from using str.rpartition to str.rindex.

Closes Issue5213.

""",
u"""
more info on long_description
""",
u"""
removed unused import
""",
u"""
The curses panel library is now supported
""",
u"""
remove deprecated symtable.Symbol methods
""",
u"""
comma
""",
u"""
the startship is rather outdated now
""",
u"""
Document that setting sys.py3kwarning wont do anything.
""",
u"""
fix str.format()'s first arg #5371
""",
u"""
Fix typo.
""",
u"""
Clarify Counter() docs.
""",
u"""
Fixed #5316 : test failure in test_site
""",
u"""
Replace long with twodigits, to avoid depending
on sizeof(digit) < sizeof(long)

""",
u"""
Remove reference to zero argument form of super() in 2.x docs.
""",
u"""
More markup and spelling fixes.
""",
u"""
Restore Py2.x version of sample call to super().
""",
u"""
Sync-up py3.1 doc updates for super().
""",
u"""
Tools/scripts/analyze_dxp.py, a module with some helper functions to
analyze the output of sys.getdxp().

""",
u"""
Expand upon test_site.test_s_option to try to debug its failure.

""",
u"""
Backport 69934:  Register xrange() as a Sequence.


""",
u"""
Fix call to os.waitpid, it does not take keyword args.
""",
u"""
update README on running tests
""",
u"""
Update itertools recipes to use next().
""",
u"""
Fix grammar.
""",
u"""
#5352: str.count() counts non-overlapping instances.

""",
u"""
more test coverage
""",
u"""
#5349: C++ pure virtuals can also have an implementation.

""",
u"""
#5348: format() converts all kinds of values.
""",
u"""
- Link the shared python library with $(MODLIBS).

""",
u"""
Removing unused __main__ sections
""",
u"""
removing map and lambda usage, so the test is similar to py3k's branch one
""",
u"""
moved distutils.text_file tests into a real unittest class
""",
u"""
Revert debugging statements, culprit is possibly test_distutils (see #5316)


""",
u"""
Try to make sense of the test_site buildbot failures


""",
u"""
using versionchanged instead of versionadded for distutils doc on sdist default files
""",
u"""
fix compiler warnings
""",
u"""
Fix a variety of spelling errors.

""",
u"""
#5338, #5339: two types in the API manual.
""",
u"""
Speedup and simplify negative counter using count's new step argument.
""",
u"""
Fix keyword arguments for itertools.count().
Step arg without a start arg was ignored.


""",
u"""
Typos in turtle.py

""",
u"""
special-case string formatting in BINARY_MODULO implementation. This shows a modest (1-3%) speed-up in templating systems, for example.

""",
u"""
Improve error message when unknown format codes are used when using str.format() with str, unicode, long, int, and float arguments.
""",
u"""
Fix punctuation.

""",
u"""
At least separate imports from other statements.
""",
u"""
#5327: fix a broken link by joining it.
""",
u"""
revert r69777 since all the experts agree that extra import lines distract from the code
""",
u"""
Since we recommend one module per import line, reflect this also in the
documentation.

""",
u"""
#5317: update IronPython URL.

""",
u"""
#5287: Add exception handling around findCaller() call to help out IronPython.
""",
u"""
Inline coefficients in gamma().  Add reflection formula.  Add comments.
""",
u"""
#5310, #3558: fix operator precedence table.
""",
u"""
Add links to helpful external resources.
""",
u"""
Add an example for math.fsum() and elaborate on the accurary note.
""",
u"""
Add some cross-references to the docs.  Simplify the python code equivalent for izip().  Supply an optional argument for the nth() recipe.
""",
u"""
Add keyword arg support to itertools.repeat().
""",
u"""
Add keyword arg support to itertools.compress().
""",
u"""
Py3k warnings now automatically include -Qwarn for division.
""",
u"""
Generalize the itertools.tee() recipe.
""",
u"""
Clarify socket timeout behavior vs system network stack behavior on connect
for issue5293.

""",
u"""
#5268: mention VMSError.

""",
u"""
#5296: sequence -> iterable.

""",
u"""
#5297: fix example.

""",
u"""
fixed the data_files inclusion behavior
""",
u"""
Fixed mmap resize on 32bit windows and unix. When offset > 0,
The file was resized to wrong size.

""",
u"""
Clarify the deprecation of platform.dist().

Add versionadded tags.


""",
u"""
Fix issue776533.

""",
u"""
Fixup intro paragraphs for the itertools docs.  Add some tables for quick reference.
""",
u"""
Fixed mmap crash on its boundary access m[len(m)].
""",
u"""
#2279 added the plain path case for data_files
""",
u"""
Fix-up intro paragraph for collections docs.
""",
u"""
Add explanation for super(type1, type2).
""",
u"""
Documentation for super() neglects to say what super() actually does


""",
u"""
note about #2279
""",
u"""
#2279: use os.sep so the MANIFEST file test work on win32
""",
u"""
Fixed #2279: distutils.sdist.add_defaults now add files listed in package_data and data_files
""",
u"""
PyList_Append() can fail
""",
u"""
remove some PyBytes_* aliases that are not in 3.x
""",
u"""
fix compiler warnings
""",
u"""
Add GC support to count() objects.  Backport candidate.
""",
u"""
note functions that are not aliased to PyBytes_ #5280
""",
u"""
Added Ross Light to ACKS, for bug 4285 (r69331).
""",
u"""
A few more minor fixes in longobject.c

""",
u"""
Various portability and standards compliance fixes, optimizations
and cleanups in Objects/longobject.c.  The most significant change is that
longs now use less memory:  average savings are 2 bytes per long on 32-bit
systems and 6 bytes per long on 64-bit systems.  (This memory saving already
exists in py3k.)

""",
u"""
Fixed typo.
""",
u"""
#5179: don't leak PIPE fds when child execution fails.
""",
u"""
this needn't be a shebang line
""",
u"""
we're no longer using CVS, so this doesn't have to be binary
""",
u"""
Replace variable
""",
u"""
Fix for #5257: refactored all tests in distutils, so they use a temporary directory.
""",
u"""
Add keyword argument support to itertools.count().
""",
u"""
fix the environ for distutils test_util
""",
u"""
Fixed #4524: distutils build_script command failed with --with-suffix=3
""",
u"""
added tests for distutils.util
""",
u"""
Add optional code signing after merging.
""",
u"""
Update Tix build procedure.
""",
u"""
Move amd64 properties further to the top, so that they override
the linker options correctly.
""",
u"""
reverted leak fix, to use the one done in py3k branch (r67382)
""",
u"""
Fix compiler warning (gcc)


""",
u"""
Reduce hash collisions for objects with no __hash__ method by
rotating the object pointer by 4 bits to the right.


""",
u"""
Fix warnings GCC emits where the argument of PyErr_Format is a single variable.

""",
u"""
Fix warnings GCC emits where the argument of PyErr_Format is a single variable.

""",
u"""
#3694: add test for fix committed in r66693.
""",
u"""
#1661108: note that urlsafe encoded string can contain "=".
""",
u"""
#3734: document complex coercing behavior better.
""",
u"""
#4894: document "newurl" parameter to redirect_request().
""",
u"""
#5158: added documentation on the depends option in distutils extensions
""",
u"""
Add links to the other versions we have in stock.

""",
u"""
- Fix hashlib to always reject unicode and non buffer-api
  supporting objects as input no matter how it was compiled (built in
  implementations or external openssl library).
(backported from a py3k branch)

""",
u"""
fixing the leak introduced in r69304
""",
u"""
Typo fix.

""",
u"""
One more test.
""",
u"""
Add an extra testcase.
""",
u"""
Fix spaces/tabs in example.
""",
u"""
added a step argument to itertools.count() and allowed non-integer arguments.


""",
u"""
no need for this __bases__ trick anymore
""",
u"""
os.fsync() should be used to ensure that data is written to disk
""",
u"""
Fixes socket.inet_aton() to always return 4 bytes even
on LP64 platforms (most 64-bit Linux, bsd, unix systems).

""",
u"""
Define _PyVerify_fd on VC6 to make
test_fdopen (test_os.py) pass.
""",
u"""
Clean-up named tuple docs.
""",
u"""
Issue#5203: ctypes segfaults when passing a unicode string to a
function without argtypes, if HAVE_USABLE_WCHAR_T is false.

""",
u"""
_testcapi depends on testcapi_long.h

Thanks Lisandro Dalcin.

""",
u"""
PyLong_AsUnsignedLongLong now raises OverflowError for
negative arguments.  Previously, it raised TypeError.

Thanks Lisandro Dalcin.


""",
u"""
Add a function to test the validity of file descriptors on Windows, and stop using global runtime settings to silence the warnings / assertions.
""",
u"""
Fixed svn:eol-style.
""",
u"""
Set eol-style to native
""",
u"""
Silence compiler warnings when compiling sqlite with VC++.
""",
u"""
Fixed #3386: the optional prefix argument was ignored under OS2 and NT in distutils.sysconfig.get_python_lib
""",
u"""
compileall used the ctime of bytecode and source to determine if the bytecode
should be recreated. This created a timing hole. Fixed by just doing what
import does; check the mtime and magic number.

""",
u"""
collections.namedtuple() to support automatic renaming of invalid fieldnames.
""",
u"""
Enforcing Tk 8.3.1 requirement.
""",
u"""
Fixed Synchronize tk load failure check to prevent a
potential deadlock.

""",
u"""
Checking for tk availability before continuing (basically the same that is done in test_ttk_guionly)
""",
u"""
Some tests for Tkinter.Text.search

""",
u"""
itertools.product docstring missing 'repeat' argument


""",
u"""
Fixed Handle empty text search pattern in 
Tkinter.Text.search

""",
u"""
Turned setup_master public
""",
u"""
fix Py_IS_INFINITY macro to work correctly on x87 FPUs.
It now forces its argument to double before testing for infinity.

""",
u"""
Fixed Unicode output bug in logging and added test case. This is a regression which did not occur in 2.5.

""",
u"""
Silence 'arg may be used uninitialized in this function' warning from gcc.

""",
u"""
a few edits and typos
""",
u"""
make sure that hash(2**63) == hash(2.**63) on 64-bit
platforms.  The previous code was fragile, depending on the twin
accidents that:

  (1) in C, casting the double value 2.**63 to long returns the integer
      value -2**63, and
  (2) in Python, hash(-2**63) == hash(2**63).

There's already a test for this in test_hash.

""",
u"""
document numliterals fixer
""",
u"""
Remove redundant assignment in _PyObject_LengthHint

""",
u"""
closeout: Make ZipImport.get_filename() a public method
""",
u"""
Mention patch submitter in NEWS entry for r69419
""",
u"""
Restore the ability to execute packages with the -m switch (but this time in a way that leaves the import machinery in a valid state). (Original patch by Andi Vajda)
""",
u"""
document individual 2to3 fixers
""",
u"""
make destinsrc private
""",
u"""
make "super only for new-style classes" a note.
""",
u"""
Add test for explict global statement works.

""",
u"""
Fix broken test in test_hotshot.  Treating the current directory as an
empty file is sloppy and non-portable.  Use NamedTemporaryFile to make
an empty file.

""",
u"""
#5174: fix wrong file closing in example.
""",
u"""
Eliminated the need to use ttk.__loadtk__ and the problems related it.

""",
u"""
The Python compiler now handles explict global statements
correctly (should be assigned using STORE_GLOBAL opcode).  This was done by
having the system table differentiate between explict and implicit globals.

""",
u"""
Make names generated for 'with' variables match the built-in compiler.

""",
u"""
#3986 replacing string and types call (like in the Py3k branch), and put exec_msg call at the right place
""",
u"""
Call Tcl_ConditionFinalize for Tcl_Conditions that will
not be used again (this requires Tcl/Tk 8.3.1), also fix a memory 
leak in Tkapp_Call when calling from a thread different than the one that 
created the Tcl interpreter.

""",
u"""
Partial fix to memory leak in Tkapp_Call when calling
from a thread different than the one that created the Tcl interpreter.

""",
u"""
Convert "srcdir" into an absolute path if that seems prudent.  Currrently
the only user of this is Lib/distutils/tests/test_build_ext.py (in order
to find the source for xxmodule.c).  I'm not sure if other platforms
need similar tweaks, I'm not brave enough to attempt it without being
able to test.

""",
u"""
Overhaul Lib/compiler block ordering.  The previous code was filled with
hacks.  The new code is based on posted by Antoine Pitrou.  I
did some further cleanups of the pyassem code and optimized the block
ordering pass.

""",
u"""
Fixed #5167: test_customize_compiler does not apply under non unix compilers
""",
u"""
Ivan on IRC in #twisted reported this crasher.

""",
u"""
Fix a number of Win32ErrorTests error cases.  chmod wasn't being tested.  'access' never raises an error.
""",
u"""
removed types usage and added test coverage (work for #3986)
""",
u"""
Fixed #3987 : removed unused import
""",
u"""
fix download link
""",
u"""
fixed #1520877: now distutils reads Read  from the environment/Makefile
""",
u"""
using >= so setting verbose to 2 will work as well
""",
u"""
Implement convert sys.version_info to a named
tuple. Patch by Ross Light.
""",
u"""
README now reflects the current state
""",
u"""
Fixed #1276768: verbose option was not used in the code.
""",
u"""
Distutils apparently requires an absolute path so provide one.

""",
u"""
Fixed #5132: enable extensions to link on Solaris
""",
u"""
Oops, Mac build needs the 'incdirlist' variable so restore it.

""",
u"""
Make setup.py work when building in a directory other than the
source directory.  Mainly use 'srcdir' rather than os.getcwd() or
'.'.

""",
u"""
Fix test_build_ext.py to work when building in a separate directory.
Since "srcdir" should now be defined on all platforms, use it to
find the module source.

""",
u"""
Since sysconfig.get_python_inc() now works when building in a
directory other than the source directory, simplify the test code in
test_sysconfig.py.

""",
u"""
Fix get_python_inc() to work when building in a directory separate from
the source.  Also, define 'srcdir' on non-posix platforms.

""",
u"""
#5031: fix Thread.daemon property docs.
""",
u"""
#4563: disable alpha and roman lists, fixes wrong formatting of contributor list.
""",
u"""
#4820: use correct module for ctypes.util.
""",
u"""
#4827: fix callback example.
""",
u"""
#5015: document PythonHome API functions.
""",
u"""
PyErr_PrintEx is also in 2.x...
""",
u"""
#5059: fix example.
""",
u"""
#5144: document that PySys_SetArgv prepends the script directory (or the empty string) to sys.path.
""",
u"""
#5153: fix typo in example.
""",
u"""
Fix comment for #1835
""",
u"""
Clarify that named tuples do not have to subclass tuple.
""",
u"""
Tweak the docs for Counter() objects.
""",
u"""
Doc fixes. Remove overbroad, redundant warnings.  Fixup example code.
""",
u"""
Minor doc fixups.
""",
u"""
Provide checks for the format string of strftime, and for the "mode" string of fopen on Windows.  These strings are user provided from python and so we can avoid invoking the C runtime invalid parameter handler by first checking that they are valid.
""",
u"""
Make importlib backwards-compatible to Python 2.2 (but this is not promised to
last; just doing it to be nice).

Also fix a message for an exception.

""",
u"""
This refactoring should make it easier to add new calling conventions.

Replace ffi_call_STDCALL and ffi_call_SYSV by a ffi_call_x86 function
that cleans up the stack when FFI_SYSV is used, and does nothing for
FFI_STDCALL.

Remove libffi_msvc\win32.S, which is out of date and also unused; it
was only used for building ctypes with the MingW compiler.

""",
u"""
Backport importlib to at least Python 2.5 by getting rid of use of str.format.
""",
u"""
Ignore bytecode files in importlib.
""",
u"""
Make importlib a package. This allows using svn:externals in the sandbox to
package up the code for separate distribution.

""",
u"""
Register decimals as numbers.Number
""",
u"""
Record operator deprecations in docs.
""",
u"""
Validate that __length_hint__ returns a usable result.
""",
u"""
list(obj) can swallow KeyboardInterrupt.
""",
u"""
NEWS entry for 
""",
u"""
Fix for 
""",
u"""
Moving to importlib
""",
u"""
Restore the previous geometry before leaving the test
""",
u"""
Fix build with Py_NO_ENABLE_SHARED on Windows.
""",
u"""
Set native svn:eol-style property for text files.
""",
u"""
Use a single Tcl interpreter through all these tests, this may help some 
failing buildbots.

""",
u"""
Restore Tkinter.Tk._loadtk so this test doesn't fail for problems 
related to ttk.

""",
u"""
wording for for issue4903.

""",
u"""
Update doc wording as suggested in issue4903.

""",
u"""
more flags which only work for function blocks
""",
u"""
add explanatory comment
""",
u"""
- The socket module now raises OverflowError when 16-bit port and
  protocol numbers are supplied outside the allowed 0-65536 range on bind()
  and getservbyport().

""",
u"""
markup fix
""",
u"""
fix indentation in comment
""",
u"""
fix indentation; looks like all I managed to do the first time is make things uglier
""",
u"""
fix indentation
""",
u"""
I believe the intention here was to avoid a global lookup
""",
u"""
fix indentation
""",
u"""
PyErr_BadInternalCall() raises a SystemError, not TypeError #5112
""",
u"""
Add an extra test for long <-> float hash equivalence.

""",
u"""
completely detabify unicodeobject.c
""",
u"""
Text edits and markup fixes
""",
u"""
Add a section
""",
u"""
check the errno in bad fd cases
""",
u"""
make _tkinter._flatten check the result of PySequence_Size for errors #3880
""",
u"""
pep8tify conditionals
""",
u"""
fixed test_make_distribution so it runs on any platform, as long as tar an gzip are available
""",
u"""
shutil.move() could believe that its destination path was
inside its source path if it began with the same letters (e.g. "src" vs.
"src.new").


""",
u"""
Fix issue5075: bdist_wininst should not depend on the vc runtime?

""",
u"""
Fix typo.
""",
u"""
Update itertools.__doc__ to include all tools.
""",
u"""
fix download url
""",
u"""
Ignore .pyc and .pyo files.

""",
u"""
Minor spelling mistake in datetime docs.

""",
u"""
Clarify some __del__ stuff.

""",
u"""
Correct docs for ABCs (MutableSequence was missing __setiem).  Simplify the table by taking out inherited requirements for abstract methods.
""",
u"""
Fixed next() vs __next__() issues in the ABCs
for Iterator and MutableSet.  Also added thorough test for
required abstractmethods.



""",
u"""
New 'gui' resource for regrtest.

""",
u"""
Make sure the root windows gets destroyed
""",
u"""
* Renaming test_tk_* to test_ttk_* since that is what they are testing.
* Added ttk tests to the expected skips mapping just like where test_tcl 
was expected to be skipped too.

""",
u"""
Added support for collecting tests only from specific packages.

""",
u"""
Demos for ttk added.

""",
u"""
Added the ttk module. See Ttk support for Tkinter.

""",
u"""
use True and False
""",
u"""
On Windows, use the Python 'Activation Context' when loading extensions
to avoid problems loading the CRT from a private assembly.  Via bug 4566.

""",
u"""
Add more tests for the powerset() recipe.
""",
u"""
More exhaustive combinatoric checks.
""",
u"""
doctest.testfile should set __name__
""",
u"""
Stronger tests for combinatoric relationships.
""",
u"""
Add tests to verify combinatoric relationships.
""",
u"""
excellent place to use a set() #5069
""",
u"""
Promote combinations_with_replacement() from a recipe to a regular itertool.
""",
u"""
Tweak column alignment for collections docs.


""",
u"""
Remove startup firewall message.  That is handled by an error dialog
whenever a connection cannot be formed.  Also, the Idle version number
is already in the About Idle dialog.  Now, the startup is clean looking
once again.


""",
u"""
Fix occasional failure of bsddb/test/test_lock.py.  Thanks
Hirokazu Yamamoto for the patch.

""",
u"""
Fix comment.

""",
u"""
Fix undefined behaviour (left shift of negative value) in long_hash.  Also,
rewrap a line of length > 79, and update comments.


""",
u"""
Copy over docs on advanced role features from Sphinx docs.

""",
u"""
Fix signed/unsigned mismatch.
""",
u"""
Backport importlib in the form of providing importlib.import_module(). This has
been done purely to help transitions from 2.7 to 3.1.

""",
u"""
Fixed #1885: --formats=tar,gztar was not working properly in the sdist command
""",
u"""
No need for carry to be type twodigits in _PyLong_AsByteArray; digit is large enough.
This change should silence a compiler warning on Windows.

""",
u"""
added missing module docstring
""",
u"""
removed backward compatibility information (out of date)
""",
u"""
Improved itertools recipe for generating powerset().
""",
u"""
Promote compress() from a recipe to being a regular itertool.
""",
u"""
removing remaining bits
""",
u"""
Fixed #4863: removed distutils.mwerkscompiler
""",
u"""
Fixed compile error on windows.
""",
u"""
fix building the core with --disable-unicode

I changed some bytearray methods to use strings instead of unicode like bytes_repr
Also, bytearray.fromhex() can take strings as well as unicode

""",
u"""
Remove uses of cmp from the decimal module.

""",
u"""
Properly document multiprocessing's logging support, resolve outstanding issues with the custom levels
""",
u"""
fix occasional test_pickletools failures.

""",
u"""
Fix unpickling of subnormal floats, which was raising
ValueError on some platforms as a result of the platform strtod setting
errno on underflow.


""",
u"""
Fix occasional test_kqueue failure on OS X.

""",
u"""
Help Tcl to load even when started through the
unreadable local symlink to "Program Files" on Vista.

""",
u"""
Add heading for 2.7a0.

""",
u"""
fix 3 classes of potential portability problems in longobject.c:
 - fix some places where counters into ob_digit were declared as
   int instead of Py_ssize_t
 - add (twodigit) casts where necessary
 - fix code in _PyLong_AsByteArray that uses << on negative values

""",
u"""
Extract directories properly in the zipfile module;
allow adding directories to a zipfile.

""",
u"""
Add a test for UNC import paths, see 
""",
u"""
Add various items
""",
u"""
multiprocessing fails to compile under --without-threads
""",
u"""
apply() documentation is unclear
""",
u"""
Clarify wording.

""",
u"""
Update comments and add an optimized path for Counter.update().
""",
u"""
More doc tweaks.
""",
u"""
Tighten-up the docs for Counter().
""",
u"""
Simplify explanation of multiset operations by removing restrictions on negative inputs.
""",
u"""
Markup fixes
""",
u"""
Add some items
""",
u"""
multiprocessing: failure in manager._debug_info()
""",
u"""
When a file is opened in append mode with the new IO library,
do an explicit seek to the end of file (so that e.g. tell() returns the
file size rather than 0). This is consistent with the behaviour of the
traditional 2.x file object.


""",
u"""
Beautify and cleanup the references section.
""",
u"""
Fixed bug in FileHandler when delay was set - added fix for RotatingFileHandler and changed header comment slightly.
""",
u"""
Fixed bug in FileHandler when delay was set.
""",
u"""
__slots__ on Fractions was useless.


""",
u"""
fix url
""",
u"""
backport r68802 (bugfix)
""",
u"""
allow unicode keyword arguments for the ** syntax #4978
""",
u"""
Fix typos.
""",
u"""
Use Georg's new permalinks to documentation by version number.
That assures that IDLE's help always points to the correct
version and the latest update with all bug fixes.


""",
u"""
Don't disrupt automatic url target name generation
with manually specified, conflicting names.

Before: 
    http://docs.python.org/dev/library/collections.html#id1

After:
    http://docs.python.org/dev/library/collections.html#counter-objects



""",
u"""
Make merging easier by formattng comment blocks the same in Py3.1
""",
u"""
Add Counter() to __all__.
""",
u"""
Build-outs for Counter() class:
* Constructor and update() support keyword args (like their dict counterparts).
* The 'del' statement no longer raises KeyError for missing values.
* Add multiset operations:  __add__, __sub__, __and__, __or__.


""",
u"""
fix windows warning that I intro'ed with r68768
""",
u"""
I'm sick of these deprecations warnings in test_os
""",
u"""
make bad file descriptor tests more robust
""",
u"""
add email address
""",
u"""
move BufferedIOBase into the base class section
""",
u"""
simplify code
""",
u"""
add a note about the ftruncate change
""",
u"""
Resolve (segfault) _multiprocessing.Connection() doesn't check handle
""",
u"""
Removed merge tracking for "svnmerge" for 
svn+ssh://pythondev@svn.python.org/python/branches/tnelson-trunk-bsddb-47-upgrade

""",
u"""
Removed merge tracking for "svnmerge" for 
svn+ssh://pythondev@svn.python.org/python/branches/trunk-math

""",
u"""

Let os.ftruncate raise OSError like documented.
""",
u"""
Added more cross-reference targets and tidied up list of useful handlers.
""",
u"""
raise an OSError for invalid fds #4991
""",
u"""
fix encoding cookie case
""",
u"""
fix test that wasn't working as expected #4990
""",
u"""
patch logging to add processName, remove the old _check_logger_class code
""",
u"""
#4986: augassigns are not expressions.
""",
u"""
#4923: clarify what was added.
""",
u"""
#4857: fix augmented assignment target spec.
""",
u"""
#4979: correct result range for some random functions.
""",
u"""
make test_capi.py more robutst, it times out on some platforms, presumably waiting for threads.  Lower the thread count to 16.
""",
u"""
#4914: trunc is in math.
""",
u"""
#4974: fix redundant mention of lists and tuples.
""",
u"""
#4976: union() and intersection() take multiple args, but talk about "the other".
""",
u"""
Resolve AssertionError in mp_benchmarks.py
""",
u"""
fix grammar
""",
u"""
bytearrays are mutable sequences
""",
u"""
follow-up of #3997: since 0xFFFF numbers are not enough to indicate a zip64 format,
always try to read the "zip64 end of directory structure".

""",
u"""
fix inspect.isclass() on instances with a custom __getattr__ #1225107
""",
u"""
#4077: No need to append \n when calling Py_FatalError
+ fix a declaration to make it match the one in pythonrun.h

""",
u"""
#4930: Slightly cleaner (and faster) code in type creation:
compare slots by address, not by name.

""",
u"""
#3997: zipfiles generated with more than 65536 files could not be opened 
with other applications.

Reviewed by Martin, will backport to 2.6 and 3.0

""",
u"""
trying to find some fpathconf() settings that all unixs support...
""",
u"""
use enumerate
""",
u"""
Change an example in the docs to avoid a mistake when the code is copy
pasted and changed afterwards.

""",
u"""
compare with == not is #4946
""",
u"""
Minor changes/corrections in markup.
""",
u"""
Made minor changes/corrections in markup. Added a couple of section headings.
""",
u"""
Make all the invalid fd tests for os subject to the function being available.
""",
u"""
Fix two test cases in test_os.  ftruncate raises IOError unlike all the others which raise OSError.  And close() on some platforms doesn't complain when given an invalid file descriptor.
""",
u"""
Handle socket errors when receiving
""",
u"""
Another typo fix.

""",
u"""
Comment typo

""",
u"""
Fix occasional test_socket failure on OS X.

""",
u"""
Fix recently introduced test cases.
For datetime, gentoo didn't seem to mind the %e format for strftime.  So, we just excercise those instead making sure that we don't crash.
For test_os, two cases were incorrect.
""",
u"""
Re-enable all tests for windows platforms.
Also, explicitly connect to the IPV4 address.  On windows platforms supporting AF_INET6, the SocketProxy would connect using socket.create_connection('localhost', port) which would cycle through all address families and try to connect.  It would try connecting using AF_INET6 first and this would cause a delay of up to a second.
""",
u"""
Fix-up indentation of sample code blocks for namedtuple mthod definitions.
""",
u"""
Add tests for __init__() and update() with no args.
""",
u"""
Minor doc tweaks.
""",
u"""
fix test_xmlrpc failures #4939
""",
u"""
#1162154: inspect.getmembers() now skips attributes that raise AttributeError,
e.g. a __slots__ attribute which has not been set.

""",
u"""
#4807: Remove a wrong usage of wsprintf in the winreg module
("windows sprintf", different than swprintf)

Needed for the windows CE port.

""",
u"""
The overflow checking code in the expandtabs() method common
to str, bytes and bytearray could be optimized away by the compiler, letting
the interpreter segfault instead of raising an error.


""",
u"""
de-spacify
""",
u"""
Use assertRaises.

""",
u"""
add bytearrayobject.h to PYTHON_HEADERS
""",
u"""
make bytearrayobject.o depend on the stringlib #4936
""",
u"""
Fix refcount leak in error cases.  Bug found by coverity.
""",
u"""
Note that first coord. is left alone
""",
u"""
ast.literal_eval can properly evaluate complex numbers now.  This fixes issue4907.


""",
u"""
Incorrect comments for MutableSet.add() and MutableSet.discard().

Needs to be backported to 2.6 and forward ported to 3.0 and 3.1.


""",
u"""
Add table of idioms/patterns for using Counter objects.
Improve the appearance and flow of the References section -- it used
to have a box around it that wasn't distinct from the preceding code
boxes and it had a weird bolding pattern and hanging indents that
made the section disproportionately large.


""",
u"""
Fix call signature and markup.

""",
u"""
Speed-up __repr__.  Eliminate duplicate tests.  Use a from-irmport.
""",
u"""
Fixup and simplify docstrings and doctests.
""",
u"""
Minor documentation tweaks and simpler update() example.
""",
u"""
small logic correction
""",
u"""
Simplify Counter() API.  Replace items keyword argument
with a mapping.  Makes Counter() idempotent, makes update()
API the same as Counter.__init__(), makes a more readable
repr, makes the API more dict-like, and allows Steven
Bethard's update() example to work.


""",
u"""
#3720: Interpreter crashes when an evil iterator removes its own next function.

Now the slot is filled with a function that always raises.

Will not backport: extensions compiled with 2.6.x would not run on 2.6.0.

""",
u"""
Add collections.Counter().
""",
u"""
Minor changes/corrections in markup.
""",
u"""
Add tests for invalid format specifiers in strftime, and for handling of invalid file descriptors in the os module.
""",
u"""
Optimize heapq.nsmallest/nlargest for cases where n==1 or n>=size.
""",
u"""
Misc/NEWS for 
""",
u"""
Update Misc/NEWS for 
""",
u"""
Use NT threading on CE.

""",
u"""
Port sysmodule to Windows CE.

""",
u"""
add email addresses
""",
u"""
Update the documentation for binascii and zlib crc32/adler32 functions
to better describe the signed vs unsigned return value behavior on
different platforms and versions of python.  Mention the workaround to
make them all return the same thing by using & 0xffffffff.

Fixes issue4903.

Also needs to be merged into release26-maint, release30-maint, & py3k.

""",
u"""
correct email address

""",
u"""
Allow buffering for HTTPResponse
""",
u"""
Use _strdup on Windows CE.

""",
u"""
Fix build of parsermodule under Cygwin.

""",
u"""
Fixed version number in build_ssl.bat.
""",
u"""
macos 9 isn't supported
""",
u"""
move seealso to a more appropiate place
""",
u"""
make tests fail if they can't be imported
""",
u"""
Corrected minor typo and added .currentmodule directives to fix missing cross-references.
""",
u"""
Remove an unnecessary check from test_decimal.

""",
u"""
fix encoding
""",
u"""
Add ACKS entries for some of the patches I've been committing.


""",
u"""
tp_iter only exists with Py_TPFLAGS_HAVE_ITER #4901
""",
u"""
rewrite verbose conditionals
""",
u"""
- ctypes.util.find_library(): Robustify. Fix library detection on
  biarch systems. Try to rely on ldconfig only, without using objdump and gcc.

                """,
u"""
Add NEWS entry for r68484.
""",
u"""
GzipFile and BZ2File now support the context manager protocol.


""",
u"""
Corrected an incorrect self-reference.
""",
u"""
Minor documentation changes cross-referencing NullHandler to the documentation on configuring logging in a library.
""",
u"""
Preserve windows error state across PyThread_get_key_value
""",
u"""
Added helper script to build Tcl/Tk.
""",
u"""
Link to debug version of Tcl/Tk when python is built as debug version.
""",
u"""
Bump up Tcl/Tk version on VC6. (tcl8.4.12 -> tcl8.5.2, tk8.4.12 -> tk8.5.2, tix8.4.0 -> tix8.4.3)
""",
u"""
Change the criteria for doing a full garbage collection (i.e.
collecting the oldest generation) so that allocating lots of objects without
destroying them does not show quadratic performance. Based on a proposal by
Martin von Lowis at http://mail.python.org/pipermail/python-dev/2008-June/080579.html.


""",
u"""
Make Py_AddPendingCall() thread safe
Add test cases and documentation
""",
u"""
Make Py_AddPendingCall() thread safe
""",
u"""
Let users of HTTPConnection.endheaders() submit a message body to the function if required.
""",
u"""
HTTPRequest._send_output() now deals with the case of the message body not being a string.  This allows clients to use endheaders(message_body) instead of endheaders() + send(message_body) without making any extra checks.
""",
u"""
Fix import from UNC paths on Windows.
""",
u"""
Improved thread support and TLS for Windows
""",
u"""
Fix preventing a crash in the socket code when python is compiled
with llvm-gcc and run with a glibc <2.10.

""",
u"""
Bump up bsddb version on VC6. (db-4.4.20 -> db-4.7.25)
""",
u"""
Bump up bzip2 version on VC6. (bzip2-1.0.3 -> bzip2-1.0.5)
""",
u"""
remove temporary code now
""",
u"""
be more specific in -3 option help
""",
u"""
add -3 to manpage
""",
u"""
fix spelling
""",
u"""
fix markup
""",
u"""
specify what -3 warnings are about
""",
u"""
Merged revisions 68306-68308,68340,68368,68422 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r68306 | benjamin.peterson | 2009-01-04 12:27:19 -0600 (Sun, 04 Jan 2009) | 1 line
  
  fix_urllib: add mappings for the url parsing functions
........
  r68307 | benjamin.peterson | 2009-01-04 12:30:01 -0600 (Sun, 04 Jan 2009) | 1 line
  
  remove duplicated function
........
  r68308 | benjamin.peterson | 2009-01-04 12:50:34 -0600 (Sun, 04 Jan 2009) | 1 line
  
  turtle is no longer renamed
........
  r68340 | georg.brandl | 2009-01-05 02:11:39 -0600 (Mon, 05 Jan 2009) | 2 lines
  
  Fix undefined locals in parse_tokens().
........
  r68368 | benjamin.peterson | 2009-01-06 17:56:10 -0600 (Tue, 06 Jan 2009) | 1 line
  
  fix typo (thanks to Robert Lehmann)
........
  r68422 | benjamin.peterson | 2009-01-08 20:01:03 -0600 (Thu, 08 Jan 2009) | 1 line
  
  run the imports fixers after fix_import, so fix_import doesn't try to make stdlib renames into relative imports #4876
........

""",
u"""
fixed #4394 make the storage of the password optional in .pypirc
""",
u"""
Forward port r68394 for 
""",
u"""
use new sphinx modules
""",
u"""
string exceptions are gone
""",
u"""
Change COUNT_ALLOCS variables to Py_ssize_t.

""",
u"""
clarify documentation for random.expovariate.

""",
u"""
test_msvc9compiler failed on VC6/7.
Reviewed by Amaury Forgeot d'Arc.
""",
u"""
Use shutil.rmtree rather than os.rmdir.


""",
u"""
When importing a module from a .pyc (or .pyo) file with
an existing .py counterpart, override the co_filename attributes of all
code objects if the original filename is obsolete (which can happen if the
file has been renamed, moved, or if it is accessed through different paths).
Patch by Ziga Seilnacht and Jean-Paul Calderone.


""",
u"""
Fix #4846 (Py_UNICODE_ISSPACE causes linker error) by moving the declaration
into the extern "C" section.

Add a few more comments and apply some minor edits to make the file contents
fit the original structure again.


""",
u"""
Make sure to checkout any new packages
""",
u"""
Update make.bat.

""",
u"""
use Jinja 2.1.1
""",
u"""
Add an optional argument to the GzipFile constructor to override the timestamp in the gzip stream.


""",
u"""
Misc/NEWS entry for r68317

""",
u"""
More Python 2.3 compatibility fixes for decimal.py.

""",
u"""
Fix Decimal.from_float to use valid Python 2.3 syntax, as per
comments at top of decimal.py.  (But note that the from_float
method itself with still not be usable before Python 2.7.)
See for discussion.

""",
u"""
It's wrong to use AC_REPLACE_FUNCS for hypot, since there's no longer any
Python/hypot.c replacement file.  Use AC_CHECK_FUNCS instead.  This change
should be backported to 2.6 and 3.0.

""",
u"""
Use C99 'isfinite' macro in preference to BSD-derived 'finite' function.

""",
u"""
Fix HAVE_DECL_ISINF/ISNAN test (again).

""",
u"""
Oops.  Need to check not only that HAVE_DECL_ISINF is defined, but also
that it's equal to 1.  (If isinf isn't defined, HAVE_DECL_ISINF is
defined to be 0, rather than being undefined.)

""",
u"""
isinf and isnan are macros, not functions; fix configure script
to use AC_CHECK_DECLS instead of AC_CHECK_FUNCS for these.
(See discussion in 

""",
u"""
Add autoconf test to detect x87-style double rounding, as described in
This information can be helpful for diagnosing platform-
specific problems in math and cmath.  The result of the test also
serves as a fairly reliable indicator of whether the x87 floating-point
instructions (as opposed to SSE2) are in use on Intel x86/x86_64 systems.

""",
u"""
using clearer syntax
""",
u"""
If user configures --without-gcc give preference to $CC instead of blindly
assuming the compiler will be "cc".

""",
u"""
Fix two issues found by the suspicious builder.

""",
u"""
Add "suspicious" builder which finds leftover markup in the HTML files.

Patch by Gabriel Genellina.

""",
u"""
Test commit.

""",
u"""
only check the actual compile() call for a SyntaxError
""",
u"""
fixed #1702551: distutils sdist was not pruning VCS directories under win32
""",
u"""
Add temporary code to fix the automatic doc build failure.

""",
u"""
Manually merge r67868 from 2.6 branch.

""",
u"""
Manually merge r68095,68186,68187,68188,68190 from 2.6 branch.

""",
u"""
Grammar fix.

""",
u"""
The _tkinter module functions "createfilehandler", "deletefilehandler",
"createtimerhandler", "mainloop", "dooneevent" and "quit" have been
deprecated for removal in 3.x (part of 

""",
u"""
Disable the line length checker by default.

""",
u"""
Remove tabs from the documentation.

""",
u"""
Remove trailing whitespace.

""",
u"""
Fix uses of the default role.

""",
u"""
Recognize usage of the default role.

""",
u"""
Add rstlint, a little tool to find subtle markup problems and inconsistencies in the Doc sources.

""",
u"""
Fix role name.

""",
u"""
Make indentation consistent.

""",
u"""
Set eol-style correctly for mp_distributing.py.

""",
u"""
Reapply r68191.
""",
u"""
Add from_float methods to the decimal module.
""",
u"""
Remove unused function PyOS_GetLastModificationTime.

""",
u"""
Merged revisions 67900-67901,67919,67928,67984,67991-67993,68106-68108,68110 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r67900 | benjamin.peterson | 2008-12-22 14:02:45 -0600 (Mon, 22 Dec 2008) | 4 lines
  
  fix_execfile: wrap the open(fn).read() call in compile(), so the filename is preserved
  
  also add unittests for the fixer
........
  r67901 | benjamin.peterson | 2008-12-22 14:09:55 -0600 (Mon, 22 Dec 2008) | 1 line
  
  remove unused import
........
  r67919 | benjamin.peterson | 2008-12-23 13:12:22 -0600 (Tue, 23 Dec 2008) | 1 line
  
  copy permission bits from the backup to the original
........
  r67928 | benjamin.peterson | 2008-12-26 20:49:30 -0600 (Fri, 26 Dec 2008) | 1 line
  
  don't be so idiot about multiple local imports in fix_import; still won't handle absolute and local imports on the same line
........
  r67984 | benjamin.peterson | 2008-12-28 09:55:16 -0600 (Sun, 28 Dec 2008) | 1 line
  
  don't need loop
........
  r67991 | benjamin.peterson | 2008-12-28 14:30:26 -0600 (Sun, 28 Dec 2008) | 1 line
  
  actually call finish_tree()
........
  r67992 | benjamin.peterson | 2008-12-28 14:34:47 -0600 (Sun, 28 Dec 2008) | 1 line
  
  remove useless test
........
  r67993 | benjamin.peterson | 2008-12-28 15:04:32 -0600 (Sun, 28 Dec 2008) | 1 line
  
  update pyk3's test grammar
........
  r68106 | benjamin.peterson | 2008-12-31 11:53:58 -0600 (Wed, 31 Dec 2008) | 1 line
  
  #2734 don't convert every instance of long (eg if it's an attribute)
........
  r68107 | benjamin.peterson | 2008-12-31 11:55:10 -0600 (Wed, 31 Dec 2008) | 1 line
  
  add another test
........
  r68108 | benjamin.peterson | 2008-12-31 12:00:12 -0600 (Wed, 31 Dec 2008) | 1 line
  
  don't change long even if it's the only argument name
........
  r68110 | benjamin.peterson | 2008-12-31 14:13:26 -0600 (Wed, 31 Dec 2008) | 1 line
  
  remove unused import
........

""",
u"""
Fix indentation.

""",
u"""
Remove useless string literal.

""",
u"""
further renaming of internal Decimal constants, for clarity.

""",
u"""
add missing underscore prefix to some internal-use-only
constants in the decimal module.  (Dec_0 becomes _Dec_0, etc.)


""",
u"""
Document how to use itertools for de-duping.
""",
u"""
Add various items
""",
u"""
fix compilation on non-Windows platforms
""",
u"""
Prevent conflict of UNICODE macros in cPickle.

""",
u"""
Use OutputDebugStringW in Py_FatalError.

""",
u"""
#4811: fix markup glitches (mostly remains of the conversion),
found by Gabriel Genellina.

""",
u"""
Minor documentation changes relating to NullHandler, the module used for handlers and references to ConfigParser.
""",
u"""
document PyMemberDef
""",
u"""
Fix for issues #841800 and #900506

""",
u"""
Fix for is incompatible with Cygwin, this patch
should fix that.

""",
u"""
Fix for 


""",
u"""
Fix for issue r1737832

""",
u"""
Fix for 

""",
u"""
Fix for 

""",
u"""
Fix for issue1594
""",
u"""
Fix for issue3559: No preferences menu in IDLE on OSX

1) Add a comment to the help file to that points to the 
   preferences menu.

2) An earlier checkin tried to detect Tk >= 8.10.14,
   but did this in the wrong way. The end result of this
   was that the IDLE->Preferences... menu got surpressed
   when using the system version of Tcl/Tk

""",
u"""
Fix for 
""",
u"""
Fix for issue4780

""",
u"""
Forgot to add a NEWS item in my previous checkin

""",
u"""
Fix for issue4472: "configure --enable-shared doesn't work on OSX"

""",
u"""
#4801 _collections module fails to build on cygwin.

_PyObject_GC_TRACK is the macro version of PyObject_GC_Track, 
and according to documentation it should not be used for extension modules.

""",
u"""
welcome to 2009, Python!

""",
u"""
fix highlighting
""",
u"""
IOError.filename was not set when _fileio.FileIO failed to open
file with `str' filename on Windows.
""",
u"""
fill in actual issue number in tests
""",
u"""
Reference cycles created through a dict, set or deque iterator did not get collected.


""",
u"""
#4767: Use correct submodules for all MIME classes.

""",
u"""
Handlers are in the `logging.handlers` module.

""",
u"""
#4776: add data_files and package_dir arguments.

""",
u"""
#4782: Fix markup error that hid load() and loads().

""",
u"""
#4784: ... on three counts ...

""",
u"""
Point to types module in new module deprecation notice.

""",
u"""
#4228: Pack negative values the same way as 2.4 
in struct's L format.


""",
u"""
#4222: document dis.findlabels() and dis.findlinestarts() and
put them into dis.__all__.

""",
u"""
#4185: clarify escape behavior of replacement strings.

""",
u"""
#4156: make clear that "protocol" is to be replaced with the protocol name.

""",
u"""
#4100: note that element children are not necessarily present on "start" events.

""",
u"""
simplfy code
""",
u"""
#4795 inspect.isgeneratorfunction() should return False instead of None
""",
u"""
Just inserted blank line.
""",
u"""
Fixed compile error on windows.
""",
u"""
fix name collision issues
""",
u"""
#4788 qualify some bare except clauses
""",
u"""
Fixed #4702: Throwing DistutilsPlatformError instead of IOError under win32 if MSVC is not found
""",
u"""
#4778: attributes can't be called.

""",
u"""
Minor documentation change relating to NullHandler.
""",
u"""
implicitly call PyType_Ready from PyObject_Hash
""",
u"""
fixed #4646 : distutils was choking on empty options arg in the setup function.
""",
u"""
fix French
""",
u"""
Fix os.times result on systems where HZ is incorrect.

""",
u"""
#4764 in io.open, set IOError.filename when trying to open a directory on POSIX platforms
""",
u"""
#4764 set IOError.filename when trying to open a directory on POSIX platforms
""",
u"""
Convert Tk object to string in tkColorChooser.

""",
u"""
Allow placing ScrolledText in a PanedWindow.

""",
u"""
#4763 PyErr_ExceptionMatches won't blow up with NULL arguments
""",
u"""
Update the fix for issue4064 to deal correctly with all three variants of
universal builds that are presented by the configure script.

""",
u"""
Issue4064: architecture string for universal builds on OSX
""",
u"""
modernize coding style of unittest.py, remove obsolete compatibility stuff.
Patch by Virgil Dupras.


""",
u"""
fix WORD_BIGEDIAN declaration in Universal builds; fixes #4060 and #4728
""",
u"""
wrong version number in doc changes committed in r67979
""",
u"""
Allow assertRaises() to be used as a context handler.


""",
u"""
#4731: clarify message about missing module prerequisites.

""",
u"""
Backport r67974: 

#4759: allow None as first argument of bytearray.translate(), for consistency with bytes.translate().

Also fix segfault for bytearray.translate(x, None) -- will backport this part to 3.0 and 2.6.


""",
u"""
Document Py_VaBuildValue.

""",
u"""
Sort UCS-2/UCS-4 name mangling list.

""",
u"""
Fix name mangling of PyUnicode_ClearFreeList.

""",
u"""
fix markup
""",
u"""
add two list comprehension tests to pybench.


""",
u"""
#4671: document that pydoc imports modules.

""",
u"""
Use :samp: role.

""",
u"""
#4695: fix backslashery.

""",
u"""
#4682: 'b' is actually unsigned char.

""",
u"""
#4754: improve winsound documentation.

""",
u"""
Follow-up to r67746 in order to restore backwards-compatibility for
those who (monkey-)patch TextWrapper.wordsep_re with a custom RE.

""",
u"""
#4748 lambda generators shouldn't return values
""",
u"""
Patch #4739 by David Laban: add symbols to pydoc help topics,
so that ``help('@')`` works as expected.

""",
u"""
#4752: actually use custom handler in example.

""",
u"""
zipfile.is_zipfile() now supports file-like objects.
Patch by Gabriel Genellina.


""",
u"""
Fix bogus unicode tests in pickletester.

""",
u"""
Add Misc/NEWS entry for r67934.

""",
u"""
Fix cPickle corrupts high-unicode strings.
Update outdated copy of PyUnicode_EncodeRawUnicodeEscape.
Add a test case.

""",
u"""
Remove unnecessary casts related to unicode_decode_call_errorhandler.
Make the _PyUnicode_Resize macro a static function.

These changes are needed to avoid breaking strict aliasing rules. 

""",
u"""
Use HIGHEST_PROTOCOL in pickle test.
(There is no behavior difference in 2.x because HIGHEST_PROTOCOL == 2)
""",
u"""
python version is included in file name now
""",
u"""
fixed #4400 : distutils .pypirc default generated file was broken.
""",
u"""
pretend exceptions don't exist a while longer
""",
u"""
#4736 BufferRWPair.closed shouldn't try to call another property as a function
""",
u"""
make global static
""",
u"""
use a global variable, so the compiler doesn't optimize the assignment out
""",
u"""
Markup fix.

""",
u"""
Fix missing "svn" command.

""",
u"""
As a result of a regression that snuck into 2.5.3 add a test case that
ensures that when you try to read from a file opened for writing an IOError
is raised.

""",
u"""
silence compiler warning
""",
u"""
add NEWS note
""",
u"""
fix #4720: the format to PyArg_ParseTupleAndKeywords can now start with '|'
""",
u"""
less attitude
""",
u"""
add py3k warnings to frame.f_exc_*
""",
u"""
compute DISTVERSION with patchlevel.py
""",
u"""
Add Tarek for work on distutils.

""",
u"""
Merged revisions 67809 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r67809 | benjamin.peterson | 2008-12-15 21:54:45 -0600 (Mon, 15 Dec 2008) | 1 line
  
  fix logic error
........

""",
u"""
there are way too many places which need to have the current version added
""",
u"""
update readme
""",
u"""
sphinx.web is long gone
""",
u"""
silence annoying DeprecationWarning
""",
u"""
add some recent releases to the list
""",
u"""
remove redundant sentence
""",
u"""
beef up docstring
""",
u"""
add headings
""",
u"""
copy sentence from docstring
""",
u"""
#4700: crtlicense.txt is displayed by the license() command and should be kept ascii-only.

Will port to 3.0

""",
u"""
Fix typo in Python equivalent for bit_length.

""",
u"""
Fix-up and clean-up docs for int.bit_length().

* Replace dramatic footnote with in-line comment about possible round-off errors in logarithms of large numbers.
* Add comments to the pure python code equivalent.
* replace floor() with int() in the mathematical equivalent so the type is correct (should be an int, not a float).
* add abs() to the mathematical equivalent so that it matches the previous line that it is supposed to be equivalent to.
* make one combined example with a negative input.


""",
u"""
_call_method -> _callmethod and _get_value to _getvalue
""",
u"""
fix typo
""",
u"""
bogus 'Make' in Makefile.pre.in; replace with '$MAKE'.
Thanks Ned Deily.

""",
u"""
gc.DEBUG_STATS reports invalid elapsed times.
Patch by Neil Schemenauer, very slightly modified.


""",
u"""
add bit_length method to int and long.
Thanks Fredrik Johansson and Victor Stinner for code,
Raymond Hettinger for review.

""",
u"""
Simplify and optimize bytecode for list comprehensions.


""",
u"""
Merged revisions 67427,67431,67433,67435,67630,67652,67656-67657,67674-67675,67678-67679,67705-67706,67716,67723,67765-67771,67774,67776,67778 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r67427 | benjamin.peterson | 2008-11-28 16:07:41 -0600 (Fri, 28 Nov 2008) | 1 line
  
  fix spelling in comment
........
  r67431 | benjamin.peterson | 2008-11-28 17:14:08 -0600 (Fri, 28 Nov 2008) | 1 line
  
  add a scripts directory; move things to it
........
  r67433 | benjamin.peterson | 2008-11-28 17:18:48 -0600 (Fri, 28 Nov 2008) | 1 line
  
  run svneol.py
........
  r67435 | benjamin.peterson | 2008-11-28 17:25:03 -0600 (Fri, 28 Nov 2008) | 1 line
  
  rename pre/post_order_mapping to pre/post_order_heads
........
  r67630 | alexandre.vassalotti | 2008-12-06 21:51:56 -0600 (Sat, 06 Dec 2008) | 2 lines
  
  Fix typo in the urllib2.HTTPDigestAuthHandler fixer.
........
  r67652 | armin.ronacher | 2008-12-07 15:39:43 -0600 (Sun, 07 Dec 2008) | 5 lines
  
  Added a fixer that cleans up a tuple argument to isinstance after the tokens
  in it were fixed.  This is mainly used to remove double occurrences of
  tokens as a leftover of the long -> int / unicode -> str conversion.
........
  r67656 | armin.ronacher | 2008-12-07 16:54:16 -0600 (Sun, 07 Dec 2008) | 3 lines
  
  Added missing copyright fo 2to3 fix_isinstance.
........
  r67657 | armin.ronacher | 2008-12-07 18:29:35 -0600 (Sun, 07 Dec 2008) | 3 lines
  
  2to3: intern and reduce fixes now add the imports if missing.  Because that is a common task the fixer_util module now has a function "touch_import" that adds imports if missing.
........
  r67674 | benjamin.peterson | 2008-12-08 19:58:11 -0600 (Mon, 08 Dec 2008) | 1 line
  
  copy permission bits when making backup files #4602
........
  r67675 | benjamin.peterson | 2008-12-08 19:59:11 -0600 (Mon, 08 Dec 2008) | 1 line
  
  add forgotten import
........
  r67678 | benjamin.peterson | 2008-12-08 20:08:30 -0600 (Mon, 08 Dec 2008) | 1 line
  
  fix #4602 for real
........
  r67679 | armin.ronacher | 2008-12-09 00:54:03 -0600 (Tue, 09 Dec 2008) | 3 lines
  
  Removed redudant code from the 2to3 long fixer.  This fixes #4590.
........
  r67705 | benjamin.peterson | 2008-12-11 13:04:08 -0600 (Thu, 11 Dec 2008) | 1 line
  
  put trailers after a range call after the list()
........
  r67706 | benjamin.peterson | 2008-12-11 13:17:57 -0600 (Thu, 11 Dec 2008) | 1 line
  
  add html related modules to the fix_imports mapping
........
  r67716 | benjamin.peterson | 2008-12-11 22:16:47 -0600 (Thu, 11 Dec 2008) | 1 line
  
  consolidate tests
........
  r67723 | benjamin.peterson | 2008-12-12 19:49:31 -0600 (Fri, 12 Dec 2008) | 1 line
  
  fix name
........
  r67765 | benjamin.peterson | 2008-12-14 14:05:05 -0600 (Sun, 14 Dec 2008) | 1 line
  
  run fix_isinstance after fix_long and fix_unicode
........
  r67766 | benjamin.peterson | 2008-12-14 14:13:05 -0600 (Sun, 14 Dec 2008) | 1 line
  
  use run_order instead of order
........
  r67767 | benjamin.peterson | 2008-12-14 14:28:12 -0600 (Sun, 14 Dec 2008) | 1 line
  
  don't retain parenthesis if there is only one item left
........
  r67768 | benjamin.peterson | 2008-12-14 14:32:30 -0600 (Sun, 14 Dec 2008) | 1 line
  
  use insert_child()
........
  r67769 | benjamin.peterson | 2008-12-14 14:59:10 -0600 (Sun, 14 Dec 2008) | 1 line
  
  parenthesize doesn't belong in pygram or FixerBase
........
  r67770 | alexandre.vassalotti | 2008-12-14 15:15:36 -0600 (Sun, 14 Dec 2008) | 2 lines
  
  Fix typo: html.paser -> html.parser.
........
  r67771 | benjamin.peterson | 2008-12-14 15:22:09 -0600 (Sun, 14 Dec 2008) | 1 line
  
  altering .children needs to call changed()
........
  r67774 | benjamin.peterson | 2008-12-14 15:55:38 -0600 (Sun, 14 Dec 2008) | 1 line
  
  employ an evil hack to fix multiple names in the same import statement
........
  r67776 | benjamin.peterson | 2008-12-14 16:22:38 -0600 (Sun, 14 Dec 2008) | 1 line
  
  make a common mixin class for Test_imports and friends
........
  r67778 | alexandre.vassalotti | 2008-12-14 17:48:20 -0600 (Sun, 14 Dec 2008) | 2 lines
  
  Make fix_imports refactor multiple imports as.
........

""",
u"""
#3632: the "pyo" macro from gdbinit can now run when the GIL is released.

Patch by haypo.

""",
u"""
#3954: Fix error handling code in _hotshot.logreader

Will port to 2.6. hotshot was deleted from python 3.

""",
u"""
Fix the remaining part of the doctest-in-zipfile problem by giving linecache access to the module globals when available
""",
u"""
#4568: remove limitation in varargs callback example.

""",
u"""
#4578: fix has_key() usage in compiler package.

""",
u"""
#4611: fix typo.

""",
u"""
#4446: document "platforms" argument for setup().

""",
u"""
modify other occurrence of test_bad_address
""",
u"""
try to fix failure in test_bad_address on some buildbots


""",
u"""
Backport r67759 (fix io.IncrementalNewlineDecoder for UTF-16 et al.).


""",
u"""
fix missing bracket
""",
u"""
Add file that was missed from r67750
""",
u"""
Fix several issues relating to access to source code inside zipfiles. Initial work by Alexander Belopolsky. See Misc/NEWS in this checkin for details.
""",
u"""
remove has_key usage
""",
u"""
Use unicode-friendly word splitting in the textwrap functions when given an unicode string.


""",
u"""
fix incorrect example
""",
u"""
TarFile.utime(): Restore directory times on Windows.

    """,
u"""
Issues #3167, #3682: tests for math.log and math.log10 were failing on
Solaris and OpenBSD.  Fix this by handling special values and domain
errors directly in mathmodule.c, passing only positive nonspecial floats
to the system log/log10.

""",
u"""

Fix max, min, max_mag and min_mag Decimal methods to
give correct results in the case where one argument is a quiet NaN
and the other is a finite number that requires rounding.
Thanks Mark Dickinson.

""",
u"""
#1030250: correctly pass the dry_run option to the mkpath() function.

""",
u"""
#4559: When a context manager's __exit__() method returns an object whose
conversion to bool raises an exception, 'with' loses that exception. 

Reviewed by Jeffrey Yasskin.
Already ported to 2.5, will port to 2.6 and 3.0

""",
u"""
Update Misc/NEWS for r67666.

""",
u"""
Add simple unittests for Request

""",
u"""
revert unrelated change to installer script
""",
u"""
specify how things are copied
""",
u"""
Fix several cases in EvalFrameEx where an exception could be
"raised" without setting x, err, or why to let the eval loop know.

""",
u"""
Consider micro version for name of CHM file.
""",
u"""
Add UUIDs for 2.6.1 and 2.6.2.
""",
u"""
#4457: rewrite __import__() documentation.

""",
u"""
Add link to the favicon to the docs.

""",
u"""
muffed the default case
""",
u"""
bugs in bytearray with exports (buffer protocol)
""",
u"""
- dbm build failures on systems with gdbm_compat lib.

""",
u"""
Follow-up to #4488: document PIPE and STDOUT properly.

""",
u"""
save 3 bytes (on average, on a typical machine) per
string allocation.

""",
u"""
Remove confusing sentence part.

""",
u"""
Followup to #4511: add link from decorator glossary entry to definition.

""",
u"""
Safety check in parsenumber (ast.c)

""",
u"""
be more specific, and parallel to the py3k branch

""",
u"""
bump version number

""",
u"""
Move __import__ to the bottom of the functions list.
It doesn't make sense for such a fundamental document to have
the most obscure function listed at the top.

""",
u"""
#3171: document that *slice are removed in 3k.

""",
u"""
#4478: document that copyfile() can raise Error.

""",
u"""
#4517: add "special method" glossary entry and clarify when __getattribute__ is bypassed.

""",
u"""
#4529: fix parser's validation for try-except-finally statements.

""",
u"""
#4544: add `dedent` to textwrap.__all__.

""",
u"""
#4441 followup: Add link to open() docs for Windows.

""",
u"""
#4458: recognize "-" as an argument, not a malformed option in gnu_getopt().

""",
u"""
Use markup.

""",
u"""
Add an index entry for "subclassing immutable types".

""",
u"""
#4441: improve doc for os.open() flags.

""",
u"""
#4409: fix asterisks looking like footnotes.

""",
u"""
#4408: document regex.groups.

""",
u"""
rename the new check_call_output to check_output.  its less ugly.

""",
u"""
Clarification to avoid confusing output with file descriptors.

""",
u"""
Took Nick Coghlan's advice about importing warnings globally in logging, to avoid the possibility of race conditions: "This could deadlock if a thread spawned as a side effect of importing a module happens to trigger a warning. warnings is pulled into sys.modules as part of the interpreter startup - having a global 'import warnings' shouldn't have any real effect on logging's import time."
""",
u"""
Adds a subprocess.check_call_output() function to return the output from a
process on success or raise an exception on error.

""",
u"""
Add another heapq example.

""",
u"""
Add reference to enumerate() to indices example.

""",
u"""
cgi.parse_header(): Fixed parsing of header parameters to
support unusual filenames (such as those containing semi-colons) in
Content-Disposition headers.

""",
u"""
Bumped up 2.6 to 2.7
""",
u"""
Added logging integration with warnings module using captureWarnings(). This change includes a NullHandler which does nothing; it will be of use to library developers who want to avoid the "No handlers could be found for logger XXX" message which can appear if the library user doesn't configure logging.
""",
u"""
Backport r67478
""",
u"""
Speed up Python (according to pybench and 2to3-on-itself) by 1-2% by caching
whether any thread has tracing turned on, which saves one load instruction in
the fast_next_opcode path in PyEval_EvalFrameEx().  See 


""",
u"""
again
Converted a C99 style comment to a C89 style comment (found by MAL).
""",
u"""
let people using SVN Sphinx still build the docs
""",
u"""
typo in comment
""",
u"""
fix pyspecific extensions that were broken by Sphinx's grand renaming
""",
u"""
w# requires Py_ssize_t
""",
u"""
Add crtassem.h constants to the msvcrt module.
""",
u"""
note the version that works
""",
u"""
Add icon to the uninstall entry in
"add-and-remove-programs".

""",
u"""
StringIO.close() stops you from using the buffer, too
""",
u"""
Fix a small typo in docstring

""",
u"""
Send HTTP headers and message body in a single send() call.

This change addresses part of 

Change endheaders() to take an optional message_body argument
that is sent along with the headers.  Change xmlrpclib and
httplib's other methods to use this new interface.

It is more efficient to make a single send() call, which should
get the entire client request into one packet (assuming it is
smaller than the MTU) and will avoid the long pause for delayed
ack following timeout.

Also:
- Add a comment about the buffer size for makefile().
- Extract _set_content_length() method and fix whitespace issues there.


""",
u"""
Reflow long lines.

""",
u"""
Move definition int sval into branch of ifdef where it is used.

Otherwise, you get a warning about an undefined variable.

""",
u"""
SVN format 9 is the same it seems
""",
u"""
Merged revisions 67384,67386-67387,67389-67390,67392,67399-67400,67403-67405,67426 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r67384 | benjamin.peterson | 2008-11-25 16:13:31 -0600 (Tue, 25 Nov 2008) | 4 lines
  
  don't duplicate calls to start_tree()
  
  RefactoringTool.pre_order values now holds a list of the fixers while pre_order_mapping holds the dict.
........
  r67386 | benjamin.peterson | 2008-11-25 16:44:52 -0600 (Tue, 25 Nov 2008) | 1 line
  
  #4423 fix_imports was still replacing usage of a module if attributes were being used
........
  r67387 | benjamin.peterson | 2008-11-25 16:47:54 -0600 (Tue, 25 Nov 2008) | 1 line
  
  fix broken test
........
  r67389 | benjamin.peterson | 2008-11-25 17:13:17 -0600 (Tue, 25 Nov 2008) | 1 line
  
  remove compatibility code; we only cater to 2.5+
........
  r67390 | benjamin.peterson | 2008-11-25 22:03:36 -0600 (Tue, 25 Nov 2008) | 1 line
  
  fix #3994; the usage of changed imports was fixed in nested cases
........
  r67392 | benjamin.peterson | 2008-11-26 11:11:40 -0600 (Wed, 26 Nov 2008) | 1 line
  
  simpilfy and comment fix_imports
........
  r67399 | benjamin.peterson | 2008-11-26 11:47:03 -0600 (Wed, 26 Nov 2008) | 1 line
  
  remove more compatibility code
........
  r67400 | benjamin.peterson | 2008-11-26 12:07:41 -0600 (Wed, 26 Nov 2008) | 1 line
  
  set svn:ignore
........
  r67403 | benjamin.peterson | 2008-11-26 13:11:11 -0600 (Wed, 26 Nov 2008) | 1 line
  
  wrap import
........
  r67404 | benjamin.peterson | 2008-11-26 13:29:49 -0600 (Wed, 26 Nov 2008) | 1 line
  
  build the fix_imports pattern in compile_pattern, so MAPPING can be changed and reflected in the pattern
........
  r67405 | benjamin.peterson | 2008-11-26 14:01:24 -0600 (Wed, 26 Nov 2008) | 1 line
  
  stop ugly messages about runtime errors being from printed
........
  r67426 | benjamin.peterson | 2008-11-28 16:01:40 -0600 (Fri, 28 Nov 2008) | 5 lines
  
  don't replace a module name if it is in the middle of a attribute lookup
  
  This fix also stops module names from being replaced if they are not in an attribute lookup.
........

""",
u"""
Retain copyright of processing examples. This was requested by a Debian maintainer during packaging of the multiprocessing package for 2.4/2.5
""",
u"""
issue4238: bsd support for cpu_count

""",
u"""
mp docs - fix issues 4012,3518,4193

""",
u"""
Fixed DISTUTILS_USE_SDK set causes msvc9compiler.py to raise an exception
""",
u"""
- Modules/Setup.dist: Update _elementtree, add _bisect, datetime

""",
u"""
- Modules/Setup.dist: Update pyexpat

""",
u"""
fix typo in sqlite3 docs
""",
u"""
- Modules/Setup.dist: Mention _elementtree and _pickle.

""",
u"""
Merged revisions 67183,67191,67371 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r67183 | benjamin.peterson | 2008-11-10 21:51:33 -0600 (Mon, 10 Nov 2008) | 1 line
  
  handle 'import x as y' in fix_imports; this still needs more work...
........
  r67191 | benjamin.peterson | 2008-11-11 17:24:51 -0600 (Tue, 11 Nov 2008) | 1 line
  
  super() is good
........
  r67371 | benjamin.peterson | 2008-11-24 16:02:00 -0600 (Mon, 24 Nov 2008) | 1 line
  
  don't blow up in the metaclass fixer when assignments in the class statement aren't simple
........

""",
u"""
always check the return value of NEW_IDENTIFIER

""",
u"""
Add unittests that verify documented behavior of public methods in Transport
class.

These methods can be overridden.  The tests verify that the overridden
methods are called, and that changes to the connection have a visible
effect on the request.


""",
u"""
#4404: make clear what "path" is.

""",
u"""
Fix typo.

""",
u"""
#4396 make the parser module correctly validate the with syntax
""",
u"""
replace reference to debugger-hooks

""",
u"""
Document PY_SSIZE_T_CLEAN for PyArg_ParseTuple.

""",
u"""
#4399: fix typo.

""",
u"""
#4392: fix parameter name.

""",
u"""
- Fix typo in last checkin

""",
u"""
 - Modules/Setup.dist: Mention _functools in section "Modules that should
   always be present (non UNIX dependent)"

""",
u"""
raise a better error
""",
u"""
#3996: On Windows, PyOS_CheckStack is supposed to protect the interpreter from
stack overflow. But doing this, it always crashes when the stack is nearly full.

Reviewed by Martin von Loewis. Will backport to 2.6.

""",
u"""
yuvconvert.c is a part of the "sv" module, an old IRIX thing
and certainly not useful for any Windows build.

""",
u"""
Fix error about "-*-" being mandatory in coding cookies.

""",
u"""
Fix typo.

""",
u"""
#4364: fix attribute name on ctypes object.

""",
u"""
backport r67325: make FileIO.mode always contain 'b'
""",
u"""
#4363: Let uuid.uuid1() and uuid.uuid4() run even if the ctypes module is not present.

Will backport to 2.6

""",
u"""
Fixed 
Changed semantic of _fileio.FileIO's close()  method on file objects with closefd=False. 
The file descriptor is still kept open but the file object behaves like a closed file. 
The FileIO  object also got a new readonly attribute closefd.

Approved by Barry

Backport of r67106 from the py3k branch

""",
u"""
backport r67300
""",
u"""
oops! didn't mean to disable that test
""",
u"""
fix indentation and a sphinx warning
""",
u"""
move useful sys.settrace information to the function's documentation from the debugger
""",
u"""
make sure that bytearray methods return a new bytearray even if there is no change

Fixes #4348
Reviewed by Brett

""",
u"""
Ignore .pyc and .pyo files.

""",
u"""
Fix for in trunk.

""",
u"""
Remove Cancel button from AdvancedDlg.
""",
u"""
Resolve member name conflict in ScrolledCanvas.__init__

""",
u"""
Try to fix problems with verbatim.

""",
u"""
patch from 
""",
u"""
#4317: Fix an Array Bounds Read in imageop.rgb2rgb8.

Will backport to 2.4.

""",
u"""
when __getattr__ is a descriptor, call it correctly; fixes #4230

patch from Ziga Seilnacht


""",
u"""
improve __hash__ docs
""",
u"""
a few fixes on the download page
""",
u"""
run autoconf
""",
u"""
#4316: fix configure.in markup problem.

""",
u"""
The docs for httplib.HTTPConnection.putheader() have claimed for quite a while
that their could be an arbitrary number of values passed in. Turns out the code
did not match that. The code now matches the docs.

""",
u"""
Clarify the docs for the 'strict' argument to httplib.HTTPConnection.
""",
u"""
#4324: fix getlocale() argument.

""",
u"""
use correct name
""",
u"""
Merged revisions 66985,67170,67173,67177-67179 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66985 | benjamin.peterson | 2008-10-20 16:43:46 -0500 (Mon, 20 Oct 2008) | 1 line
  
  no need to use nested try, except, finally
........
  r67170 | benjamin.peterson | 2008-11-08 12:28:31 -0600 (Sat, 08 Nov 2008) | 1 line
  
  fix #4271: fix_imports didn't recognize imports with parenthesis (ie from x import (a, b))
........
  r67173 | benjamin.peterson | 2008-11-08 17:42:08 -0600 (Sat, 08 Nov 2008) | 1 line
  
  consolidate test
........
  r67177 | benjamin.peterson | 2008-11-09 21:52:52 -0600 (Sun, 09 Nov 2008) | 1 line
  
  let the metclass fixer handle complex assignments in the class body gracefully
........
  r67178 | benjamin.peterson | 2008-11-10 15:26:43 -0600 (Mon, 10 Nov 2008) | 1 line
  
  the metaclass fixers shouldn't die when bases are not a simple name
........
  r67179 | benjamin.peterson | 2008-11-10 15:29:58 -0600 (Mon, 10 Nov 2008) | 1 line
  
  allow the fix_import pattern to catch from imports with parenthesis
........

""",
u"""
fix comment
""",
u"""
update link
""",
u"""
check for assignment to __debug__ during AST generation

Also, give assignment to None a better error message

""",
u"""
clarify what was added
""",
u"""
move context clue to versionchanged tag
""",
u"""
a few compile() and ast doc improvements
""",
u"""
Fix warning.

""",
u"""
Update "Documenting" a bit. Concentrate on Python-specifics.

""",
u"""
Don't use "HOWTO" as the title for all howto .tex files.

""",
u"""
ntpath.abspath returned an empty string for long unicode path.
""",
u"""
Register a drop handler for .py* files on Windows.
""",
u"""
Fix syntax.

""",
u"""
Stop including fake manifest file in DLLs directory.

""",
u"""
Fix grammar error; reword two paragraphs
""",
u"""
#4247: add "pass" examples to tutorial.

""",
u"""
Exclude manifest from extension modules in VS2008.

""",
u"""
#4245: move Thread section to the top.

""",
u"""
#4267: small fixes in sqlite3 docs.

""",
u"""
#4268: Use correct module for two toplevel functions.

""",
u"""
#4167: fix markup glitches.

""",
u"""
Fixed module build errors on FreeBSD 4.

""",
u"""
move a FileIO test to test_fileio
""",
u"""
clarify by splitting into multiple paragraphs
""",
u"""
Fixed an error when create a Tkinter menu item without command
and then remove it. Written by Guilherme Polo (gpolo).
""",
u"""
#4048 make the parser module accept relative imports as valid
""",
u"""
rephrase has_key doc
""",
u"""
make sure the parser flags and passed onto the compiler

This fixes "from __future__ import unicode_literals" in an exec statment
See #4225

""",
u"""
move unprefixed error into .c file
""",
u"""
finish backporting binary literals and new octal literals docs
""",
u"""
backport bin() documentation
""",
u"""
io.FileIO() was raising invalid warnings caused by insufficient initialization of PyFileIOObject struct members.
""",
u"""
Pickle would crash the interpreter when a __reduce__ function
does not return an iterator for the 4th and 5th items.
(sequence-like and mapping-like state)

A list is not an iterator...

Will backport to 2.6 and 2.5.

""",
u"""
Fixed a modulefinder crash on certain relative imports.

""",
u"""
Correct error message in io.open(): 
closefd=True is the only accepted value with a file name.

""",
u"""
mention the version gettempdir() was added
""",
u"""
Fix one of the tests: it relied on being present in an "output test" in
order to actually test what it was supposed to test, i.e. that the code
in the __del__ method did not crash.  Use instead the new helper
test_support.captured_output().

""",
u"""
add forgotten test for r67030
""",
u"""
fix __future__ imports when multiple features are given
""",
u"""
don't use a catch-all
""",
u"""
Typo fix.

""",
u"""
give a py3k warning when 'nonlocal' is used as a variable name
""",
u"""
only nonempty __slots__ don't work
""",
u"""
Use the correct names of the stateless codec functions (Fixes 

""",
u"""
Some tests didn't run with pickle.HIGHEST_PROTOCOL.
""",
u"""
fix #4150: pdb's up command didn't work for generators in post-mortem
""",
u"""
and another typo...
""",
u"""
fix a few typos
""",
u"""
add NEWs note for last change
""",
u"""
return ArgInfo from inspect.getargvalues #4092
""",
u"""
#4157 move two test functions out of platform.py.

Turn them into unit tests, and correct an obvious typo:
    (("a", "b") ("c", "d") ("e", "f"))
compiles even with the missing commas, but does not execute very well...

""",
u"""
make sure to call iteritems()
""",
u"""
- install versioned manpage

""",
u"""
Fixed #4062, added import for _ast.__version__ to ast to match the documented behavior.


""",
u"""
mention -n
""",
u"""
fix compiler warning
""",
u"""
Fixed #4067 by implementing _attributes and _fields for the AST root node.


""",
u"""
Fix duplicate word.

""",
u"""
clarify CALL_FUNCTION #4141
""",
u"""
Install pythonxy.dll in system32 again.
""",
u"""
fix more possible ref leaks in _json and use Py_CLEAR
""",
u"""
#4083: add "as" to except handler grammar as per PEP 3110.

""",
u"""
part of #4012: kill off old name "processing".

""",
u"""
fix possible ref leak
""",
u"""
#4131: FF3 doesn't write cookies.txt files.

""",
u"""
check for error conditions in _json #3623
""",
u"""
Add more TOC to the whatsnew index page.

""",
u"""
Fix wording (2.6.1 backport candidate)
""",
u"""
use new showwarnings signature for idle #3391
""",
u"""
document that deque indexing is O(n) #4123
""",
u"""
removed unused _PyUnicode_FromFileSystemEncodedObject.
made win32_chdir, win32_wchdir static.
""",
u"""
Merged revisions 66805,66841,66860,66884-66886,66893,66907,66910 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66805 | benjamin.peterson | 2008-10-04 20:11:02 -0500 (Sat, 04 Oct 2008) | 1 line
  
  mention what the fixes directory is for
........
  r66841 | benjamin.peterson | 2008-10-07 17:48:12 -0500 (Tue, 07 Oct 2008) | 1 line
  
  use assertFalse and assertTrue
........
  r66860 | benjamin.peterson | 2008-10-08 16:05:07 -0500 (Wed, 08 Oct 2008) | 1 line
  
  instead of abusing the pattern matcher, use start_tree to find a next binding
........
  r66884 | benjamin.peterson | 2008-10-13 15:50:30 -0500 (Mon, 13 Oct 2008) | 1 line
  
  don't print tokens to stdout when -v is given
........
  r66885 | benjamin.peterson | 2008-10-13 16:28:57 -0500 (Mon, 13 Oct 2008) | 1 line
  
  add the -x option to disable fixers
........
  r66886 | benjamin.peterson | 2008-10-13 16:33:53 -0500 (Mon, 13 Oct 2008) | 1 line
  
  cut down on some crud
........
  r66893 | benjamin.peterson | 2008-10-14 17:16:54 -0500 (Tue, 14 Oct 2008) | 1 line
  
  add an optional set literal fixer
........
  r66907 | benjamin.peterson | 2008-10-15 16:59:41 -0500 (Wed, 15 Oct 2008) | 1 line
  
  don't write backup files by default
........
  r66910 | benjamin.peterson | 2008-10-15 17:43:10 -0500 (Wed, 15 Oct 2008) | 1 line
  
  add the -n option; it stops backupfiles from being written
........

""",
u"""
add a much requested newline
""",
u"""
support the optional line argument for idle
""",
u"""
don't recurse into directories that start with '.'
""",
u"""
easter egg
""",
u"""
remove set compat cruft
""",
u"""
#4122: On Windows, Py_UNICODE_ISSPACE cannot be used in an extension module:
compilation fails with "undefined reference to _Py_ascii_whitespace"

Will backport to 2.6.

""",
u"""
document how to disable fixers
""",
u"""
Disable "for me" installations on Vista.

""",
u"""
give poplib a real test suite

#4088 from Giampaolo Rodola'x

""",
u"""
PyGILState_Acquire -> PyGILState_Ensure
""",
u"""
talk about how you can unzip with zip
""",
u"""
fix a small typo
""",
u"""
Typo: "ThreadError" is the name in the C source.

""",
u"""
- Makefile.pre.in(PROFILE_TASK): search files in srcdir

        """,
u"""
update paragraph about __future__ for 2.6
""",
u"""
r66862 contained memory leak.
""",
u"""
On windows, os.chdir given unicode was not working if GetCurrentDirectoryW
returned a path longer than MAX_PATH. (But It's doubtful this code path is
really executed because I cannot move to such directory on win2k)
""",
u"""
quiet sphinx warnings
""",
u"""
Make all whatsnew docs accessible.

""",
u"""
#3935: properly support list subclasses in the C impl. of bisect.
Patch reviewed by Raymond.

""",
u"""
#4058: fix some whatsnew markup.

""",
u"""
#4059: patch up some sqlite docs.

""",
u"""
Note how bytes alias is expected to be used
""",
u"""
#4069: aSet.remove(otherSet) would always report the empty frozenset([]) as the missing key.
Now it correctly refers to the initial otherset.

Reviewed by Raymond. Will backport to 2.6.

""",
u"""
more intensive test on dbm.
""",
u"""
save/restore stdout/stderr instead of relying on __*__ versions
""",
u"""
Pay attention to -R entries in LDFLAGS.

""",
u"""
Simplify individual tests by defining setUp and tearDown methods.

""",
u"""
Add the 'patchcheck' build target to .PHONY.

Re-closes Thanks to Ralph Corderoy for the catch.

""",
u"""
Don't claim that Python has an Alpha release status, in addition
to claiming it is Mature.

""",
u"""
Per Greg Ward, optparse is no longer being externally maintained.
I'll look at the bugs in the Optik bug tracker and copy them to the Python bug
tracker if they're still relevant.
""",
u"""
More strict test. Consider the case sys.executable itself is symlink.
""",
u"""
Added the test for issue3762.
""",
u"""
#1415508 from Rocky Bernstein: add docstrings for enable_interspersed_args(), disable_interspersed_args()
""",
u"""
fix typo
""",
u"""
Punctuation fix; expand dict.update docstring to be clearer
""",
u"""
Merged revisions 66707,66775,66782 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66707 | benjamin.peterson | 2008-09-30 18:27:10 -0500 (Tue, 30 Sep 2008) | 1 line
  
  fix #4001: fix_imports didn't check for __init__.py before converting to relative imports
........
  r66775 | collin.winter | 2008-10-03 12:08:26 -0500 (Fri, 03 Oct 2008) | 4 lines
  
  Add an alternative iterative pattern matching system that, while slower, correctly parses files that cause the faster recursive pattern matcher to fail with a recursion error. lib2to3 falls back to the iterative matcher if the recursive one fails.
  
  Fixes http://bugs.python.org/issue2532. Thanks to Nick Edds.
........
  r66782 | benjamin.peterson | 2008-10-03 17:51:36 -0500 (Fri, 03 Oct 2008) | 1 line
  
  add Victor Stinner's fixer for os.getcwdu -> os.getcwd #4023
........

""",
u"""
#4041: don't refer to removed and outdated modules.

""",
u"""
silence Sphinx warning
""",
u"""
Add What's New for 2.7
""",
u"""
Set svn:keywords
""",
u"""
two corrections
""",
u"""
Docstring change for *partition: use same tense as other docstrings.
Hyphenate left- and right-justified.
Fix 'registerd' typo
""",
u"""
Docstring changes: Specify exceptions raised
""",
u"""
Docstring change: Specify exception raised
""",
u"""
Use correct capitalization of NaN
""",
u"""
Fixed "'NoneType' object has no attribute 'rfind'" error when sqlite libfile not found.

""",
u"""
Typo fix
""",
u"""
Mention exception in docstring
""",
u"""
Fixed following error when DocXMLRPCServer failed.
  UnboundLocalError: local variable 'serv' referenced before assignment
""",
u"""
Follows to python's version change (VC6)
""",
u"""
Docstring typo.
""",
u"""
update the mac installer script
""",
u"""
Update version number to 2.7.
""",
u"""
Bump version to 2.7. Regenerate.

""",
u"""
Update the version to 2.7.  Hopefully this fixes the test_distutils failure
""",
u"""
update pydoc topics
""",
u"""
Add UUID for 2.7.

""",
u"""
Fixed a couple more C99 comments and one occurence of inline.
""",
u"""
Forward-port r66736.

""",
u"""
we're in 2.7 now
""",
u"""
Fixed a comment to C89 style as of http://drj11.wordpress.com/2008/10/02/python-and-bragging-about-c89/
""",
u"""
Use CRT 9 policy files.
""",
u"""
Bump to 2.7a0
""",
u"""
Today is the release date
""",
u"""
Bumping to 2.6 final.

""",
u"""
Bug #3989: Package the 2to3 script (as 2to3.py) in the Windows
installer.
""",
u"""
fix for test_array fails FreeBSD 7 amd64

FreeBSD 7's underlying malloc() is behaves differently to earlier versions
and seriously overcommits available memory on amd64.  This may affect
other 64bit platforms in some circumstances, so the scale of the 
problematic test is wound back.

Patch by Mark Dickinson, reviewed by Martin von Loewis.

""",
u"""
Works around issue3863: freebsd4/5/6 and os2emx are known to have OS bugs when
calling fork() from a child thread.  This disables that unit test (with a note
printed to stderr) on those platforms.

A caveat about buggy platforms is added to the os.fork documentation.

""",
u"""
Fix a refleak introduced by r66677.

Fix suggested by Amaury Forgeot d'Arc.
Closes 

""",
u"""
Markup fixes.  (optparse.rst probably needs an entire revision pass.)
""",
u"""
Markup fixes
""",
u"""
Markup fix
""",
u"""
Edits, and add markup
""",
u"""
Victor Stinner's patches to check the return result of PyLong_Ssize_t

reviewed by Amaury

""",
u"""
fix security imageop's poor validation of arguments could result in segfaults

patch by Victor Stinner
reviewed by myself and Brett

""",
u"""
issue3770: if SEM_OPEN is 0, disable the mp.synchronize module, rev. Nick Coghlan, Damien Miller

""",
u"""
Allow repeated calls to turtle.Screen, by making it a
true singleton object.

Reviewed by Gregor Lingl.

""",
u"""
Fix for MingW, update comments.
""",
u"""
fix for release blocker 3910, 2.6 regression in socket.ssl method
""",
u"""
Update nasm location.

""",
u"""
The _lsprof module could crash the interpreter if it was given an external
timer that did not return a float and a timer was still running when the
Profiler object was garbage collected.

Fixes 
Code review by Benjamin Peterson.

""",
u"""
bsddb4.7.3pre9 renamed to 4.7.3
""",
u"""
merge in the fix for test_ftplib on some bots [reviewed by Georg]
""",
u"""
Don't show version in title.

""",
u"""
No downloads for RCs.

""",
u"""
note the 2to3 -d could be useful for other refactoring
""",
u"""
better grammar
""",
u"""
#1415508: Document two functions
""",
u"""
#1579477: mention necessity to flush output before exec'ing
""",
u"""
clarify a few things
""",
u"""
#3510: future-proof text
""",
u"""
backport r66656 so people using -Qnew aren't affected
""",
u"""
enable refactor tests
""",
u"""
Merged revisions 66511,66548-66549,66644,66646-66652 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66511 | benjamin.peterson | 2008-09-18 21:49:27 -0500 (Thu, 18 Sep 2008) | 1 line
  
  remove a  useless if __name__ == '__main__'
........
  r66548 | benjamin.peterson | 2008-09-21 21:14:14 -0500 (Sun, 21 Sep 2008) | 1 line
  
  avoid the perils of mutable default arguments
........
  r66549 | benjamin.peterson | 2008-09-21 21:26:11 -0500 (Sun, 21 Sep 2008) | 1 line
  
  some places in RefactoringTool should raise an error instead of logging it
........
  r66644 | benjamin.peterson | 2008-09-27 10:45:10 -0500 (Sat, 27 Sep 2008) | 1 line
  
  fix doctest refactoring
........
  r66646 | benjamin.peterson | 2008-09-27 11:40:13 -0500 (Sat, 27 Sep 2008) | 1 line
  
  don't print to stdout when 2to3 is used as a library
........
  r66647 | benjamin.peterson | 2008-09-27 12:28:28 -0500 (Sat, 27 Sep 2008) | 1 line
  
  let fixer modules and classes have different prefixes
........
  r66648 | benjamin.peterson | 2008-09-27 14:02:13 -0500 (Sat, 27 Sep 2008) | 1 line
  
  raise errors when 2to3 is used as a library
........
  r66649 | benjamin.peterson | 2008-09-27 14:03:38 -0500 (Sat, 27 Sep 2008) | 1 line
  
  fix docstring
........
  r66650 | benjamin.peterson | 2008-09-27 14:22:21 -0500 (Sat, 27 Sep 2008) | 1 line
  
  make use of enumerate
........
  r66651 | benjamin.peterson | 2008-09-27 14:24:13 -0500 (Sat, 27 Sep 2008) | 1 line
  
  revert last revision; it breaks things
........
  r66652 | benjamin.peterson | 2008-09-27 16:03:06 -0500 (Sat, 27 Sep 2008) | 1 line
  
  add tests for lib2to3.refactor
........

""",
u"""
2to3's api should be considered unstable
""",
u"""
Add a last bunch of items
""",
u"""
give ftplib a real test suite

A asyncore based mock ftp server is used to test the protocol.
This is all thanks to Giampaolo Rodola #3939

(Barry gave me permission to do this before final on IRC.)

""",
u"""
#3967: Correct a crash in count() and find() methods of string-like objects.
For example:
   "".count("xxxx", sys.maxint, 0)

Reviewed by Benjamin Peterson.
Will port to 2.5 and 3.0.

""",
u"""
typos.

""",
u"""
add an 'other options' section
""",
u"""
add the beginnings of a C-API 2 -> 3 porting guide
""",
u"""
Fix namedtuple bug reported by Glenn Linderman.  Template did not form correctly if the field names were input in Unicode.
""",
u"""
#3965: on Windows, open() crashes if the filename or the mode is invalid,
and if the filename is a unicode string.

Reviewed by Martin von Loewis.

""",
u"""
add a NEWs entry for r66614
""",
u"""
Bug #3951: Py_USING_MEMORY_DEBUGGER should not be enabled by default.

""",
u"""
#3950 fix missing scale factors in turtle.py

reviewers: Georg, Benjamin

""",
u"""
Fix ctypes is confused by bitfields of varying integer types

Reviewed by Fredrik Lundh and Skip Montanaro.
""",
u"""
Improve wording
""",
u"""
Indentation normalization.

""",
u"""
backport the atexit test for r66563
""",
u"""
Bugfix for issue3885 and 'DB.verify()' crash.

Reviewed by Nick Coghlan.


""",
u"""
Fixed compile error on cygwin. (initializer element is not constant)
Reviewed by Amaury Forgeot d'Arc.
""",
u"""
mention how to override boolean evaluation
""",
u"""
clean up docs for platform's linux_distribution and dist functions
""",
u"""
use the new threading properties for multiprocessing (reviewed by Jesse #3927)
""",
u"""
build_os2emx.patch in - update OS/2 EMX makefile and config files

Part of source_os2emx.patch in 
  Include/pystrcmp.h:  OS/2 has same C APIs as Windows
  Lib/test/test_io.py: OS/2 has same behaviour as Windows for this test

Reviewed by Amaury Forgeot d'Arc

""",
u"""
any platform without HAVE_LOG1P should have DBL_EPSILON in <float.h>

Part of source_os2emx.patch in 
Reviewed by Amaury Forgeot d'Arc

""",
u"""
should use macro'ed symbols not direct

Part of source_os2emx.patch in 
Reviewed by Amaury Forgeot d'Arc

""",
u"""
Fill out download page.

""",
u"""
#3879 fix a regression in urllib.getproxies_environment

reviewers: Benjamin, Georg

""",
u"""
Ignores shutil.rmtree error on cygwin too.
Reviewed by Benjamin Peterson.
""",
u"""
TarFile object assigned to self.tar should be closed explicitly.
Reviewed by Lars Gustabel.
""",
u"""
Add "dist" target.

""",
u"""
#3918: note that uniform() args can be swapped.

""",
u"""
Update readme and Makefile (web builder doesn't exist).

""",
u"""
#3897: _collections now has an underscore.

""",
u"""
#3901: bsddb fix.

""",
u"""
#3914: add //= to the augmented assign operators.

""",
u"""
#3916: fixes for docs wrt. Windows directory layout

""",
u"""
#3912: document default for *places* arg.

""",
u"""
#3852: fix some select.kqueue and kevent docs.

""",
u"""
Use AMD64 version of CRT in just-for-me installations for Win64 installers.
""",
u"""
Bug #3887: Package x64 version of CRT for AMD64 
Windows binaries.
""",
u"""
Correct information about the tarfile module.

""",
u"""
Improve docs for super().
""",
u"""
Fix for documentation bug.  Fixes 

""",
u"""
tabify
""",
u"""
done with 2.6rc2
""",
u"""
Bumping to 2.6rc2
""",
u"""
avoid putting unicode objects in the environment causing 
later test failures.  As discussed on #python-dev

""",
u"""
On Windows, temporarily disable the bsddb test referenced in bug 3892.  
We do yell to stderr and the bug is marked as a blocker.
Reviewed by barry in #python-dev.

""",
u"""
fix possible integer overflows in _hashopenssl #3886
""",
u"""
document compileall command flags
""",
u"""
Note sqlite3 version; move item
""",
u"""
Remove comment about improvement: pystone is about the same, and
the improvements seem to be difficult to quantify
""",
u"""
Markup fixes
""",
u"""
usage

""",
u"""
#3888: add some deprecated modules in whatsnew.

""",
u"""
be less wordy

""",
u"""
Fix typo.

""",
u"""
Merged revisions 66470 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66470 | benjamin.peterson | 2008-09-15 18:29:43 -0500 (Mon, 15 Sep 2008) | 1 line
  
  don't use os.linesep for newlines; it breaks tests on windows
........

""",
u"""
Rewrite item a bit
""",
u"""
mention that object.__init__ no longer takes arbitrary args and kwargs
""",
u"""
Pick up a few more definitions from the glossary on the wiki.

""",
u"""
Review usage.  Fix a mistake in the new-style class definition.  Add a
couple new definitions (CPython and virtual machine).

""",
u"""
Fix grammar.

""",
u"""
Set eol-style to native.
""",
u"""
Include a licensing statement regarding the Microsoft C runtime in the Windows installer.
""",
u"""
clarify that radix for int is not 'guessed'
""",
u"""
fix a name issue; note all doc files should be encoded in utf8
""",
u"""
Misc/find_recursionlimit.py was broken.

Reviewed by A.M. Kuchling.


""",
u"""
Merged revisions 66191,66418,66438,66445 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66191 | benjamin.peterson | 2008-09-03 17:00:52 -0500 (Wed, 03 Sep 2008) | 1 line
  
  update the Grammar file after recent syntax changes
........
  r66418 | benjamin.peterson | 2008-09-12 18:49:48 -0500 (Fri, 12 Sep 2008) | 1 line
  
  a trival fix to get a few more print corner cases #2899
........
  r66438 | benjamin.peterson | 2008-09-12 21:32:30 -0500 (Fri, 12 Sep 2008) | 5 lines
  
  add Jack Diederich's fixer for metaclass syntax #2366
  
  my contribution to this was adding a few tests and fixing a few bugs
  I also reviewed it (Jack is a committer)
........
  r66445 | benjamin.peterson | 2008-09-13 10:50:00 -0500 (Sat, 13 Sep 2008) | 1 line
  
  add a few more tests concerning int literals and weird spacing
........

""",
u"""
Remove things specific to the old Macintosh, and spell "Mac OS X" consistently.

""",
u"""
remove duplicate target
""",
u"""
Incorporate some suggestions by Tait Stevens.

""",
u"""
Change product code of Win64 installer to allow simultaneous installation on Win32 and Win64; also change product name to be able to distinguish the two in ARP.
""",
u"""
Use a different upgrade code for Win64 installers.
""",
u"""
Use title case
""",
u"""
#3288: Document as_integer_ratio
""",
u"""
Remove extra 'the'; the following title includes it
""",
u"""
Use title case
""",
u"""
Update uses of string exceptions
""",
u"""
Fix SyntaxError
""",
u"""
Subclass exception
""",
u"""
Remove semicolon
""",
u"""
#687648 from Robert Schuppenies: use classic division.
""",
u"""
#687648 from Robert Schuppenies: use classic division.  From me: remove two stray semicolons
""",
u"""
#687648 from Robert Schuppenies: use classic division.  From me: don't use string exception; add __main__ section
""",
u"""
#687648 from Robert Schuppenies: use classic division.  From me: don't use string exception; flush stdout after printing
""",
u"""
#687648 from Robert Schuppenies: use classic division.  (RM Barry gave permission to update the demos.)
""",
u"""
post release updates
""",
u"""
Fix the release level
""",
u"""
Bumping to 2.6rc1
""",
u"""
Release GIL during calls to sqlite3_prepare. This improves concurrent access to the same database file from multiple threads/processes.

""",
u"""
Fixes In the sqlite3 module, made one more function static. All renaming public symbos now have the pysqlite prefix to avoid name clashes. This at least once created problems where the same symbol name appeared somewhere in Apache and the sqlite3 module was used from mod_python.

""",
u"""
sqlite3 module: Mark iterdump() method as "Non-standard" like all the other methods not found in DB-API.

""",
u"""
fix typo
""",
u"""
#3640: Correct a crash in cPickle on 64bit platforms, in the case of deeply nested lists or dicts.

Reviewed by Martin von Loewis.

""",
u"""
Final cleanup of warnings.catch_warnings and its usage in the test suite. Closes issue w.r.t. 2.6 (R: Brett Cannon)
""",
u"""
Suppress warning in obmalloc when size_t is 
larger than uint. Reverts r65975. Reviewed by Brett Cannon.

""",
u"""
update asdl_c.py from r66377
""",
u"""
#3743: PY_FORMAT_SIZE_T is designed for the OS "printf" functions, not for 
PyString_FromFormat which has an independent implementation, and uses "%zd".

This makes a difference on win64, where printf needs "%Id" to display
64bit values. For example, queue.__repr__ was incorrect.

Reviewed by Martin von Loewis.

""",
u"""
Read unidata_version from unicodedata module.
Delete old NormalizationTest.txt if it doesn't match
unidata_version.

""",
u"""
Update to test Unicode 5.1.

""",
u"""
- Fix sre "bytecode" validator for an end case.
  Reviewed by Amaury.

""",
u"""
The Unicode database was updated to 5.1.
Reviewed by Fredrik Lundh and Marc-Andre Lemburg.

""",
u"""
use the latest pygments version
""",
u"""
Fix #3634 invalid return value from _weakref.ref(Exception).__init__

Reviewers: Amaury, Antoine, Benjamin

""",
u"""
#3472: update Mac-bundled Python version info.

""",
u"""
Fix varname in docstring. #3822.

""",
u"""
Fixed spurious 'test.blah' file left behind by test_logging.
""",
u"""
#3777: long(4.2) returned an int, and broke backward compatibility.
the __long__ slot is allowed to return either int or long, but the behaviour of
float objects should not change between 2.5 and 2.6.

Reviewed by Benjamin Peterson

""",
u"""
warnings.catch_warnings() now returns a list or None instead of the custom
WarningsRecorder object. This makes the API simpler to use as no special object
must be learned.

Closes 
Review by Benjamin Peterson.

""",
u"""
LockTests in test_imp should be skipped when thread is not available.
Reviewed by Benjamin Peterson.
""",
u"""
Added test for 
Reviewed by Benjamin Peterson.
""",
u"""
incorporate fixes from SSL doc patch
""",
u"""
Add UUIDs for upcoming releases
""",
u"""
Added xrefs to each other.


""",
u"""
Set SecureCustomProperties so that installation will properly
use the TARGETDIR even for unprivileged users.

""",
u"""
Allow passing the MSI file name to merge.py.

""",
u"""

Fixing a dumb error in the deprecated parse_qsl()
function.  Tests added.

""",
u"""
reran autoconf

""",
u"""
bugfix to r66283 (see 

""",
u"""
Add a new howto about Python and the web, by Marek Kubica.

""",
u"""
reran autoconf for r66283's checkin

""",
u"""
- The configure script now tests for additional libraries
  that may be required when linking against readline.  This fixes issues
  with x86_64 builds on some platforms (at least a few Linux flavors as
  well as OpenBSD/amd64).

""",
u"""
undoing change that broke trunk.  Need to find a better solution to this.


""",
u"""
This fixes a small inconsistency between trunk and 3.0, closing bug 3764.


""",
u"""
fix missing module
""",
u"""
Backport relevant part of r66274 (in 


""",
u"""
#1317: describe the does_esmtp, ehlo_resp, esmtp_features, and helo_resp attributes
""",
u"""
#3796: A test class was not run in test_float.
Reviewed by Benjamin.

""",
u"""
#3669 from Robert Lehmann: simplify use of iterator in example
""",
u"""
docs are pretty good about new-style classes these days
""",
u"""
#1638033: add support for httponly on Cookie.Morsel

Reviewer: Benjamin

""",
u"""
#3040: include 'dest' argument in example; trim some trailing whitespace
""",
u"""
Various corrections
""",
u"""
actually tell the name of the flag to use
""",
u"""
Fix typo in multiprocessing doc, cancel_join_thread was missing _thread

""",
u"""
zipfile couldn't read some zip files larger than 2GB.

Reviewed by Amaury Forgeot d'Arc.


""",
u"""
GNU coding guidelines say that ``make check`` should verify the build. That
clashes with what Python's build target did. Rename the target to 'patchcheck'
to avoid the culture clash.

Closes 
Reviewed by Benjamin Peterson.

""",
u"""
#3601: test_unicode.test_raiseMemError fails in UCS4

Reviewed by Benjamin Peterson on IRC.



""",
u"""
Deprecate bsddb for removal in Python 3.0.

Closes 
Review by Nick Coghlan.

""",
u"""
#3671: Typo fix
""",
u"""
Make it more obvious that warnings.catch_warnings() and its arguments should be considered keyword-only.
""",
u"""
flesh out the documentation on using 2to3
""",
u"""
Added NEWS
""",
u"""
#3671: various corrections and markup fixes noted by Kent Johnson
""",
u"""
platform.architecture() fails if python is lanched via its symbolic link.
Reviewed by Amaury Forgeot d'Arc.
""",
u"""
Fixed regression problem in StreamHandler.emit().
""",
u"""
test_py3kwarn had been overlooked when test.test_support.catch_warning() was
re-implemented to use warnings.catch_warnings() and had its API improved.

Closes 
Code review by Benjamin Peterson.

""",
u"""

Relocated parse_qs() and parse_qsl(), from the cgi module
to the urlparse one.  Added a PendingDeprecationWarning in the old
module, it will be deprecated in the future.  Docs and tests updated.

""",
u"""
Python3.0 bsddb testsuite compatibility improvements
""",
u"""
3.0 still has the old threading names
""",
u"""
Fix - solaris compilation of multiprocessing fails, reviewed by pitrou

""",
u"""
Fix some leaks - Neal Norwitz
""",
u"""
Fix distutils PKG-INFO writing logic to allow having
non-ascii characters and Unicode in setup.py meta-data.


""",
u"""
Allowed spaces in separators in logging configuration files.
""",
u"""
Fix OpenBSD required -lcurses when linking with readline
to get the correct completion_matches function to avoid crashes on
x86_64 (amd64).

I don't have OpenBSD to test myself.  I tested that it does not break
anything on linux.  It is simple.

""",
u"""
Merged revisions 66176 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66176 | benjamin.peterson | 2008-09-02 21:04:06 -0500 (Tue, 02 Sep 2008) | 1 line
  
  fix typo
........

""",
u"""
update 2to3 script from 2to3 trunk
""",
u"""
Merged revisions 66173 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r66173 | benjamin.peterson | 2008-09-02 18:57:48 -0500 (Tue, 02 Sep 2008) | 8 lines
  
  A little 2to3 refactoring #3637
  
  This moves command line logic from refactor.py to a new file called
  main.py.  RefactoringTool now merely deals with the actual fixers and
  refactoring; options processing for example is abstracted out.
  
  This patch was reviewed by Gregory P. Smith.
........

""",
u"""
when compiling multiple extension modules with visual studio 2008
from the same python instance, some environment variables (LIB, INCLUDE) 
would grow without limit.

Tested with these statements:
    distutils.ccompiler.new_compiler().initialize()
    print os.environ['LIB']
But I don't know how to turn them into reliable unit tests.

""",
u"""
Attempt to correct the build files for the Microsoft VS7.1 compiler.

I don't have a working VS7.1, but VS2005 can automatically convert 
the project and build a working python interpreter.

""",
u"""
Use vs9to8.py to refresh the Visual Studio 2005 build files.

""",
u"""
test_asyncore.py leaked handle.
Reviewed by Amaury Forgeot d'Arc 
""",
u"""
Add e-mail address
""",
u"""
Clarify example; add imports
""",
u"""
Add news item for #3719.


""",
u"""
Add quotes around the file name to avoid issues with spaces.

Closes #3719.


""",
u"""
Fix caching in ABCMeta.__subclasscheck__ (R: Georg Brandl)
""",
u"""
a typo


""",
u"""
os.urandom no longer goes into an infinite loop when passed a
non-integer floating point number.

""",
u"""
Correctly pass LDFLAGS and LDLAST to the linker on shared
library targets in the Makefile.

""",
u"""
Improve compatibility with Python3.0 testsuite
""",
u"""
typo fix
""",
u"""
Move test.test_support.catch_warning() to the warnings module, rename it
catch_warnings(), and clean up the API.

While expanding the test suite, a bug was found where a warning about the
'line' argument to showwarning() was not letting functions with '*args' go
without a warning.

Closes 
Code review by Benjamin Peterson.

""",
u"""
Describe the __hash__ changes
""",
u"""
remove py3k warnings about the threading api; update docs

Reviewer: Benjamin Peterson

""",
u"""
In Python3.0, "test.test_support" is renamed to "test.support".
""",
u"""
str.rpartition would perform a left-partition when called with
a unicode argument.

will backport.

""",
u"""
Bug #3738: Documentation is now more accurate in describing handler close methods.
""",
u"""
Merged revisions 65887,65889,65967-65968,65981 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r65887 | benjamin.peterson | 2008-08-19 17:45:04 -0500 (Tue, 19 Aug 2008) | 1 line
  
  allow the raw_input fixer to handle calls after the raw_input (ie. raw_input().split())
........
  r65889 | benjamin.peterson | 2008-08-19 18:11:03 -0500 (Tue, 19 Aug 2008) | 1 line
  
  no need for 2.4 compatibility now
........
  r65967 | benjamin.peterson | 2008-08-21 18:43:37 -0500 (Thu, 21 Aug 2008) | 1 line
  
  allow a Call to have no arguments
........
  r65968 | benjamin.peterson | 2008-08-21 18:45:13 -0500 (Thu, 21 Aug 2008) | 1 line
  
  add a fixer for sys.exc_info etc by Jeff Balogh #2357
........
  r65981 | benjamin.peterson | 2008-08-22 15:41:30 -0500 (Fri, 22 Aug 2008) | 1 line
  
  add a fixer to add parenthese for list and gen comps #2367
........

""",
u"""
revert r66114 for Jesse
""",
u"""
Submit Nick's patch for reviewed by jnoller

""",
u"""
Added section about configuring logging in a library. Thanks to Thomas Heller for the idea.
""",
u"""
logging: fixed lack of use of encoding attribute specified on a stream.
""",
u"""
platform.architecture() printed vogus message on windows.
Reviewed by Marc-Andre Lemburg.
""",
u"""
logging: fixed lack of use of encoding attribute specified on a stream.
""",
u"""
Backported r53335 to supress deprecation warning.
Reviewed by Benjamin Peterson.

""",
u"""
Fix compilation when --without-threads is given #3683

Reviewer: Georg Brandl, Benjamin Peterson

""",
u"""
#3749: fix c'n'p errors.

""",
u"""
#3703 unhelpful _fileio.FileIO error message when trying to open a directory

Reviewer: Gregory P. Smith

""",
u"""
issue3715: docstring representation of hex escaped string needs to be double
escaped.

""",
u"""
Update patch/bug count
""",
u"""
Last batch of edits; remove the 'other changes' section
""",
u"""
Edit the library section, rearranging items to flow better and making lots of edits
""",
u"""
Update bsddb code to version 4.7.3pre2. This code should
be compatible with Python 3.0, also.

  http://www.jcea.es/programacion/pybsddb.htm#bsddb3-4.7.3


""",
u"""
document the ability to block inheritance of __hash__ in the language reference
""",
u"""
More edits
""",
u"""
More edits; markup fixes
""",
u"""
Fix markup.

""",
u"""
#3707: fix inf. recursion in pydoc topic search. Rev'd by Antoine.

""",
u"""
Edit four more sections
""",
u"""
Correction from Antoine Pitrou: BufferedWriter and Reader support seek()
""",
u"""
Tidy up some sentences
""",
u"""
Partial edits from revision and tidying pass
""",
u"""
super() actually returns a super object.

""",
u"""
#3569: eval() also accepts "exec"able code objects.

""",
u"""
#3716: fix typo.

""",
u"""
#3730: mention "server" attribute explicitly.

""",
u"""
A collection of crashers, all variants of the idea
of 

""",
u"""
#3668: When PyArg_ParseTuple correctly parses a s* format, but raises an
exception afterwards (for a subsequent parameter), the user code will
not call PyBuffer_Release() and memory will leak.

Reviewed by Amaury Forgeot d'Arc.


""",
u"""
#3711: .dll isn't a valid Python extension anymore.

""",
u"""
Add various items
""",
u"""
Add an item and a note
""",
u"""
Trim whitespace; add a few updates
""",
u"""
speed up isinstance() and issubclass() by 50-70%, so as to 
match Python 2.5 speed despite the __instancecheck__ / __subclasscheck__  
mechanism. In the process, fix a bug where isinstance() and issubclass(),  
when given a tuple of classes as second argument, were looking up  
__instancecheck__ / __subclasscheck__ on the tuple rather than on each  
type object.  

Reviewed by Benjamin Peterson and Raymond Hettinger.



""",
u"""
sort of backport 66038 by aliasing PyObject_Bytes to PyObject_Str
""",
u"""
Try to reduce the flakiness of this test
""",
u"""
Use bytes as return type from recv_bytes() methods.  Not sure why this only
affects some buildbots.

R=Brett
TESTED=./python -E -tt ./Lib/test/regrtest.py test_multiprocessing

""",
u"""
Fix problem reported by pychecker where AuthenticationError wasn't imported.
Add some test coverage to this code.  More tests should be added (TODO added).

R=Brett
TESTED=./python -E -tt ./Lib/test/regrtest.py test_multiprocessing

""",
u"""
Clarify that some attributes/methods are listed somewhat separately because they are not part of the threading API.
""",
u"""
#3662: Fix segfault introduced when fixing memory leaks.

TESTED=./python -E -tt ./Lib/test/regrtest.py test_fileio
R (approach from bug)=Amaury and Benjamin


""",
u"""
remove note about unimplemented feature
""",
u"""
#3654: fix duplicate test method name. Review by Benjamin P.

""",
u"""
generate py3k warnings on __getslice__, __delslice__, and __setslice__

Reviewer: Brett Cannon

""",
u"""
Use the actual blacklist of leaky tests
""",
u"""
Ignore a couple more tests that report leaks inconsistently.
""",
u"""
Fix:
 * crashes on memory allocation failure found with failmalloc
 * memory leaks found with valgrind
 * compiler warnings in opt mode which would lead to invalid memory reads
 * problem using wrong name in decimal module reported by pychecker

Update the valgrind suppressions file with new leaks that are small/one-time
leaks we don't care about (ie, they are too hard to fix).

TBR=barry
TESTED=./python -E -tt ./Lib/test/regrtest.py -uall (both debug and opt modes)
  in opt mode:
  valgrind -q --leak-check=yes --suppressions=Misc/valgrind-python.supp \
    ./python -E -tt ./Lib/test/regrtest.py -uall,-bsddb,-compiler \
                        -x test_logging test_ssl test_multiprocessing
  valgrind -q --leak-check=yes --suppressions=Misc/valgrind-python.supp \
    ./python -E -tt ./Lib/test/regrtest.py test_multiprocessing
  for i in `seq 1 4000` ; do
    LD_PRELOAD=~/local/lib/libfailmalloc.so FAILMALLOC_INTERVAL=$i \
        ./python -c pass
  done

At least some of these fixes should probably be backported to 2.5.


""",
u"""
fix warning
""",
u"""
#3643 add a few more checks to _testcapi to prevent segfaults

Author: Victor Stinner
Reviewer: Benjamin Peterson

""",
u"""
Small updates to types member docs, backport from r65994.

""",
u"""
Fix bug 3625: test issues on 64bit windows. r=pitrou

""",
u"""
d is the correct format string
""",
u"""
fix a few get_name() calls and turn then to .name 

Reviewer: Christian Heimes

""",
u"""
Fixed two format strings in the _collections module. For example
Modules/_collectionsmodule.c:674: warning: format '%i' expects type 'int', but argument 2 has type 'Py_ssize_t'
Reviewed by Benjamin Peterson
""",
u"""
Silenced a compiler warning in the sqlite module
Modules/_sqlite/row.c:187: warning: suggest parentheses around && within ||
Reviewed by Benjamin Peterson
""",
u"""
Silenced compiler warning
Objects/stringlib/find.h:97: warning: 'stringlib_contains_obj' defined but not used
Reviewed by Benjamin Peterson
""",
u"""
Changed type of numarenas from uint to size_t to silence a GCC warning on 64bit OSes. Reviewed by Benjamin Peterson.
""",
u"""
Fixed broken patch. Reviewed by	benjamin.peterson.

""",
u"""
Solaris allows fullwidth Unicode digits in isxdigit, so
rewrite float.fromhex to only allow ASCII hex digits on all platforms.
(Tests for this are already present, but the test_float failures
on Solaris hadn't been noticed before.)

Reviewed by Antoine Pitrou.

""",
u"""
Fix float.fromhex test to give additional information on failure.  This
change is aimed at diagnosing (test_float fails on Solaris).

Reviewed by Benjamin Peterson

""",
u"""
done with the release
""",
u"""
Bump to 2.6b3.

""",
u"""
Reverted r65900. See http://mail.python.org/pipermail/python-checkins/2008-August/073116.html
""",
u"""
News for the tp_flags change.

""",
u"""
News for the imageop fix.

""",
u"""
fix up the multiprocessing docs a little
""",
u"""
Added some missing basic types in ctypes.wintypes.
""",
u"""
fixed get_file_system in test_os.py ('path' is unicode on py3k and ansi on trunk)
""",
u"""
fix silly errors of mine
""",
u"""
newSymbolTable is not public API

""",
u"""
deprecate some useless, noop methods in symtable
""",
u"""
add a NEWS note for new args syntax
""",
u"""
follow-up of issue3473: update the compiler package to recognize the new syntax.

""",
u"""
check that the parser module can handle the new keyword syntax
""",
u"""
Merged revisions 65876 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r65876 | benjamin.peterson | 2008-08-19 15:54:52 -0500 (Tue, 19 Aug 2008) | 1 line
  
  apply a fix I think will help Windows
........

""",
u"""
[CVE-2007-4965] Integer overflow in imageop module.

""",
u"""
Hopeful fix for remove Py_TPFLAGS_HAVE_VERSION_TAG from
Py_TPFLAGS_DEFAULT when not building the core.

""",
u"""
allow keyword args to be passed in after *args #3473
""",
u"""
COM method code is windows specific
""",
u"""
fix a little typo
""",
u"""
Fix a regression introduced by rev. 63792: ctypes function pointers
that are COM methods must have a boolean True value.

""",
u"""
silence callable warning in hmac
""",
u"""
issue3352: clean up the multiprocessing API to remove many get_/set_ methods and convert them to properties. Update the docs and the examples included.

""",
u"""
get unparse to at least unparse its self
""",
u"""
Fix strange character in the docstring.

""",
u"""
Merged revisions 65853-65854 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r65853 | benjamin.peterson | 2008-08-19 11:09:09 -0500 (Tue, 19 Aug 2008) | 1 line
  
  apply a patch for #3131. this solves the problem for the moment, but we should do some refactoring to get display logic out of RefactoringTool
........
  r65854 | benjamin.peterson | 2008-08-19 11:37:38 -0500 (Tue, 19 Aug 2008) | 1 line
  
  another quick fix to get lib2to3 to work
........

""",
u"""
Fix grammar.

""",
u"""
update the threading docs to account for recent changes
""",
u"""
add py3k warnings for old threading APIs

they will still live in 3.0 but it can't hurt

""",
u"""
#2234 distutils failed with mingw binutils 2.18.50.20080109.
Be less strict when parsing these version numbers, 
they don't necessarily follow the python numbering scheme.

""",
u"""
fix old API names in test_ssl
""",
u"""
patch up multiprocessing until it's API can be changed too
""",
u"""
bring back the old API
""",
u"""
change a few uses of the threading APIs
""",
u"""
backport threading property changes
""",
u"""
change threading.getIdent to a property

This is new in 2.6 so now need to worry about backwards compatibility :)

""",
u"""
Backport of r63826.

Optimization of str.format() for cases with str, unicode, int, long,
and float arguments.  This gives about 30% speed improvement for the
simplest (but most common) cases.  This patch skips the __format__
dispatch, and also avoids creating an object to hold the format_spec.

Unfortunately there's a complication in 2.6 with int, long, and float
because they always expect str format_specs.  So in the unicode
version of this optimization, just check for unicode objects.  int,
float, long, and str can be added later, if needed.

""",
u"""
Fix typo
""",
u"""
document PyObject_HashNotImplemented
""",
u"""
Belated NEWS entry for r65642
""",
u"""
Restore Python 2.3 compatibility and remove "with" usage.


""",
u"""
add a test for reduce's move
""",
u"""
follup to #3473: don't duplicate the reduce code
""",
u"""
correct version
""",
u"""
Update __all__ for cookielib, csv, os, and urllib2 for objects imported into
the module but exposed as part of the API.

""",
u"""
Remove an unneeded import of abc.ABCMeta from 'inspect'.

""",
u"""
Remove two unneeded imports in 'io'.

""",
u"""
Remove imports of 'warnings' that are no longer needed in dummy_thread,
filecmp, and shelve.

""",
u"""
Fix a refleak in bytearray.split and bytearray.rsplit, detected by 
   regrtest.py -R:: test_bytes

""",
u"""
set svn:executable on a script
""",
u"""
#3580: fix a failure in test_os


""",
u"""
get the symtable module back in working order
- Fix broken functions
- Add (hopefully) extensive tests
- Modernize a little

""",
u"""
#3556: test_raiseMemError consumes an insane amount of memory


""",
u"""
backport r65723: strengthen test_os.test_closerange


""",
u"""
Backport r65661, r65760: Incremental decoder's decode
function now takes bytearray by using 's*' instead of 't#'.
""",
u"""
fix ZipFile.testzip() to work with very large embedded files


""",
u"""
I forgot to update NEWS.
""",
u"""
Fixed reference leak when occured os.rename()
fails unicode conversion on 2nd parameter. (windows only)
""",
u"""
Update distutils so that it triggers no warnings when run under -3.

""",
u"""

Supports a malformation in the URL received
in a redirect.

""",
u"""
uhh PySTEntry->ste_unoptimized has to be exposed too
""",
u"""
fix compile errors
""",
u"""
a few improvements
""",
u"""
expose PySTEntry.nested so the symtable module will work
""",
u"""
Make test_ossaudiodev work.


""",
u"""
PySTEntry's constructor is static; there's no point in a fancy API name
""",
u"""
Review symtable docs.

""",
u"""
include filename and line number in SyntaxError

""",
u"""
Silence DeprecationWarning raised by mimetools and rfc822 in cgi.

""",
u"""
Silence the DeprecationWarning raised in httplib when mimetools is imported.

""",
u"""
Silence the DeprecationWarning raised by importing mimetools in BaseHTTPServer.
This does have an unfortunate side-effect of silencing the warning for all
subsequent code that imports mimetools as well since the warning is only
executed upon the first import of mimetools.

""",
u"""
add some documentation for symtable
""",
u"""
#3424 rearrange the order of tests in imghdr to place more common types first
""",
u"""

fixed small issue when handling an URL with double slash
after a 302 response in the case of not going through a proxy.

""",
u"""
note how os.utime should be used for emulating touch
""",
u"""
fix markup
""",
u"""
Merged revisions 65397 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r65397 | collin.winter | 2008-08-01 22:39:06 -0500 (Fri, 01 Aug 2008) | 5 lines
  
  Patch #3480 by Nick Edds.
  
  Dramatically simplifies the fix_imports pattern, resulting in a reduction of the test_all_fixers runtime from 122+ secs to 59 secs (a good predictor of 2to3 performance).
........

""",
u"""
document that waitpid raises OSError

""",
u"""
#2676: email/message.py [Message.get_content_type]: Trivial regex hangs on pathological input


""",
u"""
#3558: Attribute reference binds more tightly than subscription and call.

""",
u"""
make BufferedReader and BufferedWriter thread-safe


""",
u"""
Disable the test until I have one that works.

""",
u"""
Fix memory leak: Always DECREF obj in PyBuffer_Release.

""",
u"""
Try to fix the test on 64-bit platforms.

""",
u"""
ctypes.string_at and ctypes.wstring_at must use the
pythonapi calling convention so that the GIL is held and error return
values are checked.

""",
u"""

Fixes a bug caused because of the evolution
of the RFC that describes the behaviour. Note that we now
have the same behaviour than the current browsers.

""",
u"""
Properly INCREF reference in Py_buffer.

""",
u"""
Make obj an owned reference in Py_buffer; this checkin
was missing from the patch for #3139.

""",
u"""
Added _multiprocessing module support. (VC6)
""",
u"""
Fix markup for various binary operation examples where the operands were bolded
and the operator was made literal, leading to non-valid reST. Changed to have
the entire expression just be a literal bit of text.

""",
u"""
Fixed test_distutils error (test_build_ext) on VC6.
""",
u"""
Silence the DeprecationWarning of rfc822 triggered by its importation in
mimetools.

This has an unfortunate side-effect of potentially not letting any warning
about rfc822's deprecation be seen by user-visible code if rfc822 is not
imported before mimetools. This is because modules are cached in sys.modules
and thus do not have their deprecation triggered more than once. But this
silencing would have happened by other code that silences the use of mimetools
or rfc822 anyway in the stdlib or user code, and thus seems justified to be
done here.

""",
u"""
VC6 related fix.

- PC/VC6/_bsddb.dsp:
    removed '/nodefaultlib:"msvcrt"' to fix linker error.

- PC/VC6/_msi.dsp, PC/VC6/pcbuild.dsw:
    added new module support.

- PC/VC6/_sqlite3.dsp:
    /D "MODULE_NAME=\"sqlite3\""
    caused extra leading space like
    #define MODULE_NAME " sqlite3"
    so uses
    /D MODULE_NAME=\"sqlite3\"
    instead.

- PC/VC6/python.dsp:
    changed stack size to 2MB to avoid stack overflow on
    some tests.
""",
u"""
Add Hirokazu Yamamoto.

""",
u"""
update ssl documentation
""",
u"""
remove duplicate close() from ssl.py; expose unwrap and add test for it
""",
u"""
Make buffer-interface thread-safe wrt. PyArg_ParseTuple,
by denying s# to parse objects that have a releasebuffer procedure,
and introducing s*.

More module might need to get converted to use s*.

""",
u"""
Another fix for 4-way universal builds, use the right #ifndef guard
to detect the OSX 10.5 SDK.

""",
u"""
Fix typo in the `arch` commandline

""",
u"""
Fix the connection refused error part of use errno module instead of a static list of possible connection refused messages.

""",
u"""
#3134: shutil referenced undefined WindowsError symbol


""",
u"""
Py3k warnings are now emitted for classes that will no longer inherit a__hash__ implementation from a parent class in Python 3.x. The standard library and test suite have been updated to not emit these warnings.
""",
u"""
Remove the fqdn call for 

""",
u"""
#3540: fix exception name.

""",
u"""
- Fix an assertion failure when an empty but presized dict
  object was stored in the freelist.

""",
u"""
Fix leak in Tkinter.Menu.delete. Commands associated to
menu entries were not deleted.


""",
u"""
Silence warnings in csv about using reduce() when run under -3 by using
functools.reduce() instead.

""",
u"""
Use functools.reduce() in difflib instead of __builtin__.reduce() to silence
warnings when running under -3.

""",
u"""
Copy reduce() to _functools so to have functools.reduce() not raise a warning
from usage under -3.

""",
u"""
Suppress the warning in asynchat from using buffer() when running udner -3.
Naively removing the usage causes a large number of test failures, so it was
just easier to suppress the warning.

""",
u"""
move NEWS entry to the appropriate section (oops!)


""",
u"""
#3205: bz2 iterator fails silently on MemoryError


""",
u"""
Add news item about _sre.compile() re-bytecode validator.

""",
u"""
Fix slightly misleading statement in the NEWS file.


""",
u"""
accept 
""",
u"""
Remove mention of backquotes in the tutorial.

""",
u"""
#3519: callee is an expression too.

""",
u"""
Remove buffer() usage in the socket module by just slicing directly on the
object. This removes all warnings for the module caused by running under -3.

""",
u"""
Remove warnings generated for the suprocess module when run under -3. Required
commenting out True/False compatbility stuff, remove a use of apply(), and
remove a use of buffer() (just pulled the solution used in 3.0 which is direct
slicing).

""",
u"""
Change the warning emitted for using the buffer() object; memoryview() in 3.0
is not an equivalent.

""",
u"""
Patch by Ian Charnas from 
Add F_FULLFSYNC if it exists (OS X only so far).

""",
u"""
#1288615: Python code.interact() and non-ASCII input


""",
u"""
Add some items
""",
u"""
Add imp.reload(). This to help with transitioning to 3.0 the reload() built-in
has been removed there.

""",
u"""
Remove duplicate import

""",
u"""
Docstring typo

""",
u"""
Fix longstringitem definition. #3505.

""",
u"""
Tracker sre "bytecode" verifier.

This is a verifier for the binary code used by the _sre module (this
is often called bytecode, though to distinguish it from Python bytecode
I put it in quotes).

I wrote this for Google App Engine, and am making the patch available as
open source under the Apache 2 license.  Below are the copyright
statement and license, for completeness.

# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

It's not necessary to include these copyrights and bytecode in the
source file.  Google has signed a contributor's agreement with the PSF
already.

""",
u"""
#3367: revert rev. 65539: this change causes test_parser to fail
""",
u"""
#3367 from Kristjan Valur Jonsson:
If a PyTokenizer_FromString() is called with an empty string, the 
tokenizer's line_start member never gets initialized.  Later, it is 
compared with the token pointer 'a' in parsetok.c:193 and that behavior 
can result in undefined behavior.

""",
u"""
Bug 3228: take a test from Niels Gustaebel's patch, and based on his patch, check for having os.stat available
""",
u"""
Add a note about all the modules/packages changed to silence -3 warnings. More
changes are needed once some decisions are made, but this is the work up to this
point.

""",
u"""
Remove use of callable() from pickle to silence warnings under -3.

""",
u"""
Remove tuple parameter unpacking in aifc to silence warnings under -3.

""",
u"""
Silence warnings under -3 triggered by wsgiref.

""",
u"""
(again!) Make conversion of a float NaN to an int or 
long raise ValueError instead of returning 0.  Also, change the error 
message for conversion of an infinity to an integer, replacing 'long' by 
'integer', so that it's appropriate for both long(float('inf')) and 
int(float('inf')).


""",
u"""
Remove a use of callable() from Tkinter to silence warnings under -3.

""",
u"""
Remove a dict.has_key() and list.sort(cmp=) usage from tarfile to silence
warnings under -3.

""",
u"""
Remove usage of apply() in sqlite3 to silence warnings under -3.

""",
u"""
Remove dict.has_key() usage in the shelve module to silence warnings under -3.

""",
u"""
Remove dict.has_key() usage in xml.sax to silence warnings under -3.

""",
u"""
Remove the use of callable() in re to silence warnings under -3.

""",
u"""
more cleanup ups of the recently added warnings in the subprocess docs.

""",
u"""
Add missing NEWS entry for r65487
""",
u"""
better documentation of the special method lookup process, especially for new-style classes. Also removes the warnings about not being authoritative for new-style classes - the language reference actually covers those fairly well now (albeit in a fashion that isn't always particularly easy to follow).
""",
u"""
Adds a sanity check to avoid a *very rare* infinite loop due to a corrupt tls
key list data structure in the thread startup path.

This change is a companion to r60148 which already successfully dealt with a
similar issue on thread shutdown.

In particular this loop has been observed happening from this call path:
 #0  in find_key ()
 #1  in PyThread_set_key_value ()
 #2  in _PyGILState_NoteThreadState ()
 #3  in PyThreadState_New ()
 #4  in t_bootstrap ()
 #5  in pthread_start_thread ()

I don't know how this happens but it does, *very* rarely.  On more than
one hardware platform.  I have not been able to reproduce it manually.
(A flaky mutex implementation on the system in question is one hypothesis).

As with r60148, the spinning we managed to observe in the wild was due to a
single list element pointing back upon itself.


""",
u"""
Clarify the meaning of the select() parameters and sync
names with docstring.

""",
u"""
Template is always "tmp".

""",
u"""
Fix markup.

""",
u"""
Bug 3228: Explicitly supply the file mode to avoid creating executable files,
and add corresponding tests.
Possible 2.5 backport candidate
""",
u"""
issue1606: Add warnings to the subprocess documentation about common pitfalls
of using pipes that cause deadlocks.

""",
u"""
Remove assignment to True/False and use of dict.has_key() to silence warnings
while running under -3.

""",
u"""
Silence warnings under -3 about using dict.has_key() for modulefinder.

""",
u"""
Remove dict.has_key() usage in xml.dom.minidom to silence warnings while
running under -3.

""",
u"""
- subprocess.Popen.poll gained an additional _deadstate keyword
  argument in python 2.5, this broke code that subclassed Popen to include its
  own poll method.  Fixed my moving _deadstate to an _internal_poll method.

""",
u"""
Remove dict.has_key() and apply() usage from the logging package to silence
warnings when run under -3.

""",
u"""
Remove a use of callable() in fileinput to silence a -3 warning.

""",
u"""
Move filecmp from using dict.has_key() to dict.__contains__() to silence
warnings triggered under -3.

""",
u"""
Remove a dict.has_key() usage in email._parseaddr found while running -3.

""",
u"""
Remove Barry's love of deprecated syntax to silence warnings in the email
package, when run under -3, about using <>.

""",
u"""
Remove a dict.has_key() use in DocXMLRPCServer that comes up under -3.

""",
u"""
Remove a dict.has_key() and callable() usage in SimpleXMLRPCServer as triggered
under -3 through test_xmlrpc.

""",
u"""
Silence -3 warnings in pstats: a dict.has_key() usage and backport solution to
move from list.sort(cmp=) to key=.

""",
u"""
Remove a dict.has_key() usage in profile to silence a -3 DeprecationWarning.

""",
u"""
Remove a use of list.sort(cmp=) to silence a -3 DeprecationWarning in
cookielib.

""",
u"""
Note the removal of several committers.

""",
u"""
#3495: use current version.

""",
u"""
Silence SyntaxWarning and DeprecationWarning in pydoc triggered by tuple
unpacking in parameter lists and using callable(). Found through -3.

""",
u"""
Silence some SyntaxWarnings for tuple unpacking in a parameter list for
urlparse when run under -3.

""",
u"""
Preemptively backport the relevant parts of r65420
""",
u"""
Fix TarFileCompat.writestr() which always raised an
AttributeError since __slots__ were added to zipfile.ZipInfo in
r46967 two years ago.
Add a warning about the removal of TarFileCompat in Python 3.0.

""",
u"""
Fix Tkinter.Misc._nametowidget to unwrap 
Tcl command objects.

""",
u"""
Remove a __getitem__() removal on an exception to silence a warning triggered
under -3.

""",
u"""
Remove a dict.has_key() use to silence a warning when running under -3.

""",
u"""
Remove a dict.has_key() use to silence a warning raised under -3.

""",
u"""
Remove a tuple unpacking in a parameter list to remove a SyntaxWarning raised
while running under -3.

""",
u"""
Remove a tuple unpacking in a parameter list to suppress the SyntaxWarning with
-3.

""",
u"""
fix compile error on Windows
""",
u"""
revert last revision; code was right
""",
u"""
fix indentation that caused logic bug
""",
u"""
This should really be a comment.

""",
u"""
Add the grammar to the reference manual, since the new docs don't
have the feature of putting all the small EBNF snippets together
into one big file.

""",
u"""
Submit fix for issue3393: Memory corruption in multiprocessing module
""",
u"""
Generate the PatternGrammar pickle during "make install".
Fixes part of #3131.

""",
u"""
Tone down math.fsum warning.

""",
u"""
Remove a use of callable() to silence the warning triggered under -3.

""",
u"""
Silence (Syntax|Deprecation)Warning for 'inspect'. Had to remove tuple
unpacking in a parameter list and set some constants by hand that were pulled
from the 'compiler' package.

""",
u"""
Remove use of tuple unpacking and dict.has_key() so as to silence
SyntaxWarning as triggered by -3.

""",
u"""
Remove assignment to True/False to silence the SyntaxWarning that is triggered
by -3.

""",
u"""
Fix a DeprecationWarning about __getitem__() and exceptions in the 'traceback' module.
""",
u"""
Correct a crash when two successive unicode allocations fail with a MemoryError:
the freelist contained half-initialized objects with freed pointers.

The comment 
/* XXX UNREF/NEWREF interface should be more symmetrical */
was copied from tupleobject.c, and appears in some other places.
I sign the petition.

""",
u"""
Remove a dummy test that was checked in by mistake

""",
u"""
#3479: unichr(2**32) used to return 0.
The argument was fetched in a long, but PyUnicode_FromOrdinal takes an int.

(why doesn't gcc issue a truncation warning in this case?)

""",
u"""
Security patches from Apple:  prevent int overflow when allocating memory
""",
u"""
remove usage of MacOS from Tkinter
""",
u"""
Rename testSum to testFsum and move it to proper place in test_math.py

""",
u"""
Backport test.support.fcmp() from 3.0 to silence -3 warnings.
""",
u"""
Alter recipe to show how to call izip_longest() with
both a keyword argument and star arguments.


""",
u"""
#2542: now that issubclass() may call arbitrary code,
make sure that PyErr_ExceptionMatches returns 0 when an exception occurs there.

""",
u"""
I mess up again; BufferError inherits StandardError
""",
u"""
Add note about problems with math.fsum on x86 hardware.

""",
u"""
add BufferError to the exception hieracrchy
""",
u"""
backport r64751
""",
u"""
Replace math.sum with math.fsum in a couple of comments
that were missed by r65308

""",
u"""
Rename math.sum to math.fsum

""",
u"""
getrandombits is actually getrandbits
""",
u"""
Fix special-value handling for math.sum.
Also minor cleanups to the code: fix tabbing, remove
trailing whitespace, and reformat to fit into 80
columns.

""",
u"""
Neaten-up the itertools recipes.
""",
u"""
the from __future__ import  with_statement isn't needed in 2.6
""",
u"""
More modifications to tests for math.sum:  replace the Python
version of msum by a version using a different algorithm, and
use the new float.fromhex method to specify test results exactly.

""",
u"""
Be less strict with replication timeouts (the machine
can be a bit loaded), and be sure to yield the CPU
when waiting.


""",
u"""
Refinements in the bsddb testsuite
""",
u"""
backport r65264
""",
u"""
Clarify wording
""",
u"""
clarify Popen argument
""",
u"""
Remove math.sum tests related to overflow, special values, and behaviour
near the extremes of the floating-point range.  (The behaviour of math.sum
should be regarded as undefined in these cases.)

""",
u"""
Update decimal module to use most recent specification
(v. 1.68) and tests (v. 2.58) from IBM.

""",
u"""
note robotparser bug fix.

""",
u"""
Close - missing state change when Allow lines are processed.
Adds test cases which use Allow: as well.

""",
u"""
Shorten some overlong lines.

""",
u"""
disable some failing tests in test_locale due to a bug in locale.py.
this should fix the failures on the solaris buildbot.


""",
u"""
Remove extra words
""",
u"""
This sentence continues to bug me; rewrite it for the second time
""",
u"""
Fix more buildbot failures on test_locale.


""",
u"""
try to fix most buildbot failures on test_locale + add a debug output for the solaris buildbot


""",
u"""
add a NEWS entry


""",
u"""
Raymond's patch for #1819: speedup function calls with named parameters
(35% faster according to pybench)


""",
u"""
add a pybench test for complex function calls (part of #1819)


""",
u"""
fix indentation
""",
u"""
convert test_locale to unittest, and add a mechanism to override localconv() results for further testing (#1864, #1222)


""",
u"""
#3394: zipfile.writestr doesn't set external attributes, so files are extracted mode 000 on Unix


""",
u"""
Better error reporting for operations on closed shelves.
""",
u"""
#2242: utf7 decoding crashes on bogus input on some Windows/MSVC versions


""",
u"""
document default value for fillvalue
""",
u"""
teach .bzrignore about doc tools
""",
u"""
Make ctypes compatible with Python 2.3, 2.4, and 2.5 again.
""",
u"""
Fix indentation.

""",
u"""
Convert from long to Py_ssize_t.
""",
u"""
Finish conversion from int to Py_ssize_t.
""",
u"""
add some documentation for 2to3
""",
u"""
fix markup
""",
u"""
fix spacing
""",
u"""
Parse to the correct datatype.
""",
u"""
Finish-up the partial conversion from int to Py_ssize_t for deque indices and length.
""",
u"""
Use correct indentation.

""",
u"""
Move opcode handling to Python's extension.

""",
u"""
3k-warn about parser's "ast" aliases.

""",
u"""
use isinstance
""",
u"""
bsddb module updated to version 4.7.2devel9.

This patch publishes the work done until now
for Python 3.0 compatibility. Still a lot
to be done.

When possible, we use 3.0 features in Python 2.6,
easing development and testing, and exposing internal
changes to a wider audience, for better test coverage.

Some mode details:
http://www.jcea.es/programacion/pybsddb.htm#bsddb3-4.7.2


""",
u"""
remove unneeded import
""",
u"""
One more attribution.
""",
u"""
Fix credits for math.sum()
""",
u"""
Tuples now have both count() and index().
""",
u"""
Remove out-of-date section on Exact/Inexact.
""",
u"""
Fix build issue on OSX 10.4, somehow this wasn't committed before.

""",
u"""
Fix buglet in fix for issue3381

""",
u"""
Overflow checking when allocating or reallocating memory
was not always being done properly in some python types and extension
modules.  PyMem_MALLOC, PyMem_REALLOC, PyMem_NEW and PyMem_RESIZE have
all been updated to perform better checks and places in the code that
would previously leak memory on the error path when such an allocation
failed have been fixed.

""",
u"""
don't use assert statement
""",
u"""
Issue2378: pdb would delete free variables when stepping into a class statement.

The problem was introduced by r53954, the correction is to restore the symmetry between
PyFrame_FastToLocals and PyFrame_LocalsToFast

""",
u"""
Increment version number in NEWS file, and move items that were added after 2.6b2.

(I thought there was a script to automate this kind of updates)

""",
u"""
On Windows, silence a Purify warning and initialize the memory passed to CryptGenRandom.
Since python doesn't provide any particular random data, it seems more reasonable anyway.

""",
u"""
nonlocal is not in 2.6.

""",
u"""

Fixed the autocompletion of 'int.', and worked
a little that part of the code, fixing a detail and enhancing
a bit others.

""",
u"""
Save the whole of sys.modules instead of using an import tracker.
This, when merged to py3k, will fix the spurious buildbot failure
in test_urllib2 ("<urlopen error unknown url type: do>").

""",
u"""
Fix misspeeld method name (negative)
""",
u"""
Fix a couple of names in error messages that were wrong
""",
u"""
#926501: add info where to put the docstring.

""",
u"""
Remove exception indexing in asyncore.

""",
u"""
fix issue3120 - don't truncate handles on 64-bit Windows.

This is still messy, realistically PC/_subprocess.c should never cast pointers
to python numbers and back at all.

I don't have a 64-bit windows build environment because microsoft apparently
thinks that should cost money.  Time to watch the buildbots.  It builds and
passes tests on 32-bit windows.

""",
u"""
Clean-up itertools docs and recipes.
""",
u"""
Fix compress() recipe in docs to use itertools.
""",
u"""
#3322: bounds checking for _json.scanstring
""",
u"""
Merged revisions 65137 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r65137 | georg.brandl | 2008-07-19 08:32:57 -0500 (Sat, 19 Jul 2008) | 2 lines
  
  #3334: correctly set prefix of imports.
........

""",
u"""
Add ordering info for findall and finditer.

""",
u"""
#3323: mention that if inheriting from a class without __slots__,
the subclass will have a __dict__ available too.

""",
u"""
#3319: don't raise ZeroDivisionError if number of rounds is so
low that benchtime is zero.

""",
u"""
#3303: fix crash with invalid Py_DECREF in strcoll().

""",
u"""
#3302: fix segfaults when passing None for arguments that can't
be NULL for the C functions.

""",
u"""
#3378: in case of no memory, don't leak even more memory. :)

""",
u"""
Add recipe to the itertools docs.
""",
u"""
Improve accuracy of gamma test function
""",
u"""
Fix default float format spec fails on negative numbers.
""",
u"""
Deprecate the sunaudio module for removal in Python 3.0. The sunau module can provide similar functionality.
""",
u"""
#3390: replace a remaining has_key().

""",
u"""
Replace all map(None, a) with list(a).

""",
u"""
now that test_lib2to3 actually works and isn't extremely slow, we don't need the lib2to3 resource

""",
u"""
backport test_fileio
""",
u"""
Document the different meaning of precision for {:f} and {:g}.
Also document how inf and nan are formatted. #3404.

""",
u"""
Correct attribute name.

""",
u"""
Remove duplicate entry in __all__.

""",
u"""
Allow resolving dotted names for handlers in logging configuration files. Thanks to Philip Jenvey for the patch.
""",
u"""
Allow resolving dotted names for handlers in logging configuration files. Thanks to Philip Jenvey for the patch.
""",
u"""
Allow resolving dotted names for handlers in logging configuration files. Thanks to Philip Jenvey for the patch.
""",
u"""
Allow resolving dotted names for handlers in logging configuration files. Thanks to Philip Jenvey for the patch.
""",
u"""
Last bit of a fix for issue3381 (addon for my patch in r65061)

""",
u"""
Post release cleanup
""",
u"""
Bumping to 2.6b2
""",
u"""
Fix update _debugInfo to be _debug_info


""",
u"""
Backed out r65069, pending fixing it in Windows.
""",
u"""
catch socket.error errors in badCertTest
""",
u"""
Make '%F' and float.__format__('F') convert results to upper case.
""",
u"""
#3381 fix framework builds on 10.4
""",
u"""
try to fix test_threading on the Windows bot
""",
u"""
news note for r63052

""",
u"""
Merged revisions 65053-65054 via svnmerge from 
svn+ssh://pythondev@svn.python.org/sandbox/trunk/2to3/lib2to3

........
  r65053 | benjamin.peterson | 2008-07-16 21:04:12 -0500 (Wed, 16 Jul 2008) | 1 line
  
  massive optimizations for 2to3 (especially fix_imports) from Nick Edds
........
  r65054 | benjamin.peterson | 2008-07-16 21:05:09 -0500 (Wed, 16 Jul 2008) | 1 line
  
  normalize whitespace
........

""",
u"""
#3388: add a paragraph about using "with" for file objects.

""",
u"""
Byte items *can* be chars in 2.6.

""",
u"""
Backport part of r65043.

""",
u"""
Use _getbytevalue() in init too.

""",
u"""
#3156: fix consistency in what type bytearray methods accept as items.
Also rename confusing "item" parameters to "index".

""",
u"""
#3312: fix two sqlite3 crashes.

""",
u"""
#3345: fix docstring.

""",
u"""
#3305: self->stream can be NULL.

""",
u"""
#1608818: errno can get set by every call to readdir().

""",
u"""
#3045: fix pydoc behavior for TEMP path with spaces.

""",
u"""
fix framework install on Mac 10.4
""",
u"""
Apply patch for 874900: threading module can deadlock after fork

""",
]
