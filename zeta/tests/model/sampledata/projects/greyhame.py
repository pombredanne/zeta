greyhame_description = \
u"""
nose collects tests automatically from python source files, directories and
packages found in its working directory (which defaults to the current working
directory). Any python source file, directory or package that matches the
testMatch regular expression (by default: (?:^|[b_.-])[Tt]est) will be
collected as a test (or source for collection of tests). In addition, all
other packages found in the working directory will be examined for python
source files or directories that match testMatch. Package discovery descends
all the way down the tree, so package.tests and package.sub.tests and
package.sub.sub2.tests will all be collected.

Within a test directory or package, any python source file matching testMatch
will be examined for test cases. Within a test module, functions and classes
whose names match testMatch and TestCase subclasses with any name will be
loaded and executed as tests. Tests may use the assert keyword or raise
AssertionErrors to indicate test failure. TestCase subclasses may do the same
or use the various TestCase methods available.
"""

greyhame_compdesc    = \
[
u"""
Oftentimes when testing you will want to select tests based on criteria rather
then simply by filename. For example, you might want to run all tests except
for the slow ones. You can do this with the Attribute selector plugin by
setting attributes on your test methods.
""",
u"""
This plugin captures stdout during test execution. If the test fails or raises
an error, the captured output will be appended to the error or failure output.
It is enabled by default but can be disabled with the options -s or
--nocapture.
""",
u"""
If you have Ned Batchelder's coverage module installed, you may activate a
coverage report with the --with-coverage switch or NOSE_WITH_COVERAGE
environment variable. The coverage report will cover any python source module
imported after the start of the test run, excluding modules that match
testMatch. If you want to include those modules too, use the --cover-tests
switch, or set the NOSE_COVER_TESTS environment variable to a true value. To
restrict the coverage report to modules from a particular package or packages,
use the --cover-packages switch or the NOSE_COVER_PACKAGES environment
variable.
""",
u"""
This plugin provides --pdb and --pdb-failures options. The --pdb option will
drop the test runner into pdb when it encounters an error. To drop into pdb on
failure, use --pdb-failures.
""",
u"""
Isolation works only during lazy loading. In normal use, this is only during
discovery of modules within a directory, where the process of importing,
loading tests and running tests from each module is encapsulated in a single
loadTestsFromName call. This plugin implements loadTestsFromNames to force the
same lazy-loading there, which allows isolation to work in directed mode as
well as discovery, at the cost of some efficiency: lazy-loading names forces
full context setup and teardown to run for each name, defeating the grouping
that is normally used to ensure that context setup and teardown are run the
fewest possible times for a given set of names.
""",
]

greyhame_mstndesc    = \
[
u"""
# Added multiprocess plugin that allows tests to be run in parallel across multiple processes.
# Added logcapture plugin that captures logging messages and prints them with failing tests. Thanks to Max Ischenko for the implementation.
# Added optional HTML coverage reports to coverage plugin. Thanks to Augie Fackler for the patch.
# Added plugin that enables collection of tests in all modules. Thanks to Peter Fein for the patch (#137).
# Added --failed option to testid plugin. When this option is in effect, if any tests failed in the previous test run (so long as testid was active for that test run) only the failed tests will run.
""",
u"""
# Added versioned nosetests scripts (#123).
# Fixed bug that would cause context teardown to fail to run in some cases. Thanks to John Shaw for the bug report and patch (#234).
# Enabled doctest plugin to use variable other than "_" as the default result variable. Thanks to Matt Good for the patch (#163).
# Fixed bug that would cause unicode output to crash output capture. Thanks to schickb for the bug report (#227).
# Added setUp and tearDown as valid names for module-level fixtures. Thanks to AgilityNerd for the patch (#211).
# Fixed bug in list of valid names for package-level fixtures. Thanks to Philip Jenvey for the patch (#237).
# Updated man page generation using hacked up manpage writer from docutils sandbox. Thanks grubert@users.sourceforge.net for the original module.
""",
u"""
# Fixed bug in nose.tools.with_setup that prevented use of multiple @with_setup decorators. Thanks to tlesher for the bug report (#151).
# Fixed bugs in handling of context fixtures for tests imported into a package. Thanks to Gary Bernhardt for the bug report (#145).
# Fixed bugs in handling of config files and config file options for plugins excluded by a RestrictedPluginManager. Thanks to John J Lee and Philip Jenvey for the bug reports and patches (#158, #166).
# Updated ErrorClass exception reporting to be shorter and more clear. Thanks to John J Lee for the patch (#142).
# Allowed plugins to load tests from modules starting with '_'. Thanks to John J Lee for the patch (#82).
# Updated documentation about building as rpm (#127).
# Updated config to make including executable files the default on IronPython as well as on Windows. Thanks to sanxiyn for the bug report and patch (#183).
""",
u"""
# Fixed a python 2.3 incompatibility in errorclass_failure.rst (#173). Thanks to Philip Jenvey for the bug report and patch.
# Fixed bug in adapting 0.9 plugins to 0.10 (#119 part one). Thanks to John J Lee for the bug report and tests.
# Fixed bug in handling of argv in config and plugin test utilities (#119 part two). Thanks to John J Lee for the bug report and patch.
# Fixed bug where Failure cases due to invalid test name specifications were passed to plugins makeTest (#120). Thanks to John J Lee for the bug report and patch.
# Fixed bugs in doc css that mangled display in small windows. Thanks to Ben Hoyt for the bug report and Michal Kwiatkowski for the fix.
# Made it possible to pass a list or comma-separated string as defaultTest to main(). Thanks to Allen Bierbaum for the suggestion and patch.
# Fixed a bug in nose.selector and nose.util.getpackage that caused directories with names that are not legal python identifiers to be collected as packages (#143). Thanks to John J Lee for the bug report.
""",
u"""
# Fixed bug that broke plugins with names containing underscores or hyphens. Thanks to John J Lee for the bug report and patch (Issue #81).
# Fixed typo in nose.__all__. Thanks to John J Lee for the bug report.
# Fixed handling of test descriptions that are multiline docstrings. Thanks to James Casbon for the patch (Issue #50).
# Improved documentation of doctest plugin to make it clear that entities may have doctests, or themselves be tests, but not both. Thanks to John J Lee for the bug report and patch (Issue #84).
# Made __file__ available in non-python-module doctests.
# Fixed bug that made it impossible for plugins to exclude package directories from test discovery (Issue #89). Thanks to John J Lee for the bug report and patch.
""",
]

