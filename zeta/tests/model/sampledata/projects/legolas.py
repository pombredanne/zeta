legolas_description = \
u"""
The __GNU Compiler Collection__ (usually shortened to GCC) is a compiler system
supporting various programming languages produced by the GNU Project. GCC is a
key component of the GNU toolchain. As well as being the official compiler of
the GNU system, GCC has been adopted as the standard compiler by most other
modern Unix-like computer operating systems, including //GNU/Linux//, the //BSD
family// and //Mac OS X//. GCC has been ported to a wide variety of computer
architectures, and is widely deployed as a tool in commercial, proprietary and
closed source software development environments. GCC is also available for
most embedded platforms, for example //Symbian//, //AMCC// and //Freescale Power
Architecture//-based chips. The compiler can target a wide variety of
platforms, such as the
[[ http://en.wikipedia.org/wiki/Sony_Computer_Entertainment | Playstation ]] 
and [[ http://www.sega.co.jp | Sega Dreamcast ]]. Several companies make a
business out of supplying and supporting gcc ports to various platforms, and
chip manufacturers today consider a gcc port almost essential to the success
of an architecture.

Originally named the GNU C Compiler, because it only handled the C programming
language, GCC 1.0 was released in 1987, and the compiler was extended to
compile C++ in December of that year. Front ends were later developed for
Fortran, Pascal, Objective C, Java, and Ada, among others.

>The Free Software Foundation (FSF) distributes GCC under the GNU General
>Public License (GNU GPL) and the GNU Lesser General Public License (GNU LGPL).
>GCC is free software.
"""

legolas_compdesc    = \
[
u"""
GCC's external interface is generally standard for a UNIX compiler. Users
invoke a driver program named gcc, which interprets command arguments, decides
which language compilers to use for each input file, runs the assembler on
their output, and then possibly runs the linker to produce a complete
executable binary.

Each of the language compilers is a separate program that inputs source code
and outputs assembly code. All have a common internal structure. A
per-language front end parses the source code in that language and produces an
abstract syntax tree ("tree" for short).
""",
u"""
Frontends vary internally, having to produce trees that can be handled by the
backend. Currently, the parsers are all hand-coded recursive descent parsers,
though there is no reason why a parser generator could not be used for new
front-ends in the future.
""",
u"""
Optimization on trees does not generally fit into what most compiler
developers would consider a front end task, as it is not language dependent
and does not involve parsing. A common, even though somewhat contradictory,
name for this part of the compiler is "middle end."

The exact set of GCC optimizations varies from release to release as it
develops, but includes the standard algorithms, such as loop optimization,
jump threading, common subexpression elimination, instruction scheduling, and
so forth. The RTL optimizations are of less importance with the addition of
global SSA-based optimizations on GIMPLE trees,[19] as RTL optimizations have
a much more limited scope, and have less high-level information.
""",
u"""
The behavior of GCC's back end is partly specified by preprocessor macros and
functions specific to a target architecture, for instance to define the
endianness, word size, and calling conventions. The front part of the back end
uses these to help decide RTL generation, so although GCC's RTL is nominally
processor-independent, the initial sequence of abstract instructions is
already adapted to the target. At any moment, the actual RTL instructions
forming the program representation have to comply with the machine description
of the target architecture.
""",
u"""
GCC is not only a native compiler--it can also cross-compile any program,
producing executable files for a different system from the one used by GCC
itself. This allows software to be compiled for embedded systems which are not
capable of running a compiler. GCC is written in C with a strong focus on
portability, and can compile itself, so it can be adapted to new systems
easily.

GCC has multiple language frontends, for parsing different languages. Programs
in each language can be compiled, or cross-compiled, for any architecture. For
example, an ADA program can be compiled for a microcontroller, or a C program
for a supercomputer. 
"""
]

legolas_mstndesc    = \
[
u"""
* doc/passes.texi (Tree-SSA passes): Document SLP pass.
* tree-pass.h (pass_slp_vectorize): New pass.
* params.h (SLP_MAX_INSNS_IN_BB): Define.
* timevar.def (TV_TREE_SLP_VECTORIZATION): Define.
* tree-vectorizer.c (timevar.h): Include.
(user_vect_verbosity_level): Declare.
(vect_location): Fix comment.
(vect_set_verbosity_level): Update user_vect_verbosity_level
""",
u"""
* final.c (shorten_branches): Do not align labels for jump tables.
(final_scan_insn): Use JUMP_TABLE_DATA_P.
* config/i386/i386.md (AX_REG, BX_REG, CX_REG): New constants.
* config/i386/i386.c (ix86_function_arg_regno_p, function_arg_32,
function_value_32, function_value_64, function_value_ms_64,
setup_incoming_varargs_64, ix86_expand_prologue, ix86_expand_call,
legitimize_tls_address, x86_this_parameter, x86_output_mi_thunk):
Use new constants.
""",
u"""
(mark_all_vars_used_1): Pass data through to mark_all_vars_used.
When calling set_is_used on a VAR_DECL, if data is not NULL and
its DECL_UID is in the bitmap, call mark_all_vars_used on its
DECL_INITIAL after clearing the bit in bitmap.
(remove_unused_locals): Adjust mark_all_vars_used callers.
Instead of removing unused global vars from unexpanded_var_list
immediately record them in bitmap, call mark_all_vars_used on
all used global vars from unexpanded_var_list and only purge
global vars that weren't found used even during that step.
""",
u"""
* dse.c (find_shift_sequence): Reinstate "<= UNITS_PER_WORD" condition.
* var-tracking.c (micro_operation_def): Update comment on u.loc.
(mode_for_reg_attrs, var_lowpart): New functions.
(add_uses): Consider recording a lowpart of LOC for MO_USE.
(add_stores): Likewise MO_SET and MO_COPY.  If the source of a set
or copy is known, set LOC to the SET that performs the set, instead
of the destination.
(find_src_status, find_src_set_src): Remove LOC parameter.
Replace INSN with the source value.
(compute_bb_dataflow, emit_notes_in_bb): Check for a SET u.loc when
handling MO_SET and MO_COPY.  Update the calls to find_src_status
and find_src_set_src.
""",
u"""
PR libstdc++/33771
PR libstdc++/33773
* testsuite/21_strings/headers/cwchar/macros.cc: Guard test with
_GLIBCXX_HAVE_WCHAR_H.
* testsuite/21_strings/headers/cwctype/macros.cc: Likewise with
_GLIBCXX_HAVE_WCTYPE_H.
* testsuite/17_intro/headers/c++200x/all.cc: Guard inclusions
of <wchar.h> and <wctype.h>.
* testsuite/17_intro/headers/c++200x/all_multiple_inclusion.cc:
Likewise.
* testsuite/17_intro/headers/c++1998/all.cc: Likewise.
* testsuite/17_intro/headers/c++1998/all_multiple_inclusion.cc:
Likewise.
""",
]

legolas_verdesc     = \
[
u"""
The GNU project and the GCC developers are pleased to announce the release of
GCC 3.2.3.

The purpose of the GCC 3.2 release series is to provide a stable platform for
OS distributors to use building their next releases. A primary objective was
to stabilize the C++ ABI; we believe that the interface to the compiler and
the C++ standard library are now relatively stable.

Be aware that C++ code compiled by GCC 3.2.x will (in general) not
interoperate with code compiled by GCC 3.1.1 or earlier.

Please refer to our detailed list of news, caveats, and bug-fixes for further
information.
""",
u"""
The GNU project and the GCC developers are pleased to announce the release of
GCC 3.0.4, which is a bug-fix release for the GCC 3.0 series.

GCC used to stand for the GNU C Compiler, but since the compiler supports
several other languages aside from C, it now stands for the GNU Compiler
Collection.

GCC 3.0.x has several new optimizations, new targets, new languages and many
other new features, relative to GCC 2.95.x. See the new features page for a
more complete list.

A list of successful builds is updated as new information becomes available.

The GCC developers would like to thank the numerous people that have
contributed new features, test results, bug fixes, etc to GCC. This amazing
group of volunteers is what makes GCC successful.

And finally, we can't in good conscience fail to mention some caveats to using
GCC 3.0.x.

For additional information about GCC please refer to the GCC project web site
or contact the GCC development mailing list.

To obtain GCC please use our mirror sites, or our CVS server.
""",
u"""
uly 27, 2002

The GNU project and the GCC developers are pleased to announce the release of
GCC 3.1.1.

The links below still apply to GCC 3.1.1.

May 15, 2002

The GNU project and the GCC developers are pleased to announce the release of
GCC 3.1.

GCC used to stand for the GNU C Compiler, but since the compiler supports
several other languages aside from C, it now stands for the GNU Compiler
Collection.

A list of successful builds is updated as new information becomes available.

The GCC developers would like to thank the numerous people that have
contributed new features, improvements, bug fixes, and other changes as well
as test results to GCC. This amazing group of volunteers is what makes GCC
successful.

For additional information about GCC please refer to the GCC project web site
or contact the GCC development mailing list.

To obtain GCC please use our mirror sites, or our CVS server.
""",
u"""
January 31, 2007

The GNU project and the GCC developers are pleased to announce the release of
GCC 4.0.4.

This release is a bug-fix release, containing fixes for regressions in GCC
4.0.3 relative to previous releases of GCC.
""",
u"""
GCC used to stand for the GNU C Compiler, but since the compiler supports
several other languages aside from C, it now stands for the GNU Compiler
Collection.

A list of successful builds is updated as new information becomes available.

The GCC developers would like to thank the numerous people that have
contributed new features, improvements, bug fixes, and other changes as well
as test results to GCC. This amazing group of volunteers is what makes GCC
successful.

For additional information about GCC please refer to the GCC project web site
or contact the GCC development mailing list.

To obtain GCC please use our mirror sites or our SVN server.
""",
]

legolas_comments    = \
[
u"""
	* unwind-dw2.c (_Unwind_DebugHook): New function.
	(uw_install_context): Call _Unwind_DebugHook.
""",
u"""
	* call.c (implicit_conversion): Handle conversion from
	initializer-list to scalar.
	(convert_like_real): Likewise.  Avoid crashing on list
	initialization with bad conversions.
	(can_convert): Use LOOKUP_EXPLICIT.
	(can_convert_arg_bad): Add flags parm.
	* cp-tree.h: Adjust.
	* typeck.c (convert_for_assignment): Pass flags.
""",
u"""

	* libsupc++/initializer_list: Format.
	* testsuite/18_support/initializer_list/requirements/typedefs.cc: New.
	* testsuite/18_support/initializer_list/requirements/
	explicit_instantiation.cc: New.


""",
u"""

	PR libstdc++/40273
	* include/tr1_impl/functional: Add explicit cast.
	* testsuite/20_util/function/requirements/
	explicit_instantiation.cc: New.
	* testsuite/20_util/function/null_pointer_comparisons.cc: New.


""",
u"""
Don't link to or test existence of libgfortranbegin
""",
u"""
gcc/ChangeLog
	* system.h (CONST_CAST2): Use C++ const_cast when compiled as C++

""",
u"""
./:
	* Makefile.in (LINKER, LINKER_FLAGS): Define.
	(LINKER_FOR_BUILD, BUILD_LINKERFLAGS): Define.
	(ALL_LINKERFLAGS): Define.
	(xgcc$(exeext)): Change $(COMPILER) to $(LINKER).
	(cpp$(exeext), cc1-dummy$(exeext), cc1$(exeext)): Likewise.
	(collect2$(exeext), mips-tfile, mips-tdump): Likewise.
	(gcov$(exeext), gcov-dump$(exeext)): Likewise.
	(build/gen%$(build_exeext)): Change $(COMPILER_FOR_BUILD) to
	$(LINKER_FOR_BUILD).
	(build/gcov-iov$(build_exeext)): Likewise.
cp/:
	* Make-lang.in (g++$(exeext)): Change $(COMPILER) to $(LINKER).
	(cc1plus-dummy$(exeext), cc1plus$(exeext)): Likewise.
fortran/:
	* Make-lang.in (gfortran$(exeext)): Change $(COMPILER) to
	$(LINKER).
	(f951$(exeext)): Likewise.
java/:
	* Make-lang.in ($(XGCJ)$(exeext)): Change $(COMPILER) to
	$(LINKER).
	(jc1$(exeext), jcf-dump$(exeext), jvgenmain$(exeext)): Likewise.
objc/:
	* Make-lang.in (cc1obj-dummy$(exeext)): Change $(COMPILER) to
	$(LINKER).
	(cc1obj$(exeext)): Likewise.
objcp/:
	* Make-lang.in (cc1objplus-dummy$(exeext)): Change $(COMPILER) to
	$(LINKER).
	(cc1objplus$(exeext)): Likewise.

""",
u"""

        PR fortran/40270
        * trans-decl.c (create_main_function): Mark MAIN__ and
        argc/argv as TREE_USED and push/pop function_decl context
        if needed.


""",
u"""
	gcc/
	* gcse.c (target.h): Include.
	(can_assign_to_reg_without_clobbers_p): Check that the target allows
	copy of argument to a pseudo register.


""",
u"""

	* tree-ssa-live.c (dump_scope_block): Document arguments.
	(dump_scope_blocks): Document.
	(debug_scope_blocks): New.
	* tree-flow.h (debug_scope_blocks): Declare.



""",
u"""
     * doc/contrib.texi (Contributors): add myself to the list.

""",
u"""
Change scan-tree-dump-times patterns due to frontend changes
""",
u"""
(Synchronize with addition made to binutils sources):

        * plugins.m4: New.

""",
u"""
	* expr.c (target_align): New function.  Alignment the TARGET of an
	assignment may be assume to have.
	(highest_pow2_factor_for_target): Use it instead of relying on
	immediate tree attributes of TARGET, not necessarily honored when
	intermediate bitfields are involved.

	testsuite/
	* gcc.c-torture/execute/align-nest.c: New testcase.
	* gnat.dg/misaligned_nest.adb: New testcase.


""",
u"""
Revert part of r147883 that breaks ABI
""",
u"""

	PR target/40266
	* config/i386/driver-i386.c (host_detect_local_cpu): Support
	AVX, SSE4, AES, PCLMUL and POPCNT.

""",
u"""
Apply fixed version of previous delta.

""",
u"""

	* tree-pretty-print.c (dump_location): New.
	(dump_generic_node): Call it.
	Factor code to handle BLOCK nodes ...
	(dump_block_node): ... here.


""",
u"""

       * g++.dg/plugin/attribute_plugin.c: Include gcc-plugin.h first.
       * g++.dg/plugin/dumb_plugin.c: Include gcc-plugin.h first.
       * g++.dg/plugin/selfassign.c: Include gcc-plugin.h first.
       * gcc.dg/plugin/selfassign.c: Include gcc-plugin.h first.



	* Makefile.in (GCC_PLUGIN_H): New. Replace all uses of gcc-plugin.h with
	it.
	* doc/plugins.texi: Document that gcc-plugin.h must be the first to be
	included.
	* gcc-plugin.h: Include config.h and system.h.
	(IN_GCC): Define if not defined.


""",
u"""
	PR middle-end/40249
	* Makefile.in (CRTSTUFF_CFLAGS): Replace -fno-inline-functions
	with -fno-inline.

""",
u"""
* Makefile.tpl (all): Avoid harmless warning in make all when
gcc-bootstrap is enabled but stage_last does not exist.
* Makefile.in: Rebuilt.

""",
u"""
        * config/m32r/m32r.c: Use REG_P, MEM_P and CONST_INT_P where
        applicable.
        * config/m32r/m32r.h: Ditto.
        * config/m32r/m32r.md: Ditto.
        * config/m32r/predicates.md: Ditto.

""",
u"""

        * g++.old-deja/g++.brendan/array1.C (array): Use __SIZE_TYPE__
        cast instead of assuming 0ul.
        * g++.old-deja/g++.brendan/crash64.C (size_t): Define it via
        __SIZE_TYPE__.
        (_type_desc): Make first argument const.
        * g++.old-deja/g++.jason/new3.C (dg-options): Add -Wno-long-long.


""",
u"""

	PR libfortran/40187
	* intrinsics/iso_c_binding.c (c_f_pointer_u0):  Take care
	of stride in "shape" argument.


	PR libfortran/40187
	* gfortran.dg/c_f_pointer_shape_tests_4.f03:  New file.
	* gfortran.dg/c_f_pointer_shape_tests_4_driver.c:  New file.


""",
u"""
* cgraph.c (dump_cgraph_node): Honor -fdump-noaddr.

""",
u"""
Daily bump.
""",
u"""
fortran/

        PR fortran/39178
        * gfortranspec.c (lang_specific_driver): Stop linking
        libgfortranbegin.
        * trans-decl.c (gfc_build_builtin_function_decls): Stop
        making MAIN__ publicly visible.
        (gfc_build_builtin_function_decls): Add
        gfor_fndecl_set_args.
        (create_main_function) New function.
        (gfc_generate_function_code): Use it.

libgfortran/

        PR fortran/39178
        * runtime/main.c (store_exe_path): Make static
        and multiple-times callable.
        (set_args): Call store_exe_path.
        * libgfortran.h: Remove store_exe_path prototype.
        * fmain.c (main): Remove store_exe_path call.


""",
u"""

        PR fortran/40246
        * match.c (gfc_match_nullify): NULLify freed pointer.


        PR fortran/40246
        * gfortran.dg/nullify_4.f90: New test.


""",
u"""


	* gcc/doc/plugins.texi
	(Loading plugins): typo.
	(Plugin callbacks): Documented PLUGIN_INFO, PLUGIN_GGC_START,
	PLUGIN_GGC_MARKING, PLUGIN_GGC_END, PLUGIN_REGISTER_GGC_ROOTS.
	(Interacting with the GCC Garbage Collector): Added new section.
	(Giving information about a plugin): Added new section for
	PLUGIN_INFO.
	* gcc/testsuite/gcc.dg/plugin/plugin.exp: Added ggcplug.c test plugin
	with ggcplug-test-1.c for testing PLUGIN_GGC_MARKING etc...
	* gcc/testsuite/gcc.dg/plugin/ggcplug-test-1.c: Added new file.
	* gcc/testsuite/gcc.dg/plugin/ggcplug.c: Added new file.
	* gcc/ggc.h (ggc_register_root_tab): Added declaration.
	* gcc/gcc-plugin.h (PLUGIN_GGC_START, PLUGIN_GGC_MARKING)
	(PLUGIN_GGC_END, PLUGIN_REGISTER_GGC_ROOTS): Added new events.
	(register_callback): Improved comment in declaration.
	* gcc/ggc-common.c (const_ggc_root_tab_t) Added new typedef for
	vectors.
	(extra_root_vec) Added static variable for dynamic roots
	registration.
	(ggc_register_root_tab) Added new routine.
	(ggc_mark_roots) Added iteration inside extra_root_vec, and invoke
	PLUGIN_GGC_MARKING event.
	* gcc/ggc-zone.c: Include plugin.h.
	(ggc_collect): Invoke PLUGIN_GGC_START & PLUGIN_GGC_END events.
	* gcc/ggc-page.c: Include plugin.h.
	(ggc_collect): Invoke PLUGIN_GGC_START & PLUGIN_GGC_END events.
	* gcc/plugin.c (plugin_event_name): added names of PLUGIN_GGC_START,
	PLUGIN_GGC_MARKING, PLUGIN_GGC_END, PLUGIN_REGISTER_GGC_ROOTS
	(register_callback): check lack of callbacks for
	pseudo-events. Added handling of PLUGIN_REGISTER_GGC_ROOTS,
	PLUGIN_GGC_START, PLUGIN_GGC_MARKING, PLUGIN_GGC_END.
	(invoke_plugin_callbacks): Handle PLUGIN_GGC_START,
	PLUGIN_GGC_MARKING, PLUGIN_GGC_END, PLUGIN_REGISTER_GGC_ROOTS.
	* gcc/Makefile.in (ggc-common.o, ggc-zone.o, ggc-page.o): Added
	dependency on plugin.h.
	(plugin.o): Added dependency on ggc.h...


""",
u"""
revert
	* config/arm/neon-gen.ml: Include vxWorks.h rather than stdint.h
	for VxWorks kernels.
	* config/arm/arm_neon.h: Regenerate.

""",
u"""

	* gcc.dg/tree-ssa/inline-3.c: Remove dump file.

""",
u"""

	PR middle-end/40248
	Revert
	* expr.c (expand_expr_real_1): Avoid calling do_store_flag
	with mismatched comparison modes.

	* expr.c (expand_expr_real_1): Expand the operand of a
	VIEW_CONVERT_EXPR in its natural mode.

""",
u"""
./:
	* Makefile.in (COMPILER, COMPILER_FLAGS): Define.
	(COMPILER_FOR_BUILD, BUILD_COMPILERFLAGS): Define.
	(ALL_COMPILERFLAGS): Define.
	(.c.o, xgcc$(exeext), cpp$(exeext)): Use $(COMPILER).
	(cc1-dummy$(exeext), cc1$(exeext)): Likewise.
	(collect2$(exeext), collect2.o): Likewise.
	(c-opts.o, c-cppbuiltin.o, c-pch.o, gcc.o, gccspec.o): Likewise.
	(gcc-options.o, version.o, prefix.o, toplev.o): Likewise.
	($(out_object_file), mips-tfile, mips-tdump): Likewise.
	(libbackend.o, intl.o, cppdefault.o): Likewise.
	(gcov$(exeext), gcov-dump$(exeext)): Likewise.
	(build/%.o): Use $(COMPILER_FOR_BUILD).
	(build/gen%$(build_exeext)): Likewise.
	(build/gcov-iov$(build_exeext)): LIkewise.
	* config/t-darwin (darwin.o): Use $(COMPILER).
	(darwin-c.o, darwin-f.o, darwin-driver.o): Likewise.
	* config/t-sol2 (sol2-c.o): Likewise.
	(sol2.o): Likewise.
	* config/t-vxworks (vxworks.o): Likewise.
	* config/x-darwin (host-darwin.o): Likewise.
	* config/x-hpux (host-hpux.o): Likewise.
	* config/x-linux (host-linux.o): Likewise.
	* config/x-solaris (host-solaris.o): Likewise.
	* config/alpha/x-alpha (driver-alpha.o): Likewise.
	* config/arm/t-arm (arm-c.o): Likewise.
	* config/arm/t-pe (pe.o): Likewise.
	* config/arm/t-wince-pe (pe.o): Likewise.
	* config/i386/t-cygming (winnt.o): Likewise.
	(winnt-cxx.o, winnt-stubs.o, msformat-c.o): Likewise.
	* config/i386/t-cygwin (cygwin1.o): Likewise.
	(cygwin2.o): Likewise.
	* config/i386/t-i386 (i386-c.o): Likewise.
	* config/i386/t-interix (winnt.o): Likewise.
	* config/i386/t-netware (netware.o): Likewise.
	* config/i386/t-nwld (nwld.o): Likewise.
	* config/i386/x-darwin (host-i386-darwin.o): Likewise.
	* config/i386/x-i386 (driver-i386.o): Likewise.
	* config/i386/x-cygwin (host-cygwin.o): Likewise.
	* config/i386/x-mingw32 (host-mingw32.o): Likewise.
	* config/ia64/t-ia64 (ia64-c.o): Likewise.
	* config/m32c/t-m32c (m32c-pragma.o): Likewise.
	* config/mips/x-native (driver-native.o): Likewise.
	* config/rs6000/t-rs6000 (rs6000-c.o): Likewise.
	* config/rs6000/x-darwin (host-ppc-darwin.o): Likewise.
	* config/rs6000/x-darwin64 (host-ppc64-darwin.o): Likewise.
	* config/rs6000/x-rs6000 (driver-rs6000.o): Likewise.
	* config/score/t-score-elf (score7.o): Likewise.
	(score3.o): Likewise.
	* config/sh/t-sh (sh-c.o): Likewise.
	* config/sh/t-symbian (sh-c.o): Likewise.
	(symbian.o): Likewise.
	* config/spu/t-spu-elf (spu-c.o): Likewise.
	* config/v850/t-v850 (v850-c.o): Likewise.
	* config/v850/t-v850e (v850-c.o): Likewise.
ada/:
	* gcc-interface/Makefile.in (COMPILER): Define.
	(COMPILER_FLAGS, ALL_COMPILERFLAGS): Define.
	(.c.o, cio.o, init.o, initialize.o, targext.o): Use $(COMPILER).
	(seh_init.o, tracebak.o): Likewise.
	* gcc-interface/Make-lang.in (ada/targext.o): Likewise.
	(ada/cio.o, ada/init.o, ada/initialize.o, ada/raise.o): Likewise.
	(ada/tracebak.o, ada/cuintp.o, ada/decl.o, ada/misc.o): Likewise.
	(ada/targtyps.o, ada/trans.o, ada/utils.o): Likewise.
	(ada/utils2.o): Likewise.
cp/:
	* Make-lang.in (g++spec.o): Use $(COMPILER).
	(g++$(exeext), cc1plus-dummy$(exeext)): Likewise.
	(cc1plus$(exeext)): Likewise.
fortran/:
	* Make-lang.in (gfortranspec.o): Use $(COMPILER).
	(gfortran$(exeext), f951$(exeext), fortran/cpp.o): Likewise.
java/:
	* Make-lang.in (jvspec.o): Use $(COMPILER).
	($(XGCJ)$(exeext), jc1$(exeext), jcf-dump$(exeext)): Likewise.
	(jvgenmain$(exeext), java/jcf-io.o, java/jcf-path.o): Likewise.
objc/:
	* Make-lang.in (cc1obj-dummy$(exeext)): Use $(COMPILER).
	(cc1obj$(exeext)): Likewise.
objcp/:
	* Make-lang.in (cc1objplus-dummy$(exeext)): Use $(COMPILER).
	(cc1objplus$(exeext), objcp/objcp-act.o): Likwise.

""",
u"""
	* config/arm/neon-gen.ml: Include vxWorks.h rather than stdint.h
	for VxWorks kernels.
	* config/arm/arm_neon.h: Regenerate.

""",
u"""

	PR middle-end/40252
	* fold-const.c (fold_binary): Use the correct types for building
	rotates.

	* gcc.c-torture/compile/pr40252.c: New testcase.

""",
u"""

	PR middle-end/40252
	* fold-const.c (fold_binary): Use the correct types for building
	rotates.

	* gcc.c-torture/compile/pr40252.c: New testcase.

""",
u"""
Fix PR c++/40007

    gcc/cp/ChangeLog:
    	PR c++/40007
    	* cp-tree.h (MEMBER_TYPES_NEEDING_ACCESS_CHECK): Remove this accessor.
    	(TI_TYPEDEFS_NEEDING_ACCESS_CHECKING): New accessor.
    	(get_types_needing_access_check): Declare new entry point.
    	* pt.c (append_type_to_template_for_access_check_1,
    	get_types_needing_access_check): New functions.
    	(perform_typedefs_access_check): Accept FUNCTION_DECLs and
    	RECORD_TYPEs rather than TEMPLATE_DECLs. Use the new
    	get_types_needing_access_check, no more
    	MEMBER_TYPES_NEEDING_ACCESS_CHECK.
    	(instantiate_class_template): Set input_location to the source
    	location of the most specialized template definition.
    	Perform access check using the RECORD_TYPE of the template, not its
    	associated most generic TEMPLATE_DECL.
    	(append_type_to_template_for_access_check): Augment function
    	comments. Use the new get_types_needing_access_check, not
    	MEMBER_TYPE_NEEDING_ACCESS_CHECK. Use the new
    	append_type_to_template_for_access_check_1 subroutine.

    gcc/testsuite/ChangeLog:
    	PR c++/40007
    	* g++.dg/template/typedef18.C: New test.
    	* g++.dg/template/typedef19.C: Likewise.
    	* g++.dg/template/typedef20.C: Likewise.
    	* g++.dg/template/access11.C: Adjust.


""",
u"""

	PR testsuite/40247
	* gcc.dg/struct/wo_prof_escape_substr_pointer.c: Obfuscate.

""",
u"""

	* tree-vect-data-refs.c (vect_create_data_ref_ptr): Remove
	redundant calls to merge_alias_info.
	(bump_vector_ptr): Likewise.
	* tree-ssa-copy.c (merge_alias_info): Remove.
	(replace_exp_1): Remove call to merge_alias_info.
	(propagate_tree_value): Likewise.
	(fini_copy_prop): Propagate points-to info.
	* tree-flow.h (merge_alias_info): Remove.

""",
u"""
  config/picochip/picochip.C (PARAM_INLINE_CALL_COST): Remove.


""",
u"""
	* gfortran.h (GFC_MPC_RND_MODE): New.
	* simplify.c (call_mpc_func): New helper function.
	(gfc_simplify_cos, gfc_simplify_exp, gfc_simplify_log,
	gfc_simplify_sin, gfc_simplify_sqrt): Add MPC support.


""",
u"""
Daily bump.
""",
u"""
	PR c++/38064
	* typeck.c (cp_build_binary_op): Allow ENUMERAL_TYPE in
	arithmetic comparisons.
	(cp_common_type): Handle scoped enums.

	* call.c (promoted_arithmetic_type_p): Don't use INTEGRAL_TYPE_P.
	(add_builtin_candidate, add_builtin_candidates): Likewise.
	(convert_like_real): Likewise.
	* class.c (check_bitfield_decl): Likewise.
	* decl.c (check_static_variable_definition): Likewise.
	(compute_array_index_type): Likewise.
	* decl2.c (grokbitfield): Likewise.
	* init.c (build_new_1): Likewise.
	* pt.c (convert_nontype_argument): Likewise.
	(current_instantiation): Likewise.
	* tree.c (pod_type_p): Likewise.
	* typeck.c (build_static_cast_1): Likewise.
	(build_reinterpret_cast_1): Likewise.
""",
u"""
	* cgraph.c (dump_cgraph_node): Dump size/time/benefit.
	* cgraph.h (struct inline_summary): New filed self_wize,
	size_inlining_benefit, self_time and time_inlining_benefit.
	(struct cgraph_global_info): Replace insns by time ans size fields.
	* ipa-cp (ipcp_cloning_candidate_p): Base estimate on size
	(ipcp_estimate_growth, ipcp_insert_stage): Likewise.
	(ipcp_update_callgraph): Do not touch function bodies.
	* ipa-inline.c: Include except.h
	(MAX_TIME): New constant.
	(overall_insns): Remove.
	(leaf_node_p): New.
	(overall_size, max_benefit): New static variables.
	(cgraph_estimate_time_after_inlining): New function.
	(cgraph_estimate_size_after_inlining): Rewrite using benefits.
	(cgraph_clone_inlined_nodes): Update size.
	(cgraph_mark_inline_edge): Update size.
	(cgraph_estimate_growth): Use size info.
	(cgraph_check_inline_limits): Check size.
	(cgraph_default_inline_p): Likewise.
	(cgraph_edge_badness): Compute badness based on benefit and size cost.
	(cgraph_decide_recursive_inlining): Check size.
	(cgraph_decide_inlining_of_small_function): Update size; dump sizes and
	times.
	(cgraph_decide_inlining): Likewise.
	(cgraph_decide_inlining_incrementally): Likewise; honor
	PARAM_EARLY_INLINING_INSNS.
	(likely_eliminated_by_inlining_p): New predicate.
	(estimate_function_body_sizes): New function.
	(compute_inline_parameters): Use it.
	* except.c (must_not_throw_labels): New function.
	* except.h (must_not_throw_labels): Declare.
	* tree-inline.c (init_inline_once): Kill inlining_weigths
	* tree-ssa-structalias.c: Avoid uninitialized warning.
	* params.def (PARAM_MAX_INLINE_INSNS_SINGLE): Reduce to 300.
	(PARAM_MAX_INLINE_INSNS_AUTO): Reduce to 60.
	(PARAM_INLINE_CALL_COST): Remove.
	(PARAM_EARLY_INLINING_INSNS): New.

""",
u"""

	PR tree-optimization/36327
	* tree-ssa-alias.c (walk_non_aliased_vuses): Add second walker
	callback for reference translation or lookup at the point
	of may-defs.
	* tree-ssa-alias.h (walk_non_aliased_vuses): Adjust prototype.
	* tree-ssa-sccvn.c (get_ref_from_reference_ops): Bail out
	for union COMPONENT_REFs.
	(vn_reference_lookup_3): New callback.  Lookup from memset
	and CONSTRUCTOR assignment, translate through struct copies.
	(vn_reference_lookup_pieces): Make sure to not free the
	passed operands array.  Adjust walk_non_aliased_vuses call.
	(vn_reference_lookup): Adjust walk_non_aliased_vuses call,
	make sure we do not leak memory.

	* gcc.dg/tree-ssa/ssa-fre-24.c: New testcase.
	* gcc.dg/tree-ssa/ssa-fre-25.c: Likewise.
	* gcc.dg/tree-ssa/sra-2.c: Disable FRE.
	* gcc.dg/vect/no-vfa-vect-43.c: Adjust.
	* gcc.dg/vect/vect-40.c: Likewise.
	* gcc.dg/vect/vect-42.c: Likewise.
	* gcc.dg/vect/vect-46.c: Likewise.
	* gcc.dg/vect/vect-76.c: Likewise.

""",
u"""

	PR fortran/40176
	* primary.c (gfc_match_varspec): Handle procedure pointer components
	with array return value.
	* resolve.c (resolve_expr_ppc): Ditto.
	(resolve_symbol): Make sure the interface of a procedure pointer has
	been resolved.
	* trans-array.c (gfc_walk_function_expr): Handle procedure pointer
	components with array return value.
	* trans-expr.c (gfc_conv_component_ref,gfc_conv_procedure_call,
	gfc_trans_arrayfunc_assign): Ditto.
	(gfc_trans_pointer_assignment): Handle procedure pointer assignments,
	where the rhs is a dummy argument.
	* trans-types.c (gfc_get_ppc_type,gfc_get_derived_type): Handle
	procedure pointer components with array return value.



	PR fortran/40176
	* gfortran.dg/proc_ptr_18.f90: New.
	* gfortran.dg/proc_ptr_19.f90: New.
	* gfortran.dg/proc_ptr_comp_9.f90: New.
	* gfortran.dg/proc_ptr_comp_10.f90: New.


""",
u"""

	* tree-ssa-alias.h (dump_points_to_solution): Declare.
	* tree-inline.c (expand_call_inline): Reset the escaped and
	callused solutions.
	* tree-ssa-structalias.c (pass_build_ealias): New.
	* tree-pass.h (pass_build_ealias): Declare.
	* passes.c (init_optimization_passes): Add PTA during 
	early optimizations.
	* tree-ssa-alias.c (dump_alias_info): Dump the ESCAPED
	and CALLUSED solutions.
	(dump_points_to_solution): New function, split out from ...
	(dump_points_to_info_for): ... here.
	* tree-parloops.c (parallelize_loops): Reset the escaped and
	callused solutions.

	* gcc.dg/tree-ssa/ssa-fre-14.c: Adjust.
	* gcc.dg/tree-ssa/ssa-fre-15.c: Likewise.

""",
u"""

	* makefile.vms: New file to compile gas on VMS.

	* configure.com: New file to do configuration on VMS with DCL.


""",
u"""
	PR bootstrap/40027
	* config/i386/i386.c (USE_HIDDEN_LINKONCE): Only define if missing.
	* config/i386/sol2.h [!TARGET_GNU_LD] (USE_HIDDEN_LINKONCE): Define.

""",
u"""

	PR tree-optimization/40238
	* tree-vect-stmts.c (vect_init_vector): Insert initialization
	statements after basic block's labels.
	* tree-vect-slp.c (vect_slp_transform_bb): Call destroy_bb_vec_info() 
	to free	the allocated memory.


""",
u"""
	    Dominique Dhumieres

	PR fortran/35732
	PR fortran/39872
	* trans-array.c (gfc_conv_ss_startstride): Add one to index.
	* gfortran.dg/bounds_check_fail_3.f90: New test.
	* gfortran.dg/bounds_check_fail_4.f90: New test.
	* gfortran.dg/bounds_check_14.f90: Update test.
	* gfortran.dg/bound_4.f90: Update test.

""",
u"""
Daily bump.
""",
u"""
	* gcc/config/sh/sh.c (sh_set_return_address): Mark store of
	return address with a USE.


""",
u"""

	PR middle-end/40233
	* tree.c (make_vector_type): Build the TYPE_DEBUG_REPRESENTATION_TYPEs
	array type from the main variant of the inner type.

	* gcc.c-torture/compile/pr40233.c: New testcase.

""",
u"""
	* Makefile.tpl (compare-target): Skip ./ada/*tools directories.
	* Makefile.in: Regenerate.

""",
u"""
	* gfortran.dg/erf_2.F90 (dg-options): Add -mieee
	for alpha*-*-* targets.

""",
u"""

	* config/vax/vax-protos.h (legitimate_constant_address_p): Change
	definition to bool (from int) to un-break build.
	(legitimate_constant_p, vax_mode_dependent_address_p): Likewise.

""",
u"""

	* tree-ssa-operands.h (push_stmt_changes, pop_stmt_changes,
	discard_stmt_changes): Delete.
	* tree-ssa-operands.c (scb_stack): Delete.
	(init_ssa_operands): Do not initialize it.
	(fini_ssa_operands): Do not free it.
	(push_stmt_changes, pop_stmt_changes, discard_stmt_changes): Delete.

	* tree-cfg.c (replace_uses_by): Replace pop_stmt_changes with 
	update_stmt, remove the others.  Fix comments.
	* tree-dfa.c (optimize_stack_restore): Likewise.
	* tree-ssa-forwprop.c (forward_propagate_addr_expr): Likewise.
	* tree-ssa-loop-ivopts.c (rewrite_use): Likewise.
	* tree-ssa-dce.c (eliminate_unnecessary_stmts): Likewise.
	* tree-ssa-ccp.c (optimize_stack_restore, execute_fold_all_builtins):
	Likewise.
	* tree-ssa-propagate.c (substitute_and_fold): Likewise.
	* tree-ssa-dom.c (propagate_rhs_into_lhs): Likewise.
	(dom_opt_finalize_block): Likewise, adjusting access to stmts_to_rescan.
	(optimize_stmt): Likewise, adjusting access to stmts_to_rescan.
	(stmts_to_rescan): Change item type to gimple.
	(tree_ssa_dominator_optimize): Change type of stmts_to_rescan.

""",
u"""
        * switch.adb (Is_Internal_GCC_Switch, Switch_Last): Bodies of ...
        * switch.ads (Is_Internal_GCC_Switch, Switch_Last): New functions.
        Add -auxbase variants to the list of recognized internal switches.
        * back_end.adb (Scan_Back_End_Switches): Use the new functions and
        adjust comments.
        * lib.ads: Make comment on internal GCC switches more general.
        * gcc-interface/lang-specs.h (specs for Ada): Pass -auxbase variants
        as for C.


""",
u"""

	* doc/passes.texi (Tree-SSA passes): Document SLP pass.
	* tree-pass.h (pass_slp_vectorize): New pass.
	* params.h (SLP_MAX_INSNS_IN_BB): Define.
	* timevar.def (TV_TREE_SLP_VECTORIZATION): Define.
	* tree-vectorizer.c (timevar.h): Include.
	(user_vect_verbosity_level): Declare.
	(vect_location): Fix comment.
	(vect_set_verbosity_level): Update user_vect_verbosity_level
	instead of vect_verbosity_level.
	(vect_set_dump_settings): Add an argument. Ignore user defined
	verbosity if dump flags require higher level of verbosity. Print to
	stderr only for loop vectorization.
	(vectorize_loops): Update call to vect_set_dump_settings.
	(execute_vect_slp): New function.
	(gate_vect_slp): Likewise.
	(struct gimple_opt_pass pass_slp_vectorize): New.
	* tree-vectorizer.h (struct _bb_vec_info): Define along macros to
	access its members.
	(vec_info_for_bb): New function.
	(struct _stmt_vec_info): Add bb_vinfo and a macro for its access.
	(VECTORIZATION_ENABLED): New macro.
	(SLP_ENABLED, SLP_DISABLED): Likewise.
	(vect_is_simple_use): Add bb_vec_info argument.
	(new_stmt_vec_info, vect_analyze_data_ref_dependences,
	vect_analyze_data_refs_alignment, vect_verify_datarefs_alignment,
	vect_analyze_data_ref_accesses, vect_analyze_data_refs,
	vect_schedule_slp, vect_analyze_slp): Likewise.
	(vect_analyze_stmt): Add slp_tree argument.
	(find_bb_location): Declare.
	(vect_slp_analyze_bb, vect_slp_transform_bb): Likewise.
	* tree-vect-loop.c (new_loop_vec_info): Adjust function calls.
	(vect_analyze_loop_operations, vect_analyze_loop,
	get_initial_def_for_induction, vect_create_epilog_for_reduction,
	vect_finalize_reduction, vectorizable_reduction,
	vectorizable_live_operation, vect_transform_loop): Likewise.
	* tree-data-ref.c (dr_analyze_innermost): Update comment,
	skip evolution analysis if analyzing a basic block.
	(dr_analyze_indices): Likewise.
	(initialize_data_dependence_relation): Skip the test whether the
	object is invariant for basic blocks.
	(compute_all_dependences): Skip dependence analysis for data
	references in basic blocks.
	(find_data_references_in_stmt): Don't fail in case of invariant
	access in basic block.
	(find_data_references_in_bb): New function.
	(find_data_references_in_loop): Move code to
	find_data_references_in_bb    and add a call to it.
	(compute_data_dependences_for_bb): New function.
	* tree-data-ref.h (compute_data_dependences_for_bb): Declare.
	* tree-vect-data-refs.c (vect_check_interleaving): Adjust to the case
	that STEP is 0.
	(vect_analyze_data_ref_dependence): Check for interleaving in case of
	unknown dependence in basic block and fail in case of dependence in
	basic block.
	(vect_analyze_data_ref_dependences): Add bb_vinfo argument, get data
	dependence instances from either loop or basic block vectorization
	info.
	(vect_compute_data_ref_alignment): Check if it is loop vectorization
	before calling nested_in_vect_loop_p.
	(vect_compute_data_refs_alignment): Add bb_vinfo argument, get data
	dependence instances from either loop or basic block vectorization
	info.
	(vect_verify_datarefs_alignment): Likewise.
	(vect_enhance_data_refs_alignment): Adjust function calls.
	(vect_analyze_data_refs_alignment): Likewise.
	(vect_analyze_group_access): Fix printing. Skip different checks if
	DR_STEP is 0. Keep strided stores either in loop or basic block
	vectorization data structure. Fix indentation.
	(vect_analyze_data_ref_access): Fix comments, allow zero step in
	basic blocks.
	(vect_analyze_data_ref_accesses): Add bb_vinfo argument, get data
	dependence instances from either loop or basic block vectorization
	info.
	(vect_analyze_data_refs): Update comment. Call
	compute_data_dependences_for_bb to analyze basic blocks.
	(vect_create_addr_base_for_vector_ref): Check for outer loop only in
	case of loop vectorization. In case of basic block vectorization use
	data-ref itself   as  a base.
	(vect_create_data_ref_ptr): In case of basic block vectorization:
	don't advance the pointer, add new statements before the current
	statement.  Adjust function calls.
	(vect_supportable_dr_alignment): Support only aligned accesses in
	basic block vectorization.
	* common.opt (ftree-slp-vectorize): New flag.
	* tree-vect-patterns.c (widened_name_p): Adjust function calls.
	(vect_pattern_recog_1): Likewise.
	* tree-vect-stmts.c (process_use): Likewise.
	(vect_init_vector): Add new statements in the beginning of the basic
	block in case of basic block SLP.
	(vect_get_vec_def_for_operand): Adjust function calls.
	(vect_finish_stmt_generation): Likewise.
	(vectorizable_call): Add assert that it is loop vectorization, adjust
	function calls.
	(vectorizable_conversion, vectorizable_assignment): Likewise.
	(vectorizable_operation): In case of basic block SLP, take
	vectorization factor from statement's type and skip the relevance
	check. Adjust function calls.
	(vectorizable_type_demotion): Add assert that it is loop
	vectorization, adjust function calls.
	(vectorizable_type_promotion): Likewise.
	(vectorizable_store): Check for outer loop only in case of loop
	vectorization. Adjust function calls. For basic blocks, skip the
	relevance check and don't advance pointers.
	(vectorizable_load): Likewise.
	(vectorizable_condition): Add assert that it is loop vectorization,
	adjust function calls.
	(vect_analyze_stmt): Add argument. In case of basic block SLP, check
	that it is not reduction, get vector type, call only supported
	functions, skip loop    specific parts.
	(vect_transform_stmt): Check for outer loop only in case of loop
	vectorization.
	(new_stmt_vec_info): Add new argument and initialize bb_vinfo.
	(vect_is_simple_use): Fix comment, add new argument, fix conditions
	for external definition.
	* passes.c (pass_slp_vectorize): New pass.
	* tree-vect-slp.c (find_bb_location): New function.
	(vect_get_and_check_slp_defs): Add argument, adjust function calls,
	check for patterns only in loops.
	(vect_build_slp_tree): Add argument, adjust function calls, fail in
	case of multiple types in basic block SLP.
	(vect_mark_slp_stmts_relevant): New function.
	(vect_supported_load_permutation_p): Fix comment.
	(vect_analyze_slp_instance): Add argument. In case of basic block
	SLP, take vectorization factor from statement's type, check that
	unrolling factor is 1. Adjust function call. Save SLP instance in
	either loop or basic block vectorization structure. Return FALSE,
	if SLP failed.
	(vect_analyze_slp): Add argument. Get strided stores groups from
	either loop or basic block vectorization structure. Return FALSE
	if basic block SLP failed.
	(new_bb_vec_info): New function.
	(destroy_bb_vec_info, vect_slp_analyze_node_operations,
	vect_slp_analyze_operations, vect_slp_analyze_bb): Likewise.
	(vect_schedule_slp): Add argument. Get SLP instances from either
	loop or basic block vectorization structure. Set vectorization factor
	to be 1 for basic block SLP.
	(vect_slp_transform_bb): New function.
	* params.def (PARAM_SLP_MAX_INSNS_IN_BB): Define.


""",
u"""
	
	* libsupc++/initializer_list (initializer_list): Add missing typedefs.

""",
u"""
Daily bump.
""",
u"""
	* final.c (shorten_branches): Do not align labels for jump tables.
	(final_scan_insn): Use JUMP_TABLE_DATA_P.

	* gcc.dg/falign-labels-1.c: New test.

""",
u"""
	* doc/passes.texi: Standardize spelling of RTL, Tree and Tree SSA.
	Remove outdated reference to flow.c and fix nits.
	* doc/gccint.texi: Tweak RTL description.
	* doc/rtl.texi: Likewise.

""",
u"""
	* gcc-interface/misc.c (gnat_get_subrange_bounds): Fix thinko.

""",
u"""
	* gcc-interface/decl.c (set_rm_size): Bypass the check for packed array
	types.

""",
u"""
	* gcc-interface/decl.c (gnat_to_gnu_entity) <object>: Do not modify the
	original type because of the alignment when there is an address clause.

""",
u"""
	* config/avr/avr.c: Change my email address.
	* config/avr/avr.h: Likewise.
	* config/avr/avr.md: Likewise.
	* config/avr/avr-protos.h: Likewise.
	* config/avr/libgcc.S: Likewise.



""",
u"""

	* config/spu/spu-protos.h (aligned_mem_p, spu_valid_mov): Remove.
	(spu_split_load, spu_split_store): Change return type to int.
	(spu_split_convert): Declare.
	* config/spu/predicates.md (spu_mem_operand): Remove.
	(spu_mov_operand): Update.
	(spu_dest_operand, shiftrt_operator, extend_operator): Define.
	* config/spu/spu.c (regno_aligned_for_load): Remove.
	(reg_aligned_for_addr, spu_expand_load): Define.
	(spu_expand_extv): Reimplement and handle MEM.
	(spu_expand_insv): Handle MEM.
	(spu_sched_reorder): Handle insn's with length 0.
	(spu_legitimate_address_p): Reimplement.
	(store_with_one_insn_p): Return TRUE for any mode with size
	larger than 16 bytes.
	(address_needs_split): Define.
	(spu_expand_mov): Call spu_split_load and spu_split_store for MEM
	operands.
	(spu_convert_move): Define.
	(spu_split_load): Use spu_expand_load and change all MEM's to
	TImode.
	(spu_split_store): Change all MEM's to TImode.
	(spu_init_expanders): Preallocate registers that correspond to
	LAST_VIRTUAL_REG+1 and LAST_VIRTUAL_REG+2 and set them with
	mark_reg_pointer.
	(spu_split_convert): Define.
	* config/spu/spu.md (QHSI, QHSDI): New mode iterators.
	(_move<mode>, _movdi, _movti): Update predicate and condition.
	(load, store): Change to define_split.
	(extendqiti2, extendhiti2, extendsiti2, extendditi2): Simplify to
	extend<mode>ti2.
	(zero_extendqiti2, zero_extendhiti2, <v>lshr<mode>3_imm): Define.
	(lshr<mode>3, lshr<mode>3_imm, lshr<mode>3_re): Simplify to one
	define_insn_and_split of lshr<mode>3.
	(shrqbybi_<mode>, shrqby_<mode>): Simplify to define_expand.
	(<v>ashr<mode>3_imm): Define.
	(extv, extzv, insv): Allow MEM operands.
	(trunc_shr_ti<mode>, trunc_shr_tidi, shl_ext_<mode>ti,
	shl_ext_diti, sext_trunc_lshr_tiqisi, zext_trunc_lshr_tiqisi,
	sext_trunc_lshr_tihisi, zext_trunc_lshr_tihisi): Define for combine.
	(_spu_convert2): Change to define_insn_and_split and remove the
	corresponding define_peephole2.
	(stack_protect_set, stack_protect_test, stack_protect_test_si):
	Change predicates to memory_operand.


""",
u"""
Fix typo in ChangeLog
""",
u"""
	* config/arm/thumb2.md: Add 16-bit multiply instructions.
	gcc/testsuite/

	* lib/target-supports.exp (check_effective_target_arm_thumb2_ok):
	New function.
	* gcc.target/arm/thumb2-mul-space.c: New file.
	* gcc.target/arm/thumb2-mul-space-2.c: New file.
	* gcc.target/arm/thumb2-mul-space-3.c: New file.
	* gcc.target/arm/thumb2-mul-speed.c: New file.

""",
u"""
Daily bump.
""",
u"""
Fix PR tree-optimization/40219
""",
u"""

	PR middle-end/38964
	* alias.c (write_dependence_p): Do not use TBAA for answering
	anti-dependence or output-dependence.
	* tree-ssa-structalias.c (set_uids_in_ptset): Remove TBAA pruning
	code.
	(emit_pointer_definition): Remove.
	(emit_alias_warning): Likewise.
	(find_what_var_points_to): Remove TBAA pruning code.
	(find_what_p_points_to): Likewise.  Do not warn about strict-aliasing
	violations.
	(compute_points_to_sets): Remove code computing the set of
	dereferenced pointers.
	* tree-data-ref.c (dr_may_alias_p): Properly use the split
	oracle for querying anti and output dependencies.
	* tree-ssa-alias.c (refs_may_alias_p_1): Add argument specifying
	if TBAA may be applied.
	(refs_anti_dependent_p): New function.
	(refs_output_dependent_p): Likewise.
	* tree-ssa-alias.h (refs_anti_dependent_p): Declare.
	(refs_output_dependent_p): Likewise.

	* doc/tree-ssa.texi (Memory model): New section.

	testsuite/
	* g++.dg/warn/Wstrict-aliasing-float-ref-int-obj.C: XFAIL.
	* gcc.dg/Wstrict-aliasing-converted-assigned.c: Likewise.
	* gcc.dg/Wstrict-aliasing-float-ptr-int-obj.c: Likewise.

	* doc/c-tree.texi (CHANGE_DYNAMIC_TYPE_EXPR): Remove.
	* doc/gimple.texi (GIMPLE_CHANGE_DYNAMIC_TYPE): Remove.

	* cfgexpand.c (expand_gimple_basic_block): Do not handle
	GIMPLE_CHANGE_DYNAMIC_TYPE or CHANGE_DYNAMIC_TYPE_EXPR.
	* expr.c (expand_expr_real_1): Likewise.
	* gimple-low.c (lower_stmt): Likewise.
	* gimple-pretty-print.c (dump_gimple_stmt): Likewise.
	(dump_gimple_cdt): Remove.
	* gimple.c (gss_for_code): Do not handle GIMPLE_CHANGE_DYNAMIC_TYPE.
	(gimple_size): Likewise.
	(walk_gimple_op): Likewise.
	(is_gimple_stmt): Likewise.
	(walk_stmt_load_store_addr_ops): Likewise.
	(gimple_build_cdt): Remove.
	* gimple.def (GIMPLE_CHANGE_DYNAMIC_TYPE): Remove.
	* gimple.h (gimple_cdt_new_type): Remove.
	(gimple_cdt_new_type_ptr): Likewise.
	(gimple_cdt_set_new_type): Likewise.
	(gimple_cdt_location): Likewise.
	(gimple_cdt_location_ptr): Likewise.
	(gimple_cdt_set_location): Likewise.
	* gimplify.c (gimplify_expr): Do not handle CHANGE_DYNAMIC_TYPE_EXPR.
	* tree-cfg.c (remove_useless_stmts_1): Do not handle
	GIMPLE_CHANGE_DYNAMIC_TYPE.
	(verify_types_in_gimple_stmt): Likewise.
	* tree-inline.c (estimate_num_insns): Likewise.
	(expand_call_inline): Do not copy DECL_NO_TBAA_P.
	(copy_decl_to_var): Likewise.
	(copy_result_decl_to_var): Likewise.
	* tree-pretty-print.c (dump_generic_node): Do not handle
	CHANGE_DYNAMIC_TYPE_EXPR.
	* tree-ssa-dce.c (mark_stmt_if_obviously_necessary): Likewise.
	* tree-ssa-operands.c (get_expr_operands): Likewise.
	* tree-ssa-structalias.c (struct variable_info): Remove
	no_tbaa_pruning member.
	(new_var_info): Do not set it based on DECL_NO_TBAA_P.
	(unify_nodes): Do not copy it.
	(find_func_aliases): Do not handle GIMPLE_CHANGE_DYNAMIC_TYPE.
	(dump_solution_for_var): Do not dump no_tbaa_pruning state.
	(set_uids_in_ptset): Do not check it.
	(find_what_var_points_to): Likewise.
	(compute_tbaa_pruning): Remove.
	(compute_points_to_sets): Do not call it.
	* tree.c (walk_tree_1): Do not handle CHANGE_DYNAMIC_TYPE_EXPR.
	* tree.def (CHANGE_DYNAMIC_TYPE_EXPR): Remove.
	* tree.h (CHANGE_DYNAMIC_TYPE_NEW_TYPE): Remove.
	(CHANGE_DYNAMIC_TYPE_LOCATION): Likewise.
	(DECL_NO_TBAA_P): Likewise.
	(struct tree_decl_common): Move no_tbaa_flag to unused flags section.
	* omp-low.c (copy_var_decl): Do not copy DECL_NO_TBAA_P.
	(expand_omp_atomic_pipeline): Do not set it.
	* print-tree.c (print_node): Do not dump it.
	* tree-ssa-copyrename.c (copy_rename_partition_coalesce): Remove
	redundant check.

	cp/
	* init.c (avoid_placement_new_aliasing): Remove.
	(build_new_1): Do not call it.

""",
u"""

	PR target/39856
	* reg-stack.c (subst_stack_regs_pat): Remove gcc_assert for note
	for clobber.


""",
u"""
	* src/x86/win32.S (_ffi_closure_STDCALL):  New function.
	(.eh_frame):  Add FDE for it.


""",
u"""
	* configure.ac:  Also check if assembler supports pc-relative
	relocs on X86_WIN32 targets.
	* configure:  Regenerate.
	* src/x86/win32.S (ffi_prep_args):  Declare extern, not global.
	(_ffi_call_SYSV):  Add missing function type symbol .def and
	add EH markup labels.
	(_ffi_call_STDCALL):  Likewise.
	(_ffi_closure_SYSV):  Likewise.
	(_ffi_closure_raw_SYSV):  Likewise.
	(.eh_frame):  Add hand-crafted EH data.


""",
u"""
	gcc/
	* tree.c (handle_dll_attribute): Mark dllexport'd inlines as
	non-external.

	gcc/cp
	* decl2.c (decl_needed_p): Consider dllexport'd functions needed.
	* semantics.c (expand_or_defer_fn): Similarly.

	gcc/testsuite/
	* gcc.dg/dll-6.c: New test.
	* gcc.dg/dll-6a.c: Likewise.
	* gcc.dg/dll-7.c: Likewise.
	* gcc.dg/dll-7a.c: Likewise.
	* g++.dg/ext/dllexport2.C: Likewise.
	* g++.dg/ext/dllexport2a.cc: Likewise.

""",
u"""

	PR libstdc++/40221
	* include/tr1_impl/functional: Add explicit cast.


""",
u"""
	PR fortran/40195
	* module.c (read_md5_from_module_file): Close file before returning.

""",
u"""
	* Makefile.in (bversion.h, s-bversion): New targets.
	(TOPLEV_H): Add bversion.h.
	* toplev.h: Include "bversion.h".
	(ATTRIBUTE_GCC_DIAG): When building with checking disabled, use
	the __format__ attribute only if compiling with the same version
	of GCC as the sources (the "build version").

""",
u"""
	* c-format.c (handle_format_attribute): Fix comment typo.

""",
u"""
	
	PR libstdc++/40094
	Revert:
	* include/ext/throw_allocator.h (throw_allocator_base): Avoid
	out of line member functions definitions.
	(throw_allocator_base::_S_g, _S_map, _S_throw_prob, _S_label):
	Remove, use static locals instead.
	(throw_allocator_base::do_check_allocated, print_to_string): Declare.
	* src/throw_allocator.cc: New.
	* src/Makefile.am: Add.
	* config/abi/pre/gnu.ver: Add exports.
	* src/Makefile.in: Regenerate.

""",
u"""
	
	PR libstdc++/40094
	Revert:
	* include/ext/throw_allocator.h (throw_allocator_base): Avoid
	out of line member functions definitions.
	(throw_allocator_base::_S_g, _S_map, _S_throw_prob, _S_label):
	Remove, use static locals instead.
	(throw_allocator_base::do_check_allocated, print_to_string): Declare.
	* src/throw_allocator.cc: New.
	* src/Makefile.am: Add.
	* config/abi/pre/gnu.ver: Add exports.
	* src/Makefile.in: Regenerate.

""",
u"""
Daily bump.
""",
u"""
	PR target/37846
	* gcc.target/ia64/mfused-madd-vect.c: New test.
	* gcc.target/ia64/mfused-madd.c: New test.
	* gcc.target/ia64/mno-fused-madd-vect.c: New test.
	* gcc.target/ia64/mno-fused-madd.c: New test.

""",
u"""
	PR target/37846
	* config/ia64/ia64.opt (mfused-madd): New.
	* config/ia64/ia64.h (TARGET_DEFAULT): Set MASK_FUSED_MADD.
	* config/ia64/hpux.h (TARGET_DEFAULT): Ditto.
	* config/ia64/ia64.md (maddsf4, msubsf4, nmaddsf4,
	madddf4, madddf4_trunc, msubdf4, msubdf4_trunc, nmadddf4,
	nmadddf4_truncsf, maddxf4, maddxf4_truncsf, maddxf4_truncdf,
	msubxf4, msubxf4_truncsf msubxf4_truncdf, nmaddxf4,
	nmaddxf4_truncsf, nmaddxf4_truncdf): Check TARGET_FUSED_MADD.
	* config/ia64/vect.md (addv2sf3, subv2sf3): Force fpma/fpms 
	instruction if !TARGET_FUSED_MADD.
	(fpma, fpms): Remove colon from name.

""",
u"""

	* tree-ssa-sccvn.c (copy_reference_ops_from_ref): Record
	TMR_ORIGINAL.  Always either record TMR_SYMBOL or TMR_BASE.
	* tree-ssa-pre.c (create_component_ref_by_pieces_1): Handle
	TARGET_MEM_REF.
	(create_expression_by_pieces): Only convert if necessary.
	* gimplify.c (gimplify_expr): Handle TARGET_MEM_REF.
	* tree-ssa-loop-im.c (gen_lsm_tmp_name): Handle INTEGER_CST.

""",
u"""
	* config/mips/mips.md (*extzv_trunc<mode>_exts): Turn into a
	regular pattern from a template and rename it ...
	(*extzv_truncsi_exts): ... to this.

""",
u"""

	* cgraph.h (struct cgraph_node): Remove inline_decl member.
	* ipa-inline.c (cgraph_mark_inline_edge): Do not check it.
	(cgraph_default_inline_p): Likewise.
	(cgraph_decide_inlining_incrementally): Likewise.

""",
u"""
	* MAINTAINERS: Update my e-mail address.

""",
u"""
gcc/


	* config/i386/cpuid.h (bit_MOVBE): New.

	* config/i386/driver-i386.c (host_detect_local_cpu): Check movbe.

	* config/i386/i386.c (OPTION_MASK_ISA_MOVBE_SET): New.
	(OPTION_MASK_ISA_MOVBE_UNSET): Likewise.
	(ix86_handle_option): Handle OPT_mmovbe.
	(ix86_target_string): Add -mmovbe.
	(pta_flags): Add PTA_MOVBE.
	(processor_alias_table): Add PTA_MOVBE to "atom".
	(override_options): Handle PTA_MOVBE.

	* config/i386/i386.h (TARGET_MOVBE): New.

	* config/i386/i386.md (bswapsi2): Check TARGET_MOVBE.
	(*bswapsi_movbe): New.
	(*bswapdi_movbe): Likewise.
	(bswapdi2): Renamed to ...
	(*bswapdi_1): This.
	(bswapdi2): New expander.

	* config/i386/i386.opt (mmovbe): New.

	* doc/invoke.texi: Document -mmovbe.

gcc/testsuite/


	* gcc.target/i386/movbe-1.c: New.
	* gcc.target/i386/movbe-2.c: Likewise.

""",
u"""
gcc/ChangeLog
	* plugin.c (try_init_one_plugin): Updated to new plugin_init API.
	* gcc-plugin.h (plugin_init): Updated signature.
	* gcc-plugin.h (plugin_name_args): Moved to this header.
	* doc/plugins.texi (plugin_init): Updated documention to reflect API change.
	* doc/plugins.texi (plugin_name_args): Added to documention.
gcc/testsuite/ChangeLog
	* gcc.dg/plugin/selfassign.c (plugin_init): Updated to new plugin_init signature.
	* g++.dg/plugin/selfassign.c (plugin_init): Updated to new plugin_init signature.
	* g++.dg/plugin/dumb_plugin.c (plugin_init): Updated to new plugin_init signature.
	* g++.dg/plugin/attribute_plugin.c (plugin_init): Updated to new plugin_init signature.

""",
u"""
	* config/arm/neon.md (*mul<mode>3add<mode>_neon): New pattern.
	(*mul<mode>3neg<mode>add<mode>_neon): Likewise.

	* gcc.dg/target/arm/neon-vmla-1.c: New.
	* gcc.dg/target/arm/neon-vmls-1.c: Likewise.

""",
u"""
	* configure.ac (cygwin noconfigdirs):  Remove libgcj.
	* configure:  Regenerate.


""",
u"""

	* config/i386/i386.c: Use REG_P, MEM_P, CONST_INT_P, LABEL_P and
	JUMP_TABLE_DATA_P predicates where applicable.
	* config/i386/predicates.md: Ditto.
	* config/i386/sse.md: Ditto.

""",
u"""
	* config/i386/i386.md (adddi_4_rex64, addsi_4, addhi_4): For
	operand2 -128 override length_immediate attribute to 1.
	* config/i386/predicates.md (constm128_operand): New predicate.

""",
u"""
	* config/i386/i386.c (memory_address_length): Handle %r12
	the same as %rsp and %r13 the same as %rbp.  For %rsp and %rbp
	also check REGNO.
	(ix86_attr_length_address_default): For MODE_SI lea in 64-bit
	mode look through optional ZERO_EXTEND and SUBREG.
	* config/i386/i386.md (R12_REG): New define_constant.
	(prefix_data16): For sse unit set also for MODE_TI insns.
	(prefix_rex): For -m32 always return 0.  For TYPE_IMOVX
	insns set if operand 1 is ext_QIreg_operand.
	(modrm): For TYPE_IMOV clear only if not MODE_DI.  For
	TYPE_{ALU{,1},ICMP,TEST} insn clear if there is non-shortened
	immediate.
	(*movdi_extzv_1, zero_extendhidi2, zero_extendqidi2): Change
	mode from MODE_DI to MODE_SI.
	(movdi_1_rex64): Override modrm and length_immediate attributes
	only for movabs (TYPE_IMOV, alternative 2).
	(zero_extendsidi2_rex64): Clear prefix_0f attribute if TYPE_IMOVX.
	(*float<SSEMODEI24:mode><MODEF:mode>2_mixed_interunit,
	*float<SSEMODEI24:mode><MODEF:mode>2_mixed_nointerunit,
	*float<SSEMODEI24:mode><MODEF:mode>2_sse_interunit,
	*float<SSEMODEI24:mode><MODEF:mode>2_sse_nointerunit): Set
	prefix_rex attribute if DImode.
	(*adddi_1_rex64, *adddi_2_rex64, *adddi_3_rex64, *adddi_5_rex64,
	*addsi_1, *addsi_1_zext, *addsi_2, *addsi_2_zext, *addsi_3,
	*addsi_3_zext, *addsi_5, *addhi_1_lea, *addhi_1, *addhi_2, *addhi_3,
	*addhi_5, *addqi_1_lea, *addqi_1): Override length_immediate
	attribute to 1 if TYPE_ALU and operand 2 is const128_operand.
	(pro_epilogue_adjust_stack_1, pro_epilogue_adjust_stack_rex64):
	Likewise.  For TYPE_IMOV clear length_immediate attribute.
	(*ashldi3_1_rex64, *ashldi3_cmp_rex64, *ashldi3_cconly_rex64,
	*ashlsi3_1, *ashlsi3_1_zext, *ashlsi3_cmp, **ashlsi3_cconly,
	*ashlsi3_cmp_zext, *ashlhi3_1_lea, *ashlhi3_1, *ashlhi3_cmp,
	*ashlhi3_cconly, *ashlqi3_1_lea, *ashlqi3_1, *ashlqi3_cmp,
	*ashlqi3_cconly): Override length_immediate attribute to 0 if TYPE_ALU
	or one operand TYPE_ISHIFT.
	(*ashrdi3_1_one_bit_rex64, *ashrdi3_one_bit_cmp_rex64,
	*ashrdi3_one_bit_cconly_rex64, *ashrsi3_1_one_bit,
	*ashrsi3_1_one_bit_zext, *ashrsi3_one_bit_cmp,
	*ashrsi3_one_bit_cconly, *ashrsi3_one_bit_cmp_zext,
	*ashrhi3_1_one_bit, *ashrhi3_one_bit_cmp, *ashrhi3_one_bit_cconly,
	*ashrqi3_1_one_bit, *ashrqi3_1_one_bit_slp, *ashrqi3_one_bit_cmp,
	*ashrqi3_one_bit_cconly, *lshrdi3_1_one_bit_rex64,
	*lshrdi3_cmp_one_bit_rex64, *lshrdi3_cconly_one_bit_rex64,
	*lshrsi3_1_one_bit, *lshrsi3_1_one_bit_zext, *lshrsi3_one_bit_cmp,
	*lshrsi3_one_bit_cconly, *lshrsi3_cmp_one_bit_zext,
	*lshrhi3_1_one_bit, *lshrhi3_one_bit_cmp, *lshrhi3_one_bit_cconly,
	*lshrqi3_1_one_bit, *lshrqi3_1_one_bit_slp, *lshrqi2_one_bit_cmp,
	*lshrqi2_one_bit_cconly, *rotlsi3_1_one_bit_rex64, *rotlsi3_1_one_bit,
	*rotlsi3_1_one_bit_zext, *rotlhi3_1_one_bit, *rotlqi3_1_one_bit_slp,
	*rotlqi3_1_one_bit, *rotrdi3_1_one_bit_rex64, *rotrsi3_1_one_bit,
	*rotrsi3_1_one_bit_zext, *rotrhi3_one_bit, *rotrqi3_1_one_bit,
	*rotrqi3_1_one_bit_slp): Override length_immediate attribute to 0,
	set mode attribute, don't override length attribute.
	(*btsq, *btrq, *btcq, *btdi_rex64, *btsi): Set prefix_0f attribute
	to 1.
	(return_internal_long): Set length attribute to 2 instead of 1.
	(*strmovqi_rex_1, *strsetqi_rex_1, *rep_stosqi_rex64,
	*cmpstrnqi_nz_rex_1, *cmpstrnqi_rex_1, *strlenqi_rex_1): Clear
	prefix_rex attribute.
	* config/i386/predicates.md (ext_QIreg_operand,
	const128_operand): New predicates.
	(memory_displacement_only_operand): Always return 0 for
	TARGET_64BIT.

""",
u"""

	* config/arm/thumb2.md (orsi_notsi_si): Fix typo in pattern. 


""",
u"""
./:
	* tree.c (build_tree_list_vec_stat): New function.
	(ctor_to_vec): New function.
	(build_nt_call_vec): New function.
	(build_call_array): Change args to be a const pointer.
	(build_call_vec): New function.
	* tree.h (build_nt_call_vec): Declare.
	(build_tree_list_vec_stat): Declare.
	(build_tree_list_vec): Define.
	(build_call_array): Update declaration.
	(build_call_vec): Declare.
	(ctor_to_vec): Declare.
	* c-common.c (tree_vector_cache): New static variable.
	(make_tree_vector): New function.
	(release_tree_vector): New function.
	(make_tree_vector_single): New function.
	(make_tree_vector_copy): New function.
	* c-common.h (tree_vector_cache, make_tree_vector): Declare.
	(make_tree_vector_single, make_tree_vector_copy): Declare.
	* c-parser.c (cached_expr_list_1, cached_expr_list_2): Remove.
	(c_parser_expr_list): Don't manage cache here, instead call
	make_tree_vector.
	(c_parser_release_expr_list): Remove static function.
	(c_parser_vec_to_tree_list): Remove static function.
	(c_parser_attributes): Call build_tree_list_vec instead of
	c_parser_vec_to_tree_list.  Call release_tree_vector instead of
	c_parser_release_expr_list.
	(c_parser_postfix_expression_after_primary): Likewise.
	(c_parser_objc_keywordexpr): Likewise.
cp/:
	* parser.c (cp_parser_postfix_expression): Change args to a vec.
	Release it when done.
	(tree_vector): Define typedef.  Define VEC functions.
	(cp_parser_parenthesized_expression_list): Change return type to
	vec.  Change all callers.
	(cp_parser_new_expression): Change placement and initializer to
	vecs.  Release them when done.
	(cp_parser_new_placement): Change return type to vec.  Change all
	callers.
	(cp_parser_new_initializer): Likewise.
	* typeck.c (build_function_call_vec): Just call
	cp_build_function_call_vec.
	(cp_build_function_call): Just build a vec and call
	cp_build_function_call_vec.
	(cp_build_function_call_vec): New function based on old
	cp_build_function_call.
	(convert_arguments): Remove nargs and argarray parameters.  Change
	values to a vec.  Change caller.
	(build_x_compound_expr_from_vec): New function.
	(cp_build_modify_expr): Build vec to pass to
	build_special_member_call.
	* call.c (struct z_candidate): Add first_arg field.  Change args
	field to vec.
	(convert_class_to_reference): Handle first argument separately.
	(add_candidate): Add first_arg parameter.  Change args parameter
	to vec.  Change all callers.
	(add_function_candidate, add_conv_candidate): Likewise.
	(add_template_candidate_real, add_template_candidate): Likewise.
	(add_template_conv_candidate): Likewise.
	(build_user_type_conversion_1): Handle first argument separately.
	(resolve_args): Change return type and parameter type to vecs.
	Change all callers.
	(perform_overload_resolution): Change args parameter to vec.
	Change all callers.
	(build_new_function_call, build_operator_new_call): Likewise.
	(add_candidates): Likewise.
	(build_op_call): New globally visible function, built from and
	replacing static function build_object_call.
	(build_new_op): Don't handle CALL_EXPR.  Build vec, not tree_list,
	of arguments.
	(build_op_delete_call): Build vec to pass to
	cp_build_function_call_vec.
	(build_temp): Build vec to pass to build_special_member_call.
	(convert_like_real): Likewise.
	(perform_direct_initialization_if_possible): Likewise.
	(build_over_call): Handle first_arg field.  Use build_call_array
	rather than build_call_list.
	(build_special_member_call): Change args parameter to vec.  Change
	all callers.
	(build_new_method_call): Likewise.
	* init.c (expand_default_init): Change parms to vec.
	(build_raw_new_expr): Change placement and init to vecs.  Change
	all callers.
	(build_new_1, build_new): Likewise.
	* class.c (resolve_address_of_overloaded_function): Build array to
	pass to fn_type_unification.
	* pt.c (tsubst_copy_and_build): For NEW_EXPR build vecs to pass to
	build_new.  For CALL_EXPR create a vec rather than a tree_list;
	expand a pack if necessary.
	(fn_type_unification): Change args parameter to const tree *.  Add
	nargs parameter.  Change all callers.
	(type_unification_real): Likewise.
	(unify): Build array to pass to type_unification_real.
	(get_bindings): Build array to pass to fn_type_unification.
	(any_type_dependent_arguments_p): Change args parameter to a vec.
	Change all callers.
	(make_args_non_dependent): Renamed from build_non_dependent_args.
	Change return type to void.  Change parameter type to vec.  Change
	all callers.
	(do_auto_deduction): Pass an array to type_unification_real.
	* semantics.c (perform_koenig_lookup): Change args to vec.  Change
	all callers.
	(finish_call_expr): Change args to vec.  Change all callers.  Call
	build_op_call instead of passing CALL_EXPR to build_new_op.
	(cxx_omp_create_clause_info): Allocate vec to pass to
	build_special_member_call.
	* decl2.c (build_offset_ref_call_from_tree): Change args parameter
	to vec.  Change all callers.
	* name-lookup.c (lookup_function_nonclass): Likewise.
	(struct arg_lookup): Change args to vec.
	(arg_assoc_namespace): Handle args as a vec.
	(arg_assoc_args_vec): New static function.
	(lookup_arg_dependent): Change args parameter to vec.  Change all
	callers.
	* method.c (do_build_assign_ref): Allocate vec to pass to
	build_special_member_call.
	* except.c (build_throw): Likewise.
	* typeck2.c (build_functional_cast): Likewise.
	* cvt.c (ocp_convert): Likewise.
	* tree.c (build_min_non_dep_call_vec): Change last parameter to
	vec.  Change all callers.
	* cp-tree.h: Update declarations.
	* name-lookup.h: Update declarations.
objc/:
	* objc-act.c (objc_generate_cxx_ctor_or_dtor): Pass NULL rather
	than NULL_TREE to build_special_member_call.

""",
u"""

	gcc/
	* doc/tm.texi (Misc): Document TARGET_INVALID_PARAMETER_TYPE,
	TARGET_INVALID_RETURN_TYPE, TARGET_PROMOTED_TYPE, and
	TARGET_CONVERT_TO_TYPE.
	* hooks.c (hook_tree_const_tree_null): Define.
	* hooks.h (hook_tree_const_tree_null): Declare.
	* target.h (struct gcc_target):  Add invalid_parameter_type,
	invalid_return_type, promoted_type, and convert_to_type fields.
	* target-def.h: (TARGET_INVALID_PARAMETER_TYPE): Define.
	(TARGET_INVALID_RETURN_TYPE): Define.
	(TARGET_PROMOTED_TYPE): Define.
	(TARGET_CONVERT_TO_TYPE): Define.
	(TARGET_INITIALIZER): Update for new fields.
	* c-decl.c (grokdeclarator): Check targetm.invalid_return_type.
	(grokparms): Check targetm.invalid_parameter_type.
	* c-typeck.c (default_conversion): Check targetm.promoted_type.
	* c-convert.c (convert): Check targetm.convert_to_type.

	gcc/cp/
	* typeck.c (default_conversion): Check targetm.promoted_type.
	* decl.c (grokdeclarator): Check targetm.invalid_return_type.
	(grokparms): Check targetm.invalid_parameter_type.
	* cvt.c (ocp_convert): Check targetm.convert_to_type.
	(build_expr_type_conversion): Check targetm.promoted_type.

""",
u"""

	* include/tr1_impl/functional (function): Use explicit operator bool.
	* include/bits/shared_ptr.h (__shared_ptr): Same.
	* include/bits/unique_ptr.h (unique_ptr): Same.
	* include/std/mutex (unique_lock): Same.
	* include/std/system_error (error_code): Same.
	(error_condition): Same.
	* include/std/ostream (sentry): Same.
	* include/std/istream (sentry): Same.
	* testsuite/19_diagnostics/error_condition/operators/bool.cc: Adjust.
	* testsuite/19_diagnostics/error_condition/operators/bool_neg.cc: Same.
	* testsuite/19_diagnostics/error_code/operators/bool.cc: Same.
	* testsuite/19_diagnostics/error_code/operators/bool_neg.cc: Same.
	* testsuite/20_util/unique_ptr/modifiers/reset_neg.cc: Same.
	* testsuite/20_util/unique_ptr/assign/assign_neg.cc: Same.
	* testsuite/20_util/shared_ptr/observers/bool_conv.cc: Same.


""",
u"""
Daily bump.
""",
u"""
	* config/mips/mips.md (*extenddi_truncate<mode>,
	*extendsi_truncate<mode>): Emit exts if supported.  Add attribute
	defintions.
	(*extendhi_truncateqi): New define_insn_and_sptit.

testsuite/
	* gcc.target/mips/octeon-exts-6.c: New test.
	* gcc.target/mips/extend-1.c: New test.
	* gcc.target/mips/octeon-exts-2.c: Adjust to not match sign-extension
	EXTS.
	* gcc.target/mips/octeon-exts-5.c: Likewise.

""",
u"""
	PR middle-end/40204
	* fold-const.c (fold_binary) <case BIT_AND_EXPR>: Avoid infinite
	recursion if build_int_cst_type returns the same INTEGER_CST as
	arg1.

	* gcc.c-torture/compile/pr40204.c: New test.

""",
u"""
	PR libgomp/40174
	* team.c (gomp_thread_start): Destroy thr->release semaphore.
	(gomp_free_pool_helper): Likewise.

""",
u"""
Fix formatting
""",
u"""
	* fold-const.c (build_fold_addr_expr_with_type): Take the address of
	the operand of VIEW_CONVERT_EXPR.

""",
u"""

	* config/i386/driver-i386.c (host_detect_local_cpu): Check
	extended family and model for Intel processors.  Support Intel
	Atom.

""",
u"""
	* gstab.h (stab_code_type): Define, to be used instead of the
	__stab_debug_code enum, made anonymous.  Add 2009 to the copyright
	notice.
	* dbxout.c (STAB_CODE_TYPE): Remove #define and replace use
	occurrences by stab_code_type.
	* mips-tfile.c (STAB_CODE_TYPE): Remove #define, unused.


""",
u"""

	* tree-flow.h (insert_edge_copies_seq): Undeclare.
	(sra_insert_before): Likewise.
	(sra_insert_after): Likewise.
	(sra_init_cache): Likewise.
	(sra_type_can_be_decomposed_p): Likewise.
	* tree-mudflap.c (insert_edge_copies_seq): Copied here from tree-sra.c
	* tree-sra.c (sra_type_can_be_decomposed_p): Made static.
	(sra_insert_before): Likewise.
	(sra_insert_after): Likewise.
	(sra_init_cache): Likewise.
	(insert_edge_copies_seq): Made static and moved upwards.

	* tree-complex.c (extract_component): Added VIEW_CONVERT_EXPR switch
	case.

	* tree-flow-inline.h (contains_view_convert_expr_p): New function.

	* ipa-prop.c (get_ssa_def_if_simple_copy): New function.
	(determine_cst_member_ptr): Call get_ssa_def_if_simple_copy to skip
	simple copies.



""",
u"""
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Record_Subtype>: When
	discriminants affect the shape of the subtype, retrieve the GCC type
	directly from the original field if the GNAT types for the field and
	the original field are the same.

""",
u"""

	* expr.c (expand_expr_real_1): Avoid calling do_store_flag
	with mismatched comparison modes.

	* gcc.c-torture/compile/20090518-1.c: New testcase.

""",
u"""
Fix Thumb2 bic orn

    
	* config/arm/arm.md (*arm_iorsi3): Refactored for only ARM.
        (peephole ior (reg, int) -> mov, ior): Refactored for only ARM.
        * config/arm/thumb2.md (*thumb_andsi_not_shiftsi_si): Allow bic
        with shifts for Thumb2.
        (orsi_notsi): New for orn.
        (*thumb_orsi_notshiftsi_si): Allow orn with shifts.
        (*thumb2_iorsi3): Rewrite support for iorsi for Thumb2.
        * config/arm/arm.c (const_ok_for_op): Split case for IOR for
        Thumb2.
        (arm_gen_constant): Set can_invert for IOR and Thumb2, Add
        comments. Don't invert remainder for IOR.

""",
u"""

	* testsuite/23_containers/list/14340.cc: Abstract list type.
	* testsuite/23_containers/list/init-list.cc: Same.
	* testsuite/23_containers/list/pthread5.cc: Same.
	* testsuite/23_containers/list/invalidation/1.cc: Same.
	* testsuite/23_containers/list/invalidation/2.cc: Same.
	* testsuite/23_containers/list/invalidation/3.cc: Same.
	* testsuite/23_containers/list/invalidation/4.cc: Same.
	* testsuite/23_containers/list/modifiers/insert/25288.cc: Same.
	* testsuite/23_containers/list/modifiers/1.cc: Same.
	* testsuite/23_containers/list/modifiers/2.cc: Same.
	* testsuite/23_containers/list/modifiers/3.cc: Same.
	* testsuite/23_containers/list/modifiers/swap/1.cc: Same.
	* testsuite/23_containers/list/modifiers/swap/2.cc: Same.
	* testsuite/23_containers/list/modifiers/swap/3.cc: Same.
	* testsuite/23_containers/list/cons/1.cc: Same.
	* testsuite/23_containers/list/cons/2.cc: Same.
	* testsuite/23_containers/list/cons/3.cc: Same.
	* testsuite/23_containers/list/cons/4.cc: Same.
	* testsuite/23_containers/list/cons/5.cc: Same.
	* testsuite/23_containers/list/cons/6.cc: Same.
	* testsuite/23_containers/list/cons/7.cc: Same.
	* testsuite/23_containers/list/cons/clear_allocator.cc: Same.
	* testsuite/23_containers/list/cons/8.cc: Same.
	* testsuite/23_containers/list/cons/9.cc: Same.
	* testsuite/23_containers/list/operations/1.cc: Same.
	* testsuite/23_containers/list/operations/2.cc: Same.
	* testsuite/23_containers/list/operations/3.cc: Same.
	* testsuite/23_containers/list/operations/4.cc: Same.
	* testsuite/23_containers/list/operations/5.cc: Same.
	* testsuite/23_containers/list/requirements/citerators.cc: Same.
	* testsuite/23_containers/list/requirements/dr438/assign_neg.cc: Same.
	* testsuite/23_containers/list/requirements/dr438/insert_neg.cc: Same.
	* testsuite/23_containers/list/requirements/dr438/
	constructor_1_neg.cc: Same.
	* testsuite/23_containers/list/requirements/dr438/
	constructor_2_neg.cc: Same.
	* testsuite/23_containers/list/requirements/dr438/constructor.cc: Same.
	* testsuite/23_containers/list/requirements/
	partial_specialization/1.cc: Same.
	* testsuite/23_containers/list/23781.cc: Same.
	* testsuite/23_containers/list/pthread1.cc: Same.
	* testsuite/23_containers/list/capacity/1.cc: Same.
	* testsuite/23_containers/list/capacity/29134.cc: Same.
	* testsuite/23_containers/list/check_construct_destroy.cc: Same.
	* testsuite/23_containers/list/moveable.cc: Same.

	* testsuite/util/common_type/assoc/common_type.hpp: Re-break lines.


""",
u"""
	PR tree-optimization/40087
	* tree-ssa-loop-niter.c (number_of_iterations_ne_max,
	number_of_iterations_ne): Rename never_infinite argument.
	(number_of_iterations_lt_to_ne, number_of_iterations_lt,
	number_of_iterations_le): Handle pointer-type ivs when
	exit_must_be_taken is false.
	(number_of_iterations_cond):  Do not always assume that
	exit_must_be_taken if the control variable is a pointer.

	* gcc.dg/tree-ssa/pr40087.c: New test.


""",
u"""
Daily bump.
""",
u"""

	PR libfortran/37754
	* io/write_float.def: Simplify format calculation.

""",
u"""

        * c-typeck.c (build_binary_op): Allow % on integal vectors.
        * doc/extend.texi (Vector Extension): Document that % is allowed too.


        * typeck.c (build_binary_op): Allow % on integal vectors.


        * gcc.dg/vector-4.c: New testcase.
        * gcc.dg/simd-1b.c: % is now allowed for integer vectors.
        * g++.dg/ext/vector16.C: New testcase.



""",
u"""

	PR c/40172
	* gcc.dg/pr40172.c: Renamed to ...
	* gcc.dg/pr40172-1.c: This.

	* gcc.dg/pr40172-2.c: New.
	* gcc.dg/pr40172-3.c: Likewise.

""",
u"""

	* config/i386/i386.c (ix86_avoid_jump_mispredicts): Check
	ASM_OUTPUT_MAX_SKIP_PAD instead of ASM_OUTPUT_MAX_SKIP_ALIGN.

""",
u"""

	PR c/40172
gcc/
	* c.opt (Wlogical-op): Disabled by default.
	* c-opt (c_common_post_options): Do not enable Wlogical-op with
	Wextra.
	* doc/invoke.texi (Wlogical-op): Likewise.
testsuite/
	* gcc.dg/pr40172.c: Add -Wlogical-op to dg-options.

""",
u"""
	* tree-scalar-evolution.c (follow_ssa_edge_expr) <NOP_EXPR>: Turn
	into CASE_CONVERT.
	<PLUS_EXPR>: Strip useless type conversions instead of type nops.
	Propagate the type of the first operand.
	<ASSERT_EXPR>: Simplify.
	(follow_ssa_edge_in_rhs): Use gimple_expr_type to get the type.
	Rewrite using the RHS code as discriminant.
	<NOP_EXPR>: Turn into CASE_CONVERT.
	<PLUS_EXPR>: Propagate the type of the first operand.

""",
u"""

	PR libstdc++/40184
	* include/bits/locale_classes.h (locale::facet::_S_lc_ctype_c_locale):
	Declare...
	* config/locale/gnu/c_locale.cc: ... and define.
	* config/locale/generic/c_locale.cc: Define.
	* src/localename.cc (locale::_Impl::_Impl(const char*, size_t)):
	Use it.
	* testsuite/22_locale/locale/cons/40184.cc: New.

""",
u"""
	* config/ia64/ia64-protos.h (ia64_dconst_0_5): New.
	(ia64_dconst_0_375): New.
	* config/ia64/ia64.c (ia64_override_options): Remove
	-minline-sqrt-min-latency warning.
	(ia64_dconst_0_5_rtx, ia64_dconst_0_5): New.
	(ia64_dconst_0_375_rtx, ia64_dconst_0_375): New
	* config/ia64/ia64.md (*sqrt_approx): Remove.
	(sqrtsf2): Remove #if 0.
	(sqrtsf2_internal_thr): Rewrite and move to div.md.
	(sqrtdf): Remove assert.
	(sqrtdf2_internal_thr): Rewrite and move to div.md.
	(sqrtxf2): Remove #if 0.
	(sqrtxf2_internal_thr): Rewrite and move to div.md.
	* div.md (sqrt_approx_rf): New.
	(sqrtsf2_internal_thr): New implementation.
	(sqrtsf2_internal_lat): New.
	(sqrtdf2_internal_thr: New implementation.
	(sqrtxf2_internal): New implementation.

""",
u"""
	* defaults.h (UINT_FAST64_TYPE, INTPTR_TYPE, UINTPTR_TYPE)
	(WCHAR_TYPE, MODIFIED_WCHAR_TYPE, PTRDIFF_TYPE, WINT_TYPE)
	(INTMAX_TYPE, UINTMAX_TYPE, SIG_ATOMIC_TYPE, INT8_TYPE, INT16_TYPE)
	(INT32_TYPE, INT64_TYPE, UINT8_TYPE, UINT16_TYPE, UINT32_TYPE)
	(UINT64_TYPE, INT_LEAST8_TYPE, INT_LEAST16_TYPE, INT_LEAST32_TYPE)
	(INT_LEAST64_TYPE, UINT_LEAST8_TYPE, UINT_LEAST16_TYPE)
	(UINT_LEAST32_TYPE, UINT_LEAST64_TYPE, INT_FAST8_TYPE)
	(INT_FAST16_TYPE, INT_FAST32_TYPE, INT_FAST64_TYPE)
	(UINT_FAST8_TYPE, UINT_FAST16_TYPE, UINT_FAST32_TYPE)
	(SIZE_TYPE, PID_TYPE, CHAR16_TYPE, CHAR32_TYPE): Move defaults here...
	* c-common.c: ...from here.

""",
u"""
Replace spaces with tab.

""",
u"""

	* c-common.c (warn_logical_operator): Remove unnecessary
	conditionals.

""",
u"""
	* builtins.c (do_mpc_arg1): Separate MPFR/MPC C rounding types.


""",
u"""
	* unwind-dw2-fde.c (fde_unencoded_compare): Replace type punning
	assignments with memcpy calls.
	(add_fdes): Likewise.
	(binary_search_unencoded_fdes): Likewise.
	(linear_search_fdes): Eliminate type puns.

""",
u"""

	* tree-ssa-forwprop.c (forward_propagate_addr_expr_1): Do
	not falsely claim to have propagated into all uses.

	* gcc.c-torture/compile/20090519-1.c: New testcase.

""",
u"""
	* cp-demangle.c (cplus_demangle_fill_ctor): Fix logic bug.
	(cplus_demangle_fill_dtor): Likewise.

""",
u"""
PR other/40159
* Makefile.tpl (all): Don't assume gcc-bootstrap and
gcc-no-bootstrap are mutually exclusive.
* Makefile.in: Rebuilt.

""",
u"""
Daily bump.
""",
u"""
PR other/40159
* Makefile.tpl (all): Don't end with unconditional success.
* Makefile.in: Rebuilt.

""",
u"""
	* doc/invoke.texi (C Dialect Options): Update OpenMP specification
	version to v3.0.

""",
u"""

	PR libstdc++/40192
	* include/bits/stl_construct.h (struct _Destroy_aux): Add.
	(_Destroy(_ForwardIterator, _ForwardIterator)): Use the latter.
	* testsuite/23_containers/vector/40192.cc: New.


""",
u"""
	* config/sh/sh-protos.h (sh_legitimate_address_p): Remove.
	* config/sh/sh.c (sh_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.
	* config/sh/sh.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/sh/sh.md: Clean up references to GO_IF_LEGITIMATE_ADDRESS.


""",
u"""

	* include/bits/stl_pair.h (swap): Do not swap rvalues.
	* include/bits/stl_deque.h (swap): Likewise.
	* include/bits/stl_list.h (swap): Likewise.
	* include/bits/stl_vector.h (swap): Likewise.
	* include/bits/stl_bvector.h (swap): Likewise.
	* include/bits/stl_queue.h (swap): Likewise.
	* include/bits/stl_stack.h (swap): Likewise.
	* include/bits/stl_tree.h (swap): Likewise.
	* include/bits/stl_map.h (swap): Likewise.
	* include/bits/stl_multimap.h (swap): Likewise.
	* include/bits/stl_set.h (swap): Likewise.
	* include/bits/stl_multiset.h (swap): Likewise.
	* include/bits/forward_list.h (swap): Likewise.
	* include/bits/unique_ptr.h (swap): Likewise.
	* include/debug/deque (swap): Likewise.
	* include/debug/list (swap): Likewise.
	* include/debug/vector (swap): Likewise.
	* include/debug/map.h (swap): Likewise.
	* include/debug/multimap.h (swap): Likewise.
	* include/debug/set.h (swap): Likewise.
	* include/debug/multiset.h (swap): Likewise.
	* include/debug/unordered_map (swap): Likewise.
	* include/debug/unordered_set (swap): Likewise.
	* include/ext/vstring.h (swap): Likewise.
	* include/tr1_impl/unordered_map (swap): Likewise.
	* include/tr1_impl/hashtable (swap): Likewise.
	* include/tr1_impl/unordered_set (swap): Likewise.
	* include/std/tuple (swap): Likewise.
	* include/std/mutex (swap): Likewise.
	* include/std/thread (swap): Likewise.
	(operator<<): Only output to lvalue streams.
	* testsuite/20_util/shared_ptr/modifiers/swap_rvalue.cc: Remove.
	* testsuite/23_containers/headers/forward_list/synopsis.cc: Adjust.
	* testsuite/23_containers/deque/requirements/dr438/
	assign_neg.cc: Adjust line numbers.
	* testsuite/23_containers/deque/requirements/dr438/
	constructor_1_neg.cc: Likewise.
	* testsuite/23_containers/deque/requirements/dr438/
	constructor_2_neg.cc: Likewise.
	* testsuite/23_containers/deque/requirements/dr438/
	insert_neg.cc: Likewise.
	* testsuite/23_containers/list/requirements/dr438/
	assign_neg.cc: Likewise.
	* testsuite/23_containers/list/requirements/dr438/
	constructor_1_neg.cc: Likewise.
	* testsuite/23_containers/list/requirements/dr438/
	constructor_2_neg.cc: Likewise.
	* testsuite/23_containers/list/requirements/dr438/
	insert_neg.cc: Likewise.
	* testsuite/23_containers/vector/requirements/dr438/
	assign_neg.cc: Likewise.
	* testsuite/23_containers/vector/requirements/dr438/
	constructor_1_neg.cc: Likewise.
	* testsuite/23_containers/vector/requirements/dr438/
	constructor_2_neg.cc: Likewise.
	* testsuite/23_containers/vector/requirements/dr438/
	insert_neg.cc: Likewise.
	* testsuite/30_threads/thread/swap/1.cc: Swap with lvalue and also
	test non-member swap.
	* testsuite/30_threads/thread/swap/2.cc: Remove.

""",
u"""
	Implement explicit conversions ops as specified in N2437.
	* decl.c (grokdeclarator): Handle explicit conversion ops.
	(check_initializer): Pass flags to store_init_value.
	* decl2.c (maybe_emit_vtables): Likewise.
	* init.c (expand_aggr_init_1): Likewise.
	* call.c (convert_class_to_reference): Take flags parm,
	check DECL_NONCONVERTING_P.
	(build_user_type_conversion_1): Check DECL_NONCONVERTING_P.
	(add_builtin_candidates): Simplify getting type of conversion.
	(build_object_call): Likewise.  Check DECL_NONCONVERTING_P.
	(implicit_conversion): Pass through LOOKUP_ONLYCONVERTING.
	(reference_binding): Take flags parm.  Direct-initialize copy parm.
	(add_function_candidate): Direct-initialize the copy parm.
	(add_conv_candidate): Use LOOKUP_IMPLICIT, not LOOKUP_NORMAL.
	(build_builtin_candidate): Add LOOKUP_ONLYCONVERTING.
	(conditional_conversion): Likewise.
	(convert_like_real): Only complain about DECL_NONCONVERTING_P
	constructors.
	(perform_implicit_conversion_flags): Add flags parm to
	perform_implicit_conversion.  Improve diagnostics.
	* cp-tree.h (LOOKUP_IMPLICIT): New macro.
	(LOOKUP_COPY_PARM): New bit macro.
	* cvt.c (build_expr_type_conversion): Check DECL_NONCONVERTING_P.
	* typeck.c (convert_for_assignment): Take flags parm, pass it to
	perform_implicit_conversion_flags.
	(cp_build_modify_expr): Pass flags to convert_for_assignment.
	(convert_for_initialization): Likewise.
	* typeck2.c (store_init_value): Take flags parm, pass to
	digest_init_flags.
	(digest_init_flags): Add flags parm to digest_init.
	(digest_init_r): Take flags parm, pass to convert_for_initialization.
	(process_init_constructor_array): Pass it.
	(process_init_constructor_record): Likewise.
	(process_init_constructor_union): Likewise.
""",
u"""
Fix for PR debug/40109

gcc/ChangeLog:
PR debug/40109
* dwarf2out.c (gen_type_die_with_usage): Generate the DIE as a
child of the containing namespace's DIE.

gcc/testsuite/ChangeLog:
PR debug/40109
* g++.dg/debug/dwarf2/nested-1.C: New test.


""",
u"""
	* config/mips/mips.md (*zero_extend<GPR:mode>_trunc<SHORT:mode>,
	*zero_extendhi_truncqi):  Move after the zero_extend patterns.
	(*extenddi_truncate<mode>, *extendsi_truncate<mode>): Move after the
	extend patterns.

""",
u"""

	PR target/39942
	* config/i386/i386.c (ix86_avoid_jump_misspredicts): Replace
	gen_align with gen_pad.
	(ix86_reorg): Check ASM_OUTPUT_MAX_SKIP_PAD instead of
	#ifdef ASM_OUTPUT_MAX_SKIP_ALIGN.

	* config/i386/i386.h (ASM_OUTPUT_MAX_SKIP_PAD): New.
	* config/i386/x86-64.h (ASM_OUTPUT_MAX_SKIP_PAD): Likewise.

	* config/i386/i386.md (align): Renamed to ...
	(pad): This.  Replace ASM_OUTPUT_MAX_SKIP_ALIGN with
	ASM_OUTPUT_MAX_SKIP_PAD.

""",
u"""

	PR testsuite/39907
	* gcc.target/x86_64/abi/asm-support.S (snapshot_ret): Preserve
	stack alignment.

""",
u"""
* config.gcc: Fix variable syntax.

""",
u"""
* config.gcc: Fix variable syntax.

""",
u"""
PR target/39531
* config/m68k/m68k.c (output_andsi3): Mask off sign bit copies
before calling exact_log2.
(output_iorsi3): Likewise.
(output_xorsi3): Likewise.

""",
u"""

	PR fortran/40164
	* primary.c (gfc_match_rvalue): Handle procedure pointer components in
	arrays.
	* resolve.c (resolve_ppc_call,resolve_expr_ppc): Resolve component and
	array references.
	(resolve_fl_derived): Procedure pointer components are not required to
	have constant array bounds in their return value.



	PR fortran/40164
	* gfortran.dg/proc_ptr_comp_8.f90: New.


""",
u"""

	* intrinsic.c (add_sym): Fix my last commit (r147655),
	which broke bootstrap.


""",
u"""
	* config/sh/sh.c (expand_cbranchdi4): Use a scratch register
	for the none zero constant operand except for EQ and NE
	comprisons even when the first operand is R0.


""",
u"""

	* config/s390/2064.md: Remove trailing whitespaces.
	* config/s390/2084.md: Likewise.
	* config/s390/constraints.md: Likewise.
	* config/s390/fixdfdi.h: Likewise.
	* config/s390/libgcc-glibc.ver: Likewise.
	* config/s390/s390-modes.def: Likewise.
	* config/s390/s390-protos.h: Likewise.
	* config/s390/s390.c: Likewise.
	* config/s390/s390.h: Likewise.
	* config/s390/s390.md: Likewise.
	* config/s390/tpf-unwind.h: Likewise.


""",
u"""

	PR fortran/40168
	* trans-expr.c (gfc_trans_zero_assign): For local array
	destinations use an assignment from an empty constructor.

	* gfortran.dg/array_memset_2.f90: Adjust.

""",
u"""
	* config/m68k/m68k.c (m68k_legitimize_address): Fix typo in signature.

""",
u"""

	PR fortran/36947
	PR fortran/40039
	* expr.c (gfc_check_pointer_assign): Check intents when comparing
	interfaces.
	* gfortran.h (typedef struct gfc_intrinsic_arg): Add 'intent' member.
	(gfc_compare_interfaces): Additional argument.
	* interface.c (operator_correspondence): Add check for equality of
	intents, and new argument 'intent_check'.
	(gfc_compare_interfaces): New argument 'intent_check', which is passed
	on to operator_correspondence.
	(check_interface1): Don't check intents when comparing interfaces.
	(compare_parameter): Do check intents when comparing interfaces.
	* intrinsic.c (add_sym): Add intents for arguments of intrinsic
	procedures.
	(add_sym_1,add_sym_1s,add_sym_1m,add_sym_2,add_sym_2s,add_sym_3,
	add_sym_3ml,add_sym_3red,add_sym_3s,add_sym_4): Use INTENT_IN by
	default.
	(add_sym_1_intent,add_sym_1s_intent,add_sym_2s_intent,add_sym_3s_intent)
	: New functions to add intrinsic symbols, specifying custom intents.
	(add_sym_4s,add_sym_5s): Add new arguments to specify intents.
	(add_functions,add_subroutines): Add intents for various intrinsics.
	* resolve.c (check_generic_tbp_ambiguity): Don't check intents when
	comparing interfaces.
	* symbol.c (gfc_copy_formal_args_intr): Copy intent.



	PR fortran/36947
	PR fortran/40039
	* gfortran.dg/interface_27.f90: New.
	* gfortran.dg/interface_28.f90: New.
	* gfortran.dg/proc_ptr_11.f90: Fixing invalid test case.
	* gfortran.dg/proc_ptr_result_1.f90: Ditto.


""",
u"""
	M68K TLS support.
	* configure.ac (m68k-*-*): Check if binutils support TLS.
	* configure: Regenerate.
	* config/m68k/predicates.md (symbolic_operand): Extend comment.
	* config/m68k/constraints.md (Cu): New constraint.
	* config/m68k/m68k.md (UNSPEC_GOTOFF): Remove.
	(UNSPEC_RELOC16, UNSPEC_RELOC32): New constants.
	(movsi): Handle TLS symbols.
	(addsi3_5200): Handle XTLS symbols, indent.
	* config/m68k/m68k-protos.h (m68k_legitimize_tls_address): Declare.
	(m68k_tls_reference_p): Declare.
	(m68k_legitimize_address): Declare.
	(m68k_unwrap_symbol): Declare.
	* config/m68k/m68k.opt (mxtls): New option.
	* config/m68k/m68k.c (ggc.h): Include.
	(m68k_output_dwarf_dtprel): Implement hook.
	(TARGET_HAVE_TLS, TARGET_ASM_OUTPUT_DWARF_DTPREL): Define.
	(m68k_expand_prologue): Load GOT pointer when function needs it.
	(m68k_illegitimate_symbolic_constant_p): Handle TLS symbols.
	(m68k_legitimate_constant_address_p): Same.
	(m68k_decompose_address): Handle TLS references.
	(m68k_get_gp): New static function.
	(enum m68k_reloc): New contants.
	(TLS_RELOC_P): New macro.
	(m68k_wrap_symbol): New static function.
	(m68k_unwrap_symbol): New function.
	(m68k_final_prescan_insn_1): New static function.
	(m68k_final_prescan_insn): New function.
	(m68k_move_to_reg, m68k_wrap_symbol_into_got_ref): New static
	functions.
	(legitimize_pic_address): Handle TLS references..
	(m68k_tls_get_addr, m68k_get_tls_get_addr)
	(m68k_libcall_value_in_a0_p)
	(m68k_call_tls_get_addr, m68k_read_tp, m68k_get_m68k_read_tp)
	(m68k_call_m68k_read_tp): Helper variables and functions for ...
	(m68k_legitimize_tls_address): Handle TLS references.
	(m68k_tls_symbol_p, m68k_tls_reference_p_1, m68k_tls_reference_p):
	New functions.
	(m68k_legitimize_address): Handle TLS symbols.
	(m68k_get_reloc_decoration): New static function.
	(m68k_output_addr_const_extra): Handle UNSPEC_RELOC16 and
	UNSPEC_RELOC32.
	(m68k_output_dwarf_dtprel): Implement hook.
	(print_operand_address): Handle UNSPEC_RELOC16 adn UNSPEC_RELOC32.
	(m68k_libcall_value): Return result in A0 instead of D0 when asked by
	m68k_call_* routines.
	(sched_attr_op_type): Handle TLS symbols.
	(gt-m68k.h): Include.
	* config/m68k/m68k.h (FINAL_PRESCAN_INSN): Define.
	(LEGITIMATE_PIC_OPERAND_P): Support TLS.

	* gcc.target/m68k/tls-ie.c: New test.
	* gcc.target/m68k/tls-le.c: New test.
	* gcc.target/m68k/tls-gd.c: New test.
	* gcc.target/m68k/tls-ld.c: New test.
	* gcc.target/m68k/tls-ie-xgot.c: New test.
	* gcc.target/m68k/tls-le-xtls.c: New test.
	* gcc.target/m68k/tls-gd-xgot.c: New test.
	* gcc.target/m68k/tls-ld-xgot.c: New test.
	* gcc.target/m68k/tls-ld-xtls.c: New test.
	* gcc.target/m68k/tls-ld-xgot-xtls.c: New test.

""",
u"""
	PR ada/40166
	* Makefile.in (TOOLS_TARGET_PAIRS): Use the correct path to the
	target specific sources.

""",
u"""
Daily bump.
""",
u"""

	* ipa-prop.c (ipa_check_stmt_modifications): Removed.
	(visit_store_addr_for_mod_analysis): New function.
	(ipa_detect_param_modifications): Use walk_stmt_load_store_addr_ops.
	(determine_cst_member_ptr): Use gimple_assign_single_p.
	(ipa_get_stmt_member_ptr_load_param): Use gimple_assign_single_p.
	(ipa_analyze_call_uses): Use !gimple_assign_rhs2 rather than number of
	operands.  Don't check number of operands of a NOP_EXPR.

	* testsuite/gcc.dg/ipa/modif-1.c: Do not check for unmodified int
	parameter.


""",
u"""
	* doc/tree-ssa.texi (SSA Operands): Fix a mistake.

""",
u"""

	* win32_threads.c (GC_get_thread_stack_base):  Implement for Cygwin.


""",
u"""
gcc/


	PR c/40172
	* c-common.c (warn_logical_operator): Don't warn if one of
	expression isn't always true or false.

gcc/testscase/


	PR c/40172
	* gcc.dg/pr40172.c: New.

""",
u"""
	PR c++/40139
	* pt.c (tsubst_qualified_id): Retain the type if we aren't dealing
	with a dependent type.  Actually look up the destructor.
	* semantics.c (finish_id_expression): Fix logic.
	(finish_qualified_id_expr): Don't try to use 'this' if we aren't in
	a function.
	* typeck.c (build_x_unary_op): Diagnose taking the address of a
	constructor or destructor.
	* tree.c (get_first_fn): Handle OFFSET_REF.
""",
u"""
cp:
	* tree.c (cxx_printable_name_internal): Allow consecutive
	translated and untranslated cached copies of the name of the
	current function.

testsuite:
	* g++.dg/warn/translate-ice-1.C: New test.

""",
u"""
	* iso-fortran-env.def: Define INT8, INT16, INT32, INT64, REAL32,
	REAL64 and REAL128.
	* gfortran.h (gfc_get_int_kind_from_width_isofortranenv,
	gfc_get_real_kind_from_width_isofortranenv): New prototypes.
	* iso-c-binding.def: Update definitions for the INT*_T,
	INT_LEAST*_T and INT_FAST*_T named parameters.
	* trans-types.c (get_typenode_from_name, get_int_kind_from_name,
	gfc_get_real_kind_from_width_isofortranenv): New functions.

	* gfortran.dg/c_kind_int128_test1.f03: Also test C_INT_FAST128_T.
	* gfortran.dg/c_kind_int128_test2.f03: Update comment.
	* gfortran.dg/c_kind_params.f90: Also test int_fast*_t.
	* gfortran.dg/c_kinds.c: Add int_fast*_t arguments.

""",
u"""
	libiberty/
	* pex-win32.c (pex_win32_exec_child): Fix logic to avoid closing
	standard handles (stdin, stdout, stderr) in parent.


""",
u"""
	PR fortran/36260

	* intrinsic.c (add_functions, add_subroutines): Fix argument
	names and wrap long lines.
	* intrinsic.texi: Fix documentation and argument names of
	LOG_GAMMA, DATAN2, DBESJN, DTIME, ETIME, FSTAT, STAT, LSTAT,
	GET_COMMAND, IDATE, LTIME, MOVE_ALLOC, NINT, OR, PRODUCT,
	SUM, RAND, RANDOM_SEED, REAL, SELECTED_INT_KIND,
	SELECTED_REAL_KIND and XOR.

""",
u"""

       * config/i386/biarch32.h: New file.
       * config.gcc: Add for target i386-w64-* the biarch32.h to tm_file.


""",
u"""
	* config/mips/mips.md (*zero_extend<mode>_trunchi,
	*zero_extend<mode>_truncqi): Merge these into ...
	(*zero_extend<GPR:mode>_trunc<SHORT:mode>): ... this new pattern.
	Name the pattern following this as *zero_extendhi_truncqi.

""",
u"""
Daily bump.
""",
u"""

	PR middle-end/39301
	* hwint.h: Add macro HOST_WIDEST_INT_PRINT.
	* bitmap.c (bitmap_descriptor): Make fields HOST_WIDEST_INT.
	(output_info): Make field HOST_WIDEST_INT.
	(print_statistics): Use HOST_WIDEST_INT_PRINT.
	(dump_bitmat_statistics): Same.

""",
u"""
	* config.gcc (use_gcc_stdint):  Set to wrap.
	* config/darwin.h (SIG_ATOMIC_TYPE, INT8_TYPE, INT16_TYPE,
	INT32_TYPE, INT64_TYPE, UINT8_TYPE, UINT16_TYPE, UINT32_TYPE,
	UINT64_TYPE, INT_LEAST8_TYPE, INT_LEAST16_TYPE, INT_LEAST32_TYPE,
	INT_LEAST64_TYPE, UINT_LEAST8_TYPE, UINT_LEAST16_TYPE,
	UINT_LEAST32_TYPE, UINT_LEAST64_TYPE, INT_FAST8_TYPE,
	INT_FAST16_TYPE, INT_FAST32_TYPE, INT_FAST64_TYPE,
	UINT_FAST8_TYPE, UINT_FAST16_TYPE, UINT_FAST32_TYPE,
	UINT_FAST64_TYPE, INTPTR_TYPE, UINTPTR_TYPE): Define.

""",
u"""
	PR fortran/33197

	* intrinsic.c (add_functions): Use ERFC_SCALED simplification.
	* intrinsic.h (gfc_simplify_erfc_scaled): New prototype.
	* simplify.c (fullprec_erfc_scaled, asympt_erfc_scaled,
	gfc_simplify_erfc_scaled): New functions.

	* gfortran.dg/erf_2.F90: New test.
	* gfortran.dg/erfc_scaled_2.f90: New test.

""",
u"""
	PR fortran/31243

	* resolve.c (resolve_substring): Don't allow too large substring
	indexes.
	(gfc_resolve_substring_charlen): Fix typo.
	(gfc_resolve_character_operator): Fix typo.
	(resolve_charlen): Catch unreasonably large string lengths.
	* simplify.c (gfc_simplify_len): Don't error out on LEN
	range checks.

	* gcc/testsuite/gfortran.dg/string_1.f90: New test.
	* gcc/testsuite/gfortran.dg/string_2.f90: New test.
	* gcc/testsuite/gfortran.dg/string_3.f90: New test.

""",
u"""
	* config.gcc (mips*-*-*): Support arch_32, arch_64, tune_32 and
	tune_64.
	* config/mips/mips.h (MIPS_ABI_DEFAULT, MULTILIB_ABI_DEFAULT):
	Move definitions earlier.
	(OPT_ARCH64, OPT_ARCH32): Define.
	(OPTION_DEFAULT_SPECS): Add entries for arch_32, arch_64, tune_32
	and tune_64.

""",
u"""
	* ChangeLog: Forgotten in previous commit.

""",
u"""
	PR fortran/36031

	* decl.c (set_enum_kind): Use global short-enums flag.
	* gfortran.h (gfc_option_t): Remove short_enums flag.
	* lang.opt (-fshort-enums): Refer to C documentation.
	* options.c (gfc_init_options, gfc_handle_option): Use global
	short-enums flag.

""",
u"""
	PR target/40153
	* arm.md (cstoresi_nltu_thumb1): Use a neg of ltu as the pattern name
	implies.
""",
u"""
	* arm.md (movdi2): Copy non-reg values to DImode registers.
""",
u"""

	* gfortran.dg/default_format_denormal_1.f90: XFAIL on cygwin.
	* gfortran.dg/default_format_1.f90: Revert change of 2009-05-12

Correct accidental commit of wrong file.

""",
u"""

	* include/std/mutex: Move std::lock_error to ...
	* src/compatibility.cc: Here.
	* src/mutex.cc: Likewise.
	* testsuite/30_threads/headers/mutex/types_std_c++0x.cc: Add checks
	for lock types and remove std::lock_error check.

""",
u"""
	PR target/39942
	* final.c (label_to_max_skip): New function.
	(label_to_alignment): Only use LABEL_TO_ALIGNMENT if
	CODE_LABEL_NUMBER <= max_labelno.
	* output.h (label_to_max_skip): New prototype.
	* config/i386/i386.c (ix86_avoid_jump_misspredicts): Renamed to...
	(ix86_avoid_jump_mispredicts): ... this.  Don't define if
	ASM_OUTPUT_MAX_SKIP_ALIGN isn't defined.  Update comment.
	Handle CODE_LABELs with >= 16 byte alignment or with
	max_skip == (1 << align) - 1.
	(ix86_reorg): Don't call ix86_avoid_jump_mispredicts if
	ASM_OUTPUT_MAX_SKIP_ALIGN isn't defined.

""",
u"""
	PR target/39942
	* config/i386/x86-64.h (ASM_OUTPUT_MAX_SKIP_ALIGN): Don't emit second
	.p2align 3 if MAX_SKIP is smaller than 7.
	* config/i386/linux.h (ASM_OUTPUT_MAX_SKIP_ALIGN): Likewise.

""",
u"""
gcc/ChangeLog:
	* alias.c (struct alias_set_entry_d): Rename from struct
	alias_set_entry.  Change all uses.
	* except.c (struct call_site_record_d): Rename from struct
	call_site_record.  Change all uses.
	* except.h (struct eh_region_d): Rename from struct eh_region.
	Change all uses.
	* gcse.c (struct hash_table_d): Rename from struct hash_table.
	Change all uses.
	* graphite.c (struct ivtype_map_elt_d): Rename fromstruct
	ivtype_map_elt.  Change all uses.
	(struct rename_map_elt_d): Rename fromstruct rename_map_elt.
	Change all uses.
	(struct ifsese_d): Rename fromstruct ifsese.  Change all uses.
	* graphite.h (struct name_tree_d): Rename from struct name_tree.
	Change all uses.
	(struct sese_d): Rename from struct sese.  Change all uses.
	* omega.h (struct eqn_d): Rename from struct eqn.  Change all
	uses.
	(struct omega_pb_d): Rename from struct omega_pb.  Change all
	uses.
	* optabs.h (struct optab_d): Rename from struct optab.  Change all
	uses.
	(struct convert_optab_d): Rename from struct convert_optab.
	Change all uses.
	* tree-pass.h (struct ipa_opt_pass_d): Rename fromstruct
	ipa_opt_pass.  Change all uses.
	* tree-predcom.c (struct dref_d): Rename from struct dref.  Change
	all uses.

	* c-decl.c (pushtag): If -Wc++-compat, warn if the tag is already
	defined as a typedef.
	(grokdeclarator): If -Wc++-compat, warn if a typedef is already
	defined as a tag.
gcc/cp/ChangeLog:
	* cp-tree.h (enum cp_lvalue_kind_flags): Rename from
	cp_lvalue_kind.  Change all uses.
	(enum base_access_flags): Rename from enum base_access.  Change
	all uses.
	* parser.c (enum cp_parser_flags): Remove enum tag.
gcc/testsuite/ChangeLog:
	* gcc.dg/Wcxx-compat-10.c: New testcase.
libcpp/ChangeLog:
	* include/cpplib.h (enum cpp_builtin_type): Rename from enum
	builtin_type.  Change all uses.

""",
u"""
Daily bump.
""",
u"""

	* testsuite/21_strings/basic_string/40160.cc: Remove spurious
	double include.

""",
u"""

	PR libstdc++/40160
	* include/debug/formatter.h (_Parameter::_Parameter): Don't use
	typeid when __GXX_RTTI is undefined.
	* src/debug.cc (_Error_formatter::_Parameter::_M_print_field): Adjust
	for null _M_variant._M_iterator._M_type,
	_M_variant._M_iterator._M_seq_type, _M_variant._M_sequence._M_type.
	* testsuite/21_strings/basic_string/40160.cc: New.

""",
u"""

	PR 16302
	* fold-const.c (make_range,build_range_check,merge_ranges): Move
	declaration to...
	(merge_ranges): Returns bool. 
	* tree.h (make_range): .. to here.
	(build_range_check): Likewise.
	(merge_ranges): Likewise. Renamed from merge_ranges.
	* c-typeck.c (parser_build_binary_op): Update calls to
	warn_logical_operator.
	* c-common.c (warn_logical_operator): Add new warning.
	* c-common.h (warn_logical_operator): Update declaration.
cp/
	* call.c (build_new_op): Update calls to warn_logical_operator.
	
testsuite/
	* gcc.dg/pr16302.c: New.
	* g++.dg/warn/pr16302.C: New.

""",
u"""

	* ira-conflicts.c (add_insn_allocno_copies): Fix wrong
	conditional.

""",
u"""
	* gcc.dg/torture/builtin-math-5.c: New.
	* gcc.dg/torture/builtin-math-6.c: New.
	* lib/target-supports.exp (check_effective_target_mpc): New.


""",
u"""
	* doc/install.texi: Document MPC requirements, flags etc.


""",
u"""
	* builtins.c (do_mpc_arg1, fold_builtin_ccos): New.
	(fold_builtin_cexp): Ensure we get a complex REAL_TYPE.
	Evaluate constant arguments.
	(fold_builtin_carg): Ensure we get a complex REAL_TYPE.
	(fold_builtin_1): Likewise, also evaluate constant arguments.
	Remove superfluous break.
	(do_mpc_ckconv): New.
	* real.h: Include mpc.h.
	* toplev.c (print_version): Output MPC version info if available.


""",
u"""

	gcc/
	* fold-const.c (fold_convert_const_real_from_real): Check for
	overflow.

""",
u"""

	* config/i386/i386.c (ix86_reorg): Call optimize_function_for_speed_p
	only once.

""",
u"""

	* doc/invoke.texi (max-early-inliner-iterations): New flag.
	* ipa-inline.c (enum inlining_mode): New INLINE_SIZE_NORECURSIVE.
	(try_inline): Fix return value.
	(cgraph_decide_inlining_incrementally): Honor new value.
	(cgraph_early_inlining): Handle indirect inlining.
	* params.def (PARAM_EARLY_INLINER_MAX_ITERATIONS): New.

	* testsuite/gcc.dg/tree-ssa/inline-3.c: New testcase

""",
u"""


	* cgraph.h (struct cgraph_node): Add finalized_by_frotnend flag.
	* cgraphunit.c (cgraph_finalize_function): Set it.
	(cgraph_expand_function): Use it.

""",
u"""
	* gcc.target/i386/align-main-1.c (check): Mark noinline.
	* gcc.target/i386/align-main-2.c (check): Mark noinline.
	* gcc.dg/ipa/ipa-4.c: Disable early inlining.
	* gcc.dg/vect/vect-iv-10.c (main1): Mark noinline.
	* gcc.dg/vect/costmodel/i386/costmodel-vect-33.c (main1): Mark noinline.
	* gcc.dg/vect/costmodel/x86_64/costmodel-vect-33.c (main1): Mark noinline.
	* gcc.dg/vect/pr31699.c (foo): Mark noinline.
	* gcc.dg/vect/pr18400.c (main1): Mark noinline.

""",
u"""

	* sibcall-6.c: Add no-ipa-cp argument and mark the function to be
	optimized by sibcall noinline.

""",
u"""
	* sibcall-1.c (track): Mark noinline.
	* sibcall-2.c (track): Mark noinline.
	* sibcall-3.c (track): Mark noinline.
	* sibcall-4.c (track): Mark noinline.

""",
u"""
	* flatten-2.c: Disable early inlining; add comment.
	* flatten-3.c: New test based on flatten-2.c.

""",
u"""
	* inclhack.def (glibc_tgmath): Correct bypass.
	* fixincl.x: Regenerate.

""",
u"""

	gcc/
	* real.c (encode_ieee_half): Define.
	(decode_ieee_half): Define.
	(ieee_half_format): Define.
	(arm_half_format): Define.
	* real.h (ieee_half_format): Declare.
	(arm_half_format): Declare.

""",
u"""

	gcc/
	* optabs.c (prepare_float_lib_cmp):  Test that the comparison,
	swapped, and reversed optabs exist before trying to use them.

""",
u"""

	gcc/
	* config/arm/arm.c (neon_vector_mem_operand): Handle element/structure
	loads.  Allow PRE_DEC.
	(output_move_neon): Handle PRE_DEC.
	(arm_print_operand): Add 'A' for neon structure loads.
	* config/arm/arm-protos.h (neon_vector_mem_operand): Update prototype.
	* config/arm/neon.md (neon_mov): Update comment.
	* config/arm/constraints.md (Un, Us): Update neon_vector_mem_operand
	calls.
	(Um): New constraint.

""",
u"""
	Revert the following patch until testsuite fallout is fixed:
	* cgraph.c (dump_cgraph_node): Dump size/time/benefit.
	* cgraph.h (struct inline_summary): New filed self_wize,
	size_inlining_benefit, self_time and time_inlining_benefit.
	(struct cgraph_global_info): Replace insns by time ans size fields.
	* ipa-cp (ipcp_cloning_candidate_p): Base estimate on size
	(ipcp_estimate_growth, ipcp_insert_stage): Likewise.
	(ipcp_update_callgraph): Do not touch function bodies.
	* ipa-inline.c: Include except.h
	MAX_TIME: New constant.
	(overall_insns): Remove
	(overall_size, max_benefit): New static variables.
	(cgraph_estimate_time_after_inlining): New function.
	(cgraph_estimate_size_after_inlining): Rewrite using benefits.
	(cgraph_clone_inlined_nodes): Update size.
	(cgraph_mark_inline_edge): Update size.
	(cgraph_estimate_growth): Use size info.
	(cgraph_check_inline_limits): Check size.
	(cgraph_default_inline_p): Likewise.
	(cgraph_edge_badness): Compute badness based on benefit and size cost.
	(cgraph_decide_recursive_inlining): Check size.
	(cgraph_decide_inlining_of_small_function): Update size; dump sizes and times.
	(cgraph_decide_inlining): Likewise.
	(cgraph_decide_inlining_incrementally): Likewise; honor PARAM_EARLY_INLINING_INSNS.
	(likely_eliminated_by_inlining_p): New predicate.
	(estimate_function_body_sizes): New function.
	(compute_inline_parameters): Use it.
	* except.c (must_not_throw_labels): New function.
	* except.h (must_not_throw_labels): Declare.
	* tree-inline.c (init_inline_once): Kill inlining_weigths
	* tree-ssa-structalias.c: Avoid uninitialized warning.
	* params.def (PARAM_MAX_INLINE_INSNS_SINGLE): Reduce to 300.
	(PARAM_MAX_INLINE_INSNS_AUTO): Reduce to 60.
	(PARAM_INLINE_CALL_COST): Remove.
	(PARAM_EARLY_INLINING_INSNS): New.

""",
u"""

	* tree-ssa-pre.c (eliminate): Use TODO_update_ssa_only_virtuals,
	not TODO_update_ssa.

""",
u"""

	PR tree-optimization/39999
	* gimple.h (gimple_expr_type): Use the expression type looking
	through useless conversions.
	* tree-ssa-sccvn.c (vn_nary_op_lookup_stmt): Use gimple_expr_type.
	(vn_nary_op_insert_stmt): Likewise.
	(simplify_binary_expression): Likewise.

	* gcc.c-torture/compile/pr39999.c: New testcase.

""",
u"""

	* common.opt (-ftree-forwprop, -ftree-phiprop, -ftree-pta):
	New options, enabled by default.
	* doc/invoke.texi (-ftree-forwprop, -ftree-phiprop, -ftree-pta):
	Document.
	* tree-ssa-forwprop.c (gate_forwprop): Use flag_tree_forwprop.
	* tree-ssa-phiprop.c (gate_phiprop): Use flag_tree_phiprop.
	* tree-ssa-structalias.c (gate_tree_pta): New function.
	(pass_build_alias): Use it.

""",
u"""
	* tree-ssa-forwprop.c (forward_propagate_addr_expr_1): Also
	recurse on an invariant address if a conversion from a pointer
	type to a wider integer type is involved.

testsuite:
	* gcc.c-torture/compile/ptr-conv-1.c: New test.

""",
u"""

	* testsuite/26_numerics/random/discrete_distribution/cons/
	num_xbound_fun.cc: Minor tweaks.
	* testsuite/26_numerics/random/piecewise_constant_distribution/
	cons/initlist_fun.cc: Likewise
	* testsuite/26_numerics/random/piecewise_constant_distribution/
	cons/num_xbound_fun.cc: Likewise
	* testsuite/26_numerics/random/piecewise_linear_distribution/
	cons/initlist_fun.cc: Likewise
	* testsuite/26_numerics/random/piecewise_linear_distribution/
	cons/num_xbound_fun.cc: Likewise

""",
u"""
	* cgraph.c (dump_cgraph_node): Dump size/time/benefit.
	* cgraph.h (struct inline_summary): New filed self_wize,
	size_inlining_benefit, self_time and time_inlining_benefit.
	(struct cgraph_global_info): Replace insns by time ans size fields.
	* ipa-cp (ipcp_cloning_candidate_p): Base estimate on size
	(ipcp_estimate_growth, ipcp_insert_stage): Likewise.
	(ipcp_update_callgraph): Do not touch function bodies.
	* ipa-inline.c: Include except.h
	MAX_TIME: New constant.
	(overall_insns): Remove
	(overall_size, max_benefit): New static variables.
	(cgraph_estimate_time_after_inlining): New function.
	(cgraph_estimate_size_after_inlining): Rewrite using benefits.
	(cgraph_clone_inlined_nodes): Update size.
	(cgraph_mark_inline_edge): Update size.
	(cgraph_estimate_growth): Use size info.
	(cgraph_check_inline_limits): Check size.
	(cgraph_default_inline_p): Likewise.
	(cgraph_edge_badness): Compute badness based on benefit and size cost.
	(cgraph_decide_recursive_inlining): Check size.
	(cgraph_decide_inlining_of_small_function): Update size; dump sizes and times.
	(cgraph_decide_inlining): Likewise.
	(cgraph_decide_inlining_incrementally): Likewise; honor PARAM_EARLY_INLINING_INSNS.
	(likely_eliminated_by_inlining_p): New predicate.
	(estimate_function_body_sizes): New function.
	(compute_inline_parameters): Use it.
	* except.c (must_not_throw_labels): New function.
	* except.h (must_not_throw_labels): Declare.
	* tree-inline.c (init_inline_once): Kill inlining_weigths
	* tree-ssa-structalias.c: Avoid uninitialized warning.
	* params.def (PARAM_MAX_INLINE_INSNS_SINGLE): Reduce to 300.
	(PARAM_MAX_INLINE_INSNS_AUTO): Reduce to 60.
	(PARAM_INLINE_CALL_COST): Remove.
	(PARAM_EARLY_INLINING_INSNS): New.
	doc/invoke.texi (max-inline-insns-auto, early-inlining-insns): Update.
	(inline-call-cost): Remove.
	(early-inlining-insns): New.

""",
u"""

	PR libstdc++/36211
	* testsuite/lib/libstdc++.exp(v3_target_compile):  Add
	cxxldflags to additional_flags rather than cxx_final.

""",
u"""

	* testsuite/26_numerics/random/discrete_distribution/cons/num_xbound_fun.cc:
	Replace non-standard macro M_PI with constant pi.
	* testsuite/26_numerics/random/piecewise_constant_distribution/cons/initlist_fun.cc:
	Likewise
	* testsuite/26_numerics/random/piecewise_constant_distribution/cons/num_xbound_fun.cc:
	Likewise
	* testsuite/26_numerics/random/piecewise_linear_distribution/cons/initlist_fun.cc:
	Likewise
	* testsuite/26_numerics/random/piecewise_linear_distribution/cons/num_xbound_fun.cc:
	Likewise 

""",
u"""
	* dbxout.c (dbxout_range_type): Add LOW and HIGH parameters.  Use them
	for bounds.
	(print_int_cst_bounds_in_octal_p): Likewise.
	(dbxout_type): Adjust calls to above functions.  Be prepared to deal
	with subtypes.
	* dwarf2out.c (base_type_die): Likewise.
	(is_subrange_type): Delete.
	(subrange_type_die): Add LOW and HIGH parameters.  Use them for bounds.
	(modified_type_die): Call subrange_type_for_debug_p on subtypes.
	* fold-const.c (fold_truth_not_expr) <CONVERT_EXPR>: Do not strip it if
	the destination type is boolean.
	(build_range_check): Do not special-case subtypes.
	(fold_sign_changed_comparison): Likewise.
	(fold_unary): Likewise.
	* langhooks-def.h (LANG_HOOKS_GET_SUBRANGE_BOUNDS): Define.
	(LANG_HOOKS_FOR_TYPES_INITIALIZER): Add LANG_HOOKS_GET_SUBRANGE_BOUNDS.
	* langhooks.h (lang_hooks_for_types): Add get_subrange_bounds.
	* tree.c (subrange_type_for_debug_p): New predicate based on the former
	is_subrange_type.
	* tree.h (subrange_type_for_debug_p): Declare.
	* tree-chrec.c (avoid_arithmetics_in_type_p): Delete.
	(convert_affine_scev): Remove call to above function.
	(chrec_convert_aggressive): Likewise.
	* tree-ssa.c (useless_type_conversion_p_1): Do not specifically return
	false for conversions involving subtypes.
	* tree-vrp.c (vrp_val_max): Do not special-case subtypes.
	(vrp_val_min): Likewise.
	(needs_overflow_infinity): Likewise.
	(extract_range_from_unary_expr): Likewise.
ada/
	* gcc-interface/ada-tree.h (TYPE_GCC_MIN_VALUE, TYPE_GCC_MAX_VALUE):
	New macros.
	(TYPE_RM_VALUES): Likewise.
	(TYPE_RM_SIZE): Rewrite in terms of TYPE_RM_VALUES.
	(SET_TYPE_RM_SIZE): New macro.
	(TYPE_RM_MIN_VALUE, TYPE_RM_MAX_VALUE): Likewise.
	(SET_TYPE_RM_SIZE, SET_TYPE_RM_MAX_VALUE): Likewise.
	(TYPE_MIN_VALUE, TYPE_MAX_VALUE): Redefine.
	* gcc-interface/gigi.h (create_range_type): Declare.
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Modular_Integer_Type>
	Use SET_TYPE_RM_MAX_VALUE to set the upper bound on the UMT type.
	<E_Signed_Integer_Subtype>: Build a regular integer type first and
	then set the RM bounds.  Use SET_TYPE_RM_SIZE to set the RM size.
	<E_Floating_Point_Subtype>: Build a regular floating-point type first
	and then set the RM bounds.
	<E_Array_Type>: Use create_range_type instead of build_range_type.
	<E_Array_Subtype>: Build a regular integer type first and then set
	the RM bounds for the extra subtype.
	<E_String_Literal_Subtype>: Use create_range_type instead of
	build_range_type.
	<all>: Set the RM bounds for enumeration types and the GCC bounds for
	floating-point types.
	(set_rm_size): Use SET_TYPE_RM_SIZE to set the RM size.
	(make_type_from_size) <INTEGER_TYPE>: Use SET_TYPE_RM_{MIN,MAX}_VALUE
	to set the bounds.  Use SET_TYPE_RM_SIZE to set the RM size.
	(substitute_in_type) <INTEGER_TYPE>: Deal with GCC bounds for domain
	types and with RM bounds for subtypes.
	* gcc-interface/misc.c (LANG_HOOKS_GET_SUBRANGE_BOUNDS): Define.
	(gnat_print_type) <REAL_TYPE>: New case.
	<ENUMERAL_TYPE>: Fall through to above case.
	(gnat_get_subrange_bounds): New function.
	* gcc-interface/trans.c (add_decl_expr): Mark the trees rooted as
	TYPE_RM_MIN_VALUE and TYPE_RM_MAX_VALUE, if any.
	* gcc-interface/utils.c (gnat_init_decl_processing): Use precision 8
	for booleans.  Adjust and use SET_TYPE_RM_SIZE to set the RM size.
	(create_range_type): New function.
	(create_param_decl): Build a regular integer type first and then set
	the RM bounds for the extra subtype.
	(unchecked_convert): Remove kludge for 'Valid.
	* gcc-interface/utils2.c (build_binary_op) <ARRAY_RANGE_REF>: Convert
	the index to sizetype instead of TYPE_DOMAIN.

""",
u"""
delete dummy empty svn:mergeinfo properties
""",
u"""

        * config/frv/frv.h: Clean up references to GO_IF_LEGITIMATE_ADDRESS.
        * config/frv/frv.c: Likewise.
        * config/s390/s390.c: Likewise.
        * config/sparc/sparc.h: Likewise.
        * config/i386/i386.h: Likewise.
        * config/i386/i386.c: Likewise.
        * config/crx/crx.c: Likewise.
        * config/m68hc11/m68hc11.h: Likewise.
        * config/iq2000/iq2000.c: Likewise.
        * config/mn10300/mn10300.h: Likewise.
        * config/mn10300/mn10300.c: Likewise.
        * config/m68k/m68k.c: Likewise.
        * config/rs6000/rs6000.c: Likewise.
        * config/rs6000/xcoff.h: Likewise.
        * config/rs6000/linux64.h: Likewise.
        * config/rs6000/sysv4.h: Likewise.
        * config/score/score3.c: Likewise.
        * config/score/score7.c: Likewise.
        * config/score/score.c: Likewise.
        * config/arm/arm.md: Likewise.
        * config/mips/mips.c: Likewise.
        * config/mips/mips.md: Likewise.
        * config/bfin/bfin.h: Likewise.
        * config/pa/pa.c: Likewise.
        * config/pa/constraints.md: Likewise.

        * config/pdp11/pdp11-protos.h (legitimate_address_p): Delete.
        * config/pdp11/pdp11.c (legitimate_address_p): Delete.
        * config/pdp11/pdp11.h: Use memory_address_p instead.


""",
u"""

        PR fortran/39352
        * f95-lang.c: Add gfc_maybe_initialize_eh.
        * gfortran.h: Add gfc_maybe_initialize_eh prototype.
        * Make-lang.in: Add new .h dendencies for f95-lang.c
        * openmp.c (resolve_omp_do): Call gfc_maybe_initialize_eh.
        * misc.c (gfc_free): Avoid #define trickery for free.


""",
u"""
Daily bump.
""",
u"""
Correct formatting errors commited in rev 147516
""",
u"""

    * dump-parse-tree.c (show_code_node): Add ERRMSG to the dumping
    of allocate and deallocate statements.

""",
u"""
./:
	* passes.c (finish_optimization_passes): Change i to int.
	* plugin.c (plugins_active_p): Change event to int.
	(dump_active_plugins): Likewise.
	* reginfo.c (invalid_mode_change_p): Change to to unsigned int.
	Add cast.
	* tree.c (tree_range_check_failed): Change c to unsigned int.
	(omp_clause_range_check_failed): Likewise.
	(build_common_builtin_nodes): Change mode to int.  Add cast.
	* config/ia64/ia64.c (is_emitted): Change r to unsigned int.
	(ia64_hard_regno_rename_ok, ia64_eh_uses): Likewise.

	* c-typeck.c (build_unary_op): If -Wc++-compat, warn about using
	++ or -- with a variable of enum type.
cp/:
	* class.c (layout_class_type): Change itk to unsigned int.
	* decl.c (finish_enum): Change itk to unsigned int.
	* parser.c (cp_parser_check_decl_spec): Change ds to int.  Remove
	casts.
fortran/:
	* decl.c (match_attr_spec): Change d to unsigned int.
	* dump-parse-tree.c (show_namespace): Change op to int.  Add cast.
	* interface.c (gfc_check_interfaces): Change i to int.  Add casts.
	* module.c (read_module): Change i to int.  Add cast.
	(write_module): Change i to int.
	* symbol.c (gfc_get_namespace): Change in to int.
	(gfc_free_namespace): Change i to int.
	* trans-io.c (gfc_build_io_library_fndecls): Change ptype to
	unsigned int.  Add cast.
	* trans-types.c (gfc_init_kinds): Change mode to unsigned int.
	Add casts.
testsuite/:
	* gcc.dg/Wcxx-compat-9.c: New testcase.

""",
u"""
	PR driver/40144
	* opts.c (common_handle_option): Add OPT_fcse_skip_blocks as a no-op.

""",
u"""
	* store-motion.c Do not include params.h
	* Makefile.in: Fix dependencies for various files.

""",
u"""
	* auto-inc-dec.c: Fix pass description, remove apparent
	accidental duplication.


""",
u"""

	PR fortran/40045
	* dump-parse-tree.c (show_typebound): Fix missing adaption to new
	type-bound procedure storage structure.

""",
u"""

	PR libstdc++/40123
	* random.tcc (independent_bits_engine<>::operator()()): Use
	result_type(1), not 1UL.

	* random.tcc (independent_bits_engine<>::operator()()): Use _M_b.max()
	and _M_b.min(), instead of this->max() and this->min().

	* random.h (_ShiftMin1): Remove, adjust everywhere.

	* random.tcc: Minor cosmetic changes.

""",
u"""

	PR middle-end/40147
	* ipa-utils.h (memory_identifier_string): Moved to ...
	* tree.h (memory_identifier_string): Here.  Add GTY(()).

""",
u"""

	* doc/tm.texi (TARGET_LEGITIMATE_ADDRESS_P): Refer mainly to this
	in the former documentation of...
	(GO_IF_LEGITIMATE_ADDRESS): ... this.
	* ira-conflicts.c (get_dup_num): Use address_operand.
	* targhooks.c (default_legitimate_address_p): New.
	* targhooks.h (default_legitimate_address_p): New.
	* reload.c (strict_memory_address_p) [!GO_IF_LEGITIMATE_ADDRESS]:
	Call hook.
	* recog.c (memory_address_p) [!GO_IF_LEGITIMATE_ADDRESS]: Call hook.
	* target.h (struct target): Add legitimate_address_p.
	* target-def.h (TARGET_LEGITIMATE_ADDRESS_P): New.
	(TARGET_INITIALIZER): Include it.

	* config/alpha/alpha.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/alpha/alpha-protos.h (alpha_legitimate_address_p): Remove.
	* config/alpha/alpha.c (alpha_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/frv/frv.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	(REG_OK_STRICT_P): Delete.
	* config/frv/frv-protos.h (frv_legitimate_address_p): Rename to...
	(frv_legitimate_address_p_1): ... this.
	* config/frv/frv.c (frv_legitimate_address_p): Forward to...
	(frv_legitimate_address_p_1): ... the renamed old
	frv_legitimate_address_p.
	* config/frv/predicates.md: Adjust calls to frv_legitimate_address_p.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/s390/s390.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/s390/s390-protos.h (legitimate_address_p): Remove.
	* config/s390/s390.c (legitimate_address_p): Rename to...
	(s390_legitimate_address_p): ... this, make static.
	(legitimize_address): Adjust call.
	(TARGET_LEGITIMATE_ADDRESS_P): New.
	* config/s390/constraints.md ("e"): Call strict_memory_address_p.

	* config/m32c/m32c.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/m32c/m32c-protos.h (m32c_legitimate_address_p): Remove.
	* config/m32c/m32c.c (m32c_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/spu/spu.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/spu/spu-protos.h (spu_legitimate_address): Remove.
	* config/spu/spu.c (spu_legitimate_address): Rename to...
	(spu_legitimate_address_p): ... this, make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/sparc/sparc.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/sparc/sparc-protos.h (legitimate_address_p): Remove.
	* config/sparc/sparc.c (legitimate_address_p): Rename to...
	(sparc_legitimate_address_p): ... this, make static and return bool.
	(legitimize_address): Adjust call.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/i386/i386.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/i386/i386-protos.h (legitimate_address_p): Remove.
	* config/i386/i386.c (legitimate_address_p): Rename to...
	(ix86_legitimate_address_p): ... this, make static.
	(constant_address_p): Move after it, adjust call.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/avr/avr.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/avr/avr-protos.h (legitimate_address_p): Remove.
	* config/avr/avr.c (legitimate_address_p): Rename to...
	(avr_legitimate_address_p): ... this, make static.
	(legitimize_address): Adjust call.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/crx/crx.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/crx/crx-protos.h (crx_legitimate_address_p): Remove.
	* config/crx/crx.c (crx_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/xtensa/xtensa.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/xtensa/xtensa-protos.h (xtensa_legitimate_address_p): Remove.
	* config/xtensa/xtensa.c (xtensa_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/stormy16/stormy16.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/stormy16/stormy16-protos.h (xstormy16_legitimate_address_p):
	Remove.
	* config/stormy16/stormy16.c (xstormy16_legitimate_address_p):
	Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/m68hc11/m68hc11.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/m68hc11/m68hc11-protos.h (m68hc11_go_if_legitimate_address):
	Remove.
	* config/m68hc11/m68hc11.c (m68hc11_go_if_legitimate_address):
	Rename to...
	(m68hc11_legitimate_address_p): ... this, make static.
	(go_if_legitimate_address_internal): Rename to...
	(m68hc11_legitimate_address_p_1): ... this.
	(legitimize_address): Adjust call.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/iq2000/iq2000.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/iq2000/iq2000-protos.h (iq2000_legitimate_address_p):
	Remove.
	* config/iq2000/iq2000.c (iq2000_legitimate_address_p):
	Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/mn10300/mn10300.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/mn10300/mn10300-protos.h (legitimate_address_p): Remove.
	* config/mn10300/mn10300.c (legitimate_address_p): Rename to...
	(mn10300_legitimate_address_p): ... this, make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/m68k/m68k.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/m68k/m68k-protos.h (m68k_legitimate_address_p): Remove.
	* config/m68k/m68k.c (m68k_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/rs6000/rs6000.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	(REG_OK_STRICT_FLAG, REG_OK_FOR_BASE_P, REG_OK_FOR_INDEX_P): Delete.
	(INT_REG_OK_FOR_BASE_P, INT_REG_OK_FOR_INDEX_P): Move above.
	* config/rs6000/rs6000.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/rs6000/rs6000-protos.h (rs6000_legitimate_address): Remove.
	* config/rs6000/rs6000.c (rs6000_legitimate_address): Rename to...
	(rs6000_legitimate_address_p): ... this, make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.
	(REG_MODE_OK_FOR_BASE_P): Delete.
	(rs6000_legitimize_reload_address): Use INT_REG_OK_FOR_BASE_P.

	* config/picochip/picochip.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/picochip/picochip-protos.h (picochip_legitimate_address_p):
	Delete.
	* config/picochip/picochip.c (picochip_legitimate_address_p): Make
	static, adjust types.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/score/score.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/score/score.c (score_address_p): Rename to...
	(score_legitimate_address_p): ... this.
	(TARGET_LEGITIMATE_ADDRESS_P): New.
	* config/score/score3.c (score3_address_p): Rename to...
	(score3_legitimate_address_p): ... this.
	* config/score/score7.c (score7_address_p): Rename to...
	(score7_legitimate_address_p): ... this.

	* config/arm/arm.h (ARM_GO_IF_LEGITIMATE_ADDRESS,
	THUMB2_GO_IF_LEGITIMATE_ADDRESS, THUMB1_GO_IF_LEGITIMATE_ADDRESS,
	GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/arm/arm-protos.h (thumb1_legitimate_address_p,
	thumb2_legitimate_address_p): Delete.
	(arm_legitimate_address_p): Rename to...
	(arm_legitimate_address_outer_p): ... this.
	* config/arm/constraints.md ("Uq"): Adjust call.
	* config/arm/predicates.md (arm_extendqisi_mem_op): Likewise.
	* config/arm/arm.c (arm_legitimate_address_p): New, rename old one to...
	(arm_legitimate_address_outer_p): ... this.
	(thumb1_legitimate_address_p, thumb2_legitimate_address_p): Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/mips/mips.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/mips/mips-protos.h (mips_legitimate_address_p): Remove.
	* config/mips/mips.c (mips_legitimate_address_p): ... Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/vax/vax.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/vax/vax-protos.h (legitimate_address_p): Remove.
	* config/vax/vax.c (legitimate_address_p): Rename to...
	(vax_legitimate_address_p): ... this, make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/h8300/h8300.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/h8300/h8300-protos.h (h8300_legitimate_address_p): Remove.
	* config/h8300/h8300.c (h8300_legitimate_address_p): ... Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/mmix/mmix.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/mmix/mmix-protos.h (mmix_legitimize_address): Remove.
	* config/mmix/mmix.c (mmix_legitimate_address): Rename to...
	(mmix_legitimate_address_p): ... this, make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

	* config/bfin/bfin.h (GO_IF_LEGITIMATE_ADDRESS): Delete.
	* config/bfin/bfin-protos.h (bfin_legitimate_address_p): Remove.
	* config/bfin/bfin.c (bfin_legitimate_address_p): ... Make static.
	(TARGET_LEGITIMATE_ADDRESS_P): New.

""",
u"""
delete dummy empty svn:mergeinfo properties
""",
u"""

	* config/arm/arm.h (PROMOTE_FUNCTION_MODE): Remove handling
	of MODE_COMPLEX_INT.


""",
u"""
	* gcc-interface/decl.c (elaborate_expression_1): Remove GNAT_EXPR
	parameter and move check for static expression to...
	(elaborate_expression): ...here.  Adjust call to above function.
	(gnat_to_gnu_entity): Likewise for all calls.  Use correct arguments
	in calls to elaborate_expression.
	(elaborate_entity): Likewise.
	(substitution_list): Likewise.
	(maybe_variable): Fix formatting.
	(substitute_in_type) <REAL_TYPE>: Merge with INTEGER_TYPE case and add
	missing guard.
	* gcc-interface/trans.c (protect_multiple_eval): Minor cleanup.

""",
u"""
	* config/alpha/alpha.c (alpha_initialize_trampoline): Change 0 to
	LCT_NORMAL in function call.
	* mips-tdump.c (print_file_desc): Add cast to enum type.
	* mips-tfile.c (add_ext_symbol): Add casts to enum types.
	(mark_stabs): Add casts to enum types.
	(parse_stabs_common): Add casts to enum types.

""",
u"""

	PR fortran/39996
	* decl.c (gfc_match_function_decl): Use gfc_add_type.
	* symbol.c (gfc_add_type): Better checking for duplicate types in
	function declarations. And: Always give an error for duplicte types,
	not just a warning with -std=gnu.



	PR fortran/39996
	* gfortran.dg/func_decl_2.f90: Modified (replacing warnings by errors).
	* gfortran.dg/duplicate_type_2.f90: Ditto.
	* gfortran.dg/duplicate_type_3.f90: New.


""",
u"""

	* include/bits/random.tcc (cauchy_distribution<>::
	operator()(_UniformRandomNumberGenerator&, const param_type&)): 
	Avoid M_PI, a glibc extension.

""",
u"""
	
        * ada/acats/tests/c3/c38202a.ada: Use Impdef.
        * ada/acats/tests/c5/c59002c.ada: Likewise.
	
(and fix ChangeLog formating of previous entry)

""",
u"""
Fix formatting
""",
u"""
	* config/mips/mips.c (mips_print_operand) <REG, MEM, default>:
	Check for invalid values of LETTER.

""",
u"""
gcc/
       * attribs.c moved out attribute registration into register_attribute
       * doc/plugins.texi Documented register_attribute and PLUGIN_ATTRIBUTES
       * gcc-plugin.h Added forward decl for register_attribute
       * plugin.c Added PLUGIN_ATTRIBUTES boilerplate
       * plugin.h Added PLUGIN_ATTRIBUTES

gcc/testsuite/
       * g++.dg/plugin/attribute_plugin-test-1.C Testcase input for custom attributes and decl smashing
       * g++.dg/plugin/attribute_plugin.c Testcase plugin to test user attributes
       * g++.dg/plugin/dumb_plugin.c Fixed typo
       * g++.dg/plugin/plugin.exp Added attribute_plugin test 

""",
u"""
Updated the wrong changelog
""",
u"""
gcc/
      * decl.c (duplicate_decls): Preserve parameter attributes.

""",
u"""
	* config/i386/msformat-c.c (ms_printf_length_specs):  Use enumeration
	values even in sentinel and empty entries.
	(ms_printf_flag_specs):  Likewise.
	(ms_scanf_flag_specs):  Likewise.
	(ms_strftime_flag_specs):  Likewise.
	(ms_print_char_table):  Likewise.
	(ms_scan_char_table):  Likewise.
	(ms_time_char_table):  Likewise.


""",
u"""
Daily bump.
""",
u"""

	* tree-ssa-sccvn.c (compare_ops): Stabilize qsort.


""",
u"""
	PR fortran/39865
	* io.c (resolve_tag_format): CHARACTER array in FMT= argument
	isn't an extension.  Reject non-CHARACTER array element of
	assumed shape or pointer or assumed size array.
	* trans-array.c (array_parameter_size): New function.
	(gfc_conv_array_parameter): Add size argument.  Call
	array_parameter_size if it is non-NULL.
	* trans-array.h (gfc_conv_array_parameter): Adjust prototype.
	* trans-expr.c (gfc_conv_function_call, gfc_trans_arrayfunc_assign):
	Adjust callers.
	* trans-intrinsic.c (gfc_conv_intrinsic_loc): Likewise.
	* trans-io.c (gfc_convert_array_to_string): Rewritten.

	* gfortran.dg/pr39865.f90: New test.
	* gfortran.dg/hollerith.f90: Don't expect errors for CHARACTER
	arrays in FMT=.
	* gfortran.dg/hollerith_f95.f90: Likewise.
	* gfortran.dg/hollerith6.f90: New test.
	* gfortran.dg/hollerith7.f90: New test.

""",
u"""

	PR cpp/36674
libcpp/
	* directives (do_linemarker): Compensate for the increment in
	location that occurs when we reach the end of line.
	* files (_cpp_stack_include): Mention _cpp_find_file in the
	comment.
testsuite/
	* gcc.dg/cpp/pr36674.i: New.

""",
u"""
	* config/mips/mips.md (store): Add attributes for QI and HI.
	Update comment.
	(truncdisi2, truncdihi2, truncdiqi2): Merge these into ...
	(truncdi<mode>2): ... this new pattern.

""",
u"""
Correct datestamp of my most recent entry.
""",
u"""

	* Makefile.in (TEXI_GCCINT_FILES): Add plugins.texi.


""",
u"""
	PR middle-end/40035
	* dse.c (check_mem_read_rtx): Guard against width == -1.
testsuite/
	* gcc.c-torture/compile/pr40035.c: New test.

""",
u"""

	* gfortran.h (gfc_code): Rename struct member expr to expr1.
	* openmp.c (resolve_omp_atomic): Update expr to expr1.
	* interface.c (gfc_extend_assign): Ditto.
	* trans-expr.c (gfc_conv_expr_reference, gfc_trans_assignment,
	gfc_trans_init_assign): Ditto.
	* dump-parse-tree.c (show_code_node): Ditto.
	* trans-openmp.c (gfc_trans_omp_atomic): Ditto.
	* trans-stmt.c ( gfc_trans_label_assign, gfc_trans_goto, gfc_trans_call,
	gfc_trans_return, gfc_trans_pause, gfc_trans_stop, gfc_trans_if_1,
	gfc_trans_arithmetic_if, gfc_trans_do_while, gfc_trans_integer_select,
	gfc_trans_logical_select, gfc_trans_character_select
	forall_make_variable_temp, check_forall_dependencies
	gfc_trans_forall_1, gfc_trans_where_2, gfc_trans_where_3
	gfc_trans_where, gfc_trans_allocate, gfc_trans_deallocate): Ditto.
	* io.c (match_io_element, gfc_match_inquire): Ditto.
	* resolve.c (resolve_typebound_call, resolve_ppc_call,
	resolve_allocate_expr, resolve_allocate_deallocate, resolve_select,
	resolve_transfer, resolve_where, gfc_resolve_assign_in_forall,
	gfc_resolve_blocks, resolve_code, build_init_assign): Ditto.
	* st.c (gfc_free_statement): Ditto.
	* match.c (gfc_match_assignment, gfc_match_pointer_assignment,
	match_arithmetic_if, gfc_match_if, gfc_match_elseif
	gfc_match_stopcode, gfc_match_assign, gfc_match_goto,
	gfc_match_nullify, match_typebound_call, gfc_match_call
	gfc_match_select, match_simple_where, gfc_match_where
	gfc_match_elsewhere, match_simple_forall, gfc_match_forall): Ditto.
	* trans-io.c (gfc_trans_transfer): Ditto.
	* parse.c (parse_where_block, parse_if_block): Ditto.


""",
u"""
	* gcc.target/i386/pr39543-2.c: Skip if ilp32 && pic.


""",
u"""
        PR middle-end/39976
        * tree-outof-ssa.c (maybe_renumber_stmts_bb): New function.
        (trivially_conflicts_p): New function.
        (insert_backedge_copies): Use it.

""",
u"""
	* c-pragma.c (enum pragma_switch_t): Prefix constants with PRAGMA_.
	(handle_stdc_pragma): Use new enum constant names.
	(handle_pragma_float_const_decimal64): Ditto.

""",
u"""
	* Makefile.in (build/gencheck.o): Depend upon all-tree.def, not
	tree.def.

""",
u"""

	* gfortran.h (gfc_code): Rename struct member label to label1.
	* dump-parse-tree.c (show_code_node): Update symbol.
	* trans-stmt.c (gfc_trans_label_assign, gfc_trans_goto,
	gfc_trans_arithmetic_if)": Ditto.
	* resolve.c (gfc_resolve_blocks, resolve_code): Ditto.
	* match.c (match_arithmetic_if, gfc_match_if, gfc_reference_st_label,
	gfc_match_assign, gfc_match_goto): Ditto.
	* parse.c (parse_do_block): Ditto.


""",
u"""
	* config/m68k/t-uclinux (M68K_MLIB_CPU): Check for FL_UCLINUX.
	* config/m68k/m68k-devices.def: Add FL_UCLINUX to 68020 and 54455
	multilibs.
	* config/m68k/m68k.h (FL_UCLINUX): Define.

""",
u"""

        PR fortran/34153
        * gfortran.h (gfc_exec_op): Add EXEC_END_PROCEDURE.
        * dump-parse-tree.c (show_code_node): Use EXEC_END_PROCEDURE.
        * trans.c (gfc_trans_code): Ditto.
        * resolve.c (resolve_code): Ditto.
        * st.c (gfc_free_statement): Ditto.


""",
u"""
	* doc/invoke.texi (-fwhole-file): Update docs.

	* options.c (gfc_post_options): -fwhole-program imply -fwhole-file.

""",
u"""
	* include/Makefile.am (PCHFLAGS): Remove -Winvalid-pch.
	* include/Makefile.in: Likewise.

""",
u"""
Daily bump.
""",
u"""
	* src/compatibility.cc (_ZTIe, _ZTIPe, _ZTIPKe): Change type to
	const void * const.

""",
u"""
	* config/sh/sh.h (OVERRIDE_OPTIONS): Clear flag_schedule_insns
	unless -fschedule-insns is specified.


""",
u"""
	PR target/39561
	* config/sh/sh.h (OPTIMIZATION_OPTIONS): Don't set
	TARGET_EXPAND_CBRANCHDI4.
	* config/sh/sh.md (cbranchdi4): Don't check TARGET_EXPAND_CBRANCHDI4.
	* config/sh/sh.opt (mexpand-cbranchdi): Remove.
	(cmpeqdi): Fix comment.


""",
u"""

        PR fortran/40110
        * decl.c (gfc_match_kind_spec): Turn C kind error into a
        * warning.


        PR fortran/40110
        * gfortran.dg/bind_c_usage_18.f90: Change dg-error into
        dg-warning.
        * gfortran.dg/c_kind_tests_2.f03: Ditto.
        * gfortran.dg/interop_params.f03: Ditto.


""",
u"""
	* config/sh/sh-protos.h (sh_legitimate_index_p): Declare.
	(sh_legitimate_address_p): Likewise.
	* config/sh/sh.c (sh_legitimate_index_p): New.
	(sh_legitimate_address_p): Likewise.
	* config/sh/sh.h (REG_OK_FOR_BASE_P): Add STRICT parameter.
	(REG_OK_FOR_INDEX_P, SUBREG_OK_FOR_INDEX_P): Likewise.
	(MODE_DISP_OK_4, MODE_DISP_OK_8): Remove.
	(MAYBE_BASE_REGISTER_RTX_P): New macro.
	(MAYBE_INDEX_REGISTER_RTX_P): Likewise.
	(BASE_REGISTER_RTX_P): Use MAYBE_BASE_REGISTER_RTX_P.
	(INDEX_REGISTER_RTX_P): Use MAYBE_INDEX_REGISTER_RTX_P.
	(GO_IF_LEGITIMATE_INDEX): Use sh_legitimate_index_p.
	(GO_IF_LEGITIMATE_ADDRESS): Use sh_legitimate_address_p.


""",
u"""

        * doc/xml/manual/status_cxx200x.xml: Note missing constexpr for
	random number engines, complex, bitset, array, time utilities, and
	char_traits.


""",
u"""

	* libsupc++/exception: Include nested_exception.h in C++0x mode.
	* libsupc++/nested_exception.h: New.
	* libsupc++/Makefile.am: Add new header.
	* libsupc++/Makefile.in: Regenerate.
	* testsuite/18_support/nested_exception/rethrow_nested.cc: New.
	* testsuite/18_support/nested_exception/throw_with_nested.cc: New.
	* testsuite/18_support/nested_exception/cons.cc: New.
	* testsuite/18_support/nested_exception/nested_ptr.cc: New.
	* testsuite/18_support/nested_exception/rethrow_if_nested.cc: New.
	* doc/xml/manual/status_cxx200x.xml: Adjust.

""",
u"""
	PR target/37179:
	* Correct PR number for revision 147429.

""",
u"""

	* gcc.dg/tree-ssa/loop-36.c: Reduce amount of iterations to 2 so unrolling
	still happens.
	* gcc.dg/ipa/ipacost-1.c: Prevent inlining
	* gcc.dg/ipa/ipacost-2.c: Likewise.
	* gcc.dg/vect/slp-3.c: Loop is no longer unrolled.

	* tree-inline.c (estimate_operator_cost): Add operands;
	when division happens by constant, it is cheap.
	(estimate_num_insns): Loads and stores are not having cost of 0;
	EH magic stuff is cheap; when computing runtime cost of switch,
	use log2 base of amount of its cases; builtin_expect has cost of 0;
	compute cost for moving return value of call.
	(init_inline_once): Initialize time_based flags.
	* tree-inline.h (eni_weights_d): Add time_based flag.

""",
u"""

	* df-core.c: Update head documentation.


""",
u"""
Fix PR bootstrap/40118
""",
u"""

        * gfortran.dg/default_format_1.f90: XFAIL on cygwin.

""",
u"""
	PR target/37197
	* config/i386/driver-i386.c (processor_signatures): New enum.
	(SIG_GEODE): Move from vendor_signatures to processor_signatures.
	(host_detect_local_cpu): For SIG_AMD vendor, check for SIG_GEODE
	processor signature to detect geode processor.


""",
u"""

	Revert:


	* optabs.c (prepare_cmp_insn): Temporarily disable test that
	causes spurious differences between trunk and cond-optab branch.


""",
u"""
Merge cond-optab branch.
""",
u"""

    * lib/target-supports.exp (check_profiling_available): Return
    false for -p on *-*-cygwin* targets.

""",
u"""

	* optabs.c (prepare_cmp_insn): Temporarily disable test that
	causes spurious differences between trunk and cond-optab branch.


""",
u"""
ChangeLog:
PR target/37137
* Makefile.def (flags_to_pass): Remove redundant and incomplete
STAGE1_CFLAGS, STAGE2_CFLAGS, STAGE3_CFLAGS, and STAGE4_CFLAGS.
Add FLAGS_FOR_TARGET and BUILD_CONFIG.
(bootstrap_stage): Remove bootstrap-debug custom stages.  Turn
stage_configureflags, stage_cflags and stage_libcflags into
explicit Makefile macros.
* Makefile.tpl (HOST_EXPORTS, EXTRA_HOST_FLAGS): Pass GCJ and
GFORTRAN.
(POSTSTAGE1_HOST_EXPORTS): Add XGCC_FLAGS_FOR_TARGET and TFLAGS to
CC.  Set CC_FOR_BUILD from CC.
(BASE_TARGET_EXPORTS, RAW_CXX_TARGET_EXPORTS,
NORMAL_TARGET_EXPORTS): Move SYSROOT_CFLAGS_FOR_TARGET and
DEBUG_PREFIX_CFLAGS_FOR_TARGET from CFLAGS and CXXFLAGS to
XGCC_FLAGS_FOR_TARGET.  Add it along with TFLAGS to CC, CXX, GCJ,
and GFORTRAN.
(TFLAGS, STAGE_CFLAGS, STAGE_TFLAGS, STAGE_CONFIGURE_FLAGS): New.
(_LIBCFLAGS): Renamed to _TFLAGS.
(do-compare-debug, do-compare3-debug): Drop.
(CC, GCC_FOR_TARGET, CXX_FOR_TARGET, RAW_CXX_FOR_TARGET,
GCJ_FOR_TARGET, GFORTRAN_FOR_TARGET): Remove FLAGS_FOR_TARGET.
(FLAGS_FOR_TARGET, SYSROOT_CFLAGS_FOR_TARGET,
DEBUG_PREFIX_CFLAGS_FOR_TARGET): Move down.
(XGCC_FLAGS_FOR_TARGET): New.
(BASE_FLAGS_TO_PASS): Pass STAGEid_CFLAGS, STAGEid_TFLAGS and TFLAGS.
(EXTRA_HOST_FLAGS): Pass GCJ and GFORTRAN.
(POSTSTAGE1_FLAGS_TO_PASS): Move SYSROOT_CFLAGS_FOR_TARGET and
DEBUG_PREFIX_CFLAGS_FOR_TARGET from CFLAGS, CXXFLAGS, LIBCFLAGS,
LIBCXXFLAGS to XGCC_FLAGS_FOR_TARGET.    Add it along with TFLAGS
to CC, CXX, GCJ, and GFORTRAN.  Pass XGCC_FLAGS_FOR_TARGET and
TFLAGS.
(BUILD_CONFIG): Include if requested.
(all): Set TFLAGS on bootstrap.
(configure-stageid-prefixmodule): Pass TFLAGS, adjust FLAGS.
(all-stageid-prefixmodule): Likewise.
(do-clean, distclean-stageid): Set TFLAGS.
(restrap): Fix whitespace.
* Makefile.in: Rebuilt.
config/ChangeLog:
* multi.m4: Save CXX, GFORTRAN and GCJ in config.status.
* mt-gnu (CXXFLAGS_FOR_TARGET): Adjust.
* bootstrap-O1.mk: New.
* bootstrap-O3.mk: New.
* bootstrap-debug.mk: New.
gcc/ChangeLog:
PR target/37137
* doc/install.texi (STAGE1_TFLAGS, BUILD_CONFIG): Document.
gcc/java/ChangeLog:
* Make-lang.in (GCJ): Renamed to...
(XGCJ): ... this.
libjava/ChangeLog:
* configure.ac: Insert libgcjdir in the GCJ passed in the
environment, rather than overriding completely.
* configure: Rebuilt.

""",
u"""
* tree.c (iterative_hash_pointer): Delete.
(iterative_hash_expr): Short-circuit handling of NULL pointer.
Hash UIDs and versions of SSA names.  Don't special-case built-in
function declarations.

""",
u"""
	PR bootstrap/40103
	* graphite.c: Force -Wc++-compat to only be a warning before
	#including "cloog/cloog.h".

""",
u"""
Daily bump.
""",
u"""

	PR tree-optimization/38632
	* g++.dg/tree-ssa/pr38632.C: New.

""",
u"""

	* ipa-cp.c (ipcp_cloning_candidate_p): Add missing return false.
	


""",
u"""

	* gcc.dg/tree-ssa/pr21829.c: Simplify matching since
	we now optimize better.
	* gcc.dg/Wunreachable-8.c: Bogus warnings now come
	out at different places.
	* gcc.dg/vect/vect-92.c: Increase loop iteration count to prevent
	unroling.
	* gcc.dg/vect/vect-76.c: Likewise.
	* gcc.dg/vect/vect-70.c: Likewise.
	* gcc.dg/vect/vect-66.c: Likewise.
	* gcc.dg/vect/no-section-anchors-vect-66.c: Likewise.
	* gcc.dg/vect/slp-3.c: One of loops gets now fully unrolled.
	* tree-ssa-loop-ivcanon.c: Include target.h
	(struct loop_size): new structure.
	(constant_after_peeling): New predicate.
	(tree_estimate_loop_size): New function.
	(estimated_unrolled_size): Rewrite for new estimates.
	(try_unroll_loop_completely): Use new estimates.
	* Makefile.in (tree-ssa-loop-ivcanon.o): Add dependenc on target.h

""",
u"""

        * config/spu/spu-c.c (spu_categorize_keyword): Update for recent
        libcpp interface change.
        (spu_macro_to_expand): Likewise.


""",
u"""

	PR middle-end/40080
	* gcc.c-torture/compile/pr40080.c: New.

""",
u"""

	PR tree-optimization/40026
	* gimplify.c (gimplify_init_constructor): Change initial conditional
	to assertion.  Rewrite TREE_OPERAND (*expr_p, 1) after
	optimize_compound_literals_in_ctor.

testsuite:

	* gcc.c-torture/compile/pr40026.c: New testcase.


""",
u"""
	* config/m68k/m68k-devices.def (52274, 52277, 5301x, 5225x, 51xx):
	New devices.
	* doc/invoke.texi (M680x0 Options): Document new coldfire cpus.

""",
u"""
	* resolve.c (check_host_association): Initialize tail.

""",
u"""

	PR fortran/40089
	* resolve.c (resolve_fl_derived): Only return FAILURE if
	gfc_notify_std fails.



	PR fortran/40089
	* gfortran.dg/proc_ptr_comp_7.f90: New.


""",
u"""

	* tree-vect-data-refs.c (vect_analyze_group_access): Use
	HOST_WIDE_INT for gap.

""",
u"""
	PR tree-optimization/40074
	* tree-vect-data-refs.c (vect_analyze_group_access): Take gaps into
	account in group size and step comparison.


""",
u"""

	* passes.c (init_optimization_passes): Strip now incorrect comment.
	(execute_function_todo): Do not set PROP_alias.
	* tree-pass.h (PROP_alias): Remove.
	* tree-ssa-structalias.c (pass_build_alias): Do not provide PROP_alias.
	* tree-if-conv.c (pass_if_conversion): Do not require PROP_alias.
	* tree-nrv.c (pass_return_slot): Likewise.
	* tree-object-size.c (pass_object_sizes): Likewise.
	* tree-ssa-dom.c (pass_dominator): Likewise.
	(pass_phi_only_cprop): Likewise.
	* tree-ssa-dse.c (pass_dse): Likewise.
	* tree-ssa-phiopt.c (pass_phiopt): Likewise.
	(pass_cselim): Likewise.
	* tree-ssa-pre.c (pass_pre): Likewise.
	(pass_fre): Likewise.
	* tree-ssa-reassoc.c (pass_reassoc): Likewise.
	* tree-ssa-sink.c (pass_sink_code): Likewise.
	* tree-stdarg.c (pass_stdarg): Likewise.
	* tree-tailcall.c (pass_tail_calls): Likewise.
	* tree-vrp.c (pass_vrp): Likewise.

""",
u"""
./:
	* basic-block.h (enum profile_status): Break out of struct
	control_flow_graph.
	* cgraph.h (struct inline_summary): Break out of struct
	cgraph_local_info.
	* cgraphunit.c (enum cgraph_order_sort_kind): New enum, broken out
	of struct cgraph_order_sort.
	* combine.c (enum undo_kind): New enum, broken out of struct
	undo.
	* cse.c (struct branch_path): Break out of struct
	cse_basic_block_data.
	* except.h (enum eh_region_type): Break out of struct eh_region.
	* gcc.c (enum add_del): Break out of struct modify_target.
	* genrecog.c (enum decision_type): Break out of struct
	decision_test.
	* ggc-page.c (struct ggc_pch_ondisk): Break out of struct
	ggc_pch_data.
	* matrix-reorg.c (struct free_info): Break out of struct
	matrix_info.
	* regmove.c (enum match_use): New enum, broken out of struct
	match.
	* sched-int.h (enum post_call_group): New enum, broken out of
	struct deps.
	(struct deps_reg): Break out of struct deps.
	* target.h (struct asm_int_op): Break out of struct gcc_target.
	* tree-eh.c (struct goto_queue_node): Break out of struct
	leh_tf_state.
	* tree-inline.h (enum copy_body_cge_which): Break out of
	copy_body_data.
	* tree-pass.h (enum opt_pass_type): Break out of struct opt_pass.

	* c-decl.c (in_struct, struct_types): New static variables.
	(pushtag): Add loc parameter.  Change all callers.
	(lookup_tag): Add ploc parameter.  Change all callers.
	(check_compound_literal_type): New function.
	(parser_xref_tag): Add loc parameter.  Change all callers.  If
	-Wc++-compat, warn about struct/union/enum types defined within a
	struct or union.
	(start_struct): Add enclosing_in_struct, enclosing_struct_types,
	and loc parameters.  Change all callers.  Change error calls to
	error_at, using loc.  For a redefinition, if the location of the
	original definition is known, report it.  Set in_struct and
	struct_types.  If -Wc++-compat warn if in sizeof, typeof, or
	alignof.
	(finish_struct): Add new parameters enclosing_in_struct and
	enclosing_struct_types.  Change all callers.  Set
	C_TYPE_DEFINED_IN_STRUCT for all struct/union/enum types defined
	in the struct.  If in a struct, add this struct to struct_types.
	(start_enum): Add loc parameter.  Change all callers.  Use
	error_at for errors, using loc.  For a redefinition, if the
	location of the original definition is known, report it.  If in a
	struct, add this enum type to struct_types.  If -Wc++-compat warn
	if in sizeof, typeof, or alignof.
	* c-parser.c (disable_extension_diagnostics): Disable
	-Wc++-compat.
	(enable_extension_diagnostics): Reenable -Wc++-compat if
	appropriate.
	(c_parser_enum_specifier): Get enum location for start_enum.
	(c_parser_struct_or_union_specifier): Get struct location for
	start_struct.  Save in_struct and struct_types status between
	start_struct and finish_struct.
	(c_parser_cast_expression): Get location of cast.
	(c_parser_alignof_expression): Get location of type.
	(c_parser_postfix_expression): Likewise.
	(c_parser_postfix_expression_after_paren_type): Add type_loc
	parameter.  Change all callers.  Call
	check_compound_literal_type.  Use type_loc for error about
	variable size type.
	* c-typeck.c (build_external_ref): If -Wc++-compat, warn about a
	use of an enum constant from an enum type defined in a struct or
	union.
	(c_cast_expr): Add loc parameter.  Change all callers.  If
	-Wc++-compat, warn about defining a type in a cast.
	* c-tree.h (C_TYPE_DEFINED_IN_STRUCT): Define.
	(start_enum, start_struct, finish_struct): Update declarations.
	(parser_xref_tag, c_cast_expr): Update declarations.
	(check_compound_literal_type): Declare.
fortran/:
	* gfortran.h (enum gfc_omp_sched_kind): New enum, broken out of
	gfc_omp_clauses.
	(enum gfc_omp_default_sharing): Likewise.
	* module.c (enum gfc_rsym_state): New enum, broken out of
	pointer_info.
	(enum gfc_wsym_state): Likewise.
	* parse.c (enum state_order): New enum, broken out of st_state.
objc/:
	* objc-act.c (objc_building_struct): New static variable.
	(objc_in_struct, objc_struct_types): New static variables.
	(objc_start_struct, objc_finish_struct): New static functions.
	(generate_struct_by_value_array): Call objc_start_struct instead
	of start_struct, and call objc_finish_struct instead of
	finish_struct.
	(objc_build_struct, build_objc_symtab_template): Likewise.
	(build_module_descriptor): Likewise.
	(build_next_objc_exception_stuff): Likewise.
	(build_protocol_template): Likewise.
	(build_method_prototype_list_template): Likewise.
	(build_method_prototype_template): Likewise.
	(build_category_template, build_selector_template): Likewise.
	(build_class_template, build_super_template): Likewise.
	(build_ivar_template, build_ivar_list_template): Likewise.
	(build_method_list_template): Likewise.
	(build_method_template): Likewise.
objcp/:
	* objcp-decl.h (start_struct): Add three new, ignored, macro
	parameters.
	(finish_struct): Add two new, ignored, macro parameters.
testsuite/:
	* gcc.dg/Wcxx-compat-7.c: New testcase.
	* gcc.dg/Wcxx-compat-8.c: New testcase.
	* gcc.dg/c99-tag-1.c: Recognize new "originally defined here"
	notes
	* gcc.dg/pr17188-1.c: Likewise.
	* gcc.dg/pr39084.c: Likewise.

""",
u"""
Daily bump.
""",
u"""
	* config/rs6000/rs6000-c.c (altivec_categorize_keyword): Update
	for recent libcpp interface change.
	(rs6000_macro_to_expand): Likewise.

""",
u"""
        PR target/40031
        * config/arm/arm.c (require_pic_register): Emit on entry
        edge, not at entry of function.
testsuite/
        * gcc.dg/pr40031.c: New test.

""",
u"""

	PR tree-optimization/40081
	Revert
	* tree-sra.c (instantiate_element): Instantiate scalar replacements
	using the main variant of the element type.  Do not fiddle with
	TREE_THIS_VOLATILE or TREE_SIDE_EFFECTS.

	* tree-sra.c (sra_type_can_be_decomposed_p): Do not decompose
	structs with volatile fields.

""",
u"""
Remove junk file
""",
u"""
	* tree-inline.c (delete_unreachable_blocks_update_callgraph): Declare.
	(estimate_move_cost): Assert that it does not get called for VOID_TYPE_P.
	(estimate_num_insns): Skip VOID types in argument handling.
	(optimize_inline_calls): Delete unreachable blocks and verify that
	callgraph is valid.

""",
u"""
Fix changelog entry.

""",
u"""
	* cgraphbuild.c (record_reference): Use cgraph_mark_address_taken_node.
	* cgraph.c (cgraph_mark_address_taken_node): New function.
	(dump_cgraph_node): Dump new flag.
	* cgraph.h (struct cgraph_node): Add address_taken.
	(cgraph_mark_address_taken_node): New function.
	* cp/decl2.c (cxx_callgraph_analyze_expr): Use
	cgraph_mark_address_taken.
	* ipa.c (cgraph_postorder): Prioritize functions with address taken
	since new direct calls can be born.

""",
u"""
gcc:
	* c-lex.c (c_lex_with_flags): Expect cpp_hashnode in
	tok->val.node.node.

libcpp:
	* include/cpplib.h (enum cpp_token_fld_kind): Add
	CPP_TOKEN_FLD_TOKEN_NO.
	(struct cpp_macro_arg, struct cpp_identifier): Define.
	(union cpp_token_u): Use struct cpp_identifier for identifiers.
	Use struct cpp_macro_arg for macro arguments.  Add token_no for
	CPP_PASTE token numbers.
	* directives.c (_cpp_handle_directive, lex_macro_node, do_pragma,
	do_pragma_poison, parse_assertion): Use val.node.node in place of
	val.node.
	* expr.c (parse_defined, eval_token): Use val.node.node in place
	of val.node.
	* lex.c (cpp_ideq, _cpp_lex_direct, cpp_token_len,
	cpp_spell_token, cpp_output_token, _cpp_equiv_tokens,
	cpp_token_val_index): Use val.macro_arg.arg_no or val.token_no in
	place of val.arg_no.  Use val.node.node in place of val.node.
	* macro.c (replace_args, cpp_get_token, parse_params,
	lex_expansion_token, create_iso_definition, cpp_macro_definition):
	Use val.macro_arg.arg_no or val.token_no in place of val.arg_no.
	Use val.node.node in place of val.node.

""",
u"""
Fix formatting
""",
u"""
	PR middle-end/40084
	* cgraph.c (cgraph_update_edges_for_call_stmt_node): Take old_call argument;
	rewrite.
	(cgraph_update_edges_for_call_stmt): Take old_decl argument.
	* cgraph.h (cgraph_update_edges_for_call_stmt): Update prototype.
	* tree-inline.c (copy_bb): Set frequency correctly.
	(fold_marked_statements): Update call of cgraph_update_edges_for_call_stmt.

""",
u"""
	* gcc.pot: Regenerate.

""",
u"""
	* config/arc/arc.c (arc_handle_interrupt_attribute): Use %qE for
	identifiers in diagnostics.
	* config/arm/arm.c (arm_handle_fndecl_attribute,
	arm_handle_isr_attribute): Likewise.
	* config/avr/avr.c (avr_handle_progmem_attribute,
	avr_handle_fndecl_attribute, avr_handle_fntype_attribute):
	Likewise.
	* config/bfin/bfin.c (handle_int_attribute,
	bfin_handle_longcall_attribute, bfin_handle_l1_text_attribute,
	bfin_handle_l1_data_attribute, bfin_handle_longcall_attribute,
	bfin_handle_l1_text_attribute, bfin_handle_l1_data_attribute):
	Likewise.
	* config/darwin.c (darwin_handle_kext_attribute,
	darwin_handle_weak_import_attribute): Likewise.
	* config/h8300/h8300.c (h8300_handle_fndecl_attribute,
	h8300_handle_eightbit_data_attribute,
	h8300_handle_tiny_data_attribute): Likewise.
	* config/i386/i386.c (ix86_handle_cconv_attribute,
	ix86_handle_abi_attribute, ix86_handle_struct_attribute):
	Likewise.
	* config/i386/winnt.c (ix86_handle_shared_attribute,
	ix86_handle_selectany_attribute): Likewise.
	* config/ia64/ia64.c (ia64_handle_model_attribute): Likewise.
	* config/m32c/m32c.c (function_vector_handler): Likewise.
	* config/m68hc11/m68hc11.c (m68hc11_handle_page0_attribute,
	m68hc11_handle_fntype_attribute): Likewise.
	* config/m68k/m68k.c (m68k_handle_fndecl_attribute): Likewise.
	* config/mcore/mcore.c (mcore_handle_naked_attribute): Likewise.
	* config/mips/mips.c (mips_insert_attributes,
	mips_merge_decl_attributes, mips_expand_builtin): Likewise.
	* config/rs6000/rs6000.c (rs6000_handle_longcall_attribute,
	rs6000_handle_struct_attribute): Likewise.
	* config/sh/sh.c (sh_insert_attributes,
	sh_handle_resbank_handler_attribute,
	sh_handle_interrupt_handler_attribute,
	sh2a_handle_function_vector_handler_attribute,
	sh_handle_sp_switch_attribute, sh_handle_trap_exit_attribute):
	Likewise.
	* config/sh/symbian.c (sh_symbian_mark_dllimport): Likewise.
	* config/spu/spu.c (spu_handle_fndecl_attribute,
	spu_handle_vector_attribute): Likewise.
	* config/stormy16/stormy16.c
	(xstormy16_handle_interrupt_attribute): Likewise.
	* config/v850/v850-c.c (ghs_pragma_section): Likewise.
	* config/v850/v850.c (v850_handle_interrupt_attribute): Likewise.

""",
u"""
	* pretty-print.h (struct pretty_print_info): Add
	translate_identifiers.
	(pp_translate_identifiers): New.
	(pp_identifier): Only conditionally translate identifier to locale
	character set.
	* pretty-print.c (pp_construct): Set pp_translate_identifiers.
	(pp_base_tree_identifier): Only conditionally translate identifier
	to locale character set.
	* c-pretty-print.c (M_): Define.
	(pp_c_type_specifier, pp_c_primary_expression): Mark English
	fragments for conditional translation with M_.
	* tree-pretty-print.c (maybe_init_pretty_print): Disable
	identifier translation.

cp:
	* call.c (name_as_c_string): Call type_as_string_translate.
	Translate identifiers to locale character set.
	* cp-tree.h (lang_decl_name): Update prototype.
	(type_as_string_translate, decl_as_string_translate,
	cxx_printable_name_translate): Declare.
	* cxx-pretty-print.c (M_): Define.
	(pp_cxx_unqualified_id, pp_cxx_canonical_template_parameter): Mark
	English fragments for conditional translation with M_.
	* decl.c (grokdeclarator): Translate identifiers to locale
	character set for diagnostics.
	* error.c (M_): Define.
	(dump_template_bindings, dump_type, dump_aggr_type,
	dump_type_prefix, dump_global_iord, dump_simple_decl, dump_decl,
	dump_function_decl, dump_template_parms, dump_expr,
	dump_binary_op, op_to_string, assop_to_string): Mark English
	fragments for conditional translation with M_.
	(type_as_string): Disable translation of identifiers.
	(type_as_string_translate): New.
	(expr_as_string): Disable translation of identifiers.
	(decl_as_string): Disable translation of identifiers.
	(decl_as_string_translate): New.
	(lang_decl_name): Add parameter translate.
	(args_to_string): Call type_as_string_translate.
	(cp_print_error_function): Call cxx_printable_name_translate.
	(print_instantiation_full_context,
	print_instantiation_partial_context): Call
	decl_as_string_translate.
	* parser.c (cp_lexer_get_preprocessor_token): Use %qE for
	identifier in diagnostic.
	* tree.c (cxx_printable_name): Change to
	cxx_printable_name_internal.  Add parameter translate.
	(cxx_printable_name, cxx_printable_name_translate): New wrappers
	round cxx_printable_name_internal.

objc:
	* objc-act.c: Include intl.h.
	(objc_lookup_protocol): Use complete sentences for diagnostics
	with %qE for identifiers and translating results of
	gen_type_name_0 to locale character set.
	(objc_check_decl, check_protocol_recursively,
	lookup_and_install_protocols, objc_build_string_object,
	objc_get_class_reference, objc_declare_alias, objc_declare_class,
	objc_get_class_ivars, error_with_ivar, check_duplicates,
	objc_finish_message_expr, objc_build_protocol_expr,
	objc_build_selector_expr, build_ivar_reference, objc_add_method,
	add_category, add_instance_variable, objc_is_public,
	check_methods, check_methods_accessible, check_protocol,
	start_class, finish_class, start_protocol, really_start_method,
	get_super_receiver, objc_lookup_ivar): Use %E and %qE for
	identifiers in diagnostics.  Translate generated text to locale
	character set as needed.
	(check_protocol, check_protocols): Change name parameter to type
	tree.
	(lang_report_error_function): Remove.

""",
u"""

	PR fortran/40018
	* trans-array.c (gfc_trans_array_constructor_value): Fold
	convert numeric constants.
	(gfc_build_constant_array_constructor): The same.


	PR fortran/40018
	* gfortran.dg/array_constructor_31.f90: New test.

""",
u"""

	PR fortran/40018
	* trans-array.c (gfc_trans_array_constructor_value): Fold
	convert numeric constants.
	(gfc_build_constant_array_constructor): The same.


	PR fortran/40018
	* gfortran.dg/array_constructor_31.f90: New test.

""",
u"""

	PR tree-optimization/40081
	* tree-sra.c (instantiate_element): Instantiate scalar replacements
	using the main variant of the element type.  Do not fiddle with
	TREE_THIS_VOLATILE or TREE_SIDE_EFFECTS.

	* g++.dg/torture/pr40081.C: New testcase.

""",
u"""

	PR fortran/38863
	* trans-expr.c (gfc_conv_operator_assign): Remove function.
	* trans.h : Remove prototype for gfc_conv_operator_assign.
	* trans-stmt.c (gfc_conv_elemental_dependencies): Initialize
	derivde types with intent(out).
	(gfc_trans_call): Add mask, count1 and invert arguments. Add
	code to use mask for WHERE assignments.
	(gfc_trans_forall_1): Use new arguments for gfc_trans_call.
	(gfc_trans_where_assign): The gfc_symbol argument is replaced
	by the corresponding code. If this has a resolved_sym, then
	gfc_trans_call is called. The call to gfc_conv_operator_assign
	is removed.
	(gfc_trans_where_2): Change the last argument in the call to
	gfc_trans_where_assign.
	* trans-stmt.h : Modify prototype for gfc_trans_call.
	* trans.c (gfc_trans_code): Use new args for gfc_trans_call.


	PR fortran/38863
	* gfortran.dg/dependency_24.f90: New test.
	* gfortran.dg/dependency_23.f90: Clean up module files.

""",
u"""

        PR fortran/38956
        * gfortran.dg/chmod_1.f90: Don't run on *-*-cygwin*.
        * gfortran.dg/chmod_2.f90: Likewise.
        * gfortran.dg/chmod_3.f90: Likewise.
        * gfortran.dg/open_errors.f90: Likewise.

""",
u"""
Daily bump.
""",
u"""

	PR middle-end/40080
	* cgraphunit.c (cgraph_materialize_all_clones): Do not redirect
	indirect calls; verify cgraph afterwards.

""",
u"""
	PR bootstrap/40082
	* ipa.c (update_inlined_to_pointer): New function.
	(cgraph_remove_unreachable_nodes): Use it.

""",
u"""
	* tree-eh.c (struct leh_state): Remove prev_try.
	(lower_try_finally, lower_catch, lower_eh_filter, lower_cleanup): Do
	not track prev_try.
	* except.c (gen_eh_region_cleanup, duplicate_eh_regions, 
	copy_eh_region_1, copy_eh_region, redirect_eh_edge_to_label,
	remove_eh_handler_and_replace, foreach_reachable_handler,
	verify_eh_region, verify_eh_tree): Remove tracking of prev_try pointer.
	* except.h (struct eh_region): Remove eh_region_u_cleanup.
	(gen_eh_region_cleanup): Update prototype.

""",
u"""

	* g++.dg/eh/nested-try.C: New test.

	PR middle-end/40043
	* except.c (copy_eh_region): Always set prev_try.
	(redirect_eh_edge_to_label): Find outer try.
	(foreach_reachable_handler): When looking for prev try
	handle case where previous try is not going to be taken.

""",
u"""
Fix even more formatting.

""",
u"""
Fix more formatting
""",
u"""
Fix formatting
""",
u"""
Daily bump.
""",
u"""
Update test to use __BIGGEST_ALIGNMENT__
""",
u"""
Fix PR 40049
""",
u"""
	* fold-const.c (fold_binary): Do not fold multiplication by 1 or
	-1 for complex floating-point types if honoring signed zeros.

testsuite:
	* gcc.dg/torture/complex-sign-mul-minus-one.c,
	gcc.dg/torture/complex-sign-mul-one.c: New tests.

""",
u"""
	* cgraphbuild.c (compute_call_stmt_bb_frequency): Accept function argument;
	handle correctly when profile is absent.
	(build_cgraph_edges): Update.
	(rebuild_cgraph_edges): Update.
	* cgraph.c: Do not include varrau.h 
	(cgraph_set_call_stmt_including_clones, cgraph_create_edge_including_clones):
	New function
	(cgraph_update_edges_for_call_stmt_node): New stati cfunction.
	(cgraph_update_edges_for_call_stmt): Handle clones.
	(cgraph_remove_node): Handle clone tree.
	(cgraph_remove_node_and_inline_clones): New function.
	(dump_cgraph_node): Dump clone tree.
	(cgraph_clone_node): Handle clone tree.
	(clone_function_name): Bring here from tree-inline.c
	(cgraph_create_virtual_clone): New function.
	* cgraph.h (ipa_replace_map): Move ehre from ipa.h
	(cgraph_clone_info): New function
	(strut cgraph_node): Add clone_info and new clone tree pointers.
	(cgraph_remove_node_and_inline_clones, cgraph_set_call_stmt_including_clones,
	cgraph_create_edge_including_clones, cgraph_create_virtual_clone): Declare.
	(cgraph_function_versioning): Use VEC argument.
	(compute_call_stmt_bb_frequency): Update prototype.
	(cgraph_materialize_all_clones): New function.
	* ipa-cp.c (ipcp_update_cloned_node): Remove.
	(ipcp_create_replace_map): Update to VECtors.
	(ipcp_update_callgraph): Use virtual clones.
	(ipcp_update_bb_counts, ipcp_update_edges_counts): Remove.
	(ipcp_update_profiling): Do not update local profiling.
	(ipcp_insert_stage): Use VECtors and virtual clones.
	* cgraphunit.c (verify_cgraph_node): Verify clone tree.
	(clone_of_p): New function.
	(cgraph_preserve_function_body_p): Use clone tree.
	(cgraph_optimize): Materialize clones.
	(cgraph_function_versioning): Update for VECtors.
	(save_inline_function_body): Use clone tree.
	(cgraph_materialize_clone, cgraph_materialize_all_clones): New functions.
	* ipa-inline.c (cgraph_default_inline_p): Use analyzed flags.
	* ipa.c: Include gimple.h.
	(cgraph_remove_unreachable_nodes): Use clone tree.
	* ipa-prop.c (ipa_note_param_call): Update call of compute_call_stmt_bb_frequency.
	* ipa-prop.h (ipa_replace_map): Move to cgraph.h.
	* tree-inline.c: Do not include varray.h; do not include gt-tree-inline.h
	(copy_bb): Handle updating of clone tree; add new edge when new call
	appears.
	(expand_call_inline): Be strict about every call having edge.
	(clone_fn_id_num, clone_function_name): Move to cgraph.c.
	(delete_unreachable_blocks_update_callgraph): New function.
	(tree_function_versioning): Use VECtors; always remove unreachable blocks
	and fold conditionals.
	* tree-inline.h: Do not include varray.h
	(tree_function_versioning): Remove.
	* Makefile.in (GTFILES): Remove tree-inline.c
	* passes.c (do_per_function): Do only functions having body.
	* ipa-struct-reorg.c (do_reorg_1, collect_data_accesses): Handle cone tree.

""",
u"""
gcc/


	PR c/36892
	* c-common.c (c_common_attribute_table): Permit deprecated
	attribute to take an optional argument.
	(handle_deprecated_attribute): If the optional argument to
	__attribute__((deprecated)) is not a string ignore the attribute
	and emit a warning.

	* c-decl.c (grokdeclarator): Updated warn_deprecated_use call.
	* c-typeck.c (build_component_ref): Likewise.
	(build_external_ref): Likewise.

	* toplev.c (warn_deprecated_use): Add an attribute argument.
	Emit the message associated with __attribute__((deprecated)).

	* toplev.h (warn_deprecated_use): Updated.

	* doc/extend.texi: Document new optional parameter to
	__attribute__((deprecated))

gcc/cp/


	PR c/36892
	* call.c (build_call_a): Updated warn_deprecated_use call.
	(build_over_call): Likewise.
	* decl.c (grokdeclarator): Likewise.
	(grokparms): Likewise.
	* semantics.c (finish_id_expression): Likewise.
	* typeck.c (build_class_member_access_expr): Likewise.
	(finish_class_member_access_expr): Likewise.

gcc/testsuite/


	PR c/36892
	* g++.dg/warn/deprecated-6.C: New.
	* gcc.dg/deprecated-4.c: Likewise.
	* gcc.dg/deprecated-5.c: Likewise.
	* gcc.dg/deprecated-6.c: Likewise.

""",
u"""
Fix bug in movdf_softfloat32.


""",
u"""

	* gcc.dg/vect/no-vfa-vect-37.c: Replace __aligned__(16) with
	__aligned__(__BIGGEST_ALIGNMENT__).
	* gcc.dg/vect/no-vfa-vect-43.c: Likewise.
	* gcc.dg/vect/no-vfa-vect-49.c: Likewise.
	* gcc.dg/vect/no-vfa-vect-53.c: Likewise.
	* gcc.dg/vect/no-vfa-vect-57.c: Likewise.
	* gcc.dg/vect/no-vfa-vect-61.c: Likewise.
	* gcc.dg/vect/no-vfa-vect-79.c: Likewise.
	* gcc.dg/vect/Os-vect-95.c: Likewise.
	* gcc.dg/vect/pr20122.c: Likewise.
	* gcc.dg/vect/pr36493.c: Likewise.
	* gcc.dg/vect/pr37385.c: Likewise.
	* gcc.dg/vect/slp-7.c: Likewise.
	* gcc.dg/vect/slp-9.c: Likewise.
	* gcc.dg/vect/slp-widen-mult-s16.c: Likewise.
	* gcc.dg/vect/slp-widen-mult-u8.c: Likewise.
	* gcc.dg/vect/vect-35.c: Likewise.
	* gcc.dg/vect/vect-40.c: Likewise.
	* gcc.dg/vect/vect-42.c: Likewise.
	* gcc.dg/vect/vect-44.c: Likewise.
	* gcc.dg/vect/vect-46.c: Likewise.
	* gcc.dg/vect/vect-48.c: Likewise.
	* gcc.dg/vect/vect-52.c: Likewise.
	* gcc.dg/vect/vect-54.c: Likewise.
	* gcc.dg/vect/vect-56.c: Likewise.
	* gcc.dg/vect/vect-58.c: Likewise.
	* gcc.dg/vect/vect-60.c: Likewise.
	* gcc.dg/vect/vect-74.c: Likewise.
	* gcc.dg/vect/vect-75.c: Likewise.
	* gcc.dg/vect/vect-76.c: Likewise.
	* gcc.dg/vect/vect-77-alignchecks.c: Likewise.
	* gcc.dg/vect/vect-77.c: Likewise.
	* gcc.dg/vect/vect-77-global.c: Likewise.
	* gcc.dg/vect/vect-78-alignchecks.c: Likewise.
	* gcc.dg/vect/vect-78.c: Likewise.
	* gcc.dg/vect/vect-78-global.c: Likewise.
	* gcc.dg/vect/vect-80.c: Likewise.
	* gcc.dg/vect/vect-85.c: Likewise.
	* gcc.dg/vect/vect-87.c: Likewise.
	* gcc.dg/vect/vect-88.c: Likewise.
	* gcc.dg/vect/vect-92.c: Likewise.
	* gcc.dg/vect/vect-93.c: Likewise.
	* gcc.dg/vect/vect-95.c: Likewise.
	* gcc.dg/vect/vect-97.c: Likewise.
	* gcc.dg/vect/vect-complex-1.c: Likewise.
	* gcc.dg/vect/vect-complex-4.c: Likewise.
	* gcc.dg/vect/vect-complex-5.c: Likewise.
	* gcc.dg/vect/vect-multitypes-10.c: Likewise.
	* gcc.dg/vect/vect-multitypes-11.c: Likewise.
	* gcc.dg/vect/vect-multitypes-12.c: Likewise.
	* gcc.dg/vect/vect-multitypes-13.c: Likewise.
	* gcc.dg/vect/vect-multitypes-14.c: Likewise.
	* gcc.dg/vect/vect-multitypes-15.c: Likewise.
	* gcc.dg/vect/vect-multitypes-16.c: Likewise.
	* gcc.dg/vect/vect-multitypes-17.c: Likewise.
	* gcc.dg/vect/vect-multitypes-3.c: Likewise.
	* gcc.dg/vect/vect-multitypes-6.c: Likewise.
	* gcc.dg/vect/vect-multitypes-7.c: Likewise.
	* gcc.dg/vect/vect-multitypes-8.c: Likewise.
	* gcc.dg/vect/vect-multitypes-9.c: Likewise.
	* gcc.dg/vect/vect-outer-1a.c: Likewise.
	* gcc.dg/vect/vect-outer-1.c: Likewise.
	* gcc.dg/vect/vect-outer-2a.c: Likewise.
	* gcc.dg/vect/vect-outer-2b.c: Likewise.
	* gcc.dg/vect/vect-outer-2.c: Likewise.
	* gcc.dg/vect/vect-outer-2c.c: Likewise.
	* gcc.dg/vect/vect-outer-2d.c: Likewise.
	* gcc.dg/vect/vect-outer-3a.c: Likewise.
	* gcc.dg/vect/vect-outer-3b.c: Likewise.
	* gcc.dg/vect/vect-outer-3.c: Likewise.
	* gcc.dg/vect/vect-outer-3c.c: Likewise.
	* gcc.dg/vect/vect-outer-5.c: Likewise.
	* gcc.dg/vect/vect-outer-6.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-s16a.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-s16b.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-s8a.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-s8b.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-s8c.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-u16a.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-u16b.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-u8a.c: Likewise.
	* gcc.dg/vect/vect-reduc-dot-u8b.c: Likewise.
	* gcc.dg/vect/vect-widen-mult-s16.c: Likewise.
	* gcc.dg/vect/vect-widen-mult-s8.c: Likewise.
	* gcc.dg/vect/vect-widen-mult-u16.c: Likewise.
	* gcc.dg/vect/vect-widen-mult-u8.c: Likewise.
	* gcc.dg/vect/wrapv-vect-reduc-dot-s8b.c: Likewise.

""",
u"""

	PR tree-optimization/40062
	* tree-scalar-evolution.c (follow_ssa_edge_in_condition_phi):
	Avoid exponential behavior.

""",
u"""

	PR rtl-optimization/33928
	PR 26854
	* fwprop.c (use_def_ref, get_def_for_use, bitmap_only_bit_bitween,
	process_uses, build_single_def_use_links): New.
	(update_df): Update use_def_ref.
	(forward_propagate_into): Use get_def_for_use instead of use-def
	chains.
	(fwprop_init): Call build_single_def_use_links and let it initialize
	dataflow.
	(fwprop_done): Free use_def_ref.
	(fwprop_addr): Eliminate duplicate call to df_set_flags.
	* df-problems.c (df_rd_simulate_artificial_defs_at_top, 
	df_rd_simulate_one_insn): New.
	(df_rd_bb_local_compute_process_def): Update head comment.
	(df_chain_create_bb): Use the new RD simulation functions.
	* df.h (df_rd_simulate_artificial_defs_at_top, 
	df_rd_simulate_one_insn): New.
	* opts.c (decode_options): Enable fwprop at -O1.
	* doc/invoke.texi (-fforward-propagate): Document this.

""",
u"""
	PR c/24581
	* c-typeck.c (build_binary_op): Handle arithmetic between one real
	and one complex operand specially.
	* tree-complex.c (some_nonzerop): Do not identify a real value as
	zero if flag_signed_zeros.

testsuite:
	* gcc.dg/torture/complex-sign.h: New header.
	* gcc.dg/torture/complex-sign-add.c,
	gcc.dg/torture/complex-sign-mixed-add.c,
	gcc.dg/torture/complex-sign-mixed-div.c,
	gcc.dg/torture/complex-sign-mixed-mul.c,
	gcc.dg/torture/complex-sign-mixed-sub.c,
	gcc.dg/torture/complex-sign-mul.c,
	gcc.dg/torture/complex-sign-sub.c: New tests.

""",
u"""

	PR fortran/39876
	* intrinsic.c (gfc_is_intrinsic): Do not add the EXTERNAL attribute if
	the symbol is a module procedure.



	PR fortran/39876
	* gfortran.dg/intrinsic_3.f90: New.


""",
u"""

	PR rtl-optimization/33928
        * loop-invariant.c (record_use): Fix && vs. || mishap.


""",
u"""

	PR rtl-optimization/33928
        * loop-invariant.c (struct use): Add addr_use_p.
        (struct def): Add n_addr_uses.
        (struct invariant): Add cheap_address.
        (create_new_invariant): Set cheap_address.
        (record_use): Accept df_ref.  Set addr_use_p and update n_addr_uses.
        (record_uses): Pass df_ref to record_use.
        (get_inv_cost): Do not add inv->cost to comp_cost for cheap addresses used
	only as such.


""",
u"""

       * invoke.texi: Add do/recursion to the -fcheck= summary.


""",
u"""
	* config/sh/sh.c: Do not include c-pragma.h.


""",
u"""

        * config/spu/spu.c: Remove include of c-common.h.


""",
u"""

	* include/ext/throw_allocator.h: Remove redundante include.

""",
u"""

	* include/ext/throw_allocator.h (throw_allocator_base): Avoid
	out of line member functions definitions.
	(throw_allocator_base::_S_g, _S_map, _S_throw_prob, _S_label):
	Remove, use static locals instead.
	(throw_allocator_base::do_check_allocated, print_to_string): Declare.
	* src/throw_allocator.cc: New.
	* src/Makefile.am: Add.
	* config/abi/pre/gnu.ver: Add exports.
	* src/Makefile.in: Regenerate.

""",
u"""
Daily bump.
""",
u"""
gcc/
	PR c/39037
	* c-common.h (mark_valid_location_for_stdc_pragma,
	valid_location_for_stdc_pragma_p, set_float_const_decimal64,
	clear_float_const_decimal64, float_const_decimal64_p): New.
	* c.opt (Wunsuffixed-float-constants): New.
	* c-lex.c (interpret_float): Use pragma FLOAT_CONST_DECIMAL64 for
	unsuffixed float constant, handle new warning.
	* c-cppbuiltin.c (c_cpp_builtins): Use cast for double constants.
	* c-decl.c (c_scope): New flag float_const_decimal64.
	(set_float_const_decimal64, clear_float_const_decimal64,
	float_const_decimal64_p): New.
	(push_scope): Set new flag.
	* c-parser.c (c_parser_translation_unit): Mark when it's valid
	to use STDC pragmas.
	(c_parser_external_declaration): Ditto.
	(c_parser_compound_statement_nostart): Ditto.
	* c-pragma.c (valid_location_for_stdc_pragma,
	mark_valid_location_for_stdc_pragma,
	valid_location_for_stdc_pragma_p, handle_stdc_pragma,
	handle_pragma_float_const_decimal64): New.
	(init_pragma): Register new pragma FLOAT_CONST_DECIMAL64.
	* cp/semantics.c (valid_location_for_stdc_pragma_p,
	set_float_const_decimal64, clear_float_const_decimal64,
	float_const_decimal64_p): New dummy functions.
	* doc/extend.texi (Decimal Float): Remove statement that the
	pragma, and suffix for double constants, are not supported.
	* doc/invoke.texi (Warning Options): List new option.
	(-Wunsuffixed-float-constants): New.

gcc/testsuite
	PR c/39037
	* gcc.dg/Wunsuffixed-float-constants-1.c: New test.
	* gcc.dg/cpp/pragma-float-const-decimal64-1.c: New test.
	* gcc.dg/dfp/float-constant-double.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-1.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-2.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-3.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-4.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-5.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-6.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-7.c: New test.
	* gcc.dg/dfp/pragma-float-const-decimal64-8.c: New test.
	* g++.dg/cpp/pragma-float-const-decimal64-1.C: New test.

""",
u"""
	PR fortran/38830
	* gfortran.texi: Document that we don't support variable FORMAT
	expressions.

""",
u"""
	PR fortran/39576
	* error.c (error_print): Add missing break statement.

""",
u"""
	PR fortran/36382
	* invoke.texi: Document that -fdollar-ok does not allow $ to be
	used in IMPLICIT statement.

""",
u"""
	PR fortran/22423

	* io/transfer.c (read_block_direct): Avoid warning.
	* runtime/string.c (compare0): Avoid warning.

""",
u"""
	* config/i386/i386.c: Do not include c-common.h.

""",
u"""

	* doc/invoke.texi (Debugging Options): Document change of debugging
	dump location.
        * opts.c (decode_options): Make dump_base_name relative to
	aux_base_name directory.


""",
u"""
* config/picochip/picochip.h (NO_DOLLAR_IN_LABEL): Added.
* config/picochip/libgccExtras/divmod15.asm : Removed redefiniton.


""",
u"""

	* Makefile.in (install-plugin): Simplify a bit.


""",
u"""

	* Makefile.in (OBJS-common): Add regcprop.o.
	(regcprop.o): New.
	* timevar.def (TV_CPROP_REGISTERS): New.
	* regrename.c (regrename_optimize): Return 0.
	(rest_of_handle_regrename): Delete.
	(pass_rename_registers): Point to regrename_optimize.
	(struct value_data_entry, struct value_data, 
	kill_value_one_regno, kill_value_regno, kill_value,
	set_value_regno, init_value_data, kill_clobbered_value,
	kill_set_value, kill_autoinc_value, copy_value,
	mode_change_ok, maybe_mode_change, find_oldest_value_reg,
	replace_oldest_value_reg, replace_oldest_value_addr,
	replace_oldest_value_mem, copyprop_hardreg_forward_1,
	debug_value_data, validate_value_data): Move...
	* regcprop.c: ... here.
	(rest_of_handle_cprop): Delete.
	(pass_cprop_hardreg): Point to copyprop_hardreg_forward.


""",
u"""
	PR middle-end/40057
	* dojump.c (prefer_and_bit_test): Use immed_double_const instead of
	GEN_INT for 1 << bitnum.
	(do_jump) <case BIT_AND_EXPR>: Use build_int_cst_wide_type instead of
	build_int_cst_type.

	* gcc.c-torture/execute/pr40057.c: New test.

""",
u"""

	* configure.ac: Bump libtool_VERSION to 6:12:0.
	* configure: Regenerate.

""",
u"""
	* gcc-interface/Make-lang.in: Update dependencies

""",
u"""

	* config.guess: Sync with src.

config:
2009-05-07  Paolo Bonzini

	Sync from src:

	* tcl.m4 (SC_PATH_TCLCONFIG): Don't exit 0 if tclconfig fails.
	(SC_PATH_TKCONFIG): Don't exit 0 if tkconfig fails.
	(SC_LOAD_TCLCONFIG): Quote all uses of TCL_BIN_DIR, it may contain
	"# no Tcl configs found".
	(SC_LOAD_TKCONFIG): Similarily for TK_BIN_DIR.

""",
u"""
	* doc/md.texi (Standard Pattern Names For Generation) [sync_nand]:
	Remove wrong description of "nand" functionality.


""",
u"""
	* ChangeLog: Whitespace fixes.
	* testsuite/ChangeLog: Ditto.

""",
u"""

	PR libstdc++/40038
	* src/math_stubs_long_double.cc: Add ceill.

""",
u"""
	* configure.ac ($with_ppl):  Default to no if not supplied.
	($with_cloog):  Likewise.
	configure:  Regenerate.


""",
u"""
Correct changelog from last checkin, cut-n-paste from wrong patch file.
* gcc.c-torture/compile/const-high-part.c: New test.

""",
u"""
* gcc.target/mips/const-high-part.c: New test.

""",
u"""
Daily bump.
""",
u"""
	* gimple.def (GIMPLE_ASSIGN): Fix incorrect information in the
	comment.  Add that if LHS is not a gimple register, then RHS1 has
	to be a single object (GIMPLE_SINGLE_RHS).

""",
u"""

	PR testsuite/40050
	* lib/plugin-support.exp (plugin-test-execute): Use HOSTCC to
	build plugin.

""",
u"""

        * s-linux.ads, s-linux-alpha.ads, s-linux-hppa.ads, 
        osinte-linux.ads: Define sa_handler_pos.
        * s-osinte-linux.ads: Use it.
        * s-linux-mipsel.ads: New.	
        * system-linux-mips64el.ads: New.
        * gcc-interface/Makefile.in: Multilib handling for
        mipsel-linux and mips64el-linux.
	

""",
u"""

	PR fortran/39630
	* decl.c (match_procedure_interface): New function to match the
	interface for a PROCEDURE statement.
	(match_procedure_decl): Call match_procedure_interface.
	(match_ppc_decl): New function to match the declaration of a
	procedure pointer component.
	(gfc_match_procedure):  Call match_ppc_decl.
	(match_binding_attributes): Add new argument 'ppc' and handle the
	POINTER attribute for procedure pointer components.
	(match_procedure_in_type,gfc_match_generic): Added new argument to
	match_binding_attributes.
	* dump-parse-tree.c (show_expr,show_components,show_code_node): Handle
	procedure pointer components.
	* expr.c (free_expr0,gfc_copy_expr,gfc_simplify_expr): Handle EXPR_PPC.
	(gfc_check_pointer_assign): Handle procedure pointer components, but no
	full checking yet.
	(is_proc_ptr_comp): New function to determine if an expression is a
	procedure pointer component.
	* gfortran.h (expr_t): Add EXPR_PPC.
	(symbol_attribute): Add new member 'proc_pointer_comp'.
	(gfc_component): Add new member 'formal'.
	(gfc_exec_op): Add EXEC_CALL_PPC.
	(gfc_get_default_type): Changed first argument.
	(is_proc_ptr_comp): Add prototype.
	(gfc_match_varspec): Add new argument.
	* interface.c (compare_actual_formal): Handle procedure pointer
	components.
	* match.c (gfc_match_pointer_assignment,match_typebound_call): Handle
	procedure pointer components.
	* module.c (mio_expr): Handle EXPR_PPC.
	* parse.c (parse_derived): Handle procedure pointer components.
	* primary.c (gfc_match_varspec): Add new argument 'ppc_arg' and handle
	procedure pointer components.
	(gfc_variable_attr): Handle procedure pointer components.
	(gfc_match_rvalue): Added new argument to gfc_match_varspec and changed
	first argument of gfc_get_default_type.
	(match_variable): Added new argument to gfc_match_varspec.
	* resolve.c (resolve_entries,set_type,resolve_fl_parameter): Changed
	first argument of gfc_get_default_type.
	(resolve_structure_cons,resolve_actual_arglist): Handle procedure
	pointer components.
	(resolve_ppc_call): New function to resolve a call to a procedure
	pointer component (subroutine).
	(resolve_expr_ppc): New function to resolve a call to a procedure
	pointer component (function).
	(gfc_resolve_expr): Handle EXPR_PPC.
	(resolve_code): Handle EXEC_CALL_PPC.
	(resolve_fl_derived): Copy the interface for a procedure pointer
	component.
	(resolve_symbol): Fix overlong line.
	* st.c (gfc_free_statement): Handle EXEC_CALL_PPC.
	* symbol.c (gfc_get_default_type): Changed first argument.
	(gfc_set_default_type): Changed first argument of gfc_get_default_type.
	(gfc_add_component): Initialize ts.type to BT_UNKNOWN.
	* trans.h (gfc_conv_function_call): Renamed.
	* trans.c (gfc_trans_code): Handle EXEC_CALL_PPC.
	* trans-expr.c (gfc_conv_component_ref): Ditto.
	(gfc_conv_function_val): Rename to 'conv_function_val', add new
	argument 'expr' and handle procedure pointer components.
	(gfc_conv_operator_assign): Renamed gfc_conv_function_val.
	(gfc_apply_interface_mapping_to_expr): Handle EXPR_PPC.
	(gfc_conv_function_call): Rename to 'gfc_conv_procedure_call', add new
	argument 'expr' and handle procedure pointer components.
	(gfc_get_proc_ptr_comp): New function to get the backend decl for a
	procedure pointer component.
	(gfc_conv_function_expr): Renamed gfc_conv_function_call.
	(gfc_conv_structure): Handle procedure pointer components.
	* trans-intrinsic.c (gfc_conv_intrinsic_funcall,
	conv_generic_with_optional_char_arg): Renamed gfc_conv_function_call.
	* trans-stmt.h (gfc_get_proc_ptr_comp): Add prototype.
	* trans-stmt.c (gfc_trans_call): Renamed gfc_conv_function_call.
	* trans-types.h (gfc_get_ppc_type): Add prototype.
	* trans-types.c (gfc_get_ppc_type): New function to build a tree node
	for a procedure pointer component.
	(gfc_get_derived_type): Handle procedure pointer components.



	PR fortran/39630
	* gfortran.dg/proc_decl_1.f90: Modified.
	* gfortran.dg/proc_ptr_comp_1.f90: New.
	* gfortran.dg/proc_ptr_comp_2.f90: New.
	* gfortran.dg/proc_ptr_comp_3.f90: New.
	* gfortran.dg/proc_ptr_comp_4.f90: New.
	* gfortran.dg/proc_ptr_comp_5.f90: New.
	* gfortran.dg/proc_ptr_comp_6.f90: New.


""",
u"""
	* expr.c (get_def_for_expr): Move it up in the file.
	(store_field): When expanding a bit-field store, look at the
	defining gimple stmt for the masking conversion.

""",
u"""

    gcc/cp/ChangeLog:
    	PR c++/17395
    	* pt.c (tsubst_copy) <case PARM_DECL>: We don't want to tsubst the
    	whole list of PARM_DECLs, just the current one.
    
    gcc/testsuite/ChangeLog:
    	PR c++/17395
    	* g++.dg/template/call7.C: New test.

""",
u"""
Remove extra '('.

""",
u"""

	* lib/plugin-support.exp: Do not prefix $GMPINC with -I.



""",
u"""

	* gfortran.dg/pr40021.f: Moved to ...
	* gfortran.fortran-torture/execute/pr40021.f: Here.

""",
u"""
	PR middle-end/39986
	* dfp.c (encode_decimal32, decode_decimal32, encode_decimal64,
	decode_decimal64, encode_decimal128, decode_decimal128): Avoid
	32-bit memcpy into long.

	* gcc.dg/dfp/pr39986.c: New test.

""",
u"""
	* dwarf2out.c (new_reg_loc_descr): Don't ever create DW_OP_regX.
	(one_reg_loc_descriptor): Create DW_OP_regX here instead of calling
	new_reg_loc_descr.
	(loc_by_reference): If loc is DW_OP_regX, change it into DW_OP_bregX 0
	instead of appending DW_OP_deref*.

""",
u"""
        PR middle-end/40021
        * cfgexpand.c (maybe_cleanup_end_of_block): New static function.
        (expand_gimple_cond): Use it to cleanup CFG and superfluous jumps.

        * gfortran.dg/pr40021.f: New test.

""",
u"""

	* lib/plugin-support.exp: New file containing support procs for
	plugin testcases.
	* lib/target-supports.exp (check_plugin_available): New proc.
	* gcc.dg/plugin/plugin.exp: New driver script for gcc testcases.
	* gcc.dg/plugin/selfassign.c: New plugin source file.
	* gcc.dg/plugin/self-assign-test-1.c: New test.
	* gcc.dg/plugin/self-assign-test-2.c: Likewise.
	* g++.dg/README: Add description for plugin test.
	* g++.dg/dg.exp: Exclude plugin tests from the general test list.
	* g++.dg/plugin/plugin.exp: New driver script for g++ testcases.
	* g++.dg/plugin/selfassign.c: New plugin source file.
	* g++.dg/plugin/self-assign-test-1.C: New test.
	* g++.dg/plugin/self-assign-test-2.C: Likewise.
	* g++.dg/plugin/self-assign-test-3.C: Likewise.
	* g++.dg/plugin/dumb_plugin.c: New plugin source file.
	* g++.dg/plugin/dumb-plugin-test-1.C: New test.



""",
u"""

        PR fortran/40041
        * resolve.c (resolve_symbol): Print no warning for implicitly
        typed intrinsic functions.


        PR fortran/40041
        * gfortran.dg/intrinsic_2.f90: New test.
        * gfortran.dg/intrinsic.f90: Add old and this PR as comment.


""",
u"""

	* sem_attr.adb: Add processing for Standard'Compiler_Version


	* exp_ch5.adb, exp_util.adb, exp_attr.adb, sem_util.adb, sem_res.adb,
	targparm.adb, targparm.ads, exp_ch4.adb, exp_ch6.adb, exp_disp.adb,
	opt.ads, exp_aggr.adb, exp_intr.adb, sem_disp.adb, exp_ch3.adb
	(Tagged_Type_Expansion): New flag.
	Replace use of VM_Target related to tagged types expansion by
	Tagged_Type_Expansion, since tagged type expansion is not necessarily
	linked to VM targets.


""",
u"""

	* sinput.adb (Expr_Last_Char): Fix some copy-paste errors for paren
	skipping.
	(Expr_First_Char): Add ??? comment that paren skipping needs work
	(Expr_Last_Char): Add ??? comment that paren skipping needs work

	* exp_attr.adb: Add processing for Compiler_Version

	* sem_attr.adb: New attribute Compiler_Version

	* snames.ads-tmpl: Add entries for Compiler_Version attribute

	* gnat_rm.texi: Document Compiler_Version attribute


""",
u"""

	* Makefile.in (install-plugin): Fix srcdir handling.


""",
u"""
        * tree-ssa.c (execute_update_address_taken): Handle TARGET_MEM_REF
        when processing for not_regs_needed bitmap.
        * gimple.c (walk_stmt_load_store_addr_ops): When visiting address,
        handle TARGET_MEM_REF in lhs.  Check TMR_BASE for NULL while
        handling it for rhs.


""",
u"""

	* config/i386/i386.md ((unnamed inc/dec peephole): Use
	optimize_insn_for_size_p instead
	of optimize_size.
	* config/i386/predicates.md (incdec_operand): Likewise.
	(aligned_operand): Likewise.
	* config/i386/sse.md (divv8sf3): Likewise.
	(sqrtv8sf2): Likewise.

""",
u"""

	* config/i386/i386.c (ix86_build_signbit_mask): Make it static.

	* config/i386/i386-protos.h (ix86_build_signbit_mask): Removed.

""",
u"""

	* config/i386/i386.md (*avx_<code><mode>3_finite): Replace
	ssemodesuffixf2c with avxmodesuffixf2c.

""",
u"""
	PR c/40032
	* c-decl.c (grokdeclarator): Handle incomplete type of unnamed
	field.

testsuite:
	* gcc.dg/noncompile/incomplete-5.c: New test.

""",
u"""

	* errout.adb: Minor reformatting

	* scng.adb, sem_prag.adb, par-ch4.adb, sem_res.adb, par-ch6.adb,
	sem_ch6.adb, par-prag.adb, sem_ch8.adb, sem_warn.adb, par-util.adb,
	styleg.adb: Add stylized comments to error messages that are included
	in the codefix circuitry of IDE's such as GPS.


""",
u"""

	* gnat_ugn.texi: For Misnamed_Identifiers rule all description of the
	new form of the rule parameter that allows to specify the suffix for
	access-to-access type names.


	* sem_warn.adb (Warn_On_Useless_Assignment): Avoid false negative for
	out parameter assigned when exception handlers are present.

	* sem_ch5.adb (Analyze_Exit_Statement): Kill current value last
	assignments on exit.

	* par-ch9.adb, sem_aggr.adb, par-endh.adb, sem_res.adb, par-ch6.adb,
	sinput-l.adb, par-load.adb, errout.ads, sem_ch4.adb, lib-load.adb,
	prj-dect.adb, par-ch12.adb, sem_ch8.adb, par-util.adb, par-ch3.adb,
	par-tchk.adb, par-ch5.adb: This patch adds stylized comments to error
	messages that are included in the codefix circuitry of IDE's such as
	GPS.

	* sinput.ads, sinput.adb (Expr_First_Char): New function
        (Expr_Last_Char): New function


""",
u"""

	* gnat_ugn.texi: Add subsection for Exits_From_Conditional_Loops rule
	Add formal definition for extra exit point metric


	* adaint.c: Support for setting attributes on unicode filename on
	Windows.


""",
u"""

	* sem_warn.adb: Minor reformatting


	* sem_prag.adb (Process_Import_Or_Interface): Imported CPP types must
	not have discriminants or components with default expressions.
	(Analyze_Pragma): For pragma CPP_Class check that imported types
	have no discriminants and components have no default expression.

	* sem_aggr.adb (Resolve_Aggr_Expr): Add missing check on wrong use of
	class-wide types in the expression of a record component association.


	* vms_data.ads: Add qualifier for gnatmetric extra exit points metric

	* gnat_ugn.texi: Add description for the new extra exit points metric
	(gnatmetric section).


""",
u"""

        PR libstdc++/39546
        * include/parallel/algo.h (find_switch):
        Parametrize binder2nd with const T& instead of T.
        * testsuite/25_algorithms/find/39546.cc: new test case


""",
u"""
Minor reformatting.

""",
u"""

	* s-fileio.adb: Minor comment update

	* sem_ch8.adb: Minor reformatting

	* exp_ch3.adb: Update comments.


	* init.c, s-osinte-darwin.ads: Reduce alternate stack size


""",
u"""
Revert previous change.

""",
u"""
	* gcc-interface/Makefile.in: Update LIBGNAT_TARGET_PAIRS for Xenomai.
	Fix missing unit for rtp-smp runtime on both ppc and x86 vxworks

	* gcc-interface/Make-lang.in: Update dependencies


""",
u"""

	* sem_ch12.adb (Build_Instance_Compilation_Unit_Nodes): Revert previous
	change. The context clause of a generic instance declaration must be
	preserved until the end of the compilation, because it may have to be
	installed/removed repeatedly.
	The latest change to sem.adb ensures that the context of both spec and
	body of an instance is traversed before the instance itself, making
	this patch redundant.


	* sem_aggr.adb: Minor code clean-up


""",
u"""

	* sem_aggr.adb: Fix typo.


	* exp_ch3.adb (Expand_N_Object_Declaration): For a controlled object
	declaration, do not adjust if the declaration is to be rewritten into
	a renaming.


	* sem_ch8.adb (Find_Type): Reject the use of a task type in its own
	discriminant part.


	* s-fileio.adb (File_IO_Clean_Up_Type): Make this type limited, since
	otherwise the compiler would be allowed to optimize away the cleanup
	code.


""",
u"""

	* gnat_ugn.texi: Fix typo.


	* g-debuti.adb: Minor reformatting

	* exp_attr.adb: Minor reformatting


	* sem_aggr.adb: Minor reformatting.

	* g-socthi-vms.adb: Minor reformatting


	* g-table.ads, g-table.adb, g-dyntab.ads, g-dyntab.adb:
	(Append_All): Add Append_All to g-table and g-dyntab, similar to table.


""",
u"""

	* gnat_ugn.texi, gnat_rm.texi: Add missing documentation for warnings
	flags.


""",
u"""

	* sem_aggr.adb (Valid_Ancestor_Type): Add support for C++ constructors.
	(Resolve_Extension_Aggregate): Do not reject C++ constructors in
	extension aggregates.
	(Resolve_Record_Aggregate): Add support for C++ constructors in
	extension aggregates.

	* exp_aggr.adb (Build_Record_Aggr_Code): Add support for C++
	constructors in extension aggregates.


""",
u"""

	* freeze.adb (Freeze_Record_Type): Improve error msg for bad size
	clause.


	* g-socthi-vms.adb (C_Recvmsg, C_Sendmsg): Convert Msg to appropriate
	packed type, since on OpenVMS, struct msghdr is packed.


	* sem_ch8.adb (Analyze_Object_Renaming): If the object is a function
	call returning an unconstrained composite value, create the proper
	subtype for it, as is done for object dclarations with unconstrained
	nominal subtypes. Perform this transformation regarless of whether
	call comes from source.


""",
u"""

	* freeze.adb (Freeze_Record_Type): Implement Implicit_Packing for
	records

	* gnat_rm.texi:
	Add documentation for pragma Implicit_Packing applied to record
	types.


	* sem.adb (Walk_Library_Items): Place all with_clauses of an
	instantiation on the spec, because late instance bodies may generate
	with_clauses for the instance body but are inserted in the instance
	spec.


""",
u"""

	* prj-nmsc.adb (Locate_Directory): Remove unused parameters, and add
	support for returning the directory even if it doesn't exist. This is
	used for the object directory, since we are always setting it to a
	non-null value, and we should set it to an absolute name rather than a
	relative name for the sake of external tools that might depend on it.
	(Check_Library_Attributes): When Project.Library_Dir is known, check
	that the directory exists.


	* sem_attr.adb (Check_Dereference): If the prefix of an attribute
	reference is an implicit dereference, do not freeze the designated type
	if within a default expression or when preanalyzing a pre/postcondtion.


""",
u"""

	* sem_ch8.adb (Analyze_Object_Renaming): If the object is a function
	call returning an unconstrained composite value, create the proper
	subtype for it, as is done for object dclarations with unconstrained
	nominal subtypes


	* sem_ch13.adb (Check_Constant_Address_Clause): Minor error message
	improvements

	* freeze.adb: Minor reformatting


""",
u"""

	Revert:

	* acinclude.m4 ([GLIBCXX_ENABLE_ATOMIC_BUILTINS]): Do link tests when
	possible.
	* configure: Regenerate.

""",
u"""

	* sem_ch3.adb (Access_Type_Declaration): An access type whose
	designated type is a limited view from a limited with clause (flagged
	From_With_Type) is not itself such a limited view.


	* prj-nmsc.adb: Remove unused variable.

	* clean.adb, gnatcmd.adb, makeutl.ads, prj-pars.adb, prj-pars.ads,
	prj-proc.ads, prj.ads, switch-m.adb (Subdirs_Option): Moved to
	makeutl.ads, since not all users of prj.ads need this.


""",
u"""

	* exp_aggr.adb (Build_Record_Aggr_Code): Add implicit call to the C++
	constructor in case of aggregates whose type is a CPP_Class type.


""",
u"""

	* sem_ch13.adb: Minor comment additions

	* osint.adb: Minor reformatting


	* initialize.c: On Windows, keep full pathname to expanded command
	line patterns.


""",
u"""

	* sem_aggr.adb (Resolve_Record_Aggregate): If a defaulted component of
	an aggregate with box default is of a discriminated private type, do
	not build a subaggregate for it.
	A proper call to the initialization procedure is generated for it.


	* rtsfind.adb, rtsfind.ads, exp_dist.adb, exp_dist.ads
	(Exp_Dist.Build_TC_Call, Build_From_Any_Call, Build_To_Any_Call):
	Use PolyORB strings to represent Ada.Strings.Unbounded_String value;
	use standard array code for Standard.String.
	(Exp_Dist): Bump PolyORB s-parint API version to 3.
	(Rtsfind): New entities TA_Std_String, Unbounded_String.


	* g-comlin.ads: Minor reformatting

	* xoscons.adb: Minor reformatting


""",
u"""

	* sem_aggr.adb (Resolve_Record_Aggregate): In step 5, get the
	Underlying_Type before retrieving the type definition for gathering
	components, to account for the case where the type is private.


	* g-comlin.ads: Fix minor typos (Getopt instead of Get_Opt).


	* g-socthi-vms.adb, g-socthi-vms.ads, g-socthi-vxworks.adb,
	g-socthi-vxworks.ads, g-socthi-mingw.adb g-socthi-mingw.ads,
	g-socthi.adb, g-stsifd-sockets.adb, g-socthi.ads, g-socket.adb
	(GNAT.Sockets.Thin.C_Sendmsg, GNAT.Sockets.Thin.C_Recvmsg,
	Windows versions): Fix incorrect base
	address of Iovec (it's Msg_Iov, not Msg_Iov'Address).
	(GNAT.Sockets.Thin.C_Sendto, GNAT.Sockets.Thin.C_Recvfrom): Use a
	System.Address for the To parameter instead of a Sockaddr_In_Access, to
	achieve independance from AF_INET family, and also to allow this
	parameter to be retrieved from a Msghdr for the Windows case where
	these routines are used to implement C_Sendmsg and C_Recvmsg.


	* g-expect.adb, g-expect.ads: Minor reformatting

	* sdefault.ads: Minor comment fix

	* g-expect-vms.adb: Minor reformatting

	* table.ads, table.adb (Append_All): New convenience procedure for
	appending a whole array.

	* comperr.adb (Compiler_Abort): Mention the -gnatd.n switch in the bug
	box message. Call Osint.Dump_Source_File_Names to print out the file
	list, instead of rummaging around in various data structures.

	* debug.adb: New switch -gnatd.n, to print source file names as they
	are read.

	* alloc.ads: Add parameters for Osint.File_Name_Chars.

	* osint.ads, osint.adb (Dump_Source_File_Names): New procedure to print
	out source file names during a "bug box".
	(Include_Dir_Default_Prefix): Use memo-izing to avoid repeated new/free.
	(Read_Source_File): Print out the file name, if requested via -gnatd.n.
	If it's not part of the runtimes, store it for later printing by
	Dump_Source_File_Names.


	* gnat_rm.texi (CPP_Constructor): Avoid duplication of the
	documentation and add reference to the GNAT user guide for further
	details.


	* gnat_ugn.texi: Complete documentation for CPP_Constructor and remove
	also wrong examples that use extension aggregates.


	* s-oscons-tmplt.c (System.OS_Constants): Do not use special definition
	of Msg_Iovlen_T for VMS.


""",
u"""
Daily bump.
""",
u"""

	PR libstdc++/39909
	* include/std/mutex (__get_once_functor_lock, __get_once_mutex,
	__set_once_functor_lock_ptr): Replace global lock object with local
	locks on global mutex.
	* src/mutex.cc (__get_once_functor_lock, __get_once_mutex,
	__set_once_functor_lock_ptr): Likewise, keeping old function to
	preserve ABI.
	(__once_proxy): Use pointer to local lock if set, global lock
	otherwise.
	* config/abi/pre/gnu.ver: Add new symbols to new ABI version.
	* testsuite/util/testsuite_abi.cc: Add GLIBCX_3.4.12 version.
	* testsuite/30_threads/call_once/39909.cc: New.

""",
u"""
	PR middle-end/39666
	* gimplify.c (gimplify_switch_expr): If case labels cover the whole
	range of the type, but default label is missing, add it with one
	of the existing labels instead of adding a new label for it.

	* gcc.dg/pr39666-1.c: New test.
	* gcc.dg/pr39666-2.c: Likewise.
	* g++.dg/warn/Wuninitialized-4.C: Likewise.
	* g++.dg/warn/Wuninitialized-5.C: Likewise.
	* gfortran.dg/pr39666-1.f90: Likewise.
	* gfortran.dg/pr39666-2.f90: Likewise.

""",
u"""
	* tree.h: Remove DECL_BY_REFERENCE from private_flag comment.
	(struct tree_base): Adjust spacing for 8 bit boundaries.
	(struct tree_decl_common): Add decl_by_reference_flag bit.
	(DECL_BY_REFERENCE): Adjust.
	* print-tree.c (print_node): For VAR_DECL, PARM_DECL or RESULT_DECL,
	print DECL_BY_REFERENCE bit.
	* dbxout.c (DECL_ACCESSIBILITY_CHAR): Revert last change.
	* dwarf2out.c (loc_by_reference, gen_decl_die): Check
	DECL_BY_REFERENCE for all VAR_DECLs, not just non-static ones.
	(gen_variable_die): Likewise.  Check TREE_PRIVATE/TREE_PROTECTED
	unconditionally.

""",
u"""
	* gcc.target/mips/mips.exp: Add -mtune= to mips_option_groups.
	* gcc.target/mips/dspr2-MULT.c: Pass -mtune=74kc
	* gcc.target/mips/dspr2-MULTU.c: Likewise.

""",
u"""

	PR fortran/39998
	* expr.c (gfc_check_pointer_assign): Check for statement functions and
	internal procedures in procedure pointer assignments.



	PR fortran/39998
	* gfortran.dg/proc_ptr_17.f90: New.


""",
u"""

	* cp-tree.h:
       	(opname_tab, assignop_tab, update_member_visibility, yyerror, yyhook,
       	mangle_compound_literal): Remove unused declarations.
       	(build_vfield_ref, cxx_print_statistics, clone_function_decl,
       	adjust_clone_args, maybe_push_cleanup_level, pushtag, make_anon_name,
       	pushdecl_top_level_maybe_friend, pushdecl_top_level_and_finish,
       	check_for_out_of_scope_variable, print_other_binding_stack,
       	maybe_push_decl, cxx_mark_addressable, force_target_expr,
       	build_target_expr_with_type, finish_case_label,
       	cxx_maybe_build_cleanup, begin_eh_spec_block, finish_eh_spec_block,
       	check_template_keyword, cxx_omp_predetermined_sharing,
       	cxx_omp_clause_default_ctor, cxx_omp_clause_copy_ctor,
       	cxx_omp_clause_assign_op, cxx_omp_clause_dtor, cxx_omp_finish_clause,
       	cxx_omp_privatize_by_reference): Rearrange the declarations line to
       	match the comment that indicates the .c file which the functions are
       	defined.
       	(cxx_print_xnode, cxx_print_decl, cxx_print_type,
       	cxx_print_identifier, cxx_print_error_function, pushdecl): Add comment.

""",
u"""
	* dwarf.h: Remove.

""",
u"""

	* Makefile.in (enable_plugin, plugin_includedir): New.
	(install): Depend on install-plugin.
	(PLUGIN_HEADERS): New.
	(install-plugin): New.
	* config.gcc: Add vxworks-dummy.h to tm_file for x86 and x86-64.


""",
u"""

	PR tree-optimization/40022
	* tree-ssa-phiprop.c (struct phiprop_d): Exchange vop_stmt for
	the only vuse.
	(phivn_valid_p): Fix tuplification error, simplify.
	(phiprop_insert_phi): Add dumps.
	(propagate_with_phi): Simplify.

	* gcc.c-torture/execute/pr40022.c: New testcase.

""",
u"""

	PR middle-end/40023
	* builtins.c (gimplify_va_arg_expr): Properly build the
	address.

	* gcc.c-torture/compile/pr40023.c: New testcase.

""",
u"""
	cp/
	* typeck.c (cp_build_compound_expr): Require RHS to have a known
	type.
	* class.c (resolve_address_of_overloaded_function): Use
	OVL_CURRENT for error message.
	(instantiate_type): Forbid COMPOUND_EXPRs and remove code dealing
	with them.  Do not copy the node.

	testsuite/
	* g++.old-deja/g++.other/overload11.C: Adjust expected errors.
	* g++.dg/template/overload9.C: Likewise.
	* g++.dg/ext/ms-1.C: New.

""",
u"""

	* tree.h (strip_float_extensions): Remove duplicate declaration.
      	(build_low_bits_mask, debug_fold_checksum, expand_function_end,
      	expand_function_start, stack_protect_prologue, stack_protect_epilogue,
      	block_ultimate_origin): Rearrange the declarations line to match the
      	comment that indicates the .c file which the functions are defined.
      	(dwarf2out_*, set_decl_rtl): Add comment.
      	(get_base_address): Adjust comment.
      	(change_decl_assembler_name, maybe_fold_*, build_addr): Rearrange the
      	declarations line and add comment.
      	(is_builtin_name): Add blank after function name, for clarity.

""",
u"""
	PR c++/40013
	* pt.c (tsubst): If magic NOP_EXPR with side-effects has no type,
	set it from its operand's type after tsubst_expr.

	* g++.dg/ext/vla7.C: New test.

""",
u"""
Daily bump.
""",
u"""
	* attribs.c (decl_attributes): Use %qE for identifiers in
	diagnostics.
	* cgraphunit.c (verify_cgraph_node): Translate function names to
	locale character set in diagnostics.
	* coverage.c (get_coverage_counts): Use %qE for identifiers in
	diagnostics.
	* doc/invoke.texi (-finstrument-functions-exclude-function-list):
	Document that functions are named in UTF-8.
	* expr.c (expand_expr_real_1): Translate function names to locale
	character set in diagnostics.
	* gimplify.c (omp_notice_variable, omp_is_private,
	gimplify_scan_omp_clauses): Use %qE for identifiers in
	diagnostics.
	* langhooks.c (lhd_print_error_function): Translate function names
	to locale character set.
	* langhooks.h (decl_printable_name): Document that return value is
	in internal character set.
	* stmt.c: Include pretty-print.h
	(tree_conflicts_with_clobbers_p): Use %qE for identifiers in
	diagnostics.
	(resolve_operand_name_1): Translate named operand name to locale
	character set.
	* stor-layout.c (finalize_record_size): Use %qE for identifiers in
	diagnostics.
	* toplev.c (announce_function): Translate function names to locale
	character set.
	(warn_deprecated_use): Use %qE for identifiers in diagnostics.
	(default_tree_printer): Use pp_identifier or translate identifiers
	to locale character set.  Mark "<anonymous>" for translation.
	* tree-mudflap.c (mx_register_decls, mudflap_finish_file): Use %qE
	for identifiers in diagnostics.
	* tree.c (handle_dll_attribute): Use %qE for identifiers in
	diagnostics.
	* varasm.c (output_constructor): Use %qE for identifiers in
	diagnostics.

testsuite:
	* gcc.dg/ucnid-11.c, gcc.dg/ucnid-12.c, gcc.dg/ucnid-13.c: New
	tests.

""",
u"""

	* configure.ac: use ` ` instead of $()
	* configure: Regenerate.


""",
u"""
	* config/pa/linux-atomic.c: Eliminate conditional include of
	errno.h on non-LP64 systems to simplify build requirements.

""",
u"""
	* c-common.c (handle_mode_attribute): Use %qE for identifiers in
	diagnostics.
	* c-decl.c (check_bitfield_type_and_width): Make orig_name a tree
	and pass value to identifier_to_locale.
	(warn_variable_length_array): Make name a tree.
	(grokdeclarator): Separate diagnostic texts for named and unnamed
	declarators.  Use %qE for named declarators.
	* c-parser.c (c_lex_one_token): Use %qE for identifiers in
	diagnostics.
	* c-pragma.c (pop_alignment, handle_pragma_pack): Use %qE for
	identifiers in diagnostics.
	* c-typeck.c (push_member_name, start_init): Pass identifiers to
	identifier_to_locale.  Mark "anonymous" strings for translation.

testsuite:
	* gcc.dg/ucnid-8.c, gcc.dg/ucnid-9.c, gcc.dg/ucnid-10.c: New
	tests.
	* gcc.dg/declspec-9.c, gcc.dg/declspec-10.c, gcc.dg/declspec-11.c:
	Update expected errors.

""",
u"""
Allow address for DImode/DFmode only if double-precision FP regs.


""",
u"""
Add TARGET_SINGLE_FLOAT check.


""",
u"""

	PR ada/38874
	* make.adb (Scan_Make_Arg): Pass --param= to compiler and linker.
	


""",
u"""
Add CPP_SPEC for -mxilinx-fpu.


""",
u"""
Add t-xilinx for powerpc-xilinx-eabi*.

""",
u"""

 	* doc/tm.texi (LEGITIMIZE_ADDRESS): Revise documentation.
	* gcc/defaults.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/explow.c (memory_address): Use target hook.
	* gcc/targhooks.c (default_legitimize_address): New.
	* gcc/targhooks.h (default_legitimize_address): New.
	* gcc/target.h (legitimize_address): New.
	* gcc/target-def.h (TARGET_LEGITIMIZE_ADDRESS): New.
	(TARGET_INITIALIZER): Include it.
	* gcc/system.h (LEGITIMIZE_ADDRESS): Poison.

	* config/bfin/bfin-protos.h (legitimize_address): Remove.
	* config/bfin/bfin.c (legitimize_address): Remove.
	* config/bfin/bfin.h (LEGITIMIZE_ADDRESS): Remove.
	* config/m68hc11/m68hc11-protos.h (m68hc11_legitimize_address): Remove.
	* config/m68hc11/m68hc11.c (m68hc11_legitimize_address): Remove.
	* config/m68hc11/m68hc11.h (LEGITIMIZE_ADDRESS): Remove.

	* gcc/config/arm/arm.h (LEGITIMIZE_ADDRESS, ARM_LEGITIMIZE_ADDRESS,
	THUMB_LEGITIMIZE_ADDRESS, THUMB2_LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/s390/s390.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/m32c/m32c.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/sparc/sparc.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/m32r/m32r.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/i386/i386.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/sh/sh.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/avr/avr.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/m68hc11/m68hc11.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/iq2000/iq2000.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/mn10300/mn10300.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/m68k/m68k.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/score/score.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/pa/pa.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/mips/mips.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/alpha/alpha.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/frv/frv.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/spu/spu.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/xtensa/xtensa.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/cris/cris.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/rs6000/rs6000.h (LEGITIMIZE_ADDRESS): Delete.
	* gcc/config/picochip/picochip.h (LEGITIMIZE_ADDRESS): Delete.

	* gcc/config/s390/s390-protos.h (legitimize_address): Delete.
	* gcc/config/m32c/m32c-protos.h (m32c_legitimize_address): Delete.
	* gcc/config/sparc/sparc-protos.h (legitimize_address): Delete.
	* gcc/config/i386/i386-protos.h (legitimize_address): Delete.
	* gcc/config/avr/avr-protos.h (legitimize_address): Delete.
	* gcc/config/mn10300/mn10300-protos.h (legitimize_address): Delete.
	* gcc/config/score/score-protos.h (score_legitimize_address): Delete.
	* gcc/config/arm/arm-protos.h (arm_legitimize_address,
	(thumb_legitimize_address): Delete.
	* gcc/config/pa/pa-protos.h (hppa_legitimize_address): Delete.
	* gcc/config/mips/mips-protos.h (mips_legitimize_address): Delete.
	* gcc/config/alpha/alpha-protos.h (alpha_legitimize_address): Delete.
	* gcc/config/frv/frv-protos.h (frv_legitimize_address): Delete.
	* gcc/config/spu/spu-protos.h (spu_legitimize_address): Delete.
	* gcc/config/xtensa/xtensa-protos.h (xtensa_legitimize_address): Delete.
	* gcc/config/rs6000/rs6000-protos.h (rs6000_legitimize_address): Delete.

	* config/arm/arm.c (arm_legitimize_address): Maybe call Thumb version.
	* config/m32c/m32c.c (m32c_legitimize_address): Standardize.
	* config/m32r/m32r.c (m32r_legitimize_address): New.
	* config/m68k/m68k.c (m68k_legitimize_address): New.
	* config/score/score.c (score_legitimize_address): Standardize.
	* config/score/score3.c (score3_legitimize_address): Standardize.
	* config/score/score3.h (score3_legitimize_address): Adjust.
	* config/score/score7.c (score7_legitimize_address): Standardize.
	* config/score/score7.h (score7_legitimize_address): Adjust.
	* config/sh/sh.c (sh_legitimize_address): New.
	* config/iq2000/iq2000.c (iq2000_legitimize_address): New.

	* gcc/config/s390/s390.c (legitimize_address): Rename to...
 	(s390_legitimize_address): ... this.
	* gcc/config/sparc/sparc.c (legitimize_address): Rename to...
	(sparc_legitimize_address): ... this.
	* gcc/config/i386/i386.c (legitimize_address): Rename to...
	(ix86_legitimize_address): ... this.
	* gcc/config/avr/avr.c (legitimize_address): Rename to...
	(avr_legitimize_address): ... this.
	* gcc/config/mn10300/mn10300.c (legitimize_address): Rename to...
	(mn10300_legitimize_address): ... this.
	* config/alpha/alpha.c (alpha_legitimize_address): Wrap...
	(alpha_legitimize_address_1): ... the old alpha_legitimize_address.
	(alpha_expand_mov): Adjust call.

	* config/frv/frv.c (frv_legitimize_address): Return x on failure.
	* config/spu/spu.c (spu_legitimize_address): Likewise.
	* config/xtensa/xtensa.c (xtensa_legitimize_address): Likewise.
	* config/rs6000/rs6000.c (rs6000_legitimize_address): Likewise.

""",
u"""

	PR c++/28152
cp/	
	* parser.c (cp_lexer_get_preprocessor_token):  Do not store the
	canonical spelling for keywords.
	(cp_parser_attribute_list): Use the canonical spelling for
	keywords in attributes.
testsuite/
	* g++.dg/parse/parser-pr28152.C: New.
	* g++.dg/parse/parser-pr28152-2.C: New.


""",
u"""
	* intl.c (locale_encoding, locale_utf8): New.
	(gcc_init_libintl): Initialize locale_encoding and locale_utf8.
	* intl.h (locale_encoding, locale_utf8): Declare.
	* pretty-print.c: Include ggc.h.  Include iconv.h if HAVE_ICONV.
	(pp_base_tree_identifier, decode_utf8_char, identifier_to_locale):
	New.
	* pretty-print.h (pp_identifier): Call identifier_to_locale on ID
	argument.
	(pp_tree_identifier): Define to call pp_base_tree_identifier.
	(pp_base_tree_identifier): Declare as function.
	(identifier_to_locale): Declare.
	* Makefile.in (pretty-print.o): Update dependencies.
	* varasm.c (finish_aliases_1): Use %qE for identifiers in
	diagnostics.

testsuite:
	* gcc.dg/attr-alias-5.c, gcc.dg/ucnid-7.c: New tests.

""",
u"""

	PR middle-end/40015
	* builtins.c (fold_builtin_memory_op): Do not decay to element
	type if the size matches the whole array.

""",
u"""
Daily bump.
""",
u"""
	* expmed.c (synth_mult): When trying out a shift, pass the result
	of a signed shift.

""",
u"""
	* expmed.c (shiftsub_cost): Rename to shiftsub0_cost.
	(shiftsub1_cost): New.
	(init_expmed): Compute shiftsub1_cost.
	(synth_mult): Optimize multiplications by constants of the form
	-(2^^m-1) for some constant positive integer m.

""",
u"""
	* gcc.target/sparc/fpmul-2.c: Replace final_cleanup with optimized.
	* gcc.target/sparc/fexpand-2.c: Likewise.
	* gcc.target/sparc/fpmerge-2.c: Likewise.
	* gcc.target/sparc/pdist-2.c: Likewise.

""",
u"""

	PR c/39983
	* c-typeck.c (array_to_pointer_conversion): Do not built
	ADDR_EXPRs of arrays of pointer-to-element type.
	* c-gimplify.c (c_gimplify_expr): Revert change fixing
	up wrong ADDR_EXPRs after-the-fact.
	* c-common.c (strict_aliasing_warning): Strip pointer
	conversions for obtaining the original type.
	* builtins.c (fold_builtin_memset): Handle array types.
	(fold_builtin_memory_op): Handle folded POINTER_PLUS_EXPRs
	and array types

	* gcc.c-torture/compile/pr39983.c: New testcase.

""",
u"""

	PR middle-end/23329
	* tree-ssa.c (useless_type_conversion_p_1): Use get_deref_alias_set.
	Do not lose casts from array types with unknown extent to array
	types with known extent.
	* tree-ssa-copy.c (may_propagate_copy): Remove hack checking for
	alias set compatibility.

""",
u"""

	* flags.h (extra_warnings): Delete.
	* toplev.c (process_options): Handle Wuninitialized here.
	* opts.c (extra_warnings): Delete.
	(set_Wextra): Delete.
	(common_handle_option): -Wextra can be handled automatically.
	* c-opts.c (c_common_handle_option): Delete obsolete code.
	(c_common_post_options): Simplify comment.
	* common.opt (W): Add Var.
	(Wextra): Add Var.
	(Wuninitialized): Initialize to -1.

""",
u"""
	* expr.c (get_def_for_expr): New function.
	(expand_expr_real_1) <PLUS_EXPR, MINUS_EXPR>: Adjust to work with
	SSA rather than trees.
	<MULT_EXPR>: Likewise.  Use subexp0 and subexp1 instead of
	TREE_OPERAND (exp, 0) and TREE_OPERAND (exp, 1).

""",
u"""
	* include/parallel/settings.h (get): Mark const.
	* libsupc++/unwind-cxx.h (__cxa_call_terminate): Mark throw ().
	* libsupc++/eh_call.cc (__cxa_call_terminate): Mark throw ().
	* config/io/basic_file_stdio.cc (sys_open, is_open, fd, seekoff): Mark
	throw ().
	* config/io/basic_file_stdio.h (__basic_file, sys_open): Mark throw ().
	(is_open, fd): Mark pure and throw ().
	(seekoff): Mark throw ().

""",
u"""

	* acinclude.m4 ([GLIBCXX_ENABLE_ATOMIC_BUILTINS]): Do link tests when
	possible.
	* configure: Regenerate.

""",
u"""
	* c-common.c (reswords): Add _Imaginary.
	* c-common.c (enum rid): Add RID_IMAGINARY.

testsuite:
	* gcc.dg/c99-complex-3.c: New test.

""",
u"""

	* tree.h (TYPE_VECTOR_OPAQUE): Fix documentation.
	Patch by Richard Guenther.

""",
u"""
libcpp:
	* charset.c (one_utf8_to_cppchar): Correct mask used for 5-byte
	UTF-8 sequences.

gcc/testsuite:
	* gcc.dg/cpp/utf8-5byte-1.c: New test.

""",
u"""
	* defaults.h (FRAME_POINTER_REQUIRED): Provide default.
	* doc/tm.texi (FRAME_POINTER_REQUIRED): Revise documentation.
	* config/alpha/alpha.h (FRAME_POINTER_REQUIRED): Delete.
	* config/s390/s390.h (FRAME_POINTER_REQUIRED): Delete.
	* config/spu/spu.h (FRAME_POINTER_REQUIRED): Delete.
	* config/sh/sh.h (FRAME_POINTER_REQUIRED): Delete.
	* config/pdp11/pdp11.h (FRAME_POINTER_REQUIRED): Delete.
	* config/stormy16/stormy16.h (FRAME_POINTER_REQUIRED): Delete.
	* config/m68hc11/m68hc11.h (FRAME_POINTER_REQUIRED): Delete.
	* config/iq2000/iq2000.h (FRAME_POINTER_REQUIRED): Delete.
	* config/mn10300/mn10300.h (FRAME_POINTER_REQUIRED): Delete.
	* config/ia64/ia64.h (FRAME_POINTER_REQUIRED): Delete.
	* config/m68k/m68k.h (FRAME_POINTER_REQUIRED): Delete.
	* config/rs6000/rs6000.h (FRAME_POINTER_REQUIRED): Delete.
	* config/picochip/picochip.h (FRAME_POINTER_REQUIRED): Delete.
	* config/mcore/mcore.h (FRAME_POINTER_REQUIRED): Delete.
	* config/h8300/h8300.h (FRAME_POINTER_REQUIRED): Delete.
	* config/v850/v850.h (FRAME_POINTER_REQUIRED): Delete.

""",
u"""
Daily bump.
""",
u"""
	* gcc.dg/ucnid-6.c: Fix typo in dg-do directive.

""",
u"""

	PR tree-optimization/39940
	* tree-ssa-pre.c (eliminate): Make sure we may propagate before
	doing so.

""",
u"""

	PR middle-end/40001
	* tree-ssa.c (execute_update_addresses_taken): Properly check
	if we can mark a variable DECL_GIMPLE_REG_P.
	* gimple.c (is_gimple_reg): Re-order check for DECL_GIMPLE_REG_P
	back to the end of the function.
	(is_gimple_reg_type): Remove complex type special casing.
	* gimplify.c (gimplify_bind_expr): Do not set DECL_GIMPLE_REG_P
	if not optimizing.

	* gcc.target/spu/pr40001.c: New testcase.

""",
u"""
	* include/tr1_impl/functional_hash.h (explicit specializations of ()
	operator): Mark pure.

""",
u"""
	* doc/collect2.texi (Collect2): Document search path behaviour
	when configured with --with-ld.

""",
u"""
	* tree-ssa-coalesce.c (coalesce_cost): Do not take ciritical
	parameter; update callers.
	(coalesce_cost_edge): EH edges are costier because they needs splitting
	even if not critical and even more costier when there are multiple
	EH predecestors.

""",
u"""
	* except.c (remove_eh_handler_and_replace): Handle updating after
	removing TRY blocks.

""",
u"""
	* store-motion.c (compute_store_table): Add ENABLE_CHECKING guard.

""",
u"""
	* varasm.c: Do not include c-pragma.h
	* attribs.c: Do not incude c-common.h


""",
u"""
Daily bump.
""",
u"""
        * calls.c (initialize_argument_information): Handle SSA names
        like decls with a non MEM_P DECL_RTL.

""",
u"""
	* ipa-reference.c: Do not include c-common.h, include splay-tree.h.
	* ipa-utils.c: Likewise.
	* ipa-type-escape.c: Likewise.
	* cgraphunit.c Do not include c-common.h.
	* ipa-pure-const.c: Likewise.
	* tree-if-conv.c: Likewise.
	* matrix-reorg.c: Do not include c-common.h and c-tree.h.
	* ipa-struct-reorg.c: Likewise.
	* tree-nomudflap.c: Likewise.
	* tree-ssa-structalias.c: Likewise.

""",
u"""
	* store-motion.c: Many cleanups to make this pass a first-class
	citizen instead of an appendix to gcse load motion.  Add TODO list
	to make this pass faster/cleaner/better.

	(struct ls_expr): Post gcse.c-split cleanups.
	Rename to st_expr.  Rename "loads" field to "antic_stores".  Rename
	"stores" field to "avail_stores".
	(pre_ldst_mems): Rename to store_motion_mems.
	(pre_ldst_table): Rename to store_motion_mems_table.
	(pre_ldst_expr_hash): Rename to pre_st_expr_hash, update users.
	(pre_ldst_expr_eq): Rename to pre_st_expr_eq, update users.
	(ldst_entry): Rename to st_expr_entry, update users.
	(free_ldst_entry): Rename to free_st_expr_entry, update users.
	(free_ldst_mems): Rename to free_store_motion_mems, update users.
	(enumerate_ldsts): Rename to enumerate_store_motion_mems, update caller.
	(first_ls_expr): Rename to first_st_expr, update users.
	(next_ls_expr): Rename to next_st_expr, update users.
	(print_ldst_list): Rename to print_store_motion_mems.  Print names of
	fields properly for store motion instead of names inherited from load
	motion in gcse.c.
	(ANTIC_STORE_LIST, AVAIL_STORE_LIST): Remove.
	(LAST_AVAIL_CHECK_FAILURE): Explain what this is.  Undefine when we
	are done with it.

	(ae_kill): Rename to st_kill, update users.
	(ae_gen): Rename to st_avloc, update users.
	(transp): Rename to st_transp, update users.
	(pre_insert_map): Rename to st_insert_map, update users.
	(pre_delete_map): Rename to st_delete_map, update users.
	(insert_store, build_store_vectors, free_store_memory,
	one_store_motion_pass): Update for abovementioned changes.

	(gcse_subst_count, gcse_create_count): Remove.
	(one_store_motion_pass): New statistics counters "n_stores_deleted"
	and "n_stores_created", local variables.

	(extract_mentioned_regs, extract_mentioned_regs_1): Rewrite to
	use for_each_rtx.

	(regvec, compute_store_table_current_insn): Remove.
	(reg_set_info, reg_clear_last_set): Remove.
	(compute_store_table): Use DF caches instead of local dataflow
	solvers.


""",
u"""
	* c-objc-common.c (c_tree_printer): Print identifiers with
	pp_identifier, not pp_string.  Mark "({anonymous})" for
	translation.
	* c-pretty-print.c (pp_c_ws_string): New.
	(pp_c_cv_qualifier, pp_c_type_specifier,
	pp_c_specifier_qualifier_list, pp_c_parameter_type_list,
	pp_c_storage_class_specifier, pp_c_function_specifier,
	pp_c_attributes, pp_c_bool_constant, pp_c_constant,
	pp_c_primary_expression, pp_c_postfix_expression,
	pp_c_unary_expression, pp_c_shift_expression,
	pp_c_relational_expression, pp_c_equality_expression,
	pp_c_logical_and_expression, pp_c_logical_or_expression): Mostly
	use pp_string and pp_c_ws_string in place of pp_identifier and
	pp_c_identifier for non-identifiers.  Mark English strings for
	translation.
	* c-pretty-print.h (pp_c_ws_string): Declare.

cp:
	* cxx-pretty-print.c (is_destructor_name, pp_cxx_unqualified_id,
	pp_cxx_template_keyword_if_needed, pp_cxx_postfix_expression,
	pp_cxx_new_expression, pp_cxx_delete_expression,
	pp_cxx_unary_expression, pp_cxx_assignment_operator,
	pp_cxx_assignment_expression, pp_cxx_expression,
	pp_cxx_function_specifier, pp_cxx_decl_specifier_seq,
	pp_cxx_simple_type_specifier, pp_cxx_type_specifier_seq,
	pp_cxx_exception_specification, pp_cxx_direct_declarator,
	pp_cxx_ctor_initializer, pp_cxx_type_id, pp_cxx_statement,
	pp_cxx_namespace_alias_definition, pp_cxx_template_parameter,
	pp_cxx_canonical_template_parameter, pp_cxx_template_declaration,
	pp_cxx_declaration, pp_cxx_typeid_expression,
	pp_cxx_va_arg_expression, pp_cxx_offsetof_expression,
	pp_cxx_trait_expression): Mostly use pp_string and
	pp_cxx_ws_string in place of pp_identifier and pp_cxx_identifier
	for non-identifiers.  Mark English strings for translation.
	* cxx-pretty-print.h (pp_cxx_ws_string): Define.
	* error.c (dump_template_parameter, dump_template_bindings,
	dump_type, dump_aggr_type, dump_type_prefix, dump_simple_decl,
	dump_decl, dump_template_decl, dump_function_decl,
	dump_parameters, dump_exception_spec, dump_template_parms,
	dump_expr, dump_binary_op, dump_unary_op, op_to_string,
	assop_to_string, args_to_string, cp_print_error_function,
	print_instantiation_full_context,
	print_instantiation_partial_context): Mostly use pp_string and
	pp_cxx_ws_string in place of pp_identifier and pp_cxx_identifier
	for non-identifiers.  Mark English strings for translation.
	(dump_global_iord): Mark strings for translation; use longer
	strings instead of substituting single words.
	(function_category): Return a format string marked for
	translation, not a single word or phrase to substitute in a longer
	phrase.

""",
u"""
	* doc/install.texi: Document --enable-linker-build-id option.

""",
u"""
	* configure.ac (HAVE_LD_BUILDID): New check for ld --build-id
	support.
	(ENABLE_LD_BUILDID): New configuration option.
	* gcc.c [HAVE_LD_BUILDID and ENABLE_LD_BUILDID]
	(LINK_BUILDID_SPEC): New macro.
	(init_spec): If defined, prepend it between LINK_EH_SPEC and
	link_spec.
	* doc/install.texi: Document --enable-linker-build-id option.
	* configure: Rebuild.
	* config.in: Rebuild.

""",
u"""
Daily bump.
""",
u"""
	* config/mips/mips.h (FRAME_GROWS_DOWNWARD,
	MIPS_GP_SAVE_AREA_SIZE): Define new macros.
	(STARTING_FRAME_OFFSET): Return 0 if FRAME_GROWS_DOWNWARD.  Use
	MIPS_GP_SAVE_AREA_SIZE.
	* config/mips/mips.c (struct mips_frame_info): Update comment
	before arg_pointer_offset and hard_frame_pointer_offset.
	(mips_compute_frame_info): Update diagram before function: to
	correctly use stack_pointer_rtx for fp_sp_offset and gp_sp_offset, to
	indicate the position of frame_pointer_rtx with -fstack-protector and
	to show args_size.  Don't allocate cprestore area for leaf functions
	if FRAME_GROWS_DOWNWARD.  Use MIPS_GP_SAVE_AREA_SIZE to set
	cprestore_size.
	(mips_initial_elimination_offset): Update for FRAME_GROWS_DOWNWARD.

""",
u"""
	* gcc.dg/ssp-1.c (__stack_chk_fail): Remove static.

""",
u"""
fix for PR 39955
""",
u"""
Fix from Dave Korn in case a backend does not declare any define_register_constraints
""",
u"""
	PR middle-end/39579
	* gcc.dg/vect/vect-35.c: XFAIL for IA64 and Sparc.
	* gfortran.dg/vect/fast-math-pr38968.f90: Ditto.

""",
u"""

	* scripts/create_testsuite_files: Remove thread directory.

""",
u"""
	PR testsuite/39776
	* g++.dg/ext/altivec-15.C: Remove dg-error for messages that are
	no longer issued.

""",
u"""

	* alloc-pool.c (alloc_pool_descriptor): Use an insert_opion value
	instead of an int.
	* bitmap.c (bitmap_descriptor): Likewise.
	* ggc-common.c (loc_descriptor): Likewise.
	* varray.c (varray_descriptor): Likewise.
	* vec.c (vec_descriptor): Likewise.


""",
u"""

	* lib/objc.exp (objc_init): Add	and set gcc_warning_prefix
	and gcc_error_prefix variables.
	* objc.dg/bad-receiver-type.m: Update to match correct
	diagnostics marker.
	* objc.dg/encode-5.m: Likewise.
	* objc.dg/id-1.m: Likewise.
	* objc.dg/method-1.m: Likewise.
	* objc.dg/method-6.m: Likewise.
	* objc.dg/method-7.m: Likewise.
	* objc.dg/method-9.m: Likewise.
	* objc.dg/method-11.m: Likewise.
	* objc.dg/method-20.m: Likewise.
	* objc.dg/private-1.m: Likewise.


""",
u"""
Fix PR libfortran/39667

""",
u"""
Fix date
""",
u"""
	* Makefile.in (dce.o): Add $(EXCEPT_H).
	* dce.c: Include except.h and delete redundant vector definitions.
	(deletable_insn_p): Return false for non-call insns that can throw
	if DF is running.

""",
u"""
	* gcse.c (ae_gen): Remove.
	(can_assign_to_reg_p): Rename to can_assign_to_reg_without_clobbers_p
	and make non-static function to make it available in store-motion.c.
	Update call sites with search-and-replace.
	(enumerate_ldsts, reg_set_info, reg_clear_last_set, store_ops_ok,
	extract_mentioned_regs, extract_mentioned_regs_helper,
	find_moveable_store, compute_store_table, load_kills_store, find_loads,
	store_killed_in_insn, store_killed_after, store_killed_before,
	build_store_vectors, insert_insn_start_basic_block, insert-store,
	remove_reachable_equiv_notes, replace_store_insn, delete_store,
	free_store_memory, one_store_motion_pass, gate_rtl_store_motion,
	execute_rtl_store_motion, pass_rtl_store_motion): Move to...
	* store-motion.c: ...new file.  Also copy data structures from gcse.c
	and clean up to remove parts not used by store motion.
	* rtl.h (can_assign_to_reg_without_clobbers_p): Add prototype.
	* Makefile.in (store-motion.o): New rule. Add to OBJS-common.


""",
u"""
Fix PR target/38571
""",
u"""
	* gcse.c (gcse_constant_p): Fix typo in last change.

""",
u"""

	* plugin.c: Include plugin-version.h only if ENABLE_PLUGIN is defined.


""",
u"""

	* gcse.c (gcse_constant_p): Make sure the constant is sharable.


""",
u"""
* config/mips/mips.c (mips_add_offset): Use gen_int_mode for
CONST_HIGH_PART result.

""",
u"""
Daily bump.
""",
u"""
	Revert

	* sinput-l.adb (Load_File): When preprocessing, set temporarily the
	Source_File_Index_Table entries for the source, to avoid crash when
	reporting an error.

	* gnatcmd.adb (Test_If_Relative_Path): Use
	Makeutl.Test_If_Relative_Path.
	
	* makeutl.adb:(Test_If_Relative_Path): Process switches --RTS= only if
	Including_RTS is True.

	* makeutl.ads (Test_If_Relative_Path): New Boolean parameter
	Including_RTS defaulted to False.

	* sinput.ads, scans.ads, err_vars.ads: Initialize some variables with
	a default value.

""",
u"""
	(frame_pointer_required_p): Change return type to bool.


""",
u"""
	* config/avr/avr.c (initial_elimination_offset): Rename to
	avr_initial_elimination_offset.
	(frame_pointer_required_p): Rename to avr_frame_pointer_required_p,
	change return type to bool.
	(avr_can_eliminate): New function.
	* config/avr/avr.h (CAN_ELIMINATE): Use avr_can_eliminate.
	(FRAME_POINTER_REQUIRED): Use avr_frame_pointer_required_p.
	(INITIAL_ELIMINATION_OFFSET): Use avr_initial_elimination_offset.
	* config/avr/avr-protos.h (initial_elimination_offset) : Rename to
	avr_initial_elimination_offset.
	(frame_pointer_required_p): Rename to avr_frame_pointer_required_p.
	(avr_initial_elimination_offset): Define.

""",
u"""
	PR rtl-optimization/39938
	* Makefile.in (cfgrtl.o): Add $(INSN_ATTR_H).
	* cfgrtl.c: Include insn-attr.h.
	(rest_of_pass_free_cfg): New function.
	(pass_free_cfg): Use rest_of_pass_free_cfg as execute function.
	* resource.c (init_resource_info): Remove call to df_analyze.

""",
u"""

	PR target/39943
	* config/i386/i386.c (ix86_vectorize_builtin_conversion): Only
	allow conversion to signed integers.

	* lib/target-supports.exp (check_effective_target_vect_uintfloat_cvt):
	New.
	(check_effective_target_vect_floatuint_cvt): Likewise.
	* gcc.dg/vect/slp-10.c: Adjust.
	* gcc.dg/vect/slp-11.c: Adjust.
	* gcc.dg/vect/slp-12b.c: Adjust.
	* gcc.dg/vect/slp-33.c: Adjust.
	* gcc.c-torture/compile/pr39943.c: New testcase.

""",
u"""

	* tree-cfg.c (verify_gimple_assign_binary): Allow vector
	shifts of floating point vectors if the shift amount is
	a constant multiple of the element size.

""",
u"""
        PR middle-end/39927
        PR bootstrap/39929
        * tree-outof-ssa.c (emit_partition_copy): New function.
        (insert_partition_copy_on_edge, insert_rtx_to_part_on_edge,
        insert_part_to_rtx_on_edge): Perform the partition base var
        copy using emit_partition_copy.
        (insert_value_copy_on_edge): Convert constants to the right mode.
        (insert_rtx_to_part_on_edge): Add UNSIGNEDSRCP parameter.
        (elim_create): Pass the sign of the src to insert_rtx_to_part_on_edge.

""",
u"""
	* config/bfin/bfin.c (bfin_optimize_loop): When looking for the last
	insn before the loop_end instruction, don't look past labels.


""",
u"""

	* sem_ch8.adb (Analyze_Subprogram_Renaming): Improve error message on
	box-defaulted operator in an instantiation, when the type of the
	operands is not directly visible.


	* sem_aggr.adb (Valid_Limited_Ancestor): Undo previous change.
	(Resolve_Extension_Aggregate): Call Check_Parameterless_Call after the
	analysis of the ancestor part. Remove prohibition against limited
	interpretations of the ancestor expression in the case of Ada 2005.
	Revise error message in overloaded case, adding a message to cover
	the Ada 2005 case.


	* xoscons.adb: Minor reformatting


	* sem_ch13.adb (Analyze_Attribute_Definition_Clause): Do not ignore
	attribute_definition_clauses for the following attributes when the
	-gnatI switch is used: External_Tag, Input, Output, Read, Storage_Pool,
	Storage_Size, Write. Otherwise, we get spurious errors (for example,
	missing Read attribute on remote types).

	* gnat_ugn.texi: Document the change, and add a stern warning.


	* sem_attr.adb (Check_Local_Access): Indicate that value tracing is
	disabled not just for the current scope, but for the innermost dynamic
	scope as well.


""",
u"""
	* gcc-interface/Make-lang.in: Update dependencies

""",
u"""
Removed file that should have been removed in a previous commit. Already listed on ChangeLog.


""",
u"""

	* prj-part.adb: Minor comment update


	* sem_aggr.adb (Resolve_Record_Aggregate): handle properly
	box-initialized records with discriminated subcomponents that are
	constrained by discriminants of enclosing components. New subsidiary
	procedures Add_Discriminant_Values, Propagate_Discriminants.


	* g-socket.adb: Code clean up.


""",
u"""
	* config/bfin/bfin.c (bfin_optimize_loop): If we need a scratch reg,
	scan backwards to try to find a constant to initialize it.


""",
u"""

	PR middle-end/39937
	* tree-ssa-forwprop.c (forward_propagate_addr_expr_1): Do not
	loose type conversions.
	(forward_propagate_addr_expr): Fix tuplification bug.  Remove
	stmts only if there are no uses of its definition.

	* gcc.c-torture/compile/pr39937.c: New testcase.

""",
u"""
	* config/bfin/bfin.h (splitting_loops): Declare.
	* config/bfin/bfin-protos.h (WA_05000257, WA_05000283, WA_05000315):
	Reorder bit definitions to be ascending.
	(WA_LOAD_LCREGS, ENABLE_WA_LOAD_LCREGS): New macros.
	* config/bfin/bfin.c (splitting_loops): New variable.
	(bfin_cpus): Add WA_LOAD_LCREGS as needed.
	(struct loop_info): Remove members INIT and LOOP_INIT.
	(bfin_optimize_loop): Don't set them.  Reorder the code that generates
	the LSETUP sequence.  Allow LC to be loaded from any register, but also
	add a case to push/pop a PREG scratch if ENABLE_WA_LOAD_LCREGS.
	(bfin_reorg_loops): When done, split all BB_ENDs with splitting_loops
	set to 1.
	* config/bfin/bfin.md (loop_end splitter): Use splitting_loops instead
	of reload_completed.
	From Jie Zhang:
	* config/bfin/bfin.md (movsi_insn): Refine constraints.

""",
u"""

	* sem_aggr.adb (Valid_Limited_Ancestor): Add test for the name of a
	function entity, to cover the case of a parameterless function call
	that has not been resolved.


	* err_vars.ads, prj-part.adb, scans.ads, exp_tss.adb: Minor
	reformatting and comment updates.


""",
u"""

	* gnat_ugn.texi: Update some documentation about interfacing with C++
	Mention -fkeep-inline-functions.

	* gnat_ugn.texi: Minor edits


	* sem_aggr.adb (Resolve_Record_Aggregate): When building an aggregate
	for a defaulted component of an enclosing aggregate, inherit the type
	from the component declaration of the enclosing type. 


	* g-socthi-vms.ads, g-socthi-vxworks.ads, s-oscons-tmplt.c,
	g-socthi-mingw.ads, g-socthi.ads, g-socket.adb, g-sothco.ads
	(System.OS_Constants): New type Msg_Iovlen_T which follows whether the
	msg_iovlen field in struct msghdr is 32 or 64 bits wide.
	Relocate the Msghdr record type from GNAT.Sockets.Thin to
	GNAT.Sockets.Common, and use System.OS_Constants.Msg_Iovlen_T as the
	type for the Msg_Iovlen field.


""",
u"""

	* sinput-l.adb (Load_File): When preprocessing, set temporarily the
	Source_File_Index_Table entries for the source, to avoid crash when
	reporting an error.

	* gnatcmd.adb (Test_If_Relative_Path): Use
	Makeutl.Test_If_Relative_Path.
	
	* makeutl.adb:(Test_If_Relative_Path): Process switches --RTS= only if
	Including_RTS is True.

	* makeutl.ads (Test_If_Relative_Path): New Boolean parameter
	Including_RTS defaulted to False.

	* sinput.ads, scans.ads, err_vars.ads: Initialize some variables with
	a default value.


	* gnat_ugn.texi: Adding documentation for non-default C++ constructors.


""",
u"""

	* sem_ch3.adb (Analyze_Object_Declaration): Disable error message
	associated with dyamically tagged expressions if the expression
	initializing a tagged type corresponds with a non default CPP
	constructor.
	(OK_For_Limited_Init): CPP constructor calls are OK for initialization
	of limited type objects.

	* sem_ch5.adb (Analyze_Assignment): Improve the error message reported
	when a CPP constructor is called in an assignment. Disable also the
	error message associated with dyamically tagged expressions if the
	exporession initializing a tagged type corresponds with a non default
	CPP constructor.

	* sem_prag.adb (Analyze_Pragma): Remove code disabling the use of
	non-default C++ constructors.

	* sem_util.ads, sem_util.adb (Is_CPP_Constructor_Call): New subprogram.

	* exp_tss.ads, exp_tss.adb (Base_Init_Proc): Add support for
	non-default constructors.
	(Init_Proc): Add support for non-default constructors.

	* exp_disp.adb (Set_Default_Constructor): Removed.
	(Set_CPP_Constructors): Code based in removed Set_Default_Constructor
	but extending its functionality to handle non-default constructors.

	* exp_aggr.adb (Build_Record_Aggr_Code): Add support for non-default
	constructors. Minor code cleanup removing unrequired label and goto
	statement.

	* exp_ch3.adb (Build_Initialization_Call): Add support for non-default
	constructors.
	(Build_Init_Statements): Add support for non-default constructors.
	(Expand_N_Object_Declaration): Add support for non-default constructors.
	(Freeze_Record_Type): Replace call to Set_Default_Constructor by call
	to Set_CPP_Constructors.

	* exp_ch5.adb (Expand_N_Assignment_Statement): Add support for
	non-default constructors.
	Required to handle its use in build-in-place statements.

	* gnat_rm.texi (CPP_Constructor): Document new extended use of this
	pragma for non-default C++ constructors and the new compiler support
	that allows the use of these constructors in record components, limited
	aggregates, and extended return statements.


""",
u"""

	* prj-part.adb (Parse_Single_Project): Do not attempt to find a
	project extending an abstract project.


	* targparm.ads: Fix oversight.


""",
u"""

	* lib-xref.adb (Output_Overridden_Op): Follow several levels of
	derivation when necessary, to find the user-subprogram that is actally
	being overridden.


""",
u"""

	* sem_util.adb (May_Be_Lvalue): Fix cases involving indexed/selected
	components


""",
u"""

	* Makefile.in (PLUGIN_VERSION_H): New.
	(OBJS-common): Remove plugin-version.o.
	(plugin.o): Depend on (PLUGIN_VERSION_H).
	(plugin-version.o): Remove.
	* configure: Regenerate
	* configure.ac: Create plugin-version.h.
	* gcc-plugin.h (plugin_gcc_version): Remove.
	(plugin_default_version_check): Change signature.
	* plugin-version.c: Remove.
	* plugin.c: Include plugin-version.h.
	(str_plugin_gcc_version_name): Remove.
	(try_init_one_plugin): Pass gcc version to plugin_init.
	(plugin_default_version_check): Both gcc and plugin versions are now
	arguments.


""",
u"""

	* exp_ch9.ads, exp_ch9.adb (Build_Wrapper_Spec): Use source line of
	primitive operation, rather than source line of synchronized type, when
	building the wrapper for a primitive operation that overrides an
	operation inherited from a progenitor, to improve the error message on
	duplicate declarations.

	* sem_ch3.adb (Process_Full_View): Use new signature of
	Build_Wrapper_Spec.


""",
u"""

	* prj-nmsc.ads: Minor reformatting


	* exp_ch4.adb (Expand_N_Conditional_Expression): Set the SLOC of the
	expression on the existing parent If statement.


""",
u"""
Complete previous change:


	* prj-nmsc.ads: Minor reformatting


	* exp_ch4.adb (Expand_N_Conditional_Expression): Set the SLOC of the
	expression on the existing parent If statement.


""",
u"""

	* prj-proc.adb, prj.ads: Minor reformatting


""",
u"""

	* exp_ch4.adb (Expand_N_Conditional_Expression): Set the SLOC of an
	existing parent If statement on the newly created one.


""",
u"""
	* config/bfin/bfin.c (bfin_register_move_cost): Test for subsets of
	DREGS rather than comparing directly.  Remove code that tries to
	account for latencies.


""",
u"""

	* gnatcmd.adb, prj-proc.adb, prj-proc.ads, make.adb, prj-part.adb,
	prj-part.ads, prj.adb, prj.ads, clean.adb, prj-dect.adb, prj-dect.ads,
	prj-nmsc.adb, prj-nmsc.ads, prj-pars.adb, prj-pars.ads, prj-makr.adb
	(Set_In_Configuration, In_Configuration): Removed.
	Replaced by an extra parameter Is_Config_File in several parameter to
	avoid global variables to store the state of the parser.


""",
u"""

	* g-socthi-vxworks.ads: Change the spec of Msghdr to match the one in
	the default version of GNAT.Sockets.Thin.

	* g-socthi-vms.ads: Change the spec of Msghdr to match the one in the
	default version of GNAT.Sockets.Thin.


	* sem_ch6.adb (Analyze_Subprogram_Specification): If the subprogram is
	an overriding operation of an inherited interface operation, and the
	controlling type is a synchronized type, we replace the type with its
	corresponding record, to match the proper signature of an overriding
	operation. The same processing must be performed for an access
	parameter whose designated type is derived from a synchronized
	interface.


""",
u"""
	* pex-win32.c (pex_win32_pipe): Add _O_NOINHERIT.    
	(pex_win32_exec_child): Ensure each process has only one handle open
	on pipe endpoints. Close standard input after creating child for
	symmetry with standard output/standard error.


""",
u"""
	* config/bfin/bfin.c (bfin_optimize_loop): Unify handling of
	problematic last insns.  Test for TYPE_CALL rather than CALL_P.
	Remove special case testing for last insn of inner loops. Don't fail if
	the loop ends with a jump, emit an extra nop instead.


""",
u"""

	* sinfo.ads, sinfo.adb: New attribute Next_Implicit_With, to chain
	with_clauses generated for the same unit through rtsfind, and that
	appear in the context of different units.

	* rtsfind.adb: New attribute First_Implicit_With, component of the
	Unit_Record that stores information about a unit loaded through rtsfind.


""",
u"""
Minor improvements.

""",
u"""

	* exp_ch3.adb (Stream_Operation_OK): Return True for limited interfaces
	(other conditions permitting), so that abstract stream subprograms will
	be declared for them.


	* g-expect.adb (Expect_Internal): Fix check for overfull buffer.

	* g-expect.ads: Minor comment fixes.


	* freeze.adb, lib-xref.adb (Check_Dispatching_Operation): if the
	dispatching operation is a body without previous spec, update the list
	of primitive operations to ensure that cross-reference information is
	up-to-date.


	* g-socthi-vms.adb, g-socthi-vms.ads, g-socthi-vxworks.adb,
	g-socthi-vxworks.ads, g-socthi-mingw.adb, g-socthi-mingw.ads,
	g-socthi.adb, g-socthi.ads, g-socket.adb, g-socket.ads
	(GNAT.Sockets.Thin.C_Readv,
	GNAT.Sockets.Thin.C_Writev): Remove unused subprograms.
	(GNAT.Sockets.Thin.C_Recvmsg,
	GNAT.Sockets.Thin.C_Sendmsg): New bindings to call recvmsg(2) and
	sendmsg(2).  
	(GNAT.Sockets.Receive_Vector, GNAT.Sockets.Send_Vector): Use
	C_Recvmsg/C_Sendmsg rather than Readv/C_Writev.


""",
u"""

	PR tree-optimization/39941
	* tree-ssa-pre.c (eliminate): Schedule update-ssa after
	eliminating an indirect call.

	* gcc.c-torture/compile/pr39941.c: New testcase.

""",
u"""

	* tree-cfg.c (verify_types_in_gimple_reference): Add require_lvalue
	parameter.  Allow invariants as base if !require_lvalue.
	(verify_gimple_assign_single): Adjust.

""",
u"""
Minor clean ups.

""",
u"""

	* sem_disp.adb (Check_Dispatching_Operation): if the dispatching
	operation is a body without previous spec, update the list of
	primitive operations to ensure that cross-reference information is
	up-to-date.

	* sem_ch12.adb (Build_Instance_Compilation_Unit_Nodes): When creating a
	new compilation unit node for the instance declaration, keep the
	context items of the original unit on it, so that the context of the
	instance body only holds the context inherited from the generic body.


	* sem_res.adb: Minor comment fix.


""",
u"""

	* sem_elim.adb: Minor reformatting


	* exp_aggr.adb (Convert_To_Positional): if the current unit is a
	predefined unit, allow arbitrary number of components in static
	aggregate, to ensure that the same level of constant folding applies
	for Ada 95 and Ada 05 versions of the file.


""",
u"""

	* sem_elim.adb (Check_Eliminated): Handle new improved eliminate
	information: no need for full scope check.
	(Eliminate_Error): Do not emit error in a generic context.


	* adaint.c (__gnat_rmdir): return error code if VTHREADS is defined.
	VxWorks 653 POS does not support rmdir.


	* s-stausa.adb, s-stausa.ads: Get_Usage_Range: changing the way
	results are printed.


""",
u"""

	* s-taskin.adb (Initialize): Remove pragma Warnings Off and remove
	unused assignment.


	* make.adb: Minor reformatting.
	Minor code reorganization throughout.


	* s-stausa.ads: Changed visibility of type Task_Result: moved to
	public part to give application visibility over it.
	This is for future improvement and to build a public API on top of it.
	Changed record components name of type Task_Result to reflect the new
	way of reporting. 

	* s-stausa.adb: Actual_Size_Str changed to reflect the new way of
	reporting Stack usage.

	* gnat_ugn.texi: Update doc of stack usage report.

	* g-tastus.ads, s-stusta.ads, s-stusta.adb: New files.

	* Makefile.rtl: Add new run-time files.


""",
u"""

	* initialize.c: Do not expand quoted arguments.


""",
u"""

	* prj-ext.adb, prj.adb, prj.ads: Fix memory leaks.

	* clean.adb (Ultimate_Extension_Of): removed, since duplicate of
	 Prj.Ultimate_Extending_Project_Of


""",
u"""

	* exp_ch7.adb (Build_Final_List): If the designated type is a Taft
	Amendment type, add the with_clause for Finalization.List_Controller
	only if the current context is a package body.


""",
u"""

	* sem_ch12.adb: Minor reformatting

	* sem_aggr.adb: Minor reformatting

	* sem_ch6.adb, sem_cat.ads: Minor reformatting

	* sem_ch10.adb, gnat1drv.adb, prj-nmsc.adb: Minor reformatting


	* prj.ads (Source_Id): Now general pointer type.


""",
u"""

	* exp_ch7.adb, rtsfind.adb: Minor reformatting

	* sem_res.adb: Minor reformatting


""",
u"""

	* sem_res.adb (Static_Concatenation): An N_Op_Concat with static
	operands is static only if it is a predefined concatenation operator.

	* sem_util.adb: Minor reformatting

	* sem_ch12.adb (Save_References): When propagating semantic information
	from generic copy back to generic template, for the case of an
	identifier that has been rewritten to an explicit dereference whose
	prefix is either an object name or a parameterless funcion call
	denoting a global object or function, properly capture the denoted
	global entity: perform the corresponding rewriting in the template,
	and point the rewritten identifier to the correct global entity (not
	to the associated identifier in the generic copy).


""",
u"""

	* rtsfind.adb, prj-env.adb: Minor reformatting
	Minor code reorganization


	* make.adb: Fix comment

	* prj.adb (Ultimate_Extending_Project_Of): Fix handling when no project
	is given as argument, as might happen in gnatmake.


""",
u"""

	* sem_ch3.adb (Check_Abstract_Overriding): Improve error message when
	an abstract operation of a progenitor is not properly overridden by an
	operation of a derived synchronized type.


""",
u"""

	* mlib-prj.adb, mlib-tgt.adb, mlib-tgt.ads, prj-nmsc.adb,
	prj-proc.adb: Minor reformatting
	Minor code reorganization


""",
u"""
Minor message improvement.

""",
u"""

	* exp_ch7.adb (Build_Final_List): For an access type that designates a
	Taft Amendment type, if the access type needs finalization, make sure
	the implicit with clause for List_Controller occurs on the package spec.

	* rtsfind.adb (Text_IO_Kludge): Fine tune the creation of implicit
	with's created for the pseudo-children of Text_IO and friends. In
	particular, avoid cycles, such as Ada.Wide_Text_IO.Integer_IO and
	Ada.Text_IO.Integer_IO both with-ing each other.

	* sem.adb (Walk_Library_Items): Suppress assertion failure in certain
	oddball cases when pragma Extend_System is used.

	* sem_ch12.adb (Get_Associated_Node): Prevent direct 'with' cycles in
	the case where a package spec instantiates a generic whose body with's
	this package, so Walk_Library_Items won't complain about cyclic with's.


	* gnatcmd.adb, prj-proc.adb, make.adb, mlib-prj.adb, prj.adb, prj.ads,
	prj-pp.adb, prj-pp.ads, makeutl.adb, clean.adb, prj-nmsc.adb,
	mlib-tgt.adb, mlib-tgt.ads, prj-util.adb, prj-env.adb, prj-env.ads
	(Project_Id): now a real pointer to Project_Data, instead of an index
	into the Projects_Table. This simplifies the API significantly, avoiding
	extra lookups in this table and the need to pass the Project_Tree_Ref
	parameter in several cases


""",
u"""

	* gcc-interface/Makefile.in: Produce .dSYM files for shared libs on
	darwin.


""",
u"""
gcc/
	* config/bfin/bfin.md (sp_or_sm, spm_string, spm_name): New macro.
	(ss<spm_name>hi3, ss<spm_name>hi3_parts, ss<spm_name>hi3_low_parts,
	ss<spm_name_hi3_high_parts): New patterns, replacing ssaddhi3, ssubhi3,
	ssaddhi3_parts and sssubhi3_parts.
	(flag_mulhi3_parts): Produce a HImode output rather than trying to set
	a VEC_SELECT.
	* config/bfin/bfin.c (bfin_expand_builtin, case BFIN_BUILTIN_CPLX_SQU):
	Adjust accordingly.

gcc/testsuite/
	* gcc.target/bfin/20090411-1.c: New test.


""",
u"""
 
        PR target/39565
        * gcc.dg/pr39565.c: New testcase.

""",
u"""

	* tree-vect-loop.c (get_initial_def_for_induction): Use
	correct types for pointer increment.

""",
u"""
	* gcc.target/i386/sse4_1-roundps-1.c: Skip for vxworks kernel.
	* gcc.target/i386/sse4_1-roundpd-1.c: Likewise.
	* gcc.target/i386/sse4_1-roundps-3.c: Likewise.
	* gcc.target/i386/sse4_1-roundpd-3.c: Likewise.
	* gcc.target/i386/sse4_1-roundss-1.c: Likewise.
	* gcc.target/i386/sse4_1-roundsd-1.c: Likewise.
	* gcc.target/i386/sse4_1-roundss-3.c: Likewise.
	* gcc.target/i386/sse4_1-roundsd-3.c: Likewise.
	* gcc.target/i386/sse4_1-roundps-2.c: Likewise.
	* gcc.target/i386/sse4_1-roundpd-2.c: Likewise.
	* gcc.target/i386/sse4_1-roundss-2.c: Likewise.
	* gcc.target/i386/sse4_1-roundsd-2.c: Likewise.
	* gcc.target/i386/sse4_1-roundss-4.c: Likewise.
	* gcc.target/i386/sse4_1-roundsd-4.c: Likewise.
	* gcc.target/i386/pr37191.c: Likewise.
	* gcc.target/i386/reload-1.c: Likewise.
	* g++.old-deja/g++.pt/repo1.C: Skip for vxworks kernel.
	* g++.old-deja/g++.pt/repo2.C: Likewise.
	* g++.old-deja/g++.pt/repo3.C: Likewise.
	* g++.old-deja/g++.pt/repo4.C: Likewise.
	* g++.old-deja/g++.pt/instantiate4.C: Likewise.
	* g++.old-deja/g++.pt/instantiate6.C: Likewise.
	* g++.dg/template/repo1.C: Likewise.
	* g++.dg/template/repo2.C: Likewise.
	* g++.dg/template/repo3.C: Likewise.
	* g++.dg/template/repo4.C: Likewise.
	* g++.dg/template/repo5.C: Likewise.
	* g++.dg/template/repo6.C: Likewise.
	* g++.dg/template/repo7.C: Likewise.
	* g++.dg/template/repo8.C: Likewise.
	* g++.dg/template/repo9.C: Likewise.
	* g++.dg/rtti/repo1.C: Likewise.	
	* gcc.dg/cpp/_Pragma6.c: Skip for vxworks.
	* g++.dg/cpp/_Pragma1.C: Skip for vxworks.
	* gcc.dg/pthread-init-1.c: Xfail for vxworks rtp.
	* g++.dg/other/PR23205.C: Skip for vxworks.
	* g++.dg/ext/visibility/class1.C: Requires PIC.
	* g++.dg/eh/async-unwind2.C: Requires PIC.
	* lib/target-supports.exp (check_cxa_atexit_available): Vxworks
	does not have cxa_exit.

""",
u"""

	PR libstdc++/39868
	* scripts/run_doxygen: Uncomment removal of includes.
	(problematic): Rewrite __cxxabiv1 namespace to abi.


""",
u"""
	* toplev.c (print_version): Update GMP version string calculation.


""",
u"""
Daily bump.
""",
u"""
	PR rtl-optimization/39938
	* resource.c (init_resource_info): Add call to df_analyze.

""",
u"""
	PR testsuite/39790
	* lib/target-supports.exp (check_effective_target_tls): Remove
	comment of caching.
	(check_effective_target_tls_native): Likewise.
	(check_effective_target_tls_runtime): Likewise.
	* gcc.dg/tls/alias-1.c (dg-require-effective-target): Change target
	tls to tls_runtime.
	* gcc.dg/tls/opt-2.c: Add dg-require-effective-target tls_runtime.


""",
u"""
	* config/alpha/alpha.md (usegp): Cast the result of
	alpha_find_lo_sum_using_gp to enum attr_usegp.
	* config/alpha/alpha.c (override_options): Remove end-of-structure
	marker element from cpu_table.  Use array size of cpu_table to handle
	-mcpu and -mtune options.
	(tls_symbolic_operand_type): Change 0 to TLS_MODEL_NONE.


""",
u"""
	* config.gcc (powerpc*-*-* | rs6000-*-*): Add
	rs6000/option-defaults.h to tm_file.  Support cpu_32, cpu_64,
	tune_32 and tune_64.
	* doc/install.texi (--with-cpu-32, --with-cpu-64): Document
	support on PowerPC.
	* config/rs6000/rs6000.h (OPTION_DEFAULT_SPECS): Move to ...
	* config/rs6000/option-defaults.h: ... here.  New file.
	(OPT_64, OPT_32): Define.
	(MASK_64BIT): Define to 0 if not already defined.
	(OPT_ARCH64, OPT_ARCH32): Define.
	(OPTION_DEFAULT_SPECS): Add entries for cpu_32, cpu_64, tune_32
	and tune_64.

""",
u"""
Fix nits
""",
u"""
FPA error for AAPCS
""",
u"""

	PR fortran/39946
	* resolve.c (resolve_symbol): Correctly copy the interface of a
	PROCEDURE statement if the interface involves a RESULT variable.



	PR fortran/39946
	* gfortran.dg/proc_ptr_16.f90: New.


""",
u"""
	PR rtl-optimization/39914
	* ira-conflicts.c (ira_build_conflicts): Prohibit call used
	registers for allocnos created from user-defined variables only
	when not optimizing.


""",
u"""
	* testsuite/gcc.target/ia64/sync-1.c: Check for cmpxchg8 only if
	lp64 is true.

""",
u"""
Forgot to ci fixincl.x in previous checkin.

""",
u"""

	PR middle-end/39937
	* fold-const.c (fold_binary): Use distribute_real_division only
	on float types.

	* gfortran.fortran-torture/compile/pr39937.f: New testcase.

""",
u"""
	* config.gcc (hppa*64*-*-hpux11*): Set use_gcc_stdint and
	add hpux-stdint.h to tm_file.
	(hppa[12]*-*-hpux11*): Ditto.
	(ia64*-*-hpux*): Ditto.
	* config/hpux-stdint.h: New.
	* gcc/config/ia64/hpux.h (TARGET_OS_CPP_BUILTINS): Set
	__STDC_EXT__ for all compiles.
	* gcc/config/pa/pa-hpux.h: Ditto.
	* gcc/config/pa/pa-hpux10.h: Ditto.
	* gcc/config/pa/pa-hpux11.h: Ditto.

""",
u"""
	* inclhack.def (hpux11_uint32_c): Remove.
	(hpux_long_double): Disable on hpux11.3*.
	(hpux_long_double_2): New.
	(hpux_c99_intptr): New.
	(hpux_c99_inttypes): New.
	(hpux_c99_inttypes2): New.
	(hpux_stdint_least): New.
	(hpux_stdint_fast): New.
	(hpux_inttype_int_least8_t): New.
	(hpux_inttype_int8_t): New.
	* fixincl.x: Regenerate.
	* tests/base/sys/_inttypes.h: New.
	* tests/base/inttypes.h: Update.
	* tests/base/stdlib.h: Update.
	* tests/base/stdint.h: Update.

""",
u"""

        * debug.h (set_name): Add comment.

""",
u"""
	* testsuite/libjava.jvmti/jvmti-interp.exp
	(gcj_jni_compile_c_to_so):  Fix so extension to '.dll' on win32.
	* testsuite/lib/libjava.exp (libjava_init):  Likewise.
	* testsuite/libjava.jni/jni.exp
	(gcj_jni_compile_c_to_so):  Likewise.
	(gcj_jni_test_one):  Likewise.


""",
u"""

        PR target/39929
        * config/darwin.c (machopic_gen_offset): Check
        currently_expanding_to_rtl if current_ir_type returns IR_GIMPLE.
        * config/arm/arm.c (require_pic_register): Likewise.




""",
u"""

	g++.dg/warn/pr35652.C: Removed.
	gcc.dg/pr35652.c: Likewise.

""",
u"""

        * config/m32c/m32c.c (TARGET_PROMOTE_FUNCTION_RETURN,
        m32c_promote_function_return, TARGET_PROMOTE_PROTOTYPES,
        m32c_promote_prototypes): Delete.

""",
u"""
        PR middle-end/39922
        * tree-outof-ssa.c (insert_value_copy_on_edge): Don't convert
        constants.

""",
u"""

	* tree-vect-stmts.c (vect_get_vec_def_for_operand): Fix
	type error.

""",
u"""
Add support for arm1156tf-s
""",
u"""
	* inclhack.def (glibc_stdint): New fix.
	* fixincl.x: Regenerate.
	* tests/base/stdint.h: Update.

""",
u"""
gcc/testsuite/Changelog:

	* gcc.target/ia64/20071210-2.c: New testcase.

gcc/Changelog:

	* sel-sched-ir.c (maybe_tidy_empty_bb): Do not attempt to delete a
	block if there are complex incoming edges.
	(sel_merge_blocks): Remove useless assert.
	(sel_redirect_edge_and_branch): Check that edge was redirected.
	* sel-sched-ir.h (_eligible_successor_edge_p): Remove assert.
	(sel_find_rgns): Delete declaration.
	* sel-sched.c (purge_empty_blocks): Attempt to remove first block of
	the region when it is not a preheader.


""",
u"""
	PR c/39323
	* config/alpha/elf.h (MAX_OFILE_ALIGNMENT): Sync with elfos.h

testsuite/ChangeLog:

	PR c/39323
	* gcc.dg/pr39323-2.c: Also scan for alignment in log2 format.
	* gcc.dg/pr39323-3.c: Ditto.


""",
u"""

	PR fortran/39930
	PR fortran/39931
	* expr.c (gfc_check_pointer_assign): Correctly detect if the left hand
	side is a pointer.
	* parse.c (gfc_fixup_sibling_symbols): Don't check for ambiguity.



	PR fortran/39930
	PR fortran/39931
	* gfortran.dg/ambiguous_reference_2.f90: New.
	* gfortran.dg/pointer_assign_7.f90: New.


""",
u"""

        PR libgcj/39899
        * Makefile.am (libgcj_tools_la_LDFLAGS): Add
        -fno-bootstrap-classes to libgcj_tools_la_GCJFLAGS.
        * Makefile.in: Regenerate.


""",
u"""

	* tree.h (SSA_NAME_VALUE): Remove.
	(struct tree_ssa_name): Remove value_handle member.
	* tree-vrp.c (execute_vrp): Initialize/free the value-handle
	array for jump threading.
	* tree-ssa-propagate.c (ssa_prop_init): Do not initialize
	SSA_NAME_VALUEs.
	* print-tree.c (print_node): Do not dump SSA_NAME_VALUEs.
	* tree-flow.h (threadedge_initialize_values): Declare.
	(threadedge_finalize_values): Likewise.
	* tree-ssa-threadedge.c (ssa_name_values): New global variable.
	(SSA_NAME_VALUE): Define.
	(threadedge_initialize_values): New function.
	(threadedge_finalize_values): Likewise.
	* tree-ssa-dom.c (ssa_name_values): New global variable.
	(SSA_NAME_VALUE): Define.
	(tree_ssa_dominator_optimize): Initialize/free the value-handle
	array.

""",
u"""

	* gcc.target/powerpc/20020118-1.c: Skip on vxworks targets.
	* gcc.dg/20020103-1.c: Check for __ppc.
	* gcc.dg/asm-b.c: Check for __ppc.
	* gcc.dg/20020919-1.c: Check for __ppc.
	* gcc.dg/20020312-2.c: Likewise.
	* gcc.dg/trampoline-1.c: Add appropriate NO_TRAMPOLINES #ifndefs.
	* gcc.dg/torture/asm-subreg-1.c: Skip on sparc vxworks targets.
	* gcc.dg/attr-weakref-1.c: Skip on selected vxworks targets.
	* g++.dg/warn/weak1.C: Likewise.
	* gcc.dg/tree-ssa/20030714-1.c (find_base_value): Declare as
	static so appropriate optimizations kick in.
	(find_base_value_wrapper): New function.
	* g++.dg/eh/simd-5.C: Fix target triplet.
	* gcc.target/arm/long-calls-1.c: Skip for -mlong-calls.

""",
u"""

	* tree-vect-loop-manip.c (vect_create_cond_for_alias_checks):
	Use REPORT_VECTORIZED_LOCATIONS instead 
	REPORT_VECTORIZED_LOOPS.
	* tree-vectorizer.c (vect_verbosity_level): Make static.
	(vect_loop_location): Rename to vect_location.
	(vect_set_verbosity_level): Update comment.
	(vect_set_dump_settings): Use REPORT_VECTORIZED_LOCATIONS
	and vect_location.
	(vectorize_loops): Fix comment. Use REPORT_VECTORIZED_LOCATIONS
	and vect_location. Use REPORT_UNVECTORIZED_LOCATIONS
	instead REPORT_UNVECTORIZED_LOOPS.
	* tree-vectorizer.h (enum vect_def_type): Rename vect_invariant_def and
	vect_loop_def to vect_external_def and vect_internal_def.
	(enum verbosity_levels): Rename REPORT_VECTORIZED_LOOPS
        and REPORT_UNVECTORIZED_LOOPS to 
	REPORT_VECTORIZED_LOCATIONS and 
	REPORT_UNVECTORIZED_LOCATIONS.
	(enum vect_relevant): Update comment. Rename vect_unused_in_loop
	and vect_used_in_loop and to vect_unused_in_scope and 
	vect_used_in_scope.
	(STMT_VINFO_RELEVANT_P): Use vect_unused_in_scope.
	(vect_verbosity_level): Remove declaration.
	(vect_analyze_operations): Likewise.
	(vect_analyze_stmt): Declare.
	* tree-vect-loop.c (vect_determine_vectorization_factor): Use
	REPORT_UNVECTORIZED_LOCATIONS.
	(vect_get_loop_niters): Fix indentation.
	(vect_analyze_loop_form): Use REPORT_UNVECTORIZED_LOCATIONS.
	(vect_analyze_loop_operations): New function.
	(vect_analyze_loop): Call vect_analyze_loop_operations instead of
	vect_analyze_operations.
	(vect_is_simple_reduction): Use new names.
	(vectorizable_live_operation, vect_transform_loop): Likewise.
	* tree-vect-data-refs.c (vect_check_interleaving): Add a return value to
	specify whether the data references can be a part of interleaving chain.
	(vect_analyze_data_ref_dependence): Use new names.
	(vect_analyze_data_refs_alignment, vect_analyze_data_refs): Likewise.
	(vect_create_addr_base_for_vector_ref): Remove redundant code.
	* tree-vect-patterns.c (widened_name_p): Use new names.
	(vect_recog_dot_prod_pattern): Likewise.
	* tree-vect-stmts.c (vect_stmt_relevant_p): Use new names.
	(process_use, vect_mark_stmts_to_be_vectorized, 
	vect_model_simple_cost, vect_model_store_cost,
	vect_get_vec_def_for_operand, vect_get_vec_def_for_stmt_copy,
	vectorizable_call, vectorizable_conversion, vectorizable_assignment,
	vectorizable_operation, vectorizable_type_demotion,
	vectorizable_type_promotion, vectorizable_store, vectorizable_load,
	vectorizable_condition): Likewise.
	(vect_analyze_operations): Split into vect_analyze_loop_operations
	and ...
	(vect_analyze_stmt): ... new function.
	(new_stmt_vec_info): Use new names.
	(vect_is_simple_use): Use new names and fix comment.
	* tree-vect-slp.c (vect_get_and_check_slp_defs): Use new names.
	(vect_build_slp_tree, vect_analyze_slp, vect_schedule_slp): Likewise.


""",
u"""
	PR target/39911
	* config/i386/i386.c (print_operand) ['Z']: Handle floating point
	and integer modes for x87 operands.  Do not ICE for unsupported size,
	generate error instead.  Generate error for unsupported operand types.
	['z']: Do not handle HImode memory operands specially.  Warning
	for floating-point operands.  Fallthru to 'Z' for unsupported operand
	types.  Do not ICE for unsupported size, generate error instead.
	(output_387_binary_op): Use %Z to output operands.
	(output_fp_compare): Ditto.
	(output_387_reg_move): Ditto.

testsuite/ChangeLog:

	PR target/39911
	* gcc.target/i386/pr39911.c: New test.


""",
u"""

	PR fortran/39879
	* trans_expr.c (gfc_conv_procedure_call): Deep copy a derived
	type parentheses argument if it is a variable with allocatable
	components.


	PR fortran/39879
	* gfortran.dg/alloc_comp_assign_10.f90: New test.

""",
u"""

	PR fortran/39879
	* trans_expr.c (gfc_conv_procedure_call): Deep copy a derived
	type parentheses argument if it is a variable with allocatable
	components.


	PR fortran/39879
	* gfortran.dg/alloc_comp_assign_10.f90: New test.

""",
u"""
Revert:
	PR c++/35652

gcc/
	* builtins.c (c_strlen): Do not warn here.
	* c-typeck.c (build_binary_op): Adjust calls to pointer_int_sum.
	* c-common.c (pointer_int_sum): Take an explicit location.
	Warn about offsets out of bounds.
	* c-common.h (pointer_int_sum): Adjust declaration.

cp/
	* typeck.c (cp_pointer_sum): Adjust call to pointer_int_sum.

testsuite/
	* gcc.dg/pr35652.C: New.
	* g++.dg/warn/pr35652.C: New.
	* gcc.dg/format/plus-1.c: Adjust message.

""",
u"""
	* interpret.cc (DEBUG):  Rename this ...
	(__GCJ_DEBUG):  ... to this throughout.
	* configure.ac:  Likewise.
	* interpret-run.cc:  Likewise.
	* prims.cc:  Likewise.
	* gnu/classpath/natConfiguration.cc:  Likewise.
	* include/java-assert.h:  Likewise.
	* java/io/natVMObjectInputStream.cc:  Likewise.

	* configure:  Regenerate.
	* include/config.h.in:  Regenerate.


""",
u"""
	* java/lang/natVMClassLoader.cc
	(java::lang::VMClassLoader::defineClass):  Fix assert.


""",
u"""
Daily bump.
""",
u"""
Fix date

""",
u"""
* lib/target-supports.exp (check_effective_target_double64): New.
(check_effective_target_double64plus): New.
(check_effective_target_large_double): New.
* gcc.dg/Wconversion-real-integer.c: Require double64plus.
* gcc.dg/div-double-1.c: Likewise.
* gcc.dg/Wconversion-real.c: Require large_double.
* gcc.dg/cdce1.c: Require large_double instead of checking targets.

* gcc.c-torture/execute/ieee/unsafe-fp-assoc-1.c: Skip if doubles are too small.

* gcc.c-torture/execute/ieee/20010226-1.c: Mark all floating point
constants as long.

""",
u"""
Fix formatting
""",
u"""
./:
	* collect2.c (is_ctor_dtor): Change type of ret field in struct
	names to symkind.
	* dce.c (run_fast_df_dce): Change type of old_flags to int.
	* df-core.c (df_set_flags): Change return type to int.  Change
	type of old_flags to int.
	(df_clear_flags): Likewise.
	* df-scan.c (df_def_record_1): Change 0 to VOIDmode.
	(df_get_conditional_uses): Likewise.
	* df.h (df_set_flags, df_clear_flags): Update declarations.
	* dwarf2out.c (struct indirect_string_node): Change type of form
	field to enum dwarf_form.
	(AT_string_form): Change return type to enum dwarf_form.
	* fixed-value.c (fixed_compare): Add cast to enum type.
	* fwprop.c (update_df): Change 0 to VOIDmode.
	* gensupport.c: Change 0 to UNKNOWN.
	* gimple.h (gimple_cond_code): Add cast to enum type.
	* haifa-sched.c (reemit_notes): Add cast to enum type.
	* hooks.c (hook_int_void_no_regs): Remove function.
	* hooks.h (hook_int_void_no_regs): Remove declaration.
	* optabs.c (expand_widen_pattern_expr): Change 0 to VOIDmode.
	* predict.c (combine_predictions_for_insn): Add casts to enum
	type.
	* real.c (real_arithmetic): Add cast to enum type.
	(real_compare): Likewise.
	* target.h (struct gcc_target): Change return type of
	branch_target_register_class to enum reg_class.
	* target-def.h (TARGET_BRANCH_TARGET_REGISTER_CLASS): Define as
	default_branch_target_register_class.
	* targhooks.c (default_branch_target_register_class): New
	function.
	* targhooks.h (default_branch_target_register_class): Declare.
	* tree-data-ref.c (print_direction_vector): Add cast to enum
	type.
	* tree-vect-data-refs.c (vect_supportable_dr_alignment): Remove
	cast to int.
	* tree-vect-loop.c (vect_create_epilog_for_reduction): Change 0 to
	ERROR_MARK.
	* tree-vect-slp.c (vect_build_slp_tree): Change 0 to
	vect_uninitialized_def.  Change 0 to ERROR_MARK.
	* tree-vect-stmts.c (supportable_widening_operation): Don't
	initialize icode1 and icode2.
	* tree-vectorizer.h (enum vect_def_type): Add
	vect_uninitialized_def.
	* config/sol2-c.c (cmn_err_length_specs): Change 0 to FMT_LEN_none
	and to STD_C89.
	(cmn_err_flag_specs): Change 0 to STD_C89.
	(cmn_err_char_table): Likewise.
	* config/arm/arm.c (get_arm_condition_code): Change type of code
	to enum arm_cond_code.
	(IWMMXT_BUILTIN): Change 0 to UNKNOWN.
	(IWMMXT_BUILTIN2): Likewise.
	(neon_builtin_type_bits): Don't define typedef.
	(neon_builtin_datum): Change type of bits field to int.
	(arm_expand_neon_args): Add cast to enum type.
	* config/ia64/ia64.c (tls_symbolic_operand_type): Change 0 to
	TLS_MODEL_NONE.
	* config/i386/i386.c (bdesc_multi_arg): Change 0 to UNKNOWN.  Add
	casts to enum type.
	* config/mips/mips.c (LOONGSON_BUILTIN_ALIAS): Change 0 to
	MIPS_FP_COND_f.
	* config/mips/mips.md (jal_macro): Return enum constant.
	(single_insn): Likewise.
	* config/rs6000/rs6000.c (bdesc_altivec_preds): Change 0 to
	CODE_FOR_nothing.
	* config/rs6000/rs6000-c.c (altivec_overloaded_builtins): Add
	casts to enum type.
	* config/s390/s390.c (s390_tune_flags): Change type to int.
	(s390_arch_flags): Likewise.
	(s390_handle_arch_option): Change flags field of struct pta to
	int.
	* config/s390/s390.h (s390_tune_flags): Update declaration.
	(s390_arch_flags): Likewise.
	* config/sh/sh.c (prepare_move_operands): Compare
	tls_symbolic_operand result with enum constant.
	(sh_reorg): Change PUT_MODE to PUT_REG_NOTE_KIND.
	(sh_expand_prologue): Add cast to enum type.
	(sh_expand_epilogue): Likewise.
	(tls_symbolic_operand): Change return type to enum tls_model.
	(fpscr_set_from_mem): Add cast to enum type.
	(legitimize_pic_address): Compare tls_symbolic_operand result with
	enum constant.
	(sh_target_reg_class): Change return type to enum reg_class.
	* config/sh/sh.h (OVERRIDE_OPTIONS): Change CPU_xxx to
	PROCESSOR_xxx.
	* config/sh/sh-protos.h (tls_symbolic_operand): Update
	declaration.
	* config/sparc/sparc.c (sparc_override_options): Add cast to enum
	type.
	* config/sparc/sparc.md (empty_delay_slot): Return enum constant.
	(pic, calls_alloca, calls_eh_return, leaf_function): Likewise.
	(delayed_branch, tls_call_delay): Likewise.
	(eligible_for_sibcall_delay): Likewise.
	(eligible_for_return_delay): Likewise. 
	* config/spu/spu.c (expand_builtin_args): Add cast to enum type.
	(spu_expand_builtin_1): Likewise.

	* c-typeck.c (convert_for_assignment): Issue -Wc++-compat warnings
	for all types of conversions.
	(output_init_element): Issue -Wc++-compat warning if needed when
	initializing a bitfield with enum type.
	* c-parser.c (c_parser_expression): Set original_type to
	original_type of right hand operand of comman operator.
cp/:
	* semantics.c (finish_omp_clauses): Change type of c_kind to enum
	omp_clause_code.
fortran/:
	* trans-intrinsic.c (DEFINE_MATH_BUILTIN): Add casts to enum
	type.
	* trans-io.c (st_parameter_field): Add casts to enum type.
java/:
	* builtins.c (java_builtins): Add casts to enum type.
	* verify-impl.c (check_class_constant): Add cast to enum type.
	(check_constant, check_wide_constant): Likewise.
objc/:
	* objc-act.c (objc_gimplify_expr): Add casts to enum type.
testsuite/:
	* gcc.dg/Wcxx-compat-5.c: New testcase.
	* gcc.dg/Wcxx-compat-6.c: New testcase.

""",
u"""
gcc/
	* doc/c-tree.texi (Types, Functions, Expression trees): Fix
	grammar nits.
	* doc/cfg.texi (Maintaining the CFG, Liveness information):
	Likewise.
	* doc/cpp.texi (Standard Predefined Macros)
	(Implementation-defined behavior): Likewise.
	* doc/extend.texi (Function Attributes, Type Attributes):
	Likewise.
	* doc/gimple.texi (GIMPLE Exception Handling)
	(@code{GIMPLE_ASSIGN}): Likewise.
	* doc/install.texi (Prerequisites, Configuration, Specific):
	Likewise.
	* doc/invoke.texi (Warning Options, Optimize Options)
	(AVR Options, Darwin Options): Likewise.
	(Optimize Options): Reformulate -fwhole-program description.
	* doc/loop.texi (Lambda): Likewise.
	* doc/md.texi (Output Template, Define Constraints)
	(Standard Names, Insn Splitting): Likewise.
	* doc/options.texi (Option properties): Likewise.
	* doc/passes.texi (Tree-SSA passes): Likewise.
	* doc/rtl.texi (Side Effects, Assembler, Insns): Likewise.
	* doc/tm.texi (Register Classes, Old Constraints, Scalar Return)
	(File Names and DBX): Likewise.
	* doc/trouble.texi (Incompatibilities): Likewise.


""",
u"""
* MAINTAINERS: Update my e-mail address.

""",
u"""
	* spu.c (spu_machine_dependent_reorg): Make sure branch label on hint
	instruction is correct.

""",
u"""
	PR testsuite/39807
	* dg-extract-results.sh: Close open files and use >> instead of >
	to decrease number of concurrently open files from awk.  Avoid
	= at the beginning of a regexp and redirect to a file determined
	by curfile variable rather than concatenated strings to workaround
	Solaris nawk bug.

""",
u"""
	Allow non-constant arguments to conversion intrinsics.
	* spu-protos.h (exp2_immediate_p, spu_gen_exp2): Declare.
	* predicates.md (spu_inv_exp2_operand, spu_exp2_operand): New.
	* spu.c (print_operand): Handle 'v' and 'w'.
	(exp2_immediate_p, spu_gen_exp2): Define.
	* spu-builtins.def (spu_convts, spu_convtu, spu_convtf_0,
	spu_convtf_1): Update parameter descriptions.
	* spu-builtins.md (spu_csflt, spu_cuflt, spu_cflts, spu_cfltu):
	Update.
	* constraints.md ('v', 'w'): New.
	* spu.md (UNSPEC_CSFLT, UNSPEC_CFLTS, UNSPEC_CUFLT, UNSPEC_CFLTU):
	Remove.
	(i2f, I2F): New define_mode_attr.
	(floatsisf2, floatv4siv4sf2, fix_truncsfsi2, fix_truncv4sfv4si2,
	floatunssisf2, floatunsv4siv4sf2, fixuns_truncsfsi2,
	fixuns_truncv4sfv4si2):  Update to use mode attribute.
	(float<mode><i2f>2_mul, float<mode><i2f>2_div,
	fix_trunc<mode><f2i>2_mul, floatuns<mode><i2f>2_mul,
	floatuns<mode><i2f>2_div, fixuns_trunc<mode><f2i>2_mul): New
	patterns for combine.
	* gcc.target/spu/intrinsics-3.c: Update tests.

""",
u"""
	* dbgcnt.def (cprop1, cprop2, gcse, jump_bypass): Remove
	(cprop, hoist, pre, store_motion): New debug counters.
	* tree-pass.h (pass_tracer): Move to list of gimple passes, it
	is not an RTL pass anymore.
	(pass_profiling): Remove extern decl for pass removed in 2005.
	(pass_gcse, pass_jump_bypass): Remove.
	* final.c (rest_of_clean_state): Set flag_rerun_cse_after_global_opts
	to 0 for clean state.
	* toplev.h (flag_rerun_cse_after_global_opts): Add extern declaration.
	* cse.c (gate_handle_cse_after_global_opts,
	rest_of_handle_cse_after_global_opts): New functions.
	(pass_cse_after_global_opts): New pass, does local CSE.
	* timevar.def (TV_GCSE, TV_CPROP1, TV_CPROP2, TV_BYPASS): Remove.
	(TV_CPROP): New timevar.
	* gcse.c (flag_rerun_cse_after_global_opts): New global variable.
	(run_jump_opt_after_gcse, max_gcse_regno): Remove global vars.
	(gcse_main, recompute_all_luids): Remove.
	(compute_hash_table_work): Call max_reg_num instead of reading
	max_gcse_regno.
	(cprop_jump): Don't set run_jump_opt_after_gcse.
	(constprop_register): Always allow to alter jumps.
	(cprop_insn): Likewise.
	(do_local_cprop): Likewise.
	(local_cprop_pass): Likewise.  Return non-zero if something changed.
	(cprop): Remove function, fold interesting bits into one_cprop_pass.
	(find_implicit_sets): Add note about missed optimization opportunity.
	(one_cprop_pass): Rewrite to be "the" CPROP pass, called from the
	pass_rtl_cprop execute function.
	Don't bother tracking the pass number, each pass gets its own dumpfile
	now anyway.
	Always allow to alter jumpsand bypass jumps.
	(bypass_block): Don't ignore regno >= max_gcse_regno, find_bypass_set
	will just find no suitable set.
	(pre_edge_insert): Fix dumping, this function is for PRE only.
	(one_pre_gcse_pass): Rewrite to be "the" PRE pass, called from the
	pass_rtl_pre execute function.
	(hoist_code): Return non-zero if something changed.  Keep track of
	substitutions and insertions for statistics gathering similar to PRE.
	(one_code_hoisting_pass): Rewrite to be "the" code hoisting pass,
	called from the pass_rtl_hoist execute function.  Show pass statistics.
	(compute_store_table): Use max_reg_num directly instead of using the
	formerly global max_gcse_regno.
	(build_store_vectors): Likewise.
	(replace_store_insn): Fix dumping.
	(store_motion): Rename to ...
	(one_store_motion_pass): ... this.  Rewrite to be "the" STORE_MOTION
	pass, called from the pass_rtl_store_motion execute function.  Keep
	track of substitutions and insertions for statistics gathering similar
	to PRE.
	(bypass_jumps): Remove, fold interesting bits into ...
	(one_cprop_pass): ... this.  Rewrite to be "the" CPROP pass, called
	from the pass_rtl_cprop execute function.
	(gate_handle_jump_bypass, rest_of_handle_jump_bypass,
	pass_jump_bypass): Remove.
	(gate_handle_gcse, rest_of_handle_gcse): Remove.
	(gate_rtl_cprop, execute_rtl_cprop, pass_rtl_cprop): New.
	(gate_rtl_pre, execute_rtl_pre, pass_rtl_pre): New.
	(gate_rtl_hoist, execute_rtl_hoist, pass_rtl_hoist): New.
	(gate_rtl_store_motion, execute_rtl_store_motion,
	pass_rtl_store_motion): New.
	* common.opt: Remove flag_cse_skip_blocks, adjust documentation to
	make it clear that -fcse-skip-blocks is a no-op for backward compat.
	* passes.c (init_optimization_passes): Remove pass_gcse and
	pass_jump_bypass.  Schedule cprop, pre, hoist, cprop, store_motion,
	and cse_after_global_opts in place of pass_gcse.  Schedule cprop
	instead of pass_jump_bypass.


""",
u"""

	PR middle-end/39928
	* gimplify.c (gimplify_expr): If we are required to create
	a temporary make sure it ends up as register.

	* gcc.c-torture/compile/pr39928-1.c: New testcase.
	* gcc.c-torture/compile/pr39928-2.c: Likewise.

""",
u"""
        * MAINTAINERS: Replace Aldy Hernandez as a maintainer for the FRV.

""",
u"""
gcc/


	PR target/39903
	* config/i386/i386.c (construct_container): Don't call
	gen_reg_or_parallel with BLKmode on X86_64_SSE_CLASS,
	X86_64_SSESF_CLASS and X86_64_SSEDF_CLASS.

gcc/testsuite/


	PR target/39903
	* gcc.dg/torture/pr39903-1.c: New.
	* gcc.dg/torture/pr39903-2.c: Likewise.

""",
u"""
Add dump file checks for sms tests
""",
u"""
	* ssaexpand.h (struct ssaexpand): Member 'values' is a bitmap.
	(get_gimple_for_ssa_name): Adjust, lookup using SSA_NAME_DEF_STMT.
	* tree-ssa-live.h: (find_replaceable_exprs): Return a bitmap.
	(dump_replaceable_exprs): Take a bitmap.
	* cfgexpand.c (gimple_cond_pred_to_tree): Handle bitmap instead of
	array.
	(expand_gimple_basic_block): Likewise.
	* tree-ssa-ter.c (struct temp_expr_table_d): Make
	replaceable_expressions member a bitmap.
	(free_temp_expr_table): Pass back and deal with bitmap, not gimple*.
	(mark_replaceable): Likewise.
	(find_replaceable_in_bb, dump_replaceable_exprs): Likewise.
	* tree-outof-ssa.c (remove_ssa_form): 'values' is a bitmap.

""",
u"""

	* tree-cfg.c (remove_useless_stmts): Verify stmts afterwards.
	(verify_stmts): Dispatch to gimple/type verification code.
	* tree-inline.c (remap_gimple_op_r): Work around C++ FE
	issue with call argument types.

	java/
	PR java/38374
	* constants.c (build_constants_constructor): Retain the old
	pointer type as valid TYPE_POINTER_TO after patching the
	type of the constant pool decl.

""",
u"""
        * tree-into-ssa.c (regs_to_rename, mem_syms_to_rename): Remove.
        (init_update_ssa, delete_update_ssa, update_ssa): Remove references
        to above.

""",
u"""
	* resource.c (find_basic_block): Use BLOCK_FOR_INSN to look up
	a label's basic block.
	(mark_target_live_regs): Tidy and rework obsolete comments.
	Change back DF problem to LIVE.  If a label starts a basic block,
	assume that all registers that used to be live then still are.
	(init_resource_info): If a label starts a basic block, set its
	BLOCK_FOR_INSN accordingly.
	(fini_resource_info): Undo the setting of BLOCK_FOR_INSN.

""",
u"""

	* tree-flow-inline.h (function_ann): Remove.
	(get_function_ann): Likewise.
	* tree-dfa.c (create_function_ann): Remove.
	* tree-flow.h (struct static_var_ann_d): Remove.
	(struct function_ann_d): Likewise.
	(union tree_ann_d): Remove fdecl member.
	(function_ann_t): Remove.
	(function_ann, get_function_ann, create_function_ann): Remove
	declarations.

""",
u"""
	* config/alpha/alpha.c (code_for_builtin): Declare as enum insn_code.


""",
u"""
	PR c++/39875
	* cvt.c (convert_to_void) <case INDIRECT_REF>: Only warn about
	-Wunused-value if implicit.

	* g++.dg/warn/Wunused-15.C: New test.

""",
u"""
Daily bump.
""",
u"""
	* ipa-pure-const.c (struct funct_state_d): New fields
	state_previously_known, looping_previously_known; remove
	state_set_in_source.
	(analyze_function): Use new fields.
	(propagate): Avoid assumption that state_set_in_source imply
	nonlooping.

	* tree-ssa-loop-niter.c (finite_loop_p): New function.
	* tree-ssa-loop-ivcanon.c (empty_loop_p): Use it.
	* cfgloop.h (finite_loop_p): Declare.

""",
u"""
* tree-flow.h (tree_ann_common_d): Remove aux and value_handle members.

""",
u"""
	* tree-pass.h (pass_del_ssa, pass_mark_used_blocks,
	pass_free_cfg_annotations, pass_free_datastructures): Remove decls.
	* gimple-low.c (mark_blocks_with_used_vars, mark_used_blocks,
	pass_mark_used_blocks): Remove.
	* tree-optimize.c (pass_free_datastructures,
	execute_free_cfg_annotations, pass_free_cfg_annotations): Remove.
	* passes.c (init_optimization_passes): Don't call
	pass_mark_used_blocks, remove dead code.

""",
u"""

	* tree-outof-ssa.c (rewrite_trees): Add ATTRIBUTE_UNUSED.
	* tree-ssa-live.h (register_ssa_partition): Likewise.

""",
u"""
gcc/
        Expand from SSA.
	* builtins.c (fold_builtin_next_arg): Handle SSA names.
	* tree-ssa-copyrename.c (rename_ssa_copies): Use ssa_name() directly.
	* tree-ssa-coalesce.c (create_outofssa_var_map): Mark only useful
	SSA names. 
	(compare_pairs): Swap cost comparison.
	(coalesce_ssa_name): Don't use change_partition_var.
	* tree-nrv.c (struct nrv_data): Add modified member.
	(finalize_nrv_r): Set it.
	(tree_nrv): Use it to update statements.
	(pass_nrv): Require PROP_ssa.
	* tree-mudflap.c (mf_decl_cache_locals,
	mf_build_check_statement_for): Use make_rename_temp.
	(pass_mudflap_2): Require PROP_ssa, run ssa update at finish.
	* alias.c (find_base_decl): Handle SSA names.
	* emit-rtl (set_reg_attrs_for_parm): Make non-static.
	(component_ref_for_mem_expr): Don't leak SSA names into RTL.
	* rtl.h (set_reg_attrs_for_parm): Declare.
	* tree-optimize.c (pass_cleanup_cfg_post_optimizing): Rename
	to "optimized", remove unused locals at finish.
	(execute_free_datastructures): Make global, call
	delete_tree_cfg_annotations.
	(execute_free_cfg_annotations): Don't call
	delete_tree_cfg_annotations.

	* ssaexpand.h: New file.
	* expr.c (toplevel): Include ssaexpand.h.
	(expand_assignment): Handle SSA names the same as register
	variables.
	(expand_expr_real_1): Expand SSA names.
	* cfgexpand.c (toplevel): Include ssaexpand.h.
	(SA): New global variable.
	(gimple_cond_pred_to_tree): Fold TERed comparisons into predicates.
	(SSAVAR): New macro.
	(set_rtl): New helper function.
	(add_stack_var): Deal with SSA names, use set_rtl.
	(expand_one_stack_var_at): Likewise.
	(expand_one_stack_var): Deal with SSA names.
	(stack_var_size_cmp): Use code (SSA_NAME / DECL) as tie breaker
	before unique numbers.
	(expand_stack_vars): Use set_rtl.
	(expand_one_var): Accept SSA names, add asserts for them, feed them
	to above subroutines.
	(expand_used_vars): Expand all partitions (without default defs),
	then only the local decls (ignoring those expanded already).
	(expand_gimple_cond): Remove edges when jumpif() expands an
	unconditional jump.
	(expand_gimple_basic_block): Don't clear EDGE_EXECUTABLE here,
	or remove abnormal edges.  Ignore insns setting the LHS of a TERed
	SSA name.
	(gimple_expand_cfg): Call into rewrite_out_of_ssa, initialize
	members of SA; deal with PARM_DECL partitions here; expand
	all PHI nodes, free tree datastructures and SA.  Commit instructions
	on edges, clear EDGE_EXECUTABLE and remove abnormal edges here.
	(pass_expand): Require and destroy PROP_ssa, verify SSA form, flow
	info and statements at start, collect garbage at finish.
	* tree-ssa-live.h (struct _var_map): Remove partition_to_var member.
	(VAR_ANN_PARTITION) Remove.
	(change_partition_var): Don't declare.
	(partition_to_var): Always return SSA names.
	(var_to_partition): Only accept SSA names.
	(register_ssa_partition): Only check argument.
	* tree-ssa-live.c (init_var_map): Don't allocate partition_to_var
	member.
	(delete_var_map): Don't free it.
	(var_union): Only accept SSA names, simplify.
	(partition_view_init): Mark only useful SSA names as used.
	(partition_view_fini): Only deal with SSA names.
	(change_partition_var): Remove.
	(dump_var_map): Use ssa_name instead of partition_to_var member.
	* tree-ssa.c (delete_tree_ssa): Don't remove PHI nodes on RTL
	basic blocks.
	* tree-outof-ssa.c (toplevel): Include ssaexpand.h and expr.h.
	(struct _elim_graph): New member const_dests; nodes member vector of
	ints.
	(set_location_for_edge): New static helper.
	(create_temp): Remove.
	(insert_partition_copy_on_edge, insert_part_to_rtx_on_edge,
	insert_value_copy_on_edge, insert_rtx_to_part_on_edge): New
	functions.
	(new_elim_graph): Allocate const_dests member.
	(clean_elim_graph): Truncate const_dests member.
	(delete_elim_graph): Free const_dests member.
	(elim_graph_size): Adapt to new type of nodes member.
	(elim_graph_add_node): Likewise.
	(eliminate_name): Likewise.
	(eliminate_build): Don't take basic block argument, deal only with
	partition numbers, not variables.
	(get_temp_reg): New static helper.
	(elim_create): Use it, deal with RTL temporaries instead of trees.
	(eliminate_phi): Adjust all calls to new signature.
	(assign_vars, replace_use_variable, replace_def_variable): Remove.
	(rewrite_trees): Only do checking.
	(edge_leader, stmt_list, leader_has_match, leader_match): Remove.
	(same_stmt_list_p, identical_copies_p, identical_stmt_lists_p,
	init_analyze_edges_for_bb, fini_analyze_edges_for_bb,
	contains_tree_r, MAX_STMTS_IN_LATCH,
	process_single_block_loop_latch, analyze_edges_for_bb,
	perform_edge_inserts): Remove.
	(expand_phi_nodes): New global function.
	(remove_ssa_form): Take ssaexpand parameter.  Don't call removed
	functions, initialize new parameter, remember partitions having a
	default def.
	(finish_out_of_ssa): New global function.
	(rewrite_out_of_ssa): Make global.  Adjust call to remove_ssa_form,
	don't reset in_ssa_p here, don't disable TER when mudflap.
	(pass_del_ssa): Remove.
	* tree-flow.h (struct var_ann_d): Remove out_of_ssa_tag and
	partition members.
	(execute_free_datastructures): Declare.
	* Makefile.in (SSAEXPAND_H): New variable.
	(tree-outof-ssa.o, expr.o, cfgexpand.o): Depend on SSAEXPAND_H.
	* basic-block.h (commit_one_edge_insertion): Declare.
	* passes.c (init_optimization_passes): Move pass_nrv and
	pass_mudflap2 before pass_cleanup_cfg_post_optimizing, remove
	pass_del_ssa, pass_free_datastructures, pass_free_cfg_annotations.
	* cfgrtl.c (commit_one_edge_insertion): Make global, don't declare.
	(redirect_branch_edge): Deal with super block when expanding, split
	out jump patching itself into ...
	(patch_jump_insn): ... here, new static helper.

testsuite/

	Expand from SSA.
	* gcc.dg/tree-ssa/20030728-1.c: Use -rtl-expand-details dump and
	change regexps.
	* gcc.target/i386/pr37248-1.c: Modified.
	* gcc.target/i386/pr37248-3.c: Modified.
	* gcc.target/i386/pr37248-2.c: Modified.
	* gnat.dg/aliasing1.adb: Modified.
	* gnat.dg/pack9.adb: Modified.
	* gnat.dg/aliasing2.adb: Modified.
	* gcc.dg/strict-overflow-2.c: Modified.
	* gcc.dg/autopar/reduc-1char.c: Modified.
	* gcc.dg/autopar/reduc-2char.c: Modified.
	* gcc.dg/autopar/reduc-1.c: Modified.
	* gcc.dg/autopar/reduc-2.c: Modified.
	* gcc.dg/autopar/reduc-3.c: Modified.
	* gcc.dg/autopar/reduc-6.c: Modified.
	* gcc.dg/autopar/reduc-7.c: Modified.
	* gcc.dg/autopar/reduc-8.c: Modified.
	* gcc.dg/autopar/reduc-9.c: Modified.
	* gcc.dg/autopar/reduc-1short.c: Modified.
	* gcc.dg/autopar/reduc-2short.c: Modified.
	* gcc.dg/autopar/parallelization-1.c: Modified.
	* gcc.dg/strict-overflow-4.c: Modified.
	* gcc.dg/strict-overflow-6.c: Modified.
	* gcc.dg/gomp/combined-1.c: Modified.
	* gcc.dg/no-strict-overflow-1.c: Modified.
	* gcc.dg/no-strict-overflow-3.c: Modified.
	* gcc.dg/no-strict-overflow-5.c: Modified.
	* gcc.dg/tree-ssa/reassoc-13.c: Modified.
	* gcc.dg/tree-ssa/pr18134.c: Modified.
	* gcc.dg/tree-ssa/20030824-1.c: Modified.
	* gcc.dg/tree-ssa/vector-2.c: Modified.
	* gcc.dg/tree-ssa/forwprop-9.c: Modified.
	* gcc.dg/tree-ssa/loop-21.c: Modified.
	* gcc.dg/tree-ssa/20030824-2.c: Modified.
	* gcc.dg/tree-ssa/vector-3.c: Modified.
	* gcc.dg/tree-ssa/asm-3.c: Modified.
	* gcc.dg/tree-ssa/pr23294.c: Modified.
	* gcc.dg/tree-ssa/loop-22.c: Modified.
	* gcc.dg/tree-ssa/loop-15.c: Modified.
	* gcc.dg/tree-ssa/prefetch-4.c: Modified.
	* gcc.dg/tree-ssa/pr22051-1.c: Modified.
	* gcc.dg/tree-ssa/pr20139.c: Modified.
	* gcc.dg/tree-ssa/scev-cast.c: Modified.
	* gcc.dg/tree-ssa/pr22051-2.c: Modified.
	* gcc.dg/tree-ssa/reassoc-1.c: Modified.
	* gcc.dg/tree-ssa/loop-5.c: Modified.
	* gcc.dg/tree-ssa/pr19431.c: Modified.
	* gcc.dg/tree-ssa/pr32044.c: Modified.
	* gcc.dg/tree-ssa/prefetch-7.c: Modified.
	* gcc.dg/tree-ssa/loop-19.c: Modified.
	* gcc.dg/tree-ssa/loop-28.c: Modified.
	* gcc.dg/tree-ssa/ssa-pre-15.c: Modified.
	* gcc.dg/tree-ssa/divide-1.c: Modified.
	* gcc.dg/tree-ssa/inline-1.c: Modified.
	* gcc.dg/tree-ssa/divide-3.c: Modified.
	* gcc.dg/tree-ssa/pr30978.c: Modified.
	* gcc.dg/tree-ssa/alias-6.c: Modified.
	* gcc.dg/tree-ssa/divide-4.c: Modified.
	* gcc.dg/tree-ssa/alias-11.c: Modified.
	* gcc.dg/no-strict-overflow-7.c: Modified.
	* gcc.dg/strict-overflow-1.c: Modified.
	* gcc.dg/pr15784-4.c: Modified.
	* gcc.dg/pr34263.c: Modified.
	* gcc.dg/strict-overflow-3.c: Modified.
	* gcc.dg/tree-prof/stringop-1.c: Modified.
	* gcc.dg/tree-prof/val-prof-1.c: Modified.
	* gcc.dg/tree-prof/val-prof-2.c: Modified.
	* gcc.dg/tree-prof/val-prof-3.c: Modified.
	* gcc.dg/tree-prof/val-prof-4.c: Modified.
	* gcc.dg/no-strict-overflow-2.c: Modified.
	* gcc.dg/no-strict-overflow-4.c: Modified.
	* gcc.dg/no-strict-overflow-6.c: Modified.
	* g++.dg/tree-ssa/pr27090.C: Modified.
	* g++.dg/tree-ssa/tmmti-2.C: Modified.
	* g++.dg/tree-ssa/ptrmemfield.C: Modified.
	* g++.dg/tree-ssa/pr19807.C: Modified.
	* g++.dg/opt/pr30965.C: Modified.
	* g++.dg/init/new17.C: Modified.
	* gfortran.dg/whole_file_6.f90: Modified.
	* gfortran.dg/whole_file_5.f90: Modified.
	* gfortran.dg/reassoc_1.f90: Modified.
	* gfortran.dg/reassoc_3.f90: Modified.

""",
u"""

	PR fortran/39893
	* gfortran.dg/assumed_charlen_dummy.f90: New Test.



	PR fortran/39893
	fortran/data.c (gfc_assign_data_value): If the lvalue is an 
	assumed character length entity in a data statement, then 
	return FAILURE to prevent segmentation fault.


""",
u"""
	* tree-ssa-copyrename.c (rename_ssa_copies): Don't iterate
	beyond num_ssa_names.
	* tree-ssa-ter.c (free_temp_expr_table): Likewise.
	* tree-ssa-coalesce.c (create_outofssa_var_map): Likewise.

""",
u"""
	PR inline-asm/39543
	* fwprop.c (forward_propagate_asm): New function.
	(forward_propagate_and_simplify): Propagate also into __asm, if it
	doesn't increase the number of referenced registers.

	* gcc.target/i386/pr39543-1.c: New test.
	* gcc.target/i386/pr39543-2.c: New test.
	* gcc.target/i386/pr39543-3.c: New test.

""",
u"""
	PR c/39889
	* stmt.c (warn_if_unused_value): Look through NON_LVALUE_EXPR.

	* gcc.dg/Wunused-value-3.c: New test.

""",
u"""
	* tree-nested.c (get_nonlocal_vla_type): If not optimizing, call
	note_nonlocal_vla_type for nonlocal VLAs.
	(note_nonlocal_vla_type, note_nonlocal_block_vlas,
	contains_remapped_vars, remap_vla_decls): New functions.
	(convert_nonlocal_reference_stmt): If not optimizing, call
	note_nonlocal_block_vlas on GIMPLE_BIND block vars.
	(nesting_copy_decl): Return {VAR,PARM,RESULT}_DECL unmodified
	if it wasn't found in var_map.
	(finalize_nesting_tree_1): Call remap_vla_decls.  If outermost
	GIMPLE_BIND doesn't have gimple_bind_block, chain debug_var_chain
	to BLOCK_VARS (DECL_INITIAL (root->context)) instead of calling
	declare_vars.
	* gimplify.c (nonlocal_vlas): New variable.
	(gimplify_var_or_parm_decl): Add debug VAR_DECLs for non-local
	referenced VLAs.
	(gimplify_body): Create and destroy nonlocal_vlas.

	* trans-decl.c: Include pointer-set.h.
	(nonlocal_dummy_decl_pset, tree nonlocal_dummy_decls): New variables.
	(gfc_nonlocal_dummy_array_decl): New function.
	(gfc_get_symbol_decl): Call it for non-local dummy args with saved
	descriptor.
	(gfc_get_symbol_decl): Set DECL_BY_REFERENCE when needed.
	(gfc_generate_function_code): Initialize nonlocal_dummy_decl{s,_pset},
	chain it to outermost block's vars, destroy it afterwards.
	* Make-lang.in (trans-decl.o): Depend on pointer-set.h.

""",
u"""
	* dwarf2out.c (loc_descr_plus_const): New function.
	(build_cfa_aligned_loc, tls_mem_loc_descriptor,
	mem_loc_descriptor, loc_descriptor_from_tree_1,
	descr_info_loc, gen_variable_die): Use it.

""",
u"""
	* tree.h (DECL_BY_REFERENCE): Note that it is also valid for
	!TREE_STATIC VAR_DECLs.
	* dwarf2out.c (loc_by_reference, gen_decl_die): Handle
	DECL_BY_REFERENCE on !TREE_STATIC VAR_DECLs.
	(gen_variable_die): Likewise.  Don't look at TREE_PRIVATE if
	DECL_BY_REFERENCE is valid.
	* dbxout.c (DECL_ACCESSIBILITY_CHAR): Don't look at TREE_PRIVATE
	for PARM_DECLs, RESULT_DECLs or !TREE_STATIC VAR_DECLs.
	* tree-nested.c (get_nonlocal_debug_decl, get_local_debug_decl):
	Copy DECL_BY_REFERENCE.
	(struct nesting_copy_body_data): New type.
	(nesting_copy_decl): New function.
	(finalize_nesting_tree_1): Remap types of debug_var_chain variables,
	if they have variable length.

""",
u"""
* tree-sra.c (sra_build_assignment): Don't use into_ssa mode,
mark new temporaries for renaming

""",
u"""
	PR c/39581
	* c-decl.c (global_bindings_p): Return negative value.
	(c_variable_size): New.  Based on variable_size from
	stor-layout.c.
	(grokdeclarator): Call c_variable_size not variable_size.

testsuite:
	* gcc.dg/c99-const-expr-14.c, gcc.dg/gnu99-const-expr-4.c,
	gcc.dg/vla-21.c: New tests.

""",
u"""
	* config/i386/i386.c (print_operand) ['z']: Fix typo.


""",
u"""

        * contrib/aot-compile.in: Print diagnostics for malformed or invalid
        class files.
        * contrib/generate-cacerts.pl.in: New.
        * configure.ac (AC_CONFIG_FILES): Add generate-cacerts.pl.

""",
u"""

	* config/i386/mingw-w64.h (STANDARD_INCLUDE_DIR):
	Redefine it to just use mingw/include.
	(ASM_SPEC): Rules for -m32 and -m64.
	(LINK_SPEC): Use Likewise.
	(SPEC_32): New define.
	(SPEC_64): Likewise.
	(SUB_LINK_SPEC): Likewise.
	(MULTILIB_DEFAULTS): New define.
	* config/i386/t-mingw-w64 (MULTILIB_OPTIONS):
	Add multilib options.
	(MULTILIB_DIRNAMES): Likewise.
	(MULTILIB_OSDIRNAMES): Likewise.
	(LIBGCC): Likewise.
	(INSTALL_LIBGCC): Likewise.



""",
u"""
	PR c/39556
	* c-tree.h (enum c_inline_static_type): New.
	(record_inline_static): Declare.
	* c-decl.c (struct c_inline_static, c_inline_statics,
	record_inline_static, check_inline_statics): New.
	(pop_file_scope): Call check_inline_statics.
	(start_decl): Call record_inline_static instead of pedwarning
	directly for static in inline function.
	* c-typeck.c (build_external_ref): Call record_inline_static
	instead of pedwarning directly for static referenced in inline
	function.

testsuite:
	* gcc.dg/inline-34.c: New test.

""",
u"""
	* df-scan.c (df_insn_rescan): Salvage insn's LUID if the insn is
	not new but only being rescanned.
	* gcse.c (uid_cuid, max_uid, INSN_CUID, max_cuid, struct reg_set,
	reg_set_table, REG_SET_TABLE_SLOP, reg_set_in_block,
	alloc_reg_set_mem, free_reg_set_mem, record_one_set,
	record_set_info, compute_set, grealloc): Remove.
	(recompute_all_luids): New function.
	(gcse_main): Don't compute sets, and don't do related memory
	allocations/free-ing.  If something changed before the end of the
	pass, update LUIDs using recompute_all_luids.
	(alloc_gcse_mem): Don't compute LUIDs.  Don't allocate reg_set memory.
	(free_gcse_mem): Don't free it either.
	(oprs_unchanged_p, load_killed_in_block, record_last_reg_set_info):
	Use the df insn LUIDs.
	(load_killed_in_block): Likewise.
	(compute_hash_table_work): Don't compute reg_set_in_block.
	(compute_transp): Use DF_REG_DEF_CHAINs.
	(local_cprop_pass): Don't use compute_sets and related functions.
	(one_cprop_pass, pre_gcse, one_pre_gcse_pass, one_code_hoisting_pass):
	Use get_max_uid() instead of max_cuid.
	(insert_insn_end_basic_block, pre_insert_copy_insn,
	update_ld_motion_stores): Don't try to
	keep reg_set tables up to date.
	(pre_insert_copies): Use df insn LUIDs.
	(sbitmap pre_redundant_insns): Replace with uses of INSN_DELETED_P.
	(reg_set_info): Don't use extra bitmap argument.
	(compute_store_table): Don't compute reg_set_in_block.  Use DF scan
	information to compute regs_set_in_block.
	(free_store_memory, store_motion): Don't nullify reg_set_in_block.
	(bypass_jumps): Don't use compute_sets and friends.

""",
u"""

	Revert the last commit.

""",
u"""
gcc/
	PR testsuite/39710
	* opts.c (undocumented_msg): Do not leave blank even with
	ENABLE_CHECKING.


""",
u"""
Update copyright year.  Committed without a ChangeLog entry.

""",
u"""
* Makefile.in (needed-list): Target removed (not used in GCC
3.0 and later).  All references deleted.
(mostlyclean): Remove references to needed.awk and needed2.awk.

""",
u"""
Daily bump.
""",
u"""
	* c-decl.c (build_enumerator): Allow values folding to integer
	constants but not integer constant expressions with a pedwarn if
	pedantic.

testsuite:
	* gcc.dg/enum-const-1.c, gcc.dg/enum-const-2.c,
	gcc.dg/enum-const-3.c: New tests.
	* gcc.dg/gnu89-const-expr-1.c, gcc.dg/gnu99-const-expr-1.c: Use
	-pedantic-errors.  Update expected diagnostics.

""",
u"""
	PR c/39582
	* c-typeck.c (c_expr_sizeof_type): Create a C_MAYBE_CONST_EXPR
	with non-null C_MAYBE_CONST_EXPR_PRE if size of a variable-length
	type is an integer constant.

testsuite:
	* gcc.dg/vla-20.c: New test.

""",
u"""

	* include/std/mutex (__get_once_functor_lock, __get_once_mutex):
	Replace global lock object with local locks on global mutex.
	* src/mutex.cc: Likewise.
	* config/abi/pre/gnu.ver: Adjust.
	* testsuite/30_threads/call_once/call_once2.cc: New.

""",
u"""
	PR target/39897
	* config/i386/i386.c (print_operand) ['z']: Revert handling of
	HImode operands.


""",
u"""
	* test_summary: Only include LAST_UPDATED if it exists.
	Complete copyright years.

""",
u"""

	PR libstdc++/39880
	PR libstdc++/39881
	PR libstdc++/39882
	* include/std/system_error (is_error_code_enum<errc>): Remove.
	(error_condition<>::error_condition(_ErrorCodeEnum,)
	error_condition<>::operator=(_ErrorCodeEnum)): Use make_error_condition.
	(error_code<>::error_code(_ErrorCodeEnum,),
	error_code<>::operator=(_ErrorCodeEnum)): Use make_error_code.
	* testsuite/19_diagnostics/system_error/39880.cc: New.
	* testsuite/19_diagnostics/error_condition/modifiers/39881.cc:
	Likewise.
	* testsuite/19_diagnostics/error_condition/cons/39881.cc: Likewise.
	* testsuite/19_diagnostics/error_code/modifiers/39882.cc: Likewise.
	* testsuite/19_diagnostics/error_code/cons/39882.cc: Likewise.
	* testsuite/27_io/basic_ostream/inserters_other/char/error_code.cc:
	Adjust.
	* testsuite/27_io/basic_ostream/inserters_other/wchar_t/error_code.cc:
	Likewise.
	* testsuite/19_diagnostics/error_code/cons/1.cc: Likewise.
	* testsuite/19_diagnostics/error_code/operators/bool.cc: Likewise.
	* testsuite/19_diagnostics/error_code/operators/equal.cc: Likewise.
	* testsuite/19_diagnostics/error_code/operators/not_equal.cc:
	Likewise.
	* testsuite/19_diagnostics/error_category/cons/copy_neg.cc: Likewise.
	* testsuite/19_diagnostics/system_error/cons-1.cc: Likewise.
	* testsuite/19_diagnostics/system_error/what-4.cc: Likewise.
	* testsuite/30_threads/unique_lock/locking/2.cc: Likewise.

""",
u"""

	PR libstdc++/39880
	PR libstdc++/39881
	PR libstdc++/39882
	* include/std/system_error (is_error_code_enum<errc>): Remove.
	(error_condition<>::error_condition(_ErrorCodeEnum,)
	error_condition<>::operator=(_ErrorCodeEnum)): Use make_error_condition.
	(error_code<>::error_code(_ErrorCodeEnum,),
	error_code<>::operator=(_ErrorCodeEnum)): Use make_error_code.
	* testsuite/19_diagnostics/system_error/39880.cc: New.
	* testsuite/19_diagnostics/error_condition/modifiers/39881.cc:
	Likewise.
	* testsuite/19_diagnostics/error_condition/cons/39881.cc: Likewise.
	* testsuite/19_diagnostics/error_code/modifiers/39882.cc: Likewise.
	* testsuite/19_diagnostics/error_code/cons/39882.cc: Likewise.
	* testsuite/27_io/basic_ostream/inserters_other/char/error_code.cc:
	Adjust.
	* testsuite/27_io/basic_ostream/inserters_other/wchar_t/error_code.cc:
	Likewise.
	* testsuite/19_diagnostics/error_code/cons/1.cc: Likewise.
	* testsuite/19_diagnostics/error_code/operators/bool.cc: Likewise.
	* testsuite/19_diagnostics/error_code/operators/equal.cc: Likewise.
	* testsuite/19_diagnostics/error_code/operators/not_equal.cc:
	Likewise.
	* testsuite/19_diagnostics/error_category/cons/copy_neg.cc: Likewise.
	* testsuite/19_diagnostics/system_error/cons-1.cc: Likewise.
	* testsuite/19_diagnostics/system_error/what-4.cc: Likewise.
	* testsuite/30_threads/unique_lock/locking/2.cc: Likewise.

""",
u"""
Fix typo in comment in previous commit.

""",
u"""
	PR c/39564
	* c-decl.c (grokdeclarator): Diagnose declarations of functions
	with variably modified return type and no storage class
	specifiers, except for the case of nested functions.  Distinguish
	extern declarations of functions with variably modified return
	types from those of objects with variably modified types.

testsuite:
	* gcc.dg/vla-19.c: New test.

""",
u"""
libcpp:
	PR preprocessor/39559
	* expr.c (cpp_interpret_integer): Use a pedwarn for decimal
	constants larger than intmax_t in C99 mode.

gcc/testsuite:
	* gcc.dg/c99-intconst-2.c: New test.

""",
u"""
	* tree.c (list_equal_p): New function.
	* tree.h (list_equal_p): Declare.
	* coretypes.h (edge_def, edge, const_edge, basic_block_def
	basic_block_def, basic_block, const_basic_block): New.
	* tree-eh.c (make_eh_edge): EH edges are not abnormal.
	(redirect_eh_edge): New function.
	(make_eh_edge_update_phi): EH edges are not abnormal.
	* except.c: Include tree-flow.h.
	(list_match): New function.
	(eh_region_replaceable_by_p): New function.
	(replace_region): New function.
	(hash_type_list): New function.
	(hash_eh_region): New function.
	(eh_regions_equal_p): New function.
	(merge_peers): New function.
	(remove_unreachable_regions): Verify EH tree when checking;
	merge peers.
	(copy_eh_region_1): New function.
	(copy_eh_region): New function.
	(push_reachable_handler): New function.
	(build_post_landing_pads, dw2_build_landing_pads): Be ready for
	regions without label but with live RESX.
	* except.h (redirect_eh_edge_to_label): New.
	* tree-flow.h (redirect_eh_edge): New.
	* coretypes.h (edge_def, edge, const_edge, basic_block_def
	basic_block_def, basic_block, const_basic_block): Remove.
	* Makefile.in (except.o): Add dependency on tree-flow.h
	* tree-cfg.c (gimple_redirect_edge_and_branch): Handle EH edges.
	* basic-block.h (edge, const_edge, basic_block, const_basic_block):
	Remove.

""",
u"""
	PR bootstrap/39645
	* config/sparc/sparc.c (sparc_gimplify_va_arg): Set TREE_ADDRESSABLE
	on the destination of memcpy.

""",
u"""
	* Makefile.tpl (POSTSTAGE1_HOST_EXPORTS): Add GNATBIND.
	(POSTSTAGE1_FLAGS_TO_PASS): Pick up exported value for GNATBIND.
	* Makefile.in: Regenerate.

""",
u"""
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Array_Subtype>: Put
	back kludge.

""",
u"""

	* doc/tm.texi (REGNO_OK_FOR_BASE_P, REGNO_MODE_OK_FOR_BASE_P,
	REGNO_MODE_OK_FOR_REG_BASE_P, REGNO_MODE_CODE_OK_FOR_BASE_P,
	REGNO_OK_FOR_INDEX_P): Mention strict/nonstrict difference.


""",
u"""
	* tree-eh.c (tree_remove_unreachable_handlers): Handle shared labels.
	(tree_empty_eh_handler_p): Allow non-EH predecestors; allow region
	to be reached by different label than left.
	(update_eh_edges): Update comment; remove edge_to_remove if possible
	and return true if suceeded.
	(cleanup_empty_eh): Accept sharing map; handle shared regions.
	(cleanup_eh): Compute sharing map.
	* except.c (remove_eh_handler_and_replace): Add argument if we should
	update regions.
	(remove_unreachable_regions): Update for label sharing.
	(label_to_region_map): Likewise.
	(get_next_region_sharing_label): New function.
	(remove_eh_handler_and_replace): Add update_catch_try parameter; update
	prev_try pointers.
	(remove_eh_handler): Update.
	(remove_eh_region_and_replace_by_outer_of): New function.
	* except.h (struct eh_region): Add next_region_sharing_label.
	(remove_eh_region_and_replace_by_outer_of,
	get_next_region_sharing_label): Declare.
	* tree-cfgcleanup.c (tree_forwarder_block_p): Simplify.

	* tree-cfg.c (split_critical_edges): Split also edges where we can't
	insert code even if they are not critical.

	* tree-cfg.c (gimple_can_merge_blocks_p): EH edges are unmergable.
	(gimple_can_remove_branch_p): EH edges won't remove branch by
	redirection.
	* tree-inline.c (update_ssa_across_abnormal_edges): Do handle
	updating of non-abnormal EH edges.
	* tree-cfg.c (gimple_can_merge_blocks_p): EH edges are unmergable.
	(gimple_can_remove_branch_p): EH edges are unremovable by redirection.
	(split_critical_edges): Split also edges where emitting code on them
	will lead to splitting later.

""",
u"""

	PR fortran/39688
	* decl.c (gfc_match_import): Use 'sym->name' instead of 'name'.
	They differ if the symbol has been use-renamed.



	PR fortran/39688
	* gfortran.dg/import7.f90: New.


""",
u"""
	PR target/39590
	* configure.ac (HAVE_AS_IX86_FILDQ): On x86 targets check whether
	the configured assembler supports fildq and fistpq mnemonics.
	(HAVE_AS_IX86_FILDS): Rename from HAVE_GAS_FILDS_FISTS.
	* configure: Regenerated.
	* config.in: Ditto.

	* config/i386/i386.c (print_operand): Handle 'Z'.
	['z']: Remove handling of special fild/fist suffixes.
	(output_fix_trunc): Use '%Z' to output suffix of fist{,p,tp} insn.
	* config/i386/i386.md (*floathi<mode>2_i387): Use '%Z' to output
	suffix of fild insn.
	(*floatsi<mode>2_vector_mixed): Ditto.
	(*float<SSEMODEI24:mode><MODEF:mode>2_mixed_interunit): Ditto.
	(*float<SSEMODEI24:mode><MODEF:mode>2_mixed_nointerunit): Ditto.
	(*float<SSEMODEI24:mode><X87MODEF:mode>2_i387_with_temp): Ditto.
	(*float<SSEMODEI24:mode><X87MODEF:mode>2_i387): Ditto.
	* config/i386/gas.h (GAS_MNEMONICS): Remove.


""",
u"""

        * configure.ac: Create missing directory gnu/java/security/jce/prng.
        * configure: Regenerate.

""",
u"""
	* genrecog.c (validate_pattern): Do not warn for VOIDmode CALLs as
	the source of a set operation.

""",
u"""
	* target.h (struct gcc_target): Add case_values_threshold field.
	* target-def.h (TARGET_CASE_VALUES_THRESHOLD): New.
	(TARGET_INITIALIZER): Use TARGET_CASE_VALUES_THRESHOLD.
	* targhooks.c (default_case_values_threshold): New function.
	* targhooks.h (default_case_values_threshold): Declare function.
	* stmt.c (expand_case): Use case_values_threshold target hook.
	* expr.h (case_values_threshold): Remove declartation.
	* expr.c (case_values_threshold): Remove function.
	* doc/tm.texi (CASE_VALUES_THRESHOLD): Revise documentation.

	* config/avr/avr.h (CASE_VALUES_THRESHOLD): Remove macro.
	* config/avr/avr.c (TARGET_CASE_VALUES_THRESHOLD): Define macro.
	(avr_case_values_threshold): Declare as static.
	* config/avr/avr-protos.h (avr_case_values_threshold): Remove.

	* config/avr/mn10300.h (CASE_VALUES_THRESHOLD): Remove macro.
	* config/avr/mn10300.c (TARGET_CASE_VALUES_THRESHOLD): Define macro.
	(mn10300_case_values_threshold): New function.


""",
u"""
	PR bootstrap/39739
	* configure.ac (extra_mpfr_configure_flags): Set and AC_SUBST.
	* Makefile.def (module=mpfr): Use extra_mpfr_configure_flags.

	* configure, Makefile.in: Regenerate.


""",
u"""

	* ira.c (setup_cover_and_important_classes): Add enum cast.

""",
u"""
Daily bump.
""",
u"""

	* genpreds.c (write_enum_constraint_num): Output definition of
	CONSTRAINT_NUM_DEFINED_P macro.
	* ira.c (setup_cover_and_important_classes): Use
	CONSTRAINT_NUM_DEFINED_P instead of CONSTRAINT__LIMIT in #ifdef.


""",
u"""
* config/sh/sh.h (LIBGCC2_DOUBLE_TYPE_SIZE): Test
__SH2A_SINGLE_ONLY__ also.

""",
u"""

	* xml/authors.xml: Add space.
	* xml/faq.xml: Update links.
	* xml/manual/intro.xml: Same.
	* xml/manual/abi.xml: Update.
	* xml/manual/appendix_contributing.xml: Fix typo.
	* xml/manual/status_cxxtr1.xml: Update links.
	* xml/manual/status_cxx1998.xml: Same.
	* xml/manual/status_cxx200x.xml: Same.


""",
u"""

	* gcc.dg/tree-ssa/vrp48.c: Fix.

""",
u"""

        * g++.dg/init/copy7.C: Only abort in memcpy if source and
        destination are the same.


""",
u"""
	* config/ia64/ia64.md (movfs_internal): Allow flt constants.
	(movdf_internal): Ditto.
	* config/ia64/ia64.c (ia64_legitimate_constant_p): Allow
	SFmode and DFmode constants.
	(ia64_print_operand): Add 'G' format for printing
	floating point constants.

""",
u"""

	* tree-vrp.c (extract_range_from_binary_expr): Handle overflow
	from unsigned additions.

	* gcc.dg/tree-ssa/vrp48.c: New testcase.

""",
u"""
	* c-typeck.c (set_init_index): Allow array designators that are
	not integer constant expressions with a pedwarn if pedantic.

testsuite:
	* gcc.dg/array-const-1.c, gcc.dg/array-const-2.c,
	gcc.dg/array-const-3.c: New tests.

""",
u"""
Correct filenames.

""",
u"""
Add missing ChangeLog entries for revision 146607.

""",
u"""
	* simplify-rtx.c (simplify_binary_operation_1, case AND): Result is
	zero if no overlap in nonzero bits between the operands.


""",
u"""
Fix typo
""",
u"""
gcc/:
	* combine.c (record_value_for_reg): Change 0 to VOIDmode, twice.
	(record_dead_and_set_regs): Likewise.
	* df.h (struct df_mw_hardreg): Change flags field to int.
	(struct df_base_ref): Likewise.
	(struct df): Change changeable_flags field to int.
	* df-scan.c (df_defs_record): Change clobber_flags to int.
	* dwarf2.h (enum dwarf_tag): Make lo_user and hi_user values enum
	constants rather than #define macros.
	(enum dwarf_attribute, enum dwarf_location_atom): Likewise.
	(enum dwarf_type, enum dwarf_endianity_encoding): Likewise.
	(enum dwarf_calling_convention): Likewise.
	(enum dwarf_line_number_x_ops): Likewise.
	(enum dwarf_call_frame_info): Likewise.
	(enum dwarf_source_language): Likewise.
	* dwarf2out.c (int_loc_descriptor): Add cast to enum type.
	(add_calling_convention_attribute): Likewise.
	* fold-const.c (fold_undefer_overflow_warnings): Add cast to enum
	type.
	(combine_comparisons): Change compcode to int.  Add cast to enum
	type.
	* genrecog.c (maybe_both_true_2): Change c to int.
	(write_switch): Likewise.  Add cast to enum type.
	* gimplify.c (gimplify_omp_for): Handle return values from
	gimplify_expr using MIN rather than bitwise or.
	(gimplify_expr): Add cast to enum type.
	* ipa-prop.c (update_jump_functions_after_inlining): Change
	IPA_BOTTOM to IPA_JF_UNKNOWN.
	* ira.c (setup_class_subset_and_memory_move_costs): Change mode to
	int.  Add casts to enum type.
	(setup_cover_and_important_classes): Change cl to int.  Add casts
	to enum type.
	(setup_class_translate): Change cl and mode to int.
	(ira_init_once): Change mode to int.
	(free_register_move_costs): Likewise.
	(setup_prohibited_mode_move_regs): Add casts to enum type.
	* langhooks.c (add_builtin_function_common): Rework assertion that
	value fits bitfield.
	* mcf.c (add_fixup_edge): Change type parameter to edge_type.
	* omega.c (omega_do_elimination): Avoid math on enum types.
	* optabs.c (expand_vec_shift_expr): Remove casts to int.
	* opts.c (set_debug_level): Change 2 to enum constant.  Use new
	int local to handle integral_argment value.
	* regmove.c (try_auto_increment): Change PUT_MODE to
	PUT_REG_NOTE_KIND.
	* reload.c (push_secondary_reload): Add casts to enum type.
	(secondary_reload_class, find_valid_class): Likewise.
	* reload1.c (emit_input_reload_insns): Likewise.
	* rtl.h (NOTE_VAR_LOCATION_STATUS): Likewise.
	* sel-sched.c (init_hard_regs_data): Change cur_mode to int.
	* sel-sched-ir.c (hash_with_unspec_callback): Change 0 to enum
	constant.
	* tree.c (build_common_builtin_nodes): Add casts to enum type.
	* tree-complex.c (complex_lattice_t): Typedef to int rather than
	enum type.
	(expand_complex_libcall): Add casts to enum type.
	* tree-into-ssa.c (get_ssa_name_ann): Change 0 to enum constant.
	* tree-vect-loop.c (vect_model_reduction_cost): Compare reduc_code
	with ERROR_MARK, not NUM_TREE_CODES.
	(vect_create_epilog_for_reduction): Likewise.
	(vectorizable_reduction): Don't initialize epiloc_reduc_code.
	When not using it, set it to ERROR_MARK rather than
	NUM_TREE_CODES.
	* tree-vect-patterns.c (vect_pattern_recog_1): Change vec_mode to
	enum machine_mode.
	* tree-vect-stmts.c (new_stmt_vec_info): Change 0 to
	vect_unused_in_loop.  Change 0 to loop_vect.
	* tree-vectorizer.c (vect_set_verbosity_level): Add casts to enum
	type.
	* var-tracking.c (get_init_value): Change return type to enum
	var_init_status.
	* vec.h (DEF_VEC_FUNC_P) [iterate]: Cast 0 to type T.
	* config/arm/arm.c (fp_model_for_fpu): Change to array to enum
	arm_fp_model.
	(arm_override_options): Add casts to enum type.
	(arm_emit_tls_decoration): Likewise.
	* config/i386/i386.c (ix86_function_specific_restore): Add casts
	to enum type.
	* config/i386/i386-c.c (ix86_pragma_target_parse): Likewise.
	* config/ia64/ia64.c (ia64_expand_compare): Change magic to int.
	* config/rs6000/rs6000.c (rs6000_override_options): Add casts to
	enum type.
	* config/s390/s390.c (code_for_builtin_64): Change to array of
	enum insn_code.
	(code_for_builtin_31): Likewise.
	(s390_expand_builtin): Change code_for_builtin to enum insn_code
	const *.
	* config/sparc/sparc.c (sparc_override_options): Change value
	field in struct code_model to enum cmodel.  In initializer change
	0 to NULL and add cast to enum type.

	* c-typeck.c (build_modify_expr): Add lhs_origtype parameter.
	Change all callers.  Issue a -Wc++-compat warning using
	lhs_origtype if necessary.
	(convert_for_assignment): Issue -Wc++-compat warnings about
	invalid conversions to enum type on assignment.
	* c-common.h (build_modify_expr): Update declaration.

gcc/cp/:
	* call.c (build_temp): Change 0 to enum constant.
	* cp-tree.h (cp_lvalue_kind): Typedef to int rather than enum
	type.
	* cp-gimplify.c (cp_gimplify_expr): Add cast to enum type.
	* decl2.c (constrain_visibility): Likewise.
	* parser.c (cp_lexer_get_preprocessor_token): Likewise.
	(cp_parser_flags): Typedef to int rather than enum type.
	(cp_parser_expression_stack_entry): Change prec field to enum
	cp_parser_prec.

	* typeck.c (build_modify_expr): Add lhs_origtype parameter.
	Change all callers.

gcc/fortran/:
	* gfortran.h (enum gfc_symbol_type): New named enum type, broken
	out of struct gfc_symbol.
	(struct gfc_symbol): Use enum gfc_symbol_type.
	(enum gfc_array_ref_dimen_type): New named enum type, broken out
	of struct gfc_array_ref).
	(struct gfc_array_ref): Use enum gfc_array_ref_dimen_type.
	(mod_pointee_as): Update declaration.
	* decl.c (add_global_entry): Change type to enum gfc_symbol_type.
	(gfc_mod_pointee_as): Change return type to "match".
	* module.c (mio_array_ref): Add cast to enum type.
	(mio_symbol): Likewise.
	* resolve.c (resolve_global_procedure): Change type to enum
	gfc_symbol_type.
	* trans-io.c (gfc_build_st_parameter): Change type to unsigned
	int.

gcc/java/:
	* jcf-parse.c (handle_constant): Add cast to enum type.

gcc/objc/:
	* objc-act.c (get_super_receiver): Update calls to
	build_modify_expr to pass new argument.

gcc/testsuite/:
	* gcc.dg/Wcxx-compat-4.c: New testcase.

""",
u"""
        * config/iq2000/iq2000.c (function_arg): Handle TImode values.
        (function_arg_advance): Likewise.
        * config/iq2000/iq2000.md (movsi_internal2): Fix the length of the
        5th alternative.

""",
u"""

	* gfortran.h (gfc_get_typebound_proc): Removed as macro, now a function.
	(struct gfc_symtree): Moved `typebound' member inside union.
	(struct gfc_namespace): Add `tb_sym_root' as new symtree to sort out
	type-bound procedures there.
	(gfc_get_tbp_symtree): New procedure.
	* symbol.c (tentative_tbp_list): New global.
	(gfc_get_namespace): NULL new `tb_sym_root' member.
	(gfc_new_symtree): Removed initialization of `typebound' member.
	(gfc_undo_symbols): Process list of tentative tbp's.
	(gfc_commit_symbols): Ditto.
	(free_tb_tree): New method.
	(gfc_free_namespace): Call it.
	(gfc_get_typebound_proc): New method.
	(gfc_get_tbp_symtree): New method.
	(gfc_find_typebound_proc): Adapt to structural changes of gfc_symtree
	and gfc_namespace with regards to tbp's.
	* dump-parse-tree.c (show_typebound): Ditto.
	* primary.c (gfc_match_varspec): Ditto.  Don't reference tbp-symbol
	as it isn't a symbol any longer.
	* module.c (mio_typebound_symtree): Adapt to changes.
	(mio_typebound_proc): Ditto, create symtrees using `gfc_get_tbp_symtree'
	rather than `gfc_get_sym_tree'.
	(mio_f2k_derived): Ditto.
	* decl.c (match_procedure_in_type): Ditto.
	(gfc_match_generic): Ditto.  Don't reference tbp-symbol.
	* resolve.c (check_typebound_override): Adapt to changes.
	(resolve_typebound_generic): Ditto.
	(resolve_typebound_procedures): Ditto.
	(ensure_not_abstract_walker): Ditto.
	(ensure_not_abstract): Ditto.
	(resolve_typebound_procedure): Ditto, ignore erraneous symbols (for
	instance, through removed tentative ones).
	* gfc-internals.texi (Type-bound procedures): Document changes.


	* gfortran.dg/typebound_generic_1.f03: Change so that no error is
	expected on already erraneous symbol (renamed to fresh one).

""",
u"""

	* mlib-prj.adb, prj-env.adb, prj-nmsc.adb, prj-proc.adb, make.adb,
	clean.adb: Minor reformatting.
	Minor code reorganization and message improvement.


""",
u"""

	* prj-proc.adb, prj.adb, prj.ads, prj-nmsc.adb, prj-nmsc.ads
	(Alternate_Languages): now implemented as a malloc-ed list rather
	than through a table.


""",
u"""

	* config/s390/constraints.md ('I', 'J'): Fix condition.


""",
u"""

	* sem_res.adb (Static_Concatenation): Simplify predicate to make it
	accurately handle cases such as "lit" & "lit" and
	"lit" & static_string_constant


""",
u"""

	* prj-proc.adb, make.adb, mlib-prj.adb, prj.adb, prj.ads, clean.adb,
	prj-nmsc.adb, prj-env.adb (Project_List_Table, Project_Element):
	removed. Lists of projects are now implemented via standard malloc
	rather than through the table.


	* sem_ch12.adb: Minor reformatting

	* g-trasym.adb: Minor reformatting

	* exp_ch6.adb: Minor reformatting


	* layout.adb (Layout_Type): For packed array type, copy unset
	size/alignment fields from the referenced Packed_Array_Type.


	* lib-load.adb (Make_Instance_Unit): Revert previous change, no
	longer needed after sem_ch12 changes.

	* sem.adb (Walk_Library_Items): Include with's in some debugging
	printouts.


""",
u"""
Minor reformatting.

""",
u"""

	* prj.ads, prj-nmsc.adb (Unit_Project): removed, since in fact we were
	only ever using the Project field.


	* sem_ch12.adb (Build_Instance_Compilation_Unit_Nodes): Do not set
	Body_Required on the generated compilation node. The new node is linked
	to its body, but both share the same file, so we do not set this flag
	on the new unit so as not to create a spurious dependency on a
	non-existent body in the ali file for the instance.


	* make.adb: Minor reformatting


""",
u"""

	* prj.adb, prj.ads, prj-nmsc.adb (Check_File, Record_Ada_Source,
	Add_Source): merge some code between those. In particular change where
	file normalization is done to avoid a few extra calls to
	Canonicalize_File_Name. This also removes the need for passing
	Current_Dir in a number of subprograms.


	* lib-load.adb (Make_Instance_Unit): In the case where In_Main is
	False, assign the correct unit to the Cunit field of the new table
	entry. We want the spec unit, not the body unit.

	* rtsfind.adb (Make_Unit_Name, Maybe_Add_With): Simplify calling
	interface for these.
	(Maybe_Add_With): Check whether we're trying to a with on the current
	unit, and avoid creating such directly self-referential with clauses.
	(Text_IO_Kludge): Add implicit with's for the generic pseudo-children of
	[[Wide_]Wide_]Text_IO. These are needed for Walk_Library_Items,
	and matches existing comments in the spec.

	* sem.adb (Walk_Library_Items): Add various special cases to make the
	assertions pass.

	* sem_ch12.adb (Build_Instance_Compilation_Unit_Nodes): Use Body_Cunit
	instead of Parent (N), for uniformity.


""",
u"""
(pragma Source_File_Name): add missing documentation for the Index
 argument.

""",
u"""

	* errout.ads: Minor reformatting


	* gnat_ugn.texi (Library Projects): add documentation on gnatmake's
	behavior when the project includes sources from multiple languages


	* prj.adb (Has_Foreign_Sources): Returns True in Ada_Only mode if there
	is a language other than Ada declared.

	* makeutl.adb (Linker_Options_Switches): Call For_All_Projects with
	Imported_First set to True.


""",
u"""

	* gengtype-parse.c (parse_error): Add newline after message.


""",
u"""

	* sem_res.adb: additional optimization to inhibit creation of
	redundant transient scopes.


	* rtsfind.ads: Minor comment fix


	* prj-proc.adb, prj-nmsc.adb (Find_Ada_Sources,
	Get_Path_Name_And_Record_Ada_Sources): merged, since these were
	basically doing the same work (for explicit or implicit sources).
	(Find_Explicit_Sources): renamed to Find_Sources to better reflect its
	role. Rewritten to share some code (testing that all explicit sources
	have been found) between ada_only and multi_language modes.


	* sem_prag.adb (Check_Form_Of_Interface_Name): Allow space in Ext_Name
	for CLI imported types.
	(Analyze_Pragma): Allow CIL or Java imported functions returning
	access-to-subprogram types.


""",
u"""

	* make.adb, prj.adb, prj.ads, makeutl.adb, makeutl.ads:
	(Project_Data.Dir_Path): field removed, since it can be computed
	directly from .Directory, and is needed only once when processing the
	project is buildgpr.adb or make.adb


""",
u"""
Minor reformatting.

""",
u"""

	* prj-env.adb, prj-proc.adb, prj.adb, prj.ads,
	rtsfind.adb: Minor reformatting.
	Minor code reorganization


""",
u"""

	* config/i386/sse.md (avxmodesuffixs): Removed.
	(*avx_pinsr<avxmodesuffixs>): Renamed to ...
	(*avx_pinsr<ssevecsize>): This.

""",
u"""

	* mlib-prj.adb: Use friendlier english identifier.

	* gnatcmd.adb, make.adb: Use better english identifiers.


	* clean.adb: Minor reformatting


""",
u"""

	* einfo.adb (OK_To_Rename): New flag

	* einfo.ads (OK_To_Rename): New flag

	* exp_ch3.adb (Expand_N_Object_Declaration): Rewrite as renames if
	OK_To_Rename set.

	* exp_ch4.adb (Expand_Concatenate): Mark temp variable OK_To_Rename

	* sem_ch7.adb (Uninstall_Declarations): Allow for renames from
	OK_To_Rename.


""",
u"""
	* loop-iv.c (simple_rhs_p): Allow expressions that are
	function_invariant_p.


""",
u"""
	* loop-iv.c (replace_single_def_regs): Look for REG_EQUAL notes;
	follow chains of regs with a single definition, and allow expressions
	that are function_invariant_p.


""",
u"""

	* prj-proc.adb, make.adb, mlib-prj.adb, prj.adb, prj.ads, makeutl.adb,
	clean.adb, prj-nmsc.adb, prj-env.adb, prj-env.ads (Project_Data.Seen):
	field removed. This is not a property of the
	project, just a boolean used to traverse the project tree, and storing
	it in the structure prevents doing multiple traversal in parallel.
	(Project_Data.Checked): also removed, since it was playing the same role
	as Seen when we had two nested loops, and this is no longer necessary
	(For_All_Imported_Projects): removed, since in fact there was already
	the equivalent in For_Every_Project_Imported. The latter was rewritten
	to use a local hash table instead of Project_Data.Seen
	Various loops were rewritten to use For_Every_Project_Imported, thus
	removing the need for Project_Data.Seen. This avoids a lot of code
	duplication


""",
u"""

	* sem_res.adb (Resolve_Actuals): Do not create blocks around code
	statements, even though the actual of the call is a concatenation,
	because the argument is static, and we want to preserve warning
	messages  about sequences of code statements that are not marked
	volatile.

	* sem_warn.adb: remove obsolete comment about warning being obsolete

	* s-tasren.adb (Task_Do_Or_Queue): If a timed entry call is being
	requeued and the delay has expired while within the accept statement
	that executes the requeue, do not perform the requeue and indicate that
	the timed call has been aborted.


	* mlib-prj.adb, prj.adb, prj.ads, prj-nmsc.adb, prj-env.adb
	(Has_Ada_Sources, Has_Foreign_Sources): new subprograms
	(Project_Data.Ada_Sources_Present, Foreign_Sources_Present): removed,
	since they can be computed from the above.


""",
u"""
Minor reformatting.

""",
u"""

	* gnatcmd.adb: Call Prj.Env.Initialize with the Project_Tree

	* prj-env.adb: Move all global variables to the private part of the
	project tree data.
	Access these new components instead of the global variables no longer
	in existence.
	(Add_To_Path): New Project_Tree_Ref parameter, to access the new
	components that were previously global variables.

	* prj-env.ads (Initialize): New Project_Tree_Ref parameter
	(Set_Mapping_File_Initial_State_To_Empty): New Project_Tree_Ref
	parameter.

	* prj-nmsc.adb (Compute_Unit_Name): New Project_Tree_Ref parameter to
	be able to call Set_Mapping_File_Initial_State_To_Empty with it.

	* prj.adb (Initialize): Do not call Prj.Env.Initialize
	(Reset): Do not call Prj.Env.Initialize. Instead, initialize the new
	components in the private part of the project tree data.

	* prj.ads (Private_Project_Tree_Data): new components moved from
	Prj.Env: Current_Source_Path_File, Current_Object_Path_File,
	Ada_Path_Buffer, Ada_Path_Length, Ada_Prj_Include_File_Set,
	Ada_Prj_Objects_File_Set, Fill_Mapping_File.


""",
u"""

	PR middle-end/39867
	* fold-const.c (fold_cond_expr_with_comparison): When folding
	> and >= to MAX, make sure the MAX uses the same type as the
	comparison operands.

testsuite:

	PR middle-end/39867
	* gcc.dg/pr39867.c: New.


""",
u"""
        * config/frv/frv.c (frv_frame_access): Do not use reg+reg
        addressing for DImode accesses.
        (frv_print_operand_address): Handle PLUS case.
        * config/frv/frv.h (FIXED_REGISTERS): Mark link register as
        fixed.

""",
u"""

	* opt.ads (Unchecked_Shared_Lib_Imports): New Boolean flag.

	* prj-nmsc.adb (Check_Library): No error for imports by shared library
	projects, when --unchecked-shared-lib-imports is used.


	* sem_ch7.adb: Minor reformatting


""",
u"""

	* s-osinte-darwin.adb, s-osinte-darwin.ads: lwp_self now returns the
	mach thread id.


	* prj-env.adb, prj-env.ads (Body_Path_Name_Of, Spec_Path_Name_Of,
	Path_Name_Of_Library_Unit_Body): rEmove unused subprograms.
	(For_All_Imported_Projects): new procedure
	(For_All_Source_Dirs, For_All_Object_Dirs): Rewritten based on the
	above rather than duplicating code.


""",
u"""

	* prj-proc.adb, prj.adb, prj.ads, prj-nmsc.adb, prj-env.adb
	(Source_Id, Source_Data): use a real list to store sources rather than
	using an external table to store the elements. This makes code more
	efficient and more readable.


""",
u"""

	* prj-proc.adb, prj.adb, prj.ads, prj-nmsc.adb, prj-env.adb
	(Source_Iterator): new type.
        This removes the need for having the sources on three different
        lists at the project tree, project and language level. They are now
        on a single list.


""",
u"""

	* gnatcmd.adb, prj.adb, prj.ads: Remove unused entities


""",
u"""

	* sem_warn.adb: Add comment on obsolete warning


""",
u"""
        * prj.ads (Language_Ptr): Make a general access type.

""",
u"""

	* s-tassta.adb (Create_Task): Fix violation of locking rule.


""",
u"""

	* prj.adb, prj.ads, prj-nmsc.adb, prj-env.adb (Language_Index): renamed
	to Language_Ptr to better reflect its new implementation.
	(Project_Data.First_Languages_Processing): renamed to Languages now
	that the field with that name is no longer used
	(Project_Data.Languages): removed, no longer used, and duplicates
	information already available through First_Language_Processing.
	(Prj.Language_Index): now an actual pointer, instead of an index into
	a table. This makes the list somewhat more obvious, but more importantly
	removes the need to pass a pointer to the project_tree_data in a few
	places, and makes accessing the attributes of a languages more
	efficient.


""",
u"""
	* include/tr1_impl/array (at): Do not use builtin_expect.
	* include/ext/throw_allocator.h (allocate): Likewise.
	* include/ext/pool_allocator.h (allocate): Likweise.
	* include/ext/bitmap_allocator.h (allocate): Likewise.
	* include/ext/rc_string_base.h (_S_construct): Likewise.
	* include/ext/malloc_allocator.h (allocate): Likewise.
	* include/ext/mt_allocator.h (allocate): Likewise.
	* include/ext/sso_string_base.h (_M_construct): Likewise.
	* include/bits/basic_string.tcc (_S_construct): Likewise.

""",
u"""
Fix nit
""",
u"""
	* fe.h (Set_Identifier_Casing): Add const to second parameter.
	* gcc-interface/misc.c (internal_error_function): Make copy of retur
	from pp_formatted_text before assigning BUFFER to it.
	(gnat_init): Likewise for main_input_filename and gnat_argv.
	(gnat_printable_name): Remove cast from call to Set_Identifier_Casing.

""",
u"""

	PR fortran/39861
	PR fortran/39864
	* symbol.c (gfc_copy_formal_args_intr): Set attr.flavor and attr.dummy
	for the formal arguments.



	PR fortran/39861
	PR fortran/39864
	* gfortran.dg/intrinsic_1.f90: New.


""",
u"""
Fix nits
""",
u"""
	* ttypes.ads (Target_Double_Float_Alignment): New variable.
	(Target_Double_Scalar_Alignment): Likewise.
	* get_targ.ads (Get_Strict_Alignment): Adjust external name.
	(Get_Double_Float_Alignment): New imported function.
	(Get_Double_Scalar_Alignment): Likewise.
	* layout.adb (Set_Elem_Alignment): Take into account specific caps for
	the alignment of "double" floating-point types and "double" or larger
	scalar types, as parameterized by Target_Double_Float_Alignment and
	Target_Double_Scalar_Alignment respectively.
	* gcc-interface/gigi.h (double_float_alignment): Declare.
	(double_scalar_alignment): Likewise.
	(is_double_float_or_array): Likewise.
	(is_double_scalar_or_array): Likewise.
	(get_target_double_float_alignment): Likewise.
	(get_target_double_scalar_alignment): Likewise.
	* gcc-interface/targtyps.c (get_strict_alignment): Rename into...
	(get_target_strict_alignment): ...this.
	(get_target_double_float_alignment): New function.
	(get_target_double_scalar_alignment): Likewise.
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Signed_Integer_Subtype>:
	Test the presence of an alignment clause for under-aligned integer
	types.  Take into account specific caps for the alignment of "double"
	floating-point types and "double" or larger scalar types, as
	parameterized by Target_Double_Float_Alignment and
	Target_Double_Scalar_Alignment respectively.
	(validate_alignment): Likewise.
	* gcc-interface/trans.c (Attribute_to_gnu) <Attr_Alignment>: Likewise.
	(gigi): Initialize double_float_alignment and double_scalar_alignment.
	* gcc-interface/utils.c (double_float_alignment): New global variable.
	(double_scalar_alignment): Likewise.
	(is_double_float_or_array): New predicate.
	(is_double_scalar_or_array): Likewise.

""",
u"""
	* gcc-interface/utils2.c (build_cond_expr): Move SAVE_EXPR ahead of
	the conditional expression only if it is common to both arms.

""",
u"""
	* gcc-interface/gigi.h (build_call_alloc_dealloc): Update comment.
	* gcc-interface/decl.c (gnat_to_gnu_entity) <object>: Pass correct
	arguments to build_allocator.
	* gcc-interface/utils2.c (build_call_alloc_dealloc): Update comment.
	Remove code handling special allocator and assert its uselessness.

""",
u"""
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Array_Type>: If an
	alignment is specified, do not promote that of the component type
	beyond it.
	<E_Array_Subtype>: Likewise.

""",
u"""
	PR rtl-optimization/39794
	* alias.c (canon_true_dependence): Add x_addr argument.
	* rtl.h (canon_true_dependence): Adjust prototype.
	* cse.c (check_dependence): Adjust canon_true_dependence callers.
	* cselib.c (cselib_invalidate_mem): Likewise.
	* gcse.c (compute_transp): Likewise.
	* dse.c (scan_reads_nospill): Likewise.
	(record_store, check_mem_read_rtx): Likewise.  For non-const-or-frame
	addresses pass base->val_rtx as mem_addr, for const-or-frame addresses
	canon_base_addr of the group, plus optional offset.
	(struct group_info): Rename canon_base_mem to
	canon_base_addr.
	(get_group_info): Set canon_base_addr to canon_rtx of base, not
	canon_rtx of base_mem.

	* gcc.dg/pr39794.c: New test.

""",
u"""

	* config/sh/sh.c (sh_expand_prologue, sh_expand_epilogue):
	Use memory_address_p instead of GO_IF_LEGITIMATE_ADDRESS.


""",
u"""
Daily bump.
""",
u"""
	* config/spu/spu-builtins.h: Delete file.

	* config/spu/spu.h (enum spu_builtin_type): Move here from
	spu-builtins.h.
	(struct spu_builtin_description): Likewise.  Add GTY marker.
	Do not use enum spu_function_code or enum insn_code.
	(spu_builtins): Add extern declaration.

	* config/spu/spu.c: Do not include "spu-builtins.h".
	(enum spu_function_code, enum spu_builtin_type_index,
	V16QI_type_node, V8HI_type_node, V4SI_type_node, V2DI_type_node,
	V4SF_type_node, V2DF_type_node, unsigned_V16QI_type_node,
	unsigned_V8HI_type_node, unsigned_V4SI_type_node,
	unsigned_V2DI_type_node): Move here from spu-builtins.h.
	(spu_builtin_types): Make static.  Add GTY marker.
	(spu_builtins): Add extern declaration with GTY marker.
	Include "gt-spu.h".

	* config/spu/spu-c.c: Do not include "spu-builtins.h".
	(spu_resolve_overloaded_builtin): Do not use spu_function_code.
	Check programmatically whether all parameters are scalar.

	* config/spu/t-spu-elf (spu.o, spu-c.o): Update dependencies.

""",
u"""
	* gimplify.c (gimplify_modify_expr_rhs) <VAR_DECL>: Do not do a direct
	assignment from the constructor either if the target is volatile.
ada/
	* einfo.ads (Is_True_Constant): Lift restriction on atomic objects.
	* sinfo.ads (Object Declaration): Likewise.
	(Assignment Statement): Likewise.
	* freeze.adb (Expand_Atomic_Aggregate): Remove useless test.
	Do not force Is_True_Constant to false on the temporary.
	(Freeze_Entity): Do not force Is_True_Constant to false on names on
	the RHS of object declarations.
	* gcc-interface/trans.c (lvalue_required_p) <N_Object_Declaration>:
	New case.  Return 1 if the object is atomic.
	<N_Assignment_Statement>: Likewise.

""",
u"""
	PR testsuite/39623
	* gcc.dg/vect/no-vfa-vect-57.c: XFAIL when vect_no_align.
	* gcc.dg/vect/no-vfa-vect-61.c: Ditto.

""",
u"""
	* config/arm/arm.md (insv): Do not share operands[0].

""",
u"""
	* update_web_docs_svn: Redirect output of texi2dvi to /dev/null.

""",
u"""
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Modular_Integer_Subtype>
	For packed array types, make the original array type a parallel type
	for the modular type and its JM wrapper if the type is bit-packed.
	<E_Array_Subtype>: Likewise.  Do not generate the special XA parallel
	record type for packed array types.  Remove kludge.

""",
u"""
    gcc/cp/ChangeLog:
    	PR c++/38228
    	* pt.c (unify): Do not allow the result of a template argument
    	deduction to be a METHOD_TYPE.
    	* cvt.c (cp_convert): Report a meaningful error for non-valid use
    	of pointer to member functions during conversions.
    	* call.c (build_new_op): Report a meaningful error for non-valid
    	use of pointer to member functions in binary expressions.
    	* typeck.c (invalid_nonstatic_memfn_p): Do not crash when EXPR is
    	NULL;
    
    gcc/testsuite/ChangeLog:
    	PR c++/38228
    	* g++.dg/expr/bound-mem-fun.C: New test.


""",
u"""
	* gcc-interface/gigi.h (create_index_type): Adjust head comment.
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Signed_Integer_Subtype>:
	Use front-end predicates to compute signedness and precision.
	<E_String_Literal_Subtype>: Fold range type.
	Make sure to set longest_float_type_node to a scalar type.
	(elaborate_entity): Use consistent Constraint_Error spelling.
	(substitute_in_type) <INTEGER_TYPE>: Always copy the type.
	* gcc-interface/misc.c (gnat_print_type) <INTEGER_TYPE>: Use brief
	output for the modulus, if any.
	<ENUMERAL_TYPE>: Likewise for the RM size.
	* gcc-interface/trans.c (gnat_to_gnu): Use consistent Constraint_Error
	spelling.
	* gcc-interface/utils.c (finish_record_type): Really test the alignment
	of BLKmode bit-fields to compute their addressability.
	(create_index_type): Adjust comments.
	(create_param_decl): Create the biased subtype manually.
	* gcc-interface/utils2.c (build_component_ref): Use consistent
	Constraint_Error spelling.

""",
u"""
	* gcc-interface/cuintp.c: Clean up include directives.
	* gcc-interface/targtyps.c: Likewise.
	* gcc-interface/decl.c: Likewise.
	* gcc-interface/misc.c: Likewise.
	* gcc-interface/trans.c: Likewise.
	* gcc-interface/utils.c: Likewise.
	* gcc-interface/utils2.c: Likewise.
	* gcc-interface/Make-lang.in: Adjust dependencies accordingly.

""",
u"""
	* config/vxlib-tls.c (active_tls_threads): Delete.
	(delete_hook_installed): New.
	(tls_delete_hook): Don't delete the delete hook.
	(tls_destructor): Delete it here.
	(__gthread_set_specific): Adjust installing the delete hook.
	(tls_delete_hook): Use __gthread_enter_tsd_dtor_context and
	__gthread_leave_tsd_dtor_context.

""",
u"""

        * Makefile.am (install-data-local): Fix symlinks to header files.
        * Makefile.in: Regenerate.

""",
u"""
	* gcc-interface/ada-tree.h (union lang_tree_node): Use standard idiom.
	(SET_TYPE_LANG_SPECIFIC): Likewise.  Fix formatting.
	(SET_DECL_LANG_SPECIFIC): Likewise.
	Reorder macros.
	* gcc-interface/decl.c (gnat_to_gnu_entity) <E_Signed_Integer_Subtype>:
	Update comment about use of build_range_type.
	<E_Array_Type, E_Array_Subtype>: Use consistent naming convention.
	<E_Array_Subtype>: Rework comments about TYPE_ACTUAL_BOUNDS and add
	check for other cases of overloading.
	* gcc-interface/trans.c (gigi): Use size_int in lieu of build_int_cst.
	* gcc-interface/utils2.c (build_call_raise): Fix off-by-one error.
	Use size_int in lieu of build_int_cst.
	(build_call_alloc_dealloc): Use build_index_2_type in lieu of
	build_range_type.

""",
u"""

	* gcc.dg/format/gcc_diag-1.c (foo): Don't check that %E produces a
	warning.


	* c-format.c (gcc_tdiag_char_table): Add support for %E.


""",
u"""
	* config/alpha/alpha.c (alpha_legitimize_reload_address): Add cast to
	enum type.
	(alpha_rtx_costs): Ditto.
	(emit_unlikely_jump): Use add_reg_note.
	(emit_frame_store_1): Ditto.
	(alpha_expand_prologue): Ditto.
	(alpha_expand_builtin): Change 0 to EXPAND_NORMAL in function call.
	* config/alpha/alpha.c (Unicos/Mk address splitter): Use add_reg_note.


""",
u"""
        * config/v850/v850.md (epilogue): Remove suppressed code.
        (return): Rename to return_simple and remove test of frame size.
        * config/v850/v850.c (expand_epilogue): Rename call to gen_return
        to gen_return_simple.

""",
u"""
Add rs6000/xilinx.h -- missed in earlier checkin.


""",
u"""
Daily bump.
""",
u"""
	PR testsuite/39781
	* config/arm/arm.h: Define HANDLE_PRAGMA_PACK_PUSH_POP.


""",
u"""

        PR C/31499
        * c-typeck.c (process_init_element): Treat VECTOR_TYPE like ARRAY_TYPE
        and RECORD_TYPE/UNION_TYPE.  When outputing the actual element and the
        value is a VECTOR_CST, the element type is the element type of the
        vector.


        PR C/31499
        * gcc.dg/vector-init-1.c: New testcase.
        * gcc.dg/vector-init-2.c: New testcase.


""",
u"""

	* gnu/classpath/jdwp/natVMVirtualMachine.cc (handle_single_step):  Use
	casted pointer in debugging assert.
	(jdwpBreakpointCB):  Likewise.


""",
u"""
	* gcc-interface/utils2.c (build_binary_op) <PLUS_EXPR>: If operation's
	type is an enumeral or a boolean type, change it to an integer type
	with the same mode and signedness.

""",
u"""
	* gcc-interface/utils.c (create_var_decl_1): Do not emit debug info
	for an external constant whose initializer is not absolute.

""",
u"""
* config/m32c/m32c.h: Update GTY annotations to new syntax.

""",
u"""
	PR c/39855
	* fold-const.c (fold_binary) <case LSHIFT_EXPR>: When optimizing
	into 0, use omit_one_operand.

	* gcc.dg/torture/pr39855.c: New test.

""",
u"""
	* alias.c (find_base_term): Move around LO_SUM case, so that
	CONST falls through into PLUS/MINUS handling.

""",
u"""
	* config/rs6000/linux-unwind.h (get_regs): Remove type
	puns. Change the type of `pc' to an array of unsigned ints and
	update all users.  Constify frame24.

""",
u"""
* config/m32c/m32c.c (m32c_special_page_vector_p): Move
declarations before code.
(current_function_special_page_vector): Likewise.
(m32c_expand_insv): Silence a warning.

""",
u"""

    gcc/cp/ChangeLog:
    	PR c++/39639
    	* parser.c (cp_parser_template_argument_list): Display an error
    	when an ellipsis is not preceded by a parameter pack. Also, warn
    	about variadic templates usage without -std=c++0x.
    
    gcc/testsuite/ChangeLog:
    	PR c++/39639
    	* g++.dg/cpp0x/pr39639.C: New test.


""",
u"""

	* include/hashtab.h: Update GTY annotations to new syntax
	* include/splay-tree.h: Likewise


gcc/ChangeLog


	* alias.c: Update GTY annotations to new syntax
	* basic-block.h: Likewise
	* bitmap.h: Likewise
	* c-common.h: Likewise
	* c-decl.c: Likewise
	* c-parser.c: Likewise
	* c-pragma.c: Likewise
	* c-tree.h: Likewise
	* cfgloop.h: Likewise
	* cgraph.h: Likewise
	* config/alpha/alpha.c: Likewise
	* config/arm/arm.h: Likewise
	* config/avr/avr.h: Likewise
	* config/bfin/bfin.c: Likewise
	* config/cris/cris.c: Likewise
	* config/darwin.c: Likewise
	* config/frv/frv.c: Likewise
	* config/i386/i386.c: Likewise
	* config/i386/i386.h: Likewise
	* config/i386/winnt.c: Likewise
	* config/ia64/ia64.h: Likewise
	* config/iq2000/iq2000.c: Likewise
	* config/mips/mips.c: Likewise
	* config/mmix/mmix.h: Likewise
	* config/pa/pa.c: Likewise
	* config/pa/pa.h: Likewise
	* config/rs6000/rs6000.c: Likewise
	* config/s390/s390.c: Likewise
	* config/sparc/sparc.c: Likewise
	* config/xtensa/xtensa.c: Likewise
	* cselib.h: Likewise
	* dbxout.c: Likewise
	* dwarf2out.c: Likewise
	* except.c: Likewise
	* except.h: Likewise
	* fixed-value.h: Likewise
	* function.c: Likewise
	* function.h: Likewise
	* gimple.h: Likewise
	* integrate.c: Likewise
	* optabs.c: Likewise
	* output.h: Likewise
	* real.h: Likewise
	* rtl.h: Likewise
	* stringpool.c: Likewise
	* tree-data-ref.c: Likewise
	* tree-flow.h: Likewise
	* tree-scalar-evolution.c: Likewise
	* tree-ssa-address.c: Likewise
	* tree-ssa-alias.h: Likewise
	* tree-ssa-operands.h: Likewise
	* tree.c: Likewise
	* tree.h: Likewise
	* varasm.c: Likewise
	* varray.h: Likewise
	* vec.h: Likewise
	* coretypes.h: Do not define GTY macro if it is already defined
	* doc/gty.texi: Update GTY documentation to new syntax
	* gengtype-lex.l: Enforce attribute-like syntax for GTY annotations on structs
	* gengtype-parse.c: Likewise


gcc/ada/ChangeLog


	* gcc-interface/ada-tree.h: Update GTY annotations to new syntax
	* gcc-interface/trans.c: Likewise
	* gcc-interface/utils.c: Likewise


gcc/cp/ChangeLog


	* cp-tree.h: Update GTY annotations to new syntax
	* decl.c: Likewise
	* mangle.c: Likewise
	* name-lookup.c: Likewise
	* name-lookup.h: Likewise
	* parser.c: Likewise
	* pt.c: Likewise
	* rtti.c: Likewise
	* semantics.c: Likewise
	* typeck2.c: Likewise


gcc/fortran/ChangeLog


	* f95-lang.c: Update GTY annotations to new syntax
	* trans-intrinsic.c: Likewise
	* trans-io.c: Likewise
	* trans.h: Likewise


gcc/java/ChangeLog


	* builtins.c: Update GTY annotations to new syntax
	* decl.c: Likewise
	* java-tree.h: Likewise
	* jcf.h: Likewise
	* lang.c: Likewise


gcc/objc/ChangeLog


	* objc-act.c: Update GTY annotations to new syntax
	* objc-act.h: Likewise


libcpp/ChangeLog


	* include/cpp-id-data.h: Update GTY annotations to new syntax
	* include/cpplib.h: Likewise
	* include/line-map.h: Likewise
	* include/symtab.h: Likewise


""",
u"""

       * gcc.c (LINK_COMMAND_SPEC): Link with gcov with -fprofile-generate=.

       * gcc.dg/profile-generate-3.c: New test.

""",
u"""
	* include/c_std/cstdlib (abort, exit, _Exit): Mark noreturn throw ().
	(atexit, atoll, stroll, strtoull): Mark throw ()
	* include/c_std/cstdio (snprintf, vsnprintf, vscanf): Mark throw ().
	* include/c_std/cwchar (wcstold, wcstoll, wcstoull): Mark throw ().
	* include/c_global/cstdlib (abort, exit, _Exit): Mark noreturn throw ().
	(atexit, atoll, stroll, strtoull): Mark throw ()
	* include/c_global/cstdio (snprintf, vsnprintf, vscanf): Mark throw ().
	* include/c_wchar/cstdio (snprintf, vsnprintf, vscanf): Mark throw ().

""",
]
