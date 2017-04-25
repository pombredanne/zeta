dernhelm_description = \
u"""
The Dojo Toolkit is an ''open source'' modular JavaScript library (or more
specifically JavaScript toolkit) designed to ease the rapid development of
cross platform, JavaScript/Ajax based applications and web sites. It was
started by Alex Russell, Dylan Schiemann, David Schontzler, and others in 2004
and is dual-licensed under the BSD License and the Academic Free License. The
//Dojo Foundation// is a non-profit organization[1] designed to promote the
adoption of the toolkit.
"""

dernhelm_compdesc    = \
[
u"""
One important feature of Ajax applications is asynchronous communication of
the browser with the server: information is exchanged and the page's
presentation is updated without a need for reloading the whole page.
Traditionally, this is done with the JavaScript command XMLHttpRequest. Dojo
provides an abstracted wrapper (dojo.io.bind) around various web browsers'
implementations of XMLHttpRequest, which can also use other transports (such
as hidden IFrames) and a variety of data formats. Using this approach, it is
easy to have the data a user enters into a form sent to the server "behind the
scenes"; the server can then reply with some JavaScript code that updates the
presentation of the page.
""",
u"""
Dojo provides a packaging system to facilitate modular development of
functionality in individual packages and sub-packages; the base Dojo
"bootstrap" script initializes a set of hierarchical package namespaces --
"io", "event", etc. -- under a root "dojo" namespace. After initialization of
the root namespace any Dojo package can be loaded (via XMLHttpRequest or other
similar transport) by using utility functions supplied in the bootstrap. It is
also possible to initialize additional namespaces within or parallel to the
"dojo" namespace, allowing extensions of Dojo or the development of private
Dojo-managed namespaces for third-party libraries and applications.

Dojo packages can consist of multiple files, and can specify which files
constitute the entire package. Any package or file can also specify a
dependency on other packages or files; when the package is loaded, any
dependencies it specifies will also be loaded.
""",
u"""
In addition to providing support functions for reading and writing cookies,
Dojo also provides a local, client-side storage abstraction named Dojo
Storage. Dojo Storage allows web applications to store data on the
client-side, persistently and securely and with a user's permission. It works
across existing web browsers, including Internet Explorer, Firefox, and
Safari. When included in a web page, Dojo Storage determines the best method
for persistently storing information. On Firefox 2, it uses native browser
persistence; on other browsers it uses a hidden Flash applet. With Flash 6+
being installed on about 95% of computers connected to the web [4], this makes
the storage mechanism accessible for much of the web's installed base. For a
web application that is being loaded from the file system (i.e. from a file://
URL), Dojo Storage will transparently use XPCOM on Firefox and ActiveX on
Internet Explorer to persist information. The programmer using Dojo Storage is
abstracted from the storage mechanism used, and is presented with a simple
hash table abstraction, with methods such as put() and get().
""",
u"""
Dojo can be used in javascript-based Adobe AIR applications. It has been
modified to meet AIR's security requirements.

Sitepen, a Dojo consulting company, has made an Adobe AIR application called
"Dojo Toolbox" using Dojo. It includes an API viewer, and a GUI to Dojo's
build system. Normally, the build system is run from within Rhino, but in this
AIR application the build system can be run from AIR, without use of java.
""",
]

dernhelm_mstndesc    = \
[
u"""
* Browser detection
* JSON encoding/decoding
* Package loading
* Powerful Ajax support
* Unified events
""",
u"""
* Animation support (including color animations)
* Asynchronous programming support (dojo.Deferred)
* High-performance CSS3 query engine
* Language utilities
* CSS style and positioning utilities
* Object-oriented programming (OOP) support
* Memory leak protection
""",
u"""
* Firebug integration
* Dojo build system, including ShrinkSafe
* Dojo Objective Harness (unit test harness)
* Unified data access (dojo.data)
* Universal debugging tools (integrated Firebug Lite)
""",
u"""
* Drag and drop
* i18n support
* Localizations
* Date formatting
* Number formatting
* String utilities
* Advanced Ajax transport layers (IFRAME, JSON-P)
""",
u"""
* Progressive-enhancement behavior engine
* Cookie handling
* Extended animations
* Remote procedure calling (RPC), including JSON-P
* Back button handling
* Baseline CSS styling (for setting uniform font and element sizes)
""",
]

dernhelm_verdesc     = \
[
u"""
Like every Ajax toolkit, Dojo gives you a rich set of utilities for building
responsive applications. Develop with confidence.
What sets Dojo apart is how it helps you succeed by giving you ways to
structure and optimize your project and re-use existing modules.
High-quality implementations.
""",
u"""
Dojo gives you access to a solid core library, created by some of the smartest
minds in the industry.
Unit (and battle) tested.
Hundreds of tests ensure that Dojo has a dependable infrastructure for
building great experiences. With millions of users of Dojo-based applications
every day, we wouldn't have it any other way.
Refined by design.
""",
u"""
The Dojo Core is the result of years of evolution and refinement. Built by
JavaScript experts, Dojo distills what you really need into a single package
that starts small and lets you scale up transparently.
Grow your applications.
As your application grows, Dojo's component-based approach lets you optimize
easily, collaborate more fluidly, and prototype more quickly.
No more cobbling scripts together.
""",
u"""
Best of all, the rest of the powerful modules in the Dojo Core, Dijit, and
DojoX are just a require() statement away. No more hunting for plugins or
cobbling scripts together. It's all right here.
Ajax and then some.
Getting data in the background is tremendously important to building
responsive applications, but as applications get larger in scope and more
immersive in feel it becomes clear that raw Ajax alone won't cut it. That's
why the Dojo Core gives you one of the most highly acclaimed Ajax interfaces
around.
From RPC to back button handling.
The Dojo Core provides RPC (Remote Procedure Call) modules to reduce Ajax
programming complexity, and back-button handling to help prevent users from
losing work.
Deliver amazing experiences.
From working prototype to production system, Dojo has got what you need to
deliver amazing experiences.
Parlez-vous Dojo? Sprichst Du Dojo Hablas Dojo?
""",
u"""
Internationalization is built right into the Dojo Core. With localizations for
over a dozen languages as well as date, currency, and number formatting in
hundreds of locales, the Dojo Core gives you reach, not just richness.
Speak any language.
Write JavaScript that communicates to the user in their own language Dojo
gives you the tools. Included is cultural support for entities in over 100
languages! And languages written right-to-left such as Hebrew and Arabic are
supported out of the box.
Test it, build it, optimize it, shrink it.
Your code is what gives your application life, not ours. We get it. That's why
Dojo gives you tools to help you in all phases of development and deployment.
Ensure stability with unit testing.
Dojo comes bundled with a powerful unit test harness that makes writing tests
easy and running them as simple as loading a page in your browser.
Optimize your application your way.
Tools like the Dojo build system let you optimize your entire application, not
just the parts you get from Dojo. Use ours or roll your own, Dojo's tools
support you all the way, either way.
""",
]