greyhame_verdesc     = \
[
u"""
* Fixed bug in xunit plugin xml escaping. Thanks to Nat Williams for the bug report (#266).
* Fixed bug in xunit plugin that could cause test run to crash after certain types of errors or actions by other plugins.
* Fixed bug in testid plugin that could cause test run to crash after certain types of errors or actions by other plugins.
* Fixed bug in collect only plugin that caused it to fail when collecting from test generators.
* Fixed some broken html in docs.
""",
u"""
* Made it possible to 'yield test' in addition to 'yield test,' from test generators. Thanks to Chad Whitacre for the patch (#230).
* Fixed bug that caused traceback inspector to fail when source code file could not be found. Thanks to Philip Jenvey for the bug report and patch (#236).
* Fixed some issues limiting compatibility with IronPython. Thanks to Kevin Mitchell for the patch.
* Added support for module and test case fixtures in doctest files (#60).
* Added --traverse-namespace commandline option that restores old default behavior of following all package __path__ entries when loading tests from packages. Thanks to Philip Jenvey for the patch (#167).
* Added --first-package-wins commandline option to better support testing parts of namespace packages. Thanks to Jason Coombs for the bug report (#197).
""",
u"""
* nose is now compatible with python 2.6.
* Fixed bug in nosetests setup command that caused an exception to be raised if run with options. Thanks to Philip Jenvey for the bug report (#191).
* Raised score of coverage plugin to 200, so that it will execute before default-score plugins, and so be able to catch more import-time code. Thanks to Ned Batchelder for the bug report and patch (#190).
* nose now runs under jython (jython svn trunk only at this time). Thanks to Philip Jenvey, Pam Zerbinos and the other pycon sprinters (#160).
* Fixed bugs in loader, default plugin manager, and other modules that caused plugin exceptions to be swallowed (#152, #155). Thanks to John J Lee for the bug report and patch.
* Added selftest.py script, used to test a non-installed distribution of nose (#49). Thanks to Antoine Pitrou and John J Lee for the bug report and patches.
* Fixed bug in nose.importer that caused errors with namespace packages. Thanks to Philip Jenvey for the bug report and patch (#164).
""",
u"""
* Classes with metaclasses can now be collected as tests (#153).
* Made sure the document tree in the selector plugin test is accurate and tested (#144). Thanks to John J Lee for the bug report and patch.
* Fixed stack level used when dropping into pdb in a doctest (#154). Thanks to John J Lee for the bug report and patch.
* Fixed bug in ErrorClassPlugin that made some missing keyword argument errors obscure (#159). Thanks to Philip Jenvey for the bug report and patch.
* Fixed bug in capture plugin that caused it to record captured output on the test in the wrong attribute (#113).
* Fixed bug in result proxy that caused tests to fail if they accessed certain result attibutes directly (#114). Thanks to Neilen Marais for the bug report.
""",
u"""
* Fixed bug in capture plugin that caused other error formatters changes to be lost if no output was captured (#124). Thanks to someone at ilorentz.org for the bug report.
* Fixed several bugs in the nosetests setup command that made some options unusable and the command itself unusable when no options were set (#125, #126, #128). Thanks to Alain Poirier for the bug reports.
* Fixed bug in handling of string errors (#130). Thanks to schl... at uni-oldenburg.de for the bug report.
* Fixed bug in coverage plugin option handling that prevented --cover-package=mod1,mod2 from working (#117). Thanks to Allen Bierbaum for the patch.
* Fixed bug in profiler plugin that prevented output from being produced when output capture was enabled on python 2.5 (#129). Thanks to James Casbon for the patch.
""",
]

