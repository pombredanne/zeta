orald_description = \
u"""
JavaScript is a scripting language widely used for client-side web development.
It was the originating dialect of the __ECMAScript standard__. It is a dynamic,
weakly typed, prototype-based language with first-class functions. JavaScript
was influenced by many languages and was designed to look like Java, but be
easier for non-programmers to work with.

Although best known for its use in websites (as client-side JavaScript),
JavaScript is also used to enable scripting access to objects embedded in
other applications (see below).

JavaScript, despite the name, is essentially unrelated to the Java programming
language, although both have the common C syntax, and JavaScript copies many
Java names and naming conventions. The language's name is the result of a
co-marketing deal between Netscape and Sun, in exchange for Netscape bundling
Sun's Java runtime with their then-dominant browser. The key design principles
within JavaScript are inherited from the Self and Scheme programming
languages.

''JavaScript is a trademark of Sun Microsystems''. It was used under license
for technology invented and implemented by Netscape Communications and current
entities such as the Mozilla Foundation.
"""

orald_compdesc    = \
[
u"""JavaScript is a scripting language used to enable programmatic access to
objects within other applications. It is primarily used in the form of
client-side JavaScript for the development of dynamic websites. JavaScript is
a dialect of the ECMAScript standard and is characterized as a dynamic, weakly
typed, prototype-based language with first-class functions. JavaScript was
influenced by many languages and was designed to look like Java, but to be
easier for non-programmers to work with.""",
u"""JavaScript, despite the name, is essentially unrelated to the Java
programming language even though the two do have superficial similarities.
Both languages use syntaxes influenced by that of C syntax, and JavaScript
copies many Java names and naming conventions. The language's name is the
result of a co-marketing deal between Netscape and Sun, in exchange for
Netscape bundling Sun's Java runtime with their then-dominant browser. The key
design principles within JavaScript are inherited from the Self and Scheme
programming languages.[3]""",
u"""Due to the widespread success of JavaScript as a client-side scripting
language for web pages, Microsoft developed a compatible dialect of the
language, naming it JScript to avoid trademark issues. JScript added new date
methods to fix the non-Y2K-friendly methods in JavaScript, which were based on
java.util.Date.[2] JScript was included in Internet Explorer 3.0, released in
August 1996. The dialects are perceived to be so similar that the terms
"JavaScript" and "JScript" are often used interchangeably. Microsoft, however,
notes dozens of ways in which JScript is not ECMA compliant.""",
u"""avaScript supports all the structured programming syntax in C (e.g., if
statements, while loops, switch statements, etc.). One partial exception is
scoping: C-style block-level scoping is not supported. JavaScript 1.7,
however, supports block-level scoping with the let keyword. Like C, JavaScript
makes a distinction between expressions and statements.""",
u"""Inner functions (functions defined within other functions) are created
each time the outer function is invoked, and variables of the outer functions
for that invocation continue to exist as long as the inner functions still
exist, even after that invocation is finished (e.g. if the inner function was
returned, it still has access to the outer function's variables) - this is the
mechanism behind closures within JavaScript.""",
]

orald_mstndesc    = \
[
u"""
- Fix the quickstub dependencies: when multiple targets are listed for a single rule, GNU make doesn't run the rule once and combine the targets: instead, it builds each target separately. This only really matters in parallel builds where targets may be evaluated in parallel. r=ted
specialize code for a specific global object, not just a global object shape (480905, r=graydon).
maintain globalShape in VMFragment only (486049, r=graydon).
When building with pymake, use gmake for NSS because of the pain and suffering on Windows.
Guard that object is a dense array when skipping to its prototype during property lookup (485790, r=brendan).
. Removing getBoxObjectFor from non-XUL documents. r+sr=bzbarsky
Backed out changeset 0b36bddcefe4 for to fix compiletaion errors on some platforms.
""",
u"""
- Assertion failure: newlen == 0 || obj->dslots[newlen - 1] != JSVAL_HOLE, at ../jsarray.cpp.  Modify an assertion to properly handle intentional fenceposting behavior where we copy 0 elements to the end of an array -- can't assert that the end of the array isn't a hole in this case because we're intentionally not changing the array from what it was before -- demonstrated by [,].splice(1).  r=me as obvious from debugging the testcase
Remove all traceable natives from jsstr.cpp that don't have any fast path code in them (463238 part 2, r=brendan).
- Specialize array methods which modify large numbers of array elements to work efficiently on dense arrays, avoiding highly generalized get/set/delete methods and the floating-point-to-integer conversions needed solely to handle large array indexes but which are rarely necessary in practice.  r=shaver
Make sure stack frame is flagged as constructor frame when falling off trace in a slow native constructor (491965, r=graydon).
""",
u"""
- figure out how to get crash stacks from xpcshell tests. r=bsmedberg
- TM: widen LIR instructions. Sparc Changes. r=gal. remove dead codes
- Don't optimize group assignment given holey RHS (r=igor).
: Propagate errors from tracer to interpreter. r=igor
- Reject (JSON is fixed now) E4X masquerading as JS source (r=igor/mrbkap).
""",
u"""
js_SetPropertyHelper does not null *entryp for read-only properties (489171, r=gal,brendan).
- "Assertion failure: dn->pn_defn, at ../jsemit.cpp" (r=mrbkap).
- Restore missing check for un-optimiziable frames. r=brendan
Abort trace if the global object gets wrapped and we already hold a reference to the unwrapped object (489007, r=brendan).
- Followup readability fix to rearrange the ordering of cases in various type-switch statements to correspond to numeric values; this makes it much easier (for me at least) to see that such switches are properly exhaustive.  r=gal
Sun Studio is not recognized if $CC, $CXX are not set r=jim
Backed out changeset a6071b1aa626 due to trace-test.js failures.
""",
u"""
Backed out changeset 5bd116148175 (attempting to re-land ).
Remove unsafe RegExp.test traceable native, the generic fast native mechanism can take care of it (488703, r=jorendorff).
- should _tzset on Win32, follow up to fix windows ce bustage r=crowder
Merge tracemonkey to mozilla-central.
Fix occasional leak of either array or hashtable entrystore allocated in js_AddLocal by accounting for fun->u.i.upvars in DestroyLocalNames.  ()  r=brendan
Backout changeset 143e997c858e () because it caused crashes on Mac tinderboxen.
Thread-safety comment for . r=brendan.
""",
]

orald_verdesc     = \
[
u"""
Fix for (Avoid hash lookups in XPCWrappedNative::GetNewOrUsed). r=bz, sr=jst.
Backed out changeset fbb48d6a27e3
- Initializing non-int elements calls the wrong imacro. Also call the right builtin when setting and initializing non-int properties (r=brendan).
Always check operation callback on backwards branches (484035, r=brendan).
Don't crash on non-primitive array indexes (484120, r=jwalden).
- Use core_abspath and $(CURDIR) instead of shells. Use Preprocessor.py instead of preprocessor.pl to avoid perl insanity with pymake, and generally just make me happy. r=ted
Use lir->insImmf and emit ins_eq0 centrally in guard() (483365, r=brendan).
""",
u"""
Back out 480132: orange on Linux
Back out fix for 481444; orange on Linux TraceMonkey unit test: http://tinderbox.mozilla.org/showlog.cgi
triggering tinderbox rebuild for to check if orange there persists
Crash [@ jsds_SyncFilter(FilterRecord*, jsdIFilter*) ] when appendFilter() called with Console2 installed
Crash [@ jsds_SyncFilter(FilterRecord*, jsdIFilter*) ] when appendFilter() called with Console2 installed
- Quickstub additional properties on nsIDOMHTMLAnchorElement and nsIDOMNSHTMLAnchorElement, r=bz
Check for non-stub getters/setters in SETNAME and SETPROP and invoke SetPropHit after setting the property in INITPROP (481989, r=brendan).
""",
u"""
Assert prototype shapes when reading a hole from a dense array instead of calling a builtin (481328, r=brendan).
Take out printfs. no relation to orange
A little helper function to make life in gdb more bearable (DEBUG only, no bug, r=danderson).
Make arrays with less than 256 entries always dense (479386, r=brendan).
Fixed emitTreeCall crashing on deep aborts (, r=gal).
- Integrate sparc nanojit intro tracemonkey. Put the flush instruction cache code to the correct place. r=gal
""",
u"""
- in order to exclude randam passes on platforms that do not support jit, require jit time to be less than 1/2 non jit time in order to pass.
No longer need these gcparam calls to improve performance.  In fact, even on hardware with a lot of RAM we're faster running the mandelbrot tests without these calls.
Kill trailing whitespace in jstracer.h to kick a box out of a bogus orange
Backout . Causes a massive slowdown in trace-tests.js that needs to be investigated.
Add debug hook to the threaded interpreter to trace instruction stream (476128, r=shaver).
""",
u"""
Backed out changeset d50d3681b94e (attempted re-landing of 474771).
-  TM: Assertion failed: "Should not move data from GPR/XMM to x87 FPU": false (../nanojit/Nativei386.cpp:1851) (js_BooleanOrUndefinedToNumber emitted twice). r=brendan.
- TM: js_FastValueToIterator and js_FastCallIteratorNext can reenter. r=brendan. Note that this changeset alone does not fix the bug; an upcoming patch in completes the fix.
Correct incorrectly reversed order of argument types in builtin description (472533, r=brendan).
Fixed multitrees assert regression from (, r=gal).
Fixed correctness and leak regression from landing (, r=gal, relanding).
""",
]

orald_comments    = \
[
u"""
Fix typo (494956, r=self, thanks to <soubok@gmail.com> for bug report).
""",
u"""
- Uninitialized variable undefined after assignment whose initializer is a closure capturing that var (r=mrbkap).
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
LIR_alloc doesn't get emitted correctly for stack args on ARM (494510, r=vlad).
""",
u"""
- TM: Lower maximum LIR skip size further, r=gal.
""",
u"""
- js1_5/Regress/regress-344959.js - with and eval do not inhibit the flat closure optimization. r=brendan.
""",
u"""
- [jsd] incorrect lineExtent when a while loop ends a method (r=mrbkap).
""",
u"""
: correcting native stack navigation arithmetic, r=gal
""",
u"""
Re-landing backed out part of for parity with 1.9.1
""",
u"""
Fix for . r/sr=mrbkap.
""",
u"""
: Add new js/src/ref-config makefile for HP-UXB.11.31.  NPOB.
""",
u"""
Backing out part of to see if this part is what caused the performance regression.
""",
u"""
- Static libs such as libxpcomglue_s are not shipped in the XUL SDK: revert the parts of which were too eager: we still use dist/sdk/lib and dist/sdk/bin, just not dist/sdk/include or dist/sdk/idl, r=ted
""",
u"""
Merge backout of changeset 1abeb6c87131 (-  Implement a wrapper for exposing chrome objects to content (aka COWs)) due to mochitest failures and leaks.
""",
u"""
Backed out changeset 1abeb6c87131 (-  Implement a wrapper for exposing chrome objects to content (aka COWs)) due to mochitest failures and leaks.
""",
u"""
-  Implement a wrapper for exposing chrome objects to content (aka COWs). r+sr=jst sr=bzbarsky on some parts.
""",
u"""
b=494095; use -O3 for Mac builds; r=sayrer
""",
u"""
Merge.
""",
u"""
Setting scopeChain to NULL in SynthesizeFrame breaks GetCallObject (494045, r=brendan).
""",
u"""
Fix GCC warnings about the argument to %p not being a void *. rs=jorendorff
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
- js_DumpStackFrame. r=Waldo.
""",
u"""
Wrong callee is restored when side-exiting from a trace (493657, r=brendan,mrbkap).
""",
u"""
- using the proper assert to assert the the GC is not running. r=mrbkap
""",
u"""
- NJ: Minimal fix to sign-extension in imm64, r=gal.
""",
u"""
Backout alignment-breaking patches for .
""",
u"""
: the real fix for problem left in wake of patch for (r=mrbkap).
""",
u"""
- Followup to ARM and SPARC native backends, to handle renaming, r=gal.
""",
u"""
- NJ: Fix sign-extension in imm64, r=graydon.
""",
u"""
Merge.
""",
u"""
Backed out changeset 8f6c242a75ff (backing out again).
""",
u"""
Merge.
""",
u"""
Backed out changeset c4cea7365f4e (re-landing 493657).
""",
u"""
Back out patch for 493760, chrome mochitests failed.
""",
u"""
Merge.
""",
u"""
Backed out changeset cec8ee353407 ().
""",
u"""
- TM: Crash [@ TraceRecorder::test_property_cache] (r=gal).
""",
u"""
Wrong callee is restored when side-exiting from a trace (493657, r=brendan).
""",
u"""
: fix bad typo in patch for (superluminal r=mrbkap).
""",
u"""
Fix quickstubs dependency problem, .h doesn't depend on any headers so don't add it to .dep and make .cpp depend on the interface files instead. rs=ted.
""",
u"""
-  Assertion failure: (cx)->requestDepth || (cx)->thread == (cx)->runtime->gcThread, at mozilla/js/src/jsapi.cpp:5196, r+sr=mrbkap
""",
u"""
Back out patch for 493760, chrome mochitests failed.
""",
u"""
- TM: Crash [@ TraceRecorder::test_property_cache] (r=gal).
""",
u"""
: fix bad typo in patch for (superluminal r=mrbkap).
""",
u"""
- 'XPCWrappedNativeScope creates a needless cycle with its principal provider.' r=peterv, sr=jst.
""",
u"""
gmake 3.80 bustage fix for r=bsmedberg
""",
u"""
- TM: youtube.com customization broken (r=mrbkap).
""",
u"""
. JSON.parse replacer function doesn't elide object values correctly. r=brendan
""",
u"""
Update JSSLOT_ARRAY_COUNT when emitting array constructor code on trace (493255, r=jorendorff).
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
Backout last cset. is not ready yet.
""",
u"""
- TraceMonkey: The ARM-specific Assembler::BL method is never called. r=vlad
""",
u"""
- nanojit: convert some error() tests to asserts. r=edwsmith
""",
u"""
-  nanojit: move Assembler::findVictim() from RegAlloc.cpp to Assembler.cpp
""",
u"""
-  nanojit: remove reservation table. r=gal,edwsmith
""",
u"""
-  nanojit: improve handling of 64-bit constants. r=graydon
""",
u"""
-  nanojit: remove some dead code. r=edwsmith
""",
u"""
-  nanojit: remove duplicated LIns predicates. r=edwsmith
""",
u"""
-  TraceMonkey: Improve epilogue efficiency for ARM. r=vlad
""",
u"""
b=490296; small fixup to asm_ldr_chk -- we can do PC-relative loads as long as the offset fits in U12; r=me
""",
u"""
b=490296; [arm] tidy misc insn generation macros; r=vlad
""",
u"""
b=490296; [arm] tidy ::asm_ld_imm; r=vlad
""",
u"""
Compilation fix.
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
- Make SOWs wrap more deeply. r+sr=jst
""",
u"""
- flatten dist/include and provide mechanism to install certain headers in namespaced subdirectories (e.g. #include "mozilla/XPCOM.h") r=ted
""",
u"""
: Build fixes for Symbian in js/src patch=harry.li r=jimb
""",
u"""
- fixing miscellaneous warnings. r=biesi
""",
u"""
Fix for (Possible to GC way too much during shutdown due to XUL and XBL prototypes). r/sr=bz.
""",
u"""
- fixing !JS_THREADSAFE build failure. r=mrbkap.
""",
u"""
Fix for (Windows stay alive too long because nsJSContext doesn't unlink correctly). r=bent, sr=jst.
""",
u"""
Fix compiler warning (493345, r=brendan).
""",
u"""
- Browser crashes in loading of certain page.[@ js_Interpret] (r=mrbkap; take 2).
""",
u"""
Back out last cset.
""",
u"""
- Browser crashes in loading of certain page.[@ js_Interpret] (r=mrbkap).
""",
u"""
Merge backout.
""",
u"""
Backed out changeset 0c8d4f846be8 (Fix for (Windows stay alive too long because nsJSContext doesn't unlink correctly).) to try to fix Tshutdown regression.
""",
u"""
- localStorage's constructor should be Storage, r+sr=jst
""",
u"""
Merge 
""",
u"""
- Should make global data const where possible; xpconnect; r=brendan
""",
u"""
- Random cleanup in jsdbgapi.cpp. r=sayrer
""",
u"""
- Clean up the way that TraceRecorder::elem interacts with the rest of the world. r=gal
""",
u"""
- let declaration getting lost in certain situations (r=mrbkap).
""",
u"""
Comment typo fix in tracemonkey.
""",
u"""
- Expose js_StrictlyEqual() to consumers. r=mrbkap.
""",
u"""
. Tidy ::asm_fop (v2). r=vlad.
""",
u"""
. Tidy ::asm_ldr_chk (v2). r=vlad.
""",
u"""
. Tidy ::asm_prep_fcall. r=vlad.
""",
u"""
. Tidy ::LD32_nochk. r=vlad.
""",
u"""
. Tidy ::asm_quad. r=vlad.
""",
u"""
Tidy ::asm_load64. r=vlad.
""",
u"""
Tidy ::asm_restore. r=vlad.
""",
u"""
. Tidy ::asm_nongp_copy. r=vlad
""",
u"""
- statically assert that we're not on trace in js_SetPropertyHelper, r=igor
""",
u"""
- mutating parent chain shapes only for Call objects and only when adding properties that are not parameter or var names. r=brendan
""",
u"""
Backed out changeset 5e867032abe5 (Fix for (Possible to GC way too much during shutdown due to XUL and XBL prototypes).) to try to fix Tshutdown regression.
""",
u"""
Backed out changeset 3e3d2d8cc70f (- fixing !JS_THREADSAFE build failure.) to try to fix Tshutdown regression.
""",
u"""
- TM: Fix memory pressure measurement, r=brendan.
""",
u"""
- "Assertion failure: cg->staticLevel >= level, at ../jsemit.cpp" with genexp. r=brendan
""",
u"""
- sharing object map for non-native objects. r=brendan
""",
u"""
- fixing !JS_THREADSAFE build failure. r=mrbkap.
""",
u"""
- TM: trace aborts due to flat closure analysis bug (r=mrbkap).
""",
u"""
Only the global object has to be wrapped on trace, which we can do statically and abort on With objects used as 'this' (492028, r=mrbkap).
""",
u"""
, r=mrbkap, sr=jst
""",
u"""
Rename jsdtracef.c to jsdtracef.cpp r=sayrer
""",
u"""
- Suspected Txul regression from JS engine changes (r=igor).
""",
u"""
Use js_TrashTree when purging global scripts (492496, r=graydon).
""",
u"""
- fixing bad typo in js_SetProtoOrParent. r=mrbkap
""",
u"""
Clear temporary rooting area after native calls on trace (492693, r=jwalden).
""",
u"""
Don't try to compile more code once we are in a needFlush state (492664, r=dmandelin).
""",
u"""
- Give regular JS objects that have been reflected into C++ a security policy that follows the same-origin model. Also teach caps about "same origin" for these cases. r=jst sr=bzbarsky
""",
u"""
Sync config.guess with latest from gnu "config" package. See bug for changelog. b=492623 r=ted
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
Backed out changeset c8a74fe0f9af ().
""",
u"""
Don't try to compile more code once we are in a needFlush state (492664, r=dmandelin).
""",
u"""
: correctly determine when an upvar is part of the trace, r=brendan
""",
u"""
- Recording of JSOP_NEWARRAY doesn't update JSSLOT_ARRAY_COUNT properly.  r=jorendorff
""",
u"""
Fix Windows CE from (arm architecture detection)
""",
u"""
- TM: widen LIR instructions. Sparc Changes. r=gal. remove dead codes
""",
u"""
- TM: widen LIR instructions. Sparc Changes. r=gal.
""",
u"""
: updating test case to pass when we successfully trace out-of-reach upvars
""",
u"""
Fix warning for extra args to a debug printf
""",
u"""
: enable tracing of upvar accesses that go outside the current trace to interpreter state, r=gal
""",
u"""
Ensure that cx->interpState is always accurate by maintaing a stack (490776, r=jorendorff).
""",
u"""
: make traces specialized for argc, r=gal
""",
u"""
Likely gmail bustage fix
""",
u"""
- Specialize array methods which modify large numbers of array elements to work efficiently on dense arrays, avoiding highly generalized get/set/delete methods and the floating-point-to-integer conversions needed solely to handle large array indexes but which are rarely necessary in practice.  r=shaver
""",
u"""
Make sure stack frame is flagged as constructor frame when falling off trace in a slow native constructor (491965, r=graydon).
""",
u"""
Fast-path for string constructors only works for new/call with a single argument (491989, r=dmandelin).
""",
u"""
- TM: chiptune causes Assertion failure: \!ti->typeMap.matches(ti_other->typeMap)
""",
u"""
-  Remove ARM-specific code from jstracer.cpp. r=vlad
""",
u"""
- figure out how to get crash stacks from xpcshell tests. r=bsmedberg
""",
u"""
Fix Windows CE from (arm architecture detection)
""",
u"""
- TM: widen LIR instructions. Sparc Changes. r=gal. remove dead codes
""",
u"""
- TM: widen LIR instructions. Sparc Changes. r=gal.
""",
u"""
- fixing xpcshell error message; r=ted.mielczarek sr=cbiesinger
""",
u"""
Fix for (Possible to GC way too much during shutdown due to XUL and XBL prototypes). r/sr=bz.
""",
u"""
Fix for (Windows stay alive too long because nsJSContext doesn't unlink correctly). r=bent, sr=jst.
""",
u"""
; JS Windows CE bustage fix
""",
u"""
- Unexpected error occurred when japascript.options.strict is true (r=mrbkap).
""",
u"""
-  TraceMonkey: Improve run-time detection of ARM processor features. r=vlad
""",
u"""
-  TraceMonkey: The ARM-specific _nSlot pointer should be reset along with _nIns. r=vlad,edwsmith
""",
u"""
- TraceMonkey: ARM BKPT instructions are not properly encoded. r=vlad
""",
u"""
- TM: widen LIR instructions. r=graydon,edwsmith
""",
u"""
- "Assertion failure: slot < fp->script->nslots, at ../jsinterp.cpp" with defineGetter, eval (r=mrbkap).
""",
u"""
- TM: unit tests should gc() before each, to purge JIT state, r=brendan.
""",
u"""
- regression (from firefox 2): prototype setters not called by inline cache for [[put]] (r=mrbkap).
""",
u"""
- Packed JS that works in Firefox 3.0 and all other browsers fails in Firefox 3.5 (r=mrbkap).
""",
u"""
- js_Execute must bail off trace, r=jorendorff a=josh for CLOSED TREE checkin
""",
u"""
- E4X and imacros don't mix.  r=graydon
""",
u"""
- Don't optimize group assignment given holey RHS (r=igor).
""",
u"""
- "Assertion failure: (uintN)i < ss->top, at ../jsopcode.cpp" with uneval, for, yield (r=mrbkap).
""",
u"""
- TM: Oracle bit vector allocation not thread-safe, r=gal.
""",
u"""
- Packed JS that works in Firefox 3.0 and all other browsers fails in Firefox 3.5 (r=mrbkap).
""",
u"""
- "Assertion failure: slot < fp->script->nslots, at ../jsinterp.cpp" with defineGetter, eval (r=mrbkap).
""",
u"""
- regression (from firefox 2): prototype setters not called by inline cache for [[put]] (r=mrbkap).
""",
u"""
- Unexpected error occurred when japascript.options.strict is true (r=mrbkap).
""",
u"""
- js_Execute must bail off trace, r=jorendorff a=josh for CLOSED TREE checkin
""",
u"""
- Don't optimize group assignment given holey RHS (r=igor).
""",
u"""
- "Assertion failure: (uintN)i < ss->top, at ../jsopcode.cpp" with uneval, for, yield (r=mrbkap).
""",
u"""
- TM: Store recording attempts in a long-lived hashtable rather than fragments, r=brendan.
""",
u"""
Fix up whitespace. CLOSED TREE
""",
u"""
-  [native JSON] allow to blacklist keys by name when encoding to JSON. r=brendan
""",
u"""
Partial typemap in loop exit can lead to maltyped nested trees (489682, r=gal).
""",
u"""
- Followup, change from sizeof(LIns*) to sizeof(LIns), r=gal.
""",
u"""
We don't constant fold math on doubles and ints (465286, r=edwsmith).
""",
u"""
- fixing shared setter regression and eliminating several useless anonymous prototype objects. r=brendan
""",
u"""
- Lower skip limit in tracer, r=gal.
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
- Expose this as a friendly API. r=gal
""",
u"""
Follow-up fix for 479888.
""",
u"""
kill builtins.tbl (479888, r=jorendorff).
""",
u"""
Fix burning static analysis tinderbox (no bug).
""",
u"""
Record all calls to native functions (487134, r=gal, brendan).
""",
u"""
Switch HTML mochitests from using MochiKit.js to packed.js.  ()  r=sayrer
""",
u"""
Merge tracemonkey to mozilla-central
""",
u"""
: Avoid 'may be used uninitialized' error. (no r)
""",
u"""
Backed out changeset 6534f8b9aa74 (, assert on startup).
""",
u"""
- fixing shared setter regression and eliminating several useless anonymous prototype objects. r=brendan
""",
u"""
- asserting in js_SetProtoOrParent only when not detecting cycles. r=brendan
""",
u"""
ug 490741 - Crash [@ js_GetUpvar] on datepick (r=mrbkap).
""",
u"""
- consolidating
""",
u"""
- Allow easy building of Narcissus through the autoconf build system. r=jimb
""",
u"""
, followup - copy changes to js/src/config as well to fix JS test bustage
""",
u"""
: Redirect stderr of 'cat' to /dev/null in configure.in's check for GCC pipe support. r=ted
""",
u"""
trivial follow-up: remove unneeded 'typedef' keyword to fix compile warning. r=bnewman sr=mrbkap
""",
u"""
ug 490741 - Crash [@ js_GetUpvar] on datepick (r=mrbkap).
""",
u"""
bug - 488607
""",
u"""
: Fix bustage: any function using TRACE_2 needs an 'error' label.
""",
u"""
: Propagate errors from tracer to interpreter. r=igor
""",
u"""
We don't cache access to shared properties in the property cache (490666, r=igor,brendan).
""",
u"""
- Reject (JSON is fixed now) E4X masquerading as JS source (r=igor/mrbkap).
""",
u"""
- optimizing shape prediction for set opcodes. r=brendan
""",
u"""
- Remove code duplication in xpcjsruntime.cpp.
""",
u"""
- Remove code duplication in xpcjsruntime.cpp.
""",
u"""
- Reject (JSON is fixed now) E4X masquerading as JS source (r=igor/mrbkap).
""",
u"""
Eliminate test_property_cache_direct_hit (490370, r=jorendorff).
""",
u"""
- Unexpected ReferenceError when using "new Function()" (r=mrbkap).
""",
u"""
Backout a seemingly problematic line of cset d8c2060b0f9b.
""",
u"""
- TM: Add deep-bailing write barrier to global shape change code, r=brendan.
""",
u"""
js_NewInstance locks ctor on trace (490092, r=brendan).
""",
u"""
Compilation fix for 489899.
""",
u"""
Stay on trace when reading holes from dense arrays (489899, r=brendan).
""",
u"""
- Simulate CFG in imacro assembler and decompiler, r=brendan.
""",
u"""
- TM: Add global size check to global shape check, r=gal.
""",
u"""
- Don't go slow if we don't have to.  r=jorendorff
""",
u"""
- Local Scope Variables are not displayed by default (r=mrbkap).
""",
u"""
Remove dead code inside #if 0 from JSOP_GENERATOR (cleanup, no bug).
""",
u"""
Fix burning PowerPC builds.
""",
u"""
Need an API exposed to control code cache size (474497, r=bent,brendan, sr=mrbkap).
""",
u"""
- Earth Day Recycling for Fun Kids - Assertion failure: RecycleFuncNameKids, at ../jsparse.cpp:444 (r=mrbkap).
""",
u"""
- Change tm.onTrace to tm.tracecx. r=brendan.
""",
u"""
JSOP_BINDNAME wrongful abort due to fp->fun instead of fp->callee usage (489644, r=brendan).
""",
u"""
- Add (TUnit) 'xpcshell-tests' |make| target, using |runxpcshelltests.py| new '--manifest' option; (Iv1a-MC) Update '.PHONY' target too; r=ted.mielczarek
""",
u"""
backout 
""",
u"""
- Unexpected ReferenceError when using "new Function()" (r=mrbkap).
""",
u"""
- Add (TUnit) 'xpcshell-tests' |make| target, using |runxpcshelltests.py| new '--manifest' option; (Hv1a) Stop XPCSHELL_TESTS execution by 'check' target; r=ted.mielczarek
""",
u"""
, move contextmenu listener to system event group, r=enn, sr=neil
""",
u"""
: add programmatic control of profiler to xpcom unit tests. r=bsmedberg
""",
u"""
sync up js/src/config/config.mk with config/config.mk
""",
u"""
b=488608; enable jemalloc on CE6; r+sr=stuart
""",
u"""
Backed out changeset 1eec75c27e2f
""",
u"""
b=488608; enable jemalloc on CE6; r+sr=stuart
""",
u"""
Fix for (Typo in dom_quickstubs.qsconf). r=bent, sr=mrbkap.
""",
u"""
- Distinguish between "there is no JS code running" and "there are only native frames on the stack." Also clean up the rest of the code's handling of null fp.
""",
u"""
- Move native anonymous content checks into a wrapper so that quickstubs don't sidestep them. r=jst sr=bzbarsky
""",
u"""
- Local Scope Variables are not displayed by default (r=mrbkap).
""",
u"""
- Earth Day Recycling for Fun Kids - Assertion failure: RecycleFuncNameKids, at ../jsparse.cpp:444 (r=mrbkap).
""",
u"""
- Don't call into JS when asked if we support a wrapper cache. r+sr=peterv
""",
u"""
- fixing error reporting for getter-only properties. r=mrbkap sr=jst
""",
u"""
- SPARC jit: testIntOverflow, testIntUnderflow failed. r=gal.
""",
u"""
Shoot me now (489089).
""",
u"""
: Only trace where BINDNAME will choose the global object.
""",
u"""
Trace getting String.length (484332, r=brendan).
""",
u"""
- Google Calendars disappear with latest trunk of Shredder [Error: Error parsing XML streamReferenceError: gCal is not defined] (r=mrbkap).
""",
u"""
Oh for crying out loud (489089).
""",
u"""
- JSON.parse is way slower than it needs to be  (r=igor/sayrer).
""",
u"""
Use an XPCOM array enumerator instead of rolling our own r+sr=mrbkap
""",
u"""
- Google Calendars disappear with latest trunk of Shredder [Error: Error parsing XML streamReferenceError: gCal is not defined] (r=mrbkap).
""",
u"""
- [@ js_RemoveRoot - ... - XPCThrower::ThrowExceptionObject] xpconnect is misusing nsCOMPtr. r=jonas+sr=jst
""",
u"""
- "Assertion failure: cg->lexdeps.lookup(atom), at ../jsemit.cpp" (tachyonal r=mrbkap).
""",
u"""
Leaving outermost request should js_LeaveTrace (480301, r=brendan).
""",
u"""
Fix dangling JS_PROPERTY_CACHE_METERING bits broken by patch for .
""",
u"""
js_SetPropertyHelper does not null *entryp for read-only properties (489171, r=gal,brendan).
""",
u"""
- "Assertion failure: dn->pn_defn, at ../jsemit.cpp" (r=mrbkap).
""",
u"""
- Restore missing check for un-optimiziable frames. r=brendan
""",
u"""
- Remove an unnecessary guard, specialize tracing of typeof for functions now that JSVAL_TFUN exists.  r=gal
""",
u"""
- Check for string indexes in the API entry points. r=brendan
""",
u"""
-- fix build system to use NTDDI_VERSION instead of random checks -- part 2, define MOZ_WINSDK_TARGETVER and error out if the SDK is too old. r=bsmedberg
""",
u"""
- Restore missing check for un-optimiziable frames. r=brendan
""",
u"""
Abort trace if the global object gets wrapped and we already hold a reference to the unwrapped object (489007, r=brendan).
""",
u"""
Remove bogus assert (489040, r=brendan).
""",
u"""
- js_GenerateShape just schedules, not run, the GC. r=brendan,gal
""",
u"""
Backed out changeset f4662701526b () to fix !JS_THREADSAFE compilation errors
""",
u"""
- js_GenerateShape just schedules, not run, the GC. r=brendan,gal
""",
u"""
Kick tinderboxen out of a Linux orange that looks bogus
""",
u"""
- Followup readability fix to rearrange the ordering of cases in various type-switch statements to correspond to numeric values; this makes it much easier (for me at least) to see that such switches are properly exhaustive.  r=gal
""",
u"""
- Add a trace-time type to differentiate functions from objects.  r=brendan
""",
u"""
- Rejigger how guards use side exits, and fix an erroneous comment.  r=graydon
""",
u"""
- caching only white-listed non-globals on the scope chain. r=brendan
""",
u"""
- NativeGet caching fixes. r=brendan
""",
u"""
- js/src/Makefile.in DESTDIR support. r=jim
""",
u"""
- fix some of the jemalloc windows build madness. r=bsmedberg
""",
u"""
- fix some of the jemalloc windows build madness. r=bsmedberg
""",
u"""
- content canvas getImageData always returns null from chrome context; r+sr=mrbkap
""",
u"""
Sun Studio is not recognized if $CC, $CXX are not set r=jim
""",
u"""
Failed to compile firefox on Solaris r=bsmedberg
""",
u"""
: crash due to JSString INIT macros stomping deflated flag, r=brendan
""",
u"""
During trecording detect null 'this' object before wrapping it (488816, r=brendan).
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
-  TM: "Assertion failure: !JS_TRACE_MONITOR(cx).needFlush, at ../jstracer.cpp". r=gal.
""",
u"""
- Missing write barrier on global object, r=jorendorff.
""",
u"""
Merge.
""",
u"""
Backed out changeset 324bb9dc8372 (is implicated in top site failures).
""",
u"""
Fix "unused variable tm" warning I introduced a few days ago. No bug#, r=shaver.
""",
u"""
Merge backout.
""",
u"""
Backed out changeset a6071b1aa626 due to trace-test.js failures.
""",
u"""
Fix static-analysis-tracemonkey burning due to a6071b1aa626.
""",
u"""
- TM: "Assertion failure: !JS_TRACE_MONITOR(cx).needFlush, at ../jstracer.cpp". r=gal.
""",
u"""
- updating the tests to rfelect the new restriction on the maximum string length. r=bclary
""",
u"""
- removal of JSSLOT_ARRAY_LOOKUP_HOLDER. r=mrbkap
""",
u"""
- Crash at [@js_Interpret] on YOMIURI ONLINE (r=mrbkap).
""",
u"""
fixup: adding needed macro parens
""",
u"""
Merge.
""",
u"""
Backed out changeset 5bd116148175 (attempting to re-land ).
""",
u"""
: Fix shell bustage, r=brendan
""",
u"""
: avoid unnecessary js_PurgeDeflatedStringCache calls, additional patch to address igor's review issues, r=igor
""",
u"""
Be less paranoid about jit stats for testNestedExitStackOuter since it doesn't seem to be stable.
""",
u"""
Merge.
""",
u"""
When allocating strings, only report error if we can leave trace, otherwise just return NULL (488764, r=jwalden).
""",
u"""
Remove unsafe RegExp.test traceable native, the generic fast native mechanism can take care of it (488703, r=jorendorff).
""",
u"""
- proper rooting of DeclEnv instance. r=brendan
""",
u"""
: call expensive JSString finalizers only if needed, r=brendan
""",
u"""
Properly calculate 'this' object on trace and side exit if we have to wrap (488203, r=mrbkap,jorendorff).
""",
u"""
Backed out changeset d1a4ee3d0c59 (, due to possible leak).
""",
u"""
Backed out changeset 062ea62f9bda (backed out again).
""",
u"""
Backed out changeset 64d7df1fe160 (re-landing 488203).
""",
u"""
Backed out changeset e8c23c42db7f () to see whether it causes the leak.
""",
u"""
Properly calculate 'this' object on trace and side exit if we have to wrap (488203, r=mrbkap).
""",
u"""
- avoiding extra locks for js_Native(Get|Set). r=brendan
""",
u"""
- Remove code duplication in xpcjsruntime.cpp. r=jst sr=brendan
""",
u"""
- Don't call the class getter (especially not the scriptable helper!) for functions. r+sr=jst
""",
u"""
, r+sr=jst
""",
u"""
- PRMJ_Now needs better granularity for panning in fennec r=crowder, robarnold
""",
u"""
- should _tzset on Win32, follow up to fix windows ce bustage r=crowder
""",
u"""
Merging mozilla-central to tracemonkey.  Should fix the red on talos tinderbox.
""",
u"""
- avoiding deadlocks in ClaimTitle. r=brendan
""",
u"""
Backed out changeset f97f196dcb58 - needs more work
""",
u"""
Backed out changeset d1a4ee3d0c59 due to build fail, test fail, and perf regressions.
""",
u"""
- avoiding extra locks for js_Native(Get|Set). r=brendan
""",
u"""
- TM: After deep-bailing, we can lirbuf->rewind() and then return to a dead code page. r=gal.
""",
u"""
- Crash [@ js_ValueToString] or Crash [@ js_ValueToBoolean] or "Assertion failure: slot < fp->script->nslots, at ../jsinterp.cpp" (r=mrbkap).
""",
u"""
- "Assertion failure: \!(pn->pn_dflags & flag), at ../jsparse.h" (r=me).
""",
u"""
- fixing strict mode warnings with DOm window object. r=brendan
""",
u"""
- Crash [@ js_GetUpvar ] (also bogus JS errors, also probably Crash [@js_Interpret]) (future r=mrbkap, see bug).
""",
u"""
Backed out .
""",
u"""
Merge.
""",
u"""
Backed out changeset 4c157cfe2289 ().
""",
u"""
Add missing FASTCALL declaration.
""",
u"""
Fix static analysis. It is ok for ComputeThis_tn to see a stale cx->fp since we just want to ensure the global object is wrapped.
""",
u"""
Properly compute 'this' object on trace and wrap if necessary (488203, r=mrbkap).
""",
u"""
: jsfile.cpp and jsgc.cpp fixes for Symbian patch=Harry.Li r=jimb
""",
u"""
- _tzset on Win32, patch my Mike Perry <mikeperry.unused@gmail.com>, r=crowder
""",
u"""
Fix the PYTHONPATH bits of in a not-hacky way by using a script which can set up the path and then forward to the real script we're trying to run, r=ted
""",
u"""
- Crash [@ RebindLets] (r=mrbkap).
""",
u"""
Back out bad patch for 488272.
""",
u"""
Leaving outermost request should js_LeaveTrace (480301, r=brendan).
""",
u"""
- "Assertion failure: cx->bailExit" with {__proto__: window}. r=brendan.
""",
u"""
- Crash [@ RebindLets] (r=mrbkap).
""",
u"""
- call_enumerate doesn't take upvars into account. r=brendan
""",
u"""
- TM: After deep-bailing, we can lirbuf->rewind() and then return to a dead code page. r=gal.
""",
u"""
- XPCSafeJSObjectWrapper allows regexp variables to be clobbered. r=mrbkap+sr=brendan
""",
u"""
- fixing bindname optimization regression from the plus creating js_DeclEnvClass instances together with Call objects. r=brendan
""",
u"""
Back out 
""",
u"""
failed to compile firefox on Solaris r=bsmedberg
""",
u"""
- get rid of nsSupportsArray; r=sicking, sr=bsmedberg
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
- upvar2: incorrect optimization of delete function_name (r=igor).
""",
u"""
Remove amd64 code (will be replaced with tamarin's new amd64 backend, 487981, r=danderson).
""",
u"""
Import http://hg.mozilla.org/mozilla-central/rev/a94142e82a0d to TM since it seems to be horking my shell builds (but not a browser build?  odd, I thought I'd tested both)
""",
u"""
- TM: shutdown leak of rt->builtinFunctions (r=jorendorff).
""",
u"""
- Crash [@ js_GetUpvar] or "Assertion failure: (script)->upvarsOffset != 0, at ../jsinterp.cpp" (r=mrbkap).
""",
u"""
Update ip in recycled branch fragments (487531, r=graydon).
""",
u"""
Fix occasional leak of either array or hashtable entrystore allocated in js_AddLocal by accounting for fun->u.i.upvars in DestroyLocalNames.  ()  r=brendan
""",
u"""
Potential bustage fix for weird Windows compilers.  r=red
""",
u"""
- fixing JSOP_BINDNAME caching issues. r=brendan
""",
u"""
Backed out changeset 595ebe7b82fa - it had wrong patch
""",
u"""
- fixing JSOP_BINDNAME caching issues. r=brendan
""",
u"""
- js1_5/Regress/regress-366601.js - Internal Error: script too large.  r=brendan
""",
u"""
- Store the last trace PC to pass into the decompiler. r=igor
""",
u"""
- fixing flag propagation to generator expression function. r=brendan
""",
u"""
Fix JS_LONE_INTERPRET-mislocated js_GetUpvar prototype (487563).
""",
u"""
- Crash [@ js_Interpret] (r=mrbkap).
""",
u"""
- Nesting deep-aborting trace calls don't work. r=gal.
""",
u"""
- Delete unnecessary fast natives in js shell. r=gal.
""",
u"""
- More cleanup from and patches (r=mrbkap/igor, and this fixes ).
""",
u"""
: Avoid warnings in jstracer.cpp. r=igor
""",
u"""
: Assert that we never add properties to lexical blocks. r=igor
""",
u"""
- erroneous redeclaration of let ... with try {...} catch(e) {var e...} (r=mrbkap).
""",
u"""
- left three tests broken in its wake (r=mrbkap).
""",
u"""
- TM: "Assertion failure: JSVAL_IS_NULL(v)" with function/regexp used as index.  The other half of , poorly reviewed by me -- no soup for me!  r=graydon
""",
u"""
- Crash [@ js_Invoke ], and missing google-maps background, at padmapper.com (r=mrbkap).
""",
u"""
Bustage fix from last-minute rework of 
""",
u"""
- Fail when imacros.c.out is out of date, r=jorendorff/ted
""",
u"""
- named function objects can escape without detection by the upvar analysis (r=mrbkap).
""",
u"""
: Making undefined use stub getter/setter so use of global undefined can be traced, r=mrbkap
""",
u"""
- Cap size of global object, r=graydon.
""",
u"""
: Use offsetof instead of a magic constant. r=jorendorff
""",
u"""
Merge backout.
""",
u"""
Backout changeset 143e997c858e () because it caused crashes on Mac tinderboxen.
""",
u"""
Merge.
""",
u"""
- TM: Other builtins that call JS_malloc. r=gal.
""",
u"""
Backed out changeset e201de53e918 in favor of a different approach.
""",
u"""
- Remove uses of alloca, r=gal.
""",
u"""
- imacros.c.out generation fails: Error: .igroup/.end name mismatch (r=mrbkap).
""",
u"""
- TM: Assertion failure: cx->bailExit due to _RETRY builtins that call JS_malloc. r=gal, r=igor.
""",
u"""
- named function objects can escape without detection by the upvar analysis (r=mrbkap).
""",
u"""
- A lambda expression that uses arguments might escape, so don't clear the funarg flag. r=brendan
""",
u"""
- imacros.c.out generation fails: Error: .igroup/.end name mismatch (r=mrbkap).
""",
u"""
- TM: Recording continues across loop edge. r=jorendorff
""",
u"""
backout , disable-jit bustage.
""",
u"""
- TM: Recording continues across loop edge. r=jorendorff
""",
u"""
Fix for ("ASSERTION: bad!" in XPCCallContext::XPCCallContext with feed in frame, gc). r/sr=mrbkap.
""",
u"""
Thread-safety comment for . r=brendan.
""",
u"""
- "Deep" property cache entries not invalidated when shadowed (TIBCO General Interface regression). r=brendan.
""",
u"""
- PurgeScopeChain should not deep-bail quite so eagerly (r=jorendorff, a=sayrer).
""",
u"""
Test for upvar2 dup/dep , from comment 8; also remove print noise from testPropagatedFunArgs crash test.
""",
u"""
- always using setError to set _err
""",
u"""
Style nit to kick a red tinderbox and hopefully avoid graph server fail a second time around, r=red this time
""",
u"""
Update trace-test.js jitstats for testThinLoopDemote to account for upvar2, although there's still some wonkiness here being tracked in .  r=orange
""",
u"""
Another static analysis patch (I hope the last; for 452498).
""",
u"""
Remove stale JS_REQUIRES_STACK for js_CloneFunctionObject prototype (452498 followup to fix static analysis tbox).
""",
u"""
upvar2, aka the big one take 2 (452598, r=mrbkap).
""",
u"""
More typo fixes to kick some tinderboxen
""",
u"""
Grammar fix to kick a rando-orange box to green
""",
u"""
- TM: "Assertion failure: scope->object == pobj" with function, __proto__, length.  r=gal
""",
u"""
- TM: avoid frequent mismatch exits. r=brendan
""",
u"""
Merge.
""",
u"""
Backed out changeset 972c44aa9d1f ().
""",
u"""
Merge.
""",
u"""
upvar2, aka the big one (452598, r=mrbkap).
""",
u"""
Merge.
""",
u"""
Backed out changeset b512be855093 (). See bug for details.
""",
u"""
Typo-fix in comment, cycle unit tester.
""",
u"""
TraceRecorder::prop sets stack on some return paths, not on final path (486798, r=brendan).
""",
u"""
- Remove uses of alloca, r=gal.
""",
u"""
- nested function definitions must come after destructuring argument initializer. r=mrbkap
""",
u"""
- removal of JSProperty struct definition. r=mrbkap
""",
u"""
- fixing sharp semantic regressions. r=mrbkap
""",
u"""
Don't try to abort tracing after a successful compilation (486436, r=brendan).
""",
u"""
- TM: JIT embeds stale closure in trace for JSOP_DEFLOCALFUN. r=mrbkap
""",
u"""
- annotating destructuring JSOP_DUP for the decompiler. r=brendan
""",
u"""
: Compute opcode stack usage correctly. r=igor
""",
u"""
: Fix up bytecode execution tracing.  Allow tracing to file. r=igor
""",
u"""
followup - quote things to death, r=bsmedberg
""",
u"""
- Remove bogo-assertion (and fix compilation warning). r=Waldo
""",
u"""
- Add a mochitest.
""",
u"""
- Fix the quickstub dependencies: when multiple targets are listed for a single rule, GNU make doesn't run the rule once and combine the targets: instead, it builds each target separately. This only really matters in parallel builds where targets may be evaluated in parallel. r=ted
""",
u"""
- removal of unsed fields from JSObjectOps. r=mrbkap
""",
u"""
- removal of unused TCF_HAS_DEFXMLNS. r=mrbkap
""",
u"""
- Avoid artificial OOM conditions, r=gal.
""",
u"""
- Property tree forking heuristic improvement, r=brendan.
""",
u"""
- Followup patch to fix crash in initial checkin, r=mrbkap.
""",
u"""
printf warning police
""",
u"""
- TM: "Assertion failure: !OBJ_GET_CLASS(cx, proto)->getObjectOps, at ../jsobj.cpp".  r=mrbkap
""",
u"""
- restoring JS*Lookup API compatibility with fast arrays. r=shaver
""",
u"""
specialize code for a specific global object, not just a global object shape (480905, r=graydon).
""",
u"""
maintain globalShape in VMFragment only (486049, r=graydon).
""",
u"""
- Make JSObjectOps private. r=brendan.
""",
u"""
When building with pymake, use gmake for NSS because of the pain and suffering on Windows.
""",
u"""
- Don't force link jemalloc on windows ce r=ted, crowder
""",
u"""
- Not enough quotes in mozprog.m4 when suggestions contain spaces r=ted
""",
u"""
- Minimize forking of property tree, r=brendan.
""",
u"""
Guard that object is a dense array when skipping to its prototype during property lookup (485790, r=brendan).
""",
u"""
- Incorrect null checking/assignment? (with xpcshell test case).  r=gal
""",
u"""
- TM: Assertion failure: JS_ON_TRACE(cx), at ../jsarray.cpp. r=mrbkap
""",
u"""
- Use C++ style casts in more places. r=brendan
""",
u"""
[OS/2] : fix build break in jsnum.cpp by defining the underscored float properties. r=jorendorff
""",
u"""
- hiding JSCodeSpec.(nuses|ndefs) behind inlines to properly deal with variable stack bytecodes. r=brendan
""",
u"""
- calling the call hook after fully initializing the freame. r=brendan
""",
u"""
- limitting default xml namespace search to var objects as required by e4x. r=brendan
""",
u"""
- TM: Crash [@ js_AttemptCompilation]. r=graydon
""",
u"""
. Removing getBoxObjectFor from non-XUL documents. r+sr=bzbarsky
""",
u"""
Fix style inconsistency I just introduced in 
""",
u"""
- Protect against reentrancy in deferred releases. r+sr=roc
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
Back out - 'Trace string.indexOf'. It conflicts badly with mozilla-central.
""",
u"""
backing out 273c85c827e1
""",
u"""
- Fix a few minor gcc warnings. r=igor
""",
u"""
b=484599; add calling convention tests to trace-tests and js shell; r=mrbkap
""",
u"""
b=484561; [arm] fix EABI calling convention; clean up asm_call; r=graydon
""",
u"""
b=484561; [arm] fix broken LIR_alloc; r=graydon
""",
u"""
b=484599; TM: memory stomping when a tn called with > 5 args; r=gal
""",
u"""
- jsdate.cpp AdjustTime() breaks London (GMT+0) dates when DST activates Mar 29 2009 Summary: jsdate.cpp AdjustTime() breaks London (GMT+0) dates when DST activates Mar 29. r=mrbkap
""",
u"""
Make js_DumpValue more useful with function jsvals.  r=mrbkap
""",
u"""
- proper stack limits for scatter threads. r=mrbkap
""",
u"""
Backed out changeset 0b36bddcefe4 for to fix compiletaion errors on some platforms.
""",
u"""
- proper stack limits for scatter threads. r=mrbkap
""",
u"""
- allow calling JS_DestroyContext when cx->thread is null for API compatibility. r=brendan
""",
u"""
- PutProperty E4X correctness fix. r=brendan
""",
u"""
- fixing the assert about the structure of sharp nodes. r=brendan
""",
u"""
- 'Trace string.indexOf'. r=brendan+gal.
""",
u"""
- 'Add properties with getters and setters to the shell'. r=gal.
""",
u"""
Add a static assertion for another latent LIR opcode numbering constraint.  No bug, r=mrbkap
""",
u"""
Clean up JS ID code and fix allocators r=mrbkap sr=jag
""",
u"""
- remove references to MOZ_PROFILE from the build system; (Cv2-MC) the 8 files; r=ted.mielczarek
""",
u"""
- [OS/2] simplify test_os2.cmd; r=mozilla@Weilbacher.org
""",
u"""
- We can get an interface but no member without idispatch. r+sr=jst
""",
u"""
Fix bogus debug assertions from r+sr=peterv
""",
u"""
- get rid of nsVoidArray, xpconnect part; r+sr=mrbkap
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
fix static analysis. r=gal
""",
u"""
forcing tinderbox re-run to check if indeed caused Windows orange
""",
u"""
- JSThread is no longer shared between JSRuntime instances. r=brendan
""",
u"""
- property cache fix. r=brendan
""",
u"""
- modify test to deal with new SyntaxError: duplicate argument is mixed with destructuring pattern error.
""",
u"""
- Assertion failure: newlen == 0 || obj->dslots[newlen - 1] != JSVAL_HOLE, at ../jsarray.cpp.  Modify an assertion to properly handle intentional fenceposting behavior where we copy 0 elements to the end of an array -- can't assert that the end of the array isn't a hole in this case because we're intentionally not changing the array from what it was before -- demonstrated by [,].splice(1).  r=me as obvious from debugging the testcase
""",
u"""
Modify code which produces |if (cond);| in non-debug builds to not expand into an empty control statement.  r=sparky
""",
u"""
- Some array methods don't work right on ginormous arrays.  r=brendan
""",
u"""
- new String(obj) asserts when tracing.  r=brendan, r=gal
""",
u"""
- duplicated arguments no longer supported when destructuring pattern is used. r=brendan
""",
u"""
Backed out changeset e117c22cc1d1 - the landed patch for has a shutdown leak.
""",
u"""
- JSThread is no longer shared between JSRuntime instances. r=brendan
""",
u"""
Don't reason about fragment when deep aborting (484543, r=brendan).
""",
u"""
b=484561; [arm] minimal fix to get LIR_alloc working
""",
u"""
Property close loops even in the presence of partially constant loop conditions (482800, r=brendan).
""",
u"""
Don't attempt to call fast native constructors on trace (484531, r=brendan).
""",
u"""
Can't allocate new stack chunks while on trace (484524, r=brendan).
""",
u"""
arm bustage fix
""",
u"""
Remove all traceable natives from jsstr.cpp that don't have any fast path code in them (463238 part 2, r=brendan).
""",
u"""
Support calling arbitrary JSFastNatives from trace (463238, r=brendan).
""",
u"""
trace JSOP_CALLELEM (484334, r=mrbkap)
""",
u"""
str_match should use js_GetCurrentBytecodePC (484308, r=mrbkap).
""",
u"""
Make new String() trace (484333, r=brendan).
""",
u"""
void -> bool
""",
u"""
call underrunProtect more aggressively, and remove some LD32_nochks that weren't being protected
""",
u"""
b=484196; fix softfloat due to missing iu2fArg call; r=gal
""",
u"""
b=480796; detect whether ARM chip has VFP and/or v6t2 instructions; r=gal
""",
u"""
Fix asm_quad to use existing load instructions; fix branch macros to use existing conditional branch macro
""",
u"""
trace-tests: Add int overflow/underflow test
""",
u"""
[arm] b=481761; use movw/movt when possible for loading 32-bit constants; r=graydon
""",
u"""
[arm] b=481761; clean up load and store instructions; change move macro to follow covention; r=graydon
""",
u"""
[arm] b=481761; rename MOV instructions to match ARM, not x86; r=graydon
""",
u"""
[arm] b=481761; fix up asm_cmov; assert on non-qcmov; r=graydon
""",
u"""
[arm] b=481761; Finish up ALU op conversions; r=graydon
""",
u"""
[arm] b=481761; ARM ALU step 1; r=graydon
""",
u"""
[arm] b=481761; Rename ccName -> condName, rename Scratch to IP; r=graydon
""",
u"""
- Better fixes for getting the lengths of strings and String objects.  r=brendan
""",
u"""
Bump maxbranches to 32 (484341, r=dmandelin).
""",
u"""
- removing incorrect assert. r=mrbkap
""",
u"""
436700 - fixing backref assert. r=dmandelin
""",
u"""
- JavaScript Tests by Jesse Ruderman, Gary Kwong.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Gary Kwong, Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
JavaScript Tests - sync cvs->hg browser.js, no bug.
""",
u"""
- JavaScript Test by Jesse Ruderman, merge cvs->hg.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Igor Bukanov.
""",
u"""
- JavaScript Test by Jason Orendorff.
""",
u"""
- JavaScript Tests by Igor Bukanov.
""",
u"""
- JavaScript Test by Igor Bukanov.
""",
u"""
- JavaScript Test by Jeff Walden.
""",
u"""
- JavaScript Test by Peter Seliger.
""",
u"""
- JavaScript Test by Graydon Hoare.
""",
u"""
- JavaScript Test by Jason Orendorff.
""",
u"""
- JavaScript Test by Jason Orendorff.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript regression tests for upvar2.
""",
u"""
- Sisysphus - JavaScript Tests - support timeout and crash exclusion patterns.
""",
u"""
Fix for (Set/clear cached wrappers from within XPConnect). r/sr=jst.
""",
u"""
Fix for (Traceable quickstubs don't use the nsINode fastpaths). r=bent, sr=jst.
""",
u"""
- need lib path to link jemalloc on windows ce r=bsmedberg
""",
u"""
- changes to configure.in needed to build jemalloc on windows ce r=bsmedberg
""",
u"""
: lastIndexOf pathologically slow in some cases. Patch by Neil Rashbrook <neil@parkwaycc.co.ul> and me. r=gal.
""",
u"""
-  Need to be able to run tests on arbitrary build - add packaging bits for xpcshell. r=bsmedberg
""",
u"""
-  fix all xpcshell tests to not reference files from the srcdir. r=bsmedberg,waldo
""",
u"""
- Switch to use the new JSPropertyDescriptor API. Also fix it to return values on the prototype chain (which was sort of the point of its existance...). r+sr=jst
""",
u"""
Fix for (Avoid hash lookups in XPCWrappedNative::GetNewOrUsed). r=bz, sr=jst.
""",
u"""
- 'TM: Add logging mode for aborts only'. r=gal.
""",
u"""
- INS_CONSTPTR should not cast to void*; callers should do their own casting if they want to interpret numbers as pointers.  r=gal
""",
u"""
Fix further windows build bustage
""",
u"""
Fix for windows build bustage
""",
u"""
- 'Make qsgen.py generate traceable natives'. r+sr=jst.
""",
u"""
- gcc 4.4 warnings about "may be undefined" operations.  r=gal
""",
u"""
revert to changeset b59984b88601
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
- 'TM: Add logging mode for aborts only'. r=gal.
""",
u"""
- INS_CONSTPTR should not cast to void*; callers should do their own casting if they want to interpret numbers as pointers.  r=gal
""",
u"""
Fix further windows build bustage
""",
u"""
Fix for windows build bustage
""",
u"""
- 'Make qsgen.py generate traceable natives'. r+sr=jst.
""",
u"""
- gcc 4.4 warnings about "may be undefined" operations.  r=gal
""",
u"""
Backed out changeset fbb48d6a27e3
""",
u"""
- 'Make qsgen.py generate traceable natives'. r+sr=jst
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
- Initializing non-int elements calls the wrong imacro. Also call the right builtin when setting and initializing non-int properties (r=brendan).
""",
u"""
Always check operation callback on backwards branches (484035, r=brendan).
""",
u"""
Don't crash on non-primitive array indexes (484120, r=jwalden).
""",
u"""
jslock.h conflicts with AIX system header priv.h (484010, r=mrbkap).
""",
u"""
NEWINIT creates objects with wrong prototype (484104, r=mrbkap).
""",
u"""
- Use core_abspath and $(CURDIR) instead of shells. Use Preprocessor.py instead of preprocessor.pl to avoid perl insanity with pymake, and generally just make me happy. r=ted
""",
u"""
Backing out f385e435c082, fix for (Avoid hash lookups in XPCWrappedNative::GetNewOrUsed), to try to fix orange.
""",
u"""
Fix for (Avoid hash lookups in XPCWrappedNative::GetNewOrUsed). r=bz, sr=jst.
""",
u"""
- implement localStorage, p=Honza Bambas+Dave Camp, r=jst+dcamp+bz
""",
u"""
: Include "jsstdint.h" for <stdint.h> type use within SpiderMonkey. r=brendan
""",
u"""
: Don't define <stdint.h> types in public headers. r=brendan
""",
u"""
Merge.
""",
u"""
Backed out changeset e71cb3993380 ().
""",
u"""
- TM: obj.length and slowArray.length don't trace.  r=gal
""",
u"""
Extend tree when unboxing returns a different type (479110, r=jwalden).
""",
u"""
Copy entire regular expression into the code buffer (483920, r=gal).
""",
u"""
Eliminate separate global frame and merge it with InterpState (482377, r=brendan).
""",
u"""
: native regexps confused because of bug in hash key comparison, r=gal
""",
u"""
Compilation fix for MSVC (no bug).
""",
u"""
Backed out changeset 186ae511d5f2 (static analysis annotation only, no bug).
""",
u"""
- OOM in imacro trips assert, r=brendan.
""",
u"""
Remove unnecessary JS_REQUIRES_STACK from guardNotGlobalObject (rs=brendan).
""",
u"""
Merge.
""",
u"""
Try harder to trace array access with non-int / non-string index (478525, r=brendan).
""",
u"""
- TM: "Assertion failed: p->isQuad()" with str["-1"]; make str[-1] a non-special property rather than one that returns the length of str.  r=brendan
""",
u"""
Followup nit-picks for 457065.
""",
u"""
Read barrier for global object properties (463153, r=brendan).
""",
u"""
Merge.
""",
u"""
Use lir->insImmf and emit ins_eq0 centrally in guard() (483365, r=brendan).
""",
u"""
. TM: Assertion failure: !fp->callee || fp->thisp == JSVAL_TO_OBJECT(fp->argv[-1]). r=mrbkap
""",
u"""
- improving object graph serialization. r=brendan
""",
u"""
- fix nsinstall.py to not error if a target dir already exists. r=pike
""",
u"""
: Clone lexical blocks only when needed. r=igor
""",
u"""
Backed out changeset 10b781704400 ().
""",
u"""
Fix bogus assertion (457065, r=gal).
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
- TM: objectHook is called on trace, via js_NewObject [@ LeaveTree] or [@ js_SynthesizeFrame]. r=gal.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Carsten Book, Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Carsten Book, Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
, , , , - merge js/src/trace-test.js, js/tests/js1_8_1/trace/trace-test.js.
""",
u"""
- remove public failures from source control.
""",
u"""
- Sisyphus - JavaScript Tests - add support for narcissus.
""",
u"""
- comment bug number in spidermonkey-n-1.9.2.tests.
""",
u"""
- js_GetMethod cleanup. r=brendan
""",
u"""
Back out 480132: orange on Linux
""",
u"""
: Clone lexical blocks only when needed. r=igor
""",
u"""
Back out 480132 fix; static analysis red
""",
u"""
: Clone lexical blocks only when needed. r=igor
""",
u"""
Backout patch for . Debug only nit fix busts static analysis compile.
""",
u"""
. SpiderMonkey clones too many blocks into the heap. r=igor
""",
u"""
Back out fix for 481444; orange on Linux TraceMonkey unit test: http://tinderbox.mozilla.org/showlog.cgi
""",
u"""
. better geolocation mochitests. r=ctalbert/jmaher
""",
u"""
- 'XPConnect shouldn't poke JS objects manually, should use JSAPI.' patch by Blake Kaplan <mrbkap@gmail.com> and myself. r+sr=jst.
""",
u"""
- "Several deadlocks related to nested requests and nsJSContext::CompileEventHandler". r+sr=mrbkap, a=blocking1.9.1+.
""",
u"""
- Scripts compiled before the debugger got activated cannot be debugged; r=timeless
""",
u"""
- TM: objectHook is called on trace, via js_NewObject [@ LeaveTree] or [@ js_SynthesizeFrame]. r=gal.
""",
u"""
I hate config/*.
""",
u"""
backout merge
""",
u"""
Backed out changeset 57de81309176 - - due to mochitest leaks on tinderbox
""",
u"""
triggering tinderbox rebuild for to check if orange there persists
""",
u"""
- JSThread is no longer shared between runtimes. r=brendan
""",
u"""
Backed out changeset 4159ebdfe31e to fix some typos in the patch
""",
u"""
- JSThread is not shared between runtimes. r=brendan
""",
u"""
- Avoid re-entering recorder while deep aborting, r=mrbkap.
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
Backout changeset 5e0cc374593c for .
""",
u"""
Don't emit overflow guards if the operation is constant (483030, r=danderson).
""",
u"""
Make sure we don't walk out of a thin loop even if the loop condition is constant (482800, r=danderson).
""",
u"""
triggering rebuild to check if really caused tinderbox failures
""",
u"""
- removal of JSRuntime.gcPoke checks from js_NewGCThing. r=brendan
""",
u"""
- Don't call the reviver function when the JSON parse fails. r=jwalden
""",
u"""
-  nsinstall.py should support copying directories recursively. r=pike (fix the js/src copy as well)
""",
u"""
Crash [@ jsds_SyncFilter(FilterRecord*, jsdIFilter*) ] when appendFilter() called with Console2 installed
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
Do things in a different order. . r=jwalden
""",
u"""
- TM: Crash [@ js_ConcatStrings] due to forgetting about tagbits.  r=brendan
""",
u"""
Fix Solaris bustage
""",
u"""
- Use a principal when compiling -e scripts. r+sr=jst
""",
u"""
- TM: "Assertion failure: cx->bailExit" with string.replace and type instability. r=gal.
""",
u"""
- js_IsCallable returns false for functions. r=brendan.
""",
u"""
- fixing rt->state/rt->contextList mutation race. r=brendan
""",
u"""
-  rewrite xpcshell test harness. r=bsmedberg
""",
u"""
- fix spidermonkey to compile on mingw. r=bsmedberg,jorendorff
""",
u"""
Don't leak MSYS paths into makefiles, fix Solaris bustage r=bsmedberg
""",
u"""
- TM: followup work for support String(v) -- String constructor called as a converter (r=jwalden).
""",
u"""
followup -- use a better name for the "value" field. r=brendan
""",
u"""
- Add JS_GetPropertyDescriptorById to quickly get all information about a given property, possibly off of the prototype chain. r=brendan/jorendorff
""",
u"""
- Fix GCC warnings about casting between data and function pointers. r+sr=jst
""",
u"""
Merge m-c to tm.
""",
u"""
Fix test bustage from . r=jorendorff
""",
u"""
- treating null as a primitive value in js_ValueToObject. r=brendan
""",
u"""
Waldo's followup fix to valueOf/toString misorder in patch for (r=me).
""",
u"""
Fix (r=gal).
""",
u"""
Kick tinderboxen to see if the current orange is random or not
""",
u"""
Merge.
""",
u"""
Backed out changeset 65be699dabf0.
""",
u"""
- Generate via imacro_asm.js the big condition in TraceRecorder::monitorRecording's OPDEF macro (r=gal).
""",
u"""
Try harder to trace array access with non-int / non-string index (478525, r=brendan).
""",
u"""
Support String(v) -- String constructor called as a converter (482349, r=jwalden).
""",
u"""
- Quickstub additional properties on nsIDOMHTMLAnchorElement and nsIDOMNSHTMLAnchorElement, r=bz
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
- Array.prototype getter/setter does not work as usual (r=jorendorff).
""",
u"""
: myngle.com crash due to incorrect compiled regexp end-of-string check, r=brendan
""",
u"""
Drop a few unnecessary extern declarations in jstracer.cpp (no bug).
""",
u"""
Add missing GC_POKE to js_SetRequiredSlot (481922, r=igor).
""",
u"""
Check for non-stub getters/setters in SETNAME and SETPROP and invoke SetPropHit after setting the property in INITPROP (481989, r=brendan).
""",
u"""
Better coordination of nested tree recording (481793, r=dmandelin).
""",
u"""
- Assertion failure: pobj_ == obj2, at ../jsinterp.cpp:4276 when getting a property that is cached but shadowed (r=jorendorff).
""",
u"""
Don't import slots that have a non-stub setter (476871, r=jorendorff).
""",
u"""
- JS_Assert is C++-name-mangled in non-DEBUG builds. r=brendan.
""",
u"""
Abort recording when we come across a function being written into the global object (r=brendan, 481800).
""",
u"""
- js1_8_1/trace/regress-462459-05.js - trace new Array regressed (r=gal).
""",
u"""
- update JavaScript Test failures.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
, , , , - JavaScript Tests - merge js/src/trace-test.js and js/tests/js1_8_1/trace/trace-test.js.
""",
u"""
- JavaScript Test by Blake Kaplan.
""",
u"""
- JavaScript Tests by Jesse Ruderman, Aiko.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Christopher Lenz, ash_mozilla.
""",
u"""
- JavaScript Test by Robert Sayre.
""",
u"""
- JavaScript Test by Boris Zbarsky.
""",
u"""
- JavaScript Tests by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Gary Kwong, Brendan Eich, Igor Bukanov.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Gary Kwong, Jesse Ruderman and Jason Orendorff.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong, Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- Test is for clone and not for js1.8 features. Modify to use functions and move to js1_5/extensions/.
""",
u"""
- remove test created Object.prototype.copy.
""",
u"""
: change --with-valgrind to --enable-valgrind and add hooks to tell valgrind about the JIT's self-modifying code. r=gal (JIT parts), r=luser (build config parts).
""",
u"""
- no more static asserts in headers. r=brendan
""",
u"""
b=481351; TM ARM crash in js_FastNewObject while logging in to gmail (bad constant-offset load codegen); r=graydon
""",
u"""
- Temporarily back-out / disable trace-test on make check, due to failing tinderbox.
""",
u"""
Fix for --disable-jit (again).
""",
u"""
- TM: trace RegExp constructors (r=gal).
""",
u"""
- Make check should run trace-test.js when ENABLE_JIT is defined, r=ted.
""",
u"""
Assertion: "tree->root == tree" and crash while loading a website, r=gal.
""",
u"""
b=481291, missing return statements in NativeARM.cpp, r=vlad
""",
u"""
Merge m-c to tm
""",
u"""
- Kill win32.order. r=bsmedberg.
""",
u"""
Backed out changeset 5befb6301e9b for - the patch broke 32-bit linux build.
""",
u"""
- macros to cast between function and data pointers are public now. r=brendan,mrbkap
""",
u"""
Keep --disable-jit working (480657, r=gal).
""",
u"""
Followup patch for .
""",
u"""
- TM: Add an API to define traceable constructors (r=gal, jorendorff).
""",
u"""
Assert prototype shapes when reading a hole from a dense array instead of calling a builtin (481328, r=brendan).
""",
u"""
Fixed MacOSX breakage.
""",
u"""
Merge.
""",
u"""
Browser spuriously sets runtime->anyArrayPrototypeHasElement and makes perf bad (481251, r=mrbkap).
""",
u"""
- JIT stats in tracemonkey can interfere with stdout-using embeddings. Take 2. r=jorendorff.
""",
u"""
- JIT stats in tracemonkey can interfere with stdout-using embeddings. r=jorendorff.
""",
u"""
- Prevent recording of treecalls when function calls with extra args are in pending frames, r=gal.
""",
u"""
Guard that we don't have to re-brand when writing a function into a slot if we didn't do so at recording time (481246, r=brendan).
""",
u"""
- Avoid leaking MSYS paths in Makefiles: use c:/dir/path paths whenever possible, r=ted
""",
u"""
- xpcshell's load() just silently fails for non-existent files; r=mrbkap
""",
u"""
Port xpcom to 64-bit Mac OS X, part 1. b=478687 r=mstange sr=bsmedberg
""",
u"""
Fixing test_bug478438; only print exceptions when something fails so that the Tinderbox error parser doesn't get confused
""",
u"""
b=481351; TM ARM crash in js_FastNewObject while logging in to gmail (bad constant-offset load codegen) [ARM ONLY]; r=graydon
""",
u"""
- Remove a now-unnecessary eval hack. r+sr=jst
""",
u"""
- Unwrap |obj| because you can't use a wrapper as a variables object. r=brendan
""",
u"""
- Can't access allAccess properties of cross-origin XPCNativeWrappers. r+sr=mrbkap
""",
u"""
b=481291, missing return statements in NativeARM.cpp, r=vlad
""",
u"""
- Fix up the logic a bit. r+sr=bzbarsky
""",
u"""
followup -- wrap for different-scope bug same-origin chrome wrappers since we have code that depends on it.
""",
u"""
followup -- don't wrap when the scopes are actually the same (even if they don't have principals.
""",
u"""
- Don't wrap objects that are same-origin but differently scoped. r=jst sr=bzbarsky
""",
u"""
Merge tm to m-c.
""",
u"""
- JSON.parse does not support reviver argument as defined in spec. r=jorendorff
""",
u"""
Take out printfs. no relation to orange
""",
u"""
Check where we're calling JSON functions for a few runs. Temporary debug stuff.
""",
u"""
Back out due to subsequent inadequacies and potential performance regression
""",
u"""
Backed out changeset d69277360499
""",
u"""
- Don't leave the last argument lying around in case someone accidentally uses it. r=brendan
""",
u"""
-  Process first argument to JSON stringify and parse methods as specified by ES3.1, part 2. r=jorendorff
""",
u"""
- PurgeScopeChain should deep-bail. r=brendan.
""",
u"""
- adding mixing operation callback calls. r=gal
""",
u"""
Whitespace and spelling fix (no bug, no code change).
""",
u"""
Trace index out-of-bounds case of charCodeAt and optimize for integer case (480794, r=danderson).
""",
u"""
Backed out . Massive failures across all platforms.
""",
u"""
Style nit (no bug, no code change).
""",
u"""
Add an API to define traceable constructors (480657, r=brendan).
""",
u"""
A little helper function to make life in gdb more bearable (DEBUG only, no bug, r=danderson).
""",
u"""
Kicking Windows...
""",
u"""
- __proto__ setting does not flag delegate, breaking deep property caching assumptions.  Tag-team effort of Brendan and me, r=us
""",
u"""
Delete unused member variable and fix style issue discovered by Waldo just below. No bug. r=Waldo.
""",
u"""
- Add assertEq function to JS shell. r=mrbkap.
""",
u"""
Add a mochitest for .
""",
u"""
- check-sync-dirs.py : (further) improve output format
""",
u"""
- Quickstubs leaks IIDs. r=jorendorff
""",
u"""
- Fix the test harness to work on OS/2; m-c *.mk files; r=mozilla@Weilbacher.org
""",
u"""
Merge tm to m-c.
""",
u"""
Permit and guard on dense arrays when tracing a not-found property acccess (480479, r=jwalden).
""",
u"""
Kick tinderboxen as I still think this orange is bogus, because all the oranges seem to be happening in different locations across runs
""",
u"""
Merge.
""",
u"""
Trace reading undefined properties (478512, r=jwalden).
""",
u"""
guardElemOp relies on op_offset representing JSObjectOps.getProperty or JSObjectOps.setProperty, so it should assert it.  r=lumpy, sr=jack
""",
u"""
- TM: Wrong function called via `f()` when global f is reassigned on trace.  r=brendan
""",
u"""
Follow-up fix for 479109. Regenerate imacros.c.out and bump xdr bytecode version.
""",
u"""
js_Array_dense_setelem can call arbitrary JS code (479487, r=jorendorff).
""",
u"""
- fixing most VC 2005 warnings. r=gal,mrbkap
""",
u"""
Improve blacklisting (479109, r=graydon).
""",
u"""
Make arrays with less than 256 entries always dense (479386, r=brendan).
""",
u"""
b=480659; special-case 1-char match nodes for ARM jit; r=dmandelin
""",
u"""
- Recursive submakes without shell loops, r=ted
""",
u"""
Integrate sparc nanojit, fix for LDUB/LDUH, r=gal
""",
u"""
.  remove TARGET_DEVICE=emulator. It was an old hack to get builds working on wince simulators.  no longer needed r=ted+jimb
""",
u"""
b=479525; fix nanojit on Windows CE (calling conventions, disable regexp double-char optimization); r=dmandelin
""",
u"""
- 5th arg of mktime should begin at zero; r=ted.mielczarek
""",
u"""
- Use a better method to create this function. r+sr=jst
""",
u"""
- The JS spec says that we have to iterate over string properties only. r+sr=jst
""",
u"""
- XPCSafeJSObjectWrapper's construct hook was not correct. r+sr=jst
""",
u"""
- Move wrapping back into the outerObject hook. r+sr=bent/jst
""",
u"""
- Assertion failure: cx->bailExit (from js_ReportAllocationOverflow from js_ConcatStrings). r=gal.
""",
u"""
- js/tests/js1_8_1/extensions/regress-477187.js uses timeout() but doesn't expectExitCode(6). r=bc.
""",
u"""
-  Missing parens around genexp in |while|. r=Waldo.
""",
u"""
- Remove vestigial #ifdef MOZILLA_1_8_BRANCH. r=Waldo.
""",
u"""
: memory spike on Dromaeo string due to missing GC_POKE, r=igor
""",
u"""
- jsstack.js static analysis errors in js_GetCurrentBytecodePC and specializeTreesToMissingGlobals. r=bsmedberg.
""",
u"""
- jsstack.js static analysis errors in js_GetCurrentBytecodePC and specializeTreesToMissingGlobals. r=bsmedberg.
""",
u"""
Orange fix for "changeset: 4f3614d130da" of
""",
u"""
-  Native JSON stringification aborts on functions and xml but returns JS_TRUE. r=shaver
""",
u"""
Fixed breakage of type stability guarantees between linked trees, and fixed using the wrong global typemap in LeaveTree (, r=gal).
""",
u"""
- Don't iloop if we GC exactly once. r=gal
""",
u"""
Fixed emitTreeCall crashing on deep aborts (, r=gal).
""",
u"""
- Tune dense array growth. r=brendan.
""",
u"""
- Remove cx->pcHint. r=gal.
""",
u"""
- Assertion failure: (cx)->requestDepth || (cx)->thread == (cx)->runtime->gcThread, at js/src/jsapi.cpp:957 after typing EOF at js shell prompt. r=igor and mrbkap.
""",
u"""
- Integrate sparc nanojit intro tracemonkey. Put the flush instruction cache code to the correct place. r=gal
""",
u"""
Backout 479109. Breaks trace-tests.
""",
u"""
Fix build bustage from .
""",
u"""
Merge.
""",
u"""
Improve blacklisting algorithm (479109, r=graydon).
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
- single-threaded js shell now compiles on Windows again (regression from )
""",
u"""
- TM: equalityHelper can call toString or valueOf erroneously when tracing obj == undefined.  r=brendan
""",
u"""
Fix compiler warning in jstracer.cpp. No bug, r=brendan/jorendorff
""",
u"""
Fix bustage from checkin for bug 
""",
u"""
- Rename array "dense length" to capacity. r=shaver.
""",
u"""
- Crash [@ Detecting] or "Assertion failure: (uint32)(index_) < atoms_->length, at ../jsobj.cpp". r=igor.
""",
u"""
- js_FinalizeStringRT dies with multi-threaded app. r=igor.
""",
u"""
- avoiding watchdog ticks when idle in jsshell. r=gal
""",
u"""
Back out a2b6a4c57a05 (). Cross-platform orange.
""",
u"""
Trace reading undefined properties (478512, r=brendan).
""",
u"""
- TM: kill many of the warnings when building 'js'. r=mrbkap
""",
u"""
Fix for ( "Illegal Value" exception when accessing XHR request within an extension). r=mrbkap, sr=jst.
""",
u"""
- move tools/test-harness/xpcshell-simple to testing/xpcshell
""",
u"""
- MAXPATHLEN too small for glibc's realpath(); m-c part; r=*
""",
u"""
- use JS_MAX instead of the max() macro in prmjtime due to mingw-w64 bustage; r=mrbkap
""",
u"""
- Sishyphus - JavaScript tests - patterns maintenance.
""",
u"""
- JavaScript Test by Brendan Eich.
""",
u"""
- correct bug numbers in tests.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by T. Rosenau.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Andreas Gal.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Jason Orendorff.
""",
u"""
- JavaScript Test by David Greenspan.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- modify test to handle uncaught exception.
""",
u"""
- modify test to handle uncaught exception.
""",
u"""
- modify test to handle uncaught exception.
""",
u"""
- modify test to handle uncaught exception.
""",
u"""
- in order to exclude randam passes on platforms that do not support jit, require jit time to be less than 1/2 non jit time in order to pass.
""",
u"""
- in order to exclude randam passes on platforms that do not support jit, require jit time to be less than 1/2 non jit time in order to pass.
""",
u"""
- in order to exclude randam passes on platforms that do not support jit, require jit time to be less than 1/2 non jit time in order to pass.
""",
u"""
- JavaScript Test by Norris Boyd and modify tests to handle new TypeError setting a property with only a getter.
""",
u"""
- JavaScript Tests by Gary Kwong, Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
JavaScript Tests - merge js/src/trace-test.js into js/tests/js1_8_1/trace/trace-test.js - , , , , , , , , , , , , 
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Adam L. Peller.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- remove extraneous statements in test.
""",
u"""
- JavaScript Test by simonzack.
""",
u"""
- fix bisect.sh to handle local changes in the source tree during hg bisect.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test.
""",
u"""
- JavaScript Test by Carsten Book.
""",
u"""
- JavaScript Tests by Jesse Ruderman and Jeff Walden.
""",
u"""

""",
u"""
Followup to - The creation of these directories also depends on the existence of nsinstall. This was found in tryserver clobber builds.
""",
u"""
Fixing a typo
""",
u"""
- improving JS_STATIC_ASSERT macrology for WinCE, r=jorendorff
""",
u"""
Backed out changeset 1145cd361cac.
""",
u"""
Change definition of JS_STATIC_ASSERT macro to avoid declaring a function, which causes mysterious trouble on Windows CE.  Sort of reviewed by blassey, approved-ish by sayrer.
""",
u"""
Merge tm to mc
""",
u"""
- fixing warnings about casts between function and data pointers. r=brendan
""",
u"""
: Remove parent argument to js_GetCallObject. r=brendan
""",
u"""
- "Assertion failure: script->code[offset] == JSOP_NOP" with trap, dis. r=crowder.
""",
u"""
- JS_SetTrap alters code execution. r=brendan.
""",
u"""
- JS_REQUIRES_STACK errors in nsXPCWrappedJSClass::CallMethod. Mozilla code uses some JS-internal APIs and needs to bail off trace before doing so. This shouldn't affect performance now becuase XPConnect methods are not traceable yet. r=mrbkap, sr=mrbkap.
""",
u"""
- jsstack.js static analysis error in js_GetPropertyHelper. r=mrbkap.
""",
u"""
- fix for pymake: provide an explicit value for RM so that we don't rely on the gmake implicit value. Fix some rules in js/src that don't make much sense r=ted
""",
u"""
: Eliminate PTRDIFF macro; delete jssttddef.h. r=jimb
""",
u"""
fix for Sun Studio Express r=jim
""",
u"""
- 'Context switch in mozJSComponentLoader::ImportInto without suspending outer context's request'. r+sr=jst, a=blocking1.9.1+
""",
u"""
Merge tm to m-c.
""",
u"""
Followup nitfixes to not noted in final reviews.  Egads, how'd I miss some of these?
""",
u"""
- Split ip_adj into two pointer fields, pc and imacpc. r=brendan.
""",
u"""
- A statement can follow an expclo without an intervening semicolon. r=igor.
""",
u"""
-  Integrate sparc nanojit intro tracemonkey. r=gal, r=jim.
""",
u"""
- Improve this error message and the corresponding comment to help future debuggers. r=gal
""",
u"""
- Eagerly call f2i to root out constant values. r=gal
""",
u"""
-  Process first argument to JSON stringify and parse methods as specified by ES3.1. r=shaver
""",
u"""
- Don't jump based on uninitialized memory. r=dmandelin
""",
u"""
refix: count JS_realloc memory more accurately, r=mrbkap
""",
u"""
: assert in new tableswitch generator with non-numeric input, r=gal
""",
u"""
- Back out lirbuf-based allocation of fragments and treeinfos, r=gal.
""",
u"""
Merge mc to tm
""",
u"""
- Assignments to a property that has a getter but not a setter should throw a TypeError. r=igor
""",
u"""
: LIR_jtbl: jump tables to implement jsop_tableswitch, r=gal,r=edwsmith
""",
u"""
- Eliminate operationCount. Add signal.h to include files. gal: review+
""",
u"""
- Make some nanojit classes initialize their members. r=edwsmith,gal.
""",
u"""
- Don't record after js_GetScopeChain, since we can't successfully recover from a side exit. r=gal
""",
u"""
- Don't trigger debugger hooks until frame initialization is complete. r=mrbkap
""",
u"""
- _FAIL builtins need to be GC-safe. r=brendan.
""",
u"""
- If we fall into the regexp getter case, we need to pass the original object in, not the prototype. r=brendan
""",
u"""
Don't try to align fragment entry with nopl since some processors do not support it (473552, r=graydon).
""",
u"""
- Flush script-associated fragments more correctly by unlinking from hash chain, r=jorendorff.
""",
u"""
Substitute operation counting with a watchdog thread (477187, 3nd attempt, r=brendan/mrbkap/jst, sr=brendan/jst).
""",
u"""
Backout .
""",
u"""
- Allow LIR_ret at end of trace. r=edwsmith.
""",
u"""
No longer need these gcparam calls to improve performance.  In fact, even on hardware with a lot of RAM we're faster running the mandelbrot tests without these calls.
""",
u"""
. r+sr=mrbkap.
""",
u"""
: xpcshell: default to non-interactive when isatty is missing. r=roc
""",
u"""
- xpcshell's load() function doesn't close file handle; r+sr=mrbkap
""",
u"""
Add crashtests
""",
u"""
b=477727; add WINCE_WINDOWS_MOBILE define and associated configure flag; r=ted
""",
u"""
Add a bunch of crashtests
""",
u"""
Add some crashtests
""",
u"""
b=477735; fix XPCOMUtils.generateQI to handle null/undef members in array; r=sayrer
""",
u"""
Merge tm to m-c
""",
u"""
- Fix pathological doubling in Fragmento uncovered by new pressure on lirbuf, r=jorendorff.
""",
u"""
Substitute operation counting with a watchdog thread (477187, 2nd attempt, r=brendan/mrbkap/jst, sr=brendan/jst).
""",
u"""
Merge.
""",
u"""
Backing out . Breaks xpcshell.
""",
u"""
Merge.
""",
u"""
Substitute operation counting with a watchdog thread (477187, r=brendan/mrbkap/jst, sr=brendan/jst).
""",
u"""
- Flush fragments for a JSScript when it is destroyed, r=gal.
""",
u"""
- Allocate TreeInfo and UnstableExit in LirBuffer, r=gal.
""",
u"""
- "Assertion failure: !JSVAL_IS_PRIMITIVE(regs.sp[-2]), at ../jsinterp.cpp:3237" with generator on trace. r=brendan.
""",
u"""
- "Some objects left locked in tracer code". r=brendan, a=blocking1.9.1+.
""",
u"""
Remove some trailing whitespace to maybe kick build machines out of an orange
""",
u"""
- JS version/option unsyncing results in JS modules not being loaded with the very latest JS version, resulting in syntax errors when loading modules that use new JS syntax.  r=brendan
""",
u"""
- Handle an __iterator__ implementation returning a primitive value on trace. r=brendan
""",
u"""
- make sure that js_(New|Destroy)Context() do not race against the GC. r=brendan
""",
u"""
- JS_(Set|Clear)ContextThread() must wait bfor the GC. r=brendan
""",
u"""
- TM: "Assertion failure: v != JSVAL_ERROR_COOKIE, at ../jstracer.cpp" with proto, getter. r=gal.
""",
u"""
- Always release this file descriptor. r=brendan
""",
u"""
- Report an error when a script tries to use duplicate flags on a regexp. r=brendan
""",
u"""
- TM: "Assertion failure: v == JSVAL_TRUE || v == JSVAL_FALSE, at ../jsapi.h".  r=gal
""",
u"""
: word-at-a-time compiled regexp matching, r=gal
""",
u"""
Fix bustage from 
""",
u"""
: nanojit assembler needs to clear its state before each compilation, r=gal
""",
u"""
Fix compilation errors on Windows due to a misplaced __fastcall introduced in changeset 527b21f9ab77.
""",
u"""
- TM: Trace JSOP_ARRAYPUSH. r=brendan.
""",
u"""
If js_AddAsGCBytes is called from trace and wants to GC and we can bail off trace then do so instead of returning an error (476869, r=jorendorff).
""",
u"""
- Assertion failure: cg->stackDepth == loopDepth, at ../jsemit.cpp. r=brendan.
""",
u"""
- TM: HasProperty can call into exotic lookupProperty hooks. r=brendan.
""",
u"""
Back out 21494181fdb8 and subsequent merges because they turned OS X red.
""",
u"""
If js_AddAsGCBytes is called from trace and wants to GC and we can bail off trace then do so instead of returning an error (476869, r=jorendorff).
""",
u"""
- Protect against evil E4X jsvals in args_resolve. r=brendan
""",
u"""
-  JS array and object literals should define properties, not set them, to avoid calling getters or setters along the prototype chain.  r=brendan
""",
u"""
Merge.
""",
u"""
Add skip() to LirFilter so we can pass skip-requests through instead of going to the LirBufWriter directly (477089, r=shaver).
""",
u"""
- JSOP_DEFUN fixes to deal with non-top-level function statements redeclaring local argument and variables. r=brendan
""",
u"""
How in the world did jstracer.cpp accumulate so much trailing whitespace?  Kicking Linux this time around...
""",
u"""
Kill trailing whitespace in jstracer.h to kick a box out of a bogus orange
""",
u"""
- Assert correct type in JSVAL_TO_* (and vice versa) macros to fail fast when type errors happen.  r=brendan
""",
u"""
Fix warning for unhandled switch cases
""",
u"""
Fix initialization order warning
""",
u"""
Assert that we don't leak JSVAL_ERROR_COOKIE along the JSVAL_BOXED path (r=me, debug only.)
""",
u"""
Didn't mean to disable mandelbrot
""",
u"""
Merge mc to tm
""",
u"""
Don't expect to pass test for in trace-tests.js until we have upvar (r=me, no code changes.)
""",
u"""
- Don't throw if XPCNativeWrapper is called as a function but passed a primitive value to allow for safe primitive testing. r+sr=jst
""",
u"""
- kill variadic macro warnings r=ted
""",
u"""
[OS/2] : add AVMPLUS_OS2 to get through the js's configure, r=ted.mielczarek
""",
u"""
-KPIC is obsolete in Sun Studio 12 SPARC r=jim
""",
u"""
- (0.5).toFixed(0) is 0, should be 1. r=bz,mrbkap
""",
u"""
Backed out changeset 423eea03fb54 () for being one of the two changesets that's causing chrome and a11y tests not to start.
""",
u"""
- 'nsScriptSecurityManager not thread-safe called by IsCallerChrome'. p=timeless+bent, r+sr=jst, a=blocking1.9.1+
""",
u"""
. r+sr=mrbkap, a=blocking1.9.1
""",
u"""
- jsdIDebuggerService.idl changed without changing uuid, r+sr=bz
""",
u"""
Backed out changeset 64d5b7cdeb69 - because of Windows bustage (js_LeaveTrace is not a friend API)
""",
u"""
- mozilla code uses some JS-internal APIs and needs to bail off trace before doing so. This shouldn't actually affect runtime now, because XPConnect doesn't use traceable natives. But in the 1.9.2 future we want to use traceable natives r=mrbkap r=jorendorff
""",
u"""
Merge tm to m-c
""",
u"""
- Deoptimize special own-properties, r=brendan.
""",
u"""
Backout . Causes a massive slowdown in trace-tests.js that needs to be investigated.
""",
u"""
Merge.
""",
u"""
Re-land . It seems it didn't cause the orange-ness after all.
""",
u"""
-  JS array and object literals should define properties, not set them, to avoid calling getters or setters along the prototype chain.  r=brendan
""",
u"""
b=476786; tracemonkey crash with verbose in debug mode; r=gal
""",
u"""
b=474517; add option for trace-test to skip slow tests; r=shaver
""",
u"""
Merge.
""",
u"""
Backed out . Suspected of causing Linux orange-ness.
""",
u"""
Object_p_hasOwnProperty and Object_p_propertyIsEnumerable should be BOOL_FAIL, not BOOL_RETRY (476760, r=brendan).
""",
u"""
- TM: Allow GC with traced machine code on stack. r=brendan.
""",
u"""
- Bail off trace when reentering interpreter. r=gal.
""",
u"""
Backed out changeset ca733f2cc237; looks like some include system weirdness is biting where an old version of jsapi.h is being included which then causes a *newer* included version to miscompile.  Weird, still investigating...
""",
u"""
- Assert correct type in JSVAL_TO_* (and vice versa) macros to fail fast when type errors happen.  r=brendan
""",
u"""
- Disable upvar optimizations under JS_EvaluateUCInStackFrame because we can't vouch for the display being right. r=brendan
""",
u"""
Fixed signed/unsigned compare warning
""",
u"""
- TM: Crash reading near 0 @Detecting, regression due to . r=gal.
""",
u"""
Revert to 07be1f190a3d.  Revision 5f5c1cd63641 should not have been pushed.
""",
u"""
- TM: Crash reading near 0 @Detecting, regression due to . r=gal.
""",
u"""
- TM: Allow GC with traced machine code on stack. r=brendan.
""",
u"""
[mq]: bug-462027-v9
""",
u"""
Give up on automation due to intermittent redness (r=jst).
""",
u"""
Bake the value of fp->imacpc into the trace and report it at recording time when detecting inside JSOP_GETELEM (follow-up for 476238, r=brendan,jorendorff).
""",
u"""
Merge.
""",
u"""
Leave a hint for GetProperty in the context so it can figure out the current bytecode location without de-optimizing (476238, r=jorendorff).
""",
u"""
Try hardest of all (last time) to fix redness (r=nthomas).
""",
u"""
Try hardest to fix redness (r=me).
""",
u"""
Try harder to fix redness (r=bsmedberg).
""",
u"""
Try to fix redness (r=ted).
""",
u"""
- imacros.c.out out of date; also Makefile.in bustage/cleanup (r=ted/jorendorff).
""",
u"""
- optimizing js_CheckRedeclaration for the common case of non-existing properties. r=brendan
""",
u"""
Merge.
""",
u"""
Assert that JSVAL_ERROR_COOKIE doesn't leak from the JIT into the interpreter (r=me, debug only).
""",
u"""
--enable-static builds (for comm-central apps) broken on trunk due to xpcshell requiring libxul - disable building of xpcshell for static builds. r=ted.mielczarek
""",
u"""
- Rerunning configure causes the world to be rebuilt, r=ted
""",
u"""
- Reinitializing one-shot timers by resetting delay (->SetDelay) doesn't work anymore - fix callers; r+sr=bzbarsky
""",
u"""
- Add ability to pass the GRE dir to xpcshell, r=ted - fixed patch: XRE_GetBinaryPath gets the file of the executable: we want to pass the parent directory to XPCOM.
""",
u"""
Give up on automation due to intermittent redness (r=jst).
""",
u"""
Try hardest of all (last time) to fix redness (r=nthomas).
""",
u"""
Try hardest to fix redness (r=me).
""",
u"""
Try harder to fix redness (r=bsmedberg).
""",
u"""
Try to fix redness (r=ted).
""",
u"""
- imacros.c.out out of date; also Makefile.in bustage/cleanup (r=ted/jorendorff).
""",
u"""
- jsstack.js static analysis error in js_GC. r=bsmedberg.
""",
u"""
followup - don't normalize symlinks in xpcshell's __LOCATION__. r+sr=mrbkap
""",
u"""
Standalone Spidermonkey should build on Solaris with GCC r=jim
""",
u"""
: follow-up patch, r=ted.mielczarek
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
Back out ; it has a problem with one Mochitest.
""",
u"""
I hate LiveConnect.
""",
u"""
Bustage fix, not updated for changes in c0b2c82a524e
""",
u"""
- JSON literals shouldn't have prototype setters run during evaluation.  r=brendan
""",
u"""
Fix for red caused by rev 932126be5356.
""",
u"""
- TM: cx->stackPool must not be accessed on trace. r=brendan.
""",
u"""
Add debug hook to the threaded interpreter to trace instruction stream (476128, r=shaver).
""",
u"""
Remove unused variable declaration (followup, r=gal)
""",
u"""
Do not count control-flow merges twice in IFEQX, we already do it in IFEQ (fixed by brendan as part of 469625, r=me).
""",
u"""
Merge.
""",
u"""
Don't try to immediately record a new tree when encountering a failed inner tree activation while recording the outer tree if we are no longer at the actual loop header (475916, r=danderson).
""",
u"""
- Minor followups to fix build warnings and trace-test output, r=danderson.
""",
u"""
- Maintain globalSlots per global, not just one per JIT instance, r=danderson.
""",
u"""
- Multiline comments with newlines in them should not decompose to nothing. r=brendan
""",
u"""
- TM: js_Any_GetProp and friends can reenter. r=brendan.  Note that this patch alone does not fix the bug.  The rest of the fix comes in .
""",
u"""
Backed out changeset 7246c4dcf997 () due to trace-test.js failures.
""",
u"""
Conservatively track modifications along the prototype chain of arrays (469625, r=jorendorff).
""",
u"""
Detect OOM condition and flush code cache when destroying the recorder and don't enter endAssembly when OOM (475821, r=danderson).
""",
u"""
- let callers of Components.utils.Sandbox specify JS version; r+sr=mrbkap
""",
u"""
: OS/2 build break in xpcshell.cpp due to , p=wuno@lsvw, r=ted.mielczarek
""",
u"""
- the rule for DIST_FILES should create dist/bin, syncing config/rules.mk with js/src/rules.mk r=ted
""",
u"""
Merge tracemonkey to mozilla-central.
""",
u"""
- TM: js_FastValueToIterator and js_FastCallIteratorNext can reenter (relanding with a bug fix). r=brendan. Note that this changeset alone does not fix the bug; an upcoming patch in completes the fix.
""",
u"""
Trigger a new build.
""",
u"""
Abort if we hit SETGVAR with a NULL slot (465567, r=brendan).
""",
u"""
Update the tracker if the global object's dslots are reallocated at recording time (475645, r=brendan).
""",
u"""
- Don't assume cx->fp is a scripted frame. r=dmandelin
""",
u"""
Properly initialize demote flag (475479, r=danderson).
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Backed out changeset d50d3681b94e (attempted re-landing of 474771).
""",
u"""
- Implement eval caching (r=mrbkap).
""",
u"""
Back out due to Mac Tp orange (454184).
""",
u"""
- Implement eval caching (r=mrbkap).
""",
u"""
: Use 'test !', not '! test' in configure scripts. r=bsmedberg
""",
u"""
- record mozilla-1.9.1 fix.
""",
u"""
- JavaScript Test by Jeff Walden.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Boris Zbarsky.
""",
u"""
imported patch bug-366601.patch
""",
u"""
- record mozilla-central failure.
""",
u"""
- record failures.
""",
u"""
- record failures.
""",
u"""
- record failures.
""",
u"""
- record failures.
""",
u"""
- record failure.
""",
u"""
- record variety of darwin failures.
""",
u"""
- record 1.9.0 failures.
""",
u"""
- record 64bit jit vs. non-jit test failure due to lack of jit support.
""",
u"""
- JavaScript Tests by Andreas Gal.
""",
u"""
- JavaScript Test by Robert Sayre.
""",
u"""
- add math-trace-tests.js to the JavaScript Test library.
""",
u"""
- JavaScript Test by Gary Kwong and Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Igor Bukanov.
""",
u"""
- JavaScript Test by Jeff Walden.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Edward Lee.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Igor Bukanov.
""",
u"""
- Implement eval caching (r=mrbkap).
""",
u"""
Apply rules.mk section of 's patch to js's separate rules.mk in order to fix orange.
""",
u"""
- Add a crashtest.
""",
u"""
-  TM: Assertion failed: "Should not move data from GPR/XMM to x87 FPU": false (../nanojit/Nativei386.cpp:1851) (js_BooleanOrUndefinedToNumber emitted twice). r=brendan.
""",
u"""
Merge m-c to tm.
""",
u"""
- Checking for MaybeGC conditions when allocating GC things in JS shell. r=igor
""",
u"""
Backed out changeset 39b1c9f21064 - the patch again has triggered the crashtest timeout.
""",
u"""
Set on-trace flag only during trace execution, not recording (474771, r=brendan, patch has failed before, please back out at the earliest sign of trouble).
""",
u"""
Backed out changeset ece63b96379b
""",
u"""
- TM: js_FastValueToIterator and js_FastCallIteratorNext can reenter. r=brendan. Note that this changeset alone does not fix the bug; an upcoming patch in completes the fix.
""",
u"""
Correct incorrectly reversed order of argument types in builtin description (472533, r=brendan).
""",
u"""
- provide a 2-level hash map (global, pc) -> tree, r=gal.
""",
u"""
LirNameMap gets large over time and searching it with binary search is slow (475127, r=shaver).
""",
u"""
- JS shell gets stuck on EOF. r=brendan
""",
u"""
- GetPDA returns n copies of the first entry. Bug noticed by Mads Bondo Dydensborg <mbd@dbc.dk>. r=brendan
""",
u"""
- Pass the proper size argument to ResizeSlots. r=shaver/crowder
""",
u"""
Merge m-c to tm.
""",
u"""
- JS_REQUIRES_STACK violation in TraceRecorder::hasIteratorMethod, r=jorendorff
""",
u"""
- fixing gczeal checks in RefillDoubleFreeList. r=mrbkap
""",
u"""
Backout c0b2c82a524e.
""",
u"""
Only set onTrace flag while running native code, not when recording (474771, r=brendan).
""",
u"""
Fixed multitrees assert regression from (, r=gal).
""",
u"""
- jsobj.cpp DEBUG / js_DumpObject crash on JSFunction with null proto. r=jorendorff
""",
u"""
- TM: "Assertion failure: entry->kpc == (jsbytecode*) atoms[index]" with valueOf, regexp (r=jorendorff).
""",
u"""
- TM: Crash [@ JS_CallTracer] (r=jwalden).
""",
u"""
Backout . Confirmed to leak.
""",
u"""
- Move fragment hit and blacklist counts to hashtable in oracle, r=gal.
""",
u"""
- TM: Add a way to keep stack values alive without emitting guard code.  r=gal.
""",
u"""
- TM: js_FastValueToIterator and js_FastCallIteratorNext can reenter. r=brendan. Note that this changeset alone does not fix the bug; an upcoming patch in completes the fix.
""",
u"""
Backout , it causes mochitests to hang.
""",
u"""
Only emit alias check in for *PROP if the object's shape matches the global object's shape (475048, r=brendan, relanding).
""",
u"""
[arm] fix up ARM floating point comparisons; fixes ARM trace-test (relanding)
""",
u"""
- "Assertion failure: sprop->setter != js_watch_set || pobj != obj, at jsdbgapi.c" (r=mrbkap, relanding).
""",
u"""
Fixed correctness and leak regression from landing (, r=gal, relanding).
""",
u"""
Fix incorrect reliance on the identity of the global object on trace (474888, r=brendan, relanding).
""",
u"""
Backout all patches since last mozilla-central merge (Thu Jan 22 19:14:02 2009 -500 by sayrer).
""",
u"""
Backed out changeset 1c95c3031450 (thereby re-landing 475048, it seems it was not the offending patch).
""",
u"""
Backed out changeset 9fe03078c765 ().
""",
u"""
Backed out changeset 716fe0739e2b which fixes a spelling bug to force a tinderbox build.
""",
u"""
I heard fixing spelling mistakes makes the tinderboxes happy (106386, r=me).
""",
u"""
Compilation fix for (r=me).
""",
u"""
Merge.
""",
u"""
Only set onTrace flag while running native code, not when recording (474771, r=brendan).
""",
u"""
Fixed multitrees assert regression from (, r=gal).
""",
u"""
- jsobj.cpp DEBUG / js_DumpObject crash on JSFunction with null proto. r=jorendorff
""",
u"""
Merge.
""",
u"""
Backed out changeset 05cbbc9f1ae2, which backed out (so this is re-landing 24106).
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Backed out changeset 17663da1b840 ().
""",
u"""
Backed out changeset 9fe03078c765 ().
""",
u"""
- TM: "Assertion failure: entry->kpc == (jsbytecode*) atoms[index]" with valueOf, regexp (r=jorendorff).
""",
u"""
- TM: Crash [@ JS_CallTracer] (r=jwalden).
""",
u"""
- Move fragment hit and blacklist counts to hashtable in oracle, r=gal.
""",
u"""
- TM: Add a way to keep stack values alive without emitting guard code.  r=gal.
""",
u"""
- TM: js_FastValueToIterator and js_FastCallIteratorNext can reenter. r=brendan. Note that this changeset alone does not fix the bug; an upcoming patch in completes the fix.
""",
u"""
Only emit alias check in for *PROP if the object's shape matches the global object's shape (475048, r=brendan).
""",
u"""
Backed out changeset 6657640cbbb2 - the patch from the caused leak and crash test failures
""",
u"""
-  Checking for MaybeGC conditions when allocating GC things in JS shell
""",
u"""
[arm] fix up ARM floating point comparisons; fixes ARM trace-test
""",
u"""
- "Assertion failure: sprop->setter != js_watch_set || pobj != obj, at jsdbgapi.c" (r=mrbkap).
""",
u"""
Fixed correctness and leak regression from landing (, r=gal).
""",
u"""
Merge.
""",
u"""
Fix incorrect reliance on the identity of the global object on trace (474888, r=brendan).
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
Make sure vpnum is not used incorrectly in the future (follow-up for 469044, r=shaver).
""",
u"""
Test-case for (r=me).
""",
u"""
Specialize trees to global types, so global type instability does not flush the cache (, r=gal,brendan).
""",
u"""
- Interpreter errors or pending exceptions should abort trace, r=brendan.
""",
u"""
: Trace cache OOM crash due to misplaced OOM check
""",
u"""
Backed out changeset a0e1d4a2404f - the patch for the causes timeouts in crash tests on Mac and Windows.
""",
u"""
- Checking for MaybeGC conditions when allocating GC things
""",
u"""
- Only throw errors when we have to. r=brendan
""",
u"""
Fix typo noted by bclary in 
""",
u"""
- Propagate EOF flags harder. r=brendan
""",
u"""
Backed out changeset e74857ea8248 - this caused unit test failures on Mac
""",
u"""
- Checking for MaybeGC conditions when allocating GC things
""",
u"""
- Fast natives don't enforce minargs, so we have to do it ourselves. r=jorendorff sr=brendan
""",
u"""
- Avoid roundtripping arbitrary jsids through JSAtom *s. r=brendan
""",
u"""
- PPC builds crash on startup. I moved the output of JS_STACK_GROWTH_DIRECTION inside a !CROSS_COMPILE block incorrectly in . This just moves it back.
""",
u"""
Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.
""",
u"""
Backed out changeset 81428de4b5dc (Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.).
""",
u"""
Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.
""",
u"""
Argh.
""",
u"""
Warning policing (please check and avoid adding).
""",
u"""
Fix for (Closed windows need two cycle collections to be collected). r=bent, sr=jst, a=jst.
""",
u"""
Back out changeset e919f0c1dfa9 (Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.) to try to fix red on leak tinderboxes.
""",
u"""
Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.
""",
u"""
Fix DEBUG_CC build. NPOTB.
""",
u"""
- JavaScript Tests by Jason Orendorff.
""",
u"""
- JavaScript Test by Brendan Eich.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Brian Crowder, moz_bug_r_a4.
""",
u"""
- JavaScript Tests by Blake Kaplan.
""",
u"""
- JavaScript Tests by Gary Kwong.
""",
u"""
- JavaScript Tests by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript tests by Jesse Ruderman.
""",
u"""
-  use FUN_OBJECT(callerFrame->fun) instead of potentially cloned callerFrame->callee; r=brendan
""",
u"""
Backed out changeset e81a7ff740bd for proper checkin (test drive, sorry :()
""",
u"""
-  use FUN_OBJECT(callerFrame->fun) instead of potentially cloned callerFrame->callee; p=bcrowder,r=brendan
""",
u"""
- snarf is no longer built by default in js.cpp, among other reverted changes, r=jorendorff, a=NPOTDB
""",
u"""
- Make __lookup[GS]etter__ work on quickstubbed properties by faking it for XPConnect prototype objects only. r=jorendorff sr=brendan
""",
u"""
Brad Lassey - - mkdepend crashes while compiling freetype, follow up push to js/src r=bsmedberg a191=beltzner
""",
u"""
- only MSVC needs jscpucfg.h... everyone else should be using jsautocfg.h and the configure-generated defines. If you're doing something crazy like cross-compiling from FreeBSD to Windows using MSVC, this will make your life happier r=crowder
""",
u"""
Back out changeset 32dc89bc34ad (Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.) to fix orange.
""",
u"""
Fix for (Cycle collector sometimes unlinks live cycles). r=bent, sr=jst.
""",
u"""
- "Assertion failure: sprop->setter != js_watch_set || pobj != obj, at jsdbgapi.c" (r=mrbkap).
""",
u"""
Several build failures on Solaris build for js/src r=danderson
""",
u"""
Several build failures on Solaris build for js/src r=danderson
""",
u"""
+ has a higher precendence than <<, so this needs to be parenthesized more... followup to 
""",
u"""
- update public failures.
""",
u"""
tests for , from sync of js/src/trace-test.js and js/tests/js1_8_1/trace/trace-test.js.
""",
u"""
Followup to - Use explicit casts instead of L/LL/int64, r=crowder
""",
u"""
- use stdint types instead of jscpucfg types, now that we have them auto-configured
""",
u"""
- move tools/test-harness/xpcshell-simple to testing/xpcshell; (Av1a-MC) Move the source harness directory; r=ted.mielczarek
""",
u"""
- Remove unused files from build/autoconf; +aclocal cleanup; r+sr=ted.mielczarek
""",
u"""
- fixing build bustage in xpcshell, GetCurrentDirectoryW doesn't exist on windows ce, punt on that platform r+sr=mrbkap
""",
u"""
-  Remove executable bit from files that don't need it. (Only changes file mode -- no code changes.) r=bsmedberg
""",
u"""
Backed out changeset 525e42406396, (jscpucfg-ectomy) due to Windows TUnit bustage.
""",
u"""
- Allow XPCNativeWrapper to unwrap SJOWs again. r+sr=jst
""",
u"""
- use stdint types instead of jscpucfg types, now that we have them auto-configured
""",
u"""
- Cleanup GTK includes; further cleanup + system-headers cleanup; r+sr=roc
""",
u"""
- Build error in accessible/public/msaa on x64 Windows with VC8; r=(m_kato + ted.mielczarek)
""",
u"""
prmjtime.cpp failed to compile on SunOS 5.* r=jim,crowder
""",
u"""
: --enable-system-lcms build option should be removed.r=bsmedberg,sr=ted.
""",
u"""
Merge backout of 
""",
u"""
Backed out changeset 700bca4b693f due to reftest failure ()
""",
u"""
Copy xpcshell instead of symlinking it, so that it knows where it is... Followup to 
""",
u"""
- Add ability to pass the GRE dir to xpcshell, r=ted
""",
u"""
- remove __count__ tests from js1_5/extensions/regress-434837-01.js and do not exclude it for 1.9.0 or later branches.
""",
u"""
update public failures.
""",
u"""
- limit the number of collected messages per test to less than 1000 to prevent post-process-logs.pl from running out of memory in extreme cases.
""",
u"""
- Limit skip() allocations in tracer, r=gal.
""",
u"""
Unbreak optimized builds so that jitstats typo-checking doesn't affect them; in builds without the global tracemonkey property, we won't have any known jitstats, so check for that case and don't do typo-checking when jitstats tests can't actually be performed.  r=graydon
""",
u"""
- Make behavior of +/- when one operand is an object with a custom valueOf consistent with non-JIT, even if for the moment that behavior is non-standard.  r=brendan
""",
u"""
: Protect sharpObjectMap in the presence of wrapped getters. r=igor
""",
u"""
- Protect |str| across the call to js_NewRegExp. r=jwalden
""",
u"""
backout merge
""",
u"""
Backed out changeset 562d8990f33a - with the fix for this workaround is no longer necessary.
""",
u"""
- fixing JS_GetOperationLimit to return the proper limit. r=mrbkap
""",
u"""
- fixup visibility of readline symbols. r=bsmedberg
""",
u"""
- add a __LOCATION__ field to the global object for files loaded on the commandline in xpcshell. r=timeless
""",
u"""
Backed out changeset 5d3af3ff9639. It doesn't allow UniversalXPConnect scripts to arbitrarily unwrap XPCNativeWrappers.
""",
u"""
- Allow XPCNativeWrapper to unwrap SJOWs again. r+sr=jst
""",
u"""
: Use configure-defined macros in #ifdefs for WinCE in js/src. r=crowder
""",
u"""
: Unshuffle system-specific definitions of PRMJ_Now. r=crowder
""",
u"""
Put nsIDOMNSCSS2Properties in its own file to reduce risk of bumping the IID of the wrong interface.  ()  r+sr=jst
""",
u"""
- browser components broken (checking in as bustage fix, asking for post-facto review from bsmedberg) - copy Ted's fix to js/src/config to fix TUnit bustage
""",
u"""
Branch merge for .
""",
u"""
Firefox 3 beta 4 gives unhelpful slowscript warning on leaving gmail, r+sr=mrbkap
""",
u"""
- (Back out) Standardize QueryInterface without throw, r=timeless, sr=sicking
""",
u"""
- Deal with XPCNativeWrapper.prototype properly. r+sr=jst
""",
u"""
- DumpJSStack() can set a pending exception in cx. r+sr=jst
""",
u"""
wallpaper for 
""",
u"""
- Don't attempt to compile a null buffer. r=igor
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
: JS tracing crash, typo in record_JSOP_CALL_GVAR, r=mrbkap
""",
u"""
Backed out changeset de45be487415, the real change I wanted to back out
""",
u"""
Backed out changeset 71cd51a61b67
""",
u"""
- using watchdog thread in js shell to trigger operation callback
""",
u"""
Remove a tab, kick tinderboxen to see if oranges are spurious or not
""",
u"""
- Make behavior of +/- when one operand is an object with a custom valueOf consistent with non-JIT, even if for the moment that behavior is non-standard.  r=brendan
""",
u"""
- consistent readline usage
""",
u"""
- TM: trace-test.js should throw an error when |test.jitstats| contains an unrecognized property name.  r=gal
""",
u"""
Extend tree on shape mismatch (473277, r=danderson).
""",
u"""
Trampolines can be 2 words, so take that into account when reserving space for LIR_call instructions (473225, r=danderson).
""",
u"""
Backed out changeset 8775c279e59c
""",
u"""
Trampolines can be 2 words, so take that into account when reserving space for LIR_call instructions (473225, r=graydon).
""",
u"""
Add new jitstats to the list in trace-test.js, and add a comment to jitstats.tbl noting that the two lists must be synchronized.
""",
u"""
Fix typos in jitstats property name; it's "sideExitIntoInterpreter", not "sideExits"; also bump iteration counts so it's more obvious at a glance that is unfixed (and that when it's fixed the fixedness will be clear).
""",
u"""
Fix the vim modeline.
""",
u"""
-  TM: "Assertion failure: JSVAL_IS_INT(STOBJ_GET_SLOT(callee_obj, JSSLOT_PRIVATE))" with __proto__, call, toString.  r=gal
""",
u"""
- unbox_jsval is infallible, make the signature reflect that.  r=gal
""",
u"""
Despite the previous log message, the previous push was r=brendan
""",
u"""
- Fix JSOP_NEWARRAY to be not-buggy and use it when possible.  NOT REVIEWED YET
""",
u"""
- Eagerly set the return value. r=brendan
""",
u"""
Track timeout side exits separately in jitstats (472761, r=jwalden).
""",
u"""
Push a dummy copy of EBP onto the stack to make sure EBP is aligned in the new stack frame (472791, r=graydon,edwsmith).
""",
u"""
Fix trace-test bustage due to my last checkin.
""",
u"""
-  TM: inconsistent (0 in d) where d is a String. r=brendan
""",
u"""
Destroying the temporary context used in evalcx and also doing a GC invalidates shape numbers, which kinda makes testing hard because it breaks shapeOf(evalcx("lazy")) === shapeOf(evalcx("lazy")); don't GC.  rs=brendan
""",
u"""
-  TM: "Assertion failure: cp >= buf" at homicideReport.php. r=gal.
""",
u"""
- Make analysis-tests work in out-of-tree objdir, r=jorendorff.
""",
u"""
fix check-sync-dirs to use the magic words for error output. (no bug)
""",
u"""
- export js/ system_wrappers to their own directory. r=jim
""",
u"""
Fix --enable-shark build bustage, r=ted. This is a temporary fix, real fix will be in .
""",
u"""
- tests for NaN/Infinity.toExponential(...)/toPrecision() should not check range, by szegedia%freemail.hu. Sync with CVS trunk.
""",
u"""
- update test to uniquely identify subtest results.
""",
u"""
sync developer trace tests with js test suite.
""",
u"""
- update sisyphus to build 1.9.1 from releases/mozilla-1.9.1 and 1.9.2 from mozilla-central.
""",
u"""
- JavaScript Tests by Igor Bukanov, Jesse Ruderman and Gary Kwong.
""",
u"""
- allow test parameter to be placed anywhere in query string.
""",
u"""
- obsolete test for 1.9.1 branch.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- update spidermonkey-n-1.9.1.tests to include missed test.
""",
u"""
- JavaScript Test by Boris Zbarsky, Andreas Gal.
""",
u"""
- JavaScript Test by Igor Bukanov.
""",
u"""
- JavaScript Test by Blake Kaplan.
""",
u"""
- JavaScript Test by Brendan Eich.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
followup from , forgot to sync up js/src/config/rules.mk
""",
u"""
Make DEBUG_CC compile again (broken by the fix for ). r=bent, NPOTB.
""",
u"""
- JavaScript shell should provide line editing facilities. r=bsmedberg
""",
u"""
- Build system should support building both a static and a shared library from the same Makefile. r=bsmedberg
""",
u"""
: Use autoconf to declare stdint types on platforms that don't have stdint.h r=bsmedberg
""",
u"""
Followup to (implement --disable-jit) - this block needs to be outside of the SKIP_COMPILER_CHECKS block so that it affects Windows
""",
u"""
- add a --disable-jit option, r=ted
""",
u"""
Backed out changeset 8f347bf50a53 due to x86-64 build bustage, and the fact that the committed patch didn't match the reviewed patch in an important way ()
""",
u"""
: --enable-system-lcms build option should be removed.r=vlad,sr=ted
""",
u"""
Add a static analysis pass to verify that for any do_QueryFrame<Interface> there is an Interface::kFrameIID declared. NPODB, static-checking only.
""",
u"""
- Add configure option to enable gczeal. r=crowder
""",
u"""
Add ability to mark JSDHashTable/PLDHashTable as immutable and thus prevent RECURSION_LEVEL assertions from firing due to lookups racing on multiple threads.  ()  r=brendan,mrbkap
""",
u"""
- JS not being PGOed on win32. r=bsmedberg
""",
u"""
- stop calling 'make install' for spidermonkey. r=bsmedberg,jimb
""",
u"""
part 2 - jsgc crashes with !JS_TRACER, r=jorendorff for immediate bustage fix, and I'll get ex-post-facto review from Igor
""",
u"""
part 1 - jsgc.cpp fails to compile with !JS_TRACER, initial patch by Igor, r=jorendorff with nits fixed by bsmedberg
""",
u"""
. Support a libnotify-based implementation of nsIAlertsService for GTK. r+sr=roc,r=ted
""",
u"""
Merge tracemonkey into mozilla-central.
""",
u"""
- replacing the branch callback with the operation callback. r=brendan
""",
u"""
- Annotations required by jsstack.js analysis, r=jorendorff.
""",
u"""
- Support terminating long-running scripts without using extra threads or signals. r=gal,sayrer
""",
u"""
Backed out changeset 763b96e81579 - I committed the wrong patch
""",
u"""
- Support terminating long-running scripts without using extra threads or signals. r=gal,sayrer
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
- Tighten assertion for JSFRAME_POP_BLOCKS on trace-entry frame, r=brendan.
""",
u"""
- TM: Add bytecode disassembly to JS_JIT_SPEW output (r=crowder)
""",
u"""
- TM: Make JSStackFrame reconstitution infallible (part 4 of 4, rename recoveryDoublePool to reservedDoublePool, r=brendan)
""",
u"""
- TM: Make JSStackFrame reconstitution infallible (part 3 of 4, call objects, r=brendan)
""",
u"""
- TM: Make JSStackFrame reconstitution infallible (part 2 of 4, stack, r=gal)
""",
u"""
- TM: Make JSStackFrame reconstitution infallible (part 1 of 4, easy stuff, r=gal)
""",
u"""
- Skip parentheses when doing optimizations based on parse node type. r=igor
""",
u"""
Move trace-test-math.js to math-trace-tests.js and remove trace.js because they defy my tab-complete-fu
""",
u"""
Merge.
""",
u"""
Backed out changeset adbe8e4b21dc due to tinderbox failures/timeouts (453157).
""",
u"""
Merge.
""",
u"""
Don't try to deallocate the trace recorder from inside one of its own instance methods (472049, r=brendan).
""",
u"""
-  watchdog thread as an alternative to operation count. r=myself,mrbkap
""",
u"""
Stop generating LIR when running out of memory in the regexp compiler (471924, r=danderson).
""",
u"""
: JS regression test bug with 'with (window) ...', r=mrbkap
""",
u"""
jsdIValue doesn't handle Unicode string values at all
""",
u"""
Add five crashtests
""",
u"""
Bustage fix from 
""",
u"""
- Ensure that the display is correct when evaluating a script in a stack frame. r=brendan
""",
u"""
- Don't automatically unwrap XOWs or SJOWs in XPCNativeWrappers. r+sr=jst
""",
u"""
- Deal with XPCNativeWrapper.prototype correctly. r+sr=jst
""",
u"""
Crash [@ jsdScript::CreatePPLineMap() ] with Firebug when invoking a non-function from an event handler.
""",
u"""
- invalid C++ in jsopcode.cpp, r=brendan
""",
u"""
- Use localtime_r when available, to improve Date reporting for locales like Venezuela on platforms like OS X.  r=mrbkap, r=ted (for build changes)
""",
u"""
- jsregexp.cpp should use dependent strings, r=igor
""",
u"""
- jsdIScript.isLineExecutable should return NS_ERROR_OUT_OF_MEMORY for oom, r=caillon
""",
u"""
- tolerate contexts which don't have a JSOPTION_PRIVATE_IS_NSISUPPORTS; r+sr=jst
""",
u"""
Use a single lirbuf for the tracer and rewind lirbuf during GC (471821, r=danderson).
""",
u"""
Store frame state information in the code cache and merely put a pointer to it onto the native call stack (470375, r=danderson).
""",
u"""
Fix for (Make quickstubs call nsINode/nsINodeList methods). r/sr=jst.
""",
u"""
- Some strong type conversion make GCC not complain; r=jorendorff sr=peterv
""",
u"""
part 1: make regexp compiler use one shared LIR buffer, r=gal
""",
u"""
- js1_7/decompilation/regress-379925.js | js1_8_1/decompilation/regress-371802.js FAIL (r=jorendorff).
""",
u"""
Merge.
""",
u"""
Attempted fix for : top crash in regexp LIR generation, r=gal
""",
u"""
Merge.
""",
u"""
Allocate the next page to be used in a lirbuf early to avoid running OOM during a page overflow (471316, r=danderson).
""",
u"""
- Decompiler fixes from (r=jorendorff).
""",
u"""
Merge.
""",
u"""
Backed out changeset 4acb47a25eb5
""",
u"""
Merge.
""",
u"""
Convert String objects into primitive strings when invoking String functions on them (470609, r=jorendorff).
""",
u"""
Make similar-acting code similar-reading as well (but not shared due to the +/- difference), no bug
""",
u"""
- during GC call js_GetTopStackFrame only for contexts with frames. r=brendan
""",
u"""
- Trace more == cases.  r=gal
""",
u"""
Add 19 crashtests
""",
u"""
Backed out changeset e0cce6a738c9 (- Make quickstubs call nsINode/nsINodeList methods) for failing mochitest
""",
u"""
Fix for (Make quickstubs call nsINode/nsINodeList methods). r/sr=jst.
""",
u"""
Merge for backout of changeset 55e23c647137 () so the backout for to solve can actually build
""",
u"""
Backed out changeset 55e23c647137 () so the backout for to solve can actually build
""",
u"""
Backed out changeset 73be1c836d7f () to see if that fixes Windows bustage ()
""",
u"""
Ho ho ho, it's a lump of hg coal. Merge.
""",
u"""
- fixing upgvar detection for for-in loop. r=mrbkap
""",
u"""
- Don't generate upvars on the left side of a for-in loop. r=brendan
""",
u"""
Backed out changeset 2d5e6b1c7254 - busted the WINNT 5.1 talos tracemonkey.
""",
u"""
- watchdog thread as an alternative to operation count. r=igor,mrbkap
""",
u"""
Fix bustage
""",
u"""
- TM: "switch(1/0){case Infinity:}" 4X slower with JIT enabled.  r=gal
""",
u"""
- JS_GET_SCRIPT_ATOM needs to use cx->fp safely, r=brendan
""",
u"""
- TM: Crash [@ js_EqualStrings].  r=brendan
""",
u"""
- TM: Behavioral difference in addition of objects between JIT, non-JIT.  r=brendan
""",
u"""
Backed out changeset 7184e014cd05 - the patch for bursted tgfx test on Windows.
""",
u"""
- watchdog thread as an alternative to operation count
""",
u"""
- using interrupt hook support in the interpreter for trace recording. r=brendan
""",
u"""
Backed out changeset 605fd1985d05 - more merge typos.
""",
u"""
- using interrupt hook support in the interpreter for trace recording. r=brendan
""",
u"""
Backed out changeset f13e2a2a5d66 - I was not careful when merging the unary op changes
""",
u"""
- using interrupt hook support in the interpreter for trace recording. r=brendan
""",
u"""
- TM: 20% slower to compute unary +/-.  r=brendan
""",
u"""
Whitespace patrol, move some tests before mandelSet where they should have been, add big scary warnings about not putting anything after mandelSet because they won't get run very often (not until just pre-commit, usually).
""",
u"""
- crashing LirBufWriter::insLinkToFar, r=danderson.
""",
u"""
- Calculate call-argument deltas relative to last word of LirCallIns, not first, r=danderson.
""",
u"""
Fix warnings pointed out by Waldo from apply patch (465214).
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
Back out patch for , it mysterious busts stuff.
""",
u"""
Merge, dammit!
""",
u"""
Merge m-c into tm again.
""",
u"""
Trace apply/call with an imacro (465214, r=brendan).
""",
u"""
and - prevent traces from writing to imported properties, r=brendan.
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
- avoiding js_(Add|Remove)Root for regexp statics. r=crowder
""",
u"""
- TM: fails to trace case with a type mismatch.  r=gal
""",
u"""
- operationCount as the first field in JSContext. r=brendan
""",
u"""
Fixed bogus assertion in a rare type-instability case (, r=gal).
""",
u"""
Merge.
""",
u"""
Backed out changeset 95b210c2fc92 preemptively. Seems to crash the browser.
""",
u"""
XP_MACOSX and DARWIN are not set in the shell, so use __APPLE__ (another follow-up for 465460, r=danderson).
""",
u"""
Merge.
""",
u"""
Trace apply/call using an imacro (465214, r=brendan).
""",
u"""
, bail off trace when readonly properties are written, r=brendan.
""",
u"""
. bustage fix.
""",
u"""
Return -0 for ceil if x < 0 and x > -1 (423231, r=jim).
""",
u"""
- TM: much slower than interpreter with short loop with |let| (r=mrbkap).
""",
u"""
- avoid useless duplication of Exception native. r=crowder
""",
u"""
- Add some basic tests for the red/green (cx->fp) analysis
""",
u"""
- js_DecompileValueGenerator uses cx->fp and should be made safe, r=crowder+jorendorff
""",
u"""
Follow-up fix for the follow-up fix for 465460 (r=me, again).
""",
u"""
Trivial follow-up fix for 465460 (r=me).
""",
u"""
Windows lacks ssize_t, who knew?
""",
u"""
- TM: valueOf ignored on third iteration of loop (r=gal).
""",
u"""
- Protect against apply on a non-function. r=gal
""",
u"""
- jsstack.js: give better locations for errors, r=dmandelin
""",
u"""
- red/green analysis (cx->fp) doesn't actually run the analysis, r=jorendorff
""",
u"""
- Add -j to the ./js usage string if the tracer is enabled. r=brendan
""",
u"""
- Protect the new scope object from garbage collection. r=crowder
""",
u"""
: Add coverage tests for traceable math native functions. r=mrbkap
""",
u"""
: Define traceable native versions of the rest of the math funcs. r=jorendorff
""",
u"""
Merge.
""",
u"""
Merge from m-c in an attempt to resolve mochitest startup crash in libnecko.
""",
u"""
- TM: crash (GMail): JS_Assert (s=0x368d8f "!JS_ON_TRACE(cx)", file=0x3724c8 "/Users/roc/mozilla-checkin/js/src/jsobj.cpp", ln=3765) (r=gal).
""",
u"""
-  restore utility of eval(s, o). r=mrbkap
""",
u"""
Backed out changeset 5f64a0d18e53
""",
u"""
Merge.
""",
u"""
Branch-exit and attach traces on shape mismatches (r=danderson).
""",
u"""
Backed out changeset f682453c06d0. Failing scriptaculous unit tests, doesn't build on windows or mac ppc.
""",
u"""
- TM: valueOf ignored on third iteration of loop (r=gal).
""",
u"""
- Back out further arm-wince breakage from recent merging activity.
""",
u"""
- JavaScript shell should provide line editing facilities. r=bsmedberg
""",
u"""
- Build system should support building both a static and a shared library from the same Makefile. r=bsmedberg
""",
u"""
: Move HAVE_ARM_SIMD test after header file tests. r=vladimir
""",
u"""
: Make js/src share the 'dist' tree with the enclosing build. r=ted.mielczarek
""",
u"""
- Cleanup the GTK nsFilePicker code; r+sr=roc
""",
u"""
- Enforce 'funobj' conditions in the XPCNativeWrapper case. r+sr=jst
""",
u"""
- Use a better function to compute principals. r=brendan
""",
u"""
: Test for setlocale at configure time in js/src r=crowder
""",
u"""
: Make js/src/configure take a --disable-arm-vfp option. r=vladimir
""",
u"""
- Don't use a subshell to recurse over DIRS when DIRS is empty (try #2) r=ted
""",
u"""
Back out patch for , it mysteriously busts stuff.
""",
u"""
- TM: Crash [@ js_String_getelem] (r=jorendorff).
""",
u"""
- "Assertion failure: StackBase(fp) + blockDepth == regs.sp" with |let| (r=gal).
""",
u"""
- TM: much slower than interpreter with short loop with |let| (r=mrbkap, a=sayrer).
""",
u"""
- Automatic semicolon insertion wrongly done after var with multi-line initializer (r=mrbkap, a=sayrer).
""",
u"""
: List the object files that depend on javascript-trace.h explicitly. r=bsmedberg
""",
u"""
(no bug): Add echo-tier-dirs target, to display tiers' directories.  r=bsmedberg
""",
u"""
Switch to sets module instead of using builtin set type to support Python 2.3 on mobile. Bustage fix.
""",
u"""
Fix for (Don't call FindTearoff when not needed and cache XPCNativeInterfaces in quickstubs). r/sr=jst.
""",
u"""
Fix for (Allow WrapNative to return a jsval without the wrapper). r/sr=jst.
""",
u"""
- DOMOperationCallback can get a JSContext with no global object. r=peterv sr=mrbkap
""",
u"""
- TM: crash (GMail): JS_Assert (s=0x368d8f "!JS_ON_TRACE(cx)", file=0x3724c8 "/Users/roc/mozilla-checkin/js/src/jsobj.cpp", ln=3765) (r=gal).
""",
u"""
Make nanojit build with VC7.1 r=danderson
""",
u"""
- Protect against enumerating the call object's prototype. r=brendan a=sayrer
""",
u"""
: fixed typo "ranslated" => "translated".
""",
u"""
bustage, if there's no revdepth.pl, it won't export very well
""",
u"""
: Removed test -n "$CROSS_COMPILE".  Moved
""",
u"""
- Scrape some gunk off the config/ grout, r=ted
""",
u"""
- libosso.h and hildon-uri.h should be defined in system-headers list. r=benjamin.
""",
u"""
- Back out further arm-wince breakage from recent merging activity.
""",
u"""
- back out most of changeset 2963765d5585 and ifdef-guard members of avmplus::Config, fix arm build.
""",
u"""
- Rewrite TraceRecorder::cmp, take five.  (Three, sir!)  Three!  r=gal
""",
u"""
.  Make JS_JIT_SPEW non-DEBUG build again.  r=dmandelin,brendan
""",
u"""
- enable static analysis for js/src, r=jorendorff
""",
u"""
- Censor access to block objects when they're the parents of functions. r=igor a=beltzner
""",
u"""
- configure doesn't set OS_TEST properly in 64-bit OS X builds. r=bsmedberg
""",
u"""
- Back out nanojit jump-patching machinery, r=danderson.
""",
u"""
- Minor adjustments to match changes in tamarin, r=gal.
""",
u"""
- Rename avmplus::AvmConfiguration, adjust sites of use, r=gal.
""",
u"""
Merge mozilla-central into tracemonkey, specifically to pick up .
""",
u"""
- isQuad(LIR_callh) on 32bit cpu's should be false (r=dvander+), r=danderson.
""",
u"""
- Fixed a couple more small nanojit injections, r=danderson.
""",
u"""
- LirBuffer has been modified to provide advance warning of out of memory (OOM) conditions, r=danderson.
""",
u"""
- trivial cleanups to simplify armjit merge (r=me), r=danderson.
""",
u"""
- -  Can not build tamarin-redux on solaris with Sun compiler. stejohns: review+, r=gal.
""",
u"""
- Fix cascading register spilling (r=rreitmai+), r=danderson.
""",
u"""
- TM: Assertion failure: JSVAL_IS_NULL(vp[0]) || (!JSVAL_IS_PRIMITIVE(vp[0]) && OBJ_IS_ARRAY(cx, JSVAL_TO_OBJECT(vp[0]))). r=gal.
""",
u"""
- Fixed bug causing too much spilling, other arm tweaks, r=danderson.
""",
u"""
- fix boundary bug injected by CallInfo change, r=gal.
""",
u"""
- redid nMarkExecute() to fix the bug. Now it always does exactly one page, r=gal.
""",
u"""
- Re-insert asm-counting code lost in previous redux-tracemonkey merge, r=gal.
""",
u"""
Fix bug in previous patch.
""",
u"""
- Read barrier for cx->fp. r=mrbkap, r=dmandelin.
""",
u"""
Dangit, why do the tests run correctly locally in small batches?  Backing out ...
""",
u"""
- Rewrite TraceRecorder::cmp, take two.  r=gal
""",
u"""
- make asm_output[123] varadic, and add some LIR instruction comments, r=gal.
""",
u"""
- internal tamarin-redux merge (mostly formatting), r=gal.
""",
u"""
- Macro-ize calls to new/delete to account for MMgc interactions, r=gal.
""",
u"""
- Change Fragmento's fragment map from a pointer to a member, r=gal.
""",
u"""
- js/tests/jsDriver.pl: eliminate CPAN dependency. r=bclary.
""",
u"""
Eliminate mergeCount from fragments since its unused (468391, r=danderson).
""",
u"""
Merge m-c to tracemonkey.
""",
u"""
Back out , seems I was wrong about the compile error and warning being the only bugs.
""",
u"""
Inherit context options from parent context when using evalcx in the shell (r=brendan, no bug).
""",
u"""
Followup fix for a typing bug (why wasn't I seeing errors with g++?) and a goto-past-initialization (which I also think should have been caught by g++).  r=bustage
""",
u"""
- Rewrite TraceRecorder::cmp.  r=gal
""",
u"""
Don't try to setup arguments when tracing Function.call() if we don't have at least 2 arguments (468174, r=brendan).
""",
u"""
Merge.
""",
u"""
Trace apply and call (462482, r=brendan).
""",
u"""
Fixed assembler errors not blacklisting the loop header, resulting in senseless re-recordings (, r=gal).
""",
u"""
Fixed crashing when deep aborting before a loop header (, r=gal).
""",
u"""
- |./js -b| crashes.  r=mrbkap
""",
u"""
Fixed a register allocation bug in nanojit when an argument using FST0 appeared twice in an argument list (, r=edwsmith).
""",
u"""
Fixed nanojit crashing when the reservation table filled (, r=rickr).
""",
u"""
- Math property flags regressed by .  r=brendan, a=sayrer
""",
u"""
fixed: make sure js_ThreadDestructorCB is called on main thread
""",
u"""
- TM: Better tracer support for |new Array(...)|. r=gal.
""",
u"""
(no bug) Use JS_FASTCALL for math_atan2_kernel.
""",
u"""
Merge.
""",
u"""
Guard on the JSFunction and parent pointers instead of the identity of the function object in case of shapeless calls (451974, r=brendan).
""",
u"""
: Fix result comparison function for trace tests. r=mrbkap
""",
u"""
: Use 'uneval' when printing expected and actual test results. r=mrbkap
""",
u"""
: Don't depend on type coercion when checking trace test results. r=mrbkap
""",
u"""
: Abstract out core code of math_atan2. r=brendan
""",
u"""
Fixed resolve hooks causing recorder to crash (, r=gal).
""",
u"""
Abort compilation of a regular expression if we run out of memory during recording (466588, r=danderson).
""",
u"""
Don't output JIT statistics if we don't ever record a trace (466942, r=danderson).
""",
u"""
Fixed TIMEOUT_EXIT guard being in the wrong location (from , r=gal).
""",
u"""
- post-landing style and cast fixes, sr=brendan.
""",
u"""
- Improve accuracy of tracemonkey's oracle, r=gal.
""",
u"""
Fixed regression checked in for (, r=gal).
""",
u"""
: compile regexps to native lazily, r=gal
""",
u"""
Fixed JSOP_NEG not checking overflow at recording time (, r=gal).
""",
u"""
Allow recorders to trash multiple trees on the way out (, r=gal).
""",
u"""
-  SpiderMonkey confusion over "-0" and "0" properties of an object.  r=brendan
""",
u"""
Test case to detect : case-insensitive mode in the native regexp compiler
""",
u"""
(no bug) Move definition of RESideExit *exit to top of function, to avoid error from GCC about jumping across its initialization.
""",
u"""
Fixed : use regexp source+flags as key to compiled code, r=gal
""",
u"""
Fixed : incorrect handling of 'i' flag in compiled regexps, r=gal
""",
u"""
Fixed double-free of treeInfo in a type instability edge case (, r=gal).
""",
u"""
Fix CALLPROP not guarding that the callee is not NULL (, r=gal).
""",
u"""
Fixed unsafe coercion of JSVAL_VOID to string on trace entry (, r=brendan).
""",
u"""
: Have js/src use symlinks when installing in dist. r=bsmedberg
""",
u"""
. r+sr=jst.
""",
u"""
- 'Workers: Allow JSON-able objects to be passed as messages to worker threads.' r+sr+a=jst.
""",
u"""
- 'uninitialized local variable warning in xpcwrappedjsclass.cpp'. r+sr=jst, a=blocking1.9.1
""",
u"""
- versioninfo for js3250.dll is bad. r=bsmedberg
""",
u"""
- JS_SealObject fails on Array objects (r=mrbkap, a=sayrer).
""",
u"""
- Crash/hang [@ mult][@ Balloc] when loading pages on PPC; Proposed patch for JS (trunk); r=jim
""",
u"""
, add config.mk to the GLOBAL_DEPS list as well
""",
u"""
Partially back out fix for to try to fix Txul regression on Windows.
""",
u"""
Partially back out fix for to try to fix Txul regression on Windows.
""",
u"""
- fix incorrect option in js1_5/Regress/regress-322430.js.
""",
u"""
- JavaScript Test by Andreas Gal.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Andreas Gal.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Tests by Jesse Ruderman.
""",
u"""
- JavaScript Test by Gavin Sharp.
""",
u"""
- JavaScript Test - modify expected results for js1_8_1/decompilation/regress-350991.js due to .
""",
u"""
- JavaScript Test by Igor Bukanov.
""",
u"""
- JavaScript Test by Gary Kwong and Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Brendan Eich.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Brendan Eich.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Gary Kwong.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
imported patch perl-permissions
""",
u"""
update public failures and universe.data.
""",
u"""
- Forgot to sync js's config/rules.mk; it would have been helpful if that were checked at build time rather than 'check' time.  r=redness still
""",
u"""
- Reduce the effort needed to write C++ tests.  r=ted
""",
u"""
-  windows compilers don't like variables named far r=crowder
""",
u"""
-  THIS is defined on windows mobile r=jim
""",
u"""
Merge backout of 
""",
u"""
Backed out changeset f71446b6fc7e: - directories are getting skipped, causing things like xpcshell not to be built
""",
u"""
: --with-static-checking is broken in spidermonkey. There is currently no useful static checking infrastructure for spidermonkey, so disable it for the time being, r=jimb
""",
u"""
Merge , , , , and 
""",
u"""
- test for the existence of jar.mn in make, rather than in a shell script: this allows us to avoid launching the subshell in the common case where a jar.mn is not present r=ted
""",
u"""
- Don't launch subshells to build subdirectories if there aren't any subdirectories to build r=ted
""",
u"""
- SIMPLE_PROGRAMS leads to bustage with generated.pdb r=ted
""",
u"""
- check for valid option name in js shell. r=crowder
""",
u"""
Fix for (Allow WrapNative to return a jsval without the wrapper). r/sr=jst.
""",
u"""
Version bump mozilla-central to 3.2a1pre/1.9.2a1pre. CLOSED TREE
""",
u"""
Add crashtest to CLOSED TREE
""",
u"""
Add crashtest for .  sdwilsh gave me permission to check in crashtests in today's CLOSED TREE.
""",
u"""
.  r=brendan, r=igor, a=beltzner
""",
u"""
merge to tip after backout
""",
u"""
Backed out changeset a4495a0cf2ff () to investigate Txul regression ()
""",
u"""
- Fix warnings in XPConnect. r/sr=jst, a191=beltzner.
""",
u"""
- JSExtendedClass requires an equality hook. r=crowder, a191=beltzner.
""",
u"""
Backed out changeset 037f635ced9f ()
""",
u"""
Merge to tip for peterv's bundle
""",
u"""
Fix for (Don't call FindTearoff when not needed and cache XPCNativeInterfaces in quickstubs). r/sr=jst.
""",
u"""
Fix for (Allow WrapNative to return a jsval without the wrapper). r/sr=jst.
""",
u"""
Fix for (memory leak while running SVG reftests). r/sr=jst.
""",
u"""
, Introduce GLOBAL_DEPS to build system
""",
u"""
Fix - Provide a readline function for xpcshell to read a line from stdin. r/sr=mrbkap,a191=beltzner,p=philipp,dbo
""",
u"""
Backed out changeset 17842a2d0c7f () due to test failures
""",
u"""
- 'Workers: Allow JSON-able objects to be passed as messages to worker threads.' r+sr+a=jst.
""",
u"""
- 'Following Error console link causes uncaught exception ( 0x80004002 (NS_NOINTERFACE) [nsISupports.QueryInterface] ).' Followup fix for JS impls. r+sr=jst, a=blocking1.9.1+
""",
u"""
- JavaScript Tests - deal with changes in decompilation and behavior from .
""",
u"""
- JavaScript Tests - Do not force language version upon non-Gecko browsers.
""",
u"""
- JavaScript Tests - default browser tests to non jit.
""",
u"""
- JavaScript Tests - update slow-n.tests, add branch specific slow-1.8.1.tests, slow-1.9.0.tests, slow-1.9.1.tests.
""",
u"""
: Fix test case result comparison function.
""",
u"""
- fall out from getTestCase numeric/NaN comparison .
""",
u"""
No bug - JavaScript Tests - sync js/tests/js1_8_1/trace/trace-test.js and js/src/trace-test.js
""",
u"""
- JavaScript Test by Joachim Kuebart.
""",
u"""
- JavaScript Test by Chris Evans.
""",
u"""
- JavaScript Tests - deal with changes in decompilation and behavior from .
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Brendan Eich.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- JavaScript Test by Jesse Ruderman.
""",
u"""
- Sisyphus - JavaScript Tests - add option to perform depends builds to bisect.sh.
""",
u"""
- JavaScript Test - fix test so iframe is properly appended to document. Diagnosis by Ben Turner.
""",
u"""
- Sisyphus - JavaScript Tests - update known failures.
""",
u"""
Make nanojit build with VC7.1 r=danderson a191=beltzner
""",
u"""
, r=brendan a191=beltzner
""",
u"""
, r=brendan a191=blocker
""",
u"""
Backed out changeset 7bc1ba9f91fe to fix test orange
""",
u"""
- Checking for MaybeGC conditions when allocating GC things.
""",
u"""
, r=brendan a191=blocking
""",
u"""
: version/config bumps for Firefox 3.1b2. r=anodelman CLOSED TREE
""",
u"""
Bump JS milestone.txt file manually (because automation didn't know anything about it). CLOSED TREE
""",
u"""
Backed out changeset 700ae4e59496 - caused talos oranges. CLOSED TREE
""",
u"""
- watchdog thread as an alternative to operation counting, r=igor,mrbkap a19b2=beltzner (CLOSED TREE)
""",
u"""
Backed out changeset 04cecb0ec24c to see if it fixes tinderbox oranges. CLOSED TREE
""",
u"""
- using watchdog thread as an alternative to the operation count. r=igor,mrbkap a19b2=beltzner (CLOSED TREE)
""",
u"""
Backed out changeset c54f1957d564 - - build system changes caused mouchi test failures. CLOSED TREE
""",
u"""
- using watchdog thread as an alternative to the operation count. r=igor,mrbkap a1.9.0b2=beltzner (CLOSED TREE)
""",
u"""
- There must always be at least one source note. r=brendan a=sayrer
""",
u"""
- DVG confused by |let|. r=brendan a=sayrer
""",
u"""
Backed out changeset 8329a91db67d - , CLOSED TREE
""",
u"""
- watchdog thread as an alternative to operation count. r=igor,mrbkap a1.9.0b2=beltzner
""",
u"""
- "Following Error console link causes uncaught exception ( 0x80004002 (NS_NOINTERFACE) [nsISupports.QueryInterface] )". r+sr=jst, a=mconnor.
""",
u"""
Backed out changeset 1d817f9d842f per beltzner
""",
u"""
- watchdog thread as an alternative to operation count. r=igor,mrbkap a1.9.0b2=blocker
""",
u"""
Fix CALLPROP not guarding that the callee is not NULL (, r=gal).
""",
u"""
Fixed unsafe coercion of JSVAL_VOID to string on trace entry (, r=brendan).
""",
u"""
Backing out due to Mac build failure
""",
u"""
. Solaris bustage fix. r=neil@httl.net,sr=jst,a=beltzner
""",
u"""
. Have js/src use symlinks when installing in dist. r=bsmedberg,a=sayrer
""",
u"""
Merge mozilla-central into tracemonkey
""",
u"""
I hate hg.
""",
u"""
- nested imacro abort not cleanly handled (botches assertions) (r=mrbkap, a=beltzner).
""",
u"""
Merge.
""",
u"""
NAMEDEC was incorrectly traced as a pre-decrement operator (465424, r=danderson).
""",
u"""
Check for obj being null in the JSOP_IN builtin used by the tracer (453565, r=danderson).
""",
u"""
Fix Mac OS X build failure (no bug).
""",
u"""
Comparing a string against a boolean does not always produce false (465136, r=danderson).
""",
u"""
Null converts to 0 for relations but to NaN for equality (465252, r=danderson).
""",
u"""
Merge.
""",
u"""
Inspect the actual values before trying to demote an arithmetic operation (465337, r=danderson).
""",
u"""
Adding some tests
""",
u"""
Added nanojit comment clarifying register allocation with shift instructions.
""",
u"""
Don't attempt to immediately re-record after walking out of a thin loop (465366, r=danderson).
""",
u"""
Patch for introduces buggy js_Int32ToId (465347, r=gal).
""",
u"""
Tracemonkey will crash if the compiler doesn't have FASTCALL r=danderson
""",
u"""
Don't demote multiplication, even if result is demoted and inputs are demotable (465308, r=danderson).
""",
u"""
Make sure to flush the JIT cache after a gc even if we didn't import globals (464418, r=brendan, 2nd attempt to push).
""",
u"""
Merge.
""",
u"""
Don't attempt to do CSE across labels (465276, r=danderson).
""",
u"""
No else after return if you please.
""",
u"""
Fixed regression from recent constant folding patch (, r=gal).
""",
u"""
Inline int32 to id fast path into the builtins (465268, r=danderson).
""",
u"""
Merge.
""",
u"""
Fix tracing of JSOP_IN (465241, r=danderson).
""",
u"""
Fixed branch traces being erroneously marked as dependent trees (, r=gal).
""",
u"""
Merge.
""",
u"""
Fixed edge case in nanojit register allocation for shl/shr (, r=gal).
""",
u"""
Can't bypass ECMADoubleToInt32 in js_StringToInt32 (465239, r=danderson).
""",
u"""
Merge.
""",
u"""
JIT affects truthiness of "" <= null (465234, r=Waldo).
""",
u"""
Constant fold additions to avoid erroneous isPromoteInt detection (, r=gal).
""",
u"""
- TM: JIT thinks !NaN is false.  r=gal
""",
u"""
Fixed deep abort logic when onTrace is set without a recorder (, r=gal).
""",
u"""
Merge.
""",
u"""
Backed out changeset 2601301b793d
""",
u"""
Backed out changeset 523c3f3dc744
""",
u"""
Make linux gcc happy by moving the declaration of RESideExit* exit to the top of the function (no bug).
""",
u"""
Use regexp string as key for the regexp fragment cache (464866, r=brendan).
""",
u"""
Merge.
""",
u"""
Removed bogus assert when stringifying objects (465209, r=brendan).
""",
u"""
Fixed recorders already deeply aborted being pushed onto the deep abort stack (, r=gal).
""",
u"""
: Drop JSON.jsm. r=gavin, r=sayrer, sr=brendan, a1.9.1b2=beltzner
""",
u"""
- fixing sprop management, r=brendan, a.9.1b2=sayer
""",
u"""
- removal of no longer applicable asserts that sp <= static spdepth. r=brendan a1.9.1b2=beltzner
""",
u"""
Removed bogus assert when stringifying objects (465209, r=brendan, a=mconnor).
""",
u"""
Avoid bogus assertbotch (more work needed to reconstruct imacro stack depth).
""",
u"""
Implement ordered comparison for objects (465133, r=brendan).
""",
u"""
Deep abort recorders outer recorders if we need to flush the JIT cache early (, r=brendan,gal).
""",
u"""
- TM: JIT: Initializing an array to a constant in a loop doesn't work for some constant values.  r=brendan
""",
u"""
Fast followup to pick nit in last commit.
""",
u"""
- TM: General Error trying to play video on CNN (r=gal).
""",
u"""
- TM: hang with "[] + null" (r=danderson).
""",
u"""
- Support script timeouts in compiled code, r=gal.
""",
u"""
- Crash trying to compile a trace generated from stdin in debug build.  r=danderson
""",
u"""
-  Don't use -Os with Intel C/C++ compilers r=ted.mielczarek
""",
u"""
: remove committed debugging 'echo'.  r=bsmedberg
""",
u"""
Fix bogus assertion left in .
""",
u"""
Fix bogus assertion left in .
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Compile native code for regexp first and don't shrink bytecode (464867, r=dmandelin).
""",
u"""
: win32 crash in w/ regex compiler, r=gal
""",
u"""
Don't flush JIT cache from within the recorder (464403, r=brendan).
""",
u"""
Fix from Ginn Chen <ginn.chen@sun.com> for .
""",
u"""
Fast followup to fix for-each-in (imacros bug, r=me).
""",
u"""
- (imacros) TM: Make conversion work on arbitrary JSObjects (r=gal).
""",
u"""
Fixed recursion in thin loops accidentally trying to close the parent loop (, r=gal).
""",
u"""
Remove '\n' from NanoAssertMsgf calls (made redundant by the patch in )
""",
u"""
: regression suite stack oflow on windows with regex compiler, r=gal
""",
u"""
Backed out changeset a40f2117bcc0
""",
u"""
Add imacros to support conversion of arbitrary JSObjects (456511, r=gal).
""",
u"""
- various JSOP_APPLY fixes. r=brendan
""",
u"""
Backed out changeset 313d3d61333d
""",
u"""
Make sure to flush the JIT cache after a gc even if we didn't import globals (464418, r=brendan).
""",
u"""
Don't allocate a new lirbuf if we already have a fragment for the regexp (464413, r=brendan).
""",
u"""
- Need an equivalent to jsopcode.tbl, but for LIR opcodes/instructions, take two.  r=gal, r=edwsmith on the first iteration as well
""",
u"""
: invalid use of regexp addr as unique key, r=gal
""",
u"""
: Use automatic variables in make rules, to allow VPATH to work. r=ted.mielczarek
""",
u"""
- Be less wasteful when emitting escapes. r=sayrer
""",
u"""
warnings in jstracer
""",
u"""
/Nativei386.cpp(148) : warning C4309: 'initializing' : truncation of constant value
""",
u"""
Backed out changeset cb559a14ad77
""",
u"""
- Need an equivalent to jsopcode.tbl, but for LIR opcodes/instructions.  r=gal, r=edwsmith
""",
u"""
jit pref isn't honored by regexp code
""",
u"""
: Restore js/src/Makefile.ref and supporting files. r=brendan
""",
u"""
: Don't find generated SpiderMonkey headers via VPATH. r=bsmedberg
""",
u"""
: Don't be confused by .deps dirs in the source tree. r=bsmedberg
""",
u"""
Backed out changeset dbb2a6559cf5
""",
u"""
: lazy compilation of regexps to native, r=gal
""",
u"""
b=464010, remove bogus #ifdef JS_TRACER in jsregexp.cpp that got rid of regexp.test on non-JS_TRACER builds; r=sayrer
""",
u"""
Make xterm updates work with PARALLEL_DIRS for those people not on -j19 r=ted
""",
u"""
Backed out changeset ec9a1864d1fb from , drop JSON.jsm due to OSX
""",
u"""
: drop JSON.jsm. r=gavin, r=sayrer, sr=brendan, a1.9.1b2=beltzner
""",
u"""
Fixing . Fixing crash on Windows with native regexp compiler. r=gal
""",
u"""
Fixing . Native regexp compiler regression sweet crash. r=gal
""",
u"""
- "Assertion failed: _stats.freePages == _stats.pages". r=brendan
""",
u"""
Fix for (Cache DOM wrappers in the DOM object). r/sr=jst.
""",
u"""
: Record dependency on generated header javascript-trace.h, r=mrbkap, NPOB
""",
u"""
Followup to to remove redundant line r=ted a=beltzner
""",
u"""
Fixing build bustage and nits from .
""",
u"""
- Intermittent JS regexp error on tinderbox. r=gal a=dsicore
""",
u"""
JavaScript Tests - tests for bugs 461233, 458851, 459628, 460024, 460117, 461307, 461723, 462292, 462989, 463259, 460501, 461108, 461111, 461235, 461945, 462071, 462282, 462288, 462407, updated js1_8_1/trace/trace-test.js, updated failures
""",
u"""
b=464010, remove bogus #ifdef JS_TRACER in jsregexp.cpp that got rid of regexp.test on non-JS_TRACER builds; r=sayrer
""",
u"""
[arm] b=462430, implement LIR_ldcs, re-enable regexp jit for ARM
""",
u"""
[arm] Fix up ARM nj backend to take into account exit block merging and other changes.  Also simplify some branch code along the way.
""",
u"""
[arm] Disable regexp tracer on ARM
""",
u"""
whitespace/tab cleanup in NativeARM.cpp
""",
u"""
Backed out changeset 594ec832d9a8
""",
u"""
Add back typedef for JSTraceMonitor (compilation fix for legacy C use of JS engine includes, no bug).
""",
u"""
Trace Function.apply and Function.call (462482, r=brendan).
""",
u"""
Don't spill type definitions in avmplus.h into the global namespace (462288, r=danderson).
""",
u"""
Merge.
""",
u"""
Cleanup GuardRecord, SideExit, and InterpStruct and extract VM-dependant fields (463313, r=danderson).
""",
u"""
- Assertion failure with "for (;;[]=[])" (r=mrbkap).
""",
u"""
Fixed multitrees assert when building failed speculated branches (, r=gal).
""",
u"""
If the regexp cache runs full flush it and make sure to keep bytecode version around in case the native code was thrown away (463281).
""",
u"""
Fix GC hangs when OOM during recovery pool re-allocation (463190, r=brendan).
""",
u"""
Use GuardRecord/SideExit provided by the tracer in regexp (463281, r=danderson).
""",
u"""
- "Assertion failure: VALUE_IS_FUNCTION(cx, fval)" (r=mrbkap).
""",
u"""
: remove extraneous comment, indexed loads are generated automatically
""",
u"""
: regexp compiler, style fixes, r=brendan
""",
u"""
: oom handling, somehow omitted from original commit, r=gal
""",
u"""
Fixed memory leak in nanojit's LabelStateMap (no bug, r=gal).
""",
u"""
Scale down regexp native code cache to 1MB and delete cache on shutdown (r=danderson).
""",
u"""
Fix using wrong regalloc helper in asm_ld peephole opt (r=rreitmai).
""",
u"""
Peephole optimize various LIR load patterns for x86 addressing (, r=gal).
""",
u"""
Fix MSVC sensitivity to symbols called 'far'
""",
u"""
Fixing regexp compiler nanojit spew to conform with TM
""",
u"""
Adding JS_TRACER guards to regexp compiler for ppc builds & other non-tracing
""",
u"""
Adding cast to make MSVC happy
""",
u"""
Fixing Linux breakage, stupid jump crosses initialization errors
""",
u"""
Fixing OSX build, seems related to namespace trickery
""",
u"""
Merge.
""",
u"""
Interpreter directly emits the this object found in the property cache for JSOP_CALLNAME, so do the same in the tracer (462989, r=mrbkap).
""",
u"""
WIP: compiling simple regexps, r=danderson,agal
""",
u"""
- Add interface to disconnect and reconnect loops in nanojit, r=gal.
""",
u"""
- Merge code-patching functions in nanojit, r=rreitmai.
""",
u"""
Merge mozilla-central to tracemonkey.
""",
u"""
Don't cache pointer to recorder since it might change in js_MonitorRecording (462980, r=gal).
""",
u"""
Fixed memory leak in LInsHashSet (, r=gal).
""",
u"""
: API to delete a single fragment, r=danderson
""",
u"""
Fixed OOM handling when starting a recorder or assembler (, r=gal+rreitmai).
""",
u"""
- Add a JS_ValueToSource API. r=brendan
""",
u"""
- "Assertion failure: UPVAR_FRAME_SKIP(uva->vector[i]) == 1" with nested eval (r=mrbkap).
""",
u"""
- "Assertion failure: slot < fp2->script->nslots" with nested eval (r=mrbkap).
""",
u"""
Preserve param1 over loop iters if it is used, desk r=danderson
""",
u"""
Fix build breakage --with-static-checking. No bug#.
""",
u"""
Don't manipulate stack during cpuid detection (fix for icc, r=danderson).
""",
u"""
Emit JSOP_APPLY for .call(...) (462445, r=brendan).
""",
u"""
Make sure double slots are marked as undemotable when stabilizing a tree with failed speculation (, r=gal).
""",
u"""
Resolve atom/str naming conflicts in the source for narcissus, make narcissus extensions compile again (462436, r=brendan).
""",
u"""
Add 16-bit non-volatile loads to nanojit (454301, r=danderson).
""",
u"""
Don't coerce void to string when compiling inner tree calls (, r=gal).
""",
u"""
Merge.
""",
u"""
Fixed assert (fallout from 462265).
""",
u"""
Added multitrees test to trace-tests.js for .
""",
u"""
Added multitrees test to trace-tests.js for .
""",
u"""
Fixed not tracking linked peers as dependencies (, r=gal).
""",
u"""
Perform Function.apply in the interpreter loop bypassing js_Invoke (462265, r=brendan).
""",
u"""
Merge.
""",
u"""
Fix missing JSOP_APPLY case in an assert and a condition (462292, r=brendan).
""",
u"""
.  Make INCLUDE_VERBOSE_OUTPUT actually work, and rename it to JS_JIT_SPEW.  r=brendan
""",
u"""
Mark any double slot in an unstable exit as undemotable (, r=gal).
""",
u"""
ug 460870 - Round-trip change with RHS of || (r=jorendorff).
""",
u"""
Fixed trees stabilizing from the wrong peer fragment (, r=gal).
""",
u"""
Bump XDR version, followup from changeset bd981b7737da (r=gal).
""",
u"""
Remove JSOP_UNUSED78 as 78 is now JSOP_APPLY (follow-up for 462209).
""",
u"""
Merge.
""",
u"""
Emit JSOP_APPLY for .apply(...) similar to JSOP_EVAL for .eval(...) (462209, r=brendan).
""",
u"""
- Followup correctness fix. r=brendan.
""",
u"""
- Incorrect decompilation of ({0: (4, <></>) }). r=brendan.
""",
u"""
-  Bind containing function to eval script, so upvars work in decompiler. r=brendan
""",
u"""
Prune deadwood missed in commit for .
""",
u"""
- TM: We don't trace some variants of string + other type (gal+brendan red-headed stepchild).
""",
u"""
Merge.
""",
u"""
Handle dslots == NULL case when reading past the actual length of an array (461974, r=danderson).
""",
u"""
Keep testGlobalProtoAccess last.
""",
u"""
Fixed false-positive integer demotions on non-number types (, r=gal)
""",
u"""
GC no longer flushes the JIT cache. Instead just make sure the shape of the global object will mismatch next time we try to record or execute code, which in turn will force a flush of the code cache (458288, r=brendan/danderson).
""",
u"""
Re-land patch for now that latent bug it uncovered (not filed; see hg log) is fixed.
""",
u"""
Merge.
""",
u"""
Fix tracing apply with wrong arguments (no bug, r=gal+dvander).
""",
u"""
- TM: "Assertion failure: (m != JSVAL_INT) || isInt32(*vp)" with "(0 + void 0) && 0". r=gal.
""",
u"""
Backed out changeset d4fe79372140 () due to persistent orange on TraceMonkey tinderboxes.
""",
u"""
Keep this test last, and clean up prototype pollution, plus test for .
""",
u"""
- TM: for-in loops skip every other value in certain cases (r=gal/mrbkap).
""",
u"""
Implemented multiple type specialized trees per entry point (, r=gal)
""",
u"""
. Fix JSON top crash. r=brendan
""",
u"""
- Fix the scope returned from Components.utils.lookupFunction. r=bzbarsky sr=jst
""",
u"""
Backed out changeset 874aba8a9a8a to fix orange
""",
u"""
Fix for (Cache DOM wrappers in the DOM object). r/sr=jst.
""",
u"""
- 'XPCVariant used in nsXPCException::SetThrownJSVal can cause cycle collection on non-main threads'. r=bent, sr=jst.
""",
u"""
- 'Bring workers up to latest spec'.r+sr=jst.
""",
u"""
- JavaScript Tests - update public failures, universe data
""",
u"""
- Building spidermonkey on Windows with -j3 fails: conflicts in PDB files. Related to and , where we flip-flop back and forth about this. Document the way things should actually be!
""",
u"""
Backed out changeset 4fc7c6f6f45e
""",
u"""
- "Bring workers up to latest spec". r+sr=jst.
""",
u"""
Back out changeset b83d3c8ac166 () to try to fix bustage
""",
u"""
Backing out changeset dc1aff36a411 () to try to fix bustage
""",
u"""
- 'Crash [@ xpc_qsSelfRef::~xpc_qsSelfRef] with getUserData.call'. r+sr=jst.
""",
u"""
- 'XPCVariant used in nsXPCException::SetThrownJSVal can cause cycle collection on non-main threads'. r=bent, sr=jst.
""",
u"""
- 'Bring workers up to latest spec'.r+sr=jst
""",
u"""
Backed out changeset 47c0377779bb to fix orange
""",
u"""
Backed out changeset 81c0a2ec449f to fix orange
""",
u"""
Fix for (Crash [@ xpc_qsSelfRef::~xpc_qsSelfRef] with getUserData.call). r/sr=jst
""",
u"""
Fix for (Cache DOM wrappers in the DOM object). r/sr=jst.
""",
u"""
- Remove unused PACKAGE_FILE and PACKAGE_VARS and .pkg files, mozilla-central part, r=bsmedberg
""",
u"""
- Parallel builds with -j20 don't build the submakefiles before recursing into them. Switch back to using $* in the rule because we found out the make 3.80 bug: it doesn't set $* in double-colon rules, but it does in single-colon rules. r=ted (copy rules.mk to the JS build system)
""",
u"""
Backed out changeset ba895ab8cbe7 to fix orange
""",
u"""
Fix for (Cache DOM wrappers in the DOM object). r/sr=jst.
""",
u"""
- add -isysroot to find fat version of system libraries
""",
u"""
Fix for (Remove QI on 'this' object when calling from JS to C++). Patch by jorendorff and me, r/sr=jst.
""",
u"""
- Build fails on mac in js/src/configure.in with error: Library requirements (glib-2.0 >= 1.3.7 gobject-2.0) not met; glib part; r=ted.mielczarek
""",
u"""
- Build fails on mac in js/src/configure.in with error: Library requirements (glib-2.0 >= 1.3.7 gobject-2.0) not met; elf-dynstr-gc part; r=ted.mielczarek
""",
u"""
- "Assertion failure: slot < fp2->script->nslots" with nested eval (r=mrbkap).
""",
u"""
TM: Crash when JavaScript-Debugger is enabled [ @ jsd_lock ]
""",
u"""
- Creating directories is really racy, and has an rm -rf in the middle of the race, r=ted
""",
u"""
- JavaScript Tests - update tests
""",
u"""
- javascript autoconf busted on windows mobile. r=ted
""",
u"""
TUnit bustage fix from follow up to - fix a bug in make 3.80 by avoiding  in pattern rules with explicit targets and keep mozilla/config and mozilla/js/src/config in sync. r=ted over irc
""",
u"""
- add support for PARALLEL_DIRS to build system, parallelize content. r=bsmedberg
""",
u"""
Handle dslots == NULL case when reading past the actual length of an array (461974, r=danderson).
""",
u"""
(fix tree burn; no bug): The js/src subtree needs its own copy of pgomerge.py.
""",
u"""
Fix Win32 burn: js/src/config/autoconf.mk shouldn't override MOZ_MEMORY-related LIB and PATH exported from top-level config/autoconf.mk
""",
u"""
Merging for 
""",
u"""
Merge (autoconf build environment for SpiderMonkey) again.
""",
u"""
Merge (autoconf build environment for SpiderMonkey).
""",
u"""
: Compare SpiderMonkey's copies of build files with originals at check time. r=luser
""",
u"""
: Record configuration details in an installable header. r=bsmedberg
""",
u"""
: Allow SpiderMonkey to be built on its own, or as part of Mozilla.
""",
u"""
: Delete SpiderMonkey's custom build system for separate builds. r=bsmedberg
""",
u"""
Fix red on mozilla-central because js.cpp doesn't build on Windows. No bug#.
""",
u"""
: Build SpiderMonkey stand-alone shell by default. r=ted.
""",
u"""
- TM: v8-richards.js benchmark opens a print dialog in browser with JIT enabled. r=brendan
""",
u"""
Fix build breakage from 70955fd0d1ee on platforms without JS_TRACER. No bug#.
""",
u"""
- Traceable print and shapeOf functions for js shell. r=mrbkap.
""",
u"""
Fixed trace-tests for isPromoteInt patch which reduced tree recompilation counts.
""",
u"""
Merge.
""",
u"""
guardDenseArray and guardDenseArrayIndex must guard on the actual outcome, since we don't always abort trace if its not a dense array (461611, r=me).
""",
u"""
Fixed false positive demotions due to missing isPromoteInt (, r=gal).
""",
u"""
Trace reading from dense arrays out of bounds and trace undefined -> number conversion in binary ops (461611, r=brendan).
""",
u"""
- Clear Function and Object (and any other properties) off of the outer object so that Function always refers to the inner window's function. This ensures that the implict Function and explicit window.Function forms refer to the same object. r+sr=brendan
""",
u"""
Fixed branch demotions using the branch PC rather than the root PC, causing infinite records (, r=gal).
""",
u"""
- Remove JSOP_RESUME (r=gal/jorendorff).
""",
u"""
Disabled x64 JIT in shell until the port is cleaned up from nj2.
""",
u"""
- Extra parens in decompilation of "if(a, b)". r=brendan.
""",
u"""
- TM: INT32 can't be used as return type for traceable native that actually returns an int. r=gal.
""",
u"""
Fixed crash from JIT cache flushes when js_Interpret was holding TraceRecorders (, r=brendan).
""",
u"""
- No public API for OBJ_GET_PROPERTY or the JavaScript [] operator (and similar functions). r=brendan.
""",
u"""
Merge.
""",
u"""
Eliminate warning about ignored visibility attribute on js_CloseIterator when compiling jsbuiltins.cpp. No bug#. r=brendan.
""",
u"""
Fix blatant bugs in jsbuiltins.h. No bug#. r=dvander.
""",
u"""
- Crash [@ QuoteString] with for(/x/[''] in []) (r=mrbkap).
""",
u"""
Only track and look up LOOP_EXIT side exits in the tree info (r=danderson).
""",
u"""
Fix memory leak in LInsHashSet::grow - r=danderson
""",
u"""
Make sure we set remaining fslots to void in FastNewDate (459628, r=brendan).
""",
u"""
Backed out changeset 82f5fed6d91a (Linux GCC doesn't seem to like clobbering ebx in inline assembly).
""",
u"""
Added test-case for 459630 (WFM) to make sure we don't regress it down the road.
""",
u"""
Avoid pusha/popa inside assembly (icc crashes) when checking for SSE2 using cpuid (461280, r=danderson).
""",
u"""
Backed out changeset 91277d409f44 (accidentally also touched Makefile.ref and config/Darwin.mk)
""",
u"""
Enable JIT by default for content (r=danderson).
""",
u"""
Re-use loop exit side exit if we already have one for that PC location and the same type map (461076, r=danderson).
""",
u"""
Use LIR_loop for loop edge to avoid going into a side exit handler at every loop edge (461231, r=danderson).
""",
u"""
- "Assertion failure: pos == GET_UINT16(pc)" decompiling function with array comprehension (r=mrbkap).
""",
u"""
- make callee-save LIR_param use optional. r=gal,edwsmith
""",
u"""
- for-in loops should use one backward branch (with downward goto on entry; r=mrbkap).
""",
u"""
- Extra parens in decompilation of "a += b = 3". r=brendan.
""",
u"""
- Decompiler emits extra parens around assignment in "for(;;)" condition. r=brendan.
""",
u"""
[arm] fix build after SideExit sharing patch
""",
u"""
[arm] correctly have chk version of LD underrunProtect
""",
u"""
[arm] misc codegen fix
""",
u"""
[arm] Use real B/BX instead of BL for side exit jumps; no need to update lr
""",
u"""
[arm] Get rid of CALL, just use BL directly
""",
u"""
[arm] Get correct value in return reg after fragment exit
""",
u"""
[arm] Enable VFP
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Remove code to unlink trees to reduce the size of GuardRecord. Allow GuardRecords to share one common SideExit structure. The VM places both explicitly into the LIR (460538, r=danderson).
""",
u"""
- Yet more macros for defining builtins. r=brendan
""",
u"""
- Substring needs to validate its arguments. r=brendan
""",
u"""
- Round-trip change due to "&&" constant-folding leaving extra parens. r=brendan.
""",
u"""
- TM: Inconsistent results from hasOwnProperty with JIT enabled. r=brendan.
""",
u"""
[arm] Use correct register for return value; also don't bother saving full set of callee-saved registers using PUSH, they'll be saved individually
""",
u"""
More ARM fixes; initialize free reg list correctly initially.  Also use LastReg+1 instead of NJ_MAX_REGISTERS in RegAlloc -- LastReg+1 is what's used in the .h file, to avoid any mismatches.
""",
u"""
- TM: builtins js_Any_getelem, js_Any_setelem should take int32. r=gal.
""",
u"""
Make ARM nanojit compile again (doesn't run)
""",
u"""
remove dead refs to non-existant class RegionTracker
""",
u"""
refactor Assembler.cpp ; passing acceptance on mac
""",
u"""
fix linux compile errors
""",
u"""
fixes to enable ARM nanojit to build, at least
""",
u"""
- NaN is a boolish false. Also constant fold booleans next to operator NOT. r=brendan
""",
u"""
Taking change from tamarin-redux needed to allow LIR forward branches
""",
u"""
: residual typo-fix on previous Math.max fix that went in with 457786
""",
u"""
- TM: Allow CALLINFO macros to specify linkage. r=brendan.
""",
u"""
- Always reload pn1 since it is null if we found the end of the list. r=brendan
""",
u"""
Final patch (I pray) for 460116 (r=jorendorff).
""",
u"""
Back out material change for .
""",
u"""
- buggy inCond propagation in js_FoldConstants (r=jorendorff).
""",
u"""
- Trace JSOP_POPV. r=brendan.
""",
u"""
Followup to patch for to use JS_HAS_GENERATOR_EXPRS #if'ing.
""",
u"""
- Crash [@ js_FoldConstants] (r=jorendorff).
""",
u"""
Fix build breakage from change ee94be502791 (C++ error: jump across initialization)
""",
u"""
Fix typo.
""",
u"""
- Incorrect decompilation (missing parens) with genexp in for-loop-condition (r=jorendorff).
""",
u"""
Fix the build breakage caused by the build breakage fix in d1e6c29797a9. No bug.
""",
u"""
Fix build breakage caused by trivial type mismatch in 3b894cc33338.  No bug.
""",
u"""
Allow a single level of self-calling until we have support for recursion (459775, r=brendan).
""",
u"""
Trace Number.toString(base), not just Number.toString() (459772, r=brendan).
""",
u"""
Add a builtin for RegExp.test (459766, r=mrbkap).
""",
u"""
- Makefile.ref: js{builtins,interp}.cpp are compiled without -MMD. r=mrbkap.
""",
u"""
Add back t/crypto-sha1.js, which magically disappeared at the hands of the nanojit2 patch.
""",
u"""
Merge tamarin-redux (nanojit2) into tracemonkey (457786, r=edwsmith,gal,danderson).
""",
u"""
Fix number of expected traces for testNestedExitStackOuter in trace-tests.js
""",
u"""
Back out patch for 
""",
u"""
- Clear Function and Object (and any other properties) off of the outer object so that Function always refers to the inner window's function. This ensures that the implict Function and explicit window.Function forms refer to the same object. r+sr=brendan
""",
u"""
: Rename fd_copysign to js_copysign. r=jorendorff
""",
u"""
: Drop fd_ prefix from math functions. r=jorendorff
""",
u"""
: Remove references to JS_USE_FDLIBM_MATH from js/src/jsmath.cpp. r=jorendorff
""",
u"""
- Reparameterize GetNewOrUsed and move some work around. r+sr=brendan
""",
u"""
- Check to see if we're UniversalXPConnect-enabled to allow privileged web pages to unwrap XOWs. r+sr=bzbarsky
""",
u"""
Fix for (Remove nsIDOMCustomEvent.idl). r=smaug, sr=sicking.
""",
u"""
Fix for (Remove unused quickstubs). r=jorendorff.
""",
u"""
Fix for (Dependency problem when removing an interface from dom_quickstubs.qsconf). r=ted.
""",
u"""
- Sisyphus - add fennec support
""",
u"""
Backed out changeset 4bc3dc1f6e11
""",
u"""
Backed out changeset bd2860edc1d8
""",
u"""
Try to force rebuild of dom_quickstubs.depends to fix build bustage
""",
u"""
Fix for (Remove nsIDOMCustomEvent.idl). r=smaug, sr=sicking.
""",
u"""
JavaScript Tests - tests for , , , , , , , , with updates for public failures and spidermonkey-n-1.9.1.tests
""",
u"""
- Sisyphus - JavaScript Tests - fix bisect.sh directory munging on windows
""",
u"""
JavaScript Tests - regression tests for , , , , , , , , , , , , , , , , , , , , , , , with updates for js1_8_1/trace/trace-test.js, public-failures.txt, spidermonkey-n-1.9.1.tests, universe.data
""",
u"""
. Implement toJSON for primitive wrapper classes. r=crowder
""",
u"""
. Sites not loading - redeclaration const JSON error on console. r=brendan
""",
u"""
Backed out changeset 82af7163534f
""",
u"""
-- Time offset and zone code are set wrong for some locales, r=mrbkap
""",
u"""
-- XML namespace escaping improvement, r=igor
""",
u"""
- Implementing nsIThreadJSContextStack in nsXPConnect. r+sr=mrbkap
""",
u"""
- Protect against the weird Sandbox global object case when creating XPCNativeWrappers. r+sr=bzbarsky
""",
u"""
- Don't potentially run code with an exception still on cx. r+sr=jst
""",
u"""
- Restore long-standing mozilla change to return a non-empty string for the no_digits case. r=crowder
""",
u"""
Return innermost guard from js_ExecuteTree and not outermost (r=gal).
""",
u"""
TM: Remove unreachable "return false" in TraceRecorder::record_JSOP_NOT. No bug, r=gal.
""",
u"""
Merge mozilla-central -> tracemonkey
""",
u"""
- Reunite record_JSOP_{NEW,CALL}. r=gal.
""",
u"""
Use a single instance of the shell to run the quick benchmark.
""",
u"""
Properly recover from a nested side exit with more than a single level of nesting (459539, r=danderson).
""",
u"""
Merge.
""",
u"""
Stack water level is off by +1 in getTop, and JSOP_CALLPROP premature updates the tracker (459537, r=danderson).
""",
u"""
Fixing docs a bit
""",
u"""
Adding some documentation
""",
u"""
- TM: move soft float builtins next to SoftFloatFilter. r=andreas.
""",
u"""
Merge.
""",
u"""
Don't carry around oldpc in AbortRecording path (459321, r=danderson).
""",
u"""
. Native JSON. r/sr=shaver
""",
u"""
- Rename JSTN_{CATCH,FINALLY,ITER} to JSTRY_*. r=brendan.
""",
u"""
Use standard anti-dangling-else/macro-call-expression-statement macrology.
""",
u"""
Fix dangling else blunder (459186, caught by Jesse's fuzzer).
""",
u"""
Merge.
""",
u"""
Support thin loops (iteration < 2) by closing the loop even if we are on the last iteration (456431, r=danderson).
""",
u"""
Blacklist loop if its unstable and we don't recompile it (459174, r=gal).
""",
u"""
js1_8/genexps/regress-380237-0[34].js fail, regression from introduction of JSOP_RESUME (458356, r=gal).
""",
u"""
- Move for-var-in and for-let-in hoisting from the emitter to the parser (r=mrbkap).
""",
u"""
In ifop, avoid eq0(eq0(x)), instead flip guard direction and use single eq0 (459164, r=danderson).
""",
u"""
Evaluate cond to true if value evaluates to true in non-fused if (459159, r=danderson).
""",
u"""
Non-fused ifs emit different comparison code than the interpreter uses (459151, r=danderson).
""",
u"""
- TM: Number.toString traceable native is broken (r=gal)
""",
u"""
- Improve internal API for traceable natives (r=brendan, nanojit r=edwsmith)
""",
u"""
Adding a few more comments
""",
u"""
Add missing comparison before letting the result of the conditional move flow into the guard for ordered boolean comparisons (457778, r=danderson).
""",
u"""
Trace push and pop for dense and sparse arrays (453734, r=brendan).
""",
u"""
- regexp-dna.js and generality want JSOP_GETELEM(dense array, "0") (r=mrbkap/gal).
""",
u"""
- TM: "Assertion failure: !cx->throwing" with getter that throws (r=mrbkap).
""",
u"""
.  Trace |new Date()|.  r=brendan
""",
u"""
Merge.
""",
u"""
Fixed NaN handling again after backout of busted patch (, r=gal).
""",
u"""
Add support for writing back a boxed value when side-exiting on JSOP_RESUME (453734, r=brendan).
""",
u"""
Backed out changeset 2176f46b2702 (trying to identify cause for tinderbox burning).
""",
u"""
Fixed incorrect handling of NaN in ifop causing one new branch per iteration (, r=gal).
""",
u"""
- expression-ordering fix for traced Math.max(0,-0), r=mrbkap
""",
u"""
Adding mandelbrot to trace-test
""",
u"""
- TM: Trace JSOP_SETLOCALPOP (r=mrbkap).
""",
u"""
Fixed random test failures on AMD64, booleans were being loaded as 64-bit values.
""",
u"""
Fixed more confusion of quads/numbers while emitting LIR (, r=danderson).
""",
u"""
Fixed regression where cmov was disabled on AMD64.
""",
u"""
- ecma_3/Operators/11.4.1-002.js fail; r=brendan
""",
u"""
. JSON should use internal JS functions where it makes sense. r=brendan
""",
u"""
- Consolidate code for retrieving top of the JSON parser's object stack. r=brendan
""",
u"""
Bustage fix.
""",
u"""
- "XPConnect insists on using its own error reporter even when another is already set." r+sr=jst.
""",
u"""
JavaScript Tests for , , , , , , , , , , , , , , , , , , , , , with updates to public failures, spidermonkey-n-1.9.1.tests and js1_8_1/trace/trace-test.js, and update for sisyphus configuration files.
""",
u"""
-  Storing XPCContext inside JSContext
""",
u"""
- Remove PR_STATIC_CALLBACK and PR_CALLBACK(_DECL) from the tree; r+sr=brendan
""",
u"""
- r=crowder
""",
u"""
- JavaScript Tests - update public failures
""",
u"""
- JavaScript Tests - add cvs support to bisect.sh
""",
u"""
- JavaScript Tests - do not exclude timeouts and crashes from post processing
""",
u"""
- JavaScript Tests - update js1_8_1/trace/trace-test.js
""",
u"""
- js_DumpObject can't handle objects that share proto's scope (r=crowder)
""",
u"""
- Delete unused GCC_OPT_BUG makefile variable (r=mrbkap)
""",
u"""
- window.document should not have a quick stub (r+sr=jst)
""",
u"""
- Windows CE Cleanup. r/sr=stuart+bsmedberg
""",
u"""
- json.cpp misuses rooting api. r=mrbkap
""",
u"""
Fix typo in filename.
""",
u"""
. this.JSON is enumerable. r+sr=mrbkap
""",
u"""
. JSON space patrol. r=gal
""",
u"""
No bug - Drop the request before the ResumeRequest hiding under Pop to avoid deadlocks. r=bent sr=sicking
""",
u"""
JavaScript Tests - fix typos, 
""",
u"""
JavaScript Tests - update public-failures, 
""",
u"""
JavaScript Tests - support jstest keyword bookmark, 
""",
u"""
Sisyphus - JavaScript Tests - bisect.sh should use numeric comparison on local revs, 
""",
u"""
. Native JSON. r/sr=shaver
""",
u"""
Branch merge for backout.
""",
u"""
Back out Robert Sayre's patch from due to test failures (changeset 2fe3cb0c9f7c).
""",
u"""
- DOM binding for native JSON. r+sr=shaver
""",
u"""
In the decompiler, skip over JSOP_RESUME after JSOP_NEW/CALL/EVAL/SETCALL (457824, r=brendan).
""",
u"""
For GETELEM/SETELEM we must check that its a native object first before trying to compare the objects shape to the shape of the global object to ensure its not aliasing the global object (457979, r=shaver).
""",
u"""
TM: move cmov_available setting into nj arch backends where appropriate
""",
u"""
Merge.
""",
u"""
Don't trace a property access with a watchpoint (455413, r=brendan)
""",
u"""
Merge.
""",
u"""
Fix guarding in case of sparse array setelem (regression from 457580, r=danderson).
""",
u"""
Fixed cmp number check logic for 64-bit environments (, r=gal).
""",
u"""
Don't trace empty for-in loops (457335, r=brendan).
""",
u"""
Update XDR version number after bytecode change (457789, r=brendan).
""",
u"""
Follow-up work for 457789, emit JSOP_RESUME after JSOP_NEW as well (r=brendan).
""",
u"""
Fixed global object ownership change not aborting recording (, r=gal).
""",
u"""
Fixed crash when charCodeAt failed (with NaN) while recording (, r=gal).
""",
u"""
Always use JSBool (not bool sometimes, JSBool others) as JSVAL_IS_BOOLEAN's native slot type.
""",
u"""
Add a resume point (JSOP_RESUME) immediately following JSOP_CALL (457789, r=mrbkap).
""",
u"""
Catch negative indexes at recording time. At runtime the builtins already check for us. Also guard for shape and setters/getters for non-dense integer index setelem case (57580, r=mrbkap).
""",
u"""
Add test case for 457456.
""",
u"""
Fix constant folding for cmov and add folding of or/and/xor (457456, r=danderson).
""",
u"""
Properly handle cmov and sse2 flags, and put them in a central place not into each platform-dependant assembler (457355, r=danderson).
""",
u"""
Merge.
""",
u"""
Can't use JSVAL_IS_BOOLEAN on trace since boolean type contains undefined (457351, r=brendan).
""",
u"""
Fixed a bug where no shape guard was emitted if a property was not found, causing it to remain unseen if added later.  Abort in this case instead.  (, r=brendan)
""",
u"""
Cleanup SETELEM, box early (in case we side exit on that) and don't set return value if INITELEM or followed by POP (457336, r=brendan).
""",
u"""
Merge.
""",
u"""
When replenishing the recovery double pool, detect if a GC happens (follow up work for 456826, r=gal).
""",
u"""
part 2.  Trace Date.now. r=gal
""",
u"""
.  Flush the fragment cache earlier on global shape mismatch.  r=gal
""",
u"""
part 1.  Get rid of icky JS_LL macros, r=brendan
""",
u"""
Use a pre-allocated pool of doubles to make sure we can safely recover in case of OOM or out of doubles (456826, r=brendan).
""",
u"""
- TM: regexp lastIndex property not traced correctly (r=danderson).
""",
u"""
Workaround for intermittent js_GetClassObject failures (, r=brendan).
""",
u"""
- TM: Crash on digg.com with adblock plus [@ ReconstructPCStack] (r=danderson).
""",
u"""
- TM: Crash on digg.com with adblock plus [@ ReconstructPCStack] (r=gal).
""",
u"""
Added test case for .
""",
u"""
Fixed argc < nargs miscount in js_SynthesizeFrame and adjusted a related assertion (, r=danderson).
""",
u"""
Merge.
""",
u"""
Rewrite and cleanup GETELEM and SETELEM (455748, r=brendan).
""",
u"""
Back off premature arguments tracing (453730 temporary measure).
""",
u"""
Backed out changeset c5d4e22e54ad (reopened 456201).
""",
u"""
Merge.
""",
u"""
Demote modulo operations to integer if both args are int (456934, r=brendan).
""",
u"""
- TM: GVAR op record methods use wrong object (r=gal).
""",
u"""
- TM: Don't assert that global object can't grow additional properties if none are used by any trace and we don't check for global shape mismatches (r=gal).
""",
u"""
Merge.
""",
u"""
Make sure JSOP_DEFLOCALFUN pushes the right function object (456470, r=brendan).
""",
u"""
Backing out patch for to try to fix test bustage
""",
u"""
JavaScript Tests - - update public failures
""",
u"""
- Innerize earlier so we don't rely on the JS engine providing getters that might not be there. r=brendan sr=jst
""",
u"""
- Set global flags on global objects' first use so the JS engine doesn't get confused. r+sr=jst
""",
u"""
- The eval frame might not be the top frame, but we still must find it. r=brendan
""",
u"""
JavaScript Tests - regression test by Mathieu Fenniak
""",
u"""
JavaScript Tests - regression test, by Michael Roovers
""",
u"""
JavaScript Tests - - regression tests for , by Gary Kwong
""",
u"""
- Dead variable pval in js_NativeSet (r=brendan)
""",
u"""
- js_DumpObject debugging function (r=crowder)
""",
u"""
- JS_SetProperty() ends up resolving w/o JSRESOLVE_ASSIGNING (r=brendan, sr=bzbarsky)
""",
u"""
- scalable thread-local GC free lists
""",
u"""
- fixing JSOP_TABLESWITCH to treat -0 as 0
""",
u"""
Sisyphus - JavaScript Tests - , add bisection script
""",
u"""
JavaScript Tests - - update public failures
""",
u"""
Backed out changeset 5986b4269d9d
""",
u"""
- "Implement XHR ('minus X') for worker threads". r+sr=jst.
""",
u"""
Fix warning.
""",
u"""
Merge pull from mozilla-central.
""",
u"""
Compile jsregexp.cpp with -O9 and -fomit-frame-pointer (456201, r=shaver).
""",
u"""
Only fasttrack applys where the arguments array has the same lengths as the expected arguments of the called function (456494, r=brendan).
""",
u"""
Merge.
""",
u"""
The meaning of T changed in our builtin table to object-only, so we have to mark the string builtins now with S, instead of T (454682, r=brendan).
""",
u"""
- TM: js_SynthesizeFrame must js_GetCallObject if JSFUN_HEAVYWEIGHT (r=mrbkap).
""",
u"""
- TM: Going to NEW Facebook profile page causes crash. [ @FlushNativeStackFrame] (r=danderson,mrbkap).
""",
u"""
Back out attempt to invoke natives that return a boxed value (namely push and pop, 453734).
""",
u"""
Fixed breaks in switch statements causing premature end-of-traces (, r=gal,brendan).
""",
u"""
Make nanojit build non-debug with VC7.1 (, r=danderson).
""",
u"""
- Mochitest Assertion failure: vp + 2 + argc <= (jsval *) cx->stackPool.current->avail, at jsinterp.cpp:1066 (r=igor/mrbkap).
""",
u"""
Fixed jstracer's operator delete leaking out into other shared libraries (, r=gal).
""",
u"""
Merge.
""",
u"""
Add builtin for invocation of match() on String objects (454682, r=danderson).
""",
u"""
Fix where recording could crash if globalObj->dslots got reallocated (, , r=gal).
""",
u"""
Don't demote dmod to imod since there is no case that is guaranteed to produce valid integer results for all inputs (456540, r=danderson).
""",
u"""
Use JS_snprintf instead of snprintf which Windows doesn't seem to know about (fix build breakage).
""",
u"""
- Mochitest Assertion failure: vp + 2 + argc <= (jsval *) cx->stackPool.current->avail, at jsinterp.cpp:1066 (r=igor/mrbkap).
""",
u"""
JavaScript Tests - regression tests for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Dave Reed
""",
u"""
- JS Tracer uses file-system stat structure name - WinCE compile fails. patch by dougt, r=crowder
""",
u"""
- WinCE JS DLL does not need DllMain() function. patch by wolfe, r=crowder
""",
u"""
JavaScript Tests - exclude js1_5/extensions/regress-434837-01.js for 1.9.1, 
""",
u"""
JS_snprintf for portability, not snprintf (bustage fix).
""",
u"""
Don't emit constant guards for switch and ifop (455605, r=danderson).
""",
u"""
Both sides of a modulo have to be demotable before we can optimize using imod (456477, r=danderson).
""",
u"""
.  Checking of JIT stats should not loop.  r=brendan
""",
u"""
Compilation fixes for DISABLE_JIT=1 (r=danderson).
""",
u"""
Fixed jstracer.cpp no longer building in the browser because of -pedantic.
""",
u"""
Merge with mozilla-central.
""",
u"""
Adding missing file
""",
u"""
Backed out changeset c0364f5e0a84
""",
u"""
Adding missing file
""",
u"""
Fix (r=me).
""",
u"""
Add a JIT stats object in the shell
""",
u"""
Adding test for 
""",
u"""
Properly calculate tree exit/call guards (, r=danderson).
""",
u"""
Dynamic reconstruction of arbitrary native frames (454402, r=danderson).
""",
u"""
Adding some comments
""",
u"""
Backed out changeset 5e4ec981e9ea
""",
u"""
Adding some documentation
""",
u"""
Allow tree to grow around unbox operations when the type of the value changes (452514, r=danderson).
""",
u"""
Add support for fast native that return jsval and wire up push/pop (453734, r=mrbkap).
""",
u"""
Merge.
""",
u"""
Add support for JSOP_NOT on strings (451787, r=danderson).
""",
u"""
Fixed trying to record arguments past the formal arg count in JSOP_ARGSUB and JSOP_CALL (, r=gal).
""",
u"""
Fixed -0 being treated as a promotable unsigned integer (, r=gal).
""",
u"""
Properly handle side exits in scripted constructors (originally mrbkap, r=brendan, 453462).
""",
u"""
Cleanup and unify comparison code (455811, r=danderson).
""",
u"""
- TM: "Assertion failure: !TRACE_RECORDER(cx) ^ (jumpTable == recordingJumpTable)" with gc getter (r=mrbkap).
""",
u"""
[mq]: bug455408
""",
u"""
Use Object as prototype if the prototype of the constructor is primitive (452960, r=mrbkap).
""",
u"""
Expose push pop in jsarray and add builtins (453734, r=mrbkap).
""",
u"""
Don't export operator new/delete except if really needed (452721, r=danderson).
""",
u"""
Merge.
""",
u"""
Removed bogus assert (argv is NULL if callee is NULL, assert segfaults, 452495, r=danderson).
""",
u"""
Fixed pointer arithmetic bug during trace recording on 64-bit platforms (, r=m_kato).
""",
u"""
Add test case for 455408.
""",
u"""
Don't forget to set RHS as result in SETPROP in case we don't call either SetPropHit or SetPropMiss, new patch (455408, r=gal).
""",
u"""
Backed out changeset 66a76c8c7346
""",
u"""
Don't forget to set RHS as result in SETPROP in case we don't call either SetPropHit or SetPropMiss (455408, r=gal).
""",
u"""
Detect modulo by constant that is not zero and demote to integer modulo (451788, r=brendan).
""",
u"""
Backed out changeset 61b9209c186f
""",
u"""
- "Assertion failure: !cx->onTrace" with yield string (r=gal).
""",
u"""
test_property_cache_direct_slot forgot to insist on a direct slot for get ops (453249, r=gal).
""",
u"""
Merge.
""",
u"""
Backed out changeset 87fe68f51647
""",
u"""
Fix JSOP_NOT (455380, r=brendan).
""",
u"""
Add check to make sure remains fixed.
""",
u"""
Demote modulo operation with a constant non-zero right hand side (451788).
""",
u"""
Implement comparison of numbers against null (455293, r=brendan,danderson).
""",
u"""
Whitespace nit-pick (453261, r=brendan).
""",
u"""
Merge.
""",
u"""
Properly handle floating point array indexes (453261, r=brendan).
""",
u"""
b=454530; misc trace abort fixes (trace String.concat); r=brendan
""",
u"""
Trace slow array get/set of indexed props (453261, r=brendan).
""",
u"""
TraceRecorder::record_SetPropMiss mis-layered on top of record_SetPropHit (454689, r=mrbkap).
""",
u"""
bustage on Solaris
""",
u"""
- TM: assertion when running unit tests with the JIT on (r=danderson).
""",
u"""
- TM: "Assertion failure: PCVAL_IS_SPROP(entry->vword)" with getter.
""",
u"""
Get rid of bogus nanojit arm platform stats line
""",
u"""
Merge backout of the old patch for - we can statically allocate Oracle again, now that we're linking using the C++ linker magic, r=crowder
""",
u"""
Merge backouts of - using g++ to link libjs.so means we can have static classes
""",
u"""
Backed out changeset fc4a8cc07c9f - bustage fix from the first patch for which is also being backed out
""",
u"""
Backed out changeset e2614011f194 - - the better solution is to allow static objects and link libjs.so with g++ so that _init and _fini run static constructors/destructors correctly backout r=crowder
""",
u"""
/- link using g++ instead of ld, so that static constructors/destructors will fire correctly r=crowder
""",
u"""
Work around incorrect but annoying strict-aliasing warning. r=brendan
""",
u"""
JavaScript Tests - update intel specific failures, 
""",
u"""
JavaScript Tests - correct mistaken push of incomplete universe.data, 
""",
u"""
JavaScript Tests - regression test for , by Boris Zbarsky
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Gary Kwong
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Martijn Wargers, Brendan Eich
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
JavaScript Tests - gczeal should be guarded, 
""",
u"""
JavaScript Tests - update public failures, 
""",
u"""
JavaScript Tests - GLOBAL should be computed in shell tests, 
""",
u"""
Sisyphus|JavaScript Tests - uniq truncates lines at 8190 chars, 
""",
u"""
JavaScript Tests - update known failures for js1_5/extensions/regress-452178.js, js1_5/extensions/regress-452329.js - 
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - move js18 test to proper suite, 
""",
u"""
JavaScript Tests - move js18 test to proper suite, 
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Makoto Kato
""",
u"""
JavaScript Tests - regression test for , by Rob Sayre
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - enable jit fixes, 
""",
u"""
JavaScript Tests - known failures update, 
""",
u"""
- Assertion failure: obj == pobj, at src/js/src/jsinterp.cpp:160 (r+sr=mrbkap)
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
- NodeIterator doesn't forward exception properly; r=(jonas + jst) sr=jst
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
- Don't unconditionally add inner and outer object hooks to XPConnect objects.
""",
u"""
- Quick stubs: handle members with the same name (r+sr=jst)
""",
u"""
Add crashtest
""",
u"""
- Reuse regexp arena, original patch by Robin Bate Boerop <moz@shorestreet.com>, refreshed by Ryan VanderMuelen <ryanvm@gmail.com>, r=crowder
""",
u"""
- please spell formater formatter; mozilla-central part; r=timeless
""",
u"""
TraceRecorder::record_SetPropMiss mis-layered on top of record_SetPropHit (454689, r=mrbkap).
""",
u"""
bustage on Solaris
""",
u"""
- TM: assertion when running unit tests with the JIT on (r=danderson).
""",
u"""
- TM: "Assertion failure: PCVAL_IS_SPROP(entry->vword)" with getter.
""",
u"""
Get rid of bogus nanojit arm platform stats line
""",
u"""
Fix bustage -- these macros are only defined if the tracer was enabled.
""",
u"""
Merge tracemonkey -> mozilla-central
""",
u"""
- TM: don't abort TraceRecorder::record_JSOP_SETPROP on cache miss (r=mrbkap).
""",
u"""
Back out patch for .
""",
u"""
- TM: don't abort TraceRecorder::record_JSOP_SETPROP on cache miss (r=mrbkap).
""",
u"""
- TM: eliminate silly map_is_native guards on globalObj (r=shaver).
""",
u"""
Fixed Linux build, extra qualification on member function.
""",
u"""
Fix build bustage: parent or proto might be not JSObject* when setting to null. r=brendan, patch by bz.
""",
u"""
Avoid needless prototype-shape purges (454035, r=igor).
""",
u"""
Merge.
""",
u"""
Capture the typemap of the outgoing stack frame during a function call and store a pointer to it on the native call stack.
""",
u"""
Extract the snapshot code for a single slot into determineSlotType() und use that method in snapshot().
""",
u"""
Trace Math.max. r=brendan
""",
u"""
Add date tests to correctness checks
""",
u"""
Add controlflow-recursive to correctness checks
""",
u"""
Add some basic correctness tests for benchmarks
""",
u"""
Fix - js_FillPropertyCache uses the wrong scope's shape sometimes (r=mrbkap).
""",
u"""
Don't try to record recursion until we support it properly (454277).
""",
u"""
Removing shark think which landed by accident
""",
u"""
.  Make sure to properly restore the thisp for the innermost frame when taking a nested side exit with a callDepth > 0.  r=brendan,gal
""",
u"""
Make return at callDepth 0 terminate the loop, like break (454027, r=gal).
""",
u"""
- TM: JSOP_NOT needs isPromoteInt/::demote help.
""",
u"""
Trace through parseInt(double), r=gal+brendan.
""",
u"""
Enable tracemonkey/nanojit for ARM.
""",
u"""
Easy fixes to avoid aborting on V8/raytrace.js: MAX_CALLDEPTH doubled to 10; JSOP_NOT handles int and undefined.
""",
u"""
Merge.
""",
u"""
Checkpoint arguments tour-de-force (453730).
""",
u"""
Use js_NaN global that we exported from jsnum.cpp, instead of cx->runtime->jsNaN.
""",
u"""
[arm] Use preindexed STR instruction instead of separate STR and SUB in asm_pusharg
""",
u"""
[arm] Have asm_quad copy direct from const to destination, if there's no register allocated for the const -- don't load into fp reg just to store it.
""",
u"""
[arm] use arm_ADDi and let it take care of LD32 if necessary.
""",
u"""
[arm] Don't load arg into a register in asm_pusharg if it's not in one already.
""",
u"""
[arm] Don't use STMIA + ADD to move a fp call result into memory; use two STRs.  Also use Scratch + tmp reg for asm_mmq, instead of just tmp.
""",
u"""
[arm] speed up store64 with constant value; also use xor for imm0 loads into a gp reg
""",
u"""
[arm] make asm_quad stick its constants into the instruction stream, with a branch over, to ensure that the data is close enough for a PC-relative FLDD
""",
u"""
[arm] Make ADDi into a function, since it's doing a lot of work
""",
u"""
Make TraceMonkey build on Solaris x86 with Sun Studio 12 (, r=danderson).
""",
u"""
Fixed a verbosity mode memory leak in LirNameMap::addName (, r=sayrer).
""",
u"""
Added new macro AVMPLUS_UNIX to reduce redundancy and add Solaris support to the TM browser build (, r=dvander).
""",
u"""
Trace through Math.log as a known native (, r=brendan).
""",
u"""
Abort tracing if a callee encounters a primitive |this| and doesn't support it (, r=brendan).
""",
u"""
- Replace any holes on the stack with undefined. r=gal
""",
u"""
Another fix for the patch to -- when ignoring switch guards, don't update the tracker stack.
""",
u"""
Merge.
""",
u"""
Better fix for (changeset badf4c84665f regressed) - don't emit guards rather than bailing out of comparisons (r=gal).
""",
u"""
Fixed verbose printing typo on AMD64.
""",
u"""
Make sure 32-bit loads into 64-bit registers are sign-extended.
""",
u"""
- Avoid overuse of the fun_getProperty class getter to optimize getting and setting random properties on functions. r=mrbkap
""",
u"""
House style bracing for multiline then clause.
""",
u"""
Merge again.
""",
u"""
Don't guard on constant decisions, which will always have the same path (, r=gal).
""",
u"""
Re-enabled the shell JIT as trace-tests and SunSpider pass again.
""",
u"""
Improved AMD64 allocation for float ops that get stored back into memory.
""",
u"""
Fixed float ops to deal with being handed an LHS GPR reservation on AMD64.
""",
u"""
Disabled building AMD64 JIT in shell until regressions are tracked down.  Fixed some compiling errors while I'm poking around here ().
""",
u"""
Fixed nanojit not building on VC 7.1 (, r=dvander).
""",
u"""
[OS/2] : Build break in jstracer.cpp (r=gal)
""",
u"""
Fix build bustage: parent or proto might be not JSObject* when setting to null.  r=brendan
""",
u"""
Avoid needless prototype-shape purges (454035, r=igor).
""",
u"""
- get rid of --disable-mochitest, replace MOZ_MOCHITEST with ENABLE_TESTS. r=bsmedberg
""",
u"""
Fix - js_FillPropertyCache uses the wrong scope's shape sometimes (r=mrbkap).
""",
u"""
Properly initialized mSaveDepth in JSAutoSuspendRequest, r=sayrer.
""",
u"""
: Correct prbool misuse in spidermonkey
""",
u"""
- Only look at pn_extra if we're actually a list. r=brendan
""",
u"""
Fix for (Name more CC edges). r/sr=jst.
""",
u"""
: fix prbool bugs in xpconnect. r=jorendorff
""",
u"""
: Replace "must flow through label" comments with statically-checkable macro. r=igor
""",
u"""
- merging JSOP_DEFUN and JSOP_CLOSURE. r=brendan
""",
u"""
- editline.c:1038: warning: implicit declaration of function getpid. r=mrbkap
""",
u"""
- fixing build problem with 64-bit debug builds.
""",
u"""
- eliminating compiler pseudo-frames. r=brendan
""",
u"""
use -xldscope for Sun Studio on Solaris r=vladimir,benjamin sr=benjamin
""",
u"""
Patch from Mike Kaplinskiy <mike.kaplinskiy@gmail.com> implementing trim, trimLeft, and trimRight (305064, r=me).
""",
u"""
- Remove JS_STATIC_DLL_CALLBACK and JS_DLL_CALLBACK from the tree; "dom_quickstubs.cpp" bustage fix
""",
u"""
- Remove JS_STATIC_DLL_CALLBACK and JS_DLL_CALLBACK from the tree; r=(benjamin + bent.mozilla)
""",
u"""
- Remove MOZ_DECL_CTOR_COUNTER; <mozilla-central> part; r=benjamin
""",
u"""
- "Update caps, dom, xpconnect for (checkObjectAccess moving to the JSContext)". r+sr=jst.
""",
u"""
- " Allow runtime's security callbacks to be overridden by a context". r=brendan.
""",
u"""
Merge more work by Jim Blandy on .
""",
u"""
: Give jsconfig.h a better name, and make room for the new js-config.h. r=bsmedberg
""",
u"""
- /s /S /w /W in character classes perform very poorly. r=crowder (showed up as Dromaeo test "DOM MOdification (Prototype): update()"
""",
u"""
Sisyphus - JavaScript Tests - add jit options for browser tests, 
""",
u"""
JavaScript Tests - escape timezone in patterns in known-failures.pl, 
""",
u"""
JavaScript Tests - known failures update, 
""",
u"""
JavaScript Tests - known failures update, 
""",
u"""
- Avoid overuse of the fun_getProperty class getter to optimize getting and setting random properties on functions. r=mrbkap
""",
u"""
: js/src/Makefile.in lists host_jsoplengen twice in HOST_SIMPLE_PROGRAMS r=mrbkap
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Fixed JSOP_NEG with 0 being tracked as a promotable int, and added an equals-zero guard for the same opcode (, r=gal).
""",
                                                                                        u"""
Missing guard for CallGetter builtin (453580, r=gal).
""",
                        u"""
Handle an interpreted constructor returning an object. r=brendan
""",
                                u"""
Merge.
""",
u"""
Removed a bogus assert. Inner loops can exit on a goto in case we hit a break (453051).
""",
                                                        u"""
Put the trace-recording/executing flag in the trace monitor to handle many contexts per thread (451666, r=gal).
""",
                                                                                u"""
Limit tree growth to 16 traces per tree to avoid code explosion due to tail duplication (452869, r=danderson).
""",
                                                                                u"""
Add V8 benchmark suite.
""",
u"""
Fix JS_THREADSAFE build, pick extern nit.
""",
            u"""
Fix up some ifdefs and debug printfs
""",
    u"""
Add VFP for floating point ops to nanojit ARM backend.
""",
                        u"""
Indentation sanity fixes; no code changes.
""",
u"""
Split NativeThumb.cpp into NativeThumb.cpp and NativeARM.cpp; no code changes.
""",
u"""
b=449526, TM: fix up ARM code generation / softfloat
""",
u"""
Teach js_IsLoopExit about JSOP_AND, JSOP_OR, etc. and separate extended jump cases so they can get the extended offsets.
""",
u"""
Remove outdated comment. r=gal
""",
u"""
Allocate the oracle dynamically instead of making it a global object to avoid atexit C compatibility issues (453388, r=danderson).
""",
u"""
Missing guard for CallGetter builtin (453580, r=gal).
""",
u"""
- XPConnect creates doubles without checking for the INT_FITS_IN_JSVAL case (r=jst,sr=brendan)
""",
u"""
- Confusing comment, bogus indentation in jsobj.cpp (r=mrbkap)
""",
u"""
-  Error: setting a property that has only a getter on cars.com (r+sr=bzbarsky)
""",
u"""
: Some files didn't get compiled with -fno-exceptions. r=shaver
""",
u"""
- Allow stack checking to be suppressed per-function, r=dmandelin sr=jst
""",
u"""
: avoid hidden return in CHECK_AND_SET_JUMP_OFFSET. r=igor
""",
u"""
Fix bool FASTCALL vs. Nanojit calling convention bug, also some non-bool whoppers caught in the process (453361, r=mrbkap).
""",
u"""
Fix warning pulled over from m-c (mrbkap will track down).
""",
u"""
Merge with mozilla-central.
""",
u"""
Don't flush anything if we're not even enabled. r=gal
""",
u"""
Fixed accidental debugging change I pushed with changeset de2d26b3c902.
""",
u"""
On x86 compilers without fastcall, simulate it when invoking traces and un-simulate it when invoking builtins (, r=dvander).
""",
u"""
Build fixes for MSVC 7.1 and mingw (, patch from neil@parkwaycc.co.uk).
""",
u"""
Fix for building on FreeBSD (, patch from Jeremy Lea).
""",
u"""
Use mmap() instead of valloc() in nanojit, abort on mprotect() failure (, patch+r from Asko Tontti).
""",
u"""
New attempt at fixing 453235. If building without JIT (like PPC/MacOSX), don't include the deep abort calls in jsinterp.cpp
""",
u"""
Merge.
""",
u"""
Backed out changeset 25f856429db3. Wrong fix. Looks like jstracer.h is not included. We in fact can call methods of TraceRecorder directly. Sigh. I wish we had a try server.
""",
u"""
Merge.
""",
u"""
Introduce js_DeepAbort to be used from jsinterp.cpp, instead of trying to call TraceRecorder->deepAbort directly (453235).
""",
u"""
Holey single-element dense array has null dslots, requires nulld defense (453173).
""",
u"""
Fast followup fix for unintended change to 'f' prefix handling in TraceRecorder::record_JSOP_NEW (452878).
""",
u"""
Kind of an Array initialiser tour-de-force for :
""",
u"""
Add tests containing switch statements
""",
u"""
Add test for more bitwise ops
""",
u"""
- Make js_RecordTree printfs only appear with TRACEMONKEY=verbose.  r=gal
""",
u"""
- Support JSOP_CONDSWITCH's JSOP_CASE and extended-jump-offset JSOP_CASEX variants properly.
""",
u"""
Fix gmail crash by not tracing switches. r=brendan
""",
u"""
Abort (deeply) if we re-enter js_Interpret in the middle of a trace. r=brendan
""",
u"""
Fixed an signed/unsigned comparison warning in an assert in jstracer.cpp.
""",
u"""
Merge.
""",
u"""
Add builtins for toLowerCase, toUpperCase and replace(str,str) (452885, r=mrbkap).
""",
u"""
Don't let GC run when recording.
""",
u"""
- Fix a bad assumption. r=brendan
""",
u"""
- Ensure we intern the id for JSOP_IN. r=brendan
""",
u"""
Merge.
""",
u"""
Fixed double-as-integer check not handling negative zero (, r=gal).
""",
u"""
Track number of breaks we generate loop exits for.
""",
u"""
Long-form conditional branches (IFEQX, IFNEX) are never fused, so don't check for them in fuseIf.
""",
u"""
Merge.
""",
u"""
Track locations of control-flow merges in cfgMerges during recording (452869).
""",
u"""
Fixed assumptions that nanojit's insCall() would not clobber the input argument array (, r=gal).
""",
u"""
Abort recording on invalid string indexes for JSOP_GETELEM (, r=brendan).
""",
u"""
Add tests covering division.
""",
u"""
Add tests for continue statement.
""",
u"""
Fix bogus JOF_VARPROP test; fix uninitialized id in JSOP_IN recorder, should have caught it when I reviewed danderson's patch.
""",
u"""
Fix upvar decompilation for eval-from-fun case (452441, r=igor).
""",
u"""
Consolidate equal and cmp code harder, trace switch ops, use INS_CONST more (bug to be filed -- bugzilla down atm).
""",
u"""
Unroll loops we were not able to call once, but only if we don't have a tree available for that loop header.
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Monitor downward branches only during recording (452709).
""",
u"""
Fixed trying to record JSOP_IN with some unusuable left-hand values (, r=brendan).
""",
u"""
Abort trace if forInLoop values are not stable; currently, not strings ().
""",
u"""
Fixed bogus assertion in test_property_cache (, r=dvander).
""",
u"""
Turn NANO_DIE macro into NanoAssertFail function so that it shows up in stack traces.  Having it appear in stack traces makes it clear the exit was due to an assertion failure rather than a real crash.  Followup to .
""",
u"""
Cleanup detection of gotos that were emitted as a result of a BREAK statement.
""",
u"""
Added descriptive messages to always-taken assertions in Nativei386.cpp.
""",
u"""
Fix NanoAssertMsgf in non-debug builds. Regression from my patch in .
""",
u"""
Merge.
""",
u"""
Notify the monitor of all branches, not just backwards branches.
""",
u"""
Add a message to a NanoAssert(0) to make it possible to match against. r=gal
""",
u"""
: change NanoAssert* macros to make it easier to check for nanojit assertions in automated testing. r=danderson.
""",
u"""
- Abort on the weird case where we find a global name on the prototype of the scope chain. r=brendan
""",
u"""
Merge.
""",
u"""
If the inner tree cannot be adjusted to match the call site of the outer tree because it uses an int where the outer tree uses a double, trash the inner tree, not the outer one. In CallTree, return the innermost guard we return from, not the outermost one. Jump over at most 1 loop edge that doesn't go back to our own header, not an arbitrary amount.
""",
u"""
Abort recording on JSOP_INCPROP with an invalid slot (, r=brendan).
""",
u"""
Merge.
""",
u"""
Better fix for - only track new rval for primitives (r=brendan).
""",
u"""
- Don't push tagged jsvals on the stack. r=brendan
""",
u"""
Merge.
""",
u"""
Track new rval from JSOP_RETURN when constructing inline frames (same as JSOP_STOP).
""",
u"""
- The interpreter's JSOP_VOID doesn't push anything, so we shouldn't expect it to. r=brendan
""",
u"""
Remove extra space in tracing statistics message (). r=gal
""",
u"""
- NanoAssert doesn't end the message with a line break
""",
u"""
Record JSOP_IN (452563, r=gal).
""",
u"""
Fixed asserting on valid LIR in AMD64 LIR_qcmov (, patch from Makoto Kato).
""",
u"""
Merge again
""",
u"""
Merge mozilla-central -> tracemonkey
""",
u"""
Keep unrolling inner loops as long we are not hitting the same inner loop edge twice in a row (452362).
""",
u"""
Merge.
""",
u"""
Fix trashing of inner trees. Keep track of trees that call to a tree and flush them as well since they directly embed the code address. Since flushing an inner tree might invalidate the tree we are currently compiling, trees are now trashed in the destructor of TraceRecorder.
""",
u"""
Removed INS_CONSTPTR use with JSVAL_TAG to discourage future 64-bit problems.  Fixed 32-bit build.
""",
u"""
Fixed AMD64 loop branch patching for >32-bit offstes.
""",
u"""
Merge.
""",
u"""
Added LIR_qior/pior.  Fixed more AMD64 page jumping bugs.  Fixed some other AMD64 usage bugs in jstracer.
""",
u"""
Merge.
""",
u"""
Loops with a single iteration start tracing, but never complete since we immediately walk past the loop edge after the first iteration. At least try to complete the loop around it by walking past such thin inner loops when compiling the outer loop (452362).
""",
u"""
Oops, not enough copying...
""",
u"""
Fix a bug Jesse reported: insufficient copy/paste from record_JSOP_CALL to record_JSOP_NEW.
""",
u"""
Fix upvar decompilation for eval-from-fun case.
""",
u"""
Fix another broken assert (452372).
""",
u"""
Remove bogus assertion (452178).
""",
u"""
Improved AMD64 out-of-range jumping, some cases are still broken though.  Fixed i386 build.
""",
u"""
Fixed crashing with the incremental allocation changes.  Very long jumps are still a problem but at least now we assert.
""",
u"""
Merge.
""",
u"""
Add test case for decaying inner loops that sometimes are not executed at all since the condition fails pre-entry.
""",
u"""
Flag a side exit as loop exit only if the underlying loop condition actually targets the current loop header, otherwise treat it as a branch exit. This is required for inner loops where we unroll the first iteration but the loop condition immediately fails. If we report such exits as loop exits, no branch gets ever attached to them and we keep side-exiting over and over.
""",
u"""
Correct (but sadly a bit slower) property cache guarding (452140, r=shaver).
""",
u"""
Test case for .
""",
u"""
Added knownNative for num_toString (, r=dvander).
""",
u"""
Add some tests for loops that should exit trace.
""",
u"""
For global code assume that no slots are below the current frame.
""",
u"""
Align test order with mozilla-central to avoid merge conflicts (I hope).
""",
u"""
Merge.
""",
u"""
When extending an outer tree from its nesting guard, the guard we actually exited on determines the typemap for the current frame and all inlined frames, whereas the nesting guard is consulted for all type information frames below the current frame.
""",
u"""
Rename lr->anchor in AttemptToExtendTree()
""",
u"""
Determine the tree we have to grow from the side exit we attach to in AttemptToExtendTree() instead of passing the parameter in.
""",
u"""
Fix warning.
""",
u"""
Rename gcDontBlock to runningJittedCode, and assert it's false on entry to js_Interpret (for 451657, but not the fix, just prolog).
""",
u"""
Merge.
""",
u"""
Add an assert checking that celldepth is zero upon loop exit side exits and better verbose diagnostic for trace exits.
""",
u"""
Generate an always taken LOOP_EXIT guard when an inner loop encounters a break statement. When returning from such an inner tree, make sure the recorder resumes at the target address of the goto the break was emitted as, otherwise the outer tree confuses the location with a break in its own loop. Disabled outerlining (this patch subsumes it, but we might enable it later since it might handle some cases more efficiently, currently off for debugging through). fasta currently asserts, and fannkuch hits a perf regression. These are probably bugs this change exposed.
""",
u"""
- Trace == and != involving booleans. r=gal
""",
u"""
- Trace Math.ceil. r=brendan
""",
u"""
Oops, forgot to make Print set *vp to undefined when I made it a FastNative.
""",
u"""
Merge.
""",
u"""
Fixed cases where argc varied between recording time and execution time ().
""",
u"""
Split closeLoop() and compile() and add endLoop(), which omits an always-exit guard (will be used for break statements.)
""",
u"""
Add test of (attempted) trace recording with an active call object
""",
u"""
Annotate gotos that are emitted for break statements with SRC_BREAK (452122, r=mrbkap).
""",
u"""
Cope with sub-optimal JSOP_FORNAME instead of JSOP_FORVAR inside a with, or similar (eval-created locals; 451806).
""",
u"""
Merge.
""",
u"""
Enable outlining. If a loop doesn't connect back to its own header (i.e. break inside the loop), see if the outer loop path can be attached to the inner loop (outerlining). Added test case (failure mode is high number of activated traces in trace-test.js). This test exposes a regression in access-fannkuch. Committing so we can diagnose that separately.
""",
u"""
Remove over-eager gvar optimization for JSOP_DEFFUN (451678, r=shaver).
""",
u"""
Merge.
""",
u"""
Fixed bogus assertion in debug mode.
""",
u"""
Merge.
""",
u"""
If the outer loop has a value in a float register but the inner tree expects an int, tell the oracle that we want doubles in that slot in the inner tree and trash the inner tree so it gets re-compiled with a matching layout (451673).
""",
u"""
: Avoid an invisible return. r=igor
""",
u"""
backing out due to unit test failures
""",
u"""
- "script stack space quota is exhausted" exception in JSON.jsm when calling SessionStore API for sessions with a large amount of data. r=sayrer, sr=brendan
""",
u"""
- uniform handling of bytecodes with variable stack uses. r=mrbkap,brendan
""",
u"""
- removal of the compiler pseud-frames. r=brendan,mrbkap
""",
u"""
[Solaris] Failed to build mozilla-central on solaris in js module. brendan: review+
""",
u"""
Fix orange caused by 
""",
u"""
- optimizing JS date access. r=mrbkap
""",
u"""
Fix for build breakage on Windows due to bad dom_quickstubs.depends file.
""",
u"""
- DOM quick stubs - faster paths for top N DOM methods (r+sr=jst, security r=mrbkap, build r=bsmedberg)
""",
u"""
- Delete SetExceptionWasThrown (r=dbradley, sr=jst)
""",
u"""
- eliminate Namespace and QName GC things. r=brendan
""",
u"""
- fastcall attribute should only be used on i386. r=shaver
""",
u"""
Fix upvar decompilation for eval-from-fun case (452441, r=igor).
""",
u"""
Backed out changeset 9ecf699d4047 to see if it fixes linux mochitest failures
""",
u"""
Fix upvar decompilation for eval-from-fun case (452441, r=igor).
""",
u"""
[OS/2] : fix build break and fastcall warnings in js/src, r=shaver
""",
u"""
Record JSOP_IN (452563, r=gal).
""",
u"""
- Always do LAST_FRAME_CHECKS, even if the compile failed (since that sets a pending exception). r=mrbkap
""",
u"""
Fix upvar decompilation for eval-from-fun case (451884, r=mrbkap).
""",
u"""
- Don't allow shorthand object initializer through destructuring assignment. r=brendan
""",
u"""
- Deal with embeddings that don't use principals. r=brendan
""",
u"""
- Fix latent bug in rv_alloc. r=crowder
""",
u"""
JavaScript Tests - match a[1] ~ a['1'], 
""",
u"""
Place these libraries in EXTRA_LIBS, not LDFLAGS, so we can easily
""",
u"""
There is no 'pathsubst' function in GNU make.  This assignment has
""",
u"""
Fix another broken assert (452372).
""",
u"""
Correct (but sadly a bit slower) property cache guarding (452140, r=shaver).
""",
u"""
Remove bogus assertion (452178).
""",
u"""
Why wasn't this hunk in the .rej file, or else merged properly?
""",
u"""
- knownNative for num_toString (r=danderson).
""",
u"""
Fix TM assert on wikipedia (451806, r=mrbkap).
""",
u"""
Fixed cases where argc varied between recording time and execution time (; also warning fix fe54f7fb89d1 from tracemonkey).
""",
u"""
.  Assert when decrementing the jsdhash/pldhash recursion level past 0.  r=dbaron,brendan, sr=dbaron
""",
u"""
- fixing -Wstrict-aliasing=2 warnings
""",
u"""
- build DumpJSStack in release builds. r=shaver
""",
u"""
- Array.splice() should return an empty array. r=brendan
""",
u"""
Clobbering TraceMonkey shouldn't be needed
""",
u"""
- Regression: Array index has different results (r=shaver).
""",
u"""
Backing out changeset 043ea4ef249c to try to fix failed mochitests on Windows and Linux
""",
u"""
js/src/jslock.cpp failed to compile on Solaris x86 r=igor
""",
u"""
- fixing -Wstrict-aliasing warnings, r=crowder
""",
u"""
- TM: mochi chrome tests fail under TM. xpcshell unit test. r=brendan
""",
u"""
Remove over-eager gvar optimization for JSOP_DEFFUN (451678, r=shaver).
""",
u"""
Allocate nanojit code cache incrementally ().
""",
u"""
- On x86 processors, only use SSE2 if the processor supports it, otherwise default back to x87 FPU (r=gal, sr=mrbkap)
""",
u"""
Fixed x86_64 build issue (accidentally trying to build 32-bit nanojit).
""",
u"""
Fix builtins that were accidentally flagged as CSE/FOLD but really aren't (Math.random i.e.)
""",
u"""
Cleanup spacing in builtins.tbl
""",
u"""
Fixed js_String_p_split passing in an undersized array.
""",
u"""
Fix warning about signed/unsigned comparison.
""",
u"""
, fix string split assertions and return values. Tests fail with JIT on for other reasons, it seems. r=shaver
""",
u"""
Merge.
""",
u"""
Abort recording when an error occurs.
""",
u"""
Fix script->owner maintenance; also fix warning.
""",
u"""
JSThread is not zeroed when allocated, grrr.
""",
u"""
Fix typo.
""",
u"""
Merge.
""",
u"""
Followup upvar fix, easy assertbotch avoidance.
""",
u"""
Add split built-in, also sort knownNatives for my own sanity (should sort builtins.tbl and jsbuiltins.cpp by function while at it, but too tired).
""",
u"""
Remove FastEval builtin.
""",
u"""
Merge, plus restore TraceRecorder::activeCallOrGlobalSlot.
""",
u"""
Upvar, v0.1 (limited to looking up from eval in a function, to the function's args and vars).
""",
u"""
disable tracing with active call object pending perf fix
""",
u"""
Remove FastEval, broken by design (r=brendan).
""",
u"""
Fixed code generation bug in AMD64 port.  Enabled AMD64 JIT now.
""",
u"""
Remove lambda-replace built-in, it's not safe to record into a nested js_Interpret.
""",
u"""
Fix CHECK_RECORDER macro to use XOR to evaluate both terms.
""",
u"""
Convert undefined to NULL on tree entry if the tree wants an object type.
""",
u"""
trace |new Array|, via the magic of copy and paste
""",
u"""
Merge.
""",
u"""
Tidy up globalShape mismatch reporting.
""",
u"""
If we expect a concrete value but see an undefined come into the trace, convert undefined to the concerete value.
""",
u"""
Export js_NaN.
""",
u"""
Use JS_FRIEND_API for new JS_ArrayToJSUint8Buffer, etc., and use it on prototypes and definitions (fixes some platform builds).
""",
u"""
Merge.
""",
u"""
Remove bogus fadd +1 check at the end of the loop. We have long switched over to starting slots as int and hence n++ will be emitted as integer add with i2f, so checking for i2f only is sufficient.
""",
u"""
Increase HOTEXIT to 1 (from 0).
""",
u"""
Eliminate redundant BoxDouble(UnboxDouble) chains.
""",
u"""
say what we're returning from from EnterFrame
""",
u"""
Merge.
""",
u"""
1. Add activeCallOrGlobalSlot, used by JSOP_NAME, JSOP_CALLNAME, etc. recorders to cope with Call objects on the scope chain, if they represent still-active frames covered by callDepth.
""",
u"""
Defer eval'ed script destruction to next GC; expose js_obj_eval for tracing.
""",
u"""
Support multiple returns from called trees by continueing the outer tree with a new nested guard.
""",
u"""
Restore state.sp and state.rp before the nested guard exit point so we can have a sequence of them and still have rp/sp adjusted correctly.
""",
u"""
Push actual guard that failed in a nested call, not the expected.
""",
u"""
Merge.
""",
u"""
Don't emit a guard at the end of CALLNAME and friends since the values CALLNAME puts on the stack (callee, this) are not seen by the interpreter yet, and thus get store killed. Instead, emit the guard in CALL, at which point the values are properly stacked.
""",
u"""
fix js_IsLoopExit to better handle for-in exits, r=mrbkap
""",
u"""
Add a switch to disable the oracle, in which case we never demote any slots.
""",
u"""
Clear the oracle on every GC.
""",
u"""
If at loop entry we expect a double, but at the loop tail we store an int because we suck the i2f into the side exit, we have to explicitly cast back up to double using i2f otherwise we won't be able to make sense of the value when we load it at the top of the next iteration.
""",
u"""
disable vprof building so that we can build on XP
""",
u"""
Add a way to clear the oracle.
""",
u"""
Clear global slots and global type map when clearing the code cache.
""",
u"""
Backed out changeset be63a51a0a3b. Breaks tofte if run from ./time.sh.
""",
u"""
b=451242, add fast-paths for dense array to uint/int/double buffer conversion; r=bent/mrbkap
""",
u"""
Don't disable property caching in eval (this requires GC'ing eval scripts). Do tolerate active Call object at head of scope chain in record_JSOP_CALLNAME, and go straight to the stack slots.
""",
u"""
Stub the getter and setter on class prototypes and constructor (bz, r=brendan, ).
""",
u"""
When adjusting integers to doubles in tree calls start with the current stack frame only.
""",
u"""
Fixed some valgrind whinings (not actual bug fixes).
""",
u"""
wrong condition check in nanojit with qjoin(qlo,qhi)
""",
u"""
Fixed typo that broke the tree.  Sorry!
""",
u"""
default to non-verbose for DEBUG, set TRACEMONKEY=verbose in env to go verbose
""",
u"""
Another portability fix.  math-spectral-norm is crashing in the test harness so keeping 64-bit JIT off (everything else works).
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
More AMD64 fixes (release build works now, and fixed verbosity bug).
""",
u"""
AMD64 trace-tests.js passes now (hacked in LIR_qcmov opcode, corrected builtin return types).
""",
u"""
merge from mozilla-central
""",
u"""
Add str + obj concatenation for 3d-raytrace.js.
""",
u"""
If the outer tree has a slot in an integer register, but the inner tree expects a double, make sure to promote the value before calling the tree, otherwise the inner tree will read the value from the stack incorrectly.
""",
u"""
Correctly calculate tree call stack adjustment, even if we don't have any arguments in the current frame and hand pick some cleanups from the backed-out changeset.
""",
u"""
Back out multi-trees. There is absolutely no way this will be debugged in time for tomorrow. Need a bit more gdb man-power.
""",
u"""
Always blacklist the first fragment in the peer list, and blacklist if we see a loop that is not type-stable.
""",
u"""
Don't build trees inside tree calls if no suitable tree can be found (for now.)
""",
u"""
Improved debug output.
""",
u"""
Add debugging facilities for typemaps and fix sp_adj calculation for tree calls.
""",
u"""
Support multiple fragments with different entry maps per PC location.
""",
u"""
Clear out the list of global slots when the shape changes.
""",
u"""
Emit the tree call stack setup code before executing the inner tree, otherwise we might see stale references to instructions prior to the call that no longer guarantee certain types (since the inner tree overwrite them.)
""",
u"""
Merge.
""",
u"""
Intern globals per-context, not per tree, which allows transitioning between trees that use globals. The type of all global slots compiled code uses is expected to remain stable, otherwise the entire code cache has to be flushed. Changes to the shape of the global object also flush the code cache. Working for trace-tests.js, but fails math-partial-sum.js
""",
u"""
Add a global type map to the monitor and rename slotList to globalSlots.
""",
u"""
Disabled 64-bit JIT for now, failing 3 test cases.
""",
u"""
Merge.
""",
u"""
Fixed codegen bug for amd64 64-bit binary ops.
""",
u"""
Fixed AMD64 accidentally treating the shape as a 64-bit integer.
""",
u"""
Merge.
""",
u"""
Fixed some bugs in the AMD64 port, still crash in 5 sunspider tests.
""",
u"""
Added AMD64 JIT building to the makefile.
""",
u"""
Improved AMD64 nanojit compatibility.
""",
u"""
Fixed compiling on AMD64.
""",
u"""
Back out changeset 1d0574db8320 (for 450997), it was based on a bum steer.
""",
u"""
Add a final js_ReconstructStackDepth assert after setting fp->regs->sp in js_ExecuteTree's bail-out epilog.
""",
u"""
1. Fix json2.js (it crashes later, another bug) to restore a non-empty stack for a call with missing args after a nested bail-out. This involves changing js_SynthesizeFrame to return the number of stack slots it reconstructed that map to native slots. It also means not counting the missing args in the spdist uint16 pushed onto the state.rp stack (this was the root of all over-counting evil, for this bug).
""",
u"""
Cosmetic cleanup.
""",
u"""
Add a place to store the current shape of the global object as we add slots it the global slot list.
""",
u"""
Add a global slot list to the trace monitor.
""",
u"""
Make sure to trasm the vmprivate of dependent trees as well.
""",
u"""
Updated nanojit for the AMD64 patch.
""",
u"""
Tighter fencepost in getTop, don't overshoot the stack (450997).
""",
u"""
Doh. Deep bailots are pretty rare and js_SynthesizeFrame already uses the fairly slow js_ReconstructStackDepth helper internally, so anotherone to avoid counting stack slots via spbase can't hurt.
""",
u"""
Merge.
""",
u"""
Add a method to type map that captures missing slots (which have been lazily added to the slot list since the type map was created.)
""",
u"""
Fix missing paren in comment; also s/scope/frame/ in same comment.
""",
u"""
Extend the globalTypeMap import(), not in the caller, since we missed extending it in case of re-reading registers after a tree call.
""",
u"""
If RecordTree is triggered, create a new peer fragment (or recycle and unused one) if we already have a tree for this location.
""",
u"""
Try to execute the tree first, and if that fails worry about counting and triggering compilation. This speeds up trace activiation by a tiny bit, but makes code that we can't trace a little bit slower. We use a micro optimization to bypass the call to js_ExecuteTree when its clear that it wouldn't find a tree to executed to reduce this overhead. This change is necessary for multiple trees per bytecode location.
""",
u"""
Give root fragments a treeInfo decorator only if the trace was successfully compiled. Otherwise just keep a reference in the recorder and delete it when the recorder is destroyed. Review welcome. The involved state machine is a bit complex. Added lots of asserts as safety net.
""",
u"""
Only capture the shape of the global object in a tree once that tree tries to access a global, and only check the stored global shape in trees against the current global shape if the tree actually uses globals (which also doesn't trash trees when global variables are added if that tree doesn't actually use globals.) This is approx. a 1% win for sunspider.
""",
u"""
Change interface of js_ExecuteTree to indicate which of the peer fragments it really executed (since we soon will have more than one tree that could be activated for that particular bytecode location).
""",
u"""
Add a ->first pointer to all fragments that points to the first fragment in the peer list. This is the fragment we do JIT throttling/blacklisting on.
""",
u"""
Append peer fragments at the end of the list (so f->blacklist() always counts against the same fragment).
""",
u"""
Add a simple script that calculates an aggregate score over all tests running with the jit in t/*.
""",
                                                                    u"""
Merge.
""",
u"""
Add the concept of peer fragments to nanojit. Each loop fragment can have a number of peer fragments, which we can use to have several different specialized variants of a loop (i.e. for different types). The makefile doesn't pick up the change to Fragmento.h, so make sure you clobber by hand or you will end up wasting an hour of your life in gdb (like me.)
""",
u"""
Merge.
""",
u"""
Update stale comment.
""",
u"""
Don't allow inner trees to lazily pick up any globals since we currently can't handle that. We already ensure that we don't inline trees that have globals. This patch merely makes sure they don't get some additional globals on the fly.
""",
u"""
Similarly to attaching new branches to a side exit, we might end up with a partial type map when exiting from a trace during tree execution, so make sure to merge in missing types from the tree's entry map in this case as well.
""",
u"""
Add test case for type map merging (450535).
""",
u"""
If we extend a tree along a side exit that knew about fewer global slots that we have now in the tree, merge in the types for those additional slots from the entry map (450535).
""",
u"""
Funnel all write-backs to the stack and the global frame through TraceRecorder::writeBack() so we can intercept and manipulate them in one central location.
""",
u"""
Enable nested trees by default. This is going to be exciting.
""",
u"""
I honestly to god don't know why this change is necessary but with this nesting works now for SunSpider and all of my test cases. The stack layout calculation needs some reviewing, seriously.
""",
u"""
Merge.
""",
u"""
Change sp_adj in guards to always reflect the current stack depth, so if we enter a trace/loop with something on the stack, sp_adj will reflect always at least that minimum amount. InterpState->sp now always runs in parallel with regs->sp of the current frame. This breaks nesting badly. I really need help with the stack layout logic.
""",
u"""
- Fix aliasing in LIR.h
""",
u"""
Merge
""",
u"""
- pass pc to String.prototype.match so we can avoid unnecessary object creation when tracing. r=brendan
""",
u"""
Don't just undepend the string, canonicalize it as well.
""",
u"""
Merge.
""",
u"""
Add callee onto the stack to make sure our native frame layout matches the interpreter during calls.
""",
u"""
Fix gc hazard just introduced in fix for .
""",
u"""
Merge. I love hg.
""",
u"""
Cleanup stack adjustment during tree calling.
""",
u"""
Merge.
""",
u"""
Fixed js_ValueToNumber overwriting values on the stack as different types, causing the exit type map to assert.  The breaking conversion was JSVAL_VOID becoming a NaN.  ()
""",
u"""
Consolidate tracing-out-of-js_Interpret abort code at bottom of js_Interpret.
""",
u"""
Make sure sp points to the native stack base of the inner tree when calling a nested tree.
""",
u"""
Merge.
""",
u"""
Don't over-compensate sp_adj (exclude the callee).
""",
u"""
Fixed recorder not aborting when leaving js_Execute ().
""",
u"""
Avoid the malloc altogether if we're going to use a unit string.
""",
u"""
b=450176; trace parseInt and parseFloat; r=gal
""",
u"""
- Add missing JS_free call.
""",
u"""
Fixed the known native arg handler from accidentally using 'continue' to break out of a loop one level higher.  This was causing crashes when the arg didn't match the expected types ().
""",
u"""
Assert on the recording table only if we have enabled the tracer (446551).
""",
u"""
Write back outer tree frames, but exclude the current frame (which the next tree will do). This still crashes the trace-tests.js test case with nesting enabled and for the life of me I can't figure out why (try with TRACEMONKEY=nesting).
""",
u"""
Backed out changeset 089406b2b0aa
""",
u"""
Add an explicit start frame parameter to the FORALL macros, which allows FlushNativeStackFrame to be used for other frames than just the topmost N ones.
""",
u"""
Fix outrageously incorrect comment.
""",
u"""
Added bitsinbyte-ish testcase to trace-test.js. This currently still crashes the VM in nested mode.
""",
u"""
Restore state of the outer frames in case of a nested exit. Should be feature complete but needs more debugging.
""",
u"""
Abort recording if unwinding from js_Interpret to js_Invoke and still recording (this can happen via fun.call/.apply). Also assert in threaded interpreter BEGIN_CASE and DO_OP (from END_CASE) that we either have no recorder or are using the recordingJumpTable.
""",
u"""
FlushNativeStackFrame currently only handles the innermost nested trees writeback, so at least make it use the proper adjusted stack base for that.
""",
u"""
Update inlineCallCount with the total call stack height, which is the sum of rp_adj and any adjustments nested trees added. Also make sure to read all stack adjustment information from the tree we exit on, not the tree we entered (might be different in case of nesting.)
""",
u"""
Print relative stack instead of absolute stack address upon side exit (debug mode).
""",
u"""
Added test case for nested exits.
""",
u"""
Implement nested side exits.
""",
u"""
Merge. If I had a cent for every merge. Sigh.
""",
u"""
Reshuffle code lines in the side-exit return path (do asserts closer to the GlobalFrame writeback.)
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Fix from brendan for propertyIsEnumerable having an inconsistent return type.
""",
u"""
Set rval_ins with initializing=true because nothing will get the callee, so the tracker won't have tracked it yet if it's in virgin stack.
""",
u"""
Forgot to string-tag before going from atom to jsid in two builtins.
""",
u"""
Merge. Lame.
""",
u"""
Add nestedExit to InterpState and comment its fields.
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Fixed from brendan for counting disparity between nativeStackSlots and FORALL_SLOTS_IN_PENDING_FRAMES.
""",
u"""
Fix prototype hit case in prop to advance obj and obj_ins up the proto chain.
""",
u"""
Don't print LeaveFrame debug info when falling out of the global frame.
""",
u"""
Merge.
""",
u"""
When re-importing register values after a tree call, make sure to use the inner tree's nativeStackBase, since we also use the inner tree's sp.
""",
u"""
Merge.
""",
u"""
Read back registers used by inner tree relative to inner_sp (the adjusted sp value). Print frames we enter into and return to in Enter/LeaveFrame.
""",
u"""
Fix bogus varval assert.
""",
u"""
Major and winning overhaul to for-in codegen (mad props to Andreas for advice).
""",
u"""
Don't call inner trees if they use global slots since we don't support those in inner trees yet.
""",
u"""
Merge.
""",
u"""
Flexible call stack allocation with proper guarding for call stack overflows.
""",
u"""
Fixed ifop predicting NaNs as true when they should be false.
""",
u"""
Assert on bogus always-exit guards.
""",
u"""
Fixed ExprFilter emitting corrupt LIR when reducing guards.
""",
u"""
Merge. Nothing to see here. Move along.
""",
u"""
Blacklist a trace if we hit a global shape mismatch. This makes us suck less on date-format-tofte until we find a way to fix the property cache misses.
""",
u"""
Only trash the tree, not the entire cash, on global shape mismatch.
""",
u"""
Fix deep for-in loop bug (450334).
""",
u"""
Add missingArgTest2 to cover the nativeStackOffset bug fixed recently.
""",
u"""
Merge.
""",
u"""
Don't cache loads in import into the nativeFrameTracker, since when coming back from a nested tree we re-load the frame state into registers using import() based on the called tree's state, which pushes loads into the nativeFrameTracker that are relative to the inner tree's call depth. Only cache on writes now, which should be always safe.
""",
u"""
Merge.
""",
u"""
When re-importing registers after a tree call, make sure to use the inner trees calldepth at its side exit, not the call depths of the calling tree.
""",
u"""
Remove bogus assertion.
""",
u"""
Fix missing argument stack offset computation (in both places: FORALL_FRAME_SLOTS and nativeStackOffset). Clear missing args in nativeFrameTracker.
""",
u"""
Introduce a large fixed-size native frame stack and store its ceiling in state->eos.
""",
u"""
Merge.
""",
u"""
Hands down the hardest bug I had to debug in TM so far. Make sure to read back any registers an inner tree might have changed before writing out the typemap for the nested_exit guard, otherwise we might be pointing to old stale pre-(inner-)loop state and pick an incorrect (in this case too narrow) type. fannkuch=2.8x with this.
""",
u"""
- Add String match and three replace overloadings, and allow known native matching to continue in search of exact match (not best, and not abort on first mismatch).
""",
u"""
Add constvalp and isconstp to LIR instructions (nanojit).
""",
u"""
Use aobj consistently in test_property_cache (450317).
""",
u"""
Merge.
""",
u"""
Enumerate missing argument slots on the caller's stack and initialize them to undefined (450304).
""",
u"""
Fix shapelessUnknownCalleeHelper.
""",
u"""
Fix annoying warnings, finally.
""",
u"""
Added NaN test case that fails when jitting; currently looking into why.
""",
u"""
js_obj_hasOwnProperty is supposed to return a boolean but was incorrectly generating code to return a number, resulting on a failure in the boolean comparison due to an unexpected i2f (450304).
""",
u"""
Only use fastcall on x86.
""",
u"""
More guard argument formatting.
""",
u"""
Fixed nanojit using a variable before it got set (verbosity mode only it seems).
""",
u"""
fix !JS_TRACER build
""",
u"""
add way to explicitly disable tracer for easier testing
""",
u"""
Consolidate common name (global slot) addressing code.
""",
u"""
Put trailing args on their own lines when they otherwise would seem to associate with a nested call in a previous arg position.
""",
u"""
Merge, plus ((void)0) parens.
""",
u"""
Fix goto over init whinage.
""",
u"""
fix build for !JS_TRACER, both threaded and switch interps
""",
u"""
guard all of jstracer.h against non-tracer builds
""",
u"""
NAMEINC, INCNAME, NAMEDEC, DECNAME
""",
u"""
Merge.
""",
u"""
Don't read type from typemap if we already have it in a local variable.
""",
u"""
Don't re-record traces over and over in case of excessive type mismatches. Instead, blacklist the fragment and slowly back away from recording it.
""",
u"""
JSOP_FORNAME.
""",
u"""
Factor forInOp from JSOP_FORLOCAL, use it from JSOP_FORARG's recorder too; tighten up JSOP_SETNAME.
""",
u"""
Fix some comments and tighten up assertions about block scope (mrbkap please look).
""",
u"""
Comments for JSOP_{,STRICT}{EQ,NE} about the layering and constraints on evolution of the non-strict equality ops' recorders.
""",
u"""
cmp over number and (string or bool or undefined)
""",
u"""
mistaken relanding, didn't track merges well enough
""",
u"""
reland eb01b1d55d9b after the mismerge
""",
u"""
reland 3ea1e1317707 after the mismerge
""",
u"""
Restore lost shaver rev 0e50c89c476b -- how did that get lost?
""",
u"""
Dependent string test.
""",
u"""
Merge, sigh.
""",
u"""
Rename js_DestroyJIT to js_FinishJIT to match Init/Finish vs. New/Destroy naming scheme used elsewhere; use same #if conditions around #include jstracer.h as around code depending on it.
""",
u"""
JSOP_EQ/NE for objects
""",
u"""
Argh, I hate hg.
""",
u"""
Merge, in the name of all that which does not suck\!
""",
u"""
Merge.
""",
u"""
JSOP_LENGTH handles dependent strings now.
""",
u"""
Merge.
""",
u"""
Fragmento lifetime is now associated with the thread/runtime instead of the context.
""",
u"""
implement JSOP_ADD(str, num)
""",
u"""
Fixed some explicit deallocation bugs that cropped up running in the browser.
""",
u"""
Merge.
""",
u"""
Trash tree if we see an obsolete treeinfo object on record.
""",
u"""
Merge.
""",
u"""
Object.prototype.{hasOwnProperty,propertyIsEnumerable}.
""",
u"""
Handle multi-level property cache hits; put BRANCH_EXIT on its own line so it stands out as the third param to guard in ifop.
""",
u"""
Make Print a fast native.
""",
u"""
Don't try to delete names if we are not building a DEBUG build.
""",
u"""
Merge.
""",
u"""
Added explicit deallocation (, r=gal)
""",
u"""
Support non-flat strings in Any_getelem and Any_setelem.
""",
u"""
Remove obsolete Tests.cpp file.
""",
u"""
Remove default parameter for guard, specify MISMATCH_EXIT explicitly.
""",
u"""
Remove dead code, add a debug printf.
""",
u"""
If we get a series of tree type mismatches, trash the tree (and all dependent trees in case of nesting.)
""",
u"""
Fix FastNewObject built-in to create dense array instance with its own map.
""",
u"""
Beware macro argument multiple expansion...
""",
u"""
Try fixing LOAD_INTERRUPT_HANDLER based on Andreas's patch.
""",
u"""
Match JSOP_NULLTHIS up to JSOP_NULL special cases in the decompiler.
""",
u"""
Don't try to access the name of arguments beyond nargs (r=brendan).
""",
u"""
Merge.
""",
u"""
Avoid goto across initialization of sprop2 (446508).
""",
u"""
Don't use asprintf (446508).
""",
u"""
Rework GCF_DONT_BLOCK to be cx->gcDontBlock, assert it's set, set before entering trace and clear on exit.
""",
u"""
Make js_ConcatStrings JS_FASTCALL and use directly as a built-in; remove gcflag param from it and from js_NewString.
""",
u"""
Unregress FastNewObject builtin to handle user-defined constructors (note to self: run tests before coffee...).
""",
u"""
Fix ASSERT_VALID_PROPERTY_CACHE_HIT pcoff argument (my bad from 887fc4facdeb).
""",
u"""
Back out extra gcflag param change (859b9a23adbf), I set bad precedent and will back out previous such shortly. Want cx->gcflags instead.
""",
u"""
- Trace JSOP_NEWINIT/INITPROP/INITELEM/ENDINIT, which required extending the FastNewObject builtin to create a dense Array or a new Object (easy to discriminate on the constructor function's u.n.clasp member).
""",
u"""
extend js_NewObjectWithGivenProto to permit specifying additional new-thing flags (such as GCX_DONT_BLOCK)
""",
u"""
- Skip dense array object, try prototype, in all JSOP_GET*PROP variants, interpreter and tracer.
""",
u"""
Record JSOP_LOOKUPSWITCH.
""",
u"""
Use true and false for js_EqualString return values now that its return type is bool.
""",
u"""
- Fix shapeless callee guarding to guard on function object value.
""",
u"""
Reoptimize call and new based on shape guards and branded method-ful scopes -- no need to emit function-is-interpreted guards.
""",
u"""
joinTest.
""",
u"""
Add Array (generic) join builtin, plus (not yet used) optional this-class guarding for builtins.
""",
u"""
Implement JSOP_OBJECT.
""",
u"""
Match native map guard specializations in tracer to interpreter, particularly to skip up the proto chain from a dense array in JSOP_CALLPROP (json2.js showed an abort here, pointing to the tracer/interpreter discrepancy).
""",
u"""
Fix JSOP_FORLOCAL to push false when guarded conditions are false while recording (449961).
""",
u"""
- Avoid unnecessary FASTCALL builtin wrappers for existing js_* library-private or friend functions, which could be (and now are) fastcall (JS_FASTCALL). A couple of builtins avoid name collisions by using js_Fast instead of just js_ as their name prefix.
""",
u"""
- Test JSVAL_BOOLEAN tag in TraceRecorder::record_JSOP_TYPEOF, assert no holes or other pseudo-booleans, to unify false/true/undefined testing.
""",
u"""
Restore C compilation support to jscntxt.h, used by liveconnect (only one file now: jsj_JavaClass.c had no need to include jscntxt.h).
""",
u"""
camelCaps test names restored (NewTest => newTest, etc.).
""",
u"""
JSOP_ANONFUNOBJ
""",
u"""
JSOP_TYPEOF and JSOP_TYPEOFEXPR
""",
u"""
Builtin for String.prototype.concat (single int-arg version)
""",
u"""
Implement cmp for string-on-string.
""",
u"""
- TM: trace some more builtins for string-validate-input
""",
u"""
- TM: give xpcshell a JIT switch
""",
u"""
- TM: Assertion failure: JSSTRING_IS_FLAT during trace recording. r=brendan
""",
u"""
Fix obj2 typo, meant obj (obvious use-before-set, sorry about that).
""",
u"""
restore preference for getarg+length over getargprop
""",
u"""
improve naming of anonymous functions and excess args
""",
u"""
Prettier spacing knownNatives table.
""",
u"""
Merge.
""",
u"""
Add an assert to protect against nested exits (not implemented yet.)
""",
u"""
Support calling of nested tree from within inlined frames. When we call a tree that tree expects to be the top-level tree, which means it assumes callDepth=0. If the call of the tree is within an inlined frame, thats not true (callDepth > 0). We adjust the native stack pointer accordingly before calling the tree, and then restore the value of the stack pointer after the call. Fancy stuff.
""",
u"""
Remove ip from InterpState. Calculate the new pc after a trace side exit relative to lr->from->root->ip, which also works if we side exit on a different tree than we entered (which can happen in case of nested trees.)
""",
u"""
Merge from mozilla-central.
""",
u"""
Merge.
""",
u"""
Guard against shapeless callees, with tests (more to do here, can't break the unknown callee case yet, but it should be breakable).
""",
u"""
Merge.
""",
u"""
Get operator new on interpreted functions working, along with JSOP_SETPROP on an unmutated object, or one of the right shape but where the setprop is adding the next property, and it's not in the object yet.
""",
u"""
Better idea for avoiding level-1 property cache collisions.
""",
u"""
Improve first-level property cache hash function to avoid collisions in linear sequence of setprops.
""",
u"""
Fix .
""",
u"""
Add very preliminary nesting for trees. This is disabled by default. To enable set TRACEMONKEY=nesting in the environment.
""",
u"""
Don't activate a tree if it has globals, since we can't handle that yet.
""",
u"""
Remove tracking of outer trees and merging of globals since globals will be maintained centrally soon, not attached to trees.
""",
u"""
We don't deallocate JIT-related data structures when the JIT is shut down. Add a TODO for this.
""",
u"""
Hand the script in when updating the oracle regarding global variable slots even if we don't use it right now. This will be useful for caching information across runtimes.
""",
u"""
Use a typedef SlotList instead of Queue<uint16>.
""",
u"""
Teach typemaps how to capture the types of all slots in a slot list.
""",
u"""
When merging globals from inner trees to outer trees, make sure to push the expected type upstream as well.
""",
u"""
When we trash a tree, we have to trash all outer trees that call it as well.
""",
u"""
Recognize loop edges that hit a nested tree.
""",
u"""
Fix typo (missing memcmp in statement).
""",
u"""
Remove type-map hash code. A direct memcmp seems to be faster (probably some SSE magic behind it in gcc/glibc).
""",
u"""
Factor out the code to capture the current stack type map and move around the type map method implementations to make sure they can see the FORALL macros.
""",
u"""
We expect no interned globals in a new tree. Assert on that.
""",
u"""
Always trash TreeInfo when we recompile. This avoids the much dreaded JS_ASSERT(insInt32) errors and we can do this now because the demotion information is provided by the oracle and no longer stored in the typemap directly.
""",
u"""
Use an oracle to predict when slots are demotable. This allows trashing the TreeInfo* object in the root fragment more aggressively. Rebuild the stack type map at every compile to avert type map mismatches. Purge all global slot info when we re-record a tree.
""",
u"""
If we run into an error during compilation, blacklist that fragment. If we run out of memory, flush the cache.
""",
u"""
Don't fail to flush cx->thread's JIT cache if JS_THREADSAFE.
""",
u"""
Flush JIT cache for all contexts. Clear nanojit error state when we start compiling.
""",
u"""
Remove dead code.
""",
u"""
Add a helper to flush the JIT code cache (and the fragment lookup quick cache). On a global shape mismatch trash the entire cache (might be a bit overly aggressive). Similary, during GC flush the code cache.
""",
u"""
Tracker outer trees for every tree and merge globals of inner trees into all outer trees as we register inner trees with outer trees.
""",
u"""
Add a contains method to Queue.
""",
u"""
Fix misleading debug text.
""",
u"""
add tests for missing and excess arity for trace-entry function context
""",
u"""
Fix tracing of code inside methods that were called with arity mismatch.
""",
u"""
Replace bogus assertion with runtime test for correct abort test (getter or setter, given sprop hit from propcache).
""",
u"""
Fix nonEmptyStack1 test.
""",
u"""
Disable outerlining, to be replaced with nesting.
""",
u"""
Add a helper to emit a tree-call into the currently recording trace.
""",
u"""
Add CallTree builtin.
""",
u"""
Make ip in InterpStruct const*.
""",
u"""
Cleanup stack offset calculation and eliminate the stack offset fiddling that was necessary for nanojit prior to adding the getTop hook.
""",
u"""
Add first non-empty stack testcase, which now passes (yay).
""",
u"""
Merge again, I lost to Andreas\!
""",
u"""
- Add builtins to support for-in loops, both iterating and getting/setter properties by name using o[i] instead of o.p where i is 'p'.
""",
u"""
Always trashing the tree on a type mismatch can't work since the first iteration comes in as undefined for loop-outputs and then kills the main tree that deals with the proper stable types. Have to find a different way to deal with this.
""",
u"""
Pull recompile flag out of the state and pass in as argument. Trash the tree if a secondary trace can't be connected to the loop header. This is very aggressive and might need more tinkering. Trashing the tree on every mismatch doesn't seem to work well, so thats currently disabled.
""",
u"""
If we stop recording, immediately attempt to trigger the tree.
""",
u"""
add test for non-empty stack on trace entry (fails currently, but no longer crashes)
""",
u"""
Properly deal with trace entry with non-empty stack.
""",
u"""
Split side exit handling from js_ExecuteTree.
""",
u"""
Comment or/and test framework not being traceable.
""",
u"""
- Use JSStackFrame* fp over, don't declare another JSStackFrame* f, in the FORALL macros and clones (f is canonical variable name for nanojit::Fragment*, fp for JSStackFrame*).
""",
u"""
Strength-reduced unsigned modulus in the fragment quick cache, don't use signed % which requires a branch and less-than-zero test.
""",
u"""
Misc. cleanup.
""",
u"""
Use INS_CONST to addName a few lir->insImm immediates.
""",
u"""
Fix TraceRecorder::ifop backward logic bug in the OBJECT case, and implement the STRING case. Add tests for truthy and falsy strings.
""",
u"""
Fix return NULL in bool to return false.
""",
u"""
Avoid JSUint64 (NSPR style), use uint64 (SpiderMonkey style).
""",
u"""
Restore lost or/and tests (hg strikes again, grrrr!)
""",
u"""
Merge.
""",
u"""
Use quick cache to bypass fragmento is possible.
""",
u"""
Factor out most of the remaining code in js_LoopEdge into js_RecordTree and move the code to attach new branches into js_ExecuteTree.
""",
u"""
Factor out js_ContinueRecording from js_LoopEdge.
""",
u"""
Add a fragment cache data structure. This will be used to accelerate the fragment lookup during branching.
""",
u"""
Split up FORALL_SLOTS_IN_PENDING_FRAMES macro in a macro that processes a frame, and a macro that uses that macro to process all pending frames.
""",
u"""
Backed out changeset 8421b003fb5f -- it broke string to number, demonstrated by running trace-test.js without the -j (jit) option (10 - "1.3" => NaN instead of 8.7).
""",
u"""
Fix ifop null/object inverted logic sense bug.
""",
u"""
Add || and && tests; use newlines to join pass and fail results now that there are too many tests to be readable joined by commas on one line.
""",
u"""
Add || and && tests.
""",
u"""
Merge.
""",
u"""
1. Don't store thisp literally in state.rp, get it from argv[-1]. 2. Fix DEBUG localNames code.
""",
u"""
Extend ifop to handle undefined tests; implement JSOP_OR and JSOP_AND (so much work\!).
""",
u"""
Style police raid: function names start in column 1, with one blank line between functions.
""",
u"""
1. Don't store thisp literally in state.rp, get it from argv[-1]. 2. Fix DEBUG localNames code.
""",
u"""
Remove synthesizeFrames private declaration -- js_SynthesizeFrames is a static helper now.
""",
u"""
- Implement interpreter frame reconstruction (js_SynthesizeFrame).
""",
u"""
Remove entryStackDepth. Calculate sp_adj relative to entryNativeStackSlots.
""",
u"""
Make synthesizeFrame private.
""",
u"""
Add vprof source files (this time for real.)
""",
u"""
Fixed builtin_dmod not working on Win32.
""",
u"""
Pull in Moh's vprof utility from tamarin-tracing.
""",
u"""
Sync with tamarin-tracing/nanojit tip.
""",
u"""
use optimized path for fromCharCode
""",
u"""
Refactor js_GetUnitString to permit passing in a bare jschar, and use in js_str_fromCharCode.
""",
u"""
Refactor trace-test.js to permit running a single test via `js trace-test.js testName`.
""",
u"""
add specialized StringToInt32 and filter for it
""",
u"""
give strtointeger a way to avoid octal, to streamline ValueToNumber a bit
""",
u"""
Coerce strings to numbers for appropriate ops.
""",
u"""
merge backout of d24e6005ee4c to fix the world
""",
u"""
Backed out changeset d24e6005ee4c (causing major array-fail).
""",
u"""
Merge.
""",
u"""
Remove ANY_TYPE and move debug printf around to print entry point even if we can't enter due to type mismatch.
""",
u"""
Make guard return expected, so we can trace alternate cases easily.
""",
u"""
If trees are not enabled, don't try to reuse state and param1.
""",
u"""
Re-use initial parameters on tree fragments.
""",
u"""
Implement JSOP_EQ and JSOP_NE over strings, plus JSOP_STRING.
""",
u"""
Merge.
""",
u"""
Make the global frame layout match the slot layout in the global object. This will allow leaving global values in place when switching trees as long both inner and outer tree use the same value.
""",
u"""
- Export JSSLOT_ITER_* from jsiter.cpp to jsiter.h, for jstracer.cpp to use.
""",
u"""
Merge.
""",
u"""
Use isGlobal to distinguish whether a value is a global slot instead of scanning the table every time.
""",
u"""
trace Math.random
""",
u"""
Trace String.fromCharCode.
""",
u"""
Clean up the living room a bit since people are going to come by to look at it.
""",
u"""
Add isGlobal to check whether a value is a slot of the global object.
""",
u"""
Note to self: hacking after 4am is detrimental to my spelling.
""",
u"""
Major shakeup of the interning code for globals. Globals are now detected on demand as they are used and the slots are noted in treeInfo->globalSlots. At the same time the type is recorded in treeInfo->globalTypeMap. The stack type-map is maintained separately in treeInfo->stackTypeMap. All these structures are lists and are maintained as List<T> objects. Imports for globals can appear at the top (if we have already seen some imports for the loop header and are recompiling), or on the fly for lazily found values. We no longer intern all global properties that happen to match a name in the current function, and we also support inlining of functions that touch globals that are not used in the method where the trace started in.
""",
u"""
Use List<T> to maintain global slot list in TreeInfo.
""",
u"""
Trash entire tree with all the information associated with it when we have a typemap conflict or the global shape changes.
""",
u"""
Remember number of global slots known at that point in the trace in every side exit (forward-looking change to cope with dynamic collection of interned globals.)
""",
u"""
Merge.
""",
u"""
Add a generic list data structure and fix side exit handling to always pick the right typemap to work with (exit map, not entry map).
""",
u"""
Fixed some MSVC whinings, implemented rdtsc on win32
""",
u"""
Removed unused field from TreeInfo.
""",
u"""
Fixed infinite looping on non-threaded tracing (rumor is that we do Windows builds of Firefox)
""",
u"""
Merge again.
""",
u"""
Guard property cache hits by shape(s).
""",
u"""
Merge.
""",
u"""
Fix a couple of comments.
""",
u"""
Rename gslots to globalSlots.
""",
u"""
Remove global frame transition code. Obsoleted by the new on-demand global loading code which we are about to add.
""",
u"""
Limit tree growth to side exits that expicitly declare that they want to be grown.
""",
u"""
JSOP_ADD over strings
""",
u"""
signs, signs, everywhere signs
""",
u"""
Trace String.prototype.substring for two-arg case.
""",
u"""
Trace JSOP_LENGTH over flat strings.  (Need some cmovery for dep strings.)
""",
u"""
Fix spelling.
""",
u"""
Cleanup global frame switching and add delayed write-back code for doubles.
""",
u"""
Regularize loop update in SwitchNativeGlobalFrame.
""",
u"""
Fix synthesizeFrame's newifp->callerRegs/frame.regs update to pass along the pointer to the precious js_Interpret regs local and update it.
""",
u"""
Try to fix SwitchNativeGlobalFrame, still studying it but these changes seem necessary.
""",
u"""
Fix synthesizeFrame parameterization, and have it reconstruct stack depth; warning and space fixes.
""",
u"""
Export js_ReconstructStackDepth for use by side-exit code when synthesizing stack frames.
""",
u"""
Merge.
""",
u"""
Switch from one global frame to another by walking the two sorted gslots lists.
""",
u"""
Fix uninitialized nbytes in synthesize_frame.
""",
u"""
Compilation fix for MSVC.
""",
u"""
Cleanup and split native frame reading/writing into stack and global part.
""",
u"""
Sort interned global slots in ascending order for fast comparison of two different global frames when switching between them.
""",
u"""
not-yet-working beginnings of frame reconstruction
""",
u"""
Trash the interned globals of a tree if we experience a global shape mismatch.
""",
u"""
Trash the typemap if a change of the global shape forces us to throw away a tree.
""",
u"""
Abort trace if we inline too deeply.
""",
u"""
Merge.
""",
u"""
Track the type of guards and react accordingly if we bail out on them. Guards that protect against out-of-memory conditions don't try to grow the tree. Instead we just resume the interpreter.
""",
u"""
Don't use ABORT_TRACE outside the recorder.
""",
u"""
do setelem in a builtin, so we don't abort trace every 8 times when growing
""",
u"""
If we see a f2i(UnboxDouble) chain, simplify it to UnboxInt32 which does the conversion internally. This also enables a fastpath to read 31-bit jsval integers from arrays.
""",
u"""
Merge.
""",
u"""
Add limited outerlining. Much of this will be subsumed by nested trees.
""",
u"""
remove rval tracking, since it's no longer necessary
""",
u"""
Remove guardCount. No longer needed.
""",
u"""
Smarter speculative demotion of numbers to integers and promotion of the trace seems to require actual doubles. If the number at entry looks like an int we make the slot an int and compile as such. If the loop-tail proves the slot to be a double, we recompile the trace. Currently such miss-speculation cannot be handled on secondary traces since we are currently unable to recompile the primary trace. Such secondary traces are blacklisted.
""",
u"""
Add JSSF_NO_SCRIPT_RVAL script flag, and uint8 flags field for it.
""",
u"""
Fix comment typo.
""",
u"""
Don't try to demote slots on secondary traces (we have to recompile the primary trace as well for that, which we currently don't do.)
""",
u"""
Add a test case for trees.
""",
u"""
Added sunspider tests to t/ for dvander.
""",
u"""
Fix and cleanup rp_adj and sp_adj calculation.
""",
u"""
Eliminate EntryRegs. Its not safe to keep a reference to the entry SP since we might extend the tree from a different outer stack frame. Instead just store the entryStackDepth.
""",
u"""
Print real recording point, not entryRegs and add an assert that makes sure the guard we come out of is associated with the tree we entered into.
""",
u"""
Merge.
""",
u"""
The VP engineering broke JSOP_NAME! We have to check whether the slot is actually interned and otherwise abort.
""",
u"""
Avoid JSOP_POPV in global scripts from load(), etc.
""",
u"""
Fixed entry typemap having wrong allocation size.
""",
u"""
Can't use lr->from. Seems to not get set in certain cases. Go figure. The nanojit tree code is really weird.
""",
u"""
Factor out AttemptToGrowTree.
""",
u"""
Determine ahead of time whether a side exit is a loop-terminating side exit instead of re-determining this at every side exit.
""",
u"""
Move trace activation code into js_ExecuteTree().
""",
u"""
Make demotion threshold optional (0=off, 32=default). Turn off to debug the type assert bug.
""",
u"""
Don't demote slots in overly long traces (based on counting the number of guards, current threshold=32).
""",
u"""
Cleanup iteration over all slots to use a single macro to avoid code duplication.
""",
u"""
Add shark support to md5.js directly, no longer around the recorder.
""",
u"""
Make the interpreter notify us when frames are popped so we see he right cx->fp value. Fix return value tracking for JSOP_STOP.
""",
u"""
Backed out changeset a58e7ce6eb7f. stack(0) is wrong, if at all it should have been stack(-(1 + argc)). But anyway, its impossible to write through to the frame via set() at that point because leaveFrame() doesn't actually modify cx->fp. We need to wait for the interpreter to do so. Until then nativeFrameOffset produces incorrect values and the assert fails in set.
""",
u"""
fix return-value handling for new stack layout
""",
u"""
Maintain a separate frame for globals using InterpState->gp.
""",
u"""
Add a fast path for nativeFrameOffset that walks entire groups at a time, not slots. Check against the result calculated by the FORALL macro in DEBUG builds (for sanity).
""",
u"""
Merge. Make sure we clear out all slots from the tracker when leaving a frame.
""",
u"""
When addressing locations above the stack water level, use ->sp as base. Shaver accidently changed this to ->spbase when merging Igor's patch, so we were writing past the water mark and the stores were killed.
""",
u"""
Lazy fill the stackTracker as we lookup the nativeFrameOffset for values. Purge all entries related to the current frame when it is popped. This code could be further simplified if Tracker was a template.
""",
u"""
tighten up some bounds, still not quite right
""",
u"""
merge from andreas
""",
u"""
merge (still not working, probably box/unbox dumbness)
""",
u"""
merge (now compiling, untested)
""",
u"""
merge (mostly, doesn't build)
""",
u"""
Handle leaving of frames in one central place.
""",
u"""
Reduce HOTLOOP threshold to 2.
""",
u"""
Avoid calculating native frame offset by tracking the last load/store for every slot and extracting the offset from there.
""",
u"""
Avoid nativeFrameOffset calls in import().
""",
u"""
Merge.
""",
u"""
Add a pattern to recognize safe_add and emit a simple add for it.
""",
u"""
use nargs rather than argc, since bytecode only refers to [o-nargs) args
""",
u"""
make time.sh more useful
""",
u"""
Reverse the insanity that used to be tamarin's arg passing in ins2. Now it makes sense.
""",
u"""
Avoid overflow checks on integer adds when its safe to do so.
""",
u"""
Eliminate entryFrame pointer (not safe to carry that around.)
""",
u"""
Use callDepth instead of entryFrame in the FORALL macro.
""",
u"""
Eliminate exit filter, write the type map directly in snapshot.
""",
u"""
Sink stack-targeting type conversion in the set() path instead of in the ExitFilter.
""",
u"""
Use callDepth, not entryFrame in nativeFrameSlots().
""",
u"""
Remove excess parameters of verifyTypeStability.
""",
u"""
Track call depth in the trace recorder. This lays the groundwork to get rid of entryFrame.
""",
u"""
beginning of entryFrame removal
""",
u"""
Merge.
""",
u"""
Use ti instead of fi for TreeInfo pointers.
""",
u"""
Rename VMFragmentInfo to TreeInfo.
""",
u"""
Merge.
""",
u"""
Style cleanup and eliminate redundant f2u(i2f|u2f) chains.
""",
u"""
Avoid tracking object properties, make incElem work.
""",
u"""
fix no-tracer build
""",
u"""
Cite with a FIXME instead of omfgHack_ prefix ;-).
""",
u"""
Tighten up js_IsLoopEdge and include JSOP_IFNEX.
""",
u"""
Nit patrol.
""",
u"""
add simple timing harness
""",
u"""
Simplify updating of the side exit target.
""",
u"""
simpler loop exit check (backwards is a loop exit, forwards is not)
""",
u"""
force Math to be interned, and defend against non-interned globals until upvar saves us all
""",
u"""
Use exponential backoff when trying to extend trees.
""",
u"""
Merge.
""",
u"""
Don't emit boxed values, use the unboxed representation for constants.
""",
u"""
Removed meaningless assert.
""",
u"""
don't pretend we can trace INCELEM and friends (fixes trace-test.js, ahem)
""",
u"""
move summarization to the end, so I can see it through the debug spew
""",
u"""
improve tracing/recording diagnostics
""",
u"""
discard trace on global shape mismatch
""",
u"""
Breathe, vertical-spacing, breathe!
""",
u"""
Implement DEFLOCALFUN for the fully-lightweight case.
""",
u"""
Improve js_IsLoopExit (unannotated JSOP_GOTO is still ambiguous).
""",
u"""
Fix incProp to box and store (incElem still todo).
""",
u"""
Merge. hg sucks.
""",
u"""
Don't demote fmul since it overflows in math-partial. We might try to demote it and then promote back if this happens (depends how aggressively we want so speculate). Speedup 6.6 for math-partial (since its sin/cos/pow heavy.)
""",
u"""
First stab at incops, plus unbox_jsval tag-masking guard fixes, plus misc. cleanup.
""",
u"""
Abort trace is STOP is leaving the recording context.
""",
u"""
Propagate TCF_COMPILE_N_GO through to inner functions, so that we can avoid nulling their parents and then cloning expensively in DEFLOCALFUN.
""",
u"""
Make entryFrame/entryRegs relative to the tree entry since we only adjust ip/sp/rp when exiting from the tree, not in between fragments.
""",
u"""
Adjust ip/sp/rp in the interpreter recovery code, not on the trace.
""",
u"""
Write all the debug output to stdout (we can't easily make everything go to stderr, so this way at least it all goes into the same place.)
""",
u"""
Rework some of David's changes. Make sure we don't modify the tree until we are ready to attach the new fragment. Share lirbufs between tree branches.
""",
u"""
Got side exits seemingly working, added if.js to trace-test.js
""",
u"""
Handle more operand types in ifop().
""",
u"""
Better diagnostic info for trace abort.
""",
u"""
lookup/find, but do not fill prop cache from recorder
""",
u"""
When PROPERTY_CACHE_TEST misses, fall back to doing our own lookup via js_GetPropertyHelper.
""",
u"""
Try to clean up the memory allocation/deallocation through the avmplus glue code.
""",
u"""
Warning elimination.
""",
u"""
Make sure we compile again if we reject a trace by decrementing hits.
""",
u"""
Fix hot loop triggering.
""",
u"""
can't easily find real names for globals, so just number them
""",
u"""
Merge.
""",
u"""
Disable trees for the time being.
""",
u"""
Label globals and locals with their source-names in trace.
""",
u"""
Use the property cache for JSOP_NAMEINC, etc.
""",
u"""
Fix property cache fill to use the right shape.
""",
u"""
Always select gvar ops for declared global vars, instead of only if loopy/enough-used.
""",
u"""
Add if.js example for trees.
""",
u"""
Add the beginning of support for trees.
""",
u"""
Don't allocate FpRegs if sse2 is enabled.
""",
u"""
Add js_IsLoopExit that indicates whether a side exit is likely to continue the loop or not.
""",
u"""
Cleanup recorder activation, use a single hot loop threshold (10).
""",
u"""
Added statistics and a js_DestroyJIT hook. Also use debug_only and not verbose_only as #ifdef DEBUG shortcut.
""",
u"""
remove pointless untracedCall test
""",
u"""
Fix signature of insCall in the FuncFilter and remove f2i(i2f) elimination since we shouldn't really ever hit it.
""",
u"""
Merge.
""",
u"""
Move up addName to make sure it gets inline in non-debug mode.
""",
u"""
Add setprop and tests for setprop and cleanup labling code for debug mode (m=gal).
""",
u"""
summarize test results
""",
u"""
Cleanup trace abort handling.
""",
u"""
Merge.
""",
u"""
Fixed ASSERT JS_DOUBLE != JS_VOID issue. If the root fragment fails to compile, trash the type-map and re-capture it when we try to re-compile.
""",
u"""
JSOP_LENGTH
""",
u"""
Increase code cache size.
""",
u"""
4.2, dammit
""",
u"""
Merge.
""",
u"""
Fix f2i(i2f) filter (broken since the last TT sync, argument order changed from right to left to left to right).
""",
u"""
Prefer getarg;length, etc. to getargprop.
""",
u"""
copy capacity when becoming another list
""",
u"""
Don't clear out arguments, clear out variables at method entry.
""",
u"""
Better naming of the after_JSOP_CALL event (EnterFrame).
""",
u"""
Notify the recorder when a new frame was created by JSOP_CALL.
""",
u"""
Initialize arguments to void and write JSVAL_HOLE's value onto the native stack, not its boxed representation.
""",
u"""
Fixed call tests.
""",
u"""
Hand in typemap the recorder is supposed to use (preparation for side exit compilation and trees).
""",
u"""
Move the allocation of the LIR buffer and the FragmentInfo data structure creation (which includes typemap and interned global calculation) into loopedge.
""",
u"""
Fix typo in test cases.
""",
u"""
Make JSOP_CALLNAME tell us why it doesn't like to trace.
""",
u"""
Add md5.js so we can play with it. We should sweep these test cases into a subdir or just delete them once they trace.
""",
u"""
Add testcase for chains for global calls.
""",
u"""
Fix generation of VOID immediates and initialize rval after the new frame was setup by CALL.
""",
u"""
Add generic recorder hooks that are called before and after all opcodes as we trace. We might want to instead just move to pre_OP and post_OP.
""",
u"""
Add test case for CALLPROP.
""",
u"""
Don't intern global function objects onto the native frame since we rarely ever need them anyway (we call them via the property cache).
""",
u"""
Enable CALLNAME and add test case for it so we can call global functions.
""",
u"""
Add test cases for call.
""",
u"""
Make sure this/argv[-1] is set fpr CALLVAR and CALLARG.
""",
u"""
Enable inlining for calls. Deep bailouts (from within side exits) are generated but are not allowed to be ever taken (for now).
""",
u"""
Don't use a builtin for this. For functions its interned in the native frame. For global this we read from fp->thisp. Restore jsinterp.cpp and jsinterp.h (no longer need COMPUTE_THIS exposed).
""",
u"""
Synced nanojit with TT tip.
""",
u"""
fix GETXPROP; thanks to brendan for playing chewbacca
""",
u"""
CALLARG, CALLVAR
""",
u"""
fix scalpel left in nativeFrameSlots from aborted thisp addition to frame
""",
u"""
implement JSOP_MOD
""",
u"""
Trace JSOP_THIS and JSOP_THISPROP.
""",
u"""
Fix uncomplete range check for slot numbers of interned globals.
""",
u"""
Added math-partial-sums.js for danderson.
""",
u"""
Remove dead code.
""",
u"""
Aliasing cleanup for LIR.h. Patch submitted for upstream review.
""",
u"""
Strict aliasing cleanup.
""",
u"""
Add a few consts to char* pointers to pacify gcc 4.2.
""",
u"""
Compilation fixes for gcc 4.2. Ripp out write-barrier code in our avmplus glue layer.
""",
u"""
Switch tracemonkey over to gcc-4.2 on macosx. We need a compiler that was released in this millenium so we can use SSE2-based calling conventions.
""",
u"""
rename getpropfromval, it burns mine eyes
""",
u"""
Assign blame where blame is due.
""",
u"""
Merge.
""",
u"""
Add missing namespace use (pending upstream for review.)
""",
u"""
Sync with TT.
""",
u"""
initialize dslots_ins
""",
u"""
Propagate error exceptions from TraceRecorder ctor; fiddle/trim space.
""",
u"""
GETVARPROP, GETARGPROP, GETXPROP
""",
u"""
more ABORT_TRACE instrumentation (some should be asserts?)
""",
u"""
Generate a list of interned global slots (gslots) when we process the tree header. This list is then used whenever we iterate over the native frame. This is faster and safer than looking up properties in the global object every time.
""",
u"""
Remove state exposing accessor functions from recorder and instead hand in that state via the constructor into ExitFilter.
""",
u"""
Guard in FragmentInfo on the shape of the global object. Don't check for the shape of the global object on the trace.
""",
u"""
Store list of interned global slots in struct FragmentInfo
""",
u"""
Added a callstack that will track the pc of the call that caused a function call to be inlined. This is necessary to recover from deep side exits inside inline functions. The callstack is subject to store elimination, so unnecessary stores to the stack will go dead automatically during compilation (i.e. if we inline a function that doesn't have side exits.)
""",
u"""
Fix warnings.
""",
u"""
Use JS_GetGlobalForObject to get the global object. Walking back the call chain is not equivalent and not safe.
""",
u"""
fix our aliasing idiocy by extending jsdpun, add Math.sqrt, add strict-aliasing to our Makefile.ref flags
""",
u"""
Non-null prop from js_LookupProperty means found, so must unlock obj2 (now pobj) in all such cases.
""",
u"""
Clean up shaver's cleanup.
""",
u"""
Fixed printing of integer incoming values in DEBUG mode.
""",
u"""
merge, and fix locking and logic for FORALL_SLOTS
""",
u"""
make JSOP_CALL builtin specialization data-driven
""",
u"""
Skip properties that were not found by LookupProperty.
""",
u"""
Reserve space for every global property that the current script has an atom for instead of trying to rely on ngvars.
""",
u"""
Backed out changeset 2af185cb0fb7. We will map in global variabls different so we don't need the higher ngvars count to find globals in the native frame.
""",
u"""
expand int-equality tests
""",
u"""
Merge.
""",
u"""
js_ for library-extern names like math_sin.
""",
u"""
fix the secondary map-native guard
""",
u"""
initialize traceMonitor in threadsafe builds
""",
u"""
Guard against subzero array indices
""",
u"""
Demote fneg to neg if input is known to be an integer (untested).
""",
u"""
Merge.
""",
u"""
5 hours of debugging, and 9 keystrokes to fix it. That was one expensive bug. shaver's reduced fannkuch example works now. I think independently of this one we don't check properly for index underflow in dense arrays. Shaver is going to have to take a look at that (this fix makes fannkuch indexes not become negative, but doesn't explain why we crash so hard if they do become negative).
""",
u"""
add JSOP_NEG and tests
""",
u"""
add Math.cos and Math.pow to the specialized-call party, and add tests
""",
u"""
I will remember that stacked values are not boxed.
""",
u"""
Specialized tracing of Math.sin, as a proof of concept.  Doesn't quite work due to regalloc mismatch, but close!
""",
u"""
merge
""",
u"""
Incomplete stab at CALLPROP, added ABORT_TRACE for better diagnostics, make math_sin non-static in preparation for specializing call.
""",
u"""
Nits: avoid (double-)over-parenthesization, underhang extra args to start in same column as first.
""",
u"""
add reduced fannkuch version
""",
u"""
Print meaningful filename/line-number info for trace entry/exit.
""",
u"""
Report the source location when recording a trace.
""",
u"""
Don't demote u2f conversions and sink the type cast into the side exit type map, because this loses the sign bit for unsigned values. We could fix this by adding an explicit unsigned type to the map, but for now I think we should stick to int/double only since there is the risk of fanning out trees. Crypto doesn't seem to use ush all that much so we should be ok performance-wise.
""",
u"""
Windows cares a lot more about where FASTCALL is; such a sensitive platform
""",
u"""
begone, cat nspr/Version error noise
""",
u"""
set some more config bits for Windows, mostly blindly
""",
u"""
turn on all the shift tests, and find a bug with it!
""",
u"""
Brendan fixed global variable access in non-top level code so re-enable that in trace-test.js. We pass all of shaver's trace torture tests.
""",
u"""
Poking around in the arm code, trying to make it not die miserabily with BUILD_OPT=1.
""",
u"""
Still trying to get the ARM register updating right.
""",
u"""
Trying to make arm work. Flying blind here.
""",
u"""
Adjust sp/ip for ARM. Very useful when trying to run on ARM.
""",
u"""
some ARM stuff
""",
u"""
Merge (no, really, can someone teach Mercurial to not do this?).
""",
u"""
Output the value if we can't enter a trace because of a type mismatch.
""",
u"""
Don't crash when expecting an int32 as double box in unbox but getting something else (and better debug output).
""",
u"""
1. Fix !JS_THREADED_INTERP bugs in BRANCH and recording switch case generation.
""",
u"""
here, have a _working_ Thumb back-end
""",
u"""
here, have a Thumb back-end
""",
u"""
only build JIT builtins if ENABLE_JIT, and lose antique *inlines.h
""",
u"""
Merge.
""",
u"""
IFEQ and IFNE are identical for us. We just expect the same boolean on the stack and side exit if not.
""",
u"""
Build the JIT by default if we're on x86, and control enabling it for content
""",
u"""
don't include jstracer.h (and thus nanojit, etc.) if not building with JS_TRACER
""",
u"""
use a type that windows knows about for offset computation
""",
u"""
try to get alloca on Windows; remind me to strip these flailing commits before we merge
""",
u"""
my turn to merge; had to happen eventually
""",
u"""
disable tracer for platforms not supported by nanojit
""",
u"""
some better OS_CFLAGS for Linux
""",
u"""
support non-JS_TRACER builds
""",
u"""
try to make alloca work for Windows
""",
u"""
shaver's favorite operating system of choice doesn't like templates, so de-template tracker since we use it with LInsp only anyway.
""",
u"""
Actually fixed ifeq/ifne fusion now.
""",
u"""
nanojit doesn't support loads with non-constant offsets so don't do that
""",
u"""
fix opcode math with the mighty hammer of casting
""",
u"""
the rest of the stdint defs, no idea why I didn't do them before
""",
u"""
Merge.
""",
u"""
Steal the reference to cx from the BoxDouble call instead of observing the load.
""",
u"""
Fixed the setelem a[i] bug.
""",
u"""
Nanojit needs a LINUX define (which may be my fault), fixing it here for now
""",
u"""
use VirtualAlloc for Windows, since it lacks valloc
""",
u"""
interp needs tracer.h
""",
u"""
Decouple jscntxt.h from jstracer.h so that xpconnect doesn't try to include all of
""",
u"""
FASTCALL for Windows
""",
u"""
int32_t, now available on Windows
""",
u"""
Unlike software developers, g++ doesn't like variable-sized arrays.  Have some alloca!
""",
u"""
update trace-test.js, now crashes calling lsh() the second time
""",
u"""
Fixed guarding of eq+ifeq/ifne fusions and enabled tracing JSOP_GOTO (no-op)
""",
u"""
Root all strings and objects first when unboxing. Then box values that might trigger the GC (doubles/ints). This probably needs some performance tuning over time.
""",
u"""
Merge.
""",
u"""
Don't concede an inch to ISO C++. Substract the size of array[1] from the overall struct size when allocating.
""",
u"""
MSVC knows about intptr_t, and doesn't like our remix
""",
u"""
I'm going to just keep bludgeoning these typedefs until they stick
""",
u"""
try to find malloc on Linux; this buildbot thing rules the school
""",
u"""
use typedefs instead of stdint.h, because someone forgot to tell MSVC it was 2008
""",
u"""
can't have zero-sized arrays in ISO C++, says gcc
""",
u"""
use stdint.h instead of typedefs to help Linux find intptr_t
""",
u"""
build nanojit
""",
u"""
Make nanojit arch selection explicit in config/*, though for now only OS X and Linux
""",
                u"""
rename builtins.tbl *back*, because nanojit expects that name, and whatever
""",
u"""
rename builtins.tbl to our usual form
""",
u"""
fix include ordering for THREADSAFE build
""",
u"""
fix compilation, but possibly not logic, of shared-object defense
""",
u"""
revert ancient shuffling of js_CompareAndSwap decl to fix THREADSAFE build
""",
u"""
some build fixes to help in-browser and other-arch build
""",
u"""
Prime the page cache during VM startup. This makes us eat the page cache allocation overhead there instead of during the first use. This is just a hotfix. We still need a rewrite of the page cache.
""",
u"""
Backed out changeset 234230320093 (reducing code cache size due to startup issue.)
""",
u"""
Assert if no gvar is allocated for an undeclared global.
""",
u"""
Always allocate gvars for top-level scripts if any global names are used -- may hurt some microbenchmarks but we can fix it via .
""",
u"""
Merge.
""",
u"""
varobj is not passed through the chain. Make sure to use global->varobj for gvar access.
""",
u"""
More tests, working on crashes.
""",
u"""
Merge.
""",
u"""
Condition fp->arg*/*vars usage on fp->callee, not fp->down.
""",
u"""
Reduce code cache size until we fix the page allocation code to not touch all the pages at startup (nanojit issues, assigned to gal).
""",
u"""
Fixed name/setname code to just track the value move instead of touching memory since we have global variables in our native frame now. We have to fix the page cache issues before we can benchmark this.
""",
u"""
Add verbose native stack frame printing.
""",
u"""
Memoize implicit gvars in the interpreter, on assignment (JSOP_BINDNAME/JSOP_SETNAME); fix recoder l/r operand order bug.
""",
u"""
1. Fix inc to address the right result stack slot; 2. Require via assertions that the interpreter memoize implicit gvars (patch to do that next; bitwise-and will assert until that lands).
""",
u"""
Add missing #undef, clean up trailing whitespace.
""",
u"""
Remove unnecessary JSOp cast.
""",
u"""
Memoize global name gets and sets as if they refer to a declared gvar.
""",
u"""
Merge.
""",
u"""
Removed assert that compares nativeFrameSlots to nativeFrameOffset since nativeFrameOffset is undefined in case sp is at sp+depth, so the assert sometimes randomly bites. Also fixed typo in cmp(). trace-test.js compiles now.
""",
u"""
Tweak a few interval tests, eliminate casts, space patrol.
""",
u"""
Update with some additional test coverage (crashes in setgvar test)
""",
u"""
Sync with mozilla-central.
""",
u"""
Stricter typing of the tracker code path which now only accepts jsval as suggested by Brendan.
""",
u"""
Fixed bug in nativeFrameSlots and use an assert to compare the result with nativeFrameOffset (which is slower, but more precise).
""",
u"""
Removed numMapEntries since typeMap is not really part of the SideExit struct yet anyway.
""",
u"""
Move builtin[] table in jsbuiltin.cpp
""",
u"""
Housekeeping. Remove a few warnings during BUILT_OPT and spelling in comments.
""",
u"""
sp_adj is now maintained in bytes, not words, so +8 is now the magic value to point to the top of the stack. All stores above that watermark are eliminated by StackFilter in nanojit.
""",
u"""
Merge.
""",
u"""
Removed bogus debug printfs.
""",
u"""
merge
""",
u"""
rval tracking and JSOP_POPV
""",
u"""
protect printf with DEBUG
""",
u"""
Fixed frame walking FORALL_PENDING_FRAME_SLOTS and add 4 to sp in getTop (hotfix, not the right way to do it.)
""",
u"""
Merge.
""",
u"""
Use more efficient address mode for LIR_load if possible and removed bogus printf.
""",
u"""
Merge.
""",
u"""
Single-ended interval tests, plus space patrol.
""",
u"""
Implement JSOP_SETNAME for globals.
""",
u"""
Merge.
""",
u"""
Builds against latest nanojit; merged VMSideExitInfo into SideExit
""",
u"""
Merged with tamarin-tracing (Moved SideExit and GuardRecord out of nanojit, improved labelling)
""",
u"""
Fixed argv[n] and vars[n], should be [0] of course.
""",
u"""
Add dummy vpname/vpnum parameters when not compiling in DEBUG mode.
""",
u"""
Introduce a generic stack frame walking macro. This eliminates the 6 (hg pull) redundant blocks of code that all walked the stack in 6 different ways, each with their individuals quirks.
""",
u"""
Don't check the types for invalid global slots in checkType. Proper gvar lookup in boxing path. We have to unify the stack frame traversal and enumeration code. I fixed this bug before, just in a different place. 11x speedup for gvar.js
""",
u"""
root converted argv[0]
""",
u"""
Add disfile() helper to debug shell, to make it easier to see disassembly of top-level scripts.
""",
u"""
Properly display the 'any' type in the side exit map printout.
""",
u"""
Cleanup definition of tracker (don't use LInsp, use T, its a template now).
""",
u"""
Hack: demotable stores have to be flagged as int in the exit typemap. This needs cleanup.
""",
u"""
Don't expect args and vars in a top-level frame that is mapped to the native frame.
""",
u"""
Merge.
""",
u"""
Fixed native frame offset calculation for globals.
""",
u"""
fix type checking of gvars
""",
u"""
reduce loop count in trace-test for faster interp runs
""",
u"""
more detailed type-instability diagnostics
""",
u"""
We urgently need shaver's magic native stack/typeframe iterator. Fixed exit map builder to skip argv/vars for global scope.
""",
u"""
Fixed increment for DECGVAR.
""",
u"""
Bugfixes to the native stack and typemap handling code.
""",
u"""
Attempt at cleaning up the typemap/stack frame iteration code.
""",
u"""
ngvars and the slot index are not related, so don't rely on ngvars < JS_INITIAL_NSLOTS to decide whether dslots exists
""",
u"""
Make gvar ops use the global varobj values we unbox onto the native stack. The stack offset handling needs more work.
""",
u"""
We shouldn't read globals onto the stack if the global object is used by another context so we just refuse to execute the trace in this case.
""",
u"""
Unbox global variables onto the native stack and re-box them. This has certain synchronization implications but will make top-level scripts quite a bit faster.
""",
u"""
Don't try to demote a slot we already decided we can't demote. Also, make sure we only demote additions with constants where the constant fits into an int.
""",
u"""
Removed an unused variable from the avmplus glue code.
""",
u"""
Merge.
""",
u"""
Indentation and comment wrapping (at 79, 99 looks too long and most comments still avoid going past 80+/-).
""",
u"""
Merge.
""",
u"""
Sync nanojit with tamarin-tracing tip.
""",
u"""
Use jsopcode.tbl for tracer JSOP_* method decls; trim trailing whitespace.
""",
u"""
Cleanup the native frame -> interpreter frame boxing code. We sometimes end up with numbers on our stack in double format that are really ints. We have to detect those and properly store them as in on the interpreter stack.
""",
u"""
Add support to demote stores of constants that are currently represented as float but are really integers. bitwise.js is now compiled complete fp-casts free.
""",
u"""
Demote floating point comparisons even if one side is constant (bug in nanojit, filed as #443884 against tamarin). Also demote add/sub/mul using the integer overflow detection side exit code that Ed adopted upstream. Tight loops (bitwise) are not emitted completely as integer code after the initial compilation using doubles triggered a speculative demotion of the context slots.
""",
u"""
Sink type conversions into the side exit by updating the map and seeing though the cast in the store (in ExitFilter). Add a whole bunch of asserts on the varios speculative type states to make sure we get the state machine right. Import speculated integer values as integers into the trace (indicate in entry map).
""",
u"""
Added loop-tail driven context slot type demotion. Without all the buzzwords, what this essentially means is that we detect if the last value that the trace leaves in a slot (which is the value that flows along the backedge back to the loop header) is known to originate from an integer value via i2f, we flag the slot as type integer and recompile the trace. We do this where type stability is certain (result of an and, i.e.) or where its very likely (++operator). If the speculation fails, the same analysis flags the slot as blocked, which means it will always be double. The hope is that this analysis converges quickly (1-2 recompilations tops).
""",
u"""
Make sure we don't get the argument order in BoxDouble wrong again.
""",
u"""
Make typemap uint8_t and fix order of arguments in call to BoxDouble.
""",
u"""
remove outdated guard (now inferred via filter as needed)
""",
u"""
we only speak double around here now
""",
u"""
remove bogus NOT_REACHED
""",
u"""
Strength reduce i2f(doubleToInt32(x)) and u2f(doubleToUint32(x)) to x. This eliminate most of the on-trace overhead, but we still need type peeling of loop variable into int to win back the performance loss casting introduced.
""",
u"""
Reduce redundant doubleToInt32(i2f(x)) chains to simply x.
""",
u"""
Strength reduce BoxDouble(i2f(x)) to BoxInt32(x). Make sure loop indexes are actually integers. This guard will be eliminated further down in the pipeline if we decided to peel the type of the loop variable (index) down to integer.
""",
u"""
Since numbers are now always represented by doubles at the recorder/type level, using BoxDouble and UnboxDouble only when moving numbers from or to memory. A filter will then turn f2i(UnboxDouble) into UnboxInt where appropriate.
""",
u"""
Move the type level from int/double to number. All traces start out as double in all slots, and denote and promote to/from int as needed. The FuncFilter optimizes on-trace casting and elininates redundant f->i-> chains. More optimization needed on this of course, and this code is now a bit slower than the previous integer-register use. However, this does solve the q += 2.5 issues. The heap access code does not properly cast yet and is likely unstable.
""",
u"""
Trace GETGVAR and INCGVAR, though not yet correctly.
""",
u"""
Add unary and binary helpers that automatically demote and promote when dealing with integer operations (not used yet, need loop typemap peeling in place first.)
""",
u"""
JSVAL_IS_BOOLEAN does what isTrueOrFalse was trying to do.
""",
u"""
Fix template, should use typename, not class.
""",
u"""
Add ExitFilter, which builds side exit typemaps for us. This had to be moved into a filter, because this has to happen after we eliminate redundant i2f-f2i chains as we can sink those into the side exit by simply storing the unpromoted/undemoted value and just flip the type in the exit map.
""",
u"""
Merge.
""",
u"""
Added doubleToUint32 builtin and make tracker a template.
""",
u"""
fix builtin_UnboxInt32 signature and name shape_ins for debugging
""",
u"""
Trace JSOP_NAME, and refactor out jsval unboxing.
""",
u"""
begin on JSOP_NAME, refactor stobj_get_slot to chain better
""",
u"""
Fix optimizer flags for interp and builtins in debug mode, and clean out old
""",
u"""
actually record at HOTLOOP1 (fencepost)
""",
u"""
some remaining low-hanging ops
""",
u"""
move JSOP_DOUBLE impl to, er, JSOP_DOUBLE (wtf?)
""",
u"""
Implement JSOP_DOUBLE.
""",
u"""
Added support for semi-stable loop variables. Compiling for(...) q += 2.5; is ridiculously difficult because it flip-flops between int and double. Add support to promote integer values to doubles at the loop tail if at loop entry we expect a double. Since this isn't possible the other way around, we have to get luck that we catch a path into the loop where q is already double. For this we add 3 trigger points (10, 13, 37). We will try three times to record a trace at those iteration counts of a loop. If none succeed the loop is blacklisted. This probably needs more tuning down the road.
""",
u"""
Merge and rename jsIf to ifop.
""",
u"""
Added FuncFilter from tamarin core (not part of nanojit yet since its slightly VM dependant).
""",
u"""
Add helpers for i->f and f->i conversion. The f->i path goes via builtin calls.
""",
u"""
Add type primitives for numbers (isNumber and asNumber).
""",
u"""
Implement JSOP_IFEQ, JSOP_IFNE, JSOP_DUP, JSOP_DUP2.
""",
u"""
Add casting for objects and cleanup casting code.
""",
u"""
let JSOP_GETELEM handle boolean values too
""",
u"""
Handle boolean lval in SETELEM; now runs access-nsieve unmodified.
""",
u"""
Believe it or not NEG can actually overflow the int32 range, so add an overflow bailout. This will only trap for -0x80000000.
""",
u"""
Merge.
""",
u"""
Added blacklisting of recording points where we failed to complete a trace (overly aggressive at this point, needs tuning, we want to try several times for each point.)
""",
u"""
Allow hole-filling JSOP_SETELEM to remain on trace.
""",
u"""
Fixed boolean boxing.
""",
u"""
Added boolean boxing/unboxing code.
""",
u"""
Use default parameter in LSH/RSH/URSH to indicate we don't care for the overflow.
""",
u"""
Added missing jsbuiltins.cpp
""",
u"""
Add support for some misc opcodes including binary and arithmetic and/or/not.
""",
u"""
Track trace entry/exit in debug mode and count cycles.
""",
u"""
Signal error from the boxing/unboxing using magic cookies since gcc seems to very seriously object to the use of uint64 return values during a fastcall (horribly inefficient code).
""",
u"""
Help the branch predictor in the builtins.
""",
u"""
use FASTCALL for builtins
""",
u"""
Style nitpicking. Fix overlong lines.
""",
u"""
Finish SETELEM for int and double values.
""",
u"""
Merge unboxing code into GETELEM code.
""",
u"""
Merge.
""",
u"""
Added box_int_jsval for the store path. Use only there.
""",
u"""
Code generators to access object slots and native code callouts (builtins) for boxing doubles and ints. Ints have to be boxed through a native code helper on read and write (BoxInt32 and UnboxInt32), because we sometimes have to cast internally to double to store 32-bit values. We don't want a separate trace in this case, so we have to do this inline in a helper. Also a couple of modifications to shaver's code. Always make sure to check types (JSOP_NEG).
""",
u"""
Fix dumb bugs I just committed, use JS_NOT_REACHED.
""",
u"""
Try to keep 64-bit portability via size_t instead of unsigned, jsuword for uintptr instead of long, etc.
""",
u"""
Spacing and comment nits picked while reading.
""",
u"""
shift ops
""",
u"""
Beginning of SETELEM/GETELEM tracing for dense arrays.  Needs computed-offset
""",
u"""
update to isInt
""",
u"""
merge
""",
u"""
[mq]: simple-ops
""",
u"""
Introduce asInt and asDouble to check for the type of values based on the actual value since some 32-bit integers hide out in doubles.
""",
u"""
Make trace-code 32-bit clean and extend interpreter state to carry the current context (cx). The recorder still has to record a 31-bit int path through the loop, but the emitted code is able to stay in the tree even if values bump over to 32-bit ints.
""",
u"""
Added support for SET_VAR again. bitwise.js working now.
""",
u"""
Fixed some stack handling and trace activation issues. We can run trace.js again.
""",
u"""
Cleanup of stack handling.
""",
u"""
Added back support for the instructions required to compile trace.js.
""",
u"""
Properly switch tracer on and off depending on loopEdge and abort signaling from trace recorder recording functions.
""",
u"""
Re-integrate trace recording and trace activation infrastructure. Model more closely after Tamarin.
""",
u"""
Create a stub for each opcode in TraceRecorder and invoke them from the stubs that are pointed to by the recorder dispatch-table.
""",
u"""
Extend dispatch table to include 256 extra cases for traceing.
""",
u"""
Switch back to mozilla-central jsinter.cpp. Lets try a different approach to attach the tracer to the interpreter.
""",
u"""
Sync with mozilla-central.
""",
u"""
Avoid name clash between nanojit and jsinter.cpp (full patch queued up for tamarin).
""",
u"""
Fix unnecessary type prefix (reported by bc, doesn't pass gcc 4.2.3)
""",
u"""
Added dmod builtin and flag broken builtins for removal (shaver).
""",
u"""
Support recording of ValueToECMAInt32, ValueToECMAUint32 and ValueToBoolean.
""",
u"""
VOIDs hang out in the BOOLEAN value space, so we have to treat them like a boolean on the trace. For ValuetoECMAInt32 all special boolean values except TRUE produce 0, and TRUE produces 1. Use a conditional move to implement this.
""",
u"""
Introduce a VMSideExitInfo structure (holds the exit typemap only for now).
""",
u"""
Fix returning from trace execution into the interpreter.
""",
u"""
Shortcut the wait time to activate fragments after compiling a new fragment.
""",
u"""
Use fragmento to track fragments and add proper trace activiation code.
""",
u"""
Fix unstable trace rejection for optimized build.
""",
u"""
Fix type stability check.
""",
u"""
Add type stability check for loop variables. Rename readstack to import.
""",
u"""
Removed attempt to imply ints into doubles on the fly. This can't work. Use proper float loads where needed and add some initial code for builtin functions.
""",
u"""
Add a vmprivate field to the guard record (queued for review upstream).
""",
u"""
Indicated in a separate primitive when integers get stored as a double because they don't into a jsval.
""",
u"""
Backed out changeset 745089a5d1c5
""",
u"""
no need for rooting of integer values
""",
u"""
This patch eliminates ValueToECMAInt32 and instead tries to emit specialized code depending on the true type. 32-bit integers are detected and treated like integers in fetch_int via ValueToECMA32. Similarly, int store_int NewIntInRootedValue is used if the value is really an underlying int. NewIntInRootedValue is a nop on the trace.
""",
u"""
Flag ints as type INT in the incoming context if its merely a double holding an int that was too large to fit into jsval directly. Along the side exits make sure we can properly box oversized ints (by casting them to doubles). The fetch_int/store_int paths still need fixing to ensure that values are merely passed through (prim_copy) instead of explicit casting or calling to ValueToECMAInt32 etc.
""",
u"""
Don't allocate 16MB code cache at startup. Instead use an exponentially increasing growth factor.
""",
u"""
Generate proper overflow detection code. Requires a trivial fix in nanojit (included, pending review to be pushed upstream).
""",
u"""
Fix circular dependency in makefile.
""",
u"""
use floating point LIR for dealing with doubles
""",
u"""
Merge.
""",
u"""
Create type maps during trace entry and in each side exit and store them in the LIR using LIR_skip. Use these type maps during trace entry and exit.
""",
u"""
beginning of trace-capability regression minisuite; will crash you today!
""",
u"""
snprintf takes sizeof buffer.
""",
u"""
Sync up with TT tip.
""",
u"""
Merge.
""",
u"""
Fix deallocation bug in the recorder. We will have to lift more code Tamarin's Interpreter to stabilize the recording.
""",
u"""
Better naming (MARK_EXIT => MARK_REGS).
""",
u"""
Assembler requires that guard be on a cmp, so force that
""",
u"""
fix frame offset calculation for args, I think also non-entry frames
""",
u"""
label arg/var/stack/sp/state for easier trace-reading
""",
u"""
Save the VM registers into markRegs at opcode entry and restore that state when ending or aborting recording. The same info is pushed into sideexit and used by guards. With this change we can eliminate the hack in MONITOR_BRANCH that had to adjust the stack pointer depending on the opcode type, and it also allows us to trace through the recently added boolean guard opcode fusing. This improves trace code quality, since only the pre-conditional check state is saved. The guard restores into that state, so the trace code doesn't have to emit the value of the conditional evaluation onto the stack, saving a handful ops.
""",
u"""
Rework memory management, don't leak memory in the filter pipeline.
""",
u"""
Save the side exit state at entry in to the opcode (since we want to restart ops) and enable store filter.
""",
u"""
Sync with TT-tip.
""",
u"""
Cleanup memory management. Use new char[] inside our overloaded new operator that clears out memory.
""",
u"""
Use #ifdef DEBUG instead of VERBOSE.
""",
u"""
Must use (&gc) new otherwise memory doesn't get cleared (found by danderson).
""",
u"""
Housekeeping (add comments, removed some dead code.)
""",
u"""
synthesize LIR_ne using LIR_eq instead of LIR_ugt, per edwsmith's wisdom
""",
u"""
Mockup of trace execution. Speedup is 10x for a tight loop. Keep in mind that this is a hack and the trace code is not optimized yet.
""",
u"""
Execute trace code. Boxing back the side exit state is not handled yet.
""",
u"""
Fix native frame addressing (reported by vlad.)
""",
u"""
Disable fusing of conditional check and branch when recording.
""",
u"""
When a conditional branch instructions terminates the trace, we have to make sure its restartable, so put the conditional value it was deciding on back onto the stack by incrementing sp before jumping back to the outer interpreter.
""",
u"""
Initialize jump table when side-entering the interpreter. Keep track of cx and sp directly in the recorder instead of going through the tracker.
""",
u"""
Guard inside the clause, not seperately.
""",
u"""
guard on inlined branch in TRY_BRANCH_AFTER_COND
""",
u"""
Merge with mozilla-central as of c5dc9d84d476, and restore obj-to-boolean fixes
""",
u"""
Remember JSContext instead of trying to keep track of frame pointer.
""",
u"""
Cleanup trace abort/end code.
""",
u"""
Make internal form of nativeFrameSize private.
""",
u"""
Merge.
""",
u"""
Rewritten frame management. Use cx->fp->regs chain instead of direct passing of those structures.
""",
u"""
fix typo in DoIncDec leading to script termination
""",
u"""
Implement icmp_ne (in terms of LIR_ugt(i, 0)!) and make JSOP_NE traceable.
""",
u"""
avoid trace-troubling temporaries via cast gymnastics
""",
u"""
Hook up pc and sp to the tracer in order to generate proper PC/SP adjustment code.
""",
u"""
Move obj_is_xml into interp since its not a primitive.
""",
u"""
Merge.
""",
u"""
Small cleanups and licensing blurb housekeeping.
""",
u"""
More work on tracing EQUALITY_OP.  Still need to synthesize LIR_ne before it
""",
u"""
abort tracing if we see an XML object in an equality op
""",
u"""
Add guards for XML objects, and some tracer bits to accommodate them.
""",
u"""
Merge.
""",
u"""
Move recorder initialization into TraceRecorder and encapsulate its state.
""",
u"""
Add a way to calculate the current size of the native frame.
""",
u"""
merge
""",
u"""
rename ENABLE_TRACER to TRACING_ENABLED and explicitly parameterize on cx
""",
u"""
More concise conversion from object to boolean.
""",
u"""
Clarified argument names in guard code and explain better why we guard for overflow the way we do.
""",
u"""
Added missing > which has been bugging me for the past month every time I saw it.
""",
u"""
Instead of guarding on null -> boolean conversion just emit a null compare and use the boolean result.
""",
u"""
Throw out a bunch of primitives (guards) that we are no longer interested in.
""",
u"""
Add a new option -j to enable the JIT. The default is off so we can easily benchmark the overhead without the tracer.
""",
u"""
Prepare LIR_ov to be used as soon Ed adds it and add a few comments that explain how overflow is handled.
""",
u"""
More cleanup and code move into TraceRecorder and prepare for LIR_ov.
""",
u"""
Slight cleanup of the guard code emission in the trace inlines.
""",
u"""
Move the recorder functionality into TraceRecorder to unclutter trace inlines.
""",
u"""
Move set/get into recorder and introduce init.
""",
u"""
Moved loading context slots into the recorder (more to follow).
""",
u"""
Make sure nativeOffset uses 64-bit slots on the native stack.
""",
u"""
Turn macros into inline functions and start prepatations for inlining function calls.
""",
u"""
Drop JS prefix from classes related to traceing.
""",
u"""
Merge.
""",
u"""
Backed out changeset fa82b7eda72a
""",
u"""
Removed debug printfs from tracker.
""",
u"""
Allocate recorder dynamically to avoid having a vtable in the struct holding the reference. Emit writebacks for every update to the tracker, not just stack writes.
""",
u"""
Parameterize tracker.
""",
u"""
Fixed malloc/delete mismatch (Valgrind was complaining)
""",
u"""
Fix a bug in tracing can_do_fast_inc_dec (wasn't tracking a copy and traced incorrect code). Merge with TT tip.
""",
u"""
Removed debug code.
""",
u"""
Merge.
""",
u"""
Merge.
""",
u"""
Add license block-comment, expand tabs.
""",
u"""
Random style nit-picking.
""",
u"""
Added example code for tracing.
""",
u"""
Don't setup debugging data structures when not debugging.
""",
u"""
Removed old comments that are no longer correct.
""",
u"""
Check at runtime that fast inc/dec is possible.
""",
u"""
Eliminate boxing in trace code. To execute such traces all values on the stack must have the same type at execution time as at trace time. Code to detect and enforce these types will be added next.
""",
u"""
Write back stack/local variable state in the trace code and improved redundand boxing/unboxing elimination.
""",
u"""
Added end-of-trace detection and make sure trace loops back to the loop header.
""",
u"""
Fix guard code assembly. This code generates trace code for the first time.
""",
u"""
Mork work on attaching nanojit to our primitives. Traces have now their own box type (Box), which is an opaque 64-bit value. Its never supposed to appear in the trace since we will optimize away all boxing operations.
""",
u"""
Start attaching our tracer to nanojit. This is incomplete and meant for review by David only.
""",
u"""
Fixed the test case not setting the lastIns value in Fragment
""",
u"""
Fixed _thisfrag not being set in beginAssembly
""",
u"""
Fixed beginAssembly() not setting _thisfrag which verbosity requires
""",
u"""
Backed out changeset b142c62e7602
""",
u"""
Back out explicit zeroing in the constructor and ensure heap allocated objects are implicitly zero-ed out.
""",
u"""
Fixed cases of the tests not prepping the tracer properly for verbosity
""",
u"""
fixed constructor relying on zero'd allocation
""",
u"""
fixed memory corruption in verbosity initialization code
""",
u"""
use valloc() on Darwin for GCHeap
""",
u"""
fixed code generation for the LIR_in -> LIR_param change
""",
u"""
Properly align pages allocated by GCHeap.
""",
u"""
Switch to malloc (avoid new where possible) and properly initialize capacity.
""",
u"""
Added danderson's test cases for nanojit. Execute with nanojit() from JS shell.
""",
u"""
Added hook to trigger nanojit test code from the JS shell.
""",
u"""
Drop helper code that is no longer needed.
""",
u"""
Added necessary glue code to make nanojit compile in DEBUG mode.
""",
u"""
Landed nanojit in TraceMonkey. This is untested and DEBUG must be off for now since we don't support AVM's String class.
""",
u"""
Added Assembler.h and vm_fops.h (blank for now) from TT.
""",
u"""
Added RegAlloc.h and Fragmento.h from TT.
""",
u"""
Added LIR.h from TT.
""",
u"""
Added Native*.h from TT.
""",
u"""
Added nanojit.h from TT.
""",
u"""
Renamned avm.h to avmplus.h
""",
u"""
Added BitSet data structure for nanojit.
""",
u"""
Rewrite AVM's data structures to work within spidermonkey to create an environment that allows us to land nanojit in SM.
""",
u"""
Make fast inc/dec traceable.
""",
u"""
Added new primitive guard_can_do_fast_inc_dec and report reason for trace aborts.
""",
u"""
More work on the recorder.
""",
u"""
Fixes to the trace recorder.
""",
u"""
Merge.
""",
u"""
Fix slew of gcc warnings, clear pending exception before triggering recorder error.
""",
u"""
Call into the recorder for each primitive. Don't use vp in primitives, use &v instead.
""",
u"""
Notify the recorder of all primitives as they are recorded. If the recorder doesn't support a primitive we abort the trace. In debugging mode this also stops the VM.
""",
u"""
Merge with be's last push.
""",
u"""
native_pointer_to_jsval should not lose low-order bits (plus random style nits).
""",
u"""
Initialize ok to true if we didn't side-enter via state.
""",
u"""
Use an error property in the recorder instead of a return value to indicate errors and make sure DO_OP aborts the trace once we go into the error state in the tracer.
""",
u"""
js_CallRecorder has no return value any more.
""",
u"""
Track data flow through variables in the recorder. Set an error flag if the recorder signals an error.
""",
u"""
Fix used before set ok bugs, fiddled ifdef style a bit.
""",
u"""
Expand tabs.
""",
u"""
Kill trailing spaces.
""",
u"""
Start hooking the recorder into the tracer.
""",
u"""
Pass JSContext* to all primitives (needed by the recorder.)
""",
u"""
Allow recorder to abort recording.
""",
u"""
Save and restore ok when switching interpreters.
""",
u"""
Init ok before goto exit, plus indentation style policing.
""",
u"""
Cleanup and fixed beneign bug.
""",
u"""
Notify recorder when tracing starts/stops. Restore code accidently lost during last merge.
""",
u"""
Connect tracer with the interpreter. Errors and exits are handled in the main interpreter.
""",
u"""
Merged with Brendan's changes.
""",
u"""
No need for eval call.
""",
u"""
Minimize JSInterpreterState, fix warning.
""",
u"""
Added code to switch to the tracer and back. Incomplete and for review only.
""",
u"""
Style nits, plus no need for rt in JSInterpreterState.
""",
u"""
Create a side-entry path into the interpreter that bypasses the initialization code and allows switching back and forth between two interpreters (i.e. tracing and non-tracing).
""",
u"""
Added branch monitoring using a single unified branch frequency counter.
""",
u"""
Removed JSOP_HEADER code. Its too costly. This patch restore essentially the same performance as unmodified SM.
""",
u"""
Disable JSOP_HEADER counting.
""",
u"""
Use higher optimization settings for jsinterp.cpp to ensure inlining.
""",
u"""
Fixed typo that caused sunspider to fail.
""",
u"""
Merge.
""",
u"""
Backed out value_to_iter inline method extraction.
""",
u"""
Backed out do_dorinloop inline method extraction.
""",
u"""
Backed out extraction of code from the interpreter loop as inline method.
""",
u"""
Transform do_dorinloop goto/fall through hack into a proper inline method.
""",
u"""
Convert value_to_iter goto/fall through hack into a proper inlined method.
""",
u"""
Fix firefox, etc., (top-level mozilla) builds.
""",
u"""
Merge.
""",
u"""
First stage of loop table work; bitmap free space management and GC hook-up still to come.
""",
u"""
Fix decompiler (hack, really) to cope with misplaced JSOP_HEADER in update part of for(;;) loop.
""",
u"""
Merge, simplify names, and police style.
""",
u"""
JSOP_HEADER takes a byte index of loop header counting from script->loopBase, and related changes.
""",
u"""
Fix ReconstructPCStack oplen code, extend js_OpLength to avoid cs recalculation where possible.
""",
u"""
Introduced a JavaScript recording script that is loaded dynamically.
""",
u"""
Store the recorder script in JSTraceMonitor and make sure its traced by the GC. Also clean up the tracing of JSTraceMonitor.
""",
u"""
Backed out changeset 3029f4d57bd2
""",
u"""
Switch to a uniform style for jstracer.cpp.
""",
u"""
Add location in the context where we can hold the recorder script and make sure the GC traces it.
""",
u"""
Remove InitTacer. Pointless for JSRuntime.
""",
u"""
Compiler fixes for CAS patch.
""",
u"""
Fix so it compiles, also avoid else after return.
""",
u"""
Make js_CompareAndSwap visible outside jslock.cpp.
""",
u"""
Move all inlines that do not represent primitives out of jsinterpinlines.h since we don't have to overwrite them in jstracerinlines.h. They live in jsinterp.cpp now. Added missing error handling for prim_ddiv and prim_dmod. Make sure prim_ddiv and prim_dmod do not call other primitives. Fixed bug in dmod (-1 should be n, but since all invocations had n=-1 this was a non-issue).
""",
u"""
Fiddle loop table slot interface and impl in hope of freeing slots over time.
""",
u"""
Use correct idempotent include guard macro name.
""",
u"""
Merge and undo js_AllocateLoopTableSlot reparam.
""",
u"""
No JS_TRACER ifdefs, keep line len < 80, reparameterize jstracer.cpp functions, js_OpLength helper.
""",
u"""
Avoid overlong lines per modeline comments.
""",
u"""
Merge, style nits, no locking for tracing.
""",
u"""
Left brace style.
""",
u"""
Fix goof in switching from word to jsval counters.
""",
u"""
Instrument loop headers with jsvals above fp->vars and below fp->spbase.
""",
u"""
Split trace-supporting inlines, add ifdefs/macros for deriving js_TracingInterpret in jstracer.cpp.
""",
u"""
Style (and substance for vim users: left brace opening in column 1 enables 
""",
u"""
Assign fresh loop table slots for all JSOP_HEADER opcodes in a script as it is thawed since the slots we stored there are likely stale by now.
""",
u"""
Fixed a bug that triggered the tracer at TRACE_THRESHOLD/2 already.
""",
u"""
The table is now per-thread in a multi-threaded environment, and per-runtime otherwise. During code generation we merely allocate a loop table slot to each loop. Each thread will enlarge the table as needed in JSOP_HEADER.
""",
u"""
Add a per-runtime loop attribute table that associates a jsval attribute with every loop in the code. The jsval is used initially as a counter until a certain threshold is reached, at which point the loop is traced and compiled and the resulting native code object is stored in the jsval to be executed for future encounters of the loop.
""",
u"""
Steer macro naming in jsinterinlines.h using a macro. This allows us to prefix all primitives with some prefix (i.e. interp_) when we compile the tracer and replace them with new primitives that invoke the interpreter version first, and then do some tracer specific action.
""",
u"""
Fix goof in switching from word to jsval counters.
""",
u"""
Instrument loop headers with jsvals above fp->vars and below fp->spbase.
""",
u"""
Split trace-supporting inlines, add ifdefs/macros for deriving js_TracingInterpret in jstracer.cpp.
""",
u"""
Style (and substance for vim users: left brace opening in column 1 enables  navigation).
""",
u"""
Make relational operations (<,<=,>,>=) traceable.
""",
u"""
Mark getting and setting arguments and local variables as safe for tracing.
""",
u"""
Make branch instructions traceable using a new primitive guard_boolean_is_true.
""",
u"""
Enable tracing for selected opcodes that do not have any remaining tracing hazards.
""",
u"""
Opcodes that can be traced through can be declared with TRACE_CASE(op). Currently all opcodes are declared as BEGIN_CASE(op), which automatically aborts trace recording. In addition, error handlers (defined with DEFINE_HANDLER) also abort trace recording. At every backwards branch trigger monitor_branch(), which will monitor for new trace tree anchors.
""",
u"""
Introduce primitives for common binary operations.
""",
u"""
Convert macro code in jsinterp.cpp into inline functions and introduce trace primitives (prim_*, guard_*, call_*).
""",
u"""
From Igor's patch for .
""",
u"""
Fix bad merge.
""",
u"""
Igor's patch for , r=me.
""",
u"""
Fix POP_STACK to take a macro out param.
""",
u"""
First round of macro cleanups to enable tracing.
""",
u"""
Igor's fix for , r=me.
""",
u"""
Fix for , r=igor.
""",
u"""
Backed out changeset af00b3f27c64 ()
""",
u"""
- Don't allow shorthand object initializer through destructuring assignment. r=brendan
""",
u"""
Backing out changeset cf6c811e1272 () due to debug assertions.
""",
u"""
- DOM quick stubs - faster paths for top N DOM methods (r+sr=jst, security r=mrbkap, build r=bsmedberg)
""",
u"""
Use host outoption for host binaries r=mrbkap
""",
u"""
- JS_GetScopeChain and JS_NewScriptObject should CHECK_REQUEST(cx) (r=crowder)
""",
u"""
- Allow getting the 'prototype' property through SJOWs. r=jst sr=bzbarsky
""",
u"""
- caching enumerators to speedup for-in loops. r=brendan
""",
u"""
. Merging the mozilla-qt repository. r=me,vlad
""",
u"""
merge with mozilla-central
""",
u"""
mozilla-central merge
""",
u"""
Merging mozilla-central to mozilla-qt.
""",
u"""
- Null check the right variable. r=igor
""",
u"""
- "XPConnect doesn't always suspend requests when switching contexts". r+sr=jst.
""",
u"""
JavaScript Tests - trace mini test suite, 
""",
u"""
Sisyphus - add ecma_3_1, js1_8_1 and new JavaScript options
""",
u"""
Sisyphus - Allow universe.data to be overridden by environment variable
""",
u"""
JavaScript Tests - clean up contributors on boilerplate shell.js files, no bug
""",
u"""
JavaScript Tests - update template copyright dates, no bug
""",
u"""
JavaScript Tests - update tests for , r=Mike Kaplinskiy
""",
u"""
JavaScript Tests - add ecma_3_1, js1_8_1 suites, 
""",
u"""
JavaScript Tests - update test machine universe, no bug
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
Create implicit XPCNativeWrappers in fewer situations. , r=jst sr=bzbarsky
""",
u"""
Make split global objects have the right flags. , r=crowder NPOTB
""",
u"""
Merge commit for 
""",
u"""
JavaScript Tests - remove obsolete import|export tests for trunk, 
""",
u"""
- "FindInJSObjectScope calls JS from within a request and a lock". r+sr=jst.
""",
u"""
- "Protect against null objects in a title's scope/map". r=brendan.
""",
u"""
- removal of minarg support for fast native
""",
u"""
JavaScript Tests - regression test for , by Oliver Hunt
""",
u"""
, remove the import/export functionality from spidermonkey, r=brendan
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for 
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Jason Orendorff
""",
u"""
JavaScript Tests - regression test for , by Ben Turner
""",
u"""
JavaScript Tests - regression tests for , by Cyrus Omar
""",
u"""
JavaScript Tests - regression tests for , by Cyrus Omar
""",
u"""
JavaScript Tests - regression tests for , by romaxa, Igor Bukanov
""",
u"""
JavaScript Test - binary operator evaluation order, 
""",
u"""
: fix --enable-dtrace, r=igor
""",
u"""
JavaScript Tests - regression test for  , by nanto_vi (TOYAMA Nao), Jesse Ruderman
""",
u"""
- merging var and local JS bytecodes. r=brendan
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Rob Sayre
""",
u"""
JavaScript Tests - regression test for , by Brian Crowder
""",
u"""
- js_CheckAccess should init out params on failure, r=brendan
""",
u"""
JavaScript Tests - modify test for BOM to whitespace conversion, 
""",
u"""
JavaScript Tests - regression test for , by Philip Taylor
""",
u"""
- update jsdtoa with interesting pieces of more-recent dtoa, r=igor
""",
u"""
Try to fix the orange by overriding platform-specific errors
""",
u"""
Fix missed review comment from 
""",
u"""
Propagate compilation errors to our caller to make syntax errors easier to debug. , r=shaver sr=brendan
""",
u"""
Implement ES3.1's Object.getPrototypeOf. , r=brendan
""",
u"""
let declarations at top level and function level should not shadow var. , r=brendan
""",
u"""
Don't pass around information we don't use. , r=brendan
""",
u"""
Cleanup error reporting in dis and dissrc. , r=brendan
""",
u"""
Merge backout
""",
u"""
Backed out changeset 90020c4ad446 to fix tinderbox orange while I figure out why a test was failing.
""",
u"""
Don't optimize variable names in with statements. , r=brendan
""",
u"""
Propagate compilation errors to our caller to make syntax errors easier to debug. , r=shaver sr=brendan
""",
u"""
, js hooks to control vtune, r=sayrer
""",
u"""
- re-enable OJI for Firefox 3.1, the configure changes is from jst, r=jst,crowder, sr=benjamin
""",
u"""
- fixing -Wformat warnings in debug printouts. r=crowder
""",
u"""
- fixing js shell compilation issues on Windows caused by my changes from the . r=bclary, not-part-of-the-build
""",
u"""
Backed out changeset 65836af09dac - compilation errors
""",
u"""
- fixing -Wformat warnings in debug printf code. r=crowder
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
: fix build with JS_HAS_SCRIPT_OBJECT, r=mrbkap
""",
u"""
merging backout
""",
u"""
Backed out changeset a5fc387c4622
""",
u"""
- allow to override the object dir when building js shell. r=crowder
""",
u"""
Fixing a typo in a comment.
""",
u"""
- Updating dtoa from David M. Gay's latest code, and refactoring to
""",
u"""
- Number.toLocalString() doesn't handle Infinity or exponential notation correctly, r=mrbkap
""",
u"""
- fixinge makefile for js shell to handle parallel make invocations. r=crowder, not-part-of-the-build.
""",
u"""
Sisyphus|JavaScript Tests - add repository information to failure tracking, 
""",
u"""
Sisyphus|JavaScript Tests - update public failures, 
""",
u"""
Space nit fix.
""",
u"""
Backed out changeset 084567d3ebe6. It actually made us not comply with ECMAScript 3.
""",
u"""
Attempt to make XPC_XOW_ClassNeedsXOW faster. , r=jorendorff/jst sr=jst
""",
u"""
Calculate the time zone offset correctly. , r=mrbkap
""",
u"""
Merge commit for 
""",
u"""
- patch from romaxa to fix NativeCompareAndSwap implementation on ARM. r=myself
""",
u"""
merge
""",
u"""
Landing fix for . JS_GC with GC_SET_SLOT_REQUEST doesn't loop until all threads are satisfied. Patch by brendan@mozilla.org, r=bent.mozilla@gmail.com
""",
u"""
Landing fix for . Make the JS component loader use the JS context stack so that pending requests are suspended while components load. Patch by bent.mozilla@gmail.com, r+sr=jst@mozilla.org
""",
u"""
Sisyphus|JavaScript Tests - allow user to execute tests from other location than TEST_DIR, , r=cbook
""",
u"""
Always select gvar ops for declared global vars, instead of only if loopy/enough-used (445901, r=shaver).
""",
u"""
- Delete dead code in JSObject2NativeInterface hot path (r+sr=jst)
""",
u"""
Fix property cache fill to use the best shape (445899, r=shaver).
""",
u"""
- eliminating JSStackFrame.(nvars|vars). r=brendan
""",
u"""
[] Fixing GCC conversion warnings within SpiderMonkey. r=brendan
""",
u"""
[] Fixing GCC warning on x86-64 about redefined HAVE_VA_LIST_AS_ARRAY. r=crowder
""",
u"""
[] Using explicit assembly to implement compare-and-swap on x86-64 to avoid __sync_bool_compare_and_swap (GCC intrinsic) as the latter is buggy at least on ARM. r=brendan
""",
u"""
Property-cache JSOP_NAMEINC etc. direct slot case (445893, r=shaver).
""",
u"""
Backed out changeset 5c009a853d70 for hitting a fatal JS_Assert during xpcshell unit tests (xpcom/unit/test_bug374754.js) on the DO_NEXT_OP(JSOP_INCNAME_LENGTH) line on !JS_THREADED_INTERP platforms (Windows).
""",
u"""
Property-cache JSOP_NAMEINC etc. direct slot case (445893, r=shaver).
""",
u"""
JavaScript Tests - update public-failures and universe.data to include mozilla-central 1.9.1 branch, remove unsupported machine configurations, 
""",
u"""
Sisyphus - JavaScript Tests - add detect-universe.sh, 
""",
u"""
- BOM characters are stripped from javascript before execution
""",
u"""
- Add JSAutoSuspendRequest to match JSAutoRequest
""",
u"""
[] optimizing E4X constructor calls. r=brendan
""",
u"""
- Migrate js/src/README.html to developer.mozilla.org (r=brendan)
""",
u"""
[] jsinterp.cpp source no longer split between 2 compilation units when compiling on Windows. r=brendan
""",
u"""
[] js_(Lock|Unlock) are defined as external non-inline functions to prevent linkage errors with js shell. r=brendan
""",
u"""
Test that the object has the right class, even when called from native code. , r=shaver
""",
u"""
[] implementing compare-and-swap for 64-bit Linux. r=brendan
""",
u"""
Tab removal. No bug, NPOTB.
""",
u"""
, fix standalone js shell build on windows, r=crowder
""",
u"""
dis and dissrc throw not-exceptions when passed invalid arguments. , r=shaver
""",
u"""
- "Remove MOZILLA_1_8_BRANCH ifdefs from core on trunk" [r=sicking r=brendan r=bsmedberg]
""",
u"""
- "Additional cache XPCPerThreadData for mainthread" [r=dbradley sr=brendan]
""",
u"""
- "xpcshell doesn't properly report error messages" [p=mh+mozilla@glandium.org (Mike Hommey) r=brendan]
""",
u"""
Landing fix for . Make XPCWrappedJS destruction threadsafe. Patch by bruno@flock.com and manish@flock.com, r+sr=jst@
""",
u"""
Sisyphus - documentation, 
""",
u"""
JavaScript Tests - update public failures, universe data, 
""",
u"""
, Add JS functions to stop/start callgrind, r=sayrer
""",
u"""
JavaScript Tests - remove unreliable test machines from test universe, update public-failures.txt, universe.data, 
""",
u"""
Follow the invariant that we flow through label exit2. , r=igor
""",
u"""
[] Optimized shell uses the same options as the the non-debug browser build. r=mrbkap, not-part-of-browser-build
""",
u"""
Don't use 'i' if the id was not an index. , r=shaver
""",
u"""
Don't do things to the object before we're sure it's the right type of object. , r=brendan
""",
u"""
- Optimizing the enumeration state allocation. r=brendan
""",
u"""
JavaScript Tests - regression test for , by timeless
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - update public failures, 
""",
u"""
Merge commit for 
""",
u"""
Sisyphus - JavaScript Tests - generalize std::bad_alloc -> out of memory post processing, 
""",
u"""
Javascript Tests - do not require js tests to be on path, 
""",
u"""
JavaScript Tests - update public-failures.txt, universe.data 
""",
u"""
JavaScript Tests - reportCompare doesn't print description on failures, , patch by x00000000@freenet.de, r=igor
""",
u"""
fix circular dependency on jscpucfg.h
""",
u"""
Clean up for-in ops and naming nit (443039, r=igor).
""",
u"""
- remove eval's optional second argument, r=brendan
""",
u"""
Eliminate useless genexp for(;;) conditions (442342, r=jorendorff).
""",
u"""
- Assertion failure: *vp != JSVAL_HOLE, r=shaver, r=brendan
""",
u"""
- Cannot accurately watch the 'length' property of arrays, r=shaver
""",
u"""
- Accessors in prototype chain of arrays don't assign 'this' correctly, r=shaver, r=brendan
""",
u"""
[] SM: faster js_PutCallObject, r=brendan
""",
u"""
[] SM: fixing INT_FITS_IN_JSVAL on 64 bit platforms
""",
u"""
Don't cause a GC before the script is on the JS call stack. , r=brendan
""",
u"""
: Added -fno-exceptions and -fno-rtti to Makefile.ref
""",
u"""
Fix for(;;) loops to use one branch per iter (after initial iter; 441477, r=jorendorff).
""",
u"""
Turn off these noisy and now mostly useless printfs for me. No bug, NPOTB
""",
u"""
Fixing . Don't GC when replacing safe contexts. r+sr=brendan@mozilla.org
""",
u"""
Sisyphus/JavaScript - update to support 1.9.1, 
""",
u"""
Fixing a comment spacing nit.
""",
u"""
- dense arrays yield bogus __count__ values, r=shaver
""",
u"""
- Crash [@ Decompile][@ js_GetSrcNoteOffset] with firebug/jQuery, r=igor
""",
u"""
JavaScript Tests - correct test typos, 
""",
u"""
JavaScript Tests - update statistics handling in test, by jorendorff
""",
u"""
- jsutil.cpp does not compile with Visual Studio 2003. r=crowder
""",
u"""
Make the shell's -z option work again. , r=crowder
""",
u"""
Do not attempt to lock a non-native object. , r=brendan
""",
u"""
[] SM: JSVAL_VOID as a pseudo-boolean. r=brendan
""",
u"""
Fix 433672, r=igor, a=shaver.
""",
u"""
Backed out changeset 79c0748ff2ac.
""",
u"""
[] Fixing ICC compilation issue: in goto *expr the type of expr should be void*. r=sayrer
""",
u"""
- Deprecate JS_NewDouble and JS_NewDoubleValue, add correctness assertions (r=brendan)
""",
u"""
- Assertion failure: JS_PROPERTY_CACHE(cx).disabled >= 0, at jsinterp.c:463 using js.c Scatter() test and gczeal(2) (r=brendan)
""",
u"""
[] backing out to investigate the tinderbox leak problem
""",
u"""
- "Live-lock when running JS on multiple threads". r=brendan.
""",
u"""
Make CallTree compile with a C++ compiler. , r=shaver
""",
u"""
Make PrincipalHolder threadsafe since it can be destroyed from off-thread (thanks to XPCSafeJSContexts) and no additional work is required to make it threadsafe. , r+sr=jst
""",
u"""
Make XPCNativeWrapper deal with non-browser embeddings. , r+sr=jst
""",
u"""
fixing initialization issue with JSGCFreeListSet
""",
u"""
trunk sync
""",
u"""
Updating for mozilla-central
""",
u"""
Fix bustage caused by over-aggressive TRY_BRANCH_AFTER_COND in STRICT_EQUALITY_OP (used by JSOP_CASE*).
""",
u"""
Fuse branch after relational or equality op (363534, r=igor).
""",
u"""
: Add jemalloc_stats() and jemalloc.h, r=benjamin
""",
u"""
[] More efficient interpreter switch when computed goto is not available. r=brendan
""",
u"""
Backed out changeset 97977f224aff due to build breakage
""",
u"""
[] More efficient interpreter switch when computed goto
""",
u"""
Backed out changeset 21527193c49b: the patch has used CSRCS, not CPPSRCS.
""",
u"""
[] More efficient interpreter switch when computed goto is not available. r=brendan
""",
u"""
: Remove unused directory  "js/src/fdlibm". r+a=shaver
""",
u"""
Fix old assignment expression rval mutation via getter design, optimize setprop;pop and similar cliches (312354, r=igor).
""",
u"""
Fix bogus js_Emit return value tests (438986, r=igor).
""",
u"""
Backed out changeset f201baf7bf04 (), was causing unit-test failures
""",
u"""
[] renaming decltype to declType as the former is a keyword in the next C++ standard.
""",
u"""
: xpcshell's load() just silently fails for non-existent files, r=brendan, sr=jst
""",
u"""
Removing Minimo references.  b=405705, r=ted
""",
u"""
Backout changeset 1f599577eca2 () due to mochitest failures
""",
u"""
: optimize string.replace for flat strings; r=brendan
""",
u"""
- Live JSScripts can be destroyed by script-object finalizer (r=brendan)
""",
u"""
- cannot convert __va_list_tag** to __va_list_tag (*)[1] in jsapi.cpp building js shell (r=crowder+bclary)
""",
u"""
Hack off fix for 260106, it results in interpreter stack imbalance on windows.
""",
u"""
Third and final followup patch for .
""",
u"""
Followup patch for .
""",
u"""
Fix 260106, r=shaver.
""",
u"""
: fix --enable-shark for C++ build; r=brendan
""",
u"""
b=429387, add --with-arm-kuser; use it in JS, and pass it down to NSPR's configure; r=shaver,r=ted
""",
u"""
- Decide what to do with js.mak (answer: delete it, r=crowder, a=bsmedberg)
""",
u"""
- Link errors building JS shell on WinXP (actually a documentation bug in js/src/README.html) (r=brendan, a=bsmedberg)
""",
u"""
Running xpcshell tests involving Mac components leaks memory due to not having an NSAutoreleasePool. r=shaver,sr=brendan
""",
u"""
Merge cvs-trunk-mirror to mozilla-central up through FF3RC2build2
""",
u"""
: use jemalloc on Solaris, r=ted, a=shaver
""",
u"""
[] proper stacking of JS_(PUSH|POP)_TEMP_ROOT. r=brendan aRC2=shaver
""",
u"""
Fixing . Fix GC safety issue when calling through XPCWrapper into an IDL defined function. r+sr=brendan@mozilla.org, a=shaver@mozilla.org
""",
u"""
Fixing . Make calls through XPConnect on threads other than the main thread suspend JS request to avoid blocking GC on the main thread while calling slow functions on non-main threads. Patch by benjamin@smedbergs.us and jst@mozilla.org, r=jst@mozilla.org, sr=brendan@mozilla.org, a=schrep@mozilla.com
""",
u"""
Fix 433279, r=mrbkap+shaver, a=schrep.
""",
u"""
Patch from nanto@moon.email.ne.jp for misordered alternates in string-lexing regexp, and lack of IE /[/]/ compat in regexp-lexing regexp (433831, r=me, NPOTB).
""",
u"""
- mozilla-central: js/src/Makefile.ref calculates .d filenames incorrectly (r=crowder, a=bsmedberg)
""",
u"""
Return to building spidermonkey as C++, because we believe we found the cause of the perf regression elsewhere (non-code).
""",
u"""
Back out JS-as-C++, because it's a suspect in the Linux performance regression.
""",
u"""
Back out revision bd9c9cbf9ec8 (build spidermonkey as C++) for perftesting and profit.
""",
u"""
- dtrace build fixes for C++ linkage, r=jorendorff
""",
u"""
JavaScript Tests - update test and remove from exclusion list, , r=jorendorff
""",
u"""
JavaScript Tests - add unary - tests for 
""",
u"""
- "jsfun.h uses JSArenaPool without needed typename" [p=mh+mozilla@glandium.org (Mike Hommey) r=brendan a1.9=damons]
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
- "AIX linker error for trunk build xpconnect module : ERROR: Undefined symbol: .JSAutoTempValueRooter::operator delete(void*,unsigned long)" [p=shailen.n.jain@gmail.com (Shailen) r+sr=mrbkap a1.9=beltzner]
""",
u"""
: Regression - Java applets crashing browser [@ obj_eval], patch by mrbkap, r=crowder, a=beltzner
""",
u"""
- Regression - Java applets crashing browser [@ obj_eval], r=igor, a=beltzner
""",
u"""
- "crashes [@ nsJSIID::HasInstance][@ XPCNativeSet::FindInterfaceWithIID]". r+sr=jst, a=beltzner.
""",
u"""
Merge cvs-trunk-mirror to mozilla-central. Conflict resolution:
""",
u"""
: assertion at startup with venkman, patch by mrbkap, r=brendan, a=beltzner
""",
u"""
-- (relanding) Crash [@ DecompileExpression] with trap, r=brendan, shaver, igor; a=mtschrep
""",
u"""
Merge cvs-trunk-mirror to mozilla-central. One conflict resolution: updated NSPR tag from client.mk into client.py
""",
u"""
Sisyphus|JavaScript Tests - runtests.sh -I include conflicts with msvc include on Windows
""",
u"""
Back out patch for due to unit test failures
""",
u"""
Addressing white-space nits.
""",
u"""
[] faster js_PutBlockObject(), r=brendan a1.9=shaver
""",
u"""
- Crash [@DecompileExpression] with trap, r/a=shaver
""",
u"""
JavaScript Tests - update public failures, 
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central. No conflict resolution necessary.
""",
u"""
JavaScript Tests - test for section ecma 262-3 15.4.5.1
""",
u"""
JavaScript Tests - regression test for 
""",
u"""
Fix JSOP_GETTHISPROP decompile-value-generator bug (431248, r=igor, a=dsicore).
""",
u"""
Merge cvs-trunk-mirror to mozilla-central.  No conflicts.
""",
u"""
: The return value of some of math method of javascript is not IEEE standard on solaris, patch by Leon Sha <leon.sha@gmail.com>, r=brendan, a=damon
""",
u"""
Merge cvs-trunk-mirror to mozilla-central. No manual conflict resolution was necessary.
""",
u"""
[] r=brendan a1.9=shaver
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
Clear GetSrcNote cache in js_UntrapScriptCode (431428, r/a=shaver).
""",
u"""
[] r=brendan a1.9=dsicore
""",
u"""
[] proper handling of __noSuchMethod__ when it is invoked as constructor. r=brendan a1.9=dsicore
""",
u"""
- "Browsing on the given site and closing the tab results in no active tab and keyboard shortcuts don't work until you refocus any element". r=jst, sr=mrbkap, a=beltzner.
""",
u"""
- trap changes decompilation of "{ let X }", r/a=shaver
""",
u"""
Merge cvs-trunk-mirror to mozilla-central. Automated merge, no manual conflict resolution necessary.
""",
u"""
Fix hang when GetPropertyTreeChild calls js_GenerateShape calls js_GC (424636, r=igor, a=beltzner).
""",
u"""
[] Eliminating unused JSINVOKE_INTERNAL and JSFRAME_INTERNAL. r=brendan a1.9=dsicore
""",
u"""
Don't cache shared properties under JSOP_SET{NAME,PROP} (428282, r=igor, a=mconnor).
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - update known failures due to 
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Mike Shaver
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Mike Shaver
""",
u"""
- Removal of legacy JSLL_ routines, r=brendan, a=mtschrep
""",
u"""
JavaScript Tests - jsDriver.pl doesn't detect all test failures, 
""",
u"""
[] Making sure that all let blocks has non-zero stack depth. r=brendan a1.9=beltzner
""",
u"""
Fix '(void 0) is undefined' decompilation regression (420919, r=igor, a=dsicore).
""",
u"""
: fix lookup of incorrect ID when delegating to prototype for hole in dense array. r=mrbkap, a=mconnor.
""",
u"""
- assertion botch or bogus OOM when decompiling script with debugger trap on JOF_CALL bytecode, r=igor, a1.9=shaver
""",
u"""
JavaScript Tests - update regression tests due to 
""",
u"""
: Can't define both a getter and a setter for a property of the global object, patch by Brian Crowder <crowder@fiverocks.com>, r=shaver, r=mrbkap, a=shaver
""",
u"""
Add mochitest
""",
u"""
Landing fix for plugin hang . Fix hang on pages that script plugins. Patch by bent.mozilla@gmail.com, r+sr=brendan@mozilla.org/jst@mozilla.org, a=beltzner
""",
u"""
Add crashtest
""",
u"""
- Invalid range error for some case-insensitive regular expressions, r/a=shaver
""",
u"""
[] Backing out the patch as it depends on Getopt::Long feature that is not widely available.
""",
u"""
[] Replacing deprecated Getopt::Mixed with Getopt::Long. r=bclary, a=not-part-of-the-build
""",
u"""
Fix redness. Stupid second security manager
""",
u"""
JavaScript Tests - update public failures, 
""",
u"""
JavaScript Tests - regression tests for , by Martin Honnen
""",
u"""
JavaScript Tests - update known failures.txt, 
""",
u"""
[] Backing out to investigate startup failures
""",
u"""
[] Making sure that all let blocks has non-zero stack depth. r=brendan a1.9=beltzner
""",
u"""
JavaScript Tests - update browser emulation of gc(), by Igor Bukanov, no bug, not part of the build
""",
u"""
Merge cvs-trunk-mirror to mozilla-central
""",
u"""
JavaScript Tests -regression tests for , by x00000000
""",
u"""
JavaScript Tests - regression test for , by Gary Kwong
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, Brian Crowder
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, Gary Kwong
""",
u"""
: Assertion failure !OBJ_GET_PROTO(cx, ctor) after deleting Function, r=brendan, a1.9=shaver
""",
u"""
Merge cvs-trunk-mirror to mozilla-central.
""",
u"""
[] fixing function definition emitter. r=brendan a1.9=mtschrep
""",
u"""
bug=427185 r=brendan a1.9=mtschrep
""",
u"""
, assertion failure after deleting eval 16 times, patch by mrbkap, r=brendan, a=mtschrep
""",
u"""
backing out to investigate tinderbox orange
""",
u"""
bug=428708 r=brendan a=mtschrep fixing a bogus assert
""",
u"""
bug=427185 r=brendan a1.9=mtschrep
""",
u"""
Sisyphus|JavaScript Tests - remove spidermonkey-extensions-n.tests,  
""",
u"""
: XPCSafeJSObjectWrapper provides incorrect type information, patch by shaver@mozilla.org, r=mrbkap, a=beltzner
""",
u"""
update public-failures.txt, spidermonkey-extensions-n.tests, 
""",
u"""
Sisyphus|JavaScript Tests - up browser total timeout to 6 hours, 
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Andrew Schultz
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
global_resolve should not do anything if assigning.
""",
u"""
JavaScript Tests - further refinements of public failures, 
""",
u"""
JavaScript Tests - update public failures, 
""",
u"""
Fix 427191 (r=igor, a=beltzner).
""",
u"""
Fix regression in patch for (387951, r=mrbkap, a=dsicore).
""",
u"""
JavaScript Tests - make javascript.options.strict tests insensitive to current setting, 
""",
u"""
JavaScript Tests - attempt to catch exceptions to simplify test reporting, 
""",
u"""
Sisyphus|JavaScript Tests - Spider's userhook can be stopped by exceptions in tests, 
""",
u"""
JavaScript Tests - update known failures and spidermonkey extensions list, 
""",
u"""
Sisyphus|JavaScript Tests - add ability to run tests with gczeal, 
""",
u"""
JavaScript Tests - catch script stack space quota errors
""",
u"""
JavaScript Tests - update compatibility note, 
""",
u"""
JavaScript Tests - fix filename, 
""",
u"""
- assertion failure after deleting eval 16 times, patch by mrbkap, r=brendan, a1.9=beltzner
""",
u"""
- "Some errors not displayed in Error Console when using addEventListener". Tests by Sylvain Pasche <sylvain.pasche@gmail.com>. r+sr=jst, a=beltzner.
""",
u"""
[] r=brendan a1.9=beltzner
""",
u"""
: reverting the patch from this bug as a result of test-failures
""",
u"""
Reduce the length of the "XPConnect is being called on a scope without a 'Components' property!" assertion message ().  r=mrbkap, debug-only.
""",
u"""
Make __count__ shared as well as permanent (426711, r=mrbkap, a=beltzner).
""",
u"""
- "use JSVERSION_LATEST in xpcshell" (use a context callback to set error-reporter and jsversion default) [p=crowder@fiverocks.com (Brian Crowder) r+a1.9=shaver]
""",
u"""
- "Incorrect toString for regular expression with null character or line break" [p=crowder@fiverocks.com (Brian Crowder) r=mrbkap a1.9=damons]
""",
u"""
Allow XMLHttpRequest and document.load load files from subdirectories. r/sr=dveditz
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
report address for live contexts in JS_DestroyRuntime r=brendan a=beltzner
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Joachim Kuebart
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Brian Crowder
""",
u"""
- script stack space quota is exhausted (return of MAX_INLINE_CALL_COUNT), r=igor, blocking1.9=dsicore
""",
u"""
Sisyphus - remove hard coded path dependencies, support mozilla-build, , r=rcampbell
""",
u"""
Bustage fix for DEBUG_CC builds as a result of the fix for . r=dbaron, a=NPOTDB.
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
[] clearing property cache when thread gets the first context. r=brendan a1.9=blocking1.9
""",
u"""
[] Allocating functions together with JSObject. r=brendan a1.9=blocking1.9
""",
u"""
- "Optimize read file buffer sizes for faster startup times" [p=jmathies@mozilla.com (Jim Mathies) r=sayrer sr=bsmedberg a1.9=beltzner]
""",
u"""
- "C++ compatibilty: jsdbgapi.cpp: use of JS_malloc needs a cast" [p=jorendorff@mozilla.com (Jason Orendorff) r=brendan a1.9=beltzner]
""",
u"""
- "Use -xO4 for building js/src with Sun Studio compiler on Solaris" [p=ginn.chen@sun.com (Ginn Chen) r=luser/ted a1.9=beltzner]
""",
u"""
JavaScript Tests - regression test for , by Brendan Eich
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by shutdown
""",
u"""
JavaScript Tests - regression tests for , by Seno Aiko
""",
u"""
[] fixing dtrace breakage caused by incomplete backing out of . r,a=none as the code is not apart of the build.
""",
u"""
[] optimizing call object property allocation, r=brendan a1.9=mtschrep
""",
u"""
[] optimizing reserve slot allocation, r=brendan a1.9=mtschrep
""",
u"""
[] backing out as a simpler patch would do the job with less code.
""",
u"""
[] backing out - too much compatibility problems.
""",
u"""
JavaScript Tests - update test for to handle various memory pressure scenarios
""",
u"""
Removing bogus FIXME here (comment-change only)
""",
u"""
: silencing warnings in jsdtrace.c, r/a=shaver
""",
u"""
[] post landing consetics: replacing // comments with good old /* */
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
Fixing . Clear scope on XOWs when scope is cleared on the object wrapped by the XOW. r+sr=mrbkap@gmail.com
""",
u"""
JavaScript Tests - remove unneeded image foo from test, 
""",
u"""
JavaScript Tests - remove machine name from public failures, 
""",
u"""
JavaScript Tests - regression test for 
""",
u"""
- "Crash [@ js_GetWrappedObject]" [p=mrbkap@gmail.com (Blake Kaplan) r=brendan a1.9b5=beltzner]
""",
u"""
- [p=jst@mozilla.org (Johnny Stenback [jst]) r+sr=mrbkap a1.9b5=schrep]
""",
u"""
Fix - C++ compatibilty: jsdbgapi.cpp: use of JS_malloc needs a cast (r=brendan)
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.  (This doesn't build, thanks to , which I'll fix next.)
""",
u"""
JavaScript Tests - update public failures list, , not part of the build
""",
u"""
Bugs 423443/419661: crash in MarkSharpObjects due to stack overflow, when over-deep engine-internal recursion is triggered in JS components. r=brendan, a-b5=beltzner
""",
u"""
JavaScript Tests - regression test for , by James Justin Harrell
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by moz_bug_r_a4
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Mike Shaver
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by x0
""",
u"""
[] using jsop_lineno to speedup pc->lineno mapping needed for eval. r=shaver a1.9b5=beltzner
""",
u"""
bug=356378 r=brendan a1.9b5=beltzner reporting bad getter usage at compile time, not at runtime.
""",
u"""
bug=424750 Patch from Alfred Peng to make dtrace code compilable again after my changes from . r=myself, not a part of the default browser configuration.
""",
u"""
Sisyphus|JavaScript Tests - handle cygwin drive prefix in determining test completion, 
""",
u"""
Fix bug and modularity loss introduced by patch for 424405 (424614, r/a=shaver, bug a=beltzner).
""",
u"""
JavaScript Tests - update spidermonkey-extensions-n.tests, no bug, not part of the build
""",
u"""
JavaScript Tests - update ecma_3/RegExp/regress-375711.js due to change in 
""",
u"""
Sisyphus|JavaScript Tests - make post-process-logs.pl handle incomplete log output, 
""",
u"""
bug=424376 r=brendan a1.9b5=beltzner Compile-time function objects are no longer exposed through SpiderMonkey API.
""",
u"""
- "XDR should compensate for traps set in the script it is serializing" [p=crowder@fiverocks.com (Brian Crowder) r+a1.9b5=shaver]
""",
u"""
- printObj crashes on dense arrays, r/a1.9b5=shaver
""",
u"""
Fixing build bustage from for dtrace (not a standard configuration)
""",
u"""
bug=423874 r=brendan a1.9b5=dsicore Allocating native functions together with JSObject
""",
u"""
Followup fix for . Re-enable loading file:// URIs using the subscript loader. r+sr=bzbarsky@mit.edu
""",
u"""
- C++ compilation error in jsinterp.c, r=crowder a=beltzner
""",
u"""
Fix the jsinterp.cpp here, before it gets upstreamed.
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central. There's a C++ bug in js/src/jsinterp.cpp that I am going to file upstream.
""",
u"""
- Invalid range error for case-insensitive regular expression, r=brendan, a=blocking1.9 (mtschrep)
""",
u"""
- "Script stack space in Firefox 3.0b4pre much smaller than it was in Firefox 2.0.0.12" [p=igor@mir2.org (Igor Bukanov) r=brendan a=blocking1.9+]
""",
u"""
Fix for JSCLASS_NEW_RESOLVE-related bug in js_FillPropertyCache, found by Mike Moening <MikeM@RetekSolutions.com> (418989, r=shaver, a=beltzner).
""",
u"""
reverting, wrong patch, missing AMBIGUOUS
""",
u"""
Interfaces missing from various QI implementations. r=jag sr=jag a=dsicore
""",
u"""
- Remove JSCLASS_FIXED_BINDING; the code that was to use it was removed, and it just clutters the API.  r=brendan, a=schrep
""",
u"""
Fix JSOP_SETCALL to cope with delete f() and the like (423300, r=mrbkap, a=beltzner).
""",
u"""
bug=420869 backing out as the tree is red.
""",
u"""
bug=420869 r=brendan a1.9=blocking1.9 bumping script stack quota to 100MB for better compatibility with FF2.
""",
u"""
Remove method that no longer exists.
""",
u"""
Fixing bustage.
""",
u"""
Fixing . Make XOW/SJOW wrappers do security checks on enumeration and interation. r+sr=mrbkap@gmail.com
""",
u"""
Finally kill off CheckSameOriginPrincipal, fix remaining callers to do the checks they really want to be doing.  Fix screw-up in nsPrincipal::Equals if one principal has a cert and the other does not.  , r=mrbkap,dveditz, sr=jst
""",
u"""
- "Build spidermonkey with icc on macintel" [p=ted.mielczarek@gmail.com (Ted Mielczarek [luser]) r=bsmedberg a=blocking1.9+]
""",
u"""
Set the right url in the script and don't allow loading non-chrome scripts. , r+sr=jst
""",
u"""
Add knowledge of edge names to cycle collector, ifdef DEBUG_CC.  b=420514  r+sr=peterv  a=damons
""",
u"""
Fix , js shell print() should flush stdout.  r+a=shaver.  Does not affect Firefox.
""",
u"""
, browser-test crashes on linux, patch by smaug <Olli.Pettay@gmail.com>, r=brendan, a=beltzner
""",
u"""
bug=421274 r=brendan a=beltzner Eliminating SAVE_SP_AND_PC() macro
""",
u"""
. gcc (4.1 only) zealously avoids inlining at -Os. Patch by Dan Witte. r=ted.mielczarek
""",
u"""
JavaScript Tests - modify test to catch allocation size overflow, 
""",
u"""
: uninitialized memory-read in XPCWrapper::AddProperty, r/sr=mrbkap, a=:luser
""",
u"""
bug=422432 r=brenda,jag a1.9=blocking1.9 The local free lists for doubles now restricted to 32/64 entries, not 8, to minimize locking penaltties.
""",
u"""
Fix merge bug that only shows up building spidermonkey standalone.
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central to pick up the 421274 backout especially
""",
u"""
JavaScript Tests - update tests due to changes on trunk for overflow reporting, 
""",
u"""
. support for custom options for jsinterp.c when compiling the browser. Patch by Ted Mielczarek. r=bsmedberg
""",
u"""
: backing out again due to crashes on 64 bit Linux.
""",
u"""
bug=421274 follow up to fix issues with 64 bit
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
Fix ASSERT_VALID_PROPERTY_CACHE_HIT bustage (NPOTB).
""",
u"""
bug=421274 r=brendan a1.9=mtschrep eliminating SAVE_SP_AND_PC and friends from the interpreter loop
""",
u"""
backing out 
""",
u"""
bug=421274 r=brendan a1.9=mtschrep eliminating SAVE_SP_AND_PC and friends from the interpreter loop
""",
u"""
bug=422348 r,a1.9=shaver proper overflow error reporting
""",
u"""
bug=421806 r=brendan a1.9=blockin1.9 fixing decompiler regressions with interpreter stack modeling
""",
u"""
- "jsgc.obj : error LNK2001: unresolved external symbol "int __cdecl posix_memalign(void * *,unsigned int,unsigned int)" (?posix_memalign@@YAHPAPAXII@Z)" (posix_memalign needs to be extern "C" when compiling with a C++ compiler) [p=benjamin@smedbergs.us (Benjamin Smedberg [bsmedberg]) r=brendan a1.9=damons]
""",
u"""
- Fix JS strict errors in *.jsm modules. r and rs=gavin, a1.9+=damons
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
JavaScript Tests - update known failures to account for improved CAPS messages in , not part of the build
""",
u"""
JavaScript Tests - update known failures for mac debug browser on js1_5/Array/regress-350256-03.js, , not part of the build
""",
u"""
bug=420904 support for custom options for jsinterp.c in js shell build scripts. This is outside of tree.
""",
u"""
Fix indentation nit
""",
u"""
: fix accounting of array length when slicing dense arrays. r=mrbkap, a=mconnor.
""",
u"""
JavaScript Tests - fix TimeWithinDay for negative arguments, 
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
- "Make network error constants accessible via Components.results" [p=trev.moz@adblockplus.org (Wladimir Palant) r=biesi sr=sicking a1.9=damons]
""",
u"""
- "More C++ casts required for Windows only, especially overloaded pow() and log10()" [p=benjamin@smedbergs.us (Benjamin Smedberg [bsmedberg]) r=crowder a1.9=damons]
""",
u"""
Crash [@ jsds_ScriptHookProc] r=caillon a=dsicore If we reach ~jsdService, that means our client doesn't care about us, so we can (and should) drop all references to any callbacks (if they cared, they'd have kept us alive!*). I think jsdService::Off should clear all the hooks, the strange magic of not clearing it isn't really a great idea. So for Off, we'll now clear the ScriptHook too (consumers who use off should really drop any references they have to our objects...). I'm still on the fence on this point, I suspect we can actually move it from ::Off to ~jsdService (it must be cleared at some point, otherwise if jsd_xpc's library manages to get unloaded, the function pointer would be invalid, which would be *BAD*). jsds_NotifyPendingDeadScripts needs to clear gDeadScripts whether or not there's a service or hooks, so it does. Because it's a static callback and because of the scary way GC works, I'd rather ensure (deathgrip) that jsds is available (and consistent!) for the duration of the function call. The code already handles the lack of a hook, so there's no reason to do magical returns.... The real problem which mayhemer found was that jsdService::Off was returning early (failure) because gGCStatus wasn't JSGC_END when called from ~jsdService from JS_GC from the cyclecollector, so we make sure that ~jsdService forces ::Off to act as if it is JSGC_END (after ensuring that there are no callbacks available). * a pure javascript (xpcom component, not DOM hosted!) version of a jsdService consumer means that jsdService will need to talk to the CycleCollector eventually (this is another bug for the future).
""",
u"""
. Build with -fstrict-aliasing on GCC platforms. r/a=shaver
""",
u"""
consolidate jsd static variables into main r=shaver
""",
u"""
JavaScript Tests - update test to catch exception in browser tests, 
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
bug=419632 r=brendan a1.9=blockin1.9 avoiding weak roots for doubles
""",
u"""
Back out the patch from because it broke gmail ()
""",
u"""
JavaScript Tests - regression tests for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Mike Shaver
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Brian Crowder
""",
u"""
JavaScript Tests - remove timezone dependencies for toLocaleFormat win32 tests, no bug, not part of the build
""",
u"""
js.c needs to call JSDB_TermDebugger r=brendan NPOTB
""",
u"""
Fix from Sebastian Redl to compile under GCC 4.2 (r=me, a=shaver).
""",
u"""
: array_join_sub does not handle holes in dense arrays correctly, r/a=shaver
""",
u"""
- Issues with Unicode escape sequences in JavaScript source code; Unicode escapes not part of identifiers were being treated as their equivalent CVs, and non-identifier Unicode escapes within identifiers were being treated as their CVs (simultaneously starting a new token).  acid3++  r=mrbkap, a=damons
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
Deal with nsXPCWrappedJS::GetClass being null, which it can be after Unlink.  a=Not part of the default build (DEBUG_CC only)
""",
u"""
bug=421154 r=brendan a1.9=blockin1.9 Faster number conversions
""",
u"""
Don't assume that chrome:// implies system principals. , r=brendan sr=jst
""",
u"""
bug=421314 r=myself a1.9=beltzner Patch from Mike Moening to fix VC2005 warnings that my recent changes introduced.
""",
u"""
bug=421266 r=brendan a1.9=beltzner js_Interpret now takes just single cx argument.
""",
u"""
Remove unused variable. 
""",
u"""
bug=415455 r=brendan a1.9=blocking1.9
""",
u"""
Protect |accum| from being collected in js_ConcatStrings. , r=igor a=beltzner
""",
u"""
Fix array_concat to be more generic. , r=brendan a=beltzner
""",
u"""
Allow things to happen to SJOWs if there's no code running. , r+sr=jst
""",
u"""
Remove a now-unnecessary eval hack. , r+sr=jst a=beltzner
""",
u"""
Fix mochitest depending on the old toString behavior.
""",
u"""
Propagate getters and setters onto the inner object. , r+sr=jst
""",
u"""
Make Object.prototype.toString show the underlying object. , r+a=brendan
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
Fix signed vs. unsigned comparison in assertion warning.
""",
u"""
Crash [@ jsds_NotifyPendingDeadScripts] ds->script is null r=jst a=beltzner
""",
u"""
bug=418641 r=brendan a1.9=dsicore Avoiding code bloat on slow paths in the interpreter.
""",
u"""
bug=355258 r=brendan a1.9=beltzner
""",
u"""
- Optimize parseInt for integer values, if radix is 10, r=brendan, blocking1.9=dsicore
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
Fix bracing mistake from .
""",
u"""
Always wrap content nodes in chrome with some sort of wrapper. , r+sr=jst
""",
u"""
Fix over-including dependencies, and relocate ID_TO_VALUE to avoid over-including (r=mrbkap, bustage fix).
""",
u"""
Break bad old nested include cycle for good, by un-nesting (420554, r=jorendorff, a=vlad).
""",
u"""
bug=420399 r=brendan a1.9=blocking1.9 eliminating the pc stack in the interpreter
""",
u"""
JavaScript Tests - update known failures
""",
u"""
JavaScript Tests - update known failures
""",
u"""
JavaScript Tests - remove wfm failure, 
""",
u"""
: the interpreter loop belongs to its own compilation unit. r,a1.9=brendan
""",
u"""
xpconnect should not use fun->atom r=dbradley a=brendan
""",
u"""
- "insufficient unlink methods in some DOM classes?". Fix for DEBUG_xpc_hacker builds. Not part of the normal build, r+sr+a=jst.
""",
u"""
JavaScript Tests - update known failures, 
""",
u"""
Urghh...
""",
u"""
Clean up and fix computed this under js_Execute (420610, r=mrbkap+crowder, a=vlad).
""",
u"""
mrbkap's fantabulous fix for 418565, r=me, a=beltzner.
""",
u"""
Add crashtest
""",
u"""
mrbkap's patch for 418293 with a few nits picked, r=me, a=beltzner.
""",
u"""
mrbkap's fix for 420612, r=me, a=beltzner.
""",
u"""
Checking in mrbkap's fix for 420513, r=me, a=beltzner.
""",
u"""
Add crashtest
""",
u"""
bug=420593 fixing mispellings in comments introfuced in the patch for .
""",
u"""
bug=420639 fixing comments in the checking for .
""",
u"""
Fix dependencies in the JS shell. , patch adapted from one by jorendorff, r=brendan a=NPOTB
""",
u"""
bug=418737 r=brendan a1.9b4=mtshrep fixing fast array enumerator
""",
u"""
bug=396007 r=brendan a1.9b4=mtschrep Prefering posix_memalign over mmap to allocate GC arenas.
""",
u"""
Fix property cache fill to recompute protoIndex to handle XBL and other JS_SetPrototype users (418139, r/a=shaver).
""",
u"""
Unregress perf in wake of 418069 (420426, r=mrbkap, a=mconnor).
""",
u"""
Stick exn back into the context so that js_ReportErrorAgain callees can access the exception. , patch from taras, r=mrbkap a=mconnor
""",
u"""
Backout due to regressions
""",
u"""
Fix ComputeThis perf regression (420426, r=mrbkap, a=sayrer).
""",
u"""
Remove unused variable. , r+a=brendan
""",
u"""
Outerize |this| always. , r/sr=jst/brendan a=beltzner
""",
u"""
Another assert that was an already-coped-with property cache hazard (420087, r=shaver, a=beltzner).
""",
u"""
merge cvs-trunk-mirror -> mozilla-central
""",
u"""
- _InterlockedCompareExchange needs to be extern "C" when using a C++ compiler, r=brendan a1.9b4=beltzner
""",
u"""
Fix slot type to satisfy C++ (420215, r=bsmedberg, a=beltzner).
""",
u"""
- "insufficient unlink methods in some DOM classes?". Allow the cycle collector to unlink XPCWrappedNatives in one cycle instead of two. r=peterv, sr=jst, a1.9b4+=schrep.
""",
u"""
JavaScript Tests - regression test for , by jag (Peter Annema)
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
Unbitrot JS_OPMETER (363529, r=shaver, a=beltzner/sayrer).
""",
u"""
Cope with JSOP_INITPROP property cache proto-property-with-non-stub-setter hazard (419822, r=shaver, a=beltzner).
""",
u"""
JavaScript Tests - regression tests for , by Mike Shaver
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
Fix bogus assertion with compensating code (419803, r=shaver, a=beltzner).
""",
u"""
Merge cvs-trunk-mirror to mozilla-central.
""",
u"""
Backing out to fix orange on Windows fx/tb/sm...
""",
u"""
Landing shaver's patch for 419743, r/a=me.
""",
u"""
Optimize object initialisers via property cache; remove JSOP_SET{NAME,PROP} cache hazards (129496, r=shaver).
""",
u"""
bug=400902 r,a1.9=brendan Specialized GC arena for double values
""",
u"""
JavaScript Tests - regression tests for , by Igor Bukanov
""",
u"""
Fix regression from 419152 to test for 58274 (r/a=shaver).
""",
u"""
Interfaces missing from various QI implementations. jsdContext r=caillon sr=jag a=dsicore
""",
u"""
ASSERT_VALID_LOCK failed r=gijs a=dsicore
""",
u"""
ASSERT_VALID_LOCK failed r=gijs a=dsicore
""",
u"""
Shaver's huge patch for 419152 (Huge, I say; r=me).
""",
u"""
- "Use JS_GET_CLASS, not JS_GetClass" [p=gyuyoung.kim@samsung.com (gyu-young kim) r=jorendorff r=jst sr+a1.9=brendan]
""",
u"""
Backing out . Something's still screwy :-(
""",
u"""
: specialized arena for doubles
""",
u"""
WINCE Only.  Slash doesn't work in MINGW32, but - works everywhere.
""",
u"""
- "js/src/prmjtime.c uses the wrong value for NS_HAVE_INVALID_PARAMETER_HANDLER on windows mobile" [p=dougt@meer.net (Doug Turner) r+a1.9=crowder]
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
- cast void* in js/src for C++ compatibility, r+a=crowder
""",
u"""
- Fix silly crash in slowarray_enumerate, patch by mrbkap, r=shaver, a1.9=mconnor
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, Igor Bukanov
""",
u"""
JavaScript Tests - Object destructuring shorthand, , by Brendan Eich
""",
u"""
JavaScript Tests - allow function Error() {} for the love of Pete, 
""",
u"""
windows mobile build error in js/src/jsdate.c GetLocalTime is defined in the Windows Mobile SDK patch by dougt r=crowder a=beltzner
""",
u"""
ASSERT_VALID_PROPERTY_CACHE_HIT must be for ST spidermonkey only (417817, r=shaver).
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jeff Walden
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
Beware non-native objects along scope and proto chains in property cache hit testing (418540, r=shaver).
""",
u"""
jorendorff's JS_DEBUG_TITLE_LOCKS patch (417818, r=shaver).
""",
u"""
Back out because it causes a crash on startup for Camino
""",
u"""
Sisyphus/JavaScript Tests - update public failures, no bug, not part of the build
""",
u"""
- js1_5/Regress/regress-379245.js FAIL - browser - bad this, patch by mrbkap, r=brendan, sr=jst, a1.9=brendan
""",
u"""
- various bugs in JS shell scatter() and sleep(), patch by Jason Orendorff <jorendorff@mozilla.com>, r=crowder, a=NPOTB
""",
u"""
Landing fix for . Don't run code on invalid contextx. Patch by mrbkap@gmail.com, r+sr=jst@mozilla.org
""",
u"""
bug=418614 r=mrbkap a1.9=brendan fixing JSOP_EXPORTALL regression spotted by mrbkap
""",
u"""
- fix use of uninitialized data in js_CheckAccess, patch by Blake Kaplan <mrbkap@gmail.com>, r+=shaver, a+=brendan
""",
u"""
Sisyphus/JavaScript Tests - handle malformed log files, 
""",
u"""
- "ActionMonkey: Modify js/src to use new thread-safe MMgc APIs" (tests) [p=jorendorff@mozilla.com (Jason Orendorff) r=bc a1.9=schrep]
""",
u"""
- "ActionMonkey: Modify js/src to use new thread-safe MMgc APIs" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
- "Provide stubs for JS_THREADSAFE APIs in non-JS_THREADSAFE builds" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
bug=418456 r,a1.9=brendan Fixing asserts in js_PutBlockObject
""",
u"""
: Mozilla build broken in mozilla/js/src/jsgc.c:2217. All the compilers we support can handle long long, so just go with that. Also remove ifdefs for compilers we no longer care about. r=/a=brendan
""",
u"""
- Better management of parent-finding, needed for new arrays implementation, r/a+=brendan
""",
u"""
Fix line numbering in JS components so it's not off by 1.  , r+sr+a=brendan
""",
u"""
Fix untagged boolean stored as jsval bug (418504, r=jwalden).
""",
u"""
JavaScript Tests - add js1_5/Regress/regress-416628.js to the performance tests, 
""",
u"""
JavaScript Tests - update to remove failures due to change in expected behavior, 
""",
u"""
. Using goto error in the interpreter to shrink code size. r,a1.9=brendan
""",
u"""
Property-cache dense array methods in JSOP_CALLPROP (418239, r=shaver).
""",
u"""
In JS_PrintTraceThingInfo, only print the contents of JSSLOT_PRIVATE if it represents the class's private rather than the first slot.  b=417972  r=igor  a=DEBUG-only (not part of the default build)
""",
u"""
Relaxd ES4-like yield parsing for JS1.8 (384991, r=mrbkap).
""",
u"""
Avoid calling js_ComputeThis when we don't have to from js_Invoke. , r+a=brendan
""",
u"""
Fix js_CheckAccess to handle use in non-native objects' ops, fixing test-suite regressions from native-arrays landing. r=mrbkap, a=brendan.
""",
u"""
- removed JS_ArenaFreeAllocation, r+/a+=brendan
""",
u"""
- SpanDeps allocation does not use JSArenas anymore, r+/a+=brendan
""",
u"""
Implement optimized object-ops for dense arrays, b=322889, r+a=brendan.
""",
u"""
: Mingw build error in ../mozilla/js/src/jslock.c: syntax error. p=bengt.erik.soderstrom@telia.com, r=jag, a=brendan
""",
u"""
Guard property cache tests with native ops or obj guards (417981, r=shaver).
""",
u"""
JavaScript Test - regression test for , by Brendan Eich
""",
u"""
JavaScript Tests - regression test for , by Joachim Kuebart
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
Use JS_PropertyStub for in-language bindings, for best property cache hit rates (416931, r=mrbkap).
""",
u"""
Recover trapped opcode in js_GetIndexFromBytecode (416665, r=igor).
""",
u"""
Lazy ComputeGlobalThis required now in fast native implementations (417893, r=mrbkap).
""",
u"""
Fix misindented code (418049, r=igor).
""",
u"""
Sisyphus/JavaScript Tests - update known failures, no bug, not part of the build
""",
u"""
CheckLeakedRoots should specify which JSRuntime is leaking r=brendan a=brendan
""",
u"""
- "js.c doesn't build under MOZ_SHARK" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
Sisyphus/JavaScript Tests - update known failures to match new time out variables, no bug, not part of the build
""",
u"""
Defend against compiler pseudo-frames (417944, r=shaver).
""",
u"""
Sisyphus/JavaScript Tests - add timeout for js1_6/extensions/regress-385393-08.js due to 
""",
u"""
Sisyphus/JavaScript Tests - lower timeout to 2 minutes, , not part of the build
""",
u"""
Sisyphus/JavaScript Tests - update known failures for windows, no bug, not part of the build
""",
u"""
Don't lock non-native objects (417819, r=mrbkap).
""",
u"""
Add crashtest
""",
u"""
Optimize ComputeGlobalThis (395993, r=mrbkap).
""",
u"""
: property cache is properly disabled under with statements with generators. r=brendan a1.9=blocking1.9
""",
u"""
back out for mochitest failures in prototype
""",
u"""
: implement specialized storage and operations for JS arrays; r+a=brendan.
""",
u"""
Back out due to jQuery unit test failures
""",
u"""
: implement specialized storage and operations for JS arrays; r+a=brendan
""",
u"""
: refactor JSScope locking for reuse on non-native objects. r+a=brendan.
""",
u"""
: You too can solve global-warming without making the JS_INLINE macro ugly. r=/a=brendan
""",
u"""
Sisyphus/JavaScript Tests - update known failures list, no bug, not part of the build
""",
u"""
: optimizing switch cases in the inetrpreter, r,a1.9=brendan
""",
u"""
- "JS_YieldRequest doesn't do scope-sharing" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
Optimize wrapper creation via JS_NewObjectWithGivenProto, and avoid cycle-check overhead in JS_Set{Prototype,Parent} (408871, r=mrbkap).
""",
u"""
Must set initial slot value in js_DefineNativeProperty via write barrier (417012, r=shaver).
""",
u"""
Sisyphus/JavaScript Tests - update public failures, no bug, not part of the build
""",
u"""
JavaScript Tests - update test due to 
""",
u"""
Fiddle blank lines botched in my last checkin.
""",
u"""
- Fixing windows build errors
""",
u"""
- more aggressive inlining for jsregexp.c, r=brendan, a1.9=mtschrep
""",
u"""
- more rigorous inlining functionality for JS, r/a1.9=brendan
""",
u"""
Sisyphus/JavaScript Tests - improve test timeout handling, 
""",
u"""
: non-recursive XML-filtering implementation. r,a1.9=brendan
""",
u"""
Patch from Robert Longson <longsonr@gmail.com> for _InterlockedCompareExchange on MSVC7.1 (416813, r=me).
""",
u"""
Fix stupidity from patch for 414452 (417144, r=shaver, thanks to vlad for finding).
""",
u"""
Cope with GC under js_{Find,Lookup}Property in ASSERT_VALID_PROPERTY_CACHE_HIT (417033, r=shaver).
""",
u"""
Sisyphus/JavaScript Tests - fix post-process-logs.pl page, exit status processing, 
""",
u"""
- Convert GetMessage APIs to GetMessageMoz APIs, at the C++ symbol level only (vtables remain the same), to work around brain-dead, idiotic, insane Windows API macros.  r=bsmedberg, a=schrep
""",
u"""
Sisyphus/JavaScript Tests - attempt 2 at getting known failures correct, 
""",
u"""
Sisyphus/JavaScript Tests - improve page time out handling in post-process-logs.sh, 
""",
u"""
Fixing js.mak - adding jsiter
""",
u"""
JavaScript Tests - update test for 
""",
u"""
- Optimize JS_MAX(upcase(localMax), downcase(localMax)), r=mrbkap, blocking1.9=brendan, idea from BijuMailList@gmail.com
""",
u"""
regression test. r=shaver
""",
u"""
: jsinterp.c warning: empty body in an if-statement (times 4). r=/a=brendan
""",
u"""
Sisyphus/JavaScript Tests - update known failures, 
""",
u"""
Sisyphus/JavaScript Tests - handle browser test timeouts better in non-restart mode, 
""",
u"""
Sisyphus/JavaScript Tests - improve error message, 
""",
u"""
Avoid O(n^2) hazard under JS_ARENA_RELEASE, simplifying arena-pool usage and eliminating debug code (416628, r=igor).
""",
u"""
JavaScript Tests - update *.tests lists, 
""",
u"""
- "JSContext::outstandingRequests bookkeeping is incorrect" [p=jorendorff@mozilla.com (Jason Orendorff) r=igor a1.9=schrep a=blocking1.9+]
""",
u"""
Export js_CheckForStringIndex from jsobj.c for use by assert in jsinterp.c (416460, r=shaver).
""",
u"""
- "Main content panel is not rendered for all WebCT/Blackboard installations" [p=crowder@fiverocks.com (Brian Crowder) r+a1.9=brendan a=blocking1.9+]
""",
u"""
unbalanced locking in jsd_SetExecutionHook r=crowder a=mtschrep
""",
u"""
- Yield and let expressions disappear in decompilation of object literal due to mismanagement of the sprintstack; just sprint all at once instead of in two steps.  r+a=brendan
""",
u"""
: Patch from Mike Moening to allow buiding SpiderMonkey as a static library. r=myself, a1.9=brendan
""",
u"""
Add crashtests
""",
u"""
Missing unlock in propcache setprop/setname code, plus two cleanups (416478, r=shaver, mad props to jorendorff).
""",
u"""
Put js_DisablePropertyCache in the right place in the obj_eval flow graph (416406, r=shaver).
""",
u"""
: faster js_GetLocalNameArray. r=brendan a=blocking1.9
""",
u"""
Fixing . Quiet down a bogus assertion. r+sr=peterv@propagandism.org, a=mtschrep@gmail.com
""",
u"""
Landing updated fix for . Don't allocate links on the heap. Patch by mrbkap@gmail.com and jst@mozilla.org, r+sr=brendan@mozilla.org/mrbkap@mozilla.org
""",
u"""
Fix bogus assertion (416404, r=shaver).
""",
u"""
Attachment 302122: optimizing JSOP_NEG, r=brendan a=blocking1.9
""",
u"""
: proper verification for stack layout in the decompiler, r=brendan a=blocking1.9
""",
u"""
JavaScript Tests - fix window detection in test for 
""",
u"""
More detailed description of JS objects.  b=414972  r+sr=peterv  a=not part of default build (DEBUG_CC only)
""",
u"""
Add comment explaining mJSRoots and ExplainLiveExpectedGarbage business.
""",
u"""
Return of the property cache (365851, r=shaver).
""",
u"""
- Exception from within JSNewEnumerateOp on JSENUMERATE_NEXT not supported, patch by Joachim Kuebart <jkuebart@ptc.com>, r=brendan, a1.9=brendan
""",
u"""
JavaScript Tests - regression test for , by moz_bug_r_a4
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Biju
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Rudermen
""",
u"""
Fix for ("success" returned uninitialized from XPCVariant::VariantDataToJS). r/sr=jst, a=schrep.
""",
u"""
- "C++ warnings in jsnum.c, jsutil.c (with g++ -Wconversion)" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
- "Provide stubs for JS_THREADSAFE APIs in non-JS_THREADSAFE builds" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
JavaScript Tests - run Tinderbox browser tests without restarting browser, 
""",
u"""
Fixed generation-number-optimized hash revalidation (415721, r=igor).
""",
u"""
Test case for r=bclary@bclary.com
""",
u"""
Regression test for . r=bclary@bclary.com
""",
u"""
Reload key in case of multithreaded race to atomize the same string chars (415474, r=igor).
""",
u"""
: Backing out due to test failures.
""",
u"""
: specialized arena for fast allocation of double values.r,a=brendan ab3=mtschrep
""",
u"""
As you might expect, a regression test for . r=bclary@bclary.org
""",
u"""
: backing out due to test failures.
""",
u"""
: using a specialized GC arena for doubles. r,a=brendan a1.9b3=mtschrep
""",
u"""
Bug  415207: fix time overflow in arena aging code. r=crowder a1.9,a1.9b3=beltzner
""",
u"""
: protect against oo recursion in e4x. r,a=brendan, a1.9b3=mtschrep
""",
u"""
Fix for ("ASSERTION: Fault in cycle collector: script pointer traversal failed"). r/sr=jst, a=beltzner.
""",
u"""
Get the right principal for cloned functions. , r=brendan
""",
u"""
Fix from Arjan Van De Ven <arjan.van.de.ven@intel.com> to regression from patch for (fixing 353962, r=me, a=beltzner).
""",
u"""
Top crash [@ jsds_ScriptHookProc][@jsds_ScriptHookProc(JSDContext*, JSDScript*, int, void*)] on shutdown with Fire.1.0b10 installed r=gijs a=beltzner
""",
u"""
: fixing gczeal issue. r=brendan, approval1.9b3=beltzner
""",
u"""
Back out jimm's patch from due to regressions. [a1.9b3=mconnor]
""",
u"""
Try to fix Ts regression (414452, r=shaver).
""",
u"""
Move serialized cycle detector for __proto__ and __parent__ into js_GC (414452, r=igor+shaver).
""",
u"""
Final js1.8 feature: sugar for object destructuring (404734, r=mrbkap).
""",
u"""
Landing followup to the fix for , this one somehow slipped through, just more of the same.
""",
u"""
Attachment 300249: better handling of numeric conversions. r,a=brendan
""",
u"""
Dammit.
""",
u"""
Don't wrap chrome objects in SJOWs if we don't have to. , r=jst sr=bzbarsky
""",
u"""
Oops.
""",
u"""
Don't self-lock in the JSGC_BEGIN callback (413097, r=shaver).
""",
u"""
- Improve hash performance using _rotr intrinsic (js/src hunk), patch by Michael Moy <mmoy@yahoo.com> with updates by me and r=wtc, r=brendan, a=brendan
""",
u"""
Fixing . Don't suspend/resume requests when making native calls into C++ in XPConnect, do the suspend/resume when pushing/popping JS contexts off of the context stack instead. r=shaver@mozilla.org, sr=brendan@mozilla.org
""",
u"""
Outerize this when we're computing it. , r=brendan
""",
u"""
: allocate stackPools less often, r=brendan, a=blocking1.9 (schrep)
""",
u"""
SJOW's equality hook returns true too much. , r+sr=jst a=damons
""",
u"""
Fix for (JS_Assert "!rt->gcRunning" unbinding link elements in cycle collector with JS protocol handlers), r/sr=dbaron.
""",
u"""
Preserve interesting attributes on same-origin XOWs. , r+sr=jst a=beltzner
""",
u"""
Fixing . Make sure to not use a context from a different thread when calling functions on a wrapped JS object. r+sr=peterv@propagandism.org
""",
u"""
: JS_GCMETER requires to recompile just js/src, not the whole browser. r,a=brendan
""",
u"""
Try to fix orange
""",
u"""
- "Optimize read file buffer sizes for faster startup times" [p=jmathies@mozilla.com (Jim Mathies) r=sayrer sr=bsmedberg a=blocking1.9+]
""",
u"""
Fix for (JS_Assert "!rt->gcRunning" unbinding link elements in cycle collector with JS protocol handlers), r/sr=dbaron.
""",
u"""
Missing ECMA conformance test, see https://bugzilla.mozilla.org/show_bug.cgi?id=392593
""",
u"""
Revert last checkin (414452).
""",
u"""
Move guts of js_SetProtoOrParent to jsgc.c, unifying serialization and deadlock avoidance machinery (414452, r=igor).
""",
u"""
Fixing windows bustage.
""",
u"""
Backing out to see if this is the cause for apparent random crashes.
""",
u"""
Fixing . Make XPConnect use faster accessors for JS class/parent/private/proto. r=mrbkap@gmail.com, sr=brendan@mozilla.org
""",
u"""
There might be a pushed context but no running code. , r+sr=jst a=blocking-1.9+
""",
u"""
Create a more valid pseudo-frame for liveconnect to avoid null ptr dereferences. , r=brendan sr=jst a=brendan
""",
u"""
Don't allocate links on the heap. , r+sr=brendan a=schrep
""",
u"""
: fixing JS compilation. r=outside of the browser three
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
Must lock newborn block object (shared) scope before calling js_GetMutableScope (413850, r=mrbkap).
""",
u"""
Fix think-o causing valgrind errors during evalcx(). , r=shaver NPOTB
""",
u"""
Fix #if-related bug that broken compilation of pre-1.7 versions (, r=timeless).
""",
u"""
Landing fix for . Do the right thing when converting objects wrapped in XOWs. Patch by mrbkap@gmail.com, r=jst@mozilla.org, sr=brendan@mozilla.org
""",
u"""
Landing fix for . Make sure functions get the right filename. Patch by mrbkap@gmail.com, r=brendan@mozilla.org
""",
u"""
Fixing . Prevent document principals from ever changing, and make us not use XOWs for same origin document objects. r=jonas@sickin.cc, sr=bzbarsky@mit.edu
""",
u"""
Fixing . Make XPCWrappedNative::CallMethod() initialize the nsAutoString buffer used for [out] string param handling only when needed. r+sr=jonas@sicking.cc
""",
u"""
Fixing . Make some JS API functions faster by accessing obj->fslots[] directly when possible. r=brendan@mozilla.org, r=igor@mir2.org.
""",
u"""
: Patch from Jason Orendorff to fix JS_ConvertArguments. r,a=brendan
""",
u"""
: avois rehashing of alreday atomized strings. r,a=brendan
""",
u"""
: GC now put all free cells to free lists. r,a=brendan
""",
u"""
: backing out again to fix incorrect error recovery
""",
u"""
: faster implementation of js_GetLocalNameArray. r,a=brendan
""",
u"""
: the new version of the patch shows the same bad Ts regression, backing out again.
""",
u"""
Fix #ifdef NARCISSUS code to track patch for (NPOTB).
""",
u"""
: faster implementation of js_GetLocalNames. r,a=brendan
""",
u"""
. Shark functions. r/sr=brendan
""",
u"""
Use already running code's context when executing JS code from C++. , r+sr=jst
""",
u"""
Fixing . Make XPConnect cache the per thread data for the main thread and use the cache when running on the main thread to save on time getting at the per thread data. r=dbradley@gmail.com, sr=brendan@mozilla.org
""",
u"""
Fixing . Make more XPConnect wrappers share their JS object maps. r=peterv@propagandism.org, sr=brendan@mozilla.org
""",
u"""
: fixing bogus assertion in Statements() from jsparse.c. r=brendan,mrbkap a=brendan
""",
u"""
: Backing out due to bad Ts regression.
""",
u"""
: faster implementation of js_GetLocalNames. r=brendan a=blocking1.9+
""",
u"""
Part of fix for (function objects cloned by XPConnect still keep hidden window alive late into shutdown). r=igor, sr=jst.
""",
u"""
XPCWrappedNative::HandlePossibleNameCaseError dereferences an unitialized value if !set r=dbradley sr=jst a=mtschrep
""",
u"""
: function statement and destructuring parameter name clash now favours the function. r,a=brendan
""",
u"""
I'm dumb. Please forgive me. Yes, that includes you, shaver.
""",
u"""
- "Use _InterlockedCompareExchange for js_CompareAndSwap" [p=mmoy@yahoo.com (Michael Moy) r+a1.9=brendan a=blocking1.9+]
""",
u"""
Fix typo noted by igor, 
""",
u"""
. Need Shark functions in JS component global scope. r/sr=brendan
""",
u"""
Config file for Solaris 10 from Wesley Garland (wes@page.ca), r=shaver.
""",
u"""
- js_ValueToBoolean is pure, remove cx and out parameters and just return a boolean value for better perf.  r+a=brendan
""",
u"""
: temp rooting implemenation cleanup, r,a=brendan
""",
u"""
. JS Shark renames per brendan. r/a=brendan
""",
u"""
: access to JSString is hidden behind macros even for a flat string.
""",
u"""
Back out Igor's patch from due to consistent orange on fxdbug-win32-tb.
""",
u"""
: JString stores a flag to indicate that it was atomized. r=brendan a=blocking1.9+
""",
u"""
Back out remainder of patch for to try to fix orange.
""",
u"""
Back out to try to fix orange.
""",
u"""
Fix for (function objects cloned by XPConnect still keep hidden window alive late into shutdown). r=igor, sr=jst.
""",
u"""
Back out patch from , as there may be a Ts perf regression.
""",
u"""
- "xpconnect-tools build broken" [p=armin76@gentoo.org (Raul Porcel) r+sr=bsmedberg (NPODB)]
""",
u"""
- "Optimize read file buffer sizes for faster startup times" [p=jmathies@mozilla.com (Jim Mathies) r=sayrer sr=bsmedberg a=blocking1.9+]
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central
""",
u"""
- "Finishing JS_AlreadyHasOwnProperty" (CHECK_REQUEST(cx) in JS_AlreadyHasOwn{,UC}Property) [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
. Start and stop Shark from JS. r=crowder, sr=jst
""",
u"""
: optimizing regexp upper/lower. r=crowder,a=blocking1.9
""",
u"""
- "js_BoyerMooreHorspool is sometimes called for very short texts" [p=Seno.Aiko@gmail.com r=crowder a1.9=schrep]
""",
u"""
JavaScript Tests - test iterator value scope in array comprehension, by Norris Boyd, , not part of the build
""",
u"""
Don't call js_PopStatement if there was a parse error. , r=brendan
""",
u"""
- "Permission denied to get property XULElement.ownerDocument". Patch by Blake Kaplan <mrbkap@gmail.com>. r=jst,bzbarsky. sr=brendan. a=blocking1.9.
""",
u"""
- nsIXPCNativeCallContext should not inherit from nsISupports, r=mrbkap, a=schrep
""",
u"""
- nsIXPCNativeCallContext should not inherit from nsISupports, r=mrbkap, a=schrep
""",
u"""
JavaScript Test - fix thinko in ecma_3/Number/15.7.4.3-01.js, 
""",
u"""
- Number.prototype.toLocaleString incorrectly accesses the memory where its first argument should be, even if no first argument is actually given.  Tag-team r=igor, r+a=brendan By the way, this checkin occurred on an orange tree.  Just like every other patch in the last day.  Yay checkin policy.
""",
u"""
Sisyphus|JavaScript Tests - fix runtests.sh -e extra argument processing, , not part of the build
""",
u"""
. SpiderMonkey faster at -O2 with msvc. r/a=brendan
""",
u"""
Sisyphus|JavaScript Tests - TinderboxPrint of test counts contain leading whitespace, , not part of the build
""",
u"""
: HP's OA crash [@js_FinalizeObject][@ RtlpDeCommitFreeBlock] when loading blade enclosure info. r/sr=peterv GC was clearing mJSVal without updating mData, so XPCTraceableVariant's destructor would get confused and call Cleanup() on mData when it shouldn't (the buffer pointed to wasn't ours to free, you see). Instead of avoiding Cleanup(), make it be harmless by nulling out the pointer to the buffer.
""",
u"""
JavaScript Tests - update public failures, verified fixed
""",
u"""
* Menu of -D flags for enabling instrumentation, as a commented-out CFLAGS +=   setting for convenient testing. * js_FindProperty and js_LookupPropertyWithFlags return indexes into the scope   and prototype chains, respectively, to support internal instrumentation, and   to pave the way for the return of the property cache ().. * jsutil.[ch] JSBasicStats struct and functions for computing mean/sigma/max   and auto-scaling histogram. * JS_SCOPE_DEPTH_METER instrumentation for compile- and run-time scope chain   length instrumentation: + At compile time, rt->hostenvScopeDepthStats and rt->lexicalScopeDepthStats   meter scope chains passed into the compile and evaluate APIs. + At runtime, rt->protoLookupDepthStats and rt->scopeSearchDepthStats track   steps along the prototype and scope chains until the sought-after property   is found. * JS_ARENAMETER uses JSBasicStats now. * Added rt->liveScopePropsPreSweep to fix the property tree stats code that   rotted when property tree sweeping moved to after the finalization phase. * Un-bitrotted some DEBUG_brendan code, turned some off for myself via XXX. * Mac OS X toolchain requires initialized data shared across dynamic library   member files, outlaws common data, so initialize extern metering vars. * Old HASHMETER code in jshash.[ch] is now JS_HASHMETER-controlled and based   on JSBasicStats. * DEBUG_scopemeters macro renamed JS_DUMP_SCOPE_METERS; uses JSBasicStats now. * Disentangle DEBUG and DUMP_SCOPE_STATS (now JS_DUMP_PROPTREE_STATS) and fix   inconsistent thread safety for liveScopeProps (sometimes atomic-incremented,   sometimes runtime-locked). * Compiler-modeled maxScopeDepth will propagate via JSScript to runtime for   capability-based, interpreter-inlined cache hit qualifier bits, to bypass   scope and prototype chain lookup by optimizing for common monomorphic get,   set, and call site referencing a prototype property in a well-named object   (no shadowing or mutation in 99.9% of the cases).
""",
u"""
Change to ISO C90 comment style to fix warning in sayrer's last patch.
""",
u"""
. Use OSAtomic on Darwin for JS thinlocks. r/a=brendan
""",
u"""
thoroughly whack mallocfest in nsID/nsJSID and friends. b=410250, r+sr=jst, a=blocking1.9+
""",
u"""
JavaScript Tests - regression test for , by Jeff Walden, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Jeff Walden, not part of the build
""",
u"""
backing out jst's fix for because it seems to have turned some tinderboxen red, others orange, and caused web content regressions
""",
u"""
Fix dumb mistake in the last toString patch that causes proto-acid3 to crash.
""",
u"""
- num.toPrecision(undefined) !== num.toString().  r=crowder, a=brendan
""",
u"""
- Given a = num.toString(), b = num.toString(undefined), c = num.toString(10), expect (a === b && b === c).  r=crowder, a=brendan
""",
u"""
Re-landing fix for to see if it really was the cause of the orange last time it landed. Make more XPConnect wrappers share their JSObject maps. r=peterv@propagandism.org, sr=brendan@mozilla.org
""",
u"""
Unset and reset the JS context global objects when doing ExplainLiveExpectedGarbage, just like when doing normal cycle collection.   b=410116  r+sr=peterv  Not part of default build (DEBUG_CC-only).
""",
u"""
Fix Generalize some tests for Rhino and Spidermonkey. r=bclary@bclary.com
""",
u"""
- Assertion failure !rt->gcRunning because I accidentally turned off deffered-release of wrapped natives during GC, r+sr=peterv
""",
u"""
backing out the rest.
""",
u"""
partial backout in an attempt to fix orange.
""",
u"""
relanding .
""",
u"""
backing out to fix orange.
""",
u"""
thoroughly whack mallocfest in nsID/nsJSID and friends. b=410250, r+sr=jst, a=blocking1.9+
""",
u"""
: latent GC hazard in one of the routines in js.c (npotb), r/a=brendan
""",
u"""
- Ancient OOM handling bug with an easy fix, r/a=brendan
""",
u"""
: using the new operation counting JS API for monitoring long-running scripts. r=brendan,jst
""",
u"""
Fix for (JS_Assert "!rt->gcRunning"). r/sr=dbaron.
""",
u"""
JavaScript Tests - update spidermonkey-extensions-n.tests, , not part of the build
""",
u"""
JavaScript Tests - known-failure.pl should ignore trailing spaces, , not part of the build
""",
u"""
: backing the checking as the tree was closed.
""",
u"""
: using the new operation counting JS API for monitoring long-running scripts. r=brendan,jst
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
Backing out 408301 to see if it fixes winxp01 orange
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Brendan Eich, not part of the build
""",
u"""
Support let in switch-case statement lists, scoped by switch body (411279, r=mrbkap).
""",
u"""
Fixing . Make more XPConnect wrappers share their JSObject maps. r=peterv@propagandism.org, sr=brendan@mozilla.org
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
JavaScript Tests - regression test for , by Biju, Brendan Eich, not part of the build
""",
u"""
JavaScript Tests - update test due to fix to , not part of the build
""",
u"""
Require explicit body block in 'for (let x ...) let y...' (410981, r=mrbkap).
""",
u"""
64-bit fixes for problems reported by edwin@cheatah.nl (many thanks to Edwin; 410941, r=igor).
""",
u"""
- Bad C++isms in js/src, r=crowder
""",
u"""
JavaScript Tests - update known failures to account for , not part of the build
""",
u"""
: Backing out once again to figure out the reason for talos regressions.
""",
u"""
JavaScript Tests - update tests to account for , not part of the build
""",
u"""
JavaScript Tests - tests for iterator constructor, by Norris Boyd, 
""",
u"""
: using the new operation counting JS API for monitoring long-running scripts. a,r=brendan
""",
u"""
Add moving-between-frames crashtest
""",
u"""
Add a way to find all of the XOWs for an object and use it to deal with hard cases where we have to clear the scope of XOWs in order to reflect changes to the underlying object. Also deal with objects moving between scopes by ensuring that we're always able to find their XOWs. , r+sr=jst r=brendan for some last-minute changes added in this version.
""",
u"""
Do not allow scripted getters or setters on XPCNativeWrappers. , r=jst sr=brendan
""",
u"""
Track ES4 proposal by restricting let declaration to be direct child of block (408957, r=mrbkap).
""",
u"""
Don't call arbitrary hooks from a function called from GC. , r=brendan
""",
u"""
Use the currently active scope to find the prototype. , r=jst sr=brendan
""",
u"""
Fixing . Expose a faster way of getting the subject principal, and use that from performance critical code. r+sr=mrbkap@gmail.com
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
JavaScript Tests - revert known failures due to bugs 393267, 399587 being backed out. not part of the build
""",
u"""
The last backout introduced some mochitest orange.  Let's see whether backing out as well fixes that.
""",
u"""
Backing out mrbkap's fix for , in the hope of fixing and perhaps .
""",
u"""
NPOTB assertion for Date's 'friend' API, plus comments (410647, r=bclary).
""",
u"""
Back out patch for because its suspected of causing the fxdbug-win32-tb orange
""",
u"""
Comment nit-pick.
""",
u"""
: make sure that the generator cleanup code is called on all code paths. r,a=brendan
""",
u"""
: switching to new operation counting API. r=jst a=beltzner
""",
u"""
: New operation counter API to replace branch callback. r,a=brendan
""",
u"""
JavaScript Tests - regression test for , not part of the buidl
""",
u"""
XML/XMLList need toSource love (410192, r=mrbkap).
""",
u"""
- XPConnect should never allow GC off the main thread, r=mrbkap sr=jst a=luser
""",
u"""
Fix silly think-o from , r=lumpy
""",
u"""
JavaScript Tests - update known failures due to fixes in , , not part of the build
""",
u"""
Preserve interesting attributes on same-origin XOWs. , r+sr=jst a=beltzner
""",
u"""
Add a way to find all of the XOWs for an object and use it to deal with hard cases where we have to clear the scope of XOWs in order to reflect changes to the underlying object. Also deal with objects moving between scopes by ensuring that we're always able to find their XOWs. , r+sr=jst
""",
u"""
Make enumeration over SJOWs walk the prototype chain. Also make SJOWs unwrap same-origin XOWs. , r+sr=jst
""",
u"""
Allow chrome to use SJOWs. , r+sr=jst
""",
u"""
. Native JSON support. r=crowder/jst, sr=brendan
""",
u"""
JavaScript Tests - regression tests for , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - record additional fixes from in known failure list, not part of the build
""",
u"""
Backing out igor's fixes for and in an attempt to fix Tinderbox tgfx failures that are keeping talos red
""",
u"""
JavaScript Tests - record fixes from in known failure list, not part of the build
""",
u"""
: using operation counting API instead of the branch callback. r,sr=jst
""",
u"""
: new operation callback API to replace branch callback. a,r=brendan
""",
u"""
Do not propagate our toString function onto the wrapped objects. , r+sr=jst
""",
u"""
Add mochitests for and r=bzbarsky
""",
u"""
Add crashtest
""",
u"""
Add crashtest
""",
u"""
Useless null check of jsdscript in _destroyJSDScript r=gijs sr=bz a=dsicore
""",
u"""
Kick the stupid Windows tinderbox.
""",
u"""
JavaScript Test - add additional tests for Function constructor, , not part of the build
""",
u"""
. js_DoubleToECMA(u)Int32 should return jsdouble, not a useless always-true JSBool. r/a=brendan
""",
u"""
: check for missing return when parsing a function body in one place. r,a=brendan
""",
u"""
Don't resolve things on SJOW's prototype and make toString on it work again. , r+sr=jst a=beltzner
""",
u"""
Give the JS engine some knowledge of wrappers so that they can compare equal and be noticed when they take part in __proto__ cycles; this was supposed to land before. , r=brendan sr=dveditz
""",
u"""
. js_DoubleToECMA(u)Int32 has an unused cx param. r/a=brendan
""",
u"""
JavaScript Tests - update list of known failures, no bug, not part of the build
""",
u"""
JavaScript Tests - update tests to reflect changed behavior due to 
""",
u"""
Fix this test to deal with the new error that's being thrown.
""",
u"""
Don't fix typename bindings without JS2 opt-in (409252, r=mrbkap).
""",
u"""
Give the JS engine some knowledge of wrappers so that they can compare equal and be noticed when they take part in __proto__ cycles. , r=brendan sr=dveditz
""",
u"""
Use two flags for filenames: "system" and "want native wrappers". , r=jst sr+a=brendan
""",
u"""
: avoid storing references to the global scope in the compiled scripts. r,a=brendan
""",
u"""
Make peek-on-same-line actually work correctly. , r=brendan (NPOTB)
""",
u"""
- Compile Spidermonkey with -Os on Mac, r=bsmedberg, no approval needed, NPOTB
""",
u"""
missing last character when using readline() on files. , r=crowder a=brendan
""",
u"""
Sync XPCSafeJSObjectWrapper with similar fixes that we took for XPCNativeWrapper. , r+sr=jst
""",
u"""
Make |foo instanceof XOW| work as expected. , r+sr=jst
""",
u"""
Work around weird behavior from JS_NewObject when we pass it a parent. , r=jst sr=brendan
""",
u"""
Fixing orange.
""",
u"""
Fixing bustage.
""",
u"""
Fixing . Make XPConnect string argument handling code use stack space for string wrappers rather than to heap allocate them for each string argument. r+sr=bzbarsky@mit.edu
""",
u"""
JavaScript Tests - handle 'race' in some Date tests, not part of the build
""",
u"""
JavaScript Tests - relax randomness check for to prevent spurious failures
""",
u"""
Remove DUMP_CALL_TABLE (preliminary patch for 365851, r=igor).
""",
u"""
- Suboptimal code in array_sort implementation, code by Igor Bukanov, r=crowder
""",
u"""
JavaScript Tests - regression test for must call jsTestDriverEnd() after reportCompare(), not part of the build
""",
u"""
JavaScript Tests - regression test for must call jsTestDriverEnd() after reportCompare(), not part of the build
""",
u"""
- "JSAPI should assert if embedding omits JS_ClearContextThread" [p=jorendorff@mozilla.com (Jason Orendorff) r+a1.9=brendan]
""",
u"""
. Nightlies should not override module-specific build settings. r=ted.mielczarek.
""",
u"""
Fixing . Make the JSObject for XPConnect wrappers that have classinfo share maps with their prototypes. r+sr+a=brendan@mozilla.org
""",
u"""
JavaScript Tests - update known failures, no bug, not part of the build
""",
u"""
JavaScript Tests - regression tests for , not part of the build
""",
u"""
JavaScript Tests - regression tests for , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression tests for , not part of the build
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Gavin Sharp, not part of the build
""",
u"""
Fix warning introduced by patch for , r=jst.
""",
u"""
- Huge Speed Drop in Array.prototype.sort, patch by Igor Bukanov <igor@mir2.org>, r=crowder, approval1.9 by beltzner
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
Back out last rev due to orange tboxen.
""",
u"""
Fixing . Make JSObjects share their prototypes scope (map) even if their ops differ, as long as their newObjectMap hooks are the same. r+a=brendan@mozilla.org
""",
u"""
. increase size of regexp arena to avoid unnecessary additional allocations. r=crowder
""",
u"""
Fixing . Make doGetObjectPrincipal() faster. r+sr=bzbarsky@mit.edu, r+a=brendan@mozilla.org
""",
u"""
JavaScript Tests - remove DST start/end ambiguity, r=igor, , not part of the build
""",
u"""
: backing out the check in due to regression failures.
""",
u"""
: avoid storing references to the global scope in the compiled scripts. r,a=brendan
""",
u"""
JavaScript Tests - remove fixes from known failures due to 
""",
u"""
Reflecting arguments in Call must happen irrespective of JSRESOLVE_ASSIGNING (396584, r=igor).
""",
u"""
Don't give Iterator a fixed global binding (407957, r=jwalden).
""",
u"""
-- Backed out due to mochitest failures -- crowder
""",
u"""
- Huge Speed Drop in Array.prototype.sort, patch by Igor Bukanoc <igor@mir2.org, r=crowder
""",
u"""
- "Assertion failure: (c2 <= cs->length) && (c1 <= c2)" with /[\[-h]/i, r=mrbkap, a=blocking1.9
""",
u"""
: eval with function statements adds the function to the proper var object. r,a=brendan
""",
u"""
- "Tearing down rt->unitStrings too early leads to incorrect free later" [p=jorendorff@mozilla.com (Jason Orendorff) r=igor a1.9=brendan a=blocking1.9+]
""",
u"""
: Runtime option to switch to UTF-8 encoding in byte <-> jschar conversiions. Patch from Sam Ruby with some changes by me. r,a=brendan
""",
u"""
. XPCJSContextStack::Push doesn't need to allocate as much as it does.  use an nsAutoTArray<> instead.  r/sr=jst
""",
u"""
. stack allocate small strings in js_XDRStringAtom instead of instead of using the tempPool arena to allocate them.  r=brendan,igor
""",
u"""
- Speed up GetSecurityManager() in our XOW code [p=jst@mozilla.org (Johnny Stenback [jst]) r+sr=sicking a=blocking1.9+]
""",
u"""
- Speed up GetScopeOfObject() [p=jst@mozilla.org (Johnny Stenback [jst]) r+sr=sicking a=blocking1.9+]
""",
u"""
backout due to test failures
""",
u"""
Back out jst's patch from to see if it fixes qm-centos5-01's mochitest failures.
""",
u"""
Fixing . Speed up GetScopeOfObject(). r+sr=jonas@sicking.cc
""",
u"""
Fixing . Speed up GetScopeOfObject(). r+sr=jonas@sicking.cc
""",
u"""
Fixing . Speed up GetSecurityManager() in our XOW code. r+sr=jonas@sicking.cc
""",
u"""
JavaScript Test - update regression test for due to changes in , not part of the build
""",
u"""
Sisyphus - cause test run to fail immediately if Spider fails to install properly, , not part of the build
""",
u"""
followup fix: make Error readonly/permanent, patch by Brendan Eich <brendan@mozilla.org>, r=jwalden, a=schrep for M10 landing
""",
u"""
JavaScript Tests - regression tests for , 371636, by Brendan Eich, Igor Bukanov, not part of the build
""",
u"""
: simple code now causes a slow script warning dialog to appear when it didn't before (fix bad regression in the global variable optimizer), patch by Igor Bukanov <igor@mir2.org>, r=brendan, a=schrep for M10 landing
""",
u"""
- "JSOP_NEWINIT lacks SAVE_SP_AND_PC" [p=igor@mir2.org (Igor Bukanov) r+a1.9=brendan aM10=damons]
""",
u"""
JSCLASS_FIXED_BINDING only on Namespace, for better backward and forward compat (407323, r=jwalden).
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman, Rich Dougherty, not part of the build
""",
u"""
JavaScript Tests - test regression from , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Franck, Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov, not part of the build
""",
u"""
- Fatal JS_Assert "JSVAL_IS_NUMBER(pn3->pn_val) || JSVAL_IS_STRING(pn3->pn_val) || JSVAL_IS_BOOLEAN(pn3->pn_val)", patch by Igor Bukanov <igor@mir2.org>, r=brendan, approvalM10=schrep
""",
u"""
Sisyphus - JavaScript Tests - update kernel identification and known failures, , not part of the build
""",
u"""
JavaScript Test - add missing test for , by Brendan Eich, not part of the build
""",
u"""
: dtrace can compile again. Patch from Alfred Peng, r=myself, a1.9,aM10=beltzner.
""",
u"""
JavaScript Tests - update regression test for due to , not part of the build
""",
u"""
: quelling GCC unitialized overwarning. r,a=brendan aM10=dsicore
""",
u"""
: UTF-8 encoded scripts that contain a BOM result in an "illegal character" error, r=mrbkap, r=brendan, a=schrep
""",
u"""
Backing this out to fix mochitest failures.
""",
u"""
Preserve more important attributes. , r+sr=jst a=beltzner
""",
u"""
Complete the checkin for . r+sr=jst
""",
u"""
Set XOWs' prototypes to null to avoid confusion. , r+sr=jst a=beltzner
""",
u"""
: fixing the test to report the success with read-only Array. r=Bob Clary, not part of the build
""",
u"""
: The decompiler output no longer depend on JS_C_STRINGS_ARE_UTF8 for uniformity. a,r=brendan
""",
u"""
: extra patch to move the switch case for CALL_PROP to a beter place in the source. r,a=brendan
""",
u"""
: making sure that we can compile with !JS_HAS_XML_SUPPORT. a,r=brendan
""",
u"""
JavaScript Tests - update known failure list, , not part of the build
""",
u"""
Kick the stupid Windows test box.
""",
u"""
- Prevent data leaks from cross-site JSON loads (JavaScript literals), by making the global name bindings ReadOnly/DontDelete and making [] and {} use the global bindings.  Still more that can be done here, but this covers a lot of the fix.  r+a=brendan
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
- "Cast needed in jsfun.c (C++ compatibility)" [p=jorendorff@mozilla.com (Jason Orendorff) r=igor a1.9=damons]
""",
u"""
: support optional arguments in idl; follow-up patch to address reading absent optional arguments from argv. r=enndeakin, sr=jst, a=mtschrep
""",
u"""
- "Allow using chrome:// URLs in Components.utils.import()" [p=ajvincent@gmail.com (Alex Vincent) r=sayrer sr=bsmedberg a1.9=damons]
""",
u"""
Back out WeirdAl's patch from to see if it caused the perf regression on Linux.
""",
u"""
- "Allow using chrome:// URLs in Components.utils.import()" [p=ajvincent@gmail.com (Alex Vincent) r=sayrer sr=bsmedberg a1.9=damons]
""",
u"""
Sisyphus - JavaScript Tests - additional kernel pattern for CentOS5 VM
""",
u"""
: No compiler pseudo-frames when compiling functions. r,a=brendan
""",
u"""
- "IE Array sort on numbers using default string comparator is 5x faster" [p=igor@mir2.org (Igor Bukanov) r+a1.9=brendan a=blocking1.9+]
""",
u"""
- fixing memory leak resulted from [p=igor@mir2.org (Igor Bukanov) r+a1.9=brendan]
""",
u"""
Back out Igor's patch from to see if it fixes the orange.
""",
u"""
- js.c has an unmatched fopen() resource leak, r=igor (not part of the build)
""",
u"""
: fixing memory leak resulted from . a,r=brendan
""",
u"""
Sisyphus/JavaScript Tests - cleanup log summary and TinderboxPrint output for Buildbot/Tinderbox, , not part of the build, r=rcampbell
""",
u"""
Make XOW's toString consistent over all cases. , r=jst sr=bzbarsky a=beltzner
""",
u"""
Don't use a prototype to do any work, just do it ourselves. , r=jst sr=brendan a=blocking-1.9
""",
u"""
Actually throw if the thrown thing was not an nsresult. , r+sr+a=jst
""",
u"""
Landing fix for . Fixing problem with setting __proto__ on objects with XOW's on its prototype chain. Patch by mrbkap@gmail.com, r=jst@mozilla.org, sr=brendan@mozilla.org
""",
u"""
Sisyphus/JavaScript Tests - add option -S to runtests.sh to provide simpler output for Buildbot/Tinderbox, , r=rcampbell
""",
u"""
JavaScript Tests - update test for to use regexps to match 1.8 and 1.9.0 behaviors, not part of the build
""",
u"""
: using custom storage for function argument and variable names. r,a=brendan
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
- jsshell tracing() appears to work in JS_THREADED_INTERP builds but doesn't.  r+a=brendan
""",
u"""
: patch from Jason Orendorff to restore C++ compatibility. r=myself a=brendan
""",
u"""
: consistently using JS_ARRAY_LENGTH macro. r,a=brendan
""",
u"""
JavaScript Tests - update known failures due to  , not part of the build
""",
u"""
JavaScript Tests - regression test for by Jesse Ruderman, update regression tests due to  , not part of the build
""",
u"""
: report exhausting of the script memory quota as ordinary runtime exceptions. r=brendan, a1.9=beltzner
""",
u"""
: fixing the regression in the decompiler from landing of bug	398609. r,a=brendan
""",
u"""
- Replacing js_InternalCall with js_Invoke in Array.sort for arrays with scripted compator functions (save alloc/free on each compare) [p=crowder@fiverocks.com (Brian Crowder) r=igor a=blocking1.9+]
""",
u"""
- Backing out, potentially caused orange on test tinderbox
""",
u"""
: jsfile.c fails to compile, patch by Jeff Watkins <jeff.watkins.spam@gmail.com> r=crowder, a=not part of the build
""",
u"""
- Replacing js_InternalCall with js_Invoke in Array.sort for arrays with scripted compator functions -- save alloc/free on each compare r=ibukanov, a=blocking1.9+
""",
u"""
JavaScript Tests - jsDriver.pl -k|-K fail to report test failures, , r=igor, not part of the build
""",
u"""
JavaScript Tests - update public-failures.txt, spidermonkey-extensions-n.tests, 
""",
u"""
Sisyphus - JavaScript Tests auto create known failure patterns, 
""",
u"""
JavaScript Tests - update tests to reflect changing error messages, 
""",
u"""
: simpler handling of hidden properties, r,a=brendan
""",
u"""
JavaScript Tests - handle race in some Date tests, 
""",
u"""
Sync declaration of js_TraceFunction with definition.
""",
u"""
: GC thing callback is removed. r,a=brendan
""",
u"""
: backing out due to test failures.
""",
u"""
: cleanup of hidden properties support. r,a=brendan
""",
u"""
Fix for (Replacing GCX_PRIVATE by GCX_FUNCTION). r=igor, sr=jst, a=schrep.
""",
u"""
- "(new Date).toLocaleFormat("%D") crashes Minefield" [p=mats.palmgren@bredband.net (Mats Palmgren) r=crowder a=blocking1.9+]
""",
u"""
- "mozilla-central: jsatom.cpp has bad casts in 64-bit OS" [p=benjamin@smedbergs.us (Benjamin Smedberg) r=igor a1.9=schrep]
""",
u"""
Merging from cvs-trunk-mirror to mozilla-central.
""",
u"""
- "xpcshell core dump when shutdown" [p=solar@netease.com (Solar) r=igor a=blocking1.9+]
""",
u"""
relanding since it doesn't look to be the source of the Ts regression
""",
u"""
Back out the patch for to see whether it caused the Ts regression, a=sicking
""",
u"""
JavaScript Tests - regression tests for , semicolon insertion, not part of the build
""",
u"""
Propagate end position in all cases parsing a parenthesized expression (402386, r=mrbkap/a=schrep).
""",
u"""
: objects can be marked as system only during creation. r,a=brendan
""",
u"""
: removing JSParseNode.pn_ts. r,a=brendan
""",
u"""
: removal of dependency of xpconnect on internal JS GC thing types. r,a=brendan
""",
u"""
JavaScript Tests - regression test for , not part of the build
""",
u"""
: Backing out due to mochi test failure.
""",
u"""
: cleanup of hidden properties. r,a=brendan
""",
u"""
- "Thread-unsafe updates to sub-atomic rt->gc{Poke,Zeal}" [p=crowder r=igor a1.9=brendan]
""",
u"""
- "new Date (1899, 0).toLocaleString() causes abnormal program termination if compiled with VC 8" [p=mats.palmgren@bredband.net (Mats Palmgren) r=crowder a=blocking1.9+]
""",
u"""
- "Need JS_AlreadyHasOwnProperty (UCProperty, Element)" [p=crowder r+a1.9=brendan]
""",
u"""
- "ISO 8601 dates helper" [p=erwan@flock.com (Erwan Loisant) r=sayrer sr=mscott a1.9=damons]
""",
u"""
- "Date toLocaleString() clamps the year to -32767 .. 32767" [p=mats.palmgren@bredband.net (Mats Palmgren) r=crowder a1.9=schrep]
""",
u"""
- ""has no properties" is misleading and should be replaced with "is null or undefined"" [p=rich@rd.gen.nz (Rich Dougherty) r=brendan r=crowder a1.9=damons]
""",
u"""
Undoing accidental backout of the fix for .
""",
u"""
- "Including jsapi.h generates many warnings with certain compiler configurations (e.g. gcc 3.4 -Wstrict-prototypes)" [p=wes@page.ca (Wesley W. Garland) r=mrbkap a1.9=brendan]
""",
u"""
: better handling of long jumps in the bytecode. r,a=brendan,aM9=beltzner
""",
u"""
: fixing iteraction between gczeal mode and scripts. r,a=brendan, aM9=beltzner
""",
u"""
copy WINNT5.2 config for vista, npotb, r=crowder
""",
u"""
Fix for (Cycle collection crashes with Leak Monitor extension installed). Pending-r=sicking, sr=jst, a=dsicore.
""",
u"""
Fix for (Crash with Venkman profiling [@ JS_IsSystemObject]). r=igor, pending-sr=jst.
""",
u"""
: Don't remove an XPCTraceableVariant from root set in dtor if it has already been done during unlinking. Patch by peterv. r/sr=sicking
""",
u"""
Fix post-increment/decrement automatic semicolon insertion bug (401466, r=mrbkap).
""",
u"""
Fix crash from patch for (Stop refcounting JS objects in the cycle collector). r/sr=jst, a=dsicore@mozilla.com.
""",
u"""
- "support building with dtrace enabled on Mac OS X" [p=Ryan r=luser aM9=schrep]
""",
u"""
Fixing solaris bustage from . r+sr=jonas@sicking.cc
""",
u"""
Landing patch for . Stop reference counting JS objects in the cycle collector. Patch by peterv@propagandism.org, r+sr=dbaron@mozilla.com,igor@mir2.org, a=dsicore@mozilla.com
""",
u"""
Sisyphus|JavaScript Tests - remove need to parallel dir structure of tests into results, , r=rcampbell, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Blake Kaplan, not part of the build
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
Fix conditional expressions (401405, r=mrbkap).
""",
u"""
Part 1 of fix for (using trace API for reference counts) and (cycle collector faults after tracing "JS object but unknown to the JS GC"). r=igor/jst, sr=jst, a=blocking1.9+/M9 (for ).
""",
u"""
Backing out once more to fix orange.
""",
u"""
Part 1 of fix for (using trace API for reference counts) and (cycle collector faults after tracing "JS object but unknown to the JS GC"). r=igor/jst, sr=jst, a=blocking1.9+/M9 (for ).
""",
u"""
: new shell function gcparam as a wrapper for JS_SetGCParameter. r=brendan. Browser builds do not use the file.
""",
u"""
: Don't report bogus warnings to the error console when using cross-site xmlhttprequest. Patch by Surya Ismail <suryaismail@gmail.com>, r/sr=sicking
""",
u"""
Backing out to fix orange.
""",
u"""
Part 1 of fix for (using trace API for reference counts) and (cycle collector faults after tracing "JS object but unknown to the JS GC"). r=igor/jst, sr=jst, a=blocking1.9+/M9 (for ).
""",
u"""
- "JS XPCOM component exception handled by native code shows up in error console" (don't report nsresult exceptions thrown from JS) [p=mrbkap r+sr=jst aM9=beltzner]
""",
u"""
: proper check for duplicated parameter names in xdr decoder. r=brendan,mrbkap a=brendan aM9=beltzner
""",
u"""
JavaScript Tests - update public-failures.txt 2007-10-24, , not part of the build
""",
u"""
Sisyphus - add -v verbose output switch, , r=rcampbell, not part of the build
""",
u"""
Landing fix for . Adding Dtrace probes to the JS engine. Patch by padraig.obriain@sun.com and brendan@sun.com, and some intergration work done by jst@mozilla.org. r=brendan@mozilla.org, igor@mir2.org, sayrer@gmail.com, and r+a=ted.mielczarek@gmail.com.
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - update public-failures.txt, , not part of the build
""",
u"""
Include $ and _ in identifier chars (still to do: Unicode alnums and escapes); based on patch from Frankie Robertson <frankierobertson5@googlemail.com> (399625, r=mrbkap).
""",
u"""
Fix from Frankie Robertson <frankierobertson5@googlemail.com> to Node toString (399659, r/a=me).
""",
u"""
- Can't build mozilla-central on 64-bit OS because of pointer-to-int32 casts which are ok in C but not in C++, r=igor
""",
u"""
Merge cvs-trunk-mirror -> mozilla-central
""",
u"""
ActionMonkey: Remove "extra" parameter to JS_FN patch by Jason Orendorff <jorendorff@mozilla.com> r=igor a=brendan
""",
u"""
Fixing . Make sure to initialize LiveConnect (if needed) when loading applets. r+sr+a=jonas@sicking.cc
""",
u"""
JavaScript Tests - copy regular expression testing utilities from RegExp to extensions subsuite, , not part of the build
""",
u"""
JavaScript Tests - update spidermonkey-extensions-n.tests, , not part of the build
""",
u"""
JavaScript Tests - move tests of non-standard features to extensions, , not part of the build
""",
u"""
JavaScript Tests - move tests of non-standard features to extensions, , not part of the build
""",
u"""
JavaScript Tests - move tests of non-standard features to extensions, , not part of the build
""",
u"""
JavaScript Tests - move tests of non-standard features to extensions, , not part of the build
""",
u"""
JavaScript Tests - move tests of non-standard into extensions, 
""",
u"""
JavaScript Tests - update public-failures.txt, , not part of the build
""",
u"""
JavaScript Tests - regression test for bugs 291494, 395836, not part of the build
""",
u"""
JavaScript Tests - move js1_5/Date/toLocaleFormat.js to js1_5/extensions/toLocaleFormat-01.js, , not part of the build
""",
u"""
JavaScript Tests - update regression tests for , by Michael Daumling, Mats Palmgren, not part of the build
""",
u"""
Restore dynamic indirect eval code. , r=brendan/igor a=brendan
""",
u"""
- backed out "patch with nits fixed" due to perf regressions
""",
u"""
Oops, removing windows line endings I accidentally checked in when fixing .
""",
u"""
Merge from cvs-trunk-mirror to mozilla-central.
""",
u"""
- "Wrappers don't deal with non-native objects". Patch by Blake Kaplan <mrbkap@gmail.com>, r+sr+a=jst.
""",
u"""
Wrap the strftime() call with an empty "invalid parameter handler" on Windows. b=395836, patch by Mats Palmgren <mats.palmgren@bredband.net>,  r=crowder a=brendan
""",
u"""
Don't call setters if there is no setter to call. , r=brendan sr=jst a=blocking1.9+
""",
u"""
JavaScript Test - ignore XPCCrossOriginWrapper on global object, , not part of the build
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov, not part of the build
""",
u"""
- mozilla-central has pedantic errors because of extra commas, r=mrbkap+brendan a=brendan
""",
u"""
JavaScript Tests - update Sisyphus related shell scripts to use /bin/bash, , not part of the build
""",
u"""
JavaScript Tests - update regression test to support Rhino, , by Norris Boyd, not part of the build
""",
u"""
Update JS_GetImplementationVersion to 1.8.0 on trunk, , ra=brendan
""",
u"""
: JSTokenStream is stored in JSParseContext. r=brendan
""",
u"""
Backing out the patch 397210.
""",
u"""
: JSTokenStream is stored in JSParseContext. r=brendan
""",
u"""
: the system flag is moved from GC flags to JSObject itself. r=brendan
""",
u"""
JavaScript Tests - sync Sisyphus support, , not part of the build
""",
u"""
Propagate exceptions from the evalcx context to the outer context so they can be caught. , r+a=brendan
""",
u"""
Implement an iterator hook for cross origin wrappers to avoid wrongly walking up the prototype chain during enumeration. , r+a=brendan sr=jst
""",
u"""
evalcx uses JS_BeginRequest/JS_EndRequest. , r=mrbkap, not a part of the build.
""",
u"""
JavaScript Tests - update spidermonkey-extensions-n.tests, , not part of the build
""",
u"""
JavaScript Tests - fix emca 262 section, , not part of the build
""",
u"""
- "performance improvements for JSON.jsm" (optimize string serialization) [p=zeniko@gmail.com (Simon Bunzli) r=sspitzer sr=brendan a1.9=mconnor]
""",
u"""
JavaScript Tests - fix false negatives due to embedded "false!" in output, , r=jorendorff, not part of the build
""",
u"""
: taking the patch out as it broke the test cases.
""",
u"""
: the system flag is moved from GC flags to JSObject itself. r=brendan
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression tests for , by Brendan Eich, not part of the build
""",
u"""
- Need a JSAutoRequest in xpcJSWeakReference::Init. r=brendan, sr+a=jst.
""",
u"""
Fix obsolete test and add a new test to fix orange.
""",
u"""
Only allow XOW wrapped prototypes to go to null, not other objects. , r+sr+a=brendan
""",
u"""
Fix Convert to work for JSTYPE_VOID and make sure it reports an error. , r=jst sr=brendan
""",
u"""
Fix old bug where we wouldn't close ts after a compilation error. , r+a=brendan
""",
u"""
JavaScript Test - regression test for , by Norris Boyd, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Eli Friedman, not part of the build
""",
u"""
Merge cvs-trunk-mirror to mozilla-central.
""",
u"""
Fix order of evaluation bug in bitwise and shift ops (396969, r=igor).
""",
u"""
- FLAGP_TO_THING bustage from C++, r+a=brendan
""",
u"""
- Fix const issues with strchr in C++ (when used in mozilla-central), r=mrbkap, a=brendan
""",
u"""
Merge cvs-trunk-mirror to mozilla-central
""",
u"""
: merge sweep and free phases in GC. r=brendan
""",
u"""
: avoid recursion with long chains of "||" or "&&" in JS code. r=brendan
""",
u"""
: fixing regression from in js_Invoke. r=brendan
""",
u"""
. Fix JS Request assert in nsXPCComponents_Utils::LookupMethod. r/sr/a=brendan
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
. Enforce SpiderMonkey request model with assertions. r=mrbkap, sr/a=brendan
""",
u"""
- Fix minor errors in XPCOMUtils.jsm.  Patch by Manish Singh <manish@flock.com>, r1=gavin, r2=sayrer
""",
u"""
JavaScript Test- regression test for , by Jesse Ruderman
""",
u"""
Give scx a global object so that we can always calculate a "this" object. , r+a=brendan
""",
u"""
: no JS frames for fast native calls. r=brendan
""",
u"""
: the last ditch GC gcPoke checks are moved to js_NewGCThing. r=brendan
""",
u"""
Back-out due to test failure.
""",
u"""
Make GCF_SYSTEM immutable per object (396487, r=igor).
""",
u"""
: mark the property only when tracing from GC. r=brendan
""",
u"""
: taking out the last patch as broke Windows build.
""",
u"""
Actually use an escape for the nul character. , r+a=brendan
""",
u"""
: no JS frames for fast native calls. r=brendan
""",
u"""
Merge from CVS trunk to mozilla-central.
""",
u"""
JavaScript Test - regression test for , by Martin Honnen, not part of the build
""",
u"""
JavaScript Tests - regression tests for , by Seno Aiko, not part of the build
""",
u"""
: patch from Seno Aiko to use thr proper bytecode flags. r=mrbkap
""",
u"""
: using mmap/VirtualAlloc for GC arenas. r=brendan
""",
u"""
: taking out the patch due to .
""",
u"""
Backing out patch by Mook from due to compile errors.
""",
u"""
- "Let nsIXPConnect::debugDumpJSStack take a file" [p=Mook r=bsmedberg sr=bzbarsky a1.9=jst]
""",
u"""
: using mmap/VirualAlloc for GC arenas. r=brendan
""",
u"""
Create a JSClass hook to allow object classes to easily support custom iteration without having to override __iterator__ in a resolve hook. , r+a=brendan
""",
u"""
Treat the pseudo frame even more like a real frame. , r+a=brendan
""",
u"""
: taking out the patch due to Mac build problems.
""",
u"""
: using mmap/VirualAlloc for GC arenas. r=brendan
""",
u"""
Fix old bug involving eval of a local function named by an existing local var (395907, r=mrbkap).
""",
u"""
. XPCVariant::VariantDataToJS leaks strings with sizes. r/sr=jst
""",
u"""
Fix dumb signed comparison bug (395828, r=mrbkap).
""",
u"""
Merge from cvs-trunk-mirror
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov, not part of the build
""",
u"""
- Fast-path QueryInterface in XPCWrappedNative::CallMethod, r=mrbkap sr=jst a=damons
""",
u"""
JavaScript Tests - regression test for devmo example, by Norris Boyd, , not part of the build
""",
u"""
JavaScript Test - add additional case to test, by Norris Boyd, , not part of the build
""",
u"""
Back out patch for because it caused (a=schrep/bsmedberg)
""",
u"""
: fixing memory leak with watch handlers. r+a=brendan
""",
u"""
: countHeap function for js shell and help() cleanup. r=brendan
""",
u"""
- Make nsJSID/IID/CID objects .equals method slightly faster, r=mrbkap sr=jst a=damons
""",
u"""
- "Assertion failure: nbytes != 0" with regexp quantifiers, r=mrbkap, a=brendan
""",
u"""
- Ship the JS import library in the SDK, and stop linking it from browsercomps which doesn't use it, r=luser a=NPDB
""",
u"""
: properly initializing JSContext for evalx. r=mrbkap. No 1.9 aproval as the file is outside browser's build tree.
""",
u"""
: do_GetFastLoadService should use nsGetServiceByCID. r=/sr=/a=bsmedberg
""",
u"""
- Cleanup from the handful of patches which have landed since the initial landing that have readded cast macros; I intend to remove the rest of the instances Very Soon, all but certainly before the M8 freeze, so the macro definitions can be removed, again all but certainly before the M8 freeze, if people are okay with them being removed.  Still r=bsmedberg, a=no-functionality-change
""",
u"""
Merge from cvs-trunk-mirror
""",
u"""
: patch from Edward Lee to fix wrong precision warning. r=myself,brendan
""",
u"""
Merge from cvs-trunk-mirror.
""",
u"""
- Backing out patch due to TXUL regression.
""",
u"""
- "xpconnect getters/setters don't have principals until after they pass or fail their security check." Patch by jst, sr=bzbarsky, a=jst.
""",
u"""
: new API to limit heap consumption by stack-like data structures used by compiler, decompiler and interpreter.
""",
u"""
: arena handling cleanup. r=brendan
""",
u"""
- Add category manager helpers to XPCOMUtils. Patch by Nickolay Ponomarev <asqueella@gmail.com>, r=sayrer/mark.finkle a=jst
""",
u"""
Merge from cvs-trunk-mirror.  This fixes , a C++ compatibility bug.  js/src now builds ok.
""",
u"""
: Patch from Jason Orendorff to restore ability to compile SpiderMonkey with C++ compiler. r=me
""",
u"""
When doing ExplainLiveExpectedGarbage, suspect all nsXPCWrappedJS so that we get more objects in the graph.  b=387224  r=graydon  a=brendan
""",
u"""
Make ExplainLiveExpectedGarbage print *all* references to JS objects with refcount imbalances.  b=387224  r=graydon  a=brendan
""",
u"""
: js_NewGCThing no longer zeros the allocated thing. r=brendan
""",
u"""
JavaScript Tests - destructuring assignment tests, by Norris Boyd, , not part of the build
""",
u"""
: fix JSON tests, patch by Simon Bunzli <zeniko@gmail.com>, r=me
""",
u"""
disable failing tests for the moment ()
""",
u"""
: create JSON utilities module and use it for search suggest/sessionstore/Places, patch by Simon Bunzli <zeniko@gmail.com>, r=sspitzer, sr+a=brendan
""",
u"""
Remove MAX_INLINE_CALL_COUNT policing, plus old MAX_INTERP_LEVEL deadwood (392973, r=crowder).
""",
u"""
: XDR uses lossless encoding for all string. r=brendan
""",
u"""
Merge from cvs-trunk-mirror
""",
u"""
One-char fix to recent regression (392944, r=mrbkap).
""",
u"""
JavaScript Tests - update spidermonkey-gc.tests, , by Jason Orendorff, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Norris Boyd, not part of the build
""",
u"""
Get the right class -- off of obj2, not obj and ensure that we propagate failure from outerObject. , r=brendan a=sicking
""",
u"""
- mkdepend takes more than 10 hours on Solaris for nsIconChannel.cpp.  Patch by Ginn Chen <ginn.chen@sun.com>, r=cls, a=bz
""",
u"""
Get the right property attributes and actually look up the prototype chain. , r+sr+a=jst
""",
u"""
merging from cvs-trunk-mirror
""",
u"""
: mutability flag for strings is stored inside strings. r=brendan
""",
u"""
JavaScript Test - regression test for , by Norris Boyd, not part of the build
""",
u"""
JavaScript Test - regression test for , by nanto_vi (TOYAMA Nao), not part of the build
""",
u"""
Allow 'this' to not be a wrapped object. , r+sr+a=jst
""",
u"""
Make XPCSafeJSObjectWrapper usage in PAC actually work correctly for the common case. , r=jst sr+a=brendan
""",
u"""
Don't assume that all XOWs are equal. , r+sr=jst
""",
u"""
Don't wrap everything that comes out of a wrapped function, if that function is same-origin. , r+sr+a=jst
""",
u"""
: restoring pinning of the lazy atoms to fix various regressions. r=brendan
""",
u"""
Implement correct semantics of storage class (global, var, let) for destructuring assignment.
""",
u"""
Fix compile warning. No bug, r+a=brendan
""",
u"""
Date.UTC returns incorrect value if date is less than or equal to 0. , patch from jag, r=mrbkap a=brendan
""",
u"""
: JS_IS_VALID_TRACE_KIND no longer refers to the removed JSTRACE_ATOM. r=brendan
""",
u"""
: js_PutEscapedStringImpl gets JS_FRIEND to permit usage outside js lib. r=brendan
""",
u"""
: JS_ResolveStandardClass now does nothing on shutdown. r=brendan
""",
u"""
Update #if 0'd code to work (helpful for debugging; r/a=self).
""",
u"""
: using double kashing for atoms. r=brendan
""",
u"""
: no frame manipulation when reporting errors. r=brendan
""",
u"""
Fix leak in DEBUG-only code.  b=391769  r+sr+a=jst
""",
u"""
- failed to build Spidermonkey: inresolved symbol ( prmjtime.c PRMJ_Now _SetCriticalSectionSpinCount _InitializeCriticalSectionAndSpinCount ).  Patch by Rob Arnold <robarnold@mozilla.com>, r=brendan, r=bsmedberg
""",
u"""
merging from cvs-trunk-mirror
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, not part of the build
""",
u"""
Finish the deflated string cache after uninterning atoms, so we don't leak their associated strings.  b=391587  r+a=brendan
""",
u"""
- Reposition JS_(BEGIN|END)_EXTERN_C to avoid nesting #includes.  Patch by Edward Lee <edilee@mozilla.com>, r=jorendorff, r=bsmedberg
""",
u"""
Fixing . Make setTimeout() always register the timeout on the right inner window, and add a new JS_GetGlobalForObject() JS API to eliminate some code duplication. r=mrbkap@gmail.com/brendan@mozilla.org, sr=bzbarsky@mit.edu
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, not part of the build
""",
u"""
JavaScript Tests - regression tests for , by moz_bug_r_a4, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
: patch from Rich Dougherty to name constitently JOF_* flags. r=me
""",
u"""
JavaScript Tests - regression test for , by shutdown, not part of the build
""",
u"""
JavaScript Tests - regression tests for , by shutdown, Blake Kaplan, not part of the build
""",
u"""
Try harder to find a scope chain so that we can report exceptions when there is no code running currently. , r=brendan sr=jst a=brendan
""",
u"""
Add a mochitest for __parent__ wrapping.
""",
u"""
Add a mochitest for . r=sayrer sr=bzbarsky
""",
u"""
De-confuse GetWrappedNativeOfJSObject about wrappers around the outer object. , r+sr=jst
""",
u"""
Allow UniversalXPConnect scripts to touch XPCNativeWrappers. , r+sr=bzbarsky a=jst
""",
u"""
Make XPCSafeJSObjectWrapper easier to use by not throwing for primitive values passed to the constructor. Use it in more places in PAC. , r=crowder sr=brendan a=bzbarsky
""",
u"""
- error for {return;} isn't helpful, patch by Rich Dougherty <rich@rd.gen.nz>, r=brendan
""",
u"""
, : multithreading atom fixes and cleanups. r=brendan
""",
u"""
. XPCWrappedNativeScope leaks a WrappedNative2WrapperMap. r=brendan/mrbkap, sr=brendan, a=jst
""",
u"""
Don't set aside the JS stack when pushing a JSContext which is already on top of the JSContext stack on top of itself.  , r=jst, sr=brendan, a=jst
""",
u"""
merging from cvs-trunk-mirror
""",
u"""
rename js/src/*.c back to .cpp to restore hg's knowledge of the rename
""",
u"""
- Expose cycle-collection symbols, r=graydon
""",
u"""
JavaScript Tests - regression test for , not part of the build
""",
u"""
JavaScript Tests - updated tests for JS1_8 by Igor Bukanov, , not part of the build
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman, Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman, Igor Bukanov, not part of the build
""",
u"""
JavaScript Tests - new version of test to reflect removal of close phase of GC in in JS18, by Igor Bukanov, not part of the build
""",
u"""
: fixing gen_trace assert. r=brendan
""",
u"""
- js_strtod and js_strtointeger no longer require null-terminated js chars. r=brendan
""",
u"""
: pinning of JSAtomState.emptyAtom is restored. r=brendan
""",
u"""
Cope with stillborn funobj tracing via newborn root (390743, r=igor).
""",
u"""
Fix leak of JSScript when a JSFunction is collected in a later GC than its function object.  This changes GCX_PRIVATE to GCX_FUNCTION, and is essentially the same as the finalization part of the changes from (by igor).  b=389757  r=igor  a1.9=brendan
""",
u"""
: Avoiding unnecessary GC-tracing of JSStackFrame members. r=brendan
""",
u"""
- mingw build error - error: no matching function for call to nsAutoString::nsAutoString(jschar*), r=mrbkap, sr=jst, a=jst
""",
u"""
Fix leak of xptiInterfaceInfo in DebugDump.  b=389765  r+sr=jst  a=DEBUG-only
""",
u"""
Remove an unused variable. no bug, r=sparky sr=lumpy
""",
u"""
Detect cyclic __proto__ values ourselves because the JS engine gets confused by the wrappers. , r=brendan sr=jst
""",
u"""
Remove deadlock hazard when reparenting, single-threaded DOM so don't worry (390551, r+sr=jst).
""",
u"""
Restore lost ECMA compatibility for length delegating/shadowing (390598, r=igor).
""",
u"""
Fix array_pop default return value (390684, r=igor).
""",
u"""
: baking out again accidental re-commit of the patch.
""",
u"""
: Baking out the last commit as the tree is closed.
""",
u"""
: baking out the last commit as the tree is closed.
""",
u"""
: js_strtod and js_strtointeger no longer require null-terminated js chars. r=brendan
""",
u"""
: pinning of JSAtomState.emptyAtom is restored. r=brendan
""",
u"""
: Changing the return value of js_BoyerMooreHorspool to be jsint to fix mingw compilation.
""",
u"""
Fix bogus assertion in last patch (for 385393).
""",
u"""
Fixing uninitialized v bug in InitExnPrivate (385393 followup, r=waldo).
""",
u"""
No good, un-reverting.
""",
u"""
Attempt to fix orange.
""",
u"""
Fast (frame-less) native call optimizations (385393, r=igor).
""",
u"""
Make enumeration over XOWs work. , r=jst/brendan sr=jst
""",
u"""
Let "window.eval" work again by always wrapping eval when it comes out of a cross origin wrapper. , r+sr=jst
""",
u"""
Protect vp from garbage collection, since GC could nest under several of the calls here. , r+sr=jst
""",
u"""
Don't call FindInJSObjectScope on an object that's being finalized because its parent might have been finalized already. , r+sr=jst
""",
u"""
Deal with XPCCallContexts that aren't able to initialize themselves. This also fixes bugs related to finalizing objects on dead contexts. , r+sr=jst
""",
u"""
: removal of redundant gcflags argument from string-allocation functions. r=brendan
""",
u"""
Implement cross-origin wrappers to gate accesses between sites that are cross origin. This will prevent sites from monkeying with each other by doing bad things to allAccess properties, and pave the way for more security work. , r=jst rs=brendan
""",
u"""
Fix MSVC7 build bustage from , a=gavin for checkin to closed tree
""",
u"""
Backing out, see and orange or red tinderboxes.
""",
u"""
Fast natives and related optimizations (385393, r=igor).
""",
u"""
Don't double-wrap objects when getting them out of an XPCVariant. , r=peterv sr=jst
""",
u"""
temporarily rename js/src/*.cpp to .c
""",
u"""
Fix - JavaScript Tests - global shell.js sets JavaScript version to
""",
u"""
Add more useful assertion for debugging cycle collector faults.  b=386912  r+sr=peterv
""",
u"""
Fix comment to say 'createInstance' when it really means that, since this is pointed to by devmo as API documentation; no bug; rs=shaver
""",
u"""
Fix - More reportMatch changes to generalize tests
""",
u"""
add winmm.lib to JavaScript Shell build configuration on Windows, , not part of the build. r=mrbkap
""",
u"""
merging from actionmonkey 2007/07/16 (, Always build JS as C++)
""",
u"""
, Always build JS as C++, r=benjamin
""",
u"""
merging from cvs-trunk-mirror 2007/07/13 (c++ SpiderMonkey; remove GC close phase)
""",
u"""
merging from cvs-trunk-mirror 2007/07/10
""",
u"""
merging from cvs-trunk-mirror
""",
u"""
- Build failed on solaris x86 due to checkin for 372428.  Patch by Leon Sha <leon.sha@sun.com>, r=cls
""",
u"""
Move where we convert things into strings into a more centralized place. , r=bzbarsky sr=jst
""",
u"""
: proper state checks when closing the generator. r=brendan
""",
u"""
: Followup to remove to no longer used JSGenerator.next. r=brendan
""",
u"""
Fixing build bustage.
""",
u"""
Bad millisecond resolution for (new Date).getTime() / Date.now() on Windows. , patch from Rob Arnold <robarnold@mozilla.com>, r=brendan
""",
u"""
: Taking away too zealous code simplification.
""",
u"""
: XPCOMUtils spews uuids when registering components. r=sayrer, sr=benjamin
""",
u"""
- Allow null targetObj arg to xpcIJSModuleLoader::import().
""",
u"""
synchronize documentation, Sylvain Pasche <sylvain.pasche@gmail.com>
""",
u"""
: Followup for the previous check in to remove more no longer used close-on-GC code. r=brendan
""",
u"""
: make sure that [generator] is the first bytecode. r=brendan
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov, Brendan Eich
""",
u"""
: Calling close on unreachable generators from GC is no longer supported. r=brendan
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Blake Kaplan
""",
u"""
: follow-up to fix another void* nit, patch by Edward Lee edilee@mozilla.com, r=crowder
""",
u"""
JavaScript Test - regression test for 
""",
u"""
Back out ; it broke restoring sessions in the browser.
""",
u"""
JavaScript Tests - automation updates, , not part of the build
""",
u"""
: Patch from Edward Lee to restore ability to compile SpiderMonkey with C++ compiler. It was broken after my changes. r=myself
""",
u"""
Back out ; it causes the marquee binding to throw security exceptions.
""",
u"""
Don't trust the filename of cloned functions. , r=jst sr=brendan
""",
u"""
Always return XPCSafeJSObjectWrappers from Components.utils.Sandbox and evalInSandbox. This makes this interface much, much easier to use safely, as the wrapper takes care of several common problems that occur when touching regular JS objects directly. , r=jst sr=brendan
""",
u"""
Clear dormantNext when we're done using it. , r=igor
""",
u"""
: JSAtom.number is removed in favour of using atoms itself for hashing. r=brendan
""",
u"""
Followup to to fix the alignment of trailing backslashes in macros
""",
u"""
Clean up the XDR properly even if JS_XDRScript fails.  In particular, don't
""",
u"""
Relanding , r=bsmedberg, sr=jst
""",
u"""
Create exceptions with the right parent. , r=jst sr=brendan
""",
u"""
Ensure that we have a valid scope chain at all times so C++ callers can create objects in the right scope. , r=brendan
""",
u"""
Avoid asserting for user-controlled thing (through __proto__ setting). , r+sr=jst
""",
u"""
to{Source,{,Locale}String} are not generic (387501, r=mrbkap).
""",
u"""
Backing out to fix red
""",
u"""
Make sure that we push a null JSContext on the current thread's XPConnect stack
""",
u"""
Attempt to fix leaks.
""",
u"""
Back out this change to hopefully fix the rest of the regressions test failures (from ).
""",
u"""
Associate XPCWrappedNativeScopes with XPCContexts, like the DOM does with windows and contexts, so that we can push a context that's allowed to actually call XPCWrappedJS functions. , r=jst sr=brendan
""",
u"""
Don't create exceptions using the global object as the parent, since that's bogus, use the scope chain instead. , r+sr=jst
""",
u"""
: objects and regexps are stored in separated tables in JSScript. r=brendan,mrbkap
""",
u"""
- Replace all instances of NS_STATIC_CAST and friends with C++ casts (and simultaneously bitrot nearly every patch in existence).  r=bsmedberg on the script that did this.  Tune in next time for Macro Wars: Episode II: Attack on the LL_* Macros.
""",
u"""
: now DUMP_SCOPE_STATS includes js_scope_stats into the log. r=brendan
""",
u"""
Fix bogus trace names.  b=387223  r=brendan
""",
u"""
Allow chrome files to touch implicit XPCNativeWrappers. , r+sr=jst
""",
u"""
Fixing . Implement weak references for JavaScript. Patch by Alex Fritze <alex@croczilla.com>. r+sr=shaver@mozilla.org
""",
u"""
Fix degenerate unsigned (enum) comparisons (357016, r=igor).
""",
u"""
: changing this back to (void *) for now to fix burning tree
""",
u"""
: fixing brendan's nit from comment 23
""",
u"""
: spidermonkey should be buildable by a C++ compiler, patch by
""",
u"""
Ensure that accesses to implicit XPCNativeWrappers are actually legal. , r+sr=jst
""",
u"""
Ensure that accesses to implicit XPCNativeWrappers are actually legal. , r+sr=jst
""",
u"""
Put comment in the right place.  b=180380
""",
u"""
Backing out these changes to fix tinderbox orange.
""",
u"""
Ensure that accesses to implicit XPCNativeWrappers are actually legal. , r+sr=jst
""",
u"""
Fix redundant statement and out-of-date comment.
""",
u"""
: for-in loop now always closes iterator objects. r=brendan
""",
u"""
[@ jsdASObserver::Observe] You can't dereference a NULL nsCOMPtr with operator->()
""",
u"""
. nsXPCComponents object and its wrapper leaked at shutdown. Patch by David Baron, David Bradley, and Robert Sayre. r=jst/bzbarsky, sr=dbaron
""",
u"""
Suspect all native wrappers during cycle collection (last part, rest already done by Graydon).  b=368869  r=graydon  sr=jst
""",
u"""
Make wrapped native debug dump log the native that is wrapped.  b=385549  r+sr=jst
""",
u"""
Fixing . Use the inner object when looking up methods and adding event listeners. r=mrbkap@mozilla.org, sr=brendan@mozilla.org
""",
u"""
Skip initial holes when computing the start value of reduce(Right). , r=brendan
""",
u"""
Re-land fix for cloned function object prototyping (300079, r=igor/mrbkap).
""",
u"""
, support optional args in idl, try again with fix for crash calling toString, r+sr=shaver
""",
u"""
, back out due to test content/base/test/test_bug352728.html failing
""",
u"""
, support optional arguments in idl, r+sr=shaver
""",
u"""
Back out again.
""",
u"""
Actually populate the string cache so we don't leak all deflated strings. , r=brendan
""",
u"""
, suspect all native wrappers for cycle collection.  Relanding.  Patch by graydon@mozilla.com.  r=brendan, sr=jst
""",
u"""
Remove useless variable. , patch from Gabriel Sjoberg <gabrielsjoberg@gmail.com>, r=mrbkap
""",
u"""
. Tweak XPCOMUtils. Patch by Nickolay_Ponomarev <asqueella@gmail.com>. r=sayrer, sr=bsmedberg
""",
u"""
Implement a full nsIScriptSecurityManager in xpcshell. , r+sr=jst
""",
u"""
Use the latest version of JS, so the shell always has the newest features. , r=brendan
""",
u"""
back out patch for due to leak regressions, as the new textframe code needs to land
""",
u"""
Test a hypothesis about the shutdown leak that's biting 300079's patch (a=sayrer).
""",
u"""
JavaScript Tests - regression test for , by Brendan Eich
""",
u"""
Fix violation of function prototyping due to cloned function object implementation (300079, r=mrbkap; expecting r=igor after the fact, want to get this in for widespread testing tomorrow).
""",
u"""
. C.u.import doesn't prevent recursion in the presence of circular dependencies. r=brendan, sr=bsmedberg
""",
u"""
Return value for GetJSDValue ignored leading to death
""",
u"""
Function atom if non-null must be string-keyed (385134, r=mrbkap).
""",
u"""
Back out previous patch for (bustage, and tree is closed)
""",
u"""
Implement an nsIScriptSecurityManager for the xpcshell. , r+sr=jst
""",
u"""
Backing this patch out again to fix sessionstore. See and 385085
""",
u"""
Fix violation of function prototyping due to cloned function object implementation (300079, r=igor).
""",
u"""
: Various JS engine crashes/leaks in OOM conditions, r=brendan, patch by Gavin Reaney, gavin@picsel.com
""",
u"""
Clean up property attributes (384846, r=mrbkap).
""",
u"""
: leak in jsfile.c, patch by Robin Ehrlich, rehrlich@ubiqinc.com, r=mrbkap
""",
u"""
Protect js_GetStringBytes from callers that happen during the last GC. Patch from brendan, , r=daumling sr=shaver
""",
u"""
: add ARM pure endian double support to JS engine, r=crowder, patch by Gavin Reaney gavin@picsel.com
""",
u"""
:  quieting the assertions here for all but myself and mrbkap, r=mrbkap
""",
u"""
: Patch from Mike Moening to fix warning when compiling with VC. r=me
""",
u"""
JavaScript Tests - update test range to 48.5-51.5%, 
""",
u"""
Fixing . The new Components.utils.import code shouldn't spam the console. r=sayrer@gmail.com, sr=brendan@mozilla.com
""",
u"""
Backing out to see whether that fixes tinderbox orange.
""",
u"""
Fix violation of function prototyping due to cloned function object implementation (300079, r=igor).
""",
u"""
JavaScript Test - catch indirect eval exception on trunk, 
""",
u"""
JavaScript Test - catch indirect eval exception on trunk, 
""",
u"""
Remove __callee__ property of Call prototypes (384642, r=igor).
""",
u"""
Emit JSOP_GROUP when optimizing away delete (382981, r=mrbkap).
""",
u"""
Fix recent regression in CheckSideEffects for paren-expr case (384680, r=mrbkap).
""",
u"""
JavaScript Tests - move test to extensions subsuite
""",
u"""
JavaScript Test - add strict warning tests for eval rename
""",
u"""
Better entrainment avoidance for Call.arguments (383269, r=igor).
""",
u"""
Restrict who can claim to implement nsISecurityCheckedComponent. , r=jst sr=bzbarsky
""",
u"""
Use a better filename when eval is used across scopes. , r=brendan
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
merging from cvs-trunk-mirror
""",
u"""
JavaScript Tests - update test to ignore 1ms differences, 
""",
u"""
JavaScript Test - update test to reflect new uneval(undefined) on trunk, 
""",
u"""
: Patch from Mike Moening and me to implement per-context debug hooks. r=brendan
""",
u"""
Allow C.u.Sandbox to take a principal or an nsIScriptObjectPrincipal. , r+sr=jst
""",
u"""
JavaScript Test - regression test for , by Brendan Eich
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by shutdown
""",
u"""
JavaScript Test - regression tests for , by Brendan Eich, Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by timeless
""",
u"""
Amazingly, backing out 368869 again.
""",
u"""
: removal of the previous commit.
""",
u"""
: Patch from Mike Moening to implement per-context debug hooks. r=me,brendan
""",
u"""
, suspect all native wrappers for cycle collection. Nth attempt, slightly safer.r=brendan, sr=jst
""",
u"""
Avoid entraining arguments in a Call prototype (383269, r=igor).
""",
u"""
: refactoring boxing of primitive values, r=brendan
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - fix scope on map call, 
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for 
""",
u"""
JavaScript Test - regression test for , by Laszlo Janszky, Brendan Eich
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
Make Object.prototype.toSource deal with even more __proto__ hacking. , r=crowder
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
: Using (void 0) instead of "undefined" in toSource and uneval(), r=mrbkap
""",
u"""
: escape tabs on platforms with unusual isprint() routines, r=mrbkap
""",
u"""
Fix CheckSideEffects over-aggressiveness (383674, r=mrbkap).
""",
u"""
: Fixing ALE macros to quell GCC strict-aliasing warnings. r=brendan
""",
u"""
Typo fixes
""",
u"""
Change the URI argument to Components.utils.import to be a resource: URI.  Bug380970, patch by Alex Vincent <ajvincent@gmail.com>, r=sayrer, sr=bsmedberg
""",
u"""
Backing out patch in , again. Still randomly crashing (as in ).
""",
u"""
: make JS1.8 the default for <xul:script>, and add a JSVERSION_LATEST #define to simplify future changes, patch by Nickolay Ponomarev <asqueella@gmail.com>, r+sr=brendan
""",
u"""
- Components.utils.import reports NS_ERROR_FAILURE when the file not existsswitch to NS_ERROR_FILE_NOT_FOUND and update testsr=sayrer, sr=brendan
""",
u"""
- "Assertion failure: kid2->parent == xml || !kid2->parent" with E4X after appendChild; avoid incorrectly reparenting XML by deeply copying instead of mutating.  r=mrbkap
""",
u"""
Fix syntax error.
""",
u"""
: 260 GC roots remain after destroying JSRuntime (not the complete fix, I think), r=brendan
""",
u"""
Bug #368869, suspect all native wrappers as cycle roots (yet again, after Igor's change to js gc).r=brendan, sr=jst
""",
u"""
Remove vestigial initialization
""",
u"""
Be less strict about how you can call eval. In particular, allow callers to call it through other names, as long as the this object is a global object. , r=brendan
""",
u"""
: incorrect uneval trying to output a getter function that is a sharp definition, r=igor
""",
u"""
Fix : Add new reportMatch function in shell.jsr=bclary@bclary.com
""",
u"""
- Correct backwards assertion check in XPCNativeScriptableInfo.  Patch by Manish Singh <manish@flock.com>, r=dbaron, sr=shaver
""",
u"""
Fix JOF_TMPSLOT accounting (383255, r=igor).
""",
u"""
: using code spec flag to declare extra slot used for post ++/--. r=brndan
""",
u"""
Fix overflow potential. , r=crowder rs=brendan
""",
u"""
Remove indirect eval. , r=brendan
""",
u"""
Handle error returns from ftell. , r=brendan
""",
u"""
Backing out to fix orange
""",
u"""
Fixing bustage, 
""",
u"""
Create XPCNativeWrapper function wrappers with the right parent. , r=bzbarsky sr=brendan
""",
u"""
Remove indirect eval. , r=brendan
""",
u"""
Whitespace police
""",
u"""
: new opcode flag top declare an extra temporary slot used by interpreter. r=brendan
""",
u"""
Fix fun_resolve to avoid resolving hidden properties (locals/params; 382532, r=mrbkap).
""",
u"""
: perlconnect removal continues, r=mrbkap, patch by Patrick Welche <pw-fb@newn.cam.ac.uk>
""",
u"""
Move skip lists to the testsrc directory.
""",
u"""
Add skips for tests causing OutOfMemoryErrors.
""",
u"""
Fix for ("(function(){}).apply.ee = <foo/>;" causes shutdown crash [@ nsXPConnect::Unlink] during nsCycleCollector::CollectWhite). r/sr=jst.
""",
u"""
: replacing JS_AddRoot calls via doubly-linked lists. r=jst sr=brendan
""",
u"""
: consistent termination of inline functions. r=brendan
""",
u"""
backing out checkin on closed tree
""",
u"""
: more perlconnect removal goodness
""",
u"""
JavaScript Test - fix broken test, 
""",
u"""
JavaScript Test - update test for 
""",
u"""
JavaScript Test - change eval tests to work around anonfunfix, 
""",
u"""
JavaScript Test - change native function to decodeURI since print is not native in the browser version
""",
u"""
JavaScript Tests - fix test to match new decompilation and to add missing brace in expected decompilation, 
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
Possible crashes/leaks in regexp handling in OOM conditionspatch by gavin@picsel.com r=crowder
""",
u"""
Fix let-induced anti-bracing logic to cope with group assignment expression statements (356247, r=mrbkap).
""",
u"""
Skip js1_5/Regress/regress-330352.js
""",
u"""
: object uneval gets confused by special "getter functions", r=mrbkap
""",
u"""
JavaScript Test - update expected value for decompilation, 
""",
u"""
JavaScript Test - move test to decompilation subsuite, 
""",
u"""
Use the prefix feature to avoid enumerating all skipped tests.
""",
u"""
After the recent move to consolidate shell.js code, this test broke due todifferent epsilon values used in different shell.js scripts. So this changejust makes the test values match exactly.
""",
u"""
JavaScript Test - update sudoku demo test
""",
u"""
- script tag should support version 1.8, r=jonas,sr=brendan
""",
u"""
Clean up skip list for recent test changes.
""",
u"""
: proper cleanup after generator.close(). r=brendan
""",
u"""
Updated to track revised ES4-based grammar plus paren minimization changes to the decompiler (381113).
""",
u"""
Implement ES4/JS2 expression closures (381113, r=mrbkap).
""",
u"""
Add a space here for consistency. , r=brendan
""",
u"""
JavaScript tests - fix incorrect TestCase signature, remove tests from slow-n.tests
""",
u"""
Fix delete parser to fold constants in its operand to discern genexp error case (382355, r=mrbkap).
""",
u"""
Recent code checkin regressed testcase from 356085
""",
u"""
Fix warning from last checkin (r=igor).
""",
u"""
JavaScript Test - update to remove new syntax errors, 
""",
u"""
JavaScript Test - tweak decompilation result, 
""",
u"""
JavaScript Test - remove Object.prototype.__iterator__ after test, 
""",
u"""
Add skips for new tests and for older tests now failing, likely due todifferent shell.js functions.
""",
u"""
: chomp closing ')' in obj_toSource more correctly, r=mrbkap
""",
u"""
JavaScript Test - regression test for , change test to -n negative format
""",
u"""
: make xpctools profiler work, and make it record time spend in the function itself. r=shaver
""",
u"""
JavaScript Test - regression test for , update to perform test in proper scope
""",
u"""
JavaScript Test - add js1.8 version option to browser-based test menu, no bug, not part of the build
""",
u"""
JavaScript Test - regression test for , by Robert Sayre; add version(180) foo
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , fix file name
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman, Brendan Eich
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Biju
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by James Ross
""",
u"""
JavaScript Tests - standardize test reporting for shell and browser, 
""",
u"""
Crash @ XPCWrappedNative::CallMethod passing null to out A*String parameters r+sr=jst
""",
u"""
: patch from Gavin Reaney to improve memeory allocation for the sprint stack. r=myself
""",
u"""
Fix for (Switch nsXPConnect::Traverse to use tracing). r=jst/igor, sr=dbaron.
""",
u"""
Fix for (Make cycle collector work with refcounted non-XPCOM objects). r=dbaron, sr=sicking.
""",
u"""
: SETSP is removed
""",
u"""
: static assert that does not depend on __LINE__
""",
u"""
Back this out for now to sort out what happens when we're called from C++, not from Javascript.
""",
u"""
Use the currently executing function as the nominal parent for our function so that we pull the correct prototype for our function. , r+sr=jst
""",
u"""
: Compilation error with HAS_XDR_FREEZE_THAW and old Script object, r=mrbkap
""",
u"""
: Compilation error with HAS_SCRIPT_OBJECT, r=mrbkap
""",
u"""
: "Assertion failure: (c2 <= cs->length) && (c1 <= c2)" with /[\Wb-G]/, patch by mrbkap, r=crowder
""",
u"""
Fix JOF_XMLNAME, etc., interrogation to mask the mode bits and compare (381504, r=mrbkap).
""",
u"""
More generator expression decompilation love (381372, r=mrbkap).
""",
u"""
- improve Components.utils.import-related commentsr=sayrer
""",
u"""
Mark the overwritten scope property in the space between where we remove it and re-add it in its changed form. , r=igor
""",
u"""
Protect the number from GC, even if it was originally a number. , r=crowder
""",
u"""
: StackGrowthDirection is not reliable with Sun Studio 11, patch by Ginn Chen <ginn.chen@sun.com>, r=brendan
""",
u"""
: Crash [@ js_IsIdentifier] decompiling float setter, r=mrbkap
""",
u"""
Count both the getter and setter for a given property. , r=crowder
""",
u"""
Handle Function.prototype.toString not returning what we expect it to return (a function expression). , r=crowder
""",
u"""
. Tweak generateFactory to call new, and add unit tests for module loading. Patch by Alex Vincent <ajvincent@gmail.com>. r=sayrer, sr=bsmedberg
""",
u"""
JavaScript Tests - factor common code into top level shell.js|browser.js, , r=igor, sr=brendan
""",
u"""
If the scanner returned TOK_ERROR, it already reported an error. , r=brendan
""",
u"""
Correctly parse regular expressions with the 'm' and 'y' flags. , r=brendan
""",
u"""
: fixing off-by-one caused by patch from , r=mrbkap
""",
u"""
: better obj_toSource for native functions and a few other cases, r=mrbkap
""",
u"""
Restrict for([k,v] in o) special case to JS1.7 (366941, r=mrbkap).
""",
u"""
Support generator expressions for JS1.8 (380237, r=mrbkap).
""",
u"""
Fix getter/setter decompilation to depend on generating op, not prefix string (381101, r=mrbkap).
""",
u"""
Skip over exception cookies, since we require JSOP_POP to pop them. , r=brendan
""",
u"""
Updated skip list.
""",
u"""
: AllocSlot now insists on the new slot being already set to void. r=brendan
""",
u"""
: fixing the disassembler, r=brendan
""",
u"""
: JS_GetGCMarkingTracer is removed. r=brendan
""",
u"""
JS code-sharing module system. Patch by Alex Fritze <alex@croczilla.com> and Robert Sayre <sayrer@gmail.com>. r=shaver/brendan, sr=brendan
""",
u"""
: make tooMuchGC dynamic (runtime gczeal option), r=brendan
""",
u"""
: sharp variables should deserialize using old getter/setter syntax.
""",
u"""
: keywords are no special with get/set getters. r=brendan
""",
u"""
: All XPC GC tracing now happens in the runtime trace callback.
""",
u"""
JavaScript Tests - add automation helper scripts, no bug, not part of the build
""",
u"""
JavaScript Test - regression test for , revert Object.prototype to prevent side effects
""",
u"""
JavaScript Tests - remove extraneous debugger statement, no bug, not part of the build
""",
u"""
: fixing regression from . r=brendan
""",
u"""
Fiddle cosmetics.
""",
u"""
: Crash decompiling float setter, r=brendan, r=igor
""",
u"""
: Using tracing instead of explicit root management. r=alfred.peng sr=brendan
""",
u"""
woops, backing out due to closed tree
""",
u"""
: Crash decompiling float setter, r=brendan, r=igor
""",
u"""
Fixes left in wake of JSOP_POPN (379925, r=igor).
""",
u"""
JavaScript Test - update test to match 1.8.1 and later serialization, 
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression tests for , by Jesse Ruderman
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
Stop overloading JSOP_SETSP for both exception handling and group assignment bulk popping (375695, r=igor).
""",
u"""
JavaScript Test - test automation, add js1_8, no bug, not part of the build
""",
u"""
JavaScript Tests - disable window.onerror handler to prevent false failure, 
""",
u"""
JavaScript Test - remove non-standard use of unescape, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - segregate non-standard tests, add tests lists for extensions and gc test, 
""",
u"""
JavaScript Tests - move decompilation tests to decompilation subsuites, 
""",
u"""
JavaScript Tests - setup js1_6 decompilation sub suite, 
""",
u"""
: js_CodeSpec.name/token are moved to separated arrays to shrink the code. r=brendan
""",
u"""
Unhide a crucial pop from the decompiler (379860, r=igor).
""",
u"""
: branch callback is accessed via cx->branchCallback for smaller code. r=brendan
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by moz_bu_r_a4
""",
u"""
JavaScript Test - regression test for , by moz_bu_r_a4
""",
u"""
JavaScript Test - regression test for , by moz_bu_r_a4
""",
u"""
JavaScript Test - regression test for , by shutdown
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by shutdown
""",
u"""
JavaScript Tests - regression tests for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by shutdown
""",
u"""
JavaScript Tests - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , update decompilation changes.
""",
u"""
JavaScript Tests - update change in decompilation due to fix, 
""",
u"""
Fix blunder in reworking of how SpiderMonkey detects a label statement (reported by Steve Yegge).
""",
u"""
Back out patch for , yet again. Seems to cause some obscure crashesin nightlies.
""",
u"""
JavaScript Test - regression test for , by George Kangas
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Tests - do not use anonymous functions in statement contexts, 
""",
u"""
When pushing on top of a JSContext on the XPConnect JSContext stack, save offthe JSStackFrame chain on that JSContext.  When popping, restore the stackframe chain.  , r=jst, sr=brendan
""",
u"""
JavaScript Tests - replace JavaScriptOptions, 
""",
u"""
Fix some assertions to avoid re-evaluating macro args; tweak comments.
""",
u"""
: tracing API now let the tracer to know about the GC lock count.
""",
u"""
Fix for (Only create one XPCCallContext per cycle collection). r=jst, sr=brendan.
""",
u"""
Bug #368869, suspect all native wrappers as cycle roots (again).r=brendan, sr=jst
""",
u"""
Balance the stack for destructuring catch heads (379483, r=igor).
""",
u"""
Bug  377751: Switching JSClass.mark in XPConnect to the tracing semantics. r=jst, sr=brendan
""",
u"""
fixing a compiler warning introduced by patch in , r=brendan
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Tandetnik, Martin Honnen
""",
u"""
JavaScript Tests - regression test for , by Igor Bukanov
""",
u"""
JavaScript Tests - add js1_8 suite for features not shipping on the 1.8.1 branch, no bug, not part of the build
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
Followup fix to dumb bug in last checkin (379442, r=me).
""",
u"""
Skip #n= at front of initialiser on right of destructuring assignment forms (368224, r=igor).
""",
u"""
Fix model stack management for catch guards in the decompiler; eliminate related SRC_HIDDEN abusage (375794, r=igor).
""",
u"""
: removal of the commit.
""",
u"""
: More build fixes.
""",
u"""
: Fixing windows compilation problem.
""",
u"""
: JSClass instances in xpconnect use the tracing API. r=brendan, sr=jst
""",
u"""
: incorrect decompilation for ({this setter: function () {} }) and others, r=igor, r=brendan
""",
u"""
: assertion on bogus character ranges in regexps, r=mrbkap
""",
u"""
Part of (Switch cycle collector to more efficient hashtables - only keep hashtable around while collecting). r=graydon, sr=dbaron.
""",
u"""
: New API to register application-specific GC roots. r=brendan
""",
u"""
JavaScript Tests - add missing mode lines, no bug, not part of the build
""",
u"""
JavaScript Tests - update automation scripts, no bug, not part of the build
""",
u"""
JavaScript Tests - update slow-n.tests, remove e4x/Regress/regress-350531.js, add js1_5/GC/regress-319980-01.js, js1_5/GC/regress-338653.js, no bug, not part of the build
""",
u"""
JavaScript Tests - clean up dummy shell.js, not bug, not part of the build
""",
u"""
JavaScript Test - add missing end test prolog for asynchronous test, 
""",
u"""
: Simplifing JS_DimpHeap while fixing BeOS build problems. r=brendan
""",
u"""
JavaScript Test - regression test for , only test for crash
""",
u"""
- \d pattern matches characters other than the decimal digits 0-9.  r=mrbkap
""",
u"""
: DEBUG build of xpc now dumps JS heap on shutdown to a file defined by XPC_SHUTDOWN_HEAP_DUMP environment variable. r=brendan sr=jst
""",
u"""
Allow getting the lineNumber of XPConnect expceptions.  , r=sicking,sr=jst.  r=mrbkap, sr=jst for the test.
""",
u"""
JavaScript Tests - update Daylight Savings Time, other Date related tests, 
""",
u"""
: js_PutEscapedStringImpl can now cope with in JSString. r=brendan
""",
u"""
: Information about JS_DumpDebug to replace GC_MARK_DEBUG info.
""",
u"""
Fix test not to depend on AWT, which caused headless exceptions running withouta X terminal.
""",
u"""
Skip performance test.
""",
u"""
Fix for (Improve cycle collection QI performance). r/sr=sicking.
""",
u"""
: Replacing GC_MARK_DEBUG by DumpHeap. r=brendan
""",
u"""
: proper checks for null and jsval type when tracing, r=brendan
""",
u"""
] GC: separating traversal and markingAdding help() for dumpHeap [fixing crash on solaris x86]r=igor
""",
u"""
Followup fixes to making cycle collector use more efficient hashtables:  shrink size of table and fix warnings on 64-bit machines.  b=377606  sr=peterv  r=graydon
""",
u"""
- Building with gcc 4.3 and -pendatic fails due to extra semicolons, patch by Art Haas <ahaas@airmail.net>, rs=me
""",
u"""
Fix for (Make cycle-collection debugging features optional at compile time). r=graydon, sr=jst.
""",
u"""
: fixing frprintf args in DumpHeap
""",
u"""
Fix for (Switch cycle collector to more efficient hashtables). Patch by graydon, r=peterv, sr=dbaron.
""",
u"""
Fixing a trivial warning in an assertion, r=crowder
""",
u"""
One more fix for . Make sure to find the right this object when calling functions through a wrapper. r+sr=brendan@mozilla.org
""",
u"""
Updated skip list for Rhino. Still needs more work categorizing failures.
""",
u"""
Tests in this directory oddly depend on a 3-argument TestCase constructor,rather than the conventional 4-argument constructor, so many tests wereincorrectly failing. Changed to a 3-argument constructor.
""",
u"""
: fixing compilation warning about return JS_FALSE in a function returning JSXML*. r=brendan
""",
u"""
Fix for (freeze/pause after clicking on a link). Patch by sspitzer, r/sr=peterv.
""",
u"""
: patch from Martijn Wargers <martijn.martijn@gmail.com> to fix JS_TraceChildren declarataion. r=myself
""",
u"""
: fixing JS_CLASS_TRACE macro and misspellings. r=brendan
""",
u"""
Fixing misspelling in comments.
""",
u"""
Add an assertion. , r=brendan
""",
u"""
JavaScript Test - add -Q command line option to jsDriver.pl to disable interrupt signal handler, , r=mrbkap
""",
u"""
JavaScript Test - regression test for , by Michael Lipp, David P. Caldwell
""",
u"""
JavaScript Tests - move tests 5,6 from 373082 to 376773
""",
u"""
: API to trace GC things graph without running the GC. r=brendan
""",
u"""
JavaScript Tests - reduce test output not related to success/failure, 
""",
u"""
JavaScript Tests - do not perform comparisons for skipped test, 
""",
u"""
: another regexp that makes JS allocate > 1GB and hand, r=mrbkap
""",
u"""
: incorrect decompilation for object literal with named getter function; property and function names are mashed together, r=brendan
""",
u"""
Add an API to set aside and restore cx->fp. , r=brendan
""",
u"""
Protect against someone calling XPCSafeJSObjectWrapper.prototype(). , r+sr=brendan
""",
u"""
: hiding code to set arena names behind JS_ARENAMETER. r=brendan
""",
u"""
JavaScript Test - regression test for , by Brendan Eich
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
: fixing bad English in comments for xml_lookupProperty.
""",
u"""
Add -o <option> to shell; add JSOPTION_ANONFUNFIX and test it for ECMA conformance (376052, r=igor).
""",
u"""
JavaScript Test - regression test for , update to check for new exception
""",
u"""
: Fixing compilation problems with JS_C_STRINGS_ARE_UTF8 defined.
""",
u"""
, Incorrect decompilation for "new (eval())".  r=brendan.
""",
u"""
Fix decompilation of for(a[b,c] in d) and the like (355786, r=mrbkap).
""",
u"""
Fix special case of new (f()()) and the like (352013 part deux, r=mrbkap).
""",
u"""
: simpler noSuchMethod implementation, r=brendan.
""",
u"""
Allow case yield: in JS1.7 (352441, r=mrbkap).
""",
u"""
JavaScript Test - regression test for , by HE Shi-Jun
""",
u"""
JavaScript Test - update regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Nanto Vi (TOYAMA Nao)
""",
u"""
JavaScript Test -regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for 
""",
u"""
- Update JS_GetImplementationVersion() for JS1.7rc, r=brendan
""",
u"""
Fix parser to allow eval(i)++ to compile (352453, r=mrbkap).
""",
u"""
Fix js_LineNumberToPC based on MikeM@RetekSolutions.com's input (313922, r=mrbkap).
""",
u"""
Unify double sprinting to handle non-finite and negative zero cases (375882, r=mrbkap).
""",
u"""
Taking out the patches for and until the reason for ref counting leak would be clear.
""",
u"""
: fixing regression from . r=brendan
""",
u"""
JavaScript Test - regression test for , by Biju
""",
u"""
Revert patch from because it broke Gmail ()
""",
u"""
JavaScript Test - add testcases from , by Jesse Ruderman
""",
u"""
- GCX_PRIVATE is replaced by GCX_FUNCTION. r=brendan
""",
u"""
Removal of broken patch for 
""",
u"""
- GCX_PRIVATE is replaced by GCX_FUNCTION. r=brendan
""",
u"""
: Uniform applications of GetXMLObject. r=brendan
""",
u"""
Ignore let declarations when process variable declarations to ensure proper hoisting behavior. , r=brendan
""",
u"""
Deal with the /i option before calculating the start (and localMax) for ranges. , r=crowder
""",
u"""
Continue processing the character set even though we found our max. , r=crowder
""",
u"""
, more compiler warnings fixage, r=igor@mir2.org
""",
u"""
- Constant folder treats NaN coerced to boolean as true.  r=mrbkap
""",
u"""
Fix and related (r=mrbkap).
""",
u"""
Fix JS strict warning in the wrapper code.  , r+sr=brendan
""",
u"""
: fixing generator/decompiler after . r=brendan
""",
u"""
: Fixing warnings and one build error from jsregexp "debugger" patch, r=mrbkap
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by antonlv, Andreas
""",
u"""
JavaScript Test - regression test for 
""",
u"""
JavaScript Test - Regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Igor Bukanov
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman
""",
u"""
JavaScript Test - regression test for , by Jesse Ruderman, Igor Bukanov
""",
u"""
Remove GetKeyPointer method from nsTHashtable key types.  b=374906  r=bsmedberg
""",
u"""
Remove unused getKey callback from PLDHashTableOps/JSDHashTableOps.  b=374906  r=bsmedberg
""",
u"""
Consolidate duplicated code into the beginning of the double-hashing loop.  b=374906  r=brendan
""",
u"""
- Build SpiderMonkey with JS_C_STRINGS_ARE_UTF8, not part of the build, patch by Tom Insam, r=brendan
""",
u"""
: Changine XML method lookup to never alter "this". r=brendan,jwalden
""",
u"""
: no quotas arround name matching keywords in keywordless context. r=brendan,mrbkap
""",
u"""
Avoid the need for a getKey callback in jsdhash/pldhash.  b=374906  r=brendan
""",
u"""
: Maximum recursion value is too low, r=brendan
""",
u"""
: very non-greedy regexp causes crash in jsregexp.c, r=mrbkap
""",
u"""
Relanding part of the fix for (Make XPConnect traverse more JS edges). r=brendan, sr=jst.
""",
u"""
: jsregexp preprocessor-enabled "debugging" mode
""",
u"""
Free the (distributed) Lizard! Automatic merge from CVS: Module mozilla: tag HG_REPO_INITIAL_IMPORT at 22 Mar 2007 10:30 PDT,
""",
]