dernhelm_comments    = \
[
u"""
better docs for _stash and end, code reduction in NodeList-traverse methods. For NodeList.end, throw descriptive error if no parent NodeList. This is experimental though/needs more input. Pete for one is not sold on the idea, but I feel we need to fail as fast as we can instead of silently introducing bugs into a new user's code.
""",
u"""
extra checks for null parents (suggested by uhop). parent() really just needs to get immediate parent, and from what I can tell, element nodes are not embedded in anything hazardous except document nodes, but those are weeded out in _getUniqueAsNodeList. Also added a doc clarification to clarify name of function.
""",
u"""
re-introduces a _stash and end() method for dojo.NodeList. Also, methods that return new NodeLists also call _stash() so end() can be used properly with them. dojo._queryListCtor renamed to dojo._NodeListCtor since it is a more accurate description and also set by dojo.NodeList. This allows other dojo.NodeList delegates/variants to be used by our query and NodeList operations. Introduces traversing methods for dojo.NodeList via dojo.NodeList-traverse: children, closest, parent, parennts, sibling, next, prev, first, last, odd, even. Inline documentation is there, but still need to get feedback on the change and do wiki docs so leaving the ticket open. Also, create() and wrap() are not part of this update. \!strict for query.js
""",
u"""
Making it possible to reset the store by setting either url or _jsonFileUrl.  \!strict 
""",
u"""
Style and doc updates. 
""",
u"""
allow dojo.parser to expose the attribute used for querying, so that they can be reset for widgetsInTemplate parsing in multiversion scenarios.
""",
u"""
Fixes #9133: improve json-comment-filtered. Thanks to doughays for the basic patch: looks like our unit tests allow for other code, like while(true); block before the start of the comment, so we need to look for explicit starts of an object or array.
""",
u"""
- allow doc parsing to continue. fixing syntax error in pseudo-block
""",
u"""
Doc update, 
""",
u"""
Fix problem with pseudo-docs !strict
""",
u"""
Fixes #9219, #8649, #7833 and #8724: allow publication of IO pipeline topics, add dojo.fieldToObject (thanks to foobarfighter, CLA on file), allow generic args.rawBody for setting HTTP request bodies, and if hasBody is not passed to dojo.xhr, make an intelligent guess as to whether the query should be in the http body or as a query string. \!strict for dojo.io.script code has not side effects warning, but it is ok.
""",
u"""
fix for query system matching too many elements (possibly not checking for uniqueness in a set). Back-port to 1.3.x branch will fix. !strict

""",
u"""
Show callback functions as functions in documentation (with actual arguments) !strict
""",
u"""
Show callback functions as functions in documentation (with actual arguments) !strict
""",
u"""
Fixes #8732, adds script onload detection. Most of the core trick taken from plugd, from phiggins. Also allows jsonp instead of awkward callbackParamName for setting jsonp callback name. \!strict for some bizarre no side effect warning.
""",
u"""
fixes #9170 when column reordering in grid and high contrast mode is detected, use the default DnD icons which are low vision accessible. Updated default dnd to add generateText parameter so can turn off generation of text node in the icon. !strict
""",
u"""
Fixed up a doc bug. fixes #9189. !strict
""",
u"""
Missing common in pseudo-code
""",
u"""
Fixes #9172, content with array property was not being cleaned up properly and IE the code threw an error.
""",
u"""
fixes #8615 - adding unit tests to check the status of combined and chained animations onend
""",
u"""
Fixes #9001: clarify docs on the purpose of dojo.exists.
""",
u"""
- adding unit tests for fx showing inherited in a callback (two ways)
""",
u"""
!strict Fix typo. 
""",
u"""
- doc and style updates for declare.js - no code changes, just part of the patch. \!strict
""",
u"""
fixes #8557 #8559  replace the icons that only use color with new icons that use color and different shapes.  Also provide text only equivalents for when system is in high contrast mode.  
""",
u"""
- remove extraneous boolean checks for dojo.isString()
""",
u"""
- remove extraneous boolean checks for dojo.isString()
""",
u"""
Checking in translation updates into trunk.  Updates all locales except ca, th, sk, sl.  Fixes #7691
""",
u"""
Quick-and-dirty fix to get things like the grid working in IE again short-term.  This fixes issues in IE caused by [17266] - and may not by the correct fix, but it prevents crashes. !strict
""",
u"""
Use spaces rather than tabs before keywords as discussed on dojo-contributors.
and [17196].
""",
u"""
Test that null/undefined arg to dojo.byId() returns a null value.
This test worked in 1.3 but breaks as of the [17266] dojo.byId() refactor.


""",
u"""
- add test cases which demonstrate breakage caused by changeset [17266]
""",
u"""
Fixes IE event connect issue on trunk, !strict Thanks, jfcunat
""",
u"""
Cause unknown interval for dojo.date.add to throw.  Code reductions. Fixes #8973
""",
u"""
create (and use) a local reference to dojo.byId() in order to boost addclass-odd test #'s on IE6. Very strange, but the performance difference is nearly order-of-magnitude (80ms vs > 800ms). 



!strict

""",
u"""
- officially exposing dojo.Animation and leaving an _Animation stub \!strict
""",
u"""
fun patch as mentioned onlist, notes:

a) makes dojo._Animation not use declare
b) adds a test to ensure declare() can inherit from a function
c) fixes #9068 - you can pass a function to any property, or any
property member (start/end)
d) adds unit tests for c)
e) fixes #6484 - start/end/onEnd/beforeBegin are all passed the node
reference for the animation
f) unit tests for e)
g) fixes #8703 - increase the default framerate from 10 to 20 (100fps ->
50fps). reasons cited in the ticket. seems to be snappier now.
h) fixes the rest of #9070 (units: documentation)

will manually close all tickets and update appropriate docs to change to Animation, and do a bulk checkin fixing #4824

!strict


""",
u"""
Minor enhancement to ItemFile*Store + UT. \!strict  fixes #9077
""",
u"""
Roll back line shortening changes from [17195] (leaving in lint fixes and changes to API comment formatting/content.  !strict as usual.
""",
u"""
specify a locale on all culturally-sensitive tests. 
""",
u"""
specify a locale on all culturally-sensitive tests. 
""",
u"""
Code reduction *and* fix.  \!strict fixes #9022
""",
u"""
#9063 - cleanup easing inline docs \!strict
""",
u"""
doc comment formatting cleanup. 

""",
u"""
fixing html.js formatting. !strict

""",
u"""
- add in optional flag for not starting widgets when calling parser
""",
u"""
fixes #9007 - trunk is reopen "officially". 1.3 branch in place.


""",
u"""
Fixes #8776.  Resize the robot's test page iframe and console windows such that the container browser window does not need its own scrollbar.
""",
u"""
restore capability in query.js to dynamically change the node list constructor for each query call. \!strict
""",
u"""
a cleaner fix for cloned nodes that has their IDs changed. Added test case for testing the 'form with child element that shows up as an id property on the form.\!strict
""",
u"""
fixes #8952 - adding foundation set/getObject unit tests.


""",
u"""
Fixes XML unit tests for query in Opera. We were not setting caseSensitive in that case. The doctype and contenType do not give any value, so reverting to old school toString hackery. Should be OK given that it is limited to the opera case, but subject to review from Alex. \!strict
""",
u"""
Fixes #8937, get isFunction to work for strange Opera bug. We shuld still follow up with Opera though and report the problem but at least we can work with today's opera. Once they fix, we can remove the separate var assignment. Applying patch from peller.
""",
u"""
Fixes #8076: IE8 no longer needs the bidiScrollLeft fix, neato. \!strict
""",
u"""
missed the quirks box test failure. \!strict
""",
u"""
Fixes #8940: IE8 now includes the parent's border in offsetLeft/Top \!strict
""",
u"""
Fixes #8906: dojo.byId regression. Why IE do you make it so hard to get an element by ID? \!strict
""",
u"""
Remove test(s) that while I pursue what appears to be a Firefox bug.
""",
u"""
slight code reduction.
""",
u"""
style cleanup, doc expansion, fixes minor nits. !strict

""",
u"""
Fixes #8895. Remove accidental isGecko, and hack patch for firefox variants. Not a complete detection but better than what we do now, and least risk. Need a better solution for 1.4
""",
u"""
doc patch on onFirstMove to call out the px unit assumption; fixes #8874
""",
u"""
Fixes #8839, edge case with ID selectors that have a root. Updated unit tests. \!strict
""",
u"""
re-enable index cache. !strict

""",
u"""
removing extraneous parseInt calls. !strict

""",
u"""
nth-child selectors in the DOM branch were potentially returning the wrong results since the simpleElementTest would be elided for firstChild nodes that weren't elements. This is fixed by looking for firstElementChild on browsers that can handle it. Fixes #8775. !strict

""",
u"""
mention dojo.place as a viable alternative to dojo.html.set.
""",
u"""
fixes Prototype's bug for document.getElementsByClassName(), opens up our margin on byId-rooted tests on QSA, updates the case-sensitivity bug tests, and brings the docs into alignment w/ the code. Fixes #8697. !strict

""",
u"""
Testcase that parser doesn't pass unwanted parameters to a widget.
!strict.
""",
u"""
correctness fixes in the DOM branch. Make sure we don't double-count things in "," separated queries and ensure that we don't use QSA in suspect documents on WebKit (pending webkit fix to case-sensitivity issue). Fixes #8775. !strict

""",
u"""
Parser was putting "constructor" and "toString" into the params passed to every widget.
This in turn was causing Widget to do two unnecessary (and meaningless) dojo.connect() calls.

Fixes #8806 !strict.
""",
u"""
test case. 

""",
u"""
Fixes #8797, useless code.
""",
u"""
bundleMap, not bundle, \!strict
""",
u"""
Set svn:eol-style to 'native' on files missing it. (!strict)

""",
u"""
even more speedups on the DOM branch. Was doing some dumb stuff for ID and tag-only queries which this checkin fixes. Also, attempt to preserve zip-killing across groups. Tests show us to be ~30% faster than sizzle on IE 6. QSA branch still faster nearly everywhere, but by variable amounts depending on the engine (15-50%). !strict

""",
u"""
fixes a typo in getNodeIndex which caused node indexes to be lost, dropping our speed on nth-child queries. Also significantly improves peformance on ":not" pseudos by specifying ignores in the test generator. Fixes #8654. !strict

""",
u"""
move floating point fudge from dojo.number.round to dojox.math.round (experimental)  
""",
u"""
Make sure Infinity/-Infinity are formatted to null.  
""",
u"""
Support 14 sig figs.  Fixes #8699, !strict
""",
u"""
Fixes #8744. Thanks klipstein for tracking down the problem with multiversion suppport.
""",
u"""
Fixes #8282, applying Eugene's patch with expanded unit tests for NodeList.addContent
""",
u"""
Fixes #7633, upload.cgi had a bad percent that was not escaped. Also turned off file saving by default to avoid common permission/directory missing errors.
""",
u"""
Reshuffling mouse button processing, !strict, fixes #8603.
""",
u"""
Redirecting the "class" attribute access to use node.className, !strict, fixes #8499.
""",
u"""
Updated license text to clarify this and make it CLA/Dojo license compatible. \!strict fixes #8682
""",
u"""
doc typos !strict 
""",
u"""
Fixes #8621, dojo._toDom auto-selecting an option tag. \!strict
""",
u"""
References #6245.  Remove manualTests from dojo/ in favor of creating robot tests.
""",
u"""
Only do try/catch block for relatedTarget.tagName for FF2.   It's not needed for FF3 and causes some issues.
and fixes #8555.

Also in that it fixes that issue (lingering hover effect on tree nodes) when firebug is enabled, but it's still failing when firebug is disabled as that's another issue.

!strict
""",
u"""
Test infrastructure updates, as discussed with Mark:
 - Allow test page to listen to topics published by child page
 - Use dojo.setContext() to point parent page to child page, so that dojo.global also gets redefined, in addition to dojo.doc... that lets test code easily access variables in the child by referencing dojo.global.foo, or perhaps more correctly by calling dojo.getObject()


""",
u"""
Fix doc typo, !strict
""",
u"""
and #8613. Reverts changesets [16641] [16642] [16643]. dojo.create not accepting html strings has been explicitly discussed as not being included in Dojo 1.3 multiple times now. We can talk about it more for 1.4 after we have had time to let the current create bake a bit in the wild. It is easier to add things later than take away later too. Similarly with NodeList, while I want an end() in general, i want to be sure we think through the use cases for it, and adding more API. and it was done without adequate notice. \!strict
""",
u"""
taking attr setting out of create. is redundant. these all technically beat enhancement cutoff, begrudgingly. 
- unit tests all pass so they either don't exist or didn't regress. also not sure create() accepting complex 
markup is the right thing, especially with the implemenetation with the try{}. you can createElement("<iframe blah;>") for instance. !strict 


""",
u"""
adding sugar to dojo.NodeList instances. Needs expanded tests. !strict

""",
u"""
make sure that create() works with actual markup. Fixes #8613. !strict

""",
u"""
Getting rid of console.debug calls even in comments/doc comments for code in Core, in an effort to move away from console.debug, since it is not supported in other native consoles like webkit and IE8. \!strict
""",
u"""
Fixes #8601, #8602 - added trace() and count() methods. Doing an additional check for Mozilla's firebug lite. !strict
""",
u"""
make sure that null lists don't fool us in the DOM branch + test. Fixes #7125. !strict

""",
u"""
test case for #7125. 

""",
u"""
adding existance test to ID filtering. Fixes #7368. !strict

""",
u"""
exposing _mapIntoDojo, but renaming to _mapIn. Fixes #7295. !strict

""",
u"""
Fixes #8598: change var listCtor to dojo._queryListCtor. Also had to move getNodeIndex above first use to avoid shrinksafe bug with mangled names. \!strict
""",
u"""
get the sizzle wrapper to do more of dojo.query-like work when query is not a string, then for both acme and sizzle, make sure the dojo detection works with multiversion support. \!strict for sizzle code
""",
u"""
Modifying the VML style rule to conform to Microsoft's guidelines. 
""",
u"""
Change console.debug call to console.error, fixes #8583.  (Do we really need a console message here at all if the error can be detected programatically?  Style change 
""",
u"""
dojo._base.window is browser-dependent.  Avoid tests in non-browser environments.  
""",
u"""
make sue that query-sizzle.js can still run stand-alone (for side-by-side perf tests). !strict

""",
u"""
removes cruft, updates code comments, and makes some operations slightly quicker. !strict

""",
u"""
allow sizzle as a build option replacement for normal dojo query engine. Still some rough edges/behavior differences, and want to be sure this is the best way to integrate. \!strict
""",
u"""
doc update for note about pixel values. \!strict
""",
u"""
Fixes #8506: adjust dojo.isIE if x-ua-compatible EmulateIE7 is used.
""",
u"""
some small doc changes.
""",
u"""
change the behavior of addOnUnload and addOnWindowUnload to prevent default registration of unload and onbeforeunload handlers since they can defeat fastback behavior. Updating docs for affected APIs and adding a test of the system to verify that it works. The test is kind of a pain to run, but it does proove that the change has the intended behavior.




""",
u"""
Tweak to fix case in null comparision.  fixes #8480
""",
u"""
Fixes #8047: IE8rc1 is much better now, and we do not need an offset calculation for nodes. There is still an issue with rtl direction and the offsetLeft, but will open a separate bug on that, but I believe it is Microsoft's to fix, it is a strange negative number. \!strict
""",
u"""
minimize xhr callbacks happening in the middle of an execution thread when starting a new XHR call. Still needs more work for sync requests, so leaving ticket open for a future milestone to address sync case.
""",
u"""
Fixes #8495 using patch from doughays. Thanks for catching the bad previous fix.
""",
u"""
Fixes #7690, dojo.byId fix, thanks to Mike Wilson for the pointers from DWR. Unit tests added too. \!strict for existing code
""",
u"""
reduce some more and add unit tests. 
""",
u"""
hrm, not sure how this got missed... !strict

""",
u"""
Rolling back some changes to dojo.create(), updating docs and unit tests, !strict, 
""",
u"""
handle the case where a failed scope lookup would otherwise cause us to search the entire docment. Instead, return an empty NodeList. Adds test for this case. Fixes #7211. !strict

""",
u"""
IE8: Fix problem with dojo._abs() when page is scrolled.
Fixes #8429, #8441, #8460.  but that is still an open issue.
!strict
""",
u"""
fix for IE in non-build environment. !strict. 

""",
u"""
fixes build breakage that haysmark and phiggins found. !strict

""",
u"""
- ducks quack (though are arguably quick, too). 
!strict


""",
u"""
remove the internal namespace protection closures since we get a global one generated for us by the build system. Also, remove the shortened names for Dojo where possible so that shrinksafe can alias "dojo" on its own. Saves us another couple hundred bytes or so after gzip and should speed eval time.

!strict

""",
u"""
fixes #8415 - adding .onchange support for nodeList. !strict


""",
u"""
more mobileWebkit exclusions. !strict

""",
u"""
Adding a missing unit test for a placement with a number rather than a string, !strict, 
""",
u"""
tighten it up just a bit more for the webkitMobile build. !strict

""",
u"""
The return of dojo.place() is modified as agreed => now it returns the first argument resolved to a DOM node, !strict, 
""",
u"""
my bad. !strict

""",
u"""
fix test html unit test failure in webkitMobile profile. !strict

""",
u"""
save a few more bytes. 
""",
u"""
save a few bytes. 
""",
u"""
ifdef's for the core to create a webkit-only version for use in, e.g., mobile devices. 

Build this version with:

	./build.sh profile=base action=clean,release webkitMobile=true

!strict


""",
u"""
Fixes #8367.  Per jburke, unset cached dojo._bodyLtr in withGlobal and withDoc.  Had to call delete since _isBodyLtr returns whatever value is set (null/undefined/true/false).
""",
u"""
refNode can be a string too --- making sure to count it in when attrs is missing, !strict, 
""",
u"""
More inlined docs changes, !strict, 
""",
u"""
Removing unnecessary notes from the inlined documentation, !strict, 
""",
u"""
Adding the handling of missing attrs with a unit test, !strict, 
""",
u"""
Adding dojo._toDom() functionality top dojo.create() with unit tests, !strict, 
""",
u"""
Undo inlining of rev.  Distributed SCM like git and bzr provide alternate access to our svn and will not substitute keywords.  
""",
u"""
Update to IFWS.  \!strict fixes #8432
""",
u"""
Update to IFWS.  \!strict fixes #8432
""",
u"""
Minor fix to back. \!strict fixes #8431
""",
u"""
remove hostenv comment inserted in [16348]  
""",
u"""
Update minor rev in lieu of script. 
Inline rev, remove conditional since it's always got to be there.
""",
u"""
- fixing inline docs for nodelist (slightly). adopt and place pass through position to place(), which introduced 
only and replace (if i'm not mistaken). These may not be desireable. It is also worth expanding upon the behavior of dojo.place() when used with complex creation, and the end results of only and replace. but that can be covered in user docs. 


""",
u"""
Minor cleanup in testcase code.  fixes #8403
""",
u"""
should have hit save first.  Include cast to JS String.  !strict
""",
u"""
Additional patch to correct a Rhino bug with bidi override chars in the build.  like dojo.fromJson, dojo.requireLocalization also uses eval on the file contents and must be patched.  Fixes #3808 !strict
""",
u"""
Check for setTimeout and clearTimeout definitions explicitly, since the reference does not seem to throw in Rhino 1.7.  Fixes #8159 !strict  Thanks, Mark Wubben!
""",
u"""
another query test for the weird case, but seems to pass in the query doh tests even before the 8394 fix.
""",
u"""
Fixes #8394, odd query issue in IE8, fixes tests._base.html_element tests in IE 8. \!strict
""",
u"""
Reusing dojo.create() in the base (back and dnd functionality), !strict, 
""",
u"""
Aliasing dojo.html._emptyNode() to dojo.empty(), !strict, 
""",
u"""
Implementing replace/only placing options with tests, !strict, 
""",
u"""
More comprehensive tests for dojo.place(), !strict, 
""",
u"""
Adding the HTML fragment support to dojo.place(), !strict, 
""",
u"""
Renaming dojo.toDom() to dojo._toDom(), updating all known referencing, !strict, 
""",
u"""
Removing fieldset-related records in the tag wrapping dictionary, !strict, 
""",
u"""
Taking out the HTML cleanup code, !strict, 
""",
u"""
Reduce test group name size.  \!strict fixes #8372
""",
u"""
Tweak to testcase for abort to be nicer about timing (finish before abort is called), and only running in async cases, the browser. \!strict  
""",
u"""
Implementing James Burke's suggestion to return a singular element directly without wrapping it in DocumentFragment, !strict, 
""",
u"""
Acting on James Burke's suggesting to simplify the placement of DocumentFragment, !strict, 
""",
u"""
Adding dojo.toDom() to process dojo.attr(node, "innerHTML", frag) on IE correctly,
minor changes in dojo.toDom() to save bytes, correcting the argument override in
html element tests, adding unit tests for new functionality, !strict, 
""",
u"""
Making the unique string scope-based, !strict, 
""",
u"""
Adding more elements to the self closed tag dictionary, and to the wrap dictionary, !strict, 
""",
u"""
Adding in an abort linkup in ItemFile*Store to proxy the abort call. \!strict  
""",
u"""
- update things to use 2009 as end (c) date. Also seems a small stray comma fix snuck into this checkin.

!strict because of doh.runner 


""",
u"""
Remove unneeded call to str.trim().  
""",
u"""
Reducing the code by several bytes and improving the load time a little, !strict, 
""",
u"""
Restructuring dojo.trim() and dojo.string.trim() to make a choice (native
vs. manual) only once during the loading time. !strict. Fixes #8182.
""",
u"""
Update docs to indicate native String.trim() is used.  
""",
u"""
some size reductions. Also (finally) enables the QSA branch. Not sure how I missed that.

!strict

""",
u"""
Use native String.trim() where available.  Fixes #8182
""",
u"""
Adding dojo.toDom() with unit tests, the code by James Burke (thank you!)
with minor optimizations, and an extra argument to specify the document
explicitly, !strict, 
""",
u"""
fixing regression in XML tests related to tag name case sensitivity. Fixes #8356. !strict

""",
u"""
updating for the acme engine. 

""",
u"""
Implementing dojo.empty() with unit tests, !strict, 
""",
u"""
steak -> acme. Need a better name. !strict


""",
u"""
Fixes #8344 !strict.  Change readonly to readOnly for all browsers.
""",
u"""
some require() and NodeList doc changes that happened while I was hacking on steak. #4425

""",
u"""
The new query engine (aka: "steak").

Making claims about the speed of the system would be counter-productive, but
suffice to say, steak is really, really fast.. It acheives its speed in ways
that differ from its predacessor. Instead of branching for DOM vs. XPath, the
new engine branches QSA vs. DOM, dropping the XPath engine entirely. This
allows for a sizable reduction in overall size of the codebase. Next, the query
dispatch function has been moved from a recursive system which always had some
obvious warts to a set of nested loops which have differnt (but easier to
understand and hack on) warts.

Sizable room for improvement performance exists as it may be possible to use
the tokenizer to say more about a particular query and how it should be
dispatched. Also, it may be possible to run more queries through QSA than we
currently do. This is being investigated for 1.3.x.

Lastly, steak is stand-alone. Recent versions of dojo.query have been able to
stand on their own with minimal scaffolding, but steak improves upon that by
building default scaffolding in but hiding it behind build-time ifdefs to
ensure that the size of Dojo isn't affected.

Fixes #7072. Fixes #4425. !strict

Tests coming in next commit.

""",
u"""
Escape "+" in regexp literals and add tests.  Fixes #8346
""",
u"""
Add dojo.cldr locales to svn to match translated list.  Fixes #8342
""",
u"""
fixes #8298 - minor doc notation.


""",
u"""
- update to use dojo.destroy


""",
u"""
ensure that if nothing is passed to mixin() that a blank object is still returned. Fixes #8335 and provides tests.

""",
u"""
fixes #8317 - moving Toggler out into own file for 1:1 mapping and size considerations (though a require() is issued in fx.js for backward compatibility, it may be wrapped in a deprecated build tag as per #8271)
!strict


""",
u"""
and - adding better docs for dojo.create (noting about alias to dojo.doc.createElement) and adding other examples.
!strict


""",
u"""
dojo._base.html: verified the problem, added the fix, modified tests,
fixes #7920, !strict.
""",
u"""
- deprecating use of dojo._destroyElement internally in Dojo Core
!strict

""",
u"""
- update unit test to not destroy firebuglite if in page. something about setting style:"" as an attr is wrong, so disabling that test for now and will investigate in attr itself as a separate thing. passes opera (though isFunction failed, investgate that too), and ie6/7 


""",
u"""
and - adding dojo.destroy as an alias to dojo._destroyElement (leglizing the usage), and adds simple version of dojo.create following the API:

dojo.create("div");
dojo.create("a", { href:"foo.html" });
dojo.create("div", null, dojo.body()).innerHTML = "<p>hi</p>";
dojo.create("br", null, dojo.body(), "first");

needs wiki doc pages, but inline API docs are complete. unit tests pass ff2/3 and Saf3 - testing ie after migrating patch in, though if something fails it is either a faulty test case or in one of the underlying attr/place methods used. This is just an alias with sugar. 

we can document known issues ( create("td", { innerHTML:"..." }) ) and avoid putting magic in base. 

!strict


""",
u"""
- giving vars breathing room, spacing var lists, etc. non-changing.
!strict


""",
u"""
- commiting unsaved changes from previous commit. more examples.

""",
u"""
- base size reductions, - adding many examples


""",
u"""
fixes #8319 - reducing the mixing, caveat noted in ticket.  
fixing one strict warning.



""",
u"""
i think this - a [meta] doc/style cleanup - but cannot reach trac to look up. adding example: tags and small style cleanups.
!strict 

""",
u"""
rolling back r16125, there is a larger question about supporting fetching properties of a DOM element vs things via getAttribute() and things that are considered true dom attributes. Adding all of those dom properties to _attrProps is not scalable. \!strict
""",
u"""
Fixes #8310, dojo.attr should work with defaultValue. \!strict
""",
u"""
Fixes #7875, make sure djConfig.require path uses multiversion scope name. This approach also works better in non-eval friendly envs like AIR.
""",
u"""
Use 0.9 in our test instead of 0.5, so we'll be less susceptible to other browser bugs.  
""",
u"""
fixes #7896: readonly needs to be treated different (just as tabindex) for IE<8
!strict

""",
u"""
Fixes #5732, allow dojo.js urls to end in a semicolon. Using the same match as used in hostenv_browser.js. \!strict
""",
u"""
revert isFunction() check for isWebKit.  Unit test added in [15738].  
""",
u"""
dojo.dnd: typo fix: switching from isWebkit to isWebKit, !strict.
""",
u"""
dojo.dnd: switching from isSafari to isWebkit, !strict.
""",
u"""
scrubbing dojo.isSafari use in Core, using isWebKit where appropriate. Have not done dojo.dnd internals though, and dojo._firebug had some isSafari references too, but not sure those need to change. \!strict
""",
u"""
Fixes #8270: Chrome: doojo.coords incorrect value on width. \!strict
""",
u"""
Fix dojo.coords() on IE in quirksmode.   Patch from Nic (CLA on file), thanks Nic!
Fixes #8047, !strict.
""",
u"""
Fixes #8023, allow for more descriptive cancel messages in Deferred.
""",
u"""
Fixes #7981: move the throw-instead-of-catch behavior for deferreds and related to trigger off of debugAtAllCosts. \!strict
""",
u"""
dojo.fx: simplifying dojo.fx.combine(), !strict, 
""",
u"""
dojo.fx: fixing a bug in dojo.fx.combine(), thx ashendw!
!strict, fixes #6490.
""",
u"""
- unit test for combine chained and chained combined animations. 
failing atm, fix coming.


""",
u"""
dojo._abs was returning wrong x, y in Safari (v3.2.1 on the mac) when there was an html border...
top and bottom buttons in abs.html test file.   This fixes it.

!strict
""",
u"""
Fixes #8247: dojo._abs returns wrong x, y in FF 3 when there is an html border.
Thanks Nic (CLA on file) for the patch!
!strict
""",
u"""
Fix for multivalued form field.  fixes #8212
""",
u"""
Tolerate leading zeros in whole part without separators. Fixes #6933
""",
u"""
Minor update to localise lookup of XML parsers by using _base private function.  
""",
u"""
Assure that round goes away from zero on ties.  Improve docs.  #8036
""",
u"""
Save a couple of bytes.  !strict
""",
u"""
fixes #8180 - m is undefined, so don't pass that. best bet, pass the index of the mixin that is missing. more helpful than #undefined. thanks dylanks.
!strict


""",
u"""
Fix typo.  Fixes #8181 !strict
""",
u"""


  * Changed hasBase from global to local.
  * Pass return of loadSubScript() to cb.

""",
u"""
Accounts for ugly IE bugs in toFixed().  
""",
u"""
fixes #8022, but went with .prototype instead of dojo.declare and fixes #7858 based on a [ccla][patch] from JavaStreet (bbyron). Thanks!

!strict

""",
u"""
Trim out a few bytes. 
""",
u"""
And now more patches for iframe and IE8.  Oy.  
""",
u"""
Committing in minor tweak to XML dom parser load path  \!strict 
""",
u"""
Committing in minor tweak to XML dom parser load path  
""",
u"""
Fixing _base/xhr.js for IE8.  
""",
u"""
commiting additional fx unit tests to illustrate failure in Animation when calling stop() before a play() delay has started.



""",
u"""
remove platform is* initializations; assume undefined. because I can't get to trac.
""",
u"""
Style cleanups.  !strict
""",
u"""
Make getIeDocumentElementOffset() return correct results for IE8.
(Didn't test RTL mode though)
Fixes #8047 !strict.
""",
u"""
Call _getIeDocumentElementOffset() on IE8 again, but it's returning (0,0) until we can make it return the correct value.  The IE7 branch of that function doesn't work on IE8 (in strict mode) because it's result is affected by margin on <body>, and negatively affected by body's scroll.

Also removed add()/subtract() functions since they were slightly slowing down dojo._abs().

!strict.
""",
u"""
rolling back changes to use native console as much as possible. Turns out at least IE and Safari do not have console.debug at the very least and do not support console.dir and some other functions. I should have tested more pages than my simple test case used for the previous change. \!strict
""",
u"""
Remove unnecessary chars from escapeString expression.  
""",
u"""
removing the QSA branch. Fixes #8102. !strict

""",
u"""
Event normalization should include Chrome.  Style fixups also.  !strict
""",
u"""
Style things.  !strict
""",
u"""
generalize _getQueryFunc for Chrome.  !strict
""",
u"""
Add isFunction unit test.  
""",
u"""
Fix event normalization (for mouse position) for IE8.
Fixes problem with avator being far away from text (fixes #8081 !strict)
""",
u"""
Oops, safari doesn't support getBoundingClientRect() after all.
#8047 !strict.
""",
u"""
Both opera and safari support getBoundingClientRect(), so remove special code for safari and opera in the else branch (which computes results manually by tracing the DOM tree).

It seems only FF2 needs that else branch.

#8047 !strict.
""",
u"""
Don't call _getIeDocumentElementOffset() on IE8.  This fixes the tests/_base/abs.html test.  Also various marginal size reductions.

Fixes #8047 !strict.
""",
u"""
Fixes #8048, Firebug lite broken after shrinksafe runs over the file. Happens because of a bug in shrinksafe where it does not properly replace vars that are placed after they are first used. \!strict
""",
u"""
Fixes #8072: firebug lite interfering with dojo.query tests. noFirebugLite: true was being used, but according to _firebug/firebug.js it is deprecated now in favor of just isDebug: false. Also changes in 8103 to use native consoles also reduces the need for firebug lite for this test page.
""",
u"""
Fixes #8103, favor using native browser console instead of firebug lite. Helpful in IE8. Also includes docs for a couple more djConfig parameters. \!strict
""",
u"""
oops. remove console.log. 
""",
u"""
oops. remove console.log. 
""",
u"""
Normalize whitespace/nbsp handling for currency.  
""",
u"""
- minor fix to when you specify types, need to make our value "look" like a namedItem
""",
u"""
Fixes #7090 - add in patch that allows a mixin to be passed to dojo.parser.instantiate
""",
u"""
Improve algorithm to try to round out binary floating point errors, and document it.  Fixes #7930
""",
u"""
Fixes for dojo.attr(node, "class", ...) on IE8, plus adding some hints to test file.
!strict
""",
u"""
fix some doc typos.  !strict
""",
u"""
adding dojo.pushContext and dojo.popContext calls for use in the XUL host environment.

!strict


""",
u"""
Put in comment, since all non-extension FF devs will now hit the try/catch.  Fix up some minor style issues.  !strict
""",
u"""
ensure that firebug lite doesn't throw errors when logging text nodes. Fixes #8008. !strict

""",
u"""
better. thanks, cougar.   !strict
""",
u"""
use String.indexOf   !strict
""",
u"""
Additional docs for dojo.style. \!strict
""",
u"""
Translation updates from Lotus Domino for sl/sk.  
""",
u"""
- thanks neonstalwart for the doc patch/cleanup


""",
u"""
small doc update 


""",
u"""
- summary wants a : 
!strict


""",
u"""
Remove query dependency on dojox.dom method.  Fixes #5052
""",
u"""
Use some instead of forEach searching for ActiveXObjs (thanks, Alex)  Improve corresponding test. 
""",
u"""
dnd: fixing the DnD handles problem, !strict, fixes #7944.

""",
u"""
dnd: preventing the selection on IE at the manager level, minor cleanup,
doc update, !strict, fixes #6155.

""",
u"""
make nameAnonFunc a local function inside the closure. 
""",
u"""
code reductions. 
""",
u"""
making sure that opacity animations work correctly in XUL environments. Fixes #7942. !strict

""",
u"""
Cleans up docs on isKhtml.
""",
u"""
- pass error through to callback !strict
""",
u"""
Implement dojo.date.locale.displayPattern.  Fixes #7666
""",
u"""
Ignore am/pm with alt attributes. 
""",
u"""
Update dojo.cldr.  Fixes #7665, #7849.
""",
u"""
Fixes #5574 and Fixes #7696. dojo.isChrome and dojo.isWebKit available. dojo.isWebKit now gives version numbers like 525.3. KHTML detection changed to just support being defined for KHTML browsers only, since other KHTML-related browsers are likely more sensitive to dojo.isWebKit versions. Changed dojo.isSafari check so that now Safari 3.1.2 now correctly reports as dojo.isSafari 3.1. But with that change, Chrome browser does not have dojo.isSafari defined, which should be good, since we now have dojo.isWebKit and then dojo.isChrome for chrome-specific (non-webkit) issues. Now that there are webkit numbers, switched to DOMContentLoaded for webkit versions that support it. \!strict
""",
u"""
removing bad impls of createElement() and elem(). !strict

""",
u"""
fix to prevent Firebug Lite from popping up in Firefox Minefield builds. Fixes #7818. !strict

""",
u"""
build system fix to prevent us looking for nodes in environments that don't have them. !strict

""",
u"""
ensure that attribute names and values are correctly looked up in XML documents on IE. Will need to merge this back into the 1.2 branch. !strict

""",
u"""
make the default loader work in strict XHTML environments and fix Opera to correctly detect case sensitivity in XML/XHTML environments for queries. A small PHP script is added to test these. Sadly, both Safari and Opera don't observe script ordering for injected tags, so we had to make the dev loader script a bit more complicated to accomidate. Fixes #7455. Fixes #7214. !strict

""",
u"""
major addition of comments to the dojo.query() code as well as some small cleanups to enable query portability. Adding a test page for using query() without the rest of Dojo. Fixes #7794. !strict

""",
u"""
dev-time support for detecting and loading a XUL-based host-environment. Also adds a host environment file build specifically for use in extensions and a trivial patch to allow the build system to be told that it's in a browser-like environment. 

!strict


""",
u"""
My OCD compels me to alphabetize these names.
""",
u"""
Set svn:eol-style to 'native' on files missing it. !strict

""",
u"""
Fixes #6876. Thanks to Bill for improving the patch. Arrow keys now detectable via onkeypress in Safari 3.1 without using IE code paths. Also, dojo.disconnect for onmouseenter/leave for non-IE browsers should work now. \!strict for existing code patterns.
""",
u"""
a test page for keypress events.
""",
u"""
Fixes #7748, reinstate faux onmouseenter / onmouseleave events for safari.
!strict
""",
u"""
Fixes #7714. The change to switching to setting Enabled on a filter (to preserve other filters on the node) left a previously set value of opacity as the opacity value even though it was not active. Make sure we update the opacity value to 1, but still make sure the filter is set to Enabled = false for the opacity == 1 case. \!strict
""",
u"""
Fill in example for dojo.string.pad. 
""",
u"""
Fix docs for num arg on rep. 
""",
u"""
Fixes #7667. Thanks for dfabulich for tracing down the problem and providing a patch to indicate what still needed to be checked. I did not use the patch as-is though: from what I can tell the extra setTimeout call to _xdDebugFileLoaded is not needed if we clear the currentResourceName before doing the check for inflight modules.
""",
u"""
References #7681.  The robot code should execute with the same BASE as the page being tested so that XHR gets work correctly (Safari 3.1 seems to require this).
""",
u"""
- commas are being evasive today


""",
u"""
add a comma, remove a comma.  
""",
u"""
- djConfig.require: Array was not documented.


""",
u"""
- updating the format for inline docs in requireLocalization ... _browse test accurately find the params and
types, and formats the example, so if this persists it is a parser bug it would seem.


""",
u"""
fixes #6291 - adding package-level docs and fixing syntax of dojo.behavior API docs.


""",
u"""
Fixes #6876 !strict.  Force safari to take a similar code path as IE and generate faux keypress events.  Removed the mac keycodes since safari 3.x uses the same keycodes as IE and FF.
""",
u"""
Change dojo._loadModule documentation to reference public API dojo.require.  
""",
u"""
Fixes #7642 - make sure consoleBody exists before trying to clear it !strict
""",
u"""
Update dojo.cldr with proper aliasing to preserve abbreviations.  Fixes #7607
""",
u"""
Correct iphone example. 
""",
u"""
Making typeMap parser settable. \!strict  fixes  #7625
""",
u"""
- add example and words to animateProperty docs.
!strict


""",
u"""
fixes #7604 - can't rely on djConfig being global, need to use dojo.config - which handles scopeName, and djConfig="" on the <script> tag, and conversion from a global djConfig
!strict


""",
u"""
Eliminating stray commas. !strict
Some of the stray commas are relatively harmless (e.g., in commented out examples).

""",
u"""
Use arbitrary subset of currencies by default. 
""",
u"""
update dojo.cldr with improved xslt scripts to follow aliases.  Fixes #7188
""",
u"""
Use conditional build options to leave out rhino-specific fix for browser builds, to limit impact on dojo base size. \!strict
""",
u"""
Make sure dojo.io.script documents the io args in the same way dojo.io.iframe and dojo.__xhrArgs does too, so that dojo.__IoArgs shows up as parent.
""",
u"""
Fixes #7435, optimize console calls in non-debug case. Thanks to jcerruti (CCLA on file) for the patch and testing coverage.
""",
u"""
- make core html unit tests part of the test suite


""",
u"""

* dojo.html.set, dojo.html._ContentSetter warn when no content is given
* merged the unit test patch and fixed up existing ones
""",
u"""
- updates inline docs for NodeList-html 

""",
u"""
- document default value for position !strict
""",
u"""
- adds unit tests for dojo.fx.easing sanity checks.


""",
u"""
- update fx.easing inline docs and style adherance
!strict


""",
u"""

* Adds an empty() method, which empties the node and destroys any widgets in the parseResults array
* Minor clean up in the test page
""",
u"""
Add ca, sk, sl, th translations, plus all translations for PasswordValidator.  From IBM (CCLA) Fixes #7481
""",
u"""
Simplifying argument checks in dojo.place(), fixing a bug.
Removing the related unnecessary code from NodeList.place().
Fixes #7546. !strict

""",
u"""
Fixing a typo. !strict

""",
u"""
Manual Array copy in connect.js under Rhino. Fixes #7523. !strict
""",
u"""
Fix the iframe.__ioArgs documentation definition.  !strict.
""",
u"""
Fixes #7534 !strict Added isAIR param so Lite won't launch in an AIR app
""",
u"""
removed unused parseOnLoad alias for parseContent, fixed error in the fallback error handler which was refering to this.domNode. 
""",
u"""
References #7521. Proxy commit for haysmark.
Create robotx.js so that the robot can be separated from the unit test files
Reorder mouseMoveAt parameters for API consistency.
Drop new test_dnd unit test.
""",
u"""
Run browser-based tests conditionally.  #7178
""",
u"""
Avoid instanceof check on Element for prototype.js compatibility.  Fixes #7467 !strict
""",
u"""
fixes #7406 - whitespace and duplicate variable declaration in html._ContentSetter ... thanks bitranch!
!strict


""",
u"""
get a couple of bytes back.  [14917] !strict
""",
u"""
remove spurious debug(). !strict

""",
u"""
make sure that dojo.style() returns "bold" and not 700 for font weight queries on IE. !strict

""",
u"""
Fixes #7387, order of form elements off in dojo.objectToQuery, and My fix for 6821 dropped the erro.dojoType = cancel which caused xhr doh unit test to fail.
""",
u"""
Clean up returns statements !strict
""",
u"""
Adding a delay parameter to DnD (just like in Moveable). Fixes #7436.
Thx, Revin Guillen for the patch! !strict

""",
u"""
References #7441.  Proxy commit for haysmark.  
Remove security function.
Add delay parameter to doh.robot.scrollIntoView so its properly sequenced.
""",
u"""
add load and error syntactic sugar for NodeList, fixes #7330
""",
u"""
fixes #6765
""",
u"""
fixes #7330, dojo.NodeList doesn't support .onsubmit
""",
u"""
References #7398.  Remove xhr call to check for applet existence.
""",
u"""
References #7391.  Add robot.css import to test file.
""",
u"""
References #3486.  Proxy commit for haysmark.
Initial drop of robot testing enhancement.
""",
u"""
Allows successful no-content responses (like status 204) to be successful with the JSON content handler. fixes #6601
""",
u"""
Ensure that the first callback in the Deferred chain for an XHR operation (which processes the returned XHR data) prevents the received argument from being passed to the next callback.
""",
u"""
Fixes #7326 - account for padding and margin on the body when calculating position for onFirstMove
""",
u"""
Fixes #7324 - allow array-based items to also have array-based sub-items !strict
""",
u"""
update dojo.attr() to handle the case of innerHTML and style: {...} being passed in as values. Fixes #7305. !strict

""",
u"""
adopting Cornford optimization for dojo.delegate. Thanks to Neil for the patch. Fixes #7282. !strict

""",
u"""
Iterate over cloned listener arrays in case the original arrays are modified during event processing. Fixes #6165. !strict
""",
u"""
fixes #7063 - add an .at() method to NodeList to select small subsets of NodeList's as a new NodeList - cla on file for Schontzler, David ... thanks!


""",
u"""
dnd: removing some duplicated code. Thx, chucky! Fixes #7277. !strict

""",
u"""
Honor fractional:false for dojo.currency.format. Fixes #7091
""",
u"""
Fix for issue on Opera with Infinity as count value.  \!strict fixes #7269
""",
u"""
Fixes #7250: reuse previous response if no new response from callback. Thanks pottedmeat!
""",
u"""
fixes #7205. Ensures that we detect case sensitivity correctly on XML documents in FF and Safari when they're passed in directly as the root. !strict

""",
u"""
dnd: returning a context object from forInItems(). Thx, Max, for suggestion.
!strict

""",
u"""
Fix comment; 
""",
u"""
fixing _toArray() for DOM collections on IE. Fixes #7178. !strict

""",
u"""
fixed font-size for ie6/7, fixes #6755

""",
u"""
number parsing allows unlimited places when pattern is not provided explicitly.  Fixes #6536
""",
u"""
Allow ranges "n,m" for number formatting, for symmetry and to fix Spinner widget.  Fixes #4477
""",
u"""
Fixes #7233. Fixes dojo.io.iframe docs, and also adjusted dojo.io.script's docs to match.
""",
u"""
Add workaround to long-standing FF2 drag problem.
Thanks to jfcunat for the fix!
Fixes #6345 !strict.   #6350.
Also fixing duplicate id's in the test file (if you tried to drag "lettuce" it would think you were dragging "carrot").
""",
u"""
Fixes #6772: dojo.hasAttr busts when node doesn't have the getAttributeNode function
!strict

""",
u"""
Fixes #6957 (!strict): dojo.attr() does not handle "class" correctly on IE.
Perhaps we should be doing node.className rather than node.[gs]etAttribute("className", ..) but for now just doing minimal change to get unit test working.
""",
u"""
Fixes #7216 !strict.  Check for a valid node before calling dojo.isDescendant to avoid FF2 bug.
""",
u"""
Further patches to dojo._abs() for opera and FF2.
Fixes #6921 !strict
Patch from Mark Hays (IBM, CCLA on file).  Thanks!
""",
u"""
oops, put back response arg docs.  But can't response be an Error object or structured data?  Don't we need to be more descriptive?  Is there any point to using the function(...){} syntax, since it's not parsed and only makes this less clear? 
""",
u"""
Try to improve wording (please review) and add some TODOCs. 
""",
u"""
Fixing issue with revert. \!strict   fixes #7145
""",
u"""
!strict - Added check for previous version of Firebug. Should work well now with Firebug 1 and 1.2 - 1.1 is a bad and hard to find coe base, and should probably just not be supported./nAlso did a serious of minor tweaks to make this a little more jslint friendly. A little.
""",
u"""
Add docs for dojo.xhr args.  Only problem left is that IOArgs load, error, and handle property docs aren't showing up -- is function signature confusing jsdoc?  
""",
u"""
Fixes #7193 was not escaping a string in a certain condition when it was within an object !strict
""",
u"""
added a test case for dojo._toArray with DomCollection 

""",
u"""
Update tests to work with CLDR 1.6.  Provide loose parsing of 'a.m.'. 
""",
u"""
simplify IE8 check.  !strict
""",
u"""
use undefined for falsey results from dojo.isXxxx methods like dojo.isIE, instead of 0.  Fixes #7159, #7153
""",
u"""
ensure that cross-document xpath-run queries don't bomb out on FF3 due to new security restrictions. Fixes #7075. !strict

""",
u"""
ensure that cssText works as intended. Fixes #2855. !strict

""",
u"""
ensuring that we search cssText instead of the style property directly when doing string matches on attribute values. Fixes #7037. Tested on IE, FF, Safari, and Opera 9.5. !strict

""",
u"""
adding support for the ":checked" pseudo selector. Fixes #5179. !strict

""",
u"""
add case-sensitive searching to dojo.query() for XML document. Tested on IE, FF, and Safari. Fixes #3866. Fixes #5262. !strict

""",
u"""
Fixes #7157, corrects the docs in dojo.place !strict
""",
u"""
Fix variable name typo, !strict
""",
u"""
On Safari, fix "button" edge case in "setMarginBox". Fixes #7148. See also #5518. !strict
""",
u"""
Return {} if input to getComputedStyle is not Element. Fixes #6657. !strict
""",
u"""
Detect 'border-box' for 'input' tags of type 'button'. Fixes #5518. !strict
""",
u"""
Fixes #7146 - add a definition for a data attribute so that the parser will pass it in !strict
""",
u"""
!strict Removing some stray comments
""",
u"""
Fixes #6786. Introduces dojo.addOnWindowOnload and ties IE leak cleanup to that method. Allows file download links and javascript links to work in a page without destroying widgets. \!strict
""",
u"""
- updated patch by haysmark to fix FF3 and FF2 issues.  See ticket for details !strict
""",
u"""
Fixes #6588
!strict
Changed up the FB detection, based on whether the browser is FF or not. Couldn't test FB-1.1 because I couldn't download that version (getfirebug server problems).

Note, I didn't witness the problem in the ticket. It looks that FB-1.2 works with the old detection. I fixed it anyway.

Enabling Firebug Lite is different for FF3, now you disable Firebug, and Firebug Lite will install. isDebug turns it off. Backwards compatible for FF2
""",
u"""

!strict
Fixed: 
reversed brackets and curly braces
nulls in complex object tracing caused errors
left aligned all toolbar buttons
""",
u"""
Fixes to dojo._abs().  Working much better than before (works
correctly in most cases/browsers now, including test_Tooltip.html).
See ticket for details.  !strict
Patch from Mark Hays.  Thanks Mark!
""",
u"""
Update to CLDR 1.6.  Regenerate dojo.cldr.  Fixes #7113
""",
u"""
Fixes #6821: Preserve exception info in case where xhr.send fails. The original exception is accessible off the response.cancelResult property inside the handle(response, ioArgs) callback.
""",
u"""
Add mapping for 'he' locale to assume 'il' for country.  Fixes #7126
""",
u"""
Fixes #6744. Really just a problem with the comparison.  419.3 should be Safari2, anything greater Safari3 (for now).  Thanks, jgarfield.
""",
u"""
Fix to ComboBox.  
""",
u"""
style guide cleanup for hostenv_rhino, \!strict
""",
u"""
fixes #6393, prevent rhino from overriding any existing [set|clear]Timeout implementations, thanks Jordi Albornoz Mulligan for the patch, \!strict
""",
u"""
fixes #6919, performance optimizations in array loop code, thanks schallm
""",
u"""
Fixes #6909: xhr calls were not being aborted onunload in IE7 since typeof xhr.abort is 'object' in that case, and not 'function'.
""",
u"""
Fixes #5180: move gears detection out of Dojo Base. Now in a dojo.gears module. Tested change in FF3 with Gears, using dojox.off and dojox.storage demos. \!strict
""",
u"""
Fixes #7119: customBase now injects dojo._base dependencies. Includes standardCustomBase build profile that can generate the smallest possible dojo.js needed for dojo to work. dojo.js with that profile ends up at 13,690 bytes shrinksafed, 5,558 bytes gzipped. dojo.xd.js is 25,387 bytes shrinksafed, 9,101 bytes gzipped. Required a modification to dojo.i18n to trick the customBase regexps to get that dojo.xd.js size. \!strict.
""",
u"""
Expanded error callback documentation to reflect recent changes to try/catch behavior.
""",
u"""
merging performance patch from Tom to speed up _toArray calculations (which many NodeList operations spend much time in). Fixes #6722. !strict

""",
u"""
add information about what an error case is for the error handler for xhr
""",
u"""
Assume that value returned from script IO is UTF-8.
FF and Safari work this way already, but IE does not.
Fixes #6808.
!strict

""",
u"""
Fixes #7114: multiversion support for dojox.gfx/dojo.requireIf in xdomain loading.
""",
u"""
make sure xdomain warnings are really warnings. \!strict
""",
u"""
dnd: adding the autoSync option, and the AutoSource class, which utilizes it by default.
!strict.

""",
u"""
make sure console calls are still useful outside of built files that have the calls stripped.
""",
u"""
small try/catch error reporting cleanup.
""",
u"""
get script removing working with frameDoc, and also fixes a multiversion bug with a 'dojo' string reference.
""",
u"""
Supplementary tests for dojo._abs().
Unfortunately they seem to fail in one way or another on all browsers.
This should be converted to a DOH automated test.

""",
u"""
Make it clear that dojo.fromJson throws exceptions. Fixes #7082 
""",
u"""
Fixes #7052. the _listeners array was effectively a public, global value. Making it unique per dojo._scopeName. Reviewed change with sjmiles. Tested on IE 6. \!strict
""",
u"""
Redo logic to fake aliases. [14130] failed in a build. 
""",
u"""
DnD: adding selfAccept for copyOnly sources, thx, Revin Guillen! !strict

""",
u"""
Use UTCMinutes for timezones +:30  Fixes #7014
""",
u"""
DnD: added onDraggingOver and onDraggingOut local events, thx Revin Guillen!
!strict

""",
u"""
DnD: making the default creator to accept DOM nodes and process them
just like sync(). !strict

""",
u"""
DnD: adding missing methods, adding synch() method to synchronize DOM nodes
and the internal state of Container/Selector. !strict

""",
u"""
DnD: making sure that the creator always called in the context of
the container, basing the default creator on a parent node instead of
the container node. !strict

""",
u"""
DnD: adding selfCopy flag. Thx, Revin Guillen! Fixes #7051. !strict

""",
u"""
DnD: adding local events to sources: onDrop, onDropExternal, onDropInternal.
!strict

""",
u"""
DnD: adding a local event for a drag detection. !strict

""",
u"""
Fixes #6863. Only use try/catch in the djConfig.isDebug = false case. Otherwise, let the original exception escape to allow easier debugging. \!strict for _base/fx.js (error on line unrelated to changes for this ticket)
""",
u"""
Avoid rounding issue in dojo.date.difference by comparing Date objects with the same hour.  Fixes #6960
""",
u"""
Complete the comment. 
""",
u"""
Fix regression caused by [14023] so month names show up in dijit._Calendar again.  Fixes #7041
""",
u"""
Throw an exception when a DOM node is encountered in JSON serialization (fixes #6903)
""",
u"""
Throw an exception when a DOM node is encountered in JSON serialization (fixes #6903)
""",
u"""
Fix wipeOut() to also leave the overflow setting as it was before the effect started.
Fixes #6941.
""",
u"""
size saving patch from phiggins. Nice work. !strict

""",
u"""
some more byte scrimping. !strict

""",
u"""
getting even more miserly w/ the bytes. !strict

""",
u"""
clobbering duplicate code in JSON encoding block. !strict

""",
u"""
update docs and unit tests. Also ensure that scoping is correct in dojo.string.substitute() formatters. Fixes #6247. 

""",
u"""
updating inline docs, adding examples, etc. !strict (like most things in _base)

""",
u"""
Update dojo.cldr to use new generation scripts in [14022].  Fixes regressions seen with CLDR 1.5.  Fixes #6813
""",
u"""
Remove broken 'e' pattern char and unspecified 'L' and 'c'.  
""",
u"""
monster commit: - API change with deprecation. dojox.fx.easing is now called dojo.fx.easing, and all projects in dojox using
easing by default have been updated. API shim in place for dojox.fx.easing, just an alias and dojo.deprecated() which will probably have
to live until 2.0 (on pricipal, but is unnecessary in real life i think) ... 

also adds a default "fx" build profile I find myself using often

also updates chart2d events to use a more subtle easing function by default (still configurable), now using backOut as compared to elasticOut (which
looks choppy imho on small delta animations)

I _think_ I got everything, less dojoc/ -- so we'll have to do that separate.

just to be safe:
!strict


""",
u"""
dnd: adding the missing query restriction in the avatar, thx Bryan Forbes!
!strict

""",
u"""
removing crufty zoom setting code which is now rolled into dojo.style() for IE. !strict

""",
u"""
adding non-destructive filters updating for opacity setting. Also ensuring that we tickle the zoom bit. Also adding tests to ensure that we handle dojo.attr(node, "class", "..."); correctly. Fixes #6618. Fixes #6957. Fixes #6937. !strict

""",
u"""
Fixes #6940: tree items cutoff at right for tree wrapped in narrow div
Fixes #6941: dojo.wipeIn() leaves overflow:hidden on nodes

""",
u"""
Handle patterns which start with a literal at char 0.  Fixes #6915  Merci, Matthieu et Damien!
""",
u"""
Fixes #6928: fix parser so it handles empty arrays.
Patch from Jeff Balogh (CLA on file)
""",
u"""
dnd: fixes #6847, thx Revin Guillen! !strict

""",
u"""
dnd: fixes #6923 (bleeding events), !strict

""",
u"""
Fixes for cross-window widget creation.
Make sure not to create a node in one document but then insert it into another.
(Always use dojo.withDoc.)
Otherwise, IE gets upset.
Fixes #6791.
Thanks Masato! (IBM, CCLA on file)
!strict
""",
u"""
<link ... /> is invalid, should be <link ... > (unless you are writing XHTML).
#6887.
""",
u"""
<link ... /> is invalid, should be <link ... > (unless you are writing XHTML).
#6887.
""",
u"""
References #6879 !strict.  Fixed bad DOCTYPE.
""",
u"""
Uncomment nulling of preamble in delegate classes, viz Nathan's patch, fixes #6846. !strict
""",
u"""
Get xdomain loading to work for dojox.gfx. Requires a new loader function, dojo.loadInit() for this to work. Not my favorite, but it is the only robust option at this point.
""",
u"""
Extend "inherited" method in declare to use memoized prototype information when available instead of searching. Should improve speed of "inherited" and also fixes #6846. !strict
""",
u"""
Do not assume baseclass implements _findMixin. !strict
""",
u"""
dnd: special treatmeant of the right mouse button on Safari/Mac.
Fixes #6839. !strict. Thank you, Chris Mitchell!

""",
u"""
dnd: clean up in Container. !strict

""",
u"""
Updated _fixAttrName and hasAttr to deal with idiosyncracies of htmlFor and for attributes.  Created tests. !strict
""",
u"""
dojo.fx typo correction: fixes #6833. !strict

""",
u"""
Good catch.  Fix case to match 'standAlone'.  
""",
u"""
Doc typo, remove extra wording.
""",
u"""
updates for IE 6. 

""",
u"""
updating the overall font size to be 12px as discussed in the weekly full-team meeting. Fixes #6755

""",
u"""
Fixes #6727. Support a djConfig.addOnLoad option. Also updated API docs for djConfig.
""",
u"""
Removing an obvious error.  A file had two copies of its contents in itself.  Reference patch:  dojo.tests.patch 
""",
u"""
- typo


""",
u"""
Fixes #6539. Non-string uris (like dojo._Uri objects) cause problems with cacheBust. Thanks to schallm for pinpointing the problem.
""",
u"""
Fixes #6380. Forgot to account for json-comment-optional. Thanks to gregwilkins for tracking down the issue.
""",
u"""
Fixing some broken links.  
""",
u"""
Move Norwegian resources from 'no' to 'nb', to be compliant with latest ISO
specs. 1.1 branch. Fixes #6692 

""",
u"""
Fixes #6704: make internal call to _setValueOrValues instead of the API call setValues - to simplify extension of the class. !strict
""",
u"""
Fixes #6380. Applying patch from Kris Zyp to deprecate json-comment-filtered. Updated 1.2 release notes too.
""",
u"""
Fixes #6688. Allow spaces between provide and parenthesis. Also removed some redeclaration complaints coming from rhino strict checker
""",
u"""
Tweak to message.  \!strict
""",
u"""
Fix for unknown xml mime-type issue with IE.  Generic fix also fixes the file:// issue with xml files, but required minor UT change to not fail.  Test in question is a bit hokey to begin with, passing a fake xml DOM to the handler seems a bit .. odd (and doesn't really test much).  fixes #5388
""",
u"""
Adding in fatal error for a situation that cannot be worked around (as far as I understand what could be done with JS)  fixes #6562 \!strict
""",
u"""
Fixes #3242. Applies patch from Sam Foster. Removing weird IE WebControl logic that caused some race conditions with unload firing in IE. Updated test file to reflect test results.
""",
u"""
re-add a close button to Firebug Lite. Fixes #6680. !strict

""",
u"""
Fixes  #6358: xdomain loader did not handle module paths starting with /. Matching loader.js behavior and removing some cruft. \!strict for redeclarations (merge to trunk)
""",
u"""
References #6667 !strict.  Add new charOrCode member to key event object to simplify code, removing the need to check both charCode/keyChar AND keyCode when looking for specific keys.  Reviewed by sjmiles.
""",
u"""
Thanks for the great patch, Seth!  Fix regexps for ddMMMyyyy date parse.  Fixes #6242
""",
u"""
Fixes #5887: move afterOnLoad kickoff after the dojo.config.require work in dojo._base. (merge to trunk)
""",
u"""
Added in support for reload when close() is called.  fixes #6073 \!strict
""",
u"""
Fixes #6525: all xhr calls go through dojo.xhr now. Thanks to Kris Zyp for the patch. I applied it with a slight mod to the postData and putData detection. Nice patch that reduces the code footprint, thanks Kris! Also fixed an incorrect test.
""",
u"""
fix an accidental global reference in dojo.declare._extend, \!strict
""",
u"""
fix an accidental global reference in dojo.json
""",
u"""
fix a minor style guideline variation in firebug lite, \!strict
""",
u"""
fix an accidental global reference in firebug lite, and remove a redeclaration, take 2, \!strict
""",
u"""
fix an accidental global reference in firebug lite, and remove a redeclaration, \!strict
""",
u"""
fix an accidental global reference in dojo.data.sorter
""",
u"""
fix an accidental global reference in dojo.dnd.Avatar, \!strict
""",
u"""
fix an accidental global references in dojo.cookie, \!strict
""",
u"""
fix an accidental global references in fx, \!strict
""",
u"""
fix an accidental global references in dojo.html, and remove duplicate declaration, \!strict
""",
u"""
fixing mixing variable. !strict

""",
u"""
merging great Firebug Lite enhancements patch to add DOM inspection, kill memory leaks for good, and lay out objects more teresely. From Mike Wilcox of SitePen (CCLA on file). Fixes #6619. !strict

""",
u"""
Return undefined for JSON requests with HTTP Status 204, rather than throw, since it's successful by definition.  Fixes #6601  Fix typo in dojo.query comments and style of assignments in conditionals. !strict
""",
u"""
Updated documentation on dojo.io.iframe.send.
""",
u"""
Forgot to turn off the display of the iframe so I can inspect the contents.
""",
u"""
added a CDATA block to double check the test.
""",
u"""
Adds XML support to dojo.io.iframe; nasty but working hack on IE makes this go ok.
""",
u"""
Added dojo.string.rep(), which creates a new string by repeating
the argument string given number of times in logarithmic time.
dojo.string.pad() is reformulated to take advantage of the new function.
Fixes #6636.

""",
u"""
fixes #6614. makes trims that result in one character and have trailing whitespace work for dojo.string.trim
""",
u"""



""",
u"""
merging great patch from Liu Cougar for correctly handling the "3n-3" style of CSS selectors and fixing my broken logic on earlier selectors like "0n+1". Fixes #6418. !strict

""",
u"""
API clarification 
""",
u"""
fixes #4613 and #6544

""",
u"""
Group 1 and group 2 translations for Dojo 1.1.0.  
""",
u"""
Addition of preventCache into ItemFileReadStore.  fixes #6072 \!strict
""",
u"""
Fixes #6203. Patch and unit tests from doughays. IPv6 URL support.
""",
u"""
dnd: implementing the auto scroll for nodes. Fixes #1597.
""",
u"""
merging Sam Foster's html.set() patch + tests. We can close when ContentPane is refactored to use html.set() 

!strict

""",
u"""
Honor round option in format(). Fixes #6279
""",
u"""
roll back wipeIn changes. Don't need 'em and they were borking the dijit test pages. !strict

""",
u"""
remove spurious logging statements. !strict

""",
u"""
add more time to get the fx tests to pass on IE 6. 

""",
u"""
update timings to allow unit tests to pass on slower browsers (e.g., IE 6, etc.). Fixes #6330

""",
u"""
Make sure the attribute IDs are multiversion aware. \!strict
""",
u"""
fixes animation unit tests for Opera 9.2. Fixes #6325. !strict

""",
u"""
Remove connect.html, which is testing something that isn't supported.
General <script type="dojo/method"> and <script type="dojo/connect"> tests are in parser.html.
Fixes #6271
""",
u"""
update to ensure that re-setting an event handler via dojo.attr() correctly handles dis-connection. misc size reductions. The case where dojo.connect() sets a handler and then dojo.attr() sets one will NOT be handled. Updates to tests. Fixes #6310. Fixes #6234. !strict

""",
u"""
Fixes #6270: back-bookmark.html was not ported from the 0.4.3 codebase. Removing it for now, not sure if it is still relevant anyway.
""",
u"""
Clean up docs. !strict
""",
u"""
Clean up docs. !strict
""",
u"""
Clean up docs. !strict
""",
u"""
Clean up docs. !strict
""",
u"""
- who knew you could djConfig = { popup:true } ? this was broken in rc1, adding a test case to check for
regressions etc in rc2 / 1.1


""",
u"""
Clean up docs. !strict
""",
u"""
Clean up docs. !strict
""",
u"""
update docs and default behavior for dijit.Form and dojo.attr to make it crystal clear that unified Dojo event handling is in play when using event handlers specified by dojo.attr() and that browser-specific hacks may no longer work as expected. Fixes #6280. !strict

""",
u"""
Allow multiversion support. \!strict
""",
u"""
dnd: fixes #6273, thx haysmark!
""",
u"""
Fixes #6274. Removing this test: it was for #744, but that is marked as wontfix.744
""",
u"""
merging adam peller's patch for infinite loop catching. Fixes #5961. !strict

""",
u"""
updating code and docs to enable the addOnLoad(obj, function(){}); style which other dojo APIs handle. Some work to reduce code size as well. Fixes #5404

""",
u"""
ensure that we don't blow up on Safari 3.1. Fixes #5832. !strict

""",
u"""
make the console detection code smaller. Fixes #6255

""",
u"""
make the bootstrap use built-in console.log if there is one in order to print out debugging output. Useful on Safari and Opera. 

""",
u"""
clean patch for #5617 that avoids timer for all but IE 6. Fixes #5617. !strict

""",
u"""
Apparent typo in docs for dojo.delegate \!strict
""",
u"""
References #6245.  dojo manual testing front-end.
""",
u"""
Improve djConfig docs.  
""",
u"""
Add hypertext link to docs.  !strict
""",
u"""
seems focus()/blur() isn't synchronous on IE. Adjust test accordingly to get it to pass. Fixes #4811

""",
u"""
use Firebug Lite in popup mode when debugging NodeList-fx stand-alone. 

""",
u"""
fixes dojo.style() calculation of computed heights on IE 6 when node.style.height = "auto" is set explicitly. Skip deprecated getBoxObjectFor() call for FF3 for performance and forward-compat. All unit tests run on IE 6, FF3, and Safari. Fixes #6143. !strict

""",
u"""
dnd: removing the garbage, 
""",
u"""
dnd: adding missing dojo.depricated(), 
""",
u"""
dnd: minor cleanup. 
""",
u"""
Don't duplicate dojo.cookie !strict
""",
u"""
fix cookie props doc. !strict
""",
u"""
update query() to move combinator-rooted queries off to a non-querySelectorAll branch until the webapis WG decides that they're the right thing to do (which they clearly are). !strict

""",
u"""
Somehow the window/document check didn't make it in !strict
""",
u"""
merging pottedmeat's history, object printing, and recursion changes. Fixes #6166. !strict

""",
u"""
minor doc formatting update. !strict

""",
u"""
query tests probably shouldn't be using debugAtAllCosts. 

""",
u"""
removing crufty dojo.back options which are no longer necessaray now that we've changed dojo.back to use an explicit init() method. 

""",
u"""
Fixes #6119. Make sure only do Jaxer server stuff if we are on the server. Thanks pottedmeat. \!strict for redeclarations
""",
u"""
fixes #5634. !strict

  * If the property is a color, just pass its value through to get created into a dojo.Color later on.

""",
u"""


  * bzr-svn added some bzr: props to the trunk of dojo.  Removing.

""",
u"""
fixes #5884.

  * Because of daylight savings time, changed one of the hour add tests to add an actual hour of milliseconds to the start date to get the target date.

""",
u"""
dnd: clean up stray naked dojo.query() statements. !strict
""",
u"""
dnd: removing unused debugging code (rather minor problem). 
""",
u"""
dnd: adding moving "relative" objects. Updated the existing test
to include a relative moveable. Fixes #6136.
""",
u"""
dnd: removing an unnecessary comment. 
""",
u"""
update form processing to work on IE. Fixes #6113. Updates test page and docs in dijit.form.Form as well. !strict

""",
u"""
dnd: removing dojo.marginBox() calls from all places in the DnD package,
adding new TimedMoveable class, added a test for the new class.
Thx Douglas Hays for the idea of fps throttling on move, and for the
initial patch. Fixes #6132. Fixes #6133.
""",
u"""
fix deferredList. fixes #5899 and adds test file. thanks tvachon
""",
u"""
pad milliseconds field. Fixes #6118
""",
u"""
Fix currency constraints docs.  !strict
""",
u"""
Add CurrencyTextBox constraints docs.  !strict
""",
u"""
Append //@ to buffer for debugging only for Gecko-based browsers. Fixes #5901
""",
u"""
Fixes #5372. !strict
""",
u"""
ugg. Fingered the wrong test file when checking in [12899]. !strict

""",
u"""
adding sugar to dojo.attr(), and therefore to it's mapping into dojo.NodeList. Expanding tests and docs. Supports a property-bag style for attrs the same way we do with dojo.style(). !strict

""",
u"""
- show query().style() example in dojo.style() and document common pitfall.
!strict

""",
u"""
Check the day of the month of the PST-defined date in UTC time, since the local day will vary with timezone.  Fixes #6079
""",
u"""
Must pass calling context on event handler through to event fixer to locate the correct currentTarget and window.event. Fixes #6069. Fixes #6050. !strict
""",
u"""
clobbering crufty djConfig values, adding docs for the stuff we actually use on a regular basis, and updating DOH to give us better command-line info. !strict

""",
u"""
Improve docs and markdown. 
""",
u"""
Improve docs and markdown. 
""",
u"""
Doc function param. 
""",
u"""
Allow dojo.io.script to use a child iframe. This gets the basics in there, and leaves the higher order issues of setting up the iframe to the user. Still need to document it. Ideally also show an example, but that might take longer.
""",
u"""
Fixes #6050, make sure to clear _stealthKeydownHandle, so key listener can be reconnected later.[[br]]
Fixes #6063, use new Function() to generate "pure" (closes over nothing) functions.
!strict (return value complaints)
""",
u"""
Correct kwArgs doc declaration, plus some other doc fixups.  !strict and r12790
""",
u"""
Update djConfig params
""",
u"""
Remove parameters, they confuse people !strict
""",
u"""
and r12827. Make sure that nested lists are properly nested !strict
""",
u"""
and r12824. Properly type the browser detection variables !strict
""",
u"""
and r12821. Instance variables won't show up in docs if there are no instance variables. !strict
""",
u"""
and r12790. Update markdown and pseudo-args
""",
u"""
comment cleanup and code shortening. Also expanding test cases to handle default param packing. !strict

""",
u"""
update core documentation for query, re-enable the query optimizer, update misc docs around the rest of dojo.js as well. !strict

""",
u"""
fx: Fixes #5539. !strict

""",
u"""
fx: fixes #6018. !strict

""",
u"""
update documentation for browser detection variables. !strict

""",
u"""
updating inline documentation for the bootstrap. !strict

""",
u"""
make sources configurable through passed properties for *all* attributes. Update and clarify docs. !strict

""",
u"""
Fix strict mode checking of year < 100CE in dojo.date.parse. Also remove unsupported whitespace tests and invalid 'es' locale tests. Fixes #5885
""",
u"""
shorten NodeList code, add toggleClass(), and update documentation. !strict

""",
u"""
inline doc cleanup for the default loader. !strict

""",
u"""
initial jaxer support. The oncallback() usage of Jaxer does not work yet, but the normal page request version does. \!strict for dojo.js
""",
u"""
References #5562.  Add timer to Moveable to reduce calls to dojo.marginBox to help IE performance.
""",
u"""
lastIndexOf() was totally borked. This fixes, rolling back changes from r10203. !strict

""",
u"""
Updates to the animation system and a new convenience method. Fixes #5985. !strict

This checkin provides:

	* a simpler syntax for dojo.animateProperty() property specifications when only the end value is wanted
	* a new dojo.anim() method which simplifies animating a single node immensely
	* changes the default animation period to 350ms (down from 1000ms). A full second feels like forever in most transitions.
	* updating tests for animations and expanding to cover dojo.anim()
	* adding an anim() method on dojo.NodeList objects via the dojo.NodeList-fx extension
	* Adding tests for dojo.NodeList-fx

All tested on IE 6, Firefox, and Safari


""",
u"""
Use markdown, kwargs in docs. 
""",
u"""
add more descriptive error message for onload failure. 
""",
u"""
Moves smd v1 yahoo from dojox.rpc to dojo.tests.resources for its continued use as the test smd for JsonpService. fixes #6020
""",
u"""
Minor fix.  
""",
u"""
Markdown any problematic HTML !strict
""",
u"""
Revert marking code as code !strict
""",
u"""
Mark code as code !strict
""",
u"""
Ok, it really was JavaScript 1.6, despite the misleading URLs.  
""",
u"""
cleanup docs for fx functions. Add some more examples. !strict

""",
u"""
Avoid infinite loop in indexOf. Fixes #5961
""",
u"""
fixes #5569, NodeList.connect documentation wrong
""",
u"""
Fixes #5801. Send X-Requested-With: XMLHttpRequest header with dojo.xhr calls, to match behavior of other libraries.
""",
u"""
previous fix is not so good: means that svn source usage of dojo.js will load dojo.i18n by default. Backing out that fix.
""",
u"""
Incorporating fix, but can't take test case w/o cla. 
""",
u"""
Add Wolfram's test case for string callbacks.  Fixes #5905.  Had to modify exception test since error string seems to vary across browsers.
""",
u"""
Better, but still not great, definition for dojo.data. 
""",
u"""
_base/test_FocusManager.html "restore focus" button failing.
This gets the code working on IE and FF, but not Safari...

The focus API tries to be clever, and (in this example)
saves not what is actually in focus (ie, the save button itself), but what was
in focus immediately before the save button was pressed.   That code fails on
Safari since the save button never gets focus.  Need to rethink or desupport this API
since I suspect the current code will fail on IE/FF if it's called
when nothing is in focus: it will save whatever used to be in focus, even if that
was 10 minutes earlier.  Will rethink for 2.0.

Patch partly from Nicola (CLA on file)
""",
u"""
Fixes #5576: allow args.form for dojo.io.iframe.send() calls to be a string that uses dojo.byId to find the node. Thanks rcgill for pointing out the API inconsistency.
""",
u"""
Gets opera to work after page load in xd situation. Opera was downloading modules as part of the dojo.config.require section, which happened before dojo.i18n was downloaded in the xd case. Switch to using nifty conditional include build comments so we can load dojo.i18n for dojo.xd.js before the dojo.config.require section runs in _base/browser.js \!strict
""",
u"""
Typo. Fixes #5946
""",
u"""
Apply Mike Wilcox's firebug patch.  7 up.  Fixes issues with Safari, popup blocker, resizing. Adds cookie support to remember position and size.  Fixes #5922 !strict
""",
u"""
Update pseudo-classes !strict
""",
u"""
Fixes #2172. Edited summary lines that started with a parameter name.
""",
u"""
Fix IE crash (thanks Mike Wilcox), change deprecated/experimental to console.warn.  Fixes #5490  !strict
""",
u"""
Fix up comments to match signatures, show multiple types on arguments and document their behavior, use common naming of parameters.  
""",
u"""
Fixes #4908 (thanks Bill). !strict because the pre-commit hook is confused about return types.
""",
u"""
adding NodeList.onfocus(). !strict

""",
u"""
Years < 100 are not supported.  Pad years < 1000 when formatting.  Fixes #5751
""",
u"""
updating isFunction w/ same error handling as isArray has for null being passed on IE. !strict

""",
u"""
silly IE6... Fixes #5910. !strict

""",
u"""
fix dojo.isString() for IE to correctly handle cases where "" is passed. Fixes #5910. !strict


""",
u"""
Cleaning up documentation !strict
""",
u"""
applying patch from Mike Knapp for a really janktastic IE issue when using MSHTML in embedded environments. Fixes #5904. !strict

""",
u"""
Fix typo, fixes #5897. Thanks tvachon
""",
u"""
ensure that animations which end "naturally" decrement the timer and attempt to cancel the global interval if apropos. Fixes #5662. !strict

""",
u"""
Introduces djConfig.afterOnLoad: if set to true, then dojo._loadInit will be fired after a 1 second timeout. Using a shorter timeout (100ms) had problems where the dojo._loadInit was fired before all modules were downloaded. That seemed odd given the synchronous XHR calls. Also because of a bug in the dependency mapping stuff, had to rearrange how _base.js is organized. Testing on supported browsers looks good, although Opera in the xdomain case seemed to have a problem. Still need to investigate that a little more, and then write up release notes on the djConfig option.
""",
u"""

""",
u"""
merging instantiate() patch. Needs tests.

""",
u"""
- it doesn't actually appear to be broken (the ticket claim) though new unit test
introduce new issue: onEnd is fired twice (or more?) for chained and combined animations.
unit tests pass, but you will see a console.warn() you should otherwise not.


""",
u"""
Fixing one frequent case of dragging table rows without specifying
a creator. Fixes #5823. !strict
""",
u"""
Making sure that _fire() gets an array argument.

Fixes #5866.
!strict

""",
u"""
Renaming onBeforeBegin => beforeBegin.

Adding animation of an internal animation (bug).
!strict

""",
u"""
- the onEnd tests for chain/combine work, but beforeBegin and onPlay never fire. 
needs attention.


""",
u"""
Fixes #5857, #5860: dojo.coords() wasn't accounting for borders an ancestor nodes (safari bug only) !strict
""",
u"""
remove useObject, since it's really a one-liner for the developer.  Fixes #5810. reduce some code.  use expires to remove test cookie. !strict
""",
u"""
Fixes #1704: using DOMContentLoaded now for Firefox 3, since the hang bug is now fixed (as tested in FF 3beta3).
""",
u"""
Fixes #5838: allow console to work with xhtml documents. \!strict
""",
u"""
drop base size a bit. 

""",
u"""
Don't need to seed cache with width/height. !strict
""",
u"""
One more time... don't assume pos=0 !strict
""",
u"""
Remove wildcards in toStyleValue regexp.  Still just as accurate as it was before. !strict
""",
u"""
Reduce toPixelValue with a regexp, remove redundant return statements. !strict
""",
u"""
more accurate detection of WebKit, Safari, etc. Un-breaks the editor. Fixes #5575. !strict

""",
u"""
update dojo.query to defer to [node].querySelectorAll() if it's available. Fixes #5832. !strict

""",
u"""
update dojo.style() inline docs with examples. !strict

""",
u"""
update dojo.style() to accept a style bag as the second param and ensure that the mapping in dojo.NodeList is smart enough to handle it. Add and update tests. Fixes #5511. !strict

""",
u"""


 * The bane of Torrey's existence is now fixed
 * FadeArgs will now show up properly in docs
 * !strict

""",
u"""
fixes #5252 - sanity check on _started for _Widget


""",
u"""
Missed reference in reduction. !strict
""",
u"""
Use regexp to find cookie contents. (thanks, Pat) Fixes #2881.  Correct docs on deleting cookies.  Fixes #5782 !strict
""",
u"""
Fixes #5781 !strict.  Boolean attributes need to use the javascript value instead of the DOM attribute in dojo.attr.
""",
u"""
update Dojo's Safari detection to use WebKit tech versions if explicit Safari versions aren't available. Fixes #5575. !strict

""",
u"""
Fixes #5767 (debugAtAllCosts working with dojo svn source) and #2904 (attaching cacheBust parameter inside of dojo._getText -- this allows dijit templates to be updated on reload if you set up djConfig.cacheBust correctly). \!strict
""",
u"""
adding support for Adobe AIR. Thanks to SitePen and Adobe for these excellent patches. Tests in next commit. !strict

""",
u"""
goofed on the closure variable for dojo.
""",
u"""
expand docs for registerModulePath(). 

""",
u"""
Accidentally committed this file. Reverting it.
""",
u"""
Fixes #5420. Allow other HTTP methods. To do a HEAD call: dojo.xhr('HEAD', args)
""",
u"""
Fix comment typo.  \!strict
""",
u"""
Fix to ItemFileWriteStore for reversion bug.  \!strict
""",
u"""
Fixes #5732. Allow other non-word character terminators like \; for dojo url.
""",
u"""
Always format as 4-digit year in dijit.form.DateTextBox, but continue to allow 2-digit year input where appropriate.  !strict
""",
u"""
Unnecessary to check year overflow in parse.  
""",
u"""
throw for bad json. 
""",
u"""
Fixes #4573: Removed the path remapping in loadModule, since it messed up the ability to make your own namespace for dojo, but add your own code to it outside the dojo directory. Also finished book documentation.
""",
u"""
Fix regression from [12198] - must convert hours to a number for comparison.  
""",
u"""
get debugAtAllCosts to work with scope changes.
""",
u"""
remove deprecated argument juggling in declare.js.  style fixes. !strict  
""",
u"""
another small reduction. 
""",
u"""
reduce the bounds checking code. 
""",
u"""
build the Date object at the end, not as we go along.  The setters on Date seem to have a bunch of issues.  Calling the Date constructor once is more reliable and probably more performant.  Also, use 1970 as the default year.  Fixes #5716, #5680
""",
u"""
fix lowercase map to pass i18n/date unit tests. 
""",
u"""
dnd: minor cleanup (switching to dojo.deeclare for the sake of uniformity)

""",
u"""
Update copyrights to 2008.  Thanks to doughays for reminding me :)  
""",
u"""
Convert to dojo.config instead of djConfig internally. \!strict
""",
u"""
Moving scope tests to own directory, adding a djConfig burn in test.
""",
u"""
Modify API doc of dojo._abs() to match behavior on FF.
Modify behavior of dojo_abs() on Safari3 and Opera9 to match behavior on FF.
This fixes popup positioning on safari (fixes #5295).
html.js unit test still passes.
Tested on FF2, FF3, Safari, IE6.
!strict
""",
u"""
Fixes #5631 !strict.  Add explicit test for boolean and function types in dojo.attr.
""",
u"""
Moving scope tests to their own directory
""",
u"""
fixes #5460 - makes public method fire() private (_fire) because you should never ever call it.
also changes the return value of stop() if called on a non-running animation, so if you were 
relying on undefined coming back, you can now reliablly chain .status() on .stop() instead ...
fixes #5611 - some d = dojo love cleanups included
!strict

""",
u"""
- tiny tiny cleanup to parser, and note on usage of dojo/method dojo/event


""",
u"""
dojo.fx: new versions of dojo.fx.combine() and dojo.fx.chain()
based on Bryan Forbes' patch. Minor cleanup, new fx test.
Fixes #4083. Thank you, Bryan!
""",
u"""
Fixes #5620 !strict.  Added support to dojo.attr for boolean attributes on Firefox.
""",
u"""
Added tests for combine and chain.  

""",
u"""
Treat 2 year dates as 4 year dates, regardless of the pattern for strict=false.  
""",
u"""
Fix dojo.coords() on FF to account for borders  (rather than returning the content box).  Fixes #3222, #3676, #5541.  !strict
""",
u"""
- ugly (safe) patch moves closure up to top. precedes coming patch to do other cleanups, that otherwise
would be unreadable with this patch included.
!strict

""",
u"""
References #5607.  Added function attribute support to dojo.attr. !strict
""",
u"""
build results of new cldr 1.5.1.  Fixes #4503
""",
u"""
isDisabledDate should compare date portion only.  DST bug?  Fixes #5595 !strict
""",
u"""
oops.  default for date should be 1, since dates are 1-index based.  
""",
u"""
putting in scope changes. Say hello to _scopeName for string IDs. \!strict
""",
u"""
some reductions (=== undefined) and style mods.  
""",
u"""
ensure that the position default is actually respected. Fixes #5542. Adds better docs. !strict

""",
u"""
Small code simplification for dojo.hasAttr(). !strict
""",
u"""
GB weeks start on Monday. Fixes #5533
""",
u"""
Updated to ItemFileReadStore and ItemFileWriteStore to enable reference integrity.  fixes #4552 \!strict
""",
u"""
change styles to style
""",
u"""
fixes #5473 !strict
""",
u"""
fixes #5506. When query() is called without any params, the source list should be passed back. !strict

""",
u"""
Fixes bidi in quirks mode (thanks, makin) Fixes #3721 and backs out change from [11944] Plus some size reductions.  !strict
""",
u"""
Correct DnD/dropdown bidi placement.  Fixes #4369, #4228.  Also some size reductions. !strict
""",
u"""
put global funcs in local scope. fix b0rken array logging.  Fixes #5489  !strict
""",
u"""
Some code reductions. Fixes #5375.
""",
u"""
so it seems right to revert this to [10980] unless there's a reason not to.  Fixes #5464 !strict
""",
u"""
fixes #5464 - updating dojo.isDescendant to return false on error !strict
""",
u"""
handle undefined/null correctly when outputing them in console (!strict)
""",
u"""
Fixes #5091: debugAtAllCosts including files twice in the head.
""",
u"""
fixes #5452 (!strict, warning from exsiting content)
""",
u"""
Fixes #5408. Useless percent, thanks to peller for the catch.
""",
u"""
Updated test to explicitly check for failures with Boolean coercion - Invalid month/day names on parse now return null. Thanks, Doug.  Fixes #4864
""",
u"""
re-enable :contains, expose the pseudo-match list to extension through dojo.query.pseudos, and enable sibling selectors (and tests for them). Fixes #5022. !strict

""",
u"""
Fixed up the _base/html.html unit test file to pass on Opera 9. I disabled some tests that cannot pass (tabindex="-1"). 
""",
u"""
Minor doc fix. !strict
""",
u"""
Added new API for getting and setting HTML attributes: dojo.hasAttr(), dojo.attr(), and dojo.removeAttr(). Fixes #5055. !strict (errors outside of my changes)
""",
u"""
Fix xhr unit test for json pp change.  Also, reduce json code some more.  
""",
u"""
fixes #5421
""",
u"""
Fix unresolved reference 'url'. 
""",
u"""
repair encoding regression in [11732] and add test cases.  Fixes #5415
""",
u"""
Fix regex for removing opacity FILTER() clause when opacity==100%.  Fixes #5371, 
""",
u"""
put onload trigger in try/catch so a failure doesn't kill the bootstrap. 
""",
u"""
Fix for a fat-fingered typo caused by #5399, 'iobject' instead of 'object'.  
""",
u"""
fixes #5399, firebug lite support to catch xml documents
""",
u"""
fixes #4969 - went with dojo.cookie.useObject (get/setObject combination? - contemplated asObject, and others. change if
inappropriate) ... adds test to and enabled the cookie doh test. couldn't figure out a simple simple way to drop
useObject functionality into dojo.cookie without mini refactor. 


""",
u"""
Fixes #5367: dojo.isSafari was not reporting 2 if using Safari 2. (merge to trunk)
""",
u"""
Minor defect fix + UT.  fixes #5357
""",
u"""
Adding Date object support to dojo.clone(). Fixes #5284.

Added tests for dojo.clone().
""",
u"""
Fix doc typos. 
""",
u"""
fixes #5335.

  * Changed _Animation to check the _percent property rather than the step in the _cycle function to allow overshooting in an easing function.

""",
u"""
Allow mouseless start of DnD. 

The DnD can be started by dojo.dnd.manager().startDrag() without
recording what mouse was pressed to start it. This fix allows this
scenario.
""",
u"""
More compact revision match. 
""",
u"""
Fixes #5332.

""",
u"""
xml response handler - can't return out of a dojo.forEach, and prefixes was undefined.  Fixes #5320  Also, make objectToQuery shorter and faster.
""",
u"""
fixes #5276. fixes #5315.

  * Changed dojo.date.add to only use the setUTC/getUTC on intervals less than or equal to an hour.

""",
u"""
fixes #5313
""",
u"""
Minor patch.  fixes #5307
""",
u"""
Fill in missing summary.  
""",
u"""
- package level sup docs for dojo

""",
u"""
Move singleton docs inline, where possible.  Fill in some missing summaries.  
""",
u"""
Fix typo. Fixes #5291
""",
u"""
Reporting the overSource event only for the current source. Fixes #5268.
""",
u"""
Implemented /dnd/drop/before topic. Fixes #5266.
""",
u"""
Add final Greek strings.  Thanks again, Dionysios.  Fixes #5205
""",
u"""
Fixes #4325 on trunk: typo in safari version number about messing up dojo.abs() and thus drop down/popup placement
""",
u"""
Fixes #5174. Remove 100 multiplication from gotoPercent
""",
u"""
updated translations. 
""",
u"""
Fixes #5131. Make sure if trying to access parent frame, catch any exceptions and eat them. This is important if the iframe is on a different domain than the parent frame. (Checkin for trunk)
""",
u"""
- add common blank.gif file to dojo base


""",
u"""
Fixes really old regression in add weekday routine.  Thanks, Bryan for catching this.  
""",
u"""
trac svn hooks fixed.  fixes #5067
""",
u"""
test commit 
""",
u"""
test commit 
""",
u"""
clobber spurious debug calls. 

""",
u"""
Bryan's patch to fix DST problems. 
""",
u"""
dnd: fixing missed renames. Fixes #4934.
""",
u"""
introduced an error just prior to cutting 1.0 in an effort to debug iframeio for Safari 3. Fixes #5021

""",
u"""
updating Safari version detection code to give us a real major version number. Using that update to ensure that we get/set iframe properties correctly in dojo.io.iframe. Fixes #5012

""",
u"""
doc updates to ensure that we capture the optional property bags correctly. 

""",
u"""
update for dojo.cookie() docs. 

""",
u"""
comment formatting cleanup. 

""",
u"""
clean up doc formatting. 

""",
u"""
minor doc formatting updates for readability. 

""",
u"""
minor formatting updates. 

""",
u"""
documentation updates. 

""",
u"""
documentation updates. 

""",
u"""
minor doc updates and formatting for debugging. toJson() no longer tries to handle DOM nodes. Fixes #4186

""",
u"""
minor doc update. 

""",
u"""
minor doc updates. 

""",
u"""
Documentation updates

""",
u"""
Documentation updates

""",
u"""
dnd: reflect changed capitalization of some DnD files. Fixes #4430.
""",
u"""
dnd: re-adding files back with the correct capitalization. 
""",
u"""
dnd: temporary removing two more files to change their case. 
""",
u"""
dnd: re-adding files back with the correct capitalization. 
""",
u"""
dnd: temporary removing files to change their case. 
""",
u"""
good spot by Neil. Clobbering stray global. 

""",
u"""
No reason to put intermediate delegates into any namespace. Prefer simply removing this code. 
""",
u"""
Cleaning up documentation

""",
u"""
Update documentation
""",
u"""
Fixes #4978. Remove duplicate mousemove, and reorder names alphabetically.
""",
u"""
Couple UT.  fixes #4931
""",
u"""
fix rpc so it can accept (convert) a dojo._Url object when passed this as its parameter.  Cleaner solution to the last checkin's little test hack.  Fixes #4750
""",
u"""
update documentation and fix a few minor bugs like comments in the yahoo smd causing the tests to fail. 
""",
u"""
add inline docs for DeferredList. fixes #3499
""",
u"""
Try to avoid the user from hitting a bundle loading error case.
""",
u"""
Format the kwArgs docs for IO methods so they show up nice in the parsed docs.
""",
u"""
they're not wrong, they're just in need of some love. 
""",
u"""
requireInto is not ready for prime time yet. In particular, it will not work with xd loading. Removing for now, to help reduce base.
""",
u"""
fix up docs a bit. 
""",
u"""
fixes editor drop-downs. 

""",
u"""
clean up doc formatting and a bit of structure. Also some code size reductions. 

""",
u"""
go with "example" instead of "usage". 

""",
u"""
keep declare() from leaking stray globals when there's no superclass. Updating docs for parser conformance. 

""",
u"""
keep "pStart" out of the global namespace. 

""",
u"""
minor nits. I'm still very unhappy about how much space the gears detection code takes up.

""",
u"""
updating inline docs such that they get picked up by the parser. 

""",
u"""
add back in docs for deprecated() and experimental(). 

""",
u"""
make dojo.delegate public and add docs. 

""",
u"""
docs for dojo.loaded and dojo.unloaded. 

""",
u"""
ugg. I keep forgetting to re-enable the query optimizer! 

""",
u"""
cleaning up a stray debugging call, removing the non-standard ":contains" selector, fixing ":empty", and adding tons more unit tests. 

""",
u"""
updating for removed "!=" selector in dojo.query. Also, size reductions. 

""",
u"""
allow colons in IDs, names, etc. Fixes #3520

""",
u"""
Fixes #4938. Removing .* to __package__.js support.
""",
u"""
make the bootstrap smaller through scope protection closures now that the doctool is picking everything up. Big props to Neil for making this possible (and safe). 

""",
u"""
make sure we get animations to combine. Fixes #4924

""",
u"""
Might as well clean up comments as well
""",
u"""
After more looking, I don't think you can do jsonp comment filtered.  So reverting #4888.  
""",
u"""
Committing in minor enhancement for RPC.  fixes #4888
""",
u"""
oops. remove commented out code. 
""",
u"""
Fix bugs in _containsValue - wasn't searching the whole list.  Use dojo.some.  use toString() for regexp match on primitives.  Still needs UT.
""",
u"""
make direct descendant selectors more robust when they occur at the end of a selector. Fixes #4364

""",
u"""
re-enable query optimizer. 

""",
u"""
complete replacement for the tokenization strategy of the query engine. Moved from ad-hoc substring searching to an AST generation/consumption system. The query engine should be significantly more robust in the face of whitespace and funky formatting than before. Code size change should be minimal despite the large-scale change. Expanded tests and a first stab at inline docs for dojo.query. All unit tests pass on FF2, Safari3, and IE 6 and 7. Fixes #4365. Fixes #4640. Fixes #2423.

""",
u"""
ensure that if we're in an iframe and the parent has a console that we use it instead. 

""",
u"""
I give up. Put back the indexOf searches for comments in place of regexp attempt.  #4829, #4888  Reverts part of change in [10834]
""",
u"""
Rename NodeList extension to reflect fx additions.  
""",
u"""
minor doc update. 

""",
u"""
expanding documentation and reducing file size for dojo.NodeList. 

""",
u"""
tests for slice/splice. Splice isn't working correctly on IE 6 yet (still digging). 

""",
u"""
making the constructor smaller ('cause we can), adding slice/splice, and moving animations out to dojo.NodeList-ext. Fixes #4822

""",
u"""
adding first extension file for dojo.NodeList. 

""",
u"""
Updated examples and descriptions that use code to work with tomorrow's API tool update.

""",
u"""
When formatting time only, do not include a timezone.  Fixes #4879
""",
u"""
Test for unmatched substitute. 
""",
u"""
- minor doc changes in html.js (can't start a line with 'returns') and adds in more verbose "description" vs "summary" in a few places.


""",
u"""
add spacing for Safari. Fixes #4325

""",
u"""
usage -> examples. 

""",
u"""
dnd: constraints implemented with special Moveables instead of Movers, 
""",
u"""
dnd: partial refactoring of dnd.move, which preserves the old API, but provides new facilities, 
""",
u"""
removing unused exactOnly argument to dojo._loadModule()
""",
u"""
dnd: modified the behavior of the drop in case of moving items withing a source, fixes #4585, thx sarkasm for the suggestion.
""",
u"""
dnd: implemented optional drag handles for DnD items, added a test demonstrating the usage, fixes #4840, thx manishaNC for the suggestion.
""",
u"""
dnd: propagating changes from DnD to Moveable, 
""",
u"""
dnd: propagating changes from DnD to Moveable, 
""",
u"""
dnd: missed one place the first time around, added a test for start/stop events, fixes #4799.
""",
u"""
removing a stray global in the test. 

""",
u"""
clobbery stray global "param" name. 

""",
u"""
clobber the "gearsObj" stray global. 

""",
u"""
dnd: fixes #4673.
""",
u"""
dnd: fixes #4140, thx blowery for the enhancement suggestion.
""",
u"""
ensure that combinations return a wrapper animation. Also, move all animations to be keyed on a single timing loop for smoother animations when mutliple animations are joined (as in dojo.fx.combine()). Fixes #3477

""",
u"""
Fix regexp for json comment filtering to accept multilines.  Fixes #4829
""",
u"""
Minor fix to squelch warnings,  refs  #4829
""",
u"""
ensure that dojo.query passes back a node list if it's inadvertently passed in. Fixes #4825

""",
u"""
Fixes #4821. Fixes #4378. Now NodeLists are just arrays augmented with extra methods. splice() and slice() are still oddballs, but will be fixed shortly (in the same manner).

""",
u"""
output something saner for most object types. Fixes #4823

""",
u"""
updating docs to note string args. Thanks to ptwobrussell and phiggins for staying on me about it = )

""",
u"""
make sure we're accepting string args for the dojo.*Class methods. 

""",
u"""
In a build, an exact match is required for locale.  Fixes #4814
""",
u"""
fixes #4818
throw new Error("newItem() was not passed an identify for the new item");

corrected to:
throw new Error("newItem() was not passed an identity for the new item");
""",
u"""
make sure that exceptions and such don't fake IE out WRT base URL. 

""",
u"""
dnd: typo fix --- fixes #4799, thx jbondc for bring it to my attention.
""",
u"""
make the console usable on IE 6. 

""",
u"""
fixes #2352

""",
u"""
re-enable onMouseEnter/onMouseLeave, but this time with some smarts about FF's bugs. Fixes #4307

""",
u"""
catch the exception in json comment filtering. 

""",
u"""
merging patch from jonu to allow custom errors in Deferreds. Very useful. Fixes #4337

""",
u"""
Fixes initial state storage by using normalized getHash function, scopes safari2 history hack, speeds up checkLocation just a tick
""",
u"""
Fixes #4777. Consistent hash handling and test cases added to dojo.back
""",
u"""
Fixes #4647. Comment out calls to console, except for diagnostic call for x-domain.
""",
u"""
Perhaps this is slightly better. 
""",
u"""
sorry, didn't understand the original bug report.  How's this? (probably close to where we started)  Fixes #4744
""",
u"""
Fixes #4741. Reduce timer to 200ms, matching 0.4's impl
""",
u"""
D.O.H. uses clearTimeout as well as setTimeout. Support both. Fixes #4621

""",
u"""
it's not a problem with date, and the validation tests pass. strangely this bug seems limited to DateTextBox in Forms?  
""",
u"""
include license text. 
""",
u"""
Handle false in parseResults.  Fixes #4744
""",
u"""
Just do the registerLibrary call, for now.  Fixes #4145
""",
u"""
fixes #4336

""",
u"""
ship a copy of the unicode license with modified ldml. 
""",
u"""
Fixes #3944. Prevent bad code that adds things to Object.prototype to cause errors in xdomain loading. Not bullet-proof, if an Object.prototype property is added that is a boolean true, xd loading will fail, but hey, don't do that to Object.prototype.
""",
u"""
some code reductions. Throw if json filtered comment fails.
""",
u"""
Fix for identity problem.  Fixes #4691
""",
u"""
Tolerate no space before am/pm in parse.  Fixes #4718
""",
u"""
Fix failure log statement.  Fixes #4722
""",
u"""
Have xd loader use same comment removal code as the build system, so behavior is consistent. Also makes xd loader smaller.
""",
u"""
fixes deferred list return problem. fixes #4240  execept issue 3 which is the expected behavior though admittedly can be confusing at times.
""",
u"""
fix scope issue with deferredLists.  fixes #4687
""",
u"""
- cannot have (lowercased) reserved words as the first word
in a summary or comment block, or the parser goes into a different 
tangent.  minor cleanups and assit parser.


""",
u"""
Lines can't start with keywords
""",
u"""
removing Myriad Pro from the CSS for various reasons, one being that there are a number of overlapping issues in Firefox. The other being that most people don't have this font anyways so we shouldn't really rely on it as our default font. fixes #4429
""",
u"""
make logging before the console is available not bomb things out. 

""",
u"""
merging patch from Mike Wilcox (mike@sitepen.com) that adds object inspection and a popup mode to Dojo's integrated Firebug Lite. Excellent patch, needed only the most minor style cleanups. Great work. Fixes #4589

""",
u"""
Updating error message.  fixes #4629
""",
u"""
Fixes #4495. The extra set () should avoid the jslint error.
""",
u"""
Fixes #4327. Single quotes in the value where causing trouble. Patch from schallm, CLA on file. Thank you.
""",
u"""
Minor fix to sorter.  fixes #4491
""",
u"""
fixes #4239 - code size reduction and optimization for dojo.fx.slideTo.

""",
u"""
Disable onmouseenter and onmouseout until #4307 is fixed on FF.  (
""",
u"""
- small doc fixes to loader.js


""",
u"""
fixes #2103 - by documenting the easing object some, and adding more inline docs for core fx + dojo.fx


""",
u"""
More moves from Mover to Moveable. 
""",
u"""
Moved topics from Mover to Moveable. 
""",
u"""
Splitting Mover and Moveable from move.js. 
Added local events to Moveable.
""",
u"""
Reductions for _base, including:

* removal of unnecessary typeof foo != "undefined" pattern
* removal of Konqueror workaround (fixed in 3.5.5: http://bugs.kde.org/show_bug.cgi?id=126482)
* removal of unnecessary instance defaults on prototype object


""",
u"""
Fix up German color translations. 
""",
u"""
testcase for delay. 
""",
u"""
fixes #4586
""",
u"""
fixes #4516
FF uses "" and "none", not "normal" and "none" to control selectability.
""",
u"""
Translations for dojo.color. 
""",
u"""
Another minor ref fix.  
""",
u"""
era was broken. Fixes #4548
""",
u"""
add onmouseenter and onmouseleave to the shortcuts provided by NodeList. 

""",
u"""
add support for onmouseenter and onmouseleave to all DOM Nodes which are dojo.connect()-ed to. Fixes #4307

""",
u"""
Style and space fix for dojo.isArrayLike. 
""",
u"""
Ensure non-null 'props' before dereferencing, fixes #4532.
""",
u"""
Minor fix.  fixes #4481
""",
u"""
Handle "class" and "style" attributes according to IE quirks. 

""",
u"""
"." becomes "+", fixes #4449.
""",
u"""
ensure that dojo.publish() does not stop execution of code following it if the topic doesn't exist. Fixes #4447

""",
u"""
Minor fix to save.  fixes #4394
""",
u"""
Fixes #3583. Introduces debugAtAllCosts support via dynamically loading loader_xd.js and a debug support file. Requires use of dojo.addOnLoad() to work.
""",
u"""
Add comments for isObject plus style mods.  Fixes #4424, #3961
""",
u"""
Fixes #4259 and #4330. Fixes for form values with multiple names and for selects with multiple selected options
""",
u"""
Rearrange code to separate loader concerns from other things. Ends up with a slightly smaller dojo.js too. Still a bit more to do on it, but this tested well.
""",
u"""
Add LICENSE file.
""",
u"""
Style faux pas, 
""",
u"""
Repair _watchInFlight loop, fixes #4386.
""",
u"""
Adding conditional comments to strip out functions duplicated in dojo.xd.js.
""",
u"""
Add 'extend' method to declared classes (not instances), fixes #4348.
""",
u"""
Now when dojo.dnd.Mover publishes a topic, it passes itself as a parameter, instead of a node. The node is still accessible from it as a "node" member. It gives more flexibility including the access to the latest mouse position, which is updated automatically on every move. Additionally subscribers can customize a mover on the fly.

I did trivial updates to existing /dnd/move/ subscribers.

Fixes #4344.
""",
u"""
Fixes #4338: allow setting widget startup methods via <script type="dojo/method" event="foo">
""",
u"""
Fixes #4288. Bad variable reference from a refactor. Fixes loading if the page uses an xdomain baseUrl and relative paths to that for the modulePaths.
""",
u"""
Call "postscript" method after construction, 
""",
u"""
make the sorting look right and re-enable row actions. 

""",
u"""
Prevent duplicating 'preamble' in intermediate delegates, fixes #4243.
""",
u"""
fixing scoped execution of connections for Declarations. 

""",
u"""
make sure that deferreds get results. 

""",
u"""
NodeList's aren't instances of the parent docuemnt's Array class. Use a test that encodes this data. 

""",
u"""
IE methods were being plucked out of the wrong scope. Fixes #4226

""",
u"""
Removing document.domain references. Tested on FF 2.0.06, Safari 3.0.3, Opera 9.23, IE 6 and IE 7.
""",
u"""
Porting XHR IFrame Proxy. Need to pass args object, not URL.
""",
u"""
allow dojo.forEach(), dojo.map(), and related functions to take strings as functions to execute. Need to investigate caching the resulting anonymous functions. Makes operating on NodeLists much easier. 

""",
u"""
start of some syntatic sugar for NodeLists. Makes connecting to common events easier as well as changing css class names on a list. 

""",
u"""
start of checkins for syntatic sugar for dojo.NodeList. This doesn't directly add sugar, but other methods will want/need dojo.connectPublisher(). 

""",
u"""
Porting XHR IFrame Proxy. Cleared core change with Alex.
""",
u"""
#Fixes #4195. addOnUnload not being called. Resulted from r10151. Adding a simple test and cleaning up docs (thanks to liucougar for pointing that out).
""",
u"""
Testing for the dojo stylesheet change with the addition of the dojoTabular class for tables.
""",
u"""
initial cut at a fix for default table styling backoff. Adds new table-specific rule dojoTabular which is opt-in. 

""",
u"""
Removed reference to dojo.lang.repr() --- it didn't harm, but we can save a few bytes by removing it. Thanks, guest! Fixes #4208.
""",
u"""
Fixed typo in html.js. Tweaked the default DnD avatar for better visibility. Fixes #4210.
""",
u"""
Removed English text from the default Avatar. Added an example on how to override the text using a custom code to Flickr Viewer. 
""",
u"""
More tweaking to Flickr Viewer, removed gif files. 
""",
u"""
Created new dnd.css, images moved to resources, all DnD-related tests and demos are updated, Flickr Viewer is tweaked somewhat. 
""",
u"""
Fixes #3051.  Provides basic inline documentation as to the purpose of the stylesheet, and what it will do to a web page that uses it.
""",
u"""
make Joe's license terms 100% specific. 

""",
u"""
Replacing images with a new normalized set. 
""",
u"""
ensure that type=dojo/connect style scripts work correctly with dijit.Declaration. Fixes #4199

""",
u"""
Fix typo I made in 'faux declaration' of getComputedStyle.  
""",
u"""
Use new docparser comment feature for 'faux declaration'.  
""",
u"""
Fixes #3845. Needless double transform of form info, but also pointed to an issue with dojo.queryToObject, it was not calling decodeURIComponent for the query names. Fixed that too.
""",
u"""
Comply with Dojo style.  
""",
u"""
pick up a couple more bytes from array.  Use xor bitwise logic on booleans.  
""",
u"""
eliminates the native branch for dojo.* array methods. There wasn't a perceptable or testable speed difference and it cost us in bytes. 

""",
u"""
trimming cruft from dojo.Deferred. The toString() was especially useless. 

""",
u"""
Initial checkin of OpenAjax hub, r100 (not yet integrated into bootstrap) under Apache License 2.0.  
""",
u"""
Yes, it was the Firebug-Lite all along, who triggered some bizarre bugs in IE. This simple fix takes care of it by delaying the Firebug CSS loading. Fixes #4157.
""",
u"""
Comment out unused dependency on PEAR, fixes #4158.
""",
u"""
[[BR]]Aggressive leak protection on IE7 (which is more broken than we had hoped), fixes #4141.[[BR]]
[[BR]]Indirect listener from disconnect package, fixes #4142.[[BR]]
[[BR]]Remove closure over 'node' in _fixCallback on IE, fixes #4159.[[BR]]
[[BR]]Key hack to normalize arrow and page keys on Safari for Windows, fixes #4129.[[BR]]
""",
u"""
Make toPixelValue translate 'medium' to 4, hack 
Repair scrolling adjustment in _abs, fixes #3455.
""",
u"""
dojo.removeClass() changes the className only if it is different after removal. 
""",
u"""
IE doesn't recognize several things that are web 2.0

""",
u"""
special case the ">" query. Was a major oversight that new tests helped dig up. 

""",
u"""
some size-related changes and a bit of crusty function removal. 

""",
u"""
make sure that the doc system picks up _getText but that we don't pay for it otherwise. 

""",
u"""
size optimizations for loader. 

""",
u"""
no one's using "makeCalled()". Removing it. 

""",
u"""
clobber cruft function. 

""",
u"""
size reductions for NodeList. 

""",
u"""
make sure that map returns a NodeList.  
""",
u"""
remove some spruious function calls in the fast path on IE. Ensure that form disambiguation code still in play on IE and opera (where it's still, apparently, a problem). 

""",
u"""
Fixes #3973. Support BASE tags. Does not work with Opera 9.22, but it could be a general issue with Opera, base tags and XHR loading. Still would like to fix the core issue of why we need a dojo._Url call in here, but can't seem to crack it.
""",
u"""
Fixes #3984: adds a djConfig option to turn off the json-comment warning when using handleAs: 'json' with the xhr calls. Changed the handleAs names for dojo.io.iframe to be consistent with xhr handleAs names. Using dojo.fromJson in the dojo.io.iframe 'json' handleAs logic branch. Added some more unit tests for dojo.io.iframe.
""",
u"""
Fix parse/regexp with places ranging from 0 to n: "0,n".  Fixes #2864, 
""",
u"""
Fixes #2713 #4085 #3801. Flattened bundles for i18n layers should work in xd and non-xd load cases now. Also brought over some xd fixes that were made after the 0.9 code was copied from the old trunk.
""",
u"""
Should have been part of previous commit.
""",
u"""
Makes dojo.declare more extensible

""",
u"""
Reverting back changes, which were lost during the dojo.declare cleanup. 
""",
u"""
Make sumAncestorProperties do what it says it will do (+test), fixes #1965.
""",
u"""
Fix files that got messed up when merging changes, 
""",
u"""
Updates to handle multiple fetches odduring at data load time.  
""",
u"""
Monster commit to update uses of declare to new cleaner syntax, Changes are 99% syntactic only. If you have a problem, let me know and I will help you fix it asap.
""",
u"""
Added a parameter to handle form elements. Fixes #4032.
""",
u"""
Abstracted access to the data map. Fixes #3923.
""",
u"""
use parseFloat instead of parseInt where appropriate. Fixes #4061

""",
u"""
Less zealousness when clobbering keyCodes in preventDefault for IE, 
""",
u"""
Removing accidental global.  
""",
u"""
Don't select a prototype tree for 'inherited' that doesn't contain the target method at all, 
""",
u"""
Additional (crufty) filter for native toString implementation in dojo.mixin, 
""",
u"""
Remove accidental global reference.  
""",
u"""
Reduce footprint of boilerplate constructor by simplifying closure, 
""",
u"""
Implement mixin semantic as an inheritance tree to support robust "inherited", Support improved initializer syntax, including deprecation warning for older style, 
""",
u"""
Fixes #3743. Need to wait until after browser_hostenv does script tag parsing for djConfig. Doing a copy/paste job in all hostenvs to avoid bloating base by having duplicate check in loader.js.
""",
u"""
References #4034.  Change the str2obj to return NaN for value="" wrt number attributes.
""",
u"""
migrate the rather tedious <script type="dojo/method" mode="connect" event="....">  syntax to simply <script type="dojo/connect" event="...">. Fixes #3615

""",
u"""
ensure that all unit tests are being run. Fixes #4060

""",
u"""
Rename slideIn/slideOut to wipeIn/wipeOut.  
""",
u"""
Rename slideIn/slideOut to wipeIn/wipeOut.  Fixes #3917
""",
u"""
fixes to NodeList.map and eliding away the node list single arg ctor method to match IE's (b0rken) behavior. themeTester.html should work on IE now. Fixes #3987

""",
u"""
port DeferredList from 0.4 to 0.9. 
""",
u"""
Fixes #2765: calling dojo.addOnLoad inside a dojo.addOnLoad after doing an xdomain dojo.require() should work now.
""",
u"""
Need to put the function definition above the call, otherwise bad things happen with shrinksafe.
""",
u"""
References #3985.  IE doesn't always set item.selected=true for the value attribute.
""",
u"""
Fixes #3724. Now IE 6 should pass xhr unit tests. Note that only testing from a server is officially supported, given that the tests try to do PUTs and DELETEs, which do not make sense for local files.
""",
u"""
Fixes #3733: Exposes semi-public method to cancel all pending IO requests.
""",
u"""
Remove script elements in the jsonp style of usage that have already succeeded. This is not the fix though, and not sure if there will be a complete one without engaging browser vendors. Even in a test I did before without using dojo, just simple script attachments and removal of nodes when it was done, I saw a few bytes leaked on each call (I think the amount depends on the size of the response in the script).
""",
u"""
References #1140. In the timeout case, remove the script tag immediately instead of waiting for the next 50ms check. Some oddities with some browsers noted in the test page, but I will file bugs with the browser vendors once this test is in the nightlies.
""",
u"""
Fixes #3978. Using dojo.doc instead of document inside of dojo.io.script.
""",
u"""
adding developer docs for dojo.query(). Fixes #3908

""",
u"""
Fix setSelectable() on IE to affect the selectability of all the subnodes.
This makes IE function like Mozilla.
To test this change, just try selecting the label on a tab (TabContainer.js).
Fixes #1031.
""",
u"""
adding docs for many of the NodeList methods, adding tests for some of them, improving the code structure in general to make it clear that extending NodeList is straightforward, and expanding the unit tests to check for return types from NodeList methods. Still more work to be done there, though. 

""",
u"""
On IE7 Alpha(Filter opacity=100) makes text look fuzzy so remove it altogether.
Fixes fuzzy text on Dialog.
Fixes #2661.

""",
u"""
Fix parser bugs reading disabled/checked, and also b="false" and foo="" type
attributes (which should be obeyed not ignored).

Make date="" convert to an invalid date (the NaN of dates), and date="now" convert
to the current date.

Fixes #3682, #3968.
""",
u"""
Prevent in-flight leakage on IE. fixes #2357

""",
u"""
adding better in-code docs for xhr.js. Fixes #3975

""",
u"""
Minor cleanup. 
""",
u"""
slight variable factoring for size. 

""",
u"""
adding a toggler class and the start of unit tests for the dojo.fx namespace. Fixes #3641. 

""",
u"""
Checking if fix to  non-tf8 char.  Byte emcodin check didn't catch the bad bytes.   Fooey, validator test failed.  Restoring to good file.  
""",
u"""
Deliberately trying to commit a file that won't pass UTF-8 checks.  If this gets in, the check doesn't work.  
""",
u"""
Remove bogus char(s).  
""",
u"""
accepting Eugene's clone() patch. Fixes #3553

""",
u"""
Fix comment to match code.  Fixes #3869.
""",
u"""
ensure that XML documents are passed back unserialized on IE, even when it's being lame. Fixes #3294

""",
u"""
style nits. comments and docs need fixing badly. Fixes #1837

""",
u"""
fixes #78. The name of the ".*" files is now settable via djConfig.packageFileName, which defaults to "__package__". A global, recursive rename is required on the part of users affected by #78, but that's not our issue. mod_rewrite or similar provide a way out.

""",
u"""
fixes #2237, handle case for RPCService where an error object should be returned instead of a string
""",
u"""
Move source uri hint to end of file (for firebug 1.1) so that it won't throw off the line count in the eval buffer by 1.  
""",
u"""
dojo.style(node, "height") can return "auto" or "" on IE rather than a number,
so use offsetHeight instead.  Fixes #3891.
""",
u"""
Fix *re*-execution of animations with start/end points specified as functions.  The function references were getting overwritten on the first execution.

Various fixes to wipeIn()/wipeOut(): since the start/end points are read in _base/fx.js's beforeBegin(), and that function is called before fx.js's beforeBegin(), we can't set start/end in fx.js's beforeBegin().

Changed TitlePane's wipeIn/wipeOut to work on node w/no padding or border.  Otherwise setting height=1px will actually set height to 21px on firefox (because height is just the content height).

Overrode TitlePane.setContent() to animate height change, so that when an href loads it has a smooth expand.

Seeing weird problem w/scrollbars on firefox.  Needs to be investigated.  Also, IE closes instantly rather than wiping out (bug where dojo.style(node, "height") returns 0 on IE on visible node with height:auto)


""",
u"""
Add a warning instead of throwing an obscure exception if dojo.back.init() hasn't been called. Fixes #3861.
""",
u"""
Changed zIndex of avatar to 1999 --- it ensures that it is above any pop-up widgets. Minor typo fix in docs. Fixes #654.
""",
u"""
fixes #3873 -- Bug in ItemFileWriteStore that would show up when using a file that did not specify an identifier and then calling newItem() after calling deleteItem().  Changed deleteItem() to place null values in the _arrayOfAllItems, rather than removing elements from the array.  Should also improve performance of deleteItem() and revert().
""",
u"""
Fixes #2982.  Changed ele.id to ele.attributes.id.value.  Added a testcase for the IE getElementById bug.
""",
u"""
Minor style, spelling changes.  
""",
u"""
Comments hopefully clarified, 
""",
u"""
Fix comments (evt is obviously not optional).  
""",
u"""
Minor doc update that was missed. 
""",
u"""
Adding a small bit to the Write API.  fixes #3862
""",
u"""
Fixing browser host env to get local file loads working on IE 7 (and providing option to force ActiveX xhr all the time if so desirred.)  
""",
u"""
Replacing the dndItem class with already defined and already in use the dojoDndItem class. Fixes #3846.
""",
u"""
Patch to 0.9 for form handling issue.  fixes #2844
""",
u"""
Do whitespace replacement within [] regexp.  Fixes #3837
""",
u"""
Trivial fix in ItemFireWriteStore fixes #3824
""",
u"""
Allow setting a property to false from markup, Fixes #3832
""",
u"""
Following dojo (core)'s lead, make dijit.js include certain modules by default,
and make the names of the modules and methods shorter.
(ie, dijit.util.popup.open --> dijit.popup.open)


""",
u"""
am/pm can come before or after the hour.  Fixes #3672.
""",
u"""
Revert [9708] and make dojo.requireLocalization smarter about local vs xd when we're in a cross-domain scenario. Break out check for xd or local from _loadPath to support it. 
""",
u"""
Account for the fact that IE doesn't treat nbsp as whitespace in regexps.  

""",
u"""
Fixes #3801
""",
u"""
Use dojo.fromJson for default case, rather than eval() for clarity and re-use.  
""",
u"""
Updates to custom data type handling.  fixes #3792
""",
u"""
Fix issue no. 1 in currency test for numbers and dates. 
""",
u"""
Reduced size of dojo.Color, removed almost all type checks, changed the signature of dojo.blendColors(), and updated dojo.fx accordingly, dojo.Color.sanitize() moved to the core, added dojo.colors.makeGrey(), changed tests, added tests for dojo.blendColors(). Thanks, Adam. Fixes #3653.
""",
u"""
Fix issue #1 in currency test. 
""",
u"""

fixes #3405 - callback goes unused in example in documentation.


""",
u"""
fixes #3403
""",
u"""
dojo.date.difference also fixes #2587, #2024
""",
u"""
Revert change to enable native array iteration methods
on Safari3. The change fails the existing unit tests for array.js, and it does
not appear that Safari3's implementation is sufficient for dojo's forEach 
contract. Specifically, forEach is not defined on String objects or null / 
undefined values, so call against those types fail with a TypeError.

We could insert an adapter that used the fast path on Safari3 when available
and fell back to the default Dojo implementation otherwise, but we'd need to 
vet that technique with performance testing. For now, I'm just reverting the
change and we can figure out what we'd like to do long term.. later.

""",
u"""
Go back to iterative approach to calculate day/week of year, due to DST bug. Fixes #2587, #2024
""",
u"""
add a test case that allows array to be tested from a browser-based environment.
""",
u"""
Added full CSS3 component recognition (rgb, rgba, hsl, hsla, and rgb/rgba with percentage values).
Added tests for enhanced functionality (copied from CSS3 examples).
Added "transparent" color as descrobed by CSS3.
Fixes #3652.
""",
u"""
Added one more test for dojo.Color. Fixed dojo.data test, which used dojo.Color. 
""",
u"""
New implementation of dojo.Color as an object, support for common CSS formats, updates to utility functions, optimizations for fx.js, expanded test cases, minor updates to dojox.gfx. 
""",
u"""
replace another trim func. 
""",
u"""
Fix various IE problems with parameters that are builtin function names,
like onclick and onchange.

Example:
  <button dojoType=dijit.form.Button onChange="foo" onClick="setValue();}>

The onChange got defined as an invalid function:
  function anonymous(){ foo }
  
The onClick ended up calling dijit.form.Button.setValue(), rather than the global
setValue().

Fixes #3745.
""",
u"""
Added dojo.trim() (one-liner), and dojo.string.trim(). Thx Steven Levithan. Fixes #3731.
""",
u"""
Put a more descriptive throw in _Templated for missing keys.  Don't want to just return an empty string, or the developer may never notice the error.  Also allow user to use HTML literals in templates using "!" prefix. Fixes #3700
""",
u"""
fixup little whitespace issue.
""",
u"""
fixes #3742. add support for native array iteration methods for safari3
""",
u"""
Fixing minor issue with RPC tests and Rhino.  fixes #3730
""",
u"""
Ugh.  We were off by a scrollbar. Fixed logic in getIeDocumentElementOffset (thanks, Justin)  

""",
u"""
IE doesn't support iframe.contentDocument.  

""",
u"""
Update to testcases to get around a problem with Rhino running the UT.  Further investigation should still be done....  fixes #3729
""",
u"""
Fixes #3699
""",
u"""
Fixes #3651
""",
u"""
Checking in fix to the date serializer to use dojo.date.stamp to use ISO formats for storage and default serialize/deserialize.  fixes #3679
""",
u"""
Fixed rgb2hex so that it returns 3 octets, not 4.  But I still don't think animateProperty is working right for colors. Fixes #3667
""",
u"""
Don't try to unload bundles in teardown to restore state.  delete isn't sufficient, and we don't do this for any other modules.  Fixes #3605
""",
u"""
Fixes #3702. Loading local i18n bundles was failing.
""",
u"""
Forgot RTL test file. 

""",
u"""
Patch to workaround BiDi problems calculating offsets on IE.  Fixes #3115

""",
u"""
Bogus checkin to test post-commit script. 
""",
u"""
Bogus checkin to test post-commit script. 
""",
u"""
Bogus checkin to test post-commit script. 
""",
u"""
Bogus checkin to test post-commit script. 
""",
u"""
Bogus checkin to test post-commit script. 
""",
u"""
Fixes #3699
""",
u"""
More efficient color conversion, plus inline docs. Fixes #3667
""",
u"""
this time for sure...
fixes #3669
Re-factored the unit tests for ItemFileReadStore and ItemFileWriteStore, so that the common tests are shared in a common file.
""",
u"""

reverting parser.js changes from chengeset 9557.  broke: TabContainer, 
Editor, and more. ... "bill made me doit." 


""",
u"""
ensuring the that parser tests pass and that the parser is working for some builtins attrs where it previously failed. Fixes #3682

""",
u"""
turn parsing on in the parser tests ;-). 

""",
u"""
fixes #3669
Re-factored the unit tests for ItemFileReadStore and ItemFileWriteStore, so that the common tests are shared in a common file. Deleted 1,500 of duplicate code. 
""",
u"""
fixes #3669
Re-factored the unit tests for ItemFileReadStore and ItemFileWriteStore, so that the common tests are shared in a common file. Deleted 1,500 of duplicate code. 
""",
u"""
Implementing moving and cloning nodes, when there is no creator function. Fixes #3664.
""",
u"""
References #3621.  Fixed parser test page to use commas instead of semi-colons.
""",
u"""
more spelling fixes.  hope I got them all this time. 
""",
u"""
Add translation comments, fix a few spellings. 
""",
u"""
Provide translations for dojo.colors.  Use mixins to add CSS3 to existing colors in _base.  Fixes #3188
""",
u"""
After multiple consultations I am committing a table of all named CSS3 colors. It populates (replaces) dojo.Color.named table. Because it is out of the core we don't sweat too much about its size => it is not manually compressed. Fixes #3188.
""",
u"""
DnD move is adapted to be used with the Dojo markup. Fixes #3650.
""",
u"""
Minor normalization of user-supplied functions. 
""",
u"""
Removed selectors and filters, switched to dojo.query() selection, implemented the Dojo markup for DnD (no move yet), added examples. 
""",
u"""
fixes #3654
Now ItemFileReadStore always implements the Identity API, even if no identifier is specified in the data file.
""",
u"""
All topic names are normalized from the camel case to the folder case. Fixes #3649.
""",
u"""
References #3621.  Change array delimiter in the parser to comma from semi-colon to align with JSON delimiters and to allow HTML special characters like &nbsp;
""",
u"""
Make slideIn()/slideOut() assume a natural height for the node, rather
than trying to obey a height specification on the node's style.  This
simplification fixes #2944, #2343, #3152
""",
u"""

renamed JsonItemStore and JsonItemWriteStore to be ItemFileReadStore and ItemFileWriteStore
""",
u"""
[dojo.data] in JsonItemStore file format, change {reference: to
{_reference:
""",
u"""
Add tests for parsing "checked" and "disabled" attributes.  
""",
u"""
fixes #3629
tested in: [Firefox 2.0, Safari 3.0, IE 6.0]

""",
u"""
fixes #3627
fixes #3628

tested in: [Firefox 2.0, Safari 3.0, IE 6.0]
""",
u"""
Prevent _getMarginBox and _sumAncestorProperties from calling getComputedStyle on non style-bearing objects (i.e. document). 
""",
u"""
Replace removeChild with dojo._destroyElement. 
""",
u"""
Fixes #3605
""",
u"""
Added a todo item: need tests for dojo.place(). 
""",
u"""
Added more tests for semi-public box functions. 
""",
u"""
Implemented an inexpensive space trimming for class strings. Fixes #3604.
""",
u"""
adding isDescendant() and setSelectable() methods. Still need to update dijit to use the new methods.

""",
u"""
Added testClassFunctions(). 
""",
u"""
Updated TODO. 
""",
u"""
Added rawXhrPost() test. 
""",
u"""
Added xhrPut() and xhrDelete() tests. Corrected an IE-specific bug (the trailing comma). 
""",
u"""
dojo._destroyElement argument doesn't necessarily have a parent node,
specifically in the case of closing a tab (in a dijit.TabContainer).

""",
u"""
Fixes #3588. Use new dojo._destroyElement call instead of removeChild
""",
u"""
Fixes #3526. IO docs. Also updated port guide at http://dojotoolkit.org/book/dojo-porting-guide-0-4-x-0-9/io-transports-ajax
""",
u"""
adding inline docs for html functions. Fixes #3162

""",
u"""
Fixes #3507: canceled deferreds get an error object with dojoType property of cancel.
""",
u"""
Fixes #3577. Obsolete dojo.render reference.
""",
u"""
implement djConfig.parseOnLoad param. Move tests to use parseOnLoad to signify that they want/need full page parsing onload. Lots of hygene fixes for the dijit test pages. Fixes #3510

""",
u"""
adding dojo._destroyElement method. Fixes #2931

""",
u"""
Refactored autoscroll, minor cleanup. Implemented dojo.dnd.autoScrollNodes(), but at the moment it works only on FF --- apparently dojo.html methods do not isolate us good enough from idiosyncrasies of different browsers. Will investigate more. For the new method is not used anywhere. 
""",
u"""
Added a try guard against some FF-related quirks. See the ticket for details. Added a test for this kind of problem. Fixes #3370.
""",
u"""
Fixes #3534. args.url query params are not added to the list of params inside of dojo._ioSetArgs, but query params discovered as a result of dojo._ioSetArgs can be added to the querystring for qualifying http methods. The result is that the input args.url is preserved with its querystring params.
""",
u"""
missing 'var'.  Fixes #3575
""",
u"""
Break out dojo.Color into its own module.  Fixes #3343
""",
u"""
don't need to log these squelches. They're legit. 
""",
u"""

adding default list of dnd-based classes and make tests follow along.
consistant, pretty enough, could probably include tundra theme classes
without problem, though adds a 'dep' of dijit on dojo asthetically.
perhaps tundra should have some basic matching classes to over-ride
base dnd classes? this fixes #3052 (?) ... randomly added dojo.subscribe
example call to test_dnd, too.



""",
u"""
Forgot to add one more thing. 
""",
u"""
In order to stop critics I've implemented dojo.dnd.Target for them. Enjoy! Fixes #3568.
""",
u"""
Implemented autoscroll. Tested on FF, IE, Op, and Safari -- the last two suffer from giblets --- probably need to file bugs to them. Implemented a condenced version of getViewport(). It is quite small --- probably it should go to html.js.
Fixes #1597.
""",
u"""
Cleanup. 
""",
u"""
Fix test names. 
""",
u"""
Numerous additional tests for html.js courtesy of Steve Orvell (TurboAjax Group). 
""",
u"""
Change addOnUnload events to fire at window.onbeforeunload (except on IE), 
""",
u"""
making it look a bit better. 

""",
u"""
Restrict Safari margin hack to nodes that are not position: absolute, allowing more tests to pass, 
Correct getMarginBox adjustment for Opera offsetLeft/Top, 
""",
u"""
General cleanup and a typo fix. Thx, Scott. Fixes #3229.
""",
u"""
API update for dojo.data.api.Identity.  
""",
u"""
Added global and local classes, so programmers can change UI during the move. Added topics to indicated that the move has started and ended. Fixes #3371.
""",
u"""
Added the customization for copyOnly sources. 
""",
u"""
Standardize on "label" (not caption).  Fixes #3288.
""",
u"""
IE-specific fixes. Fixes #3224.
""",
u"""
Updates to accomodate new refactored html.js, and minor typo fixes. 
""",
u"""
Refactoring of html.js. 
""",
u"""
Repair blunder in connect, now connect target should correctly return it's value. Had to effect the change in the leak-proof listener also. 
""",
u"""
Declare url as a string for the benefit of the parser.
Fixes #3539
""",
u"""
add timeout param to jsonpservice. fixes #3538
""",
u"""
test for markupFactory(). 

""",
u"""
updating the parser to:

	* handle preambles
	* enhance the semantics for <script> parsing. Mixin assignment is now the default, connects happen via mode="connect"
	* array parsing enhancements (now snarfs surrounding whitespace)
	* markupFactory() for classes which don't wish to modify their ctor semantics
	* less hitch()-ing

Fixes #3535. Still need more tests (esp for markupFactory).


""",
u"""
adding first-argument preamble plucking. Makes impedence matching easier when you don't want to muge the prototoype's preamble. 

""",
u"""
make sure we log our squelches. 

""",
u"""
tests for dojo.parser. 

""",
u"""
ensure that connect() works correctly in non-browser hostenvs. Fixes #3530

""",
u"""
Fixes #3139. Using the standard dojo.addOnLoad() to initiatilize the console div. Seems to fix the problem.
""",
u"""
Fixes #3509. Timeout path in general for io operations fixed, and specific issues in dojo.io.script were addressed. Thanks to dmachi for the timeout test file.
""",
u"""
Fixes #3500. Bad cancel() reference.
""",
u"""
Test for the window.eval issue in IE and Safari.
""",
u"""
Remove instance-based chain/combine methods, fix event connections on combine.  Update affected Dijit code.  Fixes #3325.
""",
u"""
More minor doc updates.  
""",
u"""
Minor tweaks to the Notification docs.  
""",
u"""
was missing a passthrough arg. 

""",
u"""
provide animation for node lists. 

""",
u"""
make sure we're logging errors. 

""",
u"""
add in smd to the rpc obj, fixes #3457
""",
u"""
Every node on IE defines "removeChild" as a native attribute,
but we want to ignore this attribute unless the user has actually specified it.
Thanks to Nicola Rizzo (CLA on file) for this patch.
Fixes #3074.
""",
u"""
make sure attribute searches handle all-lower-case variants on IE. Not true case insensitivity, but it's as close as we're gonna get on that browser. Fixes #3438

""",
u"""
fixes empyt param case in jsonpservice. fixes #3443
""",
u"""
change the error thrown by a deferred on cancel so we can identify it is of this type. 
""",
u"""
Improve docs.  Fixes #3338
""",
u"""
Fixes #2912. dojo.io.iframe ported. Tests succeed in IE 6, Opera 9.21, Safari 2.0.4 and FF 2.0
""",
u"""
Got an upload test working. Not part of doh unit tests since it requires user action to select a file to upload. It works in Firefox. Need to test other browsers and add an HTML response test.
""",
u"""
fixes #3440
""",
u"""
Porting dojo.io.iframe. Not there yet. Got one very simple test to work. Still needs more tests.
""",
u"""
Porting dojo.io.iframe. Not there yet. Also made io arg handleAs understandable in xhr code.
""",
u"""
Starting port of IframeIO. Just doing a copy over first.
""",
u"""
Updating version string
""",
u"""
bed-lumping the event connection machinery in the parser. 

""",
u"""
add an additional dojo.query unit test, 
""",
u"""
More typo fixes. 
""",
u"""
Typo fix. 
""",
u"""
thanks to Cameron Braid for spotting this typo. 

""",
u"""
Fixes #3388: Converted firebug lite to work as a div in the page instead of an iframe. Now usable in xdomain cases.
""",
u"""
Fixes #3340: Second try. Previous attempt bypassed safari (thanks Bill for the catch). Gets rid of an odd activexobject error sometimes showing up in firefox firebug.
""",
u"""
Fixes #3340: Gets rid of an odd activexobject error sometimes showing up in firefox firebug.
""",
u"""
Assume local timezone if none is specified in fromISOString. Fixes #3386

""",
u"""
Added docs, changed the API for dojo.dnd2.parentConstrainedMover to make it more flexible, fixed static positioning of a parent, broken absolute positioning of a parent. 
""",
u"""
Unify connect and event listener interfaces. Change disconnect package to hold a direct reference to a listener. Introduce IE6 leak protection for custom (non-DOM) events on DOM-nodes. 
""",
u"""
Add overflow: hidden to parent in DnD test to avoid confusion about the results. 
""",
u"""
Forgot to account for border when switch between client and offset sizing. 
""",
u"""
Add DnD test for parent_constraints with margins. 
""",
u"""
Safari: add a null test and return a golem object from getComputedStyle if necessary. 

Adjust _setContentBox for TABLE and BUTTON, 

Move left/top margin box adjustments out of _set and into _get. and #3320.

Let _getContentBox fall back to offsetWidth/Height if clientWidth/Height are 0. 

""",
u"""
source -> event as per discussion w/ Owen. 

""",
u"""
first cut of a <script type="dojo/connect"> system. 

""",
u"""
Include dojo.i18n in dojo.xd.js. Otherwise, the logic was getting complicated to dynamically load it, and wait to process requireLocalization calls after it is loaded. With dojo.i18n included, dojo.xd.js gzipped is 27146 vs. 25477 without it (dojo.js is 23062 gzipped).
""",
u"""
make query() more resiliant in whitespace parsing for compund queries. 

""",
u"""
Fixes #3378.  Change clientWidth/Height to offsetWidth/Height in _getContentBox and adjust calculations accordingly.
""",
u"""
Updating UT for JsonItemStore.  fixes #3361
""",
u"""
Removal of now unused test data.  fixes #3362
""",
u"""
Trivial cleanup.  fixes #3372
""",
u"""
Fixes #3369 
""",
u"""
some terminology changes to ensure that things "feel" as general as they are. 

""",
u"""
updates for stubs to improve compat. 

""",
u"""
beginning of move of parser into core. 

""",
u"""
matching the part in r9012 about ensuring that the _loadedUrls property of the dojo object actually acts as an array
""",
u"""
JsonItemStore: replaced some spaces with tabs, and removed attribute-item in doc strings. #3291
""",
u"""
Use faster regexp methods.  
""",
u"""
Minor doc updates for identity.  
""",
u"""
More dojo.query() tests.
Patch from Simon Bates (CLA on file).


Note that the dojo.query() test is currently failing, but the failure is unrelated
to this new added test.
""",
u"""
fixing more of the Java-in-JavaScript cruft that pervades the offline code. Ensuring that the _loadedUrls property of the dojo object actually acts as an array. 

""",
u"""
Getting xd loader working. Not quite there yet.
""",
u"""
Fixes #3240: adds guards around module code to avoid redefitions in layered build scenarios
""",
u"""
fixes to some rpc tests and show a useful error for tests that we know are going to fail when accessed from file://. fixes #3111
""",
u"""
fix some Rpc bugs. references #3111. references #2915
""",
u"""
update json serializer to produce yaml compliant output. also fixed dependent xhr test. fixes #1889
""",
u"""
Rename JsonPService.js to JsonpService.js for consistency with the io system. fixes #3237
""",
u"""
remove trailing comma. Fixes #3322
""",
u"""
Now ESCAPE cancels the drag. Fixes #2214.
""",
u"""
Increased the distance between the cursor and the avatar. Fixes #3341.
""",
u"""
Added a missing mouse button state change. Fixes #3316.
""",
u"""
fixes #3339: dojo.isGears incorrectly initialized
""",
u"""
For the lack of better place I ported flickr_demo.html to dojo/tests/dnd/. Fixes #3334.
""",
u"""
Fixing typo (thx Anni Hienola), and slightly restructuring the code to accomodate for new dojo.unsubscribe() syntax. Fixes #3331.
""",
u"""
add a connect() method to NodeList so we don't have to do so much forEach()-ing to set up a behavior. 

""",
u"""
Adding in getLabel API. 
""",
u"""
ensure that return order is right on IE/Safari. Fixes #3293

""",
u"""
Implements enhanced styles of drag detection, and customizable Mover. Includes box-constrained, and parent-constrained movers. A grid mover is implemented as an example of custom mover. 
""",
u"""
Fixes #3065, adds load, error, handle function callback support for io methods.
""",
u"""
post, put, and delete support from Jared. Fixes #3276

""",
u"""
Making sure that the correct document is used for move operations. Tahnk you, doughays! Fixes #3298.
""",
u"""
Reverting the change to fix #3178. 
""",
u"""
Switched from manual code to dojo.marginBox() for all element movements reducing the code size in the process. Thanks Scott J. Miles! Fixes #3249. Fixes #3255.
""",
u"""
Non-ideally, remove assertions that are not be on WebKit, allow tests to pass. 
""",
u"""
Fix _toStyleValue caching, 
Adjust _setMarginBox for TABLE and BUTTON, 
Adjust _setMarginBox left/top for non-Mozilla, 
""",
u"""
Checking in minor API addition.  
""",
u"""
Commiting in minor change to remove the attribute-item concept from the API.  fixes #3291
""",
u"""

Removing style definitions in dojo.css which make dijit's hard to style.  Approved by ttrenka.


""",
u"""
ensure that repeated showings of a dialog continue to show the background. Improve background show/hide to actually fade things in and out. We want dialogs to be visually attractive. More work on transitions may be in order (e.g., Lightbox effects). 

""",
u"""
tests.date.stamp UT was failing on IE.  

""",
u"""
Updated API files for dojo.data to remove use of dojo.unimplemented.  
""",
u"""
Privatize add/removeListener, client code should just use connect/disconnect. 
""",
u"""
Update test for new unsubscribe syntax, 
""",
u"""
Minor comment edit on subscribe, 

""",
u"""
Inline docs for subscribe/unsubscribe/publish, 
Change API so that the handle returned from subscribe is all you need (necessary and sufficient) for unsubscribe, 
""",
u"""
Putting in performance patch.  
""",
u"""
make iso date unit tests pass with new API. 
""",
u"""
Refactor dojo.dnd._getOffset(), fixing problem with border calculation and
making code more efficient (since getComputedValue() is only called once).
Fixes #3254.

Still seeing a jump on drag move start (bug #3255), but that was happening
before this code change.
""",
u"""
adding Google Gears detection support. 

""",
u"""
Moves the dragged node to the body to avoid esoteric settings on nodes parents. The fix works on FF and Opera, but has some subtle shift on IE. Fixes #3178.
""",
u"""
Bug: an empty drag is possible. Fixes #3230.
""",
u"""
Bug: moving items without a current item raises an exception. Fixes #3246.
""",
u"""
Additional comments. 
""",
u"""
Replace Rfc3339/Iso8601 methods with to/fromISOString methods to resemble ECMAScript 4 spec.  Fixes #3007
""",
u"""
Fixes #3243, which was failing because dojo.map() wasn't passing the idx and this
pointer to the callback function.

There's still a separate issue that Nodelist.map() returns an array, rather than
a Nodelist.  That seems wrong although I can't say for sure, since those functions
in Nodelist aren't documented.
""",
u"""
Unit test for dojo.map.  Not working on IE.  
""",
u"""
changes dojo.io.script's jsonpParam to callbackParamName
""",
u"""
Minor stylistic changes. Fixes #3227.
""",
u"""
Fix to handle null cases, as well as a performance fix + UT.  fixes #3153
""",
u"""
fixes #3225  adding quick check so we don't perturb class on removeClass unless class was found
""",
u"""
Mostly reverting previous changes.
""",
u"""
Reverting the previous change. 
""",
u"""
fixes #3227 Add dojo.toggleClass method.  See bug for details.
""",
u"""
Replaces the last instance of direct access to className to indirect getAttribute(). Fixes #3225.
""",
u"""
Replaces direct access to className to indirect getAttribute(), which is better supported. Minor performance improvement for dojo.addClass(). Fixes #3225.
""",
u"""

""",
u"""
Committing in fix for warning about comment filtered Json in JsonItemStore.  fixes #3098
""",
u"""
fixes #3194. Makes forEach() tollerent of b0rken array params just like the built-in variant. This seems to fix rendering on themeTest.html in which the checkbox widget was passing a null array to forEach.

""",
u"""
Forgot to port README for CLDR. 

""",
u"""
adding "json-comment-optional" handleAs type. 

""",
u"""
Committing in minor updates.  
""",
u"""
thanks to david schontzler for coming out of retirement to spot some errors in html.js. 

""",
u"""
Updating firebug console references to the right place.
""",
u"""
Moving firebug out of base, but keeping it private. Confirmed with Alex.
""",
u"""
logging some oversights in testing. 

""",
u"""
Implement options.fractional, set to [true,false] by default for currencies.  Fixes #2862, #2860
""",
u"""
added some tabs to make Alex happy :-P  dojo.cldr is mostly generated data and therefore really doesn't have any standalone functional tests; dojo.{date,number,currency} ought to include tests which use this data.  
""",
u"""
In process of porting loader_xd.js to 0.9. Not working yet (particularly for i18n)
""",
u"""
un-effing <em> and <strong> tags so that dojo.css can actually be used in RichText areas. 

""",
u"""
Fixes IE regression. Fixes #2729

""",
u"""
Group space between currency symbol and number with the symbol in the regexp.  Fixes #3036
""",
u"""
fix typo.  
""",
u"""
give the fx unit tests 15 seconds to finish. They were timing out intermittently before. Fixes #3141

""",
u"""
make sure things get zindex more correctly on Webkit, Opera, and IE. 

""",
u"""
remove unneeded function wrapper
""",
u"""
fixes #3133. force extractRgb to return an array of number instead of an array of string for rgb(0,0,0) style strings
""",
u"""
Replace for loops with dojo.forEach to reduce code.  Fix non-strict comparison for month parsing.  Fixes #2729
""",
u"""
add test showing dojo.query whitespace pickiness
""",
u"""
Updates the alpha value of the "_cache" member. Fixes #3128.
""",
u"""
Fix millisecond problem on IE by removing timestamp-style arguments, plus some style fixes.Fixes #3112
""",
u"""
Making sure that dojo.blendColor() works under IE, with wider range of arguments; added all 16 HTML4 colors from the CSS3 color module --- we need to support at least those. Fixes #3123.
""",
u"""
adding test todo file. 

""",
u"""
Multiple style bugs prevented dojo.hex2rgb() from workin on IE. Fixes #3119.
""",
u"""
Fixes #3116 --- undefined variable.
""",
u"""
Trap extra calls to Object constructor. 
""",
u"""
Add an exception for a bad hitch, 
""",
u"""
Change some "this" to "dojo". Library functions are generally callable in any scope. 

""",
u"""
Messed up and forgot to commit updated test. #3030.
""",
u"""
Simple conformance tests for JsonItemStore.  
""",
u"""
Thanks, Doug.  Missed some regexp special chars.  Fixes #3102
""",
u"""
move the regexes out of the fast path so that there's less chance they'll be recompiled. Drops heavy dojo._Url usage speed by ~20%. 

""",
u"""
remove spurious debugging. 

""",
u"""
switch to _base class functions. fixes #3087
""",
u"""
Make _getMarginBox left/top always be at least 0 (vs. NaN). 

""",
u"""
Fix typos. 
""",
u"""
Fix mixin specifity issue. Additional general optimizations. 
""",
u"""
Inline set*OfWeek methods, change paths to get*OfWeek methods to conform to new package conventions.  
""",
u"""
adding tests for dojo.behavior. 
Fixing off-by-one re-appliation error. 
Fixing topic publication name/action swap. 
Fixing "found" mapping for singular. topic action values.

Fixes #3001. New issues w/ dojo.behavior should be filed under separate cover.


""",
u"""
merging a (great) patch from peller. Fixes #3033

""",
u"""
fixes #3059. add in proper provide
""",
u"""
Provide a bit more flexibility to allow null references to be run through the format function, as intended.  
""",
u"""
Make _getMarginBox return proper left/top. 

""",
u"""
ben's inital port. 

""",
u"""
make it possible to declare this store from markup w/ the parser. Fixes #3021

""",
u"""
Date refactor -- move helper functions out of dojo.date.  
""",
u"""
More dojo.date refactoring based on Owen's suggestions. 

dojo.date.diff->dojo.date.difference
moved large-ish function out of format into closure
move isWeekend from dojo.cldr.supplemental to dojo.date.locale

""",
u"""
start of work to port to 0.9. 

""",
u"""
starting port of dojo.behavior to 0.9. 

""",
u"""
port YahooService to 0.9 as a generic JsonPService, 
""",
u"""
more work on rpc service. Add string arg back in for automatic retrieval of smd if desired.  moved constructor from JsonService to RpcService in preparation for enhancement. add new tests for this functionality. 
""",
u"""
Fixes #2350
""",
u"""
animation isn't useful if we can't manipulate colors. Adds dojo.Color class (completely reworked) and adds support for color animations back into the the Base animation system. Wish it were smaller, but it is what it is. 



""",
u"""
Replace enum-style args with string literals.  
""",
u"""
make sure that the NodeList tests don't bring up the firebug list console when fired up stand-alone. We don't want to screw the results. 

""",
u"""
fixup a couple of test errors, rpc tests now pass, 
""",
u"""
oops. didn't mean to check in loader.  
""",
u"""
apply dojo.date refactor to dijit/dojox. 
""",
u"""
should fix content serialization bug. Brings things closer to style-guide compliance. Tests are still failing, though.

""",
u"""
Get the dojo.date unit tests running again. 
""",
u"""
Get jsonp callbacks working. Forgot a test file.
""",
u"""
Part 2 of date refactor, to be continued.  Basde on Owen's suggestions. 

""",
u"""
port rpc to 0.9 and fix some other tickets along the way, fixes #2750 , fixes #2303 , fixes #2185 , There is still a json serialization bug, but its almost done
""",
u"""
. Reorg of rpc
""",
u"""
. Reorg of rpc
""",
u"""
. Reorg of rpc
""",
u"""
Reoorg of rpc
""",
u"""
. Reorg of rpc
""",
u"""
. Reorg of rpc
""",
u"""
. Reorg of rpc
""",
u"""
Fixes #2989. preventCache is now supported for IO calls
""",
u"""
Get jsonp callbacks working.
""",
u"""
fixes issues w/ context nodes + "> ..." rules. Fixes #2615. New issues on query should be filed under separate cover.

""",
u"""
Tweaking the box getters and setters to deal with scrollbars, change boxMode to boxModel, assume border-box on IE5.5. 

""",
u"""
fixing XHR Post regression added in last rev. 

""",
u"""
fixes weirdness w/ nodes that have display="none" on Safari. Helps to fix a slew of widget-related breakage on shipping Safari.

""",
u"""
more cleanup from Scott's back-porting. 

""",
u"""
test stub for RPC. 

""",
u"""
More repairs due to side-effects of trying to clear keyCode as on Mozilla. Just eliminating that part of the normalization for now, it's not necessary. 
""",
u"""
Special event handling for CTRL-ENTER on IE. 
""",
u"""
Handle parse of empty string. Fixes #2930
""",
u"""
fixes the tests. 

""",
u"""
merging James' patches (source and tests) for script src IO. Fixes #2911

""",
u"""
merging the first part James' patch to add ScriptSrc IO to Core. 

""",
u"""
Error trap in 'inherited' was in the wrong place. 
""",
u"""
cleanup for bed-lumped names. 

""",
u"""
Minor update to JsonItemStore tests to remove functions from the global space.  
""",
u"""
and updated version of html.js from Scott Miles. Passes unit tests and improves performance. Thanks to him for pushing so hard on me to get this right. 

""",
u"""
Consolation of some rules.
""",
u"""
Fix test that was using the console instead of the test object. 
""",
u"""
patch from Ben Lowery for numeric additions to cookies. 

""",
u"""
On Mozilla, printable chars have a 0 keyCode, trying to simulate that on IE clobbers regular key handling. 
""",
u"""
Fix bug (x2) setting stealthKeyDown flag. Thanks Doug. 
""",
u"""
another dumb mistake on my part. 

""",
u"""
dumb mistake. 

""",
u"""
use indexOf instead of regexp's. Bed-lumping _docScroll. 

""",
u"""
style guide conformance for changeset 8402. 

""",
u"""
Thanks to Scott Miles for fighting for these methods.

exposing as semi-public:
	dojo._setOpacity
	dojo._getOpacity
	dojo._getContentBox
	dojo._setContentBox
	dojo._getMarginBox
	dojo._setMarginBox
	dojo._abs
	dojo._getOpacity
	dojo._setOpacity
	dojo._getPadBorderBounds
	dojo._getMartinExtents
	dojo._toPixelValue



""",
u"""
Fine tuning in connect. Redo IE keyboard magic in event.js so it actually works. Update docs. 
""",
u"""
A modified, dojo-ized, style-guide-compliant version of Firebug Lite for use in
0.9. The icons aren't working right yet since we imported all the styles
directly into firebug.html.

Huge thanks to Joe Hewitt for re-licensing this code under the BSD license. It
significantly eased the import proceedure. 

""",
u"""
fixes #2913

""",
u"""
break stuff up into individual test fixtures to assist in debugging. 

""",
u"""
Fix typo in previous checkin to this file.

""",
u"""
Another round of revisions to connect and event. 
*connect*: had to separate argument normalization from the main functions (hopefully this will aid the doc parser since there is only one "connect/disconnect" pair now, and overrides are done to private "_connect/_disconnect" functions. 
*event*: eliminated confusing 'clean' methods and moved a key function out of the closure for leak prevention. 
*disconnect*: changed disconnect so that it only takes one argument: the handle returned from connect, simplifying client code that needs to manage connections. Updated code in various modules to reflect this change.
""",
u"""
Adding in queryIgnoreCase option into JsonItemStore (from dojo.data meeting on 2007.05.01 )  
""",
u"""
Applying two patches from Michael Smith for minor documentation updates (dojo.data.util.simpleFetch_20070429.patch and dojo.data.api.Read_20070501.patch).  
""",
u"""
fixes #2757

""",
u"""
Checking in application of Michael Smith's #2542 sorter patch + UT +
Read.js update.  fixes #2903

""",
u"""
make sure our test pages look like Dojo test pages. 

""",
u"""
roll in the YUI CSS rules now that we've vetted the IP. Should speed up page loading considerably. Fixes #2872.

""",
u"""
dojo.event.addListener was returning the wrong function, 
""",
u"""
Add another trap for read-only keyCode on IE, 
""",
u"""
Fixes to minor issues such as a var name consistency issue and a spacing nit.  fixes #2891
""",
u"""
format returns null for invalid input. 
""",
u"""
fixes #2878
""",
u"""
fixes #2877
""",
u"""
fixing formatting for comments. C'mon people, if it doesn't look readable to you, it's not. 

""",
u"""
fix DnD on IE. 

""",
u"""
foo should be "foo", my bad. 
""",
u"""
Make sure stealth onkeydown listeners are disconnected with their progenitors. Fixes last known missing requirement for event.js. 
""",
u"""
Check for built-in constructors that do not expose "apply". 
""",
u"""
Remove vestigal argument to "dispatcher". 
""",
u"""
Help fx.html work in IE: ensure integer endHeight, set overflow: hidden to allow resizing test node. 
""",
u"""
native EOLs. 
""",
u"""
native EOL. 
""",
u"""
native EOL. 
""",
u"""
native EOL. 
""",
u"""
ensure native EOL. 
""",
u"""
setting native EOL on _base files. 
""",
u"""
Simple update to UT.  
""",
u"""
Rearrange dojo.style so it doesn't call getComputedStyle unless needed. 

""",
u"""
Fix unit test references so they all run.  
""",
u"""
Changed selector API for dojo.date. Added dojo.cldr UT.  
""",
u"""
Minor update that fixes #2801  Doc updates for clarification and a new
UT case.

""",
u"""
ensure that textareas are included in form serialization. 

""",
u"""
adding Ben Lowery's patch for dojo.cookie(). Nice work, Ben. Fixes #2796

""",
u"""
removing the Moz x86_64 workaround. FF 1.5 is nearly EOL'd anyway. 

""",
u"""
more tweaking to the defaults. Force IE to cache background CSS images to prevent request flooding. No need to make things unreadably small, 13px is just fine. 

""",
u"""
Initial checkin of dojo.date.  Needs more cleanup for 0.9M2.  
""",
u"""
Repair test by using dojo.marginBox to measure height. 
""",
u"""
Event.js: all browsers: set keyCode to 0 when charCode has a value, norm CTRL-BREAK to CTRL-c where possible, IE: use native keypress for ESC and ENTER

""",
u"""
tests.* -> doh.* migration. Moving DOH out of Core. Fixes #2795

""",
u"""
ensure that "doh" has a default mapping (to the anon/committer view layout) in the package system. 

""",
u"""
final DOH files. 

""",
u"""
moving the browser runner. 

""",
u"""
more movement. 

""",
u"""
moving sounds to the new test dir. 

""",
u"""
fixing runner accuracy in reporting group failure. 

""",
u"""
I'm a freaking idiot. My apologies to scott and adam for screwing things up for both of them. 

""",
u"""
Fixes #2769
""",
u"""
wipeIn/Out was renamed to slideIn/Out. 
""",
u"""
committing Scott's new keyboard handling work + tests. Still needs more unit tests.

""",
u"""
fix wipeOut.  
""",
u"""
more fixing up for 0.9. 
""",
u"""
Missed a dojo.html reference. 
""",
u"""

""",
u"""
Fix NaN tests. 
""",
u"""
An edge case when loading local and remote modules via xd. Second part of fix comes over when loader_xd.js is ported.
""",
u"""
IE has "issues" with calls to apply() on the COM XHR object. Work around is to directly call into open(). Fixes #2767

""",
u"""


  * Changed dojo._Line to only take single values for start and end, rather than an array for both.
  * Changed repeatCount to repeat.
  * Removed some unnecessary intermediate variables.
  * Changed all fx functions to only operate on one node rather than an array of nodes.
  * Changed all fx functions to use one keyword object argument.
  * Uncommented the 3rd fx test.

""",
u"""
changing the returns of NodeList's style() and styles() functions. Returning a NodeList from them is idiotic. 

""",
u"""
now that we've got lots of test groups, roll them up but make them expandable.  

""",
u"""
super-trivial diff. 

""",
u"""
ensuring that we exercise all the filter() argument sets. 

""",
u"""
make our test pages look like dojo. 

""",
u"""
more NodeList tests. 

""",
u"""
more formatting cleanup. 

""",
u"""
Changed font to Tundra default.
""",
u"""


  * Removed calculation of the difference between start and end in dojo._Line and PropLine.
  * Changed dojo._Animation's and dojo.animateProperty's constructors to take one argument that gets mixed into the _Animation object.
  * Changed dojo.animateProperty to not use an intermediate variable (targs) to store information about the property animation.
  * Changed dojo.animateProperty back to using an object (rather than an array of objects) for property values.
  * Removed connection of handlers in dojo._Animation.  User will have to connect to events after the creation of the animation.
  * Removed repeat function.  This can be set in the constructor now.
  * Changed chain and combine methods to take an array of animations rather than figure it out from arguments.
  * Added a delay property on dojo._Animation that can be overridden in the play method.
  * Changed the _percent property to hold a value between 0 and 1 rather than 1 and 100.  This should speed things up a bit since it's not calculating the decimal each time it's used.
  * Changed core fx.js to use the changes listed above.

""",
u"""
starting to make comments readable. Still need more work on this front. 

""",
u"""
use a font that's more available on XP. 

""",
u"""
Add dojo.fx.wipeIn, add some tests. animate test not yet working. 
""",
u"""
Fixes #2749
""",
u"""
use our default CSS for the test runner. 

""",
u"""
make safari/ff work right on OS X. 

""",
u"""
make body text readable. 

""",
u"""
making the default CSS file readable. 

""",
u"""
Moved test to new test directory.
""",
u"""
adds rule for ordered lists.
""",
u"""
Uses @import to pull in YUI reset, to avoid IP issues.
""",
u"""
(Hopefully) proper attribution made WRT YUI Reset; added table definitions and tests.
""",
u"""
making the console() tests pass on Safari. 

""",
u"""
Fixes #2747: _byId was defined after it was first used, and the dojo compressor stripped it out.
""",
u"""
Generate cldr currency data without objects.  Fixes #2742
""",
u"""


  * Changed dojo.fx.chain and dojo.fx.combine to work correctly.

""",
u"""


  * Added dojo._toArray()
  * Changed dojo._hitchArgs(), dojo.partial(), dojo.NodeList.style(), and dojo.NodeList.styles() to use dojo._toArray().

""",
u"""
Start of a default stylesheet.  Includes some (but not all!) of YUI Reset, and defines a baseline for content-based materials.
""",
u"""
adds a delay between test execution. May fixt it, but it'll need more testing and Jared's verification.

""",
u"""
fix dojo. reference.  
""",
u"""
ported DnD2 to 0.9 as DnD with all tests, there is a small bug related to dojo.connect(), which will be fixed later; 
""",
u"""


  * Removd dojo.fx._Chain and dojo.fx._Combine; removed _IAnimation.
  * Added combine and chain methods on _Animation and combine and chain convenience functions on dojo.fx.
  * Removed polymorphism checks in the constructor of _Animation.

""",
u"""
port dojo.lfx.slideTo, some style changes and reductions. 
""",
u"""


  * Cleaned up some cruft that wasn't used.
  * Changed animateProperty to only accept a list of properties rather than an object with properties defined on it.

""",
u"""
implement NodeList.style() and NodeList.styles(). 

""",
u"""
give this test more breathing room. 

""",
u"""
Check in common set of cldr transforms, as built by xslt files.  Fixes #2719, #2325, #2326, #2327
""",
u"""
Port unit tests for number and currency. 
""",
u"""
Fix slideIn/slideOut. 
""",
u"""


""",
u"""
make sure the xhr tests get added to the default set. 

""",
u"""
Port dojo.number and currency along with string and regexp dependencies.  
""",
u"""
Update to use dojo.connect.  
""",
u"""
Still trying to get unit tests working.  
""",
u"""
The first test in JsonItemStore (fetch_all) fails for me.  Jared, can you take a look?  
""",
u"""
Fix regression in fade animation.  
""",
u"""
potential fix for sync requests. Needs verification

""",
u"""
(merge from 0.4 branch) Fixes #2683. Did not fix debugAtAllCosts case with previous fix, and I was trying to fix it in the wrong way.
""",
u"""
code re-ordering to survive the build. M1 tests now pass post-build. Obsoletes the attached patch.

""",
u"""
implement rawXhrPost, add tests for xhrPost(). 

""",
u"""
first cut of Ajax core + tests. 

""",
u"""
ensure that paused groups resume correctly. 

""",
u"""
Fixes json tests so that they pass in Rhino.
""",
u"""
Get the unit tests in rhino to work, except for json tests. Rhino does not serialize object properties in the same order as they appeared in the source string. Probably something to do with for/in loops not guaranteed to happen in any particular order. We just get lucky in the browser. Need to possibly rethink the tests for it.

""",
u"""
API location refacotoring, style updates, and reformatting. 

""",
u"""
minor style nits. 

""",
u"""
use a more accureate success tests. Also make semi-private to allow the xhr* functions to use it directly. 

""",
u"""
make the log output slightly smaller. 

""",
u"""
unfscking log output for Webkit and Opera. 

""",
u"""
Changing dojo.global() and doc() to properties for smaller code size and performance. No credible use case to have them as functions.
""",
u"""
First draft of new connect/event stuff. 
""",
u"""
Opera reports computed color styles in #xxxxxx format. Test accordingly. 

""",
u"""
ensure that the tests anticipate IE b0rkennes. Fixes more IE6 bone-headedness. Ensures that setting opacity values in IE returns the right value. 

""",
u"""
ensure that we get non-pixel-valued styles without casting and ensure that we do it in a compact and relatively performant way. 

""",
u"""
some reformatting of the fx code to remove use of the dojo._base.fx object. Also enabling it in the default require list for Base. 

""",
u"""
correctly scope queries. Not sure how I'd missed this. Guess we need more tests for query(). 

""",
u"""

""",
u"""
First stab at porting Animation and lfx (fx).  

""",
u"""

""",
u"""

""",
u"""


""",
u"""
Not thrilled with asserts - will revisit later.  Also, still need to port io/xhrGet code when ready.  

""",
u"""

""",
u"""

""",
u"""
IE is a steaming pile. 

""",
u"""
fixing strange issues on IE. 

""",
u"""
Change _baseUrl to baseUrl to allow developers to make url paths relative to it, also make Uri() constructor private, since we might want to change it to make it simpler. Waiting to see if there are use cases that require its current complexity.
""",
u"""
fixes byId issue on IE. 

""",
u"""
removing async options for _getText. It was completely unused. 

""",
u"""
un-fscking NodeList.filter(). Push was pushing *all* the args. 

""",
u"""
formatting fixes. Correctly detect firefox and IE versions now. 

""",
u"""
only branch for setOpacity on IE. 

""",
u"""
minor change to let root's be IDs. 

""",
u"""
un-busting NodeList's filter method. 

""",
u"""
dumb error. Thanks again to Jared for catching it. 

""",
u"""
great catch by Jared Jurkiewicz on async test completion w/ sync results. 

""",
u"""
minor updates to address logging issues on Opera and IE. 

""",
u"""
ensure that object comparison tests can end successfully. 

""",
u"""
IE byId hack only for IE < 7, get/set style properties, and a fix for boxMode calculations typo. Still needs docs and tests.

""",
u"""
porting in dojo.declare() and tests for it. Huge thanks to sjmiles and Steve from TurboAjax for their contribution of this code. Fixes #2692

""",
u"""
enable a bit of debugging output for rhino and sm. 

""",
u"""
command line tests were b0rken. This fixes. 

""",
u"""
adding quirks-mode tests for HTML namespace. 

""",
u"""
updating style code w/ the APIs Scott and I had agreed on. Updating the NodeList to use the new (corrected) APIs. Still need to implement style reading and setting. 

""",
u"""
ensure that coords() works at least minimally. 

""",
u"""
adding a first cut at style, DOM, and html utils. 

""",
u"""
prevent us from bombing out should we be loaded stand-alone. 

""",
u"""
ensure that we dont' fail when loaded stand-alone. 

""",
u"""
Fix annoying String.replace problem on IE and pass unit tests.  
""",
u"""
seems the cleanup was throwing errors. Fixes getObject() tests on IE. 

""",
u"""
a basic summarizer. 

""",
u"""
creating t, f, and is aliases for assertTrue, assertFalse, and assertEqual (respectively). I'm getting really freaking sick of typing the long names. 

""",
u"""
more correctness fixes for non-xpath code paths. 

""",
u"""
ensure that we actually play the "woohoo!" sound if it all goes well. Rate limits sounds. 

""",
u"""
we probably don't want selfTest to always be on when not loading Dojo. 

""",
u"""
beginning of tests for the NodeList class. 

""",
u"""
adding sounds so that success and failure sound like...well...success or failure. 

""",
u"""
(merge from 0.4 branch) Fixes #2683. Loading local modules after page load should work now.
""",
u"""
tests and correctness fixes for dojo.query(). This is something of a backslide on performance, but correctness trumps. Still need to find another week or so to spend on query(). 

""",
u"""
adding dojo.Uri and dojo.moduleUri. Also removing the "walk up" for .* packages. 

""",
u"""
more fixes to prevent errors with test pages not hosted in harness. 

""",
u"""
keep the system from throwing errors when a test page that includes dojo but doesn't have a parent harness loads it. We still get success/failure info at the console. 

""",
u"""
Port ant script to build cldr localization data. 
""",
u"""
Oops... locale setting was already in hostenv_browser.  Undo.  
""",
u"""
adds support for:

	- registering URLs
	- loading of tests in loaded URLs
	- automatic timeouts for loaded URLs
	- automatic test creation from code strings
	- improvements in use with dojo
	- group-level setUp() and tearDown()
	
Also includes myriad bug fixes. Still need to document many of these changes in the porting guide.

""",
u"""
include query() tests. 

""",
u"""


""",
u"""
dojo.raise() is removed in 0.9. 

""",
u"""
make sure that we don't bomb out in non-browser envs. 

""",
u"""
fixes requireIf's for rhino testing. 

""",
u"""
enable the djConfig attribute on <script> tags that pull in Dojo. Simplifies setting config options. 

""",
u"""


""",
u"""
unit test for dojo.i18n. 

""",
u"""
load dojo.i18n from bootstrap. 
""",
u"""
dojo.i18n and tests. 


""",
u"""
completing test set for array utilities. Updating utils to use fast-path if available. Fixes #2610.

""",
u"""
fix loading on IE. 

""",
u"""
Fixing up baseUrl so it works right after a build.
""",
u"""
fixes #2629  -- ads prettyPrint option to dojo.toJson, added JSON tests to harness
""",
u"""
special-case NodeList in isArray() and use the slightly faster comparators for isFunction. 

""",
u"""
updating docs, expanding description, fixing style. 

""",
u"""
fixing style, updating comments, and un-breaking toJson. 

""",
u"""
adding docs to base loader. 

""",
u"""
Starting tests for hostenvs. Might not be working in rhino and spidermonkey
""",
u"""
Adding some tests for loader.js
""",
u"""
bogus checkin to confirm that #2552 is solved. 

""",
u"""
fixing a bug and adding more array tests. 

""",
u"""
tests and updates to the basic lang utilities. 

""",
u"""
output how many tests need to be run. 

""",
u"""
get debugging output working correctly on the webkit nightlies. 

""",
u"""
fix test-name-finding on Opera. 

""",
u"""
brings NodeList and query() up to date. I'm surprised at how small the diff is. Still need to bring in/write tests for them. 

""",
u"""
start logging error objects directly. Helps us get actual failure info out of exceptions. Huzzah. 

""",
u"""
add NodeList and query to the Base. 

""",
u"""
ensure that the array methods work correctly on IE/Opera/Safari/etc. Earlier revs were using the removed dj_global and is* functions to tell type. 

""",
u"""
Tests for dojo.getObject()
""",
u"""
from discussion w/ james burke. 

""",
u"""
removing last arg to getObject() after discussion w/ jburke. 

""",
u"""
add tests for Deferred and fix Deffered to not use dojo.raise(). 

""",
u"""
note to self. 

""",
u"""
removing unused functions. 

""",
u"""
adding basic array tests. Still need to add test for lastIndexOf. 

""",
u"""


""",
u"""
better conformance w/ the refactor document. 

""",
u"""
pull in the query() system to Core

""",
u"""
pull in the query system to Base

""",
u"""
try harder to get function-only test names, add a minimal test file for the bootstrap, and ensure that test harness self-tests aren't run all the time. 

""",
u"""
nowhere near working yet. 

""",
u"""
ugg. It's late. 

""",
u"""


""",
u"""
initial start at pulling in some of the utility funcs. 

""",
u"""


""",
u"""
beginning port of Deferreds. 

""",
u"""
pull in stuff that the Base needs. 

""",
u"""
ensure that the base loader get added to the mix. 

""",
u"""
go straight for the document.all case in IE. 

""",
u"""
prevent leakage of an inadvertant global name. 

""",
u"""
remove dojo.findModule. It was effing useless. 

""",
u"""
dojo.debug --> console.debug. 

""",
u"""
dojo.post_load_ --> dojo._postLoad. 

""",
u"""
ensure that the play/pause button is in the right state. 

""",
u"""
ensure that the console is cleared for each test run. 

""",
u"""
ensure that all tests get loaded in from tests/_base.js. 

""",
u"""
provide console.* stubs for environments that don't have Firebug. 

""",
u"""
fixes onload code, removes TONS of cruft, and slims the built (browser) bootstrap loader to 11K from 21K. 

""",
u"""
implements changes that allow both the Rhino and Spidermonkey hostenv's to run the test harness smoke test successfully. 

""",
u"""
keep the test system from conflicting w/ Dojo when run in a browser environment. 

""",
u"""
port the command-line tests to run using the most primordial Dojo package loader. 

""",
u"""
updating the throw-away bootstrapper to reference the new locations of the loader files. 

""",
]