greyhame_comments    = \
[
u"""
Additional changelog bits
""",
u"""
Updated changelog for 0.11.1 bugfix release
""",
u"""
Bumped version
""",
u"""
: last commit forgot single & double quoting.  Also added a few more tests to catch both of these better.
""",
u"""
Fixed : Xunit plugin had its bracket escapes swapped.  oops!
""",
u"""
Fixed bug collect only vs generator tests
""",
u"""
Merged Kumar's fixes
""",
u"""
Whitespace
""",
u"""
A less likely case but fixes early failures and/or successes sent to Xunit where startTest may not be called.  Fixes AttributeError
""",
u"""
Bumped version
""",
u"""
Making testid plugin more defensive to early errors (before startTest()).  Fixes KeyError
""",
u"""
In the face of an early error (probably raises in setup()), the Xunit plugin sets test time to 0.  Fixes AttributeError bug
""",
u"""
Fixed broken html
""",
u"""
Corrected download link
""",
u"""
Fixed setup.cfg.release, was out of sync w/setup.cfg
""",
u"""
Added nose/usage.txt to manifest
""",
u"""
Added selftest.py to manifest
""",
u"""
release script/manifest improvements
""",
u"""
Disabled multiprocess for windows, noted in docs that it is not available on windows
""",
u"""
ignore build files
""",
u"""
Made import safe
""",
u"""
Added another debug log statement, may help tracking down 
""",
u"""
Revised mkrelease to build in clone
""",
u"""
Doc updates
""",
u"""
pypi info updated
""",
u"""
jython test fix
""",
u"""
Tweakin the docs
""",
u"""
Missed changes from merge, other tweaks
""",
u"""
Doc tweaks
""",
u"""
Merged Pam's documentation updates
""",
u"""
minor spag tweaks
""",
u"""
small tweaks for consistency
""",
u"""
fixed a lot of broken links, did some formatting consistency stuff
""",
u"""
fixing broken link by pulling in the nose.commands stuff
""",
u"""
typos and punctuation
""",
u"""
missed a colon
""",
u"""
i spilled some red ink on the plugin documentation.
""",
u"""
apparently i have an uncommitted merge
""",
u"""
Improved param formatting
""",
u"""
tweaks for clarity in some plugins
""",
u"""
clarity
""",
u"""
Stray whitespace
""",
u"""
Updated mkrelease to handle branching and tagging better.
""",
u"""
adding istest and nottest to __all__ so their docstrings get pulled for the docs
""",
u"""
grammatical tweaks to usage.txt
""",
u"""
Clarified plugin api change in 0.11, compatibility with 0.10 and 0.9
""",
u"""
Updated outdated docstrings
""",
u"""
Updated with hg urls, better explanations of what version is where
""",
u"""
Fixed #143
""",
u"""
Missed test update in transition
""",
u"""
Made it possible to pass main(), run(), etc a list or comma-separated text as defaultTest.
""",
u"""
Added autogeneration of readme
""",
u"""
Removed rst2wiki.py, which is not used.
""",
u"""
Copy generated manpage to right place
""",
u"""
Turned off deprecation warning for string exceptions in string exception test.
""",
u"""
Improved option help display, some whitespace cleanups
""",
u"""
Updated CHANGELOG
""",
u"""
Removed some debug prints
""",
u"""
Fixed #120: applied patch.
""",
u"""
Work in progress on automated man page generation
""",
u"""
Normalize paths so windows tests have a chance of passing.
""",
u"""
Added community, old version links
""",
u"""
Provisional fix for #121
""",
u"""
Added basic contributing page
""",
u"""
Fixed #119 part 2
""",
u"""
Clarified differences between module/test doctest fixtures
""",
u"""
Fixed #119 -- first part.
""",
u"""
Added project index redirector, updated mkrelease
""",
u"""
Fixed #129. Applied patch with small backwards-compatibility change.
""",
u"""
Converted svn tags
""",
u"""
Fixed #117: applied patch with small modification.
""",
u"""
Examples are no longer doctests which makes them more readable.  Also tightened up the prose while I was at it.
""",
u"""
Fixed #130
""",
u"""
Fixed for 2.3
""",
u"""
Updated CHANGELOG to include fixes for 125, 126 and 128
""",
u"""
Added section in plugin writing docs showing how to register a plugin without setuptools
""",
u"""
Fixed #128
""",
u"""
Fixing attrib plugin unit tests for 2.3 compatibility (removed decorators)
""",
u"""
Fixed #125
""",
u"""
Added an @attr decorator and better documentation for the Attribute plugin.
""",
u"""
Fixed #126
""",
u"""
Made sys.path adjustment more brutal to work around easy_install's viscious pth hacks
""",
u"""
Fixed #124
""",
u"""
Formatting fix
""",
u"""
Fixed #114. Updated CHANGELOG.
""",
u"""
Doc improvements
""",
u"""
Bumped version to 0.10.1
""",
u"""
Made test repeatable
""",
u"""
Fixed missing examples in release distribution.
""",
u"""
Restored loading tests from methods, for 2.6 compat
""",
u"""
Added coverage output file needed by doc builder. Added docs to Failure. Updated Failure to have usable address when possible so that testid can be used to retry. Added tests for that case.
""",
u"""
Fixed MANIFEST and noted a needed change in mkrelease after fixing 0.10.0 package.
""",
u"""
More, cleaner 2.6 compat in unit tests
""",
u"""
Added placeholder for documenting plugins page
""",
u"""
Fixed bad paths in mkrelease
""",
u"""
More 2.6 compat work
""",
u"""
Fixed bugs in testid, test suite
""",
u"""
Tweaked news and index template link.
""",
u"""
Further adventures in 2/3 compat
""",
u"""
Doc updates, some done some in progress
""",
u"""
Updated changelog, readme and news
""",
u"""
Working on 2.6 compatibility
""",
u"""
Updating, fixing symlink
""",
u"""
Regenerated docs
""",
u"""
Official supported for this release... in theory
""",
u"""
Added missing changelog entries for closed tickets
""",
u"""
Updated docs and doc generation to catch a few missing links.
""",
u"""
Added to make hg happy with empty dir
""",
u"""
add a csv report option to performance plugin
""",
u"""
Updated CHANGELOG and regenerated docs
""",
u"""
Renamed nosetests to nosetests3 to avoid clashes
""",
u"""
docstrings for all peformance plugin hooks
""",
u"""
Additional clarification of generators and fixtures
""",
u"""
A bit more script cleanup
""",
u"""
Removed nose.proxy import and proxy mocks from unit test mock library
""",
u"""
better option handling, PEP8 fixes, remove duplicated number of test reporting
""",
u"""
Fixed swapped docstrings
""",
u"""
Made testid plugin use a file in cwd instead of ~ by default.
""",
u"""
Fixed a few more test failures
""",
u"""
correct performance logger name
""",
u"""
A different way of getting a different sidebar on index
""",
u"""
Removed old docs
""",
u"""
Replaced globals mistakenly moved to main()
""",
u"""
Fixed a few more test failures, issues in assert inspector, testid plugin, result handling of test cases
""",
u"""
simple performance plugin that will rerun tests a given number of times and report min, avg, max times
""",
u"""
Some basic experiments with sphinxification
""",
u"""
Committed PyCon sprint work.
""",
u"""
Cleaned up mkwiki and mkdocs somewhat
""",
u"""
Revised method of attaching extra info (captured output, etc) to exceptions to enable exception chaining to continue to work
""",
u"""
create branch for ticket 20 - perfomance plugin
""",
u"""
Cut branch for work on sphinxed docs
""",
u"""
Work on making mkrelease less clunky.
""",
u"""
wantMethod() must take class, as class is no longer derivable from method. Plus other result-related fixes
""",
u"""
Fixed dependency loading in nosetests command
""",
u"""
Updated NEWS, docs, version in preparation for 0.10.0 final release.
""",
u"""
Removed dtcompat module, needed only by python 2.3
""",
u"""
Updated changelog
""",
u"""
Updated changelog and regenerated docs.
""",
u"""
Removed nose.proxy, put functionality into nose.result.
""",
u"""
Fixed (patch from pjenvey)
""",
u"""
Applied patch from #107, with small changes. Fixes #107.
""",
u"""
More work on fixing tests, cleaning up prints and such
""",
u"""
Fixed (patch from pjenvey)
""",
u"""
Fixed issue #109
""",
u"""
Fixed some doctests for 3.0
""",
u"""
Updated changelog
""",
u"""
Fixed issue #108
""",
u"""
Restored sorting of test cases
""",
u"""
Removed deprecated TestCollector class. Deprecated collector() function.
""",
u"""
A few more pylint tweaks.
""",
u"""
Fixed for 3.0
""",
u"""
Added to ignore
""",
u"""
A few more pylint fixes.
""",
u"""
A few more fixes. test_address(SomeClass.foo) is never going to work in 3.0, as SomeClass.foo is just a plain function with no reference to the class in which it is defined.
""",
u"""
Applied patch making namespace package path traversal optional
""",
u"""
Doc updates
""",
u"""
First batch of little fixes from pylint.
""",
u"""
ID plugin must open ids file in binary mode
""",
u"""
Made it possible to just "yield test" in test generators
""",
u"""
Updated multiprocess plugin docs
""",
u"""
Misc. small cleanups.
""",
u"""
Fixed float div
""",
u"""
Added tests for logcapture bugfix
""",
u"""
Fixed test errors
""",
u"""
Missed a new doc file.
""",
u"""
Some progress getting loader to work, some unit tests now passing
""",
u"""
Added some warnings about plugin interoperation
""",
u"""
Added to multiprocess plugin docs
""",
u"""
Rebuilt docs.
""",
u"""
First halting steps -- basically nothing works
""",
u"""
Started updating changelog
""",
u"""
Started on doctest describing how to use a doctest fixtures module
""",
u"""
Fixed some interlinking issues.
""",
u"""
Cut branch for py3k support
""",
u"""
Added basic support for using a fixtures module with a doctest file. This was required to allow multiprocess plugin doctest to gracefully degrade when processing module is not available.
""",
u"""
Moved nose.plugins.doctests.run to nose.plugins.plugintest. Updated tests. A few other tweaks and minor fixes.
""",
u"""
Removed coverage output dir
""",
u"""
Working on tests for multiprocess plugin: currently broken, need to be made conditional. Other tests also failing on 2.3/jython.
""",
u"""
Avoid deprecation warning under 2.5
""",
u"""
Small fixes
""",
u"""
Some files in wrong place
""",
u"""
nose.plugins.plugintest was excluded from doc generation.
""",
u"""
Removed jython class file
""",
u"""
Reorganized test support files
""",
u"""
Applied patch from issue #58.
""",
u"""
Applied patch from Augie Fackler implementing optional html coverage reports
""",
u"""
Added multiprocess functional test dir
""",
u"""
Added some debug logging and cleaned up some cruft.
""",
u"""
Note why mp test is skipped under 2.6 when mp is active
""",
u"""
Fixed some FIXMEs and removed some verbosity from debug log
""",
u"""
Clarified doc slightly.
""",
u"""
Fixed bug in logcapture plugin that set default filters to be [logging format]
""",
u"""
Added some module-level docs
""",
u"""
Made it easier to deal with tracebacks in plugin doctests (Issue #104) (patch applied).
""",
u"""
Fixed bug that caused SkipTests, etc, to be seen as errors on all but first batch processed by a runner in mp
""",
u"""
Preliminary work towards supporting shared context fixtures
""",
u"""
Updated changelog.
""",
u"""
Stopped mp test from running under 2.6 when mp is active. Fixed bug in unpacking of error class results in mp runner.
""",
u"""
Fixed bug in picking up env settings
""",
u"""
Updated profiler plugin to close profiler in finalize (may fix windows bug #103).
""",
u"""
Fixed bug in doctest fixture support that caused module fixtures to be called twice
""",
u"""
Added attempt at supporting --stop flag in mp runs
""",
u"""
2nd try at fixing one windows test failure.
""",
u"""
Tried to make mp test run under mp in 2.6. Failed, gave up.
""",
u"""
Fixed doctest plugin/tests so that testid works with doctests again, and tests reflect new test packaging
""",
u"""
Made loader unit test safer for windows (maybe).
""",
u"""
Applied patch from Augie Fackler to make import of processing lazy. Importing processing can cause stdin to freak out, at least on some platforms, so it should only be imported when needed.
""",
u"""
Added ability to set _multiprocess_can_split_ in a context to override default split behavior.
""",
u"""
changed import paths so that xml plugin tests all pass
""",
u"""
Fixed typo in changelog
""",
u"""
somehow this pyc file got checked in and every time I run nose it shows up as modified even though I have a global ignore set on all pyc files.  hmm.  Deleting it!
""",
u"""
Fixed issues with doctests of properties; made doctest suites non-splittable
""",
u"""
updated comments with missing instructions on getting selftest.py to work
""",
u"""
Updated changelog with latest bug fixes.
""",
u"""
applied patch from Augie Fackler -- syntax fix (missing parens) that was generating a SyntaxError warning in 2.6
""",
u"""
Fixed silly bugs in errorclass consolidation
""",
u"""
committing Paul Davis' work from http://python-nosexml.googlecode.com/svn/trunk up to revision 18 (nosexml 0.2)
""",
u"""
Fixed issue #101.
""",
u"""
added more accurate help text for --match and --include options
""",
u"""
Able to execute selftest, excluding twisted tests, but still in a primitive state
""",
u"""
creating work branch for : a builtin XML plugin
""",
u"""
Fixed issue #100.
""",
u"""
Progress, but still broken -- failures errors etc cause test run to wedge
""",
u"""
Fixed issues with python 2.6 compatiblity
""",
u"""
Fixed #97: accepted environment.patch to make env usage consistent.
""",
u"""
Minor tweaks/debug -- still broken and noisy
""",
u"""
Merged multiprocess plugin branch (
""",
u"""
Fixed issue #98: loader can now accept selector class or instance in selector argument.
""",
u"""
Basic but very broken (and noisy!) multiprocess implementation
""",
u"""
rewrote and expanded help strings for logcapture
""",
u"""
Fixed a typo, updated TODO and regenerated docs.
""",
u"""
Started work on multiprocess plugin
""",
u"""
removed forgotten print statement
""",
u"""
Changed wording
""",
u"""
Corrected typo.
""",
u"""
Added hasFixtures method to context suite
""",
u"""
Applied patch from with minor changes for jython compatibility
""",
u"""
Added plugin example for injecting custom selector.
""",
u"""
Cut work branch for (parallel testing)
""",
u"""
implemented --logging-filter option to filter logging statements by loggers
""",
u"""
Cut branch for 0.10.4 (2.6 compat) release
""",
u"""
Fixed #96 with help from http://bugs.python.org/issue644744.
""",
u"""
Merged ticket-148 branch: added logcapture plugin. Bumped version to 0.11
""",
u"""
Release branch for 0.10.3
""",
u"""
Fixed issue #95.
""",
u"""
Updated for new release
""",
u"""
Minor doc tweaks.
""",
u"""
Updated CHANGELOG
""",
u"""
Finished init plugin example.
""",
u"""
Bumped score of cover plugin to 200, so it will execute before plugins with default score
""",
u"""
Doc updates
""",
u"""
Made Config() env default to {}. Fixed config.testNames getting clobbered by empty command line (issue #92) and made some usability changes to nose.plugins.doctests.run.
""",
u"""
Removed some cruft
""",
u"""
Fixed failing tests, added docs
""",
u"""
Fixed out-of-date docstring in TestProgram.createTests (issue #94).
""",
u"""
Added regression tests for 
""",
u"""
Added some basic help text
""",
u"""
Started work on 2nd example plugin doctest.
""",
u"""
Fixed #191. Regression test for #191 is still in progress.
""",
u"""
Supporting bits for loop-on-fail
""",
u"""
Release branch for 0.10.2
""",
u"""
Fixed typo.
""",
u"""
Added first cut at loop-on-fail mode to testid
""",
u"""
Updated for release
""",
u"""
Fixed a few more problems with the unwanted_package test. Added that test to the generated documentation, and tweaked doc generation and highlighting styles.
""",
u"""
Make hg happy
""",
u"""
* Fix issue #184 (sys.argv[0] treated as option)
""",
u"""
Added special run() function to nose.plugins.doctests to make it easier to write doctests that test test runs. Removed use of +ELLIPSIS in unwanted_package test.
""",
u"""
Started work on collect-only plugin
""",
u"""
minor update to attrib plugin docs, mentioning how quoting may be necessary for some shells (i.e. nosetests -a '!slow')
""",
u"""
Added two ideas for plugin example doctests to TODO.
""",
u"""
Cut branch for work on collect-only plugin for 0.11
""",
u"""
fixing test_address() so that it is compatible with unittest.TestCase classes which define __metaclass__ -- see http://code.google.com/p/python-nose/issues/detail?id=153
""",
u"""
Fixed #89. Added first plugin example doctest to functional_tests/doc_tests.
""",
u"""
Added some missing changelog updates
""",
u"""
Made __file__ available in globals of non-python-module doctests to facilitate functional doctests that need filesystem resources.
""",
u"""
Updated CHANGELOG
""",
u"""
Fixed (IronPython compatibility)
""",
u"""
Applied doc patch from #84 to improve documentation of doctest plugin.
""",
u"""
Fixed #127 (doc fix)
""",
u"""
Applied patch for issue #50 and extended it to work around unittest.TestCase bugs.
""",
u"""
Fixed another case where imported test gets wrong ancestors: selection of TestClass.test_method on commandline was not transplanting parent class.
""",
u"""
Fixed missing exec bit on non-setuptools nosetests script.
""",
u"""
Add missing trailing newline to the standard test run report (it was removed accidentally in r479)
""",
u"""
Fixed typo in nose.__all__.
""",
u"""
Applied patch from
""",
u"""
Removed done items from TODO
""",
u"""
Applied updated patch from
""",
u"""
Cleaned up implementation a bit
""",
u"""
Added John J Lee to AUTHORS (ref: patch in issue #81).
""",
u"""
Remove extraneous plugins argument from a ConfiguredDefaultsOptionParser method
""",
u"""
Implemented function and class transplanting. Some cleanup left to do.
""",
u"""
Applied patch from #81 to allow plugins with underscores or hypens in name.
""",
u"""
Merged 158-166-config-files. Fixes #158 and #166.
""",
u"""
Added failing functional tests for imported test fixtures and naming.
""",
u"""
Changed nose.suite to use nose.util.isclass instead of inspect.isclass when introspecting contexts.
""",
u"""
Merged 145-imported-test-fixtures.
""",
u"""
Cut branch for work on
""",
u"""
Fixed more upload bugs
""",
u"""
Updated changelog with info on #151 fix
""",
u"""
Fixed uploading bugs in release script.
""",
u"""
Made new run() behavior optional, with deprecation warning. Changed config file parser interface to allow warning on excluded plugin options with a looser binding, rather than referencing plugins directly. Updated tests to use run_buffered where needed.
""",
u"""
Updated NEWS and CHANGELOG and fixed a few more documentation goofs.
""",
u"""
Fixed incorrect test for $JYTHON
""",
u"""
Updated option parsing and restricted plugin manager to issue warnings when excluded plugin options are set in config files.
""",
u"""
Started sketching token/tokenstream
""",
u"""
Forgot to check in improved documentation
""",
u"""
Merged 160-jython. Add test.sh shell script to run selftest under python2.3-2.5 and jython. Updated ls_tree and svn:ignore to ignore $py.class files.
""",
u"""
Added remaining reporter methods. Changed progress* names to report*. Still a few failing tests due to plugin api changes.
""",
u"""
Improved documentation.
""",
u"""
Branching to '158-166-config-files'
""",
u"""
Added unittest_reporter plugin, continued sketching new output system
""",
u"""
Updated html example plugin to 0.10 api
""",
u"""
Added changelog entry about jython compatibility.
""",
u"""
Added placeholders for reporter classes
""",
u"""
Fixed made it possible to call finalize() on plugins under all runs, made finalize() in capture plugin clean up stdout.
""",
u"""
Fixed from 2.3 incompatibilties in ls_tree
""",
u"""
Really set svn:ignore
""",
u"""
Added test for (SkipTest used with python setup.py test). Fixed python 2.5 compat problem in some config tests.
""",
u"""
Applied ls_tree patch from
""",
u"""
trying to get svn to ignore .pyc files
""",
u"""
Fixed module links and doctest blocks in wiki generation.
""",
u"""
Moved plugin output test dir to a dir that will be discovered
""",
u"""
Cleaned up links from writing plugins guide to plugins in generated docs.
""",
u"""
Fixed #173  Fix a 2.3 incompatibility.
""",
u"""
Made node.result into package
""",
u"""
Added better comments to testid plugin.
""",
u"""
Add the tests for issue #155 I intended to commit with r456
""",
u"""
Added preliminary api sketch/doctest
""",
u"""
Added highlighted source to builtin plugin doc files
""",
u"""
Fixed #155
""",
u"""
Cut branch for work on reporting sprint at pycon (3/16 4pm-7pm in open space)
""",
u"""
Re-fixed profile/plugin tests for jython
""",
u"""
Added basic plugin use and 0.9 plugin compat info to usage.
""",
u"""
Fixed #159.  Correct bad ErrorClass exception detail
""",
u"""
Possibly fixed twisted error under jython
""",
u"""
Reworked fix for issue #72 to avoid changes to the plugin interfaces for formatError and formatFailure.
""",
u"""
Fixed #154.  Use correct stack frame in doctest pdb support monkeypatch
""",
u"""
Possibly fixed hotshot import error under jython
""",
u"""
Fixed issue #72. Bumped version to 0.10.0b1.
""",
u"""
Add the tests for #142 I intended to commit with r439
""",
u"""
Applied patch from issue #160
""",
u"""
Made minor cosmetic changes. Added --logging-clear-handlers option to logcapture plugin. Added a bit more documentation to logcapture module. Changed plugin to disable itself if a logging config file is in use.
""",
u"""
fixing my embarrassing mistake of overwriting the name variable.  And renaming TC_Custom to TestMetaclassed.  makes more sense
""",
u"""
Fixed #71. Updated CHANGELOG with recent fixes.
""",
u"""
Fixed #142.  For ignored (false .isfailure) errorclass errors, like SkipTest,
""",
u"""
Cut branch to work on jython compatibility
""",
u"""
minor code changes and cleanup
""",
u"""
patched isclass() so that it detected classes with custom types (__metaclass__).  Added several tests for this in various places.  However, there is still something wrong and I can't reproduce it in a test yet.  I can reproduce it with a short test module.  I will try that next.  This is a start
""",
u"""
Fixed issue #65
""",
u"""
merged Ticket-153 branch into trunk, -r433:HEAD .  This fixes bugs in metaclass support when nose is discovering tests.
""",
u"""
changed default logformat
""",
u"""
"creating branch Ticket-153"
""",
u"""
Fixed issue #68
""",
u"""
implemented --logging-format option
""",
u"""
Clarify comment
""",
u"""
Removed stray debug print from nose.commands
""",
u"""
first working version (still rough)
""",
u"""
Handle attribute errors raised by doctest when a module sets __test__ to something other than a dict.
""",
u"""
Updated changelog
""",
u"""
typo fixed
""",
u"""
Forgot to add new file
""",
u"""
For function and method test cases, if the test function or method has the attribute description, use that as the test description. Most useful for generators: set the description attribute on the yielded function.
""",
u"""
spelling typo fixed
""",
u"""
Updated changelog
""",
u"""
whoops, forgot the alias to self.suiteClass
""",
u"""
initial version from rev 418
""",
u"""
Fixed #152: applied patch
""",
u"""
created functional tests out of the proof of concept suites for lazy importing
""",
u"""
Regenerated docs
""",
u"""
Bumped version post-release and fixed some bugs in mkrelease.
""",
u"""
got AST loading from a test suite as module working for a very limited scenario
""",
u"""
Release branch for 0.10.1
""",
u"""
Added google analytics code to templates
""",
u"""
as described in last commit, here is the actual test suite used for a proof of concept
""",
u"""
Updated copyright date range
""",
u"""
Better svnroot finding
""",
u"""
broke a ton of stuff but got AST working for a very very basic test suite in my tmp dir: a single directory named "test" (not a module) with two files: test_muhah.py and test_foos.py.  the former will raise an import error if imported and contains no tests, the latter contains one test which passes
""",
u"""
Updated NEWS and docs for release.
""",
u"""
Added missing doc, fixed paths in setup and mkwiki.
""",
u"""
a proof of concept ast visitor
""",
u"""
MERGED 0.10.0-stable 378:411 to trunk in preparation for 0.10.1 release.
""",
u"""
Updated documentation in preparation for release.
""",
u"""
creating branch ast_discovery
""",
u"""
CSS fix for issue #139.
""",
u"""
Added test for entrypoint name fix
""",
u"""
Bumped trunk version number to 0.11
""",
u"""
Fixed issue #63. Bumped version to 0.10.0a2 in preparation for release.
""",
u"""
Merged 0.10.0-stable [308]:[378] into trunk
""",
u"""
Fixed plugin loading bugs.
""",
u"""
Merged 0.10.0-stable [282]:[308] into trunk
""",
u"""
Fixed added is_generator to nose.util (alias for isgenerator)
""",
u"""
Merged 0.10.0-stable [266]:[282] into trunk.
""",
u"""
Release branch for 0.10.0a1
""",
u"""
Added missing doc file, fixed some typos
""",
u"""
More tweaks
""",
u"""
More release script tweaking
""",
u"""
Working on fixes to release script
""",
u"""
Fixed typo
""",
u"""
Doc updates; sort menu sections.
""",
u"""
Preparing for 0.10a1 release
""",
u"""
Updated man page
""",
u"""
Implemented loadTestsFromTestCase hook for plugins, with test.
""",
u"""
Added regression test for issue #3
""",
u"""
Pass kw args from runmodule to TestProgram
""",
u"""
Removed testgears reference from site index. Added api doc index.
""",
u"""
Added icons and cleaned up some formatting.
""",
u"""
Divided menu into sections
""",
u"""
More work on doc generation: added module attributes
""",
u"""
More work on doc generation
""",
u"""
More work on doc generation
""",
u"""
Hide DeprecationWarning for multiple -w args in test of multiple -w args
""",
u"""
Further work on documentation generation.
""",
u"""
Changed loader to more defensive when plugins try to load tests.
""",
u"""
Added menu links to generated docs
""",
u"""
More plugin doc updates
""",
u"""
Improved formatting of plugin interface and builtin plugin docs
""",
u"""
Started work on generating html docs for builtin plugins
""",
u"""
Updated NEWS and CHANGELOG. Further work (still in progress) on generating plugin api docs.
""",
u"""
Working on doc writers for plugin guide and api docs
""",
u"""
Fixed #48 (verbose/verbosity doc issue)
""",
u"""
Started work on doc links and index organization
""",
u"""
Fixed mkindex.py script. Started revising index documentation.
""",
u"""
Added additional twisted integration tests. Fixed bug in twistedtools handling of reactors that caused twisted.trial tests run after twistedtools tests to hang or otherwise fail to report any outcome.
""",
u"""
Changed exit argument to TestProgram to exit from exit_. Added failing error classes to test run summary.
""",
u"""
Restored --testmatch option used to set test match regex. Added -p, --plugins option that displays list of available plugins.
""",
u"""
Restored correct default behavior of main() (exits), run() (does not exit, returns success)
""",
u"""
Copied branches/0.10-dev to trunk. Trunk is now on 0.10.
""",
u"""
Updated setup.py to work without setuptools, if setuptools is not available
""",
u"""
Finished docstring sanity checks
""",
u"""
Updated docs in plugins.attrib and plugins.base
""",
u"""
Corrected some orphan imports found by pyflakes
""",
u"""
Added nosetests script under bin for non-setuptools use.
""",
u"""
Updated add_path so that it adds lib and src dirs in the parent path to sys.path also. Added functional test for lib/ src/ tests/ package layout.
""",
u"""
Updated docs in nose.plugins (top level of package only)
""",
u"""
Added functional test for testid/doctest integration when tests are from non-module files.
""",
u"""
Doc updates: all but plugins
""",
u"""
Applied missing changeset from trunk with fix and tests for multi-line docstrings near introspected asserts
""",
u"""
Restored lib-first sorting to loadTestFromDir -- needs tests.
""",
u"""
Fixed bugs in doctest loading from non-module files. Added functional test.
""",
u"""
Added shortDescription() to suite class, since it can push errors into result. Marked TODO items that need to be done before moving branch to trunk.
""",
u"""
Added camelCase variants for context fixture function names
""",
u"""
Doc updates (through nose.core)
""",
u"""
Reworked plugin manager and proxy to be more efficient
""",
u"""
Removed log.debug calls in some inner loops (optimization)
""",
u"""
Updated TODO, made another note of docs that need fixing.
""",
u"""
Changed getTestCaseNames to include runTest in test case case names if no other name selected -- 2.3 compat
""",
u"""
Added python 2.4 doctest as nose.ext.dtcompat to enable better doctest support for python 2.3
""",
u"""
Fixed 2.3 compat error in suites.
""",
u"""
Added --tests argument and deprecation warning for multiple use of -w
""",
u"""
Most of new -w behavior
""",
u"""
Removed __del__ from capture plugin: was causing odd side-effects when doctest enabled(?). Added set_trace convenience method to tools. Fixed various other small bugs.
""",
u"""
Implemented loadTestsFromNames hook in isolate plugin.
""",
u"""
Added first isolate plugin functional tests (one failing)
""",
u"""
Added support files for isolate plugin functional tests
""",
u"""
Some work on 2.3 compat -- still much to do
""",
u"""
Added plugin hooks that isolate plugin will need
""",
u"""
Fixed failing unit test imported from trunk
""",
u"""
Copied files missing from trunk merge due to lost history from hosting move
""",
u"""
Fixed tests failing after trunk merge
""",
u"""
MERGE trunk r10:r196 into 0.10-dev branch: some tests now fail
""",
u"""
Updated TODO and some docs/comments
""",
u"""
Modifed doctests plugin to use local subclasses of DocTestCase and DocFileCase that add address() and fix name attribute rather than wrapping. Removed TestWrapper from nose.case. Made builtin plugin loading slightly less manual and more robust.
""",
u"""
Moved test wrapper class from doctest to nose.case, most test-loading plugins will need it.
""",
u"""
Work on integrating doctest and testid plugins; doctest still needs some work to provide correct information to rest of system when individual tests are loaded.
""",
u"""
Fixed bugs in address() method for test generators. Fixed multiple ids output for generators in testid plugin. Updated TODO.
""",
u"""
Implemented basics of testid plugin. Still needs tests for doctests, and more tests for generator tests
""",
u"""
Started work on testid plugin
""",
u"""
Implemented loading from file.py:callable name. Removed debug log features from plugintest -- too complex to implement for this release.
""",
u"""
Updated TODO with issues relating to enabling debug logging within plugintester test runs, fixed python 2.5 test failure in nose.plugins.errorclass
""",
u"""
Started suite of tests of individual plugin api calls. Made plugin api call tracking test actually test something.
""",
u"""
Updated TODO. Added prepareTestCase plugin hook.
""",
u"""
Updated TODO
""",
u"""
Fixed bug in 0.9 addSuccess plugin call adaptation.
""",
u"""
Work on filling in gaps in plugin api, compat tests for 0.9-api plugins.
""",
u"""
Moved logging config to Config.configureLogging, added option to configure logging via logging config file.
""",
u"""
Fixed nose.core.collector, restored python setup.py test functionality
""",
u"""
Fixed commands module. Started work on making setuptools optional for install -- setup most likely is broken.
""",
u"""
Replaced inspect.isclass with less-permissive isclass.
""",
u"""
Additional function tests for mixedSuites suite/loader interaction. Cleaned up debug prints.
""",
u"""
Work in progress on loadTestsFromNames/context suite interaction
""",
u"""
Added ContextList helper class. Revised naming -- s/parent/context/ in context suites, cases and loader.
""",
u"""
Work on context suite/factory/loader to make them more compatible and able to run loadTestsFromNames efficiently (nowhere near done)
""",
u"""
About to being removed parent arg from context suite factory
""",
u"""
Started work on fixture changes needed to support effecient loadTestsFromNames
""",
u"""
Additional notes on efficiency vs correct fixture context
""",
u"""
Notes and work on fixing design of context fixtures, w/r/t loadTestsFromNames
""",
u"""
Added a few more plugin hooks to loader
""",
u"""
Implemented assert inspection as a plugin.
""",
u"""
Added array-attribute tests
""",
u"""
Use selector for test case loading, too, unless configured otherwise. More attrib plugin tests.
""",
u"""
Added functional test for test cases, implemented testName and describeTest plugin hooks.
""",
u"""
CamelCased Importer methods for consistency
""",
u"""
Started attrib plugin functional test suite. Fixed bugs in attrib plugin.
""",
u"""
Updated TODO. Fixed bugs in unit and functional tests. Changed some attibute names in plugin tester to be more appropriate.
""",
u"""
Fixed interaction between doctest test and importer test. Changed program tests to use canned config so they do not pick up settings from config files. Removed no longer appropriate unit tests.
""",
u"""
Added basic functional test for doctest plugin using plugintester
""",
u"""
Removed a stray import added by previous patch
""",
u"""
Added plugintest, adapted from Kumar McMillan's patch in #35.
""",
u"""
Added support for loading tests from plugins. Added discovered flag to loader so it can distinguish discovered modules from requested modules. Added __test__ flag support to selector for marking modules, classes, methods or function as tests or not tests.
""",
u"""
Fixed option handling in builtin plugins. Removed missed tests builtin, no longer needed
""",
u"""
Updated TODO. Added beforeTest and afterTest to plugin interface definition. Fixed bug in capture plugin that caused capture to stop after first error.
""",
u"""
Implemented Test.address method. Fixed failing test_address tests
""",
u"""
Fixed some failing imports in tests
""",
u"""
Make capture store a stack of stdout patches so it may be called repeatedly.
""",
u"""
Implemented config file support (#18) based on patch from Antoine Pitrou.
""",
u"""
Fixed some unit tests
""",
u"""
Removed deprecated tests and modules
""",
u"""
Restored stop on error functionality
""",
u"""
Removed deprecated code from selector, integrated selector into loader
""",
u"""
Added some doctests to errorclass
""",
u"""
Fixed loader and result bugs.
""",
u"""
Abstracted ErrorClassPlugin and helpers from SkipTest plugin. Implemented DeprecatedTest plugin
""",
u"""
Added score attribute to plugins and made them sorted by score. Fixed failing skip/pdb interaction test
""",
u"""
Added failing test for skip/pdb interaction
""",
u"""
Fixed a 2.3 compat issue in suite, added failing functional test for id plugin
""",
u"""
More work on moving output capture to a plugin
""",
u"""
Sketched legacy plugin manager/proxy that will be used to support 0.9 plugins in 0.10
""",
u"""
Updated pdb plugin to actively reset sys.stdout to sys.__stdout__ before running pdb. Added notes for test name() function that must return round-trip name for a test
""",
u"""
Started work on output capture plugin
""",
u"""
Added TODO and PLUGIN_API_CHANGES.txt documents. Filled in pdb plugin. Fixed some broken tests.
""",
u"""
Started work on pdb-errors/pdb-fails plugin
""",
u"""
Moved some functionality from skip plugin to nose.result, anticipating deprecated test plugin and erroClass plugin base class
""",
u"""
Added config methods to skip plugin, fixed patching logic, added 3rd term to errorClasses to allow registering whether a given error should cause the run to not be successful.
""",
u"""
Further work on self-hosting, skip plugin
""",
u"""
Started work on converting skip/deprecated test handling to plugins
""",
u"""
Approaching self-hosting: 0.10 can load and run its own functional test suite.
""",
u"""
Added start of plugins integration test, additional failing test to config unit test
""",
u"""
Work on integrating plugin calls, notes on result/proxy system.
""",
u"""
Cleaned up some tests, added real plugin managers
""",
u"""
Added a functional test for testprogram that loads some tests
""",
u"""
Fixed bugs in context handling and loader
""",
u"""
Improved importer behavior with dotted names.
""",
u"""
Work in progress on moving more of the context functionality into the context suite/factory
""",
u"""
Work on fixing bugs in context fixture handling when test names are specified
""",
u"""
Began work on functional tests from TestProgram
""",
u"""
Work on integration of resultProxy into suite/case, unit and functional tests, continued removal of context bits
""",
u"""
Fixed case and suite unittests (post context removal)
""",
u"""
Fixing tests and such for removal of context object
""",
u"""
Extremely broken: half way through removal of context class.
""",
u"""
Moved trunk to branches/0.9 in anticipation of copying 0.10-dev to trunk
""",
u"""
Moved trunk to branches/0.9 in anticipation of copying 0.10-dev to trunk
""",
u"""
Release branch for 0.9.3
""",
u"""
Further work on integrating result proxying. Just about to start removing the context object.
""",
u"""
Small edit to NEWS
""",
u"""
Work on result proxying and new plugin manager.
""",
u"""
Applied patch in #52 to fix bug in doctests/exclude interaction.
""",
u"""
Missed test support files
""",
u"""
Added config file support. Thanks to Antoine Pitrou.
""",
u"""
Fleshed out loader/fixture functional test
""",
u"""
Final updates prior to 0.9.3 release
""",
u"""
Work on suite fixtures/loader function test.
""",
u"""
Fixed 0-byte temp file leak with patch from Antoine Pitrou (#2)
""",
u"""
Current context implementation is flawed: it has to do a *lot* of extra work when a parent-level setup fails. Beginning new, suite-based fixture implementation.
""",
u"""
Catch "has no tests" value errors in all python versions -- 2.4 can raise them too.
""",
u"""
Updated test_loader.py to use a mock Importer
""",
u"""
Fixed doctest error handling in 2.4
""",
u"""
Work on supporting packages in importer.
""",
u"""
Added test using twisted test case to check compatibility
""",
u"""
Work on loader and importer integration.
""",
u"""
Included with_setup in nose.tools.__all__
""",
u"""
Started work on loader functional tests, revising importer interface
""",
u"""
Added support files for importer functional test and tried (again) to ignore .pyc files
""",
u"""
* Bumped version to 0.9.3
""",
u"""
Work on importer, plus propset to ignore .pyc files
""",
u"""
Only remove the profile stats temp file when no profile stats file was specified.
""",
u"""
Added functional tests dir, started work on revised importer.
""",
u"""
Work on better use of temp file in profiler plugin
""",
u"""
Work on basic result proxy tests and implementation.
""",
u"""
Possible fix for errors with twisted.unittest.TestCase tests
""",
u"""
Release branch for 0.9.2
""",
u"""
Started work on new implementation of result proxying/output capture
""",
u"""
More fixes to mkrelease script
""",
u"""
Added __str__, id() and shortDescription() to MethodTestCase
""",
u"""
More fixes to mkrelease script
""",
u"""
Implemented run() in nose.case.Test to avoid duplicate result calls.
""",
u"""
Fixed paths in mkrelease script
""",
u"""
Moved nose.fixture to nose.context and renamed Context to FixtureContext. Began implementing result proxying.
""",
u"""
Updated docs and ez_setup for 0.9.2 release
""",
u"""
Implemented first draft support for class-level fixtures.
""",
u"""
Fixed bugs in 2.3 compatibility
""",
u"""
Fixed issues resulting from file move. Implemented instance fixtures in MethodTestCase. Renamed some parameters.
""",
u"""
Fixed bugs in make_decorator that hid tests from selector in python 2.3. Made test_twisted compatible with 2.3 by changing decorator syntax to direct calls.
""",
u"""
Moved in-progress loader and suite and their tests into place.
""",
u"""
Wiki and doc updates for 0.9.2
""",
u"""
Removed old versions of suite, loader and their tests.
""",
u"""
Updated NEWS and CHANGELOG for 0.9.2 release
""",
u"""
Renamed some args and funcs in test case classes. Added support for generator methods.
""",
u"""
Improved nosetests man page formatting.
""",
u"""
Added failing tests for features under development (generator methods, class-level fixture context). Fleshed out MethodTestCase a bit.
""",
u"""
Added nosetests.1 man page.
""",
u"""
Added support for generator functions to new loader. Assorted code cleanups.
""",
u"""
Revised cheeseshop long description
""",
u"""
Added some implementation notes, started work on generator support
""",
u"""
Changed INFO message issued when working directory is inside of a package (issue #15)
""",
u"""
Misc notes and reformattings
""",
u"""
Fixed issue #25
""",
u"""
Renamed poorly named method
""",
u"""
More fixes to mkwiki
""",
u"""
Refactored TestLoader to tighten it up a bit. Made loader tests a bit more comprehensive.
""",
u"""
Fixed mkwiki ref issues
""",
u"""
Further work on filling out loader functionality. Fixed bugs in util functions.
""",
u"""
Work on expanding and correcting documentation.
""",
u"""
Renamed some poorly-named functions. Implemented rudimentary test function support in loader. Added context suite tests and fixed bugs in nested context suites.
""",
u"""
Fixed issue #6: method generators using inline functions no longer raises an exception.
""",
u"""
Updated README with warning and description of release goals
""",
u"""
Applied patch to fix handling of some options from setup.cfg from issue #13
""",
u"""
Work on integrating the fixture context into the test loader
""",
u"""
Applied patch for 2.2 compat from issue #23
""",
u"""
Work on new loader and tests. Started adding doctests to nose.util.
""",
u"""
Applied patch from issue #1, with minor tweaks and a unit test.
""",
u"""
Moved and renamed fixture.Case to case.Test, began work on new suite and loader
""",
u"""
Updated svn:ignore, docs, mkwiki
""",
u"""
Moved fixtr and test_fixtr into proper locations
""",
u"""
Moving rst2wiki to mkwiki
""",
u"""
Removed some completed FIXMEs
""",
u"""
More work on rst2wiki and doc updates
""",
u"""
Fixture context passes mod.submod test
""",
u"""
Work in progress on new rst->wiki formatter
""",
u"""
Added failing tests for handling dotted modules in fixture context (work)
""",
u"""
Updated index page for project home with new project hosting details
""",
u"""
Started work on experimental fixture context
""",
u"""
Added tickets from old site (rrss feed)
""",
u"""
Consolidated notes and NOTES into NOTES
""",
u"""
Added tickets from old site (csv format)
""",
u"""
[0.10-dev] Imported last revision from python-hosting to start 0.10-dev branch
""",
u"""
Imported trunk last revision from python hosting.
""",
]


