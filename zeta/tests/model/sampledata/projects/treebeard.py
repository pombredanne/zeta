treebeard_description = \
u"""
SQL databases behave less like object collections the more size and
performance start to matter; object collections behave less like tables and
rows the more abstraction starts to matter. SQLAlchemy aims to accommodate
both of these principles.

SQLAlchemy doesn't view databases as just collections of tables; it sees them
as relational algebra engines. Its object relational mapper enables classes to
be mapped against the database in more than one way. SQL constructs don't just
select from just tables you can also select from joins, subqueries, and
unions. Thus database relationships and domain object models can be cleanly
decoupled from the beginning, allowing both sides to develop to their full
potential.

The main goal of SQLAlchemy is to change the way you think about databases and
SQL!

Most importantly, SQLAlchemy is not just an ORM. Its data abstraction layer
allows construction and manipulation of SQL expressions in a platform agnostic
way, and offers easy to use and superfast result objects, as well as table
creation and schema reflection utilities. No object relational mapping
whatsoever is involved until you import the orm package. Or use SQLAlchemy to
write your own !
"""

treebeard_compdesc    = \
[
u"""
The **Engine** is the starting point for any SQLAlchemy application.  It's
"home base" for the actual database and its DBAPI, delivered to the SQLAlchemy
application through a connection pool and a **Dialect**, which describes how
to talk to a specific kind of database/DBAPI combination.
""",
u"""
This section references most major configurational patterns involving the
:func:`~sqlalchemy.orm.mapper` and :func:`~sqlalchemy.orm.relation` functions.
It assumes you've worked through :ref:`ormtutorial_toplevel` and know how to
construct and use rudimentary mappers and relations. The default behavior of a
``mapper`` is to assemble all the columns in the mapped ``Table`` into mapped
object attributes.  This behavior can be modified in several ways, as well as
enhanced by SQL expressions.
""",
u"""
The core of SQLAlchemy's query and object mapping operations are supported by
**database metadata**, which is comprised of Python objects that describe
tables and other schema-level objects.  These objects can be created by
explicitly naming the various components and their properties, using the
Table, Column, ForeignKey, Index, and Sequence objects imported from
``sqlalchemy.schema``.  There is also support for **reflection** of some
entities, which means you only specify the *name* of the entities and they are
recreated from the database automatically.""",
u"""
The `Mapper` is the entrypoint to the configurational API of the SQLAlchemy
object relational mapper.  But the primary object one works with when using
the ORM is the :class:`~sqlalchemy.orm.session.Session`.
"""
]

treebeard_mstndesc    = \
[
u"""
# Significant performance enhancements regarding Sessions/flush() in conjunction with large mapper graphs, large numbers of objects:
# Removed all* O(N) scanning behavior from the flush() process, i.e. operations that were scanning the full session, including an extremely expensive one that was erroneously assuming primary key values were changing when this was not the case.
# The Session's "weak referencing" behavior is now *full* - no strong references whatsoever are made to a mapped object or related items/collections in its __dict__.  Backrefs and other cycles in objects no longer affect the Session's ability to lose all references to unmodified objects.  Objects with pending changes still are maintained strongly until flush.
# The unit of work no longer genererates a graph of "dependency" processors for the full graph of mappers during flush(), instead creating such processors only for those mappers which represent objects with pending changes.  This saves a tremendous number of method calls in the context of a large interconnected graph of mappers.
# Cached a wasteful "table sort" operation that previously occured multiple times per flush, also removing significant method call count from flush().  
# Other redundant behaviors have been simplified in mapper._save_obj().
# Modified query_cls on DynamicAttributeImpl to accept a full mixin version of the AppenderQuery, which allows subclassing the AppenderMixin.
""",
u"""
# Session.scalar() now converts raw SQL strings to text() the same way Session.execute() does and accepts same alternative **kw args.  
# improvements to the "determine direction" logic of relation() such that the direction of tricky situations like mapper(A.join(B)) -> relation-> mapper(B) can be determined.
# When flushing partial sets of objects using session.flush([somelist]), pending objects which remain pending after the operation won't inadvertently be added as persistent. [ticket:1306]
# Added "post_configure_attribute" method to InstrumentationManager, so that the "listen_for_events.py" example works again.  [ticket:1314]
# a forward and complementing backwards reference which are both of the same direction, i.e. ONETOMANY or MANYTOONE, is now detected, and an error message is raised.   Saves crazy CircularDependencyErrors later on.  
# Fixed bugs in Query regarding simultaneous selection of multiple joined-table inheritance entities with common base classes: 
""",
u"""
# It is now an error to specify both columns of a binary primaryjoin condition in the foreign_keys or remote_side collection.  Whereas previously it was just nonsensical, but would succeed in a non-deterministic way.
# Added a quote_schema() method to the IdentifierPreparer class so that dialects can override how schemas get handled. This enables the MSSQL dialect to treat schemas as multipart identifiers, such as 'database.owner'. [ticket: 594, 1341]
# Back-ported the "compiler" extension from SQLA 0.6.  This is a standardized interface which allows the creation of custom ClauseElement subclasses and compilers.  In particular it's handy as an alternative to text() when you'd like to build a construct that has database-specific compilations.  See the extension docs for details.
# Exception messages are truncated when the list of bound parameters is larger than 10, preventing enormous multi-page exceptions from filling up screens and logfiles for large executemany() statements. [ticket:1413] 
# ``sqlalchemy.extract()`` is now dialect sensitive and can extract components of timestamps idiomatically across the supported databases, including SQLite.  
""",
u"""
# Reflecting a FOREIGN KEY construct will take into account a dotted schema.tablename combination, if the foreign key references a table in a remote schema. [ticket:1405] 
# Modified how savepoint logic works to prevent it from stepping on non-savepoint oriented routines. Savepoint support is still very experimental.  
# Added in reserved words for MSSQL that covers version 2008 and all prior versions. [ticket:1310]
# Corrected problem with information schema not working with a binary collation based database. Cleaned up information schema since it is only used by mssql now. [ticket:1343]
# Corrected the SLBoolean type so that it properly treats only 1 as True. [ticket:1402]
# Corrected the float type so that it correctly maps to a SLFloat type when being reflected. [ticket:1273]
""",
u"""
# Query.group_by() properly takes into account aliasing applied to the FROM clause, such as with select_from(), using with_polymorphic(), or using from_self().  
# An alias() of a select() will convert to a "scalar subquery" when used in an unambiguously scalar context, i.e. it's used in a comparison operation.  This applies to the ORM when using query.subquery() as well.
# Fixed missing _label attribute on Function object, others when used in a select() with use_labels (such as when used in an ORM column_property()).  [ticket:1302] 
# anonymous alias names now truncate down to the max length allowed by the dialect.  More significant on DBs like Oracle with very small character limits. [ticket:1309] 
# the __selectable__() interface has been replaced entirely by __clause_element__().
# The per-dialect cache used by TypeEngine to cache dialect-specific types is now a WeakKeyDictionary.  This to prevent dialect objects from being referenced forever for an application that creates an arbitrarily large number of engines or dialects.   There is a small performance penalty which will be resolved in 0.6.  [ticket:1299]
""",
]

treebeard_verdesc     = \
[
u"""
* Fixed bug introduced in 0.5.4 whereby Composite types fail when default-holding columns are flushed.
* Repaired the printing of SQL exceptions which are not based on parameters or are not executemany() style.
* Deprecated the hardcoded TIMESTAMP function, which when used as func.TIMESTAMP(value) would render "TIMESTAMP value".  This breaks on some platforms as Postgres doesn't allow bind parameters to be used in this context.  The hard-coded uppercase is also inappropriate and there's lots of other PG casts that we'd need to support.  So instead, use text constructs i.e. select(["timestamp '12/05/09'"]).
* Fixed an attribute error introduced in 0.5.4 which would occur when merge() was used with an incomplete object.
""",
u"""
* The "polymorphic discriminator" column may be part of a primary key, and it will be populated with the correct discriminator value.  [ticket:1300]
* Fixed the evaluator not being able to evaluate IS NULL clauses.  
* Fixed the "set collection" function on "dynamic" relations to initiate events correctly.  Previously a collection could only be assigned to a pending parent instance, otherwise modified events would not be fired correctly.  Set collection is now compatible with merge(), fixes [ticket:1352].
* Allowed pickling of PropertyOption objects constructed with instrumented descriptors; previously, pickle errors would occur when pickling an object which was loaded with a descriptor-based option, such as query.options(eagerload(MyClass.foo)).
* Lazy loader will not use get() if the "lazy load" SQL clause matches the clause used by get(), but contains some parameters hardcoded.  Previously the lazy strategy would fail with the get().  Ideally get() would be used with the hardcoded parameters but this would require further development.
* MapperOptions and other state associated with query.options() is no longer bundled within callables associated with each lazy/deferred-loading attribute during a load.  The options are now associated with the instance's state object just once when it's populated.  This removes the need in most cases for per-instance/attribute loader objects, improving load speed and memory overhead for individual instances. [ticket:1391]
""",
u"""
* Fixed another location where autoflush was interfering with session.merge().  autoflush is disabled completely for the duration of merge() now. [ticket:1360] 
* Fixed bug which prevented "mutable primary key" dependency logic from functioning properly on a one-to-one relation().  [ticket:1406] 
* Fixed bug in relation(), introduced in 0.5.3, whereby a self referential relation from a base class to a joined-table subclass would not configure correctly.
* Fixed obscure mapper compilation issue when inheriting mappers are used which would result in un-initialized attributes.
* Fixed documentation for session weak_identity_map - the default value is True, indicating a weak referencing map in use.
* Fixed a unit of work issue whereby the foreign key attribute on an item contained within a collection owned by an object being deleted would not be set to None if the relation() was self-referential. [ticket:1376]
* Fixed Query.update() and Query.delete() failures with eagerloaded relations. [ticket:1378] 
""",
u"""
* Fixed adding of deferred or other column properties to a declarative class. [ticket:1379]
* The "objects" argument to session.flush() is deprecated.  State which represents the linkage between a parent and child object does not support "flushed" status on one side of the link and not the other, so supporting this operation leads to misleading results.  [ticket:1315]
* Query now implements __clause_element__() which produces its selectable, which means a Query instance can be accepted in many SQL expressions, including col.in_(query), union(query1, query2), select([foo]).select_from(query), etc.
* Query.join() can now construct multiple FROM clauses, if needed.  Such as, query(A, B).join(A.x).join(B.y) might say SELECT A.*, B.* FROM A JOIN X, B JOIN Y.  Eager loading can also tack its joins onto those multiple FROM clauses.  [ticket:1337]
* Fixed bug in dynamic_loader() where append/remove events after construction time were not being propagated to the UOW to pick up on flush(). [ticket:1347]
* Fixed bug where column_prefix wasn't being checked before not mapping an attribute that already had class-level name present.
* a session.expire() on a particular collection attribute will clear any pending backref additions as well, so that the next access correctly returns only what was present in the database.  Presents some degree of a workaround for [ticket:1315], although we are considering removing the flush([objects]) feature altogether.
""",
u"""
* previously the adaption applied to "B" on "A JOIN B" would be erroneously partially applied to "A".  
* comparisons on relations (i.e. A.related==someb) were not getting adapted when they should.  
* Other filterings, like query(A).join(A.bs).filter(B.foo=='bar'), were erroneously adapting "B.foo" as though it were an "A".
* Fixed adaptation of EXISTS clauses via any(), has(), etc.  in conjunction with an aliased object on the left and of_type() on the right.  [ticket:1325] 
* Added an attribute helper method ``set_committed_value`` in sqlalchemy.orm.attributes.  Given an object, attribute name, and value, will set the value on the object as part of its "committed" state, i.e. state that is understood to have been loaded from the database.   Helps with the creation of homegrown collection loaders and such.  
* Query won't fail with weakref error when a non-mapper/class instrumented descriptor is passed, raises "Invalid column expession".  
""",
]

treebeard_comments    = \
[
u"""
This document provides an overview of lexing and parsing with PLY. Given the intrinsic complexity of parsing, I would strongly advise that you read (or at least skim) this entire document before jumping into a big development project with PLY.
""",
u"""
PLY-3.0 is compatible with both Python 2 and Python 3. Be aware that Python 3 support is new and has not been extensively tested (although all of the examples and unit tests pass under Python 3.0). If you are using Python 2, you should try to use Python 2.4 or newer. Although PLY works with versions as far back as Python 2.2, some of its optional features require more modern library modules.
PLY is a pure-Python implementation of the popular compiler construction tools lex and yacc. The main goal of PLY is to stay fairly faithful to the way in which traditional lex/yacc tools work. This includes supporting LALR(1) parsing as well as providing extensive input validation, error reporting, and diagnostics. Thus, if you've used yacc in another programming language, it should be relatively straightforward to use PLY.
""",
u"""
Early versions of PLY were developed to support an Introduction to Compilers Course I taught in 2001 at the University of Chicago. In this course, students built a fully functional compiler for a simple Pascal-like language. Their compiler, implemented entirely in Python, had to include lexical analysis, parsing, type checking, type inference, nested scoping, and code generation for the SPARC processor. Approximately 30 different compiler implementations were completed in this course. Most of PLY's interface and operation has been influenced by common usability problems encountered by students. Since 2001, PLY has continued to be improved as feedback has been received from users. PLY-3.0 represents a major refactoring of the original implementation with an eye towards future enhancements.
""",
u"""
Since PLY was primarily developed as an instructional tool, you will find it to be fairly picky about token and grammar rule specification. In part, this added formality is meant to catch common programming mistakes made by novice users. However, advanced users will also find such features to be useful when building complicated grammars for real programming languages. It should also be noted that PLY does not provide much in the way of bells and whistles (e.g., automatic construction of abstract syntax trees, tree traversal, etc.). Nor would I consider it to be a parsing framework. Instead, you will find a bare-bones, yet fully capable lex/yacc implementation written entirely in Python.
""",
u"""
The rest of this document assumes that you are somewhat familar with parsing theory, syntax directed translation, and the use of compiler construction tools such as lex and yacc in other programming languages. If you are unfamilar with these topics, you will probably want to consult an introductory text such as "Compilers: Principles, Techniques, and Tools", by Aho, Sethi, and Ullman. O'Reilly's "Lex and Yacc" by John Levine may also be handy. In fact, the O'Reilly book can be used as a reference for PLY as the concepts are virtually identical.
""",
u"""
PLY consists of two separate modules; lex.py and yacc.py, both of which are found in a Python package called ply. The lex.py module is used to break input text into a collection of tokens specified by a collection of regular expression rules. yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar. yacc.py uses LR parsing and generates its parsing tables using either the LALR(1) (the default) or SLR table generation algorithms.
""",
u"""
The two tools are meant to work together. Specifically, lex.py provides an external interface in the form of a token() function that returns the next valid token on the input stream. yacc.py calls this repeatedly to retrieve tokens and invoke grammar rules. The output of yacc.py is often an Abstract Syntax Tree (AST). However, this is entirely up to the user. If desired, yacc.py can also be used to implement simple one-pass compilers.
""",
u"""
Like its Unix counterpart, yacc.py provides most of the features you expect including extensive error checking, grammar validation, support for empty productions, error tokens, and ambiguity resolution via precedence rules. In fact, everything that is possible in traditional yacc should be supported in PLY.
""",
u"""
The primary difference between yacc.py and Unix yacc is that yacc.py doesn't involve a separate code-generation process. Instead, PLY relies on reflection (introspection) to build its lexers and parsers. Unlike traditional lex/yacc which require a special input file that is converted into a separate source file, the specifications given to PLY are valid Python programs. This means that there are no extra source files nor is there a special compiler construction step (e.g., running yacc to generate Python code for the compiler). Since the generation of the parsing tables is relatively expensive, PLY caches the results and saves them to a file. If no changes are detected in the input source, the tables are read from the cache. Otherwise, they are regenerated.
""",
u"""
lex.py is used to tokenize an input string. For example, suppose you're writing a programming language and a user supplied the following input string:
    x = 3 + 42 * (s - t)
""",
u"""
Lexers also support the iteration protocol. So, you can write the above loop as follows:
    for tok in lexer:
        print tok
""",
u"""
The tokens returned by lexer.token() are instances of LexToken. This object has attributes tok.type, tok.value, tok.lineno, and tok.lexpos. The following code shows an example of accessing these attributes:
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok.type, tok.value, tok.line, tok.lexpos
""",
u"""
Each token is specified by writing a regular expression rule. Each of these rules are are defined by making declarations with a special prefix t_ to indicate that it defines a token. For simple tokens, the regular expression can be specified as strings such as this (note: Python raw strings are used since they are the most convenient way to write regular expression strings):
    t_PLUS = r'\+'
""",
u"""
In this case, the name following the t_ must exactly match one of the names supplied in tokens. If some kind of action needs to be performed, a token rule can be specified as a function. For example, this rule matches numbers and converts the string into a Python integer.
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t
""",
u"""
When a function is used, the regular expression rule is specified in the function documentation string. The function always takes a single argument which is an instance of LexToken. This object has attributes of t.type which is the token type (as a string), t.value which is the lexeme (the actual text matched), t.lineno which is the current line number, and t.lexpos which is the position of the token relative to the beginning of the input text. By default, t.type is set to the name following the t_ prefix. The action function can modify the contents of the LexToken object as appropriate. However, when it is done, the resulting token should be returned. If no value is returned by the action function, the token is simply discarded and the next token read.
""",
u"""
Internally, lex.py uses the re module to do its patten matching. When building the master regular expression, rules are added in the following order:
   1. All tokens defined by functions are added in the same order as they appear in the lexer file.
   2. Tokens defined by strings are added next by sorting them in order of decreasing regular expression length (longer expressions are added first). 
""",
u"""
Without this ordering, it can be difficult to correctly match certain types of tokens. For example, if you wanted to have separate tokens for "=" and "==", you need to make sure that "==" is checked first. By sorting regular expressions in order of decreasing length, this problem is solved for rules defined as strings. For functions, the order can be explicitly controlled since rules appearing first are checked first.
""",
u"""
This approach greatly reduces the number of regular expression rules and is likely to make things a little faster.
Note: You should avoid writing individual rules for reserved words. For example, if you write rules like this,
    t_FOR   = r'for'
    t_PRINT = r'print'
those rules will be triggered for identifiers that include those words as a prefix such as "forget" or "printed". This is probably not what you want.
""",
u"""
When tokens are returned by lex, they have a value that is stored in the value attribute. Normally, the value is the text that was matched. However, the value can be assigned to any Python object. For instance, when lexing identifiers, you may want to return both the identifier name and information from some sort of symbol table. To do this, you might write a rule like this:
    def t_ID(t):
        ...
        # Look up symbol table information and return a tuple
        t.value = (t.value, symbol_lookup(t.value))
        ...
        return t
""",
u"""
It is important to note that storing data in other attribute names is not recommended. The yacc.py module only exposes the contents of the value attribute. Thus, accessing other attributes may be unnecessarily awkward. If you need to store multiple values on a token, assign a tuple, dictionary, or instance to value.
""",
u"""
To discard a token, such as a comment, simply define a token rule that returns no value. For example:
    def t_COMMENT(t):
        r'\#.*'
        pass
        # No return value. Token discarded
""",
u"""
Alternatively, you can include the prefix "ignore_" in the token declaration to force a token to be ignored. For example:
    t_ignore_COMMENT = r'\#.*'
Be advised that if you are ignoring many different kinds of text, you may still want to use functions since these provide more precise control over the order in which regular expressions are matched (i.e., functions are matched in order of specification whereas strings are sorted by regular expression length).
""",
u"""
By default, lex.py knows nothing about line numbers. This is because lex.py doesn't know anything about what constitutes a "line" of input (e.g., the newline character or even if the input is textual data). To update this information, you need to write a special rule. In the example, the t_newline() rule shows how to do this.

    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

""",
u"""
Within the rule, the lineno attribute of the underlying lexer t.lexer is updated. After the line number is updated, the token is simply discarded since nothing is returned.
""",
u"""
- Add support for create_engine(isolation_level=...); postgres &
  sqlite initially [ticket:443]
- Dialects gain visit_pool
- Pools gained a first_connect event

""",
u"""
- rollback everything before dropping tables.   PG + jython is a rough combo
- zxJDBC totally not returning rowcounts correctly
- some dict ordering for jython

""",
u"""
- jython support.  works OK for expressions, there's a major weakref bug in ORM tho
- reraises of exceptions pass along the original stack trace


""",
u"""
- connection initialize moves to a connection pool event [ticket:1340]
- sqlite doesn't support schemas.  not sure if some versions do, but marking those as unsupported for now.
- added a testing.requires callable for schema support.
- standardized the "extra schema" name for unit tests as "test_schema" and "test_schema_2".
- sqlite needs description_encoding (was some other version of pysqlite tested here ?)
- other test fixes.

""",
u"""
- modernized UnicodeTest/BinaryTest
- removed PickleType homegrown comparison method
- testtypes passes in 3k for sqlite/pg8000

""",
u"""
- sql round trips are coming on line for sqlite, pg8000
- pg8000 returns col.description as bytes, heh
- absolute module imports play havoc with "python test/foo/test.py" - start using -m

""",
u"""
use sqlalchemy.util functions here.  the previous implementation is
not compatible with py3k.   I can run all tests or any combination of tests
by using sqlalchemy.util so it's not clear to me why sqlalchemy.util 
reportedly cannot be imported at this phase.

""",
u"""
- the 'expire' option on query.update() has been renamed to 'fetch', thus matching
that of query.delete()
- query.update() and query.delete() both default to 'evaluate' for the synchronize 
strategy.
- the 'synchronize' strategy for update() and delete() raises an error on failure.  
There is no implicit fallback onto "fetch".   Failure of evaluation is based
on the structure of criteria, so success/failure is deterministic based on 
code structure.


""",
u"""
- added a compiler extension that allows easy creation of user-defined compilers,
which register themselves with custom ClauseElement subclasses such that the compiler
is invoked along with the primary compiler.  The compilers can also be registered
on a per-dialect basis.

This provides a supported path for SQLAlchemy extensions such as ALTER TABLE 
extensions and other SQL constructs.


""",
u"""
- more or less pg8000 support. has a rough time with non-ascii data.
- removed "send unicode straight through" logic from sqlite, this becomes
base dialect configurable
- simplfied Interval type to not have awareness of PG dialect.  dialects
can name TypeDecorator classes in their colspecs dict.

""",
u"""
- mysql+pyodbc working for regular usage, ORM, etc.   types and unicode still flaky.
- updated testing decorators to receive  "name+driver"-style specifications

""",
u"""
- It's an error to add new Column objects to a declarative class
that specified an existing table using __table__.


""",
u"""
- Column with no name (as in declarative) won't raise a 
NoneType error when it's string output is requsted
(such as in a stack trace).


""",
u"""
- Fixed a bug with the unitofwork's "row switch" mechanism,
i.e. the conversion of INSERT/DELETE into an UPDATE, when
combined with joined-table inheritance and an object
which contained no defined values for the child table where
an UPDATE with no SET clause would be rendered.


""",
u"""
- Can now specify Column objects on subclasses which have no
table of their own (i.e. use single table inheritance).  
The columns will be appended to the base table, but only
mapped by the subclass.

- For both joined and single inheriting subclasses, the subclass
will only map those columns which are already mapped on the 
superclass and those explicit on the subclass.  Other 
columns that are present on the `Table` will be excluded
from the mapping by default, which can be disabled
by passing a blank `exclude_properties` collection to the
`__mapper_args__`.  This is so that single-inheriting
classes which define their own columns are the only classes
to map those columns.   The effect is actually a more organized
mapping than you'd normally get with explicit `mapper()`
calls unless you set up the `exclude_properties` arguments
explicitly.

- docs/tests


""",
u"""
Corrected SAVEPOINT support on the adodbapi dialect by changing the handling
of savepoint_release, which is unsupported on mssql.

The way it was being discarded previously resulted in an empty execute being
called on the dialect; adodbapi didn't like that much.
""",
u"""
Modified the do_begin handling in mssql to use the Cursor not the Connection.

This corrects a problem where we were trying to call execute on the Connection
object instead of against the cursor. This is supported on pyodbc but not in
the DBAPI. Overrode the behavior in pymssql to not do special do_begin
processing on that dialect.
""",
u"""
- 0.5.1 bump
- modernized mapper()/no table exception
- added __tablename__ exception to declarative since ppl keep complaining

""",
u"""
fix some tests, a py3k import
""",
u"""
oops, checked in a pdb
""",
u"""
merged -r5974:5987 of trunk
""",
u"""
fixes
""",
u"""
schema, reflection, and type refinements.  in particular the default precision/scale args are 
removed from Numeric/Float.
""",
u"""
most ORM tests passing in py3.1 with these changes
""",
u"""
move StringIO to its own line  for 2to3 compat
""",
u"""
- pg8000 fixes
- removed hardcoded TIMESTAMP func, deprecated in 0.5.4p2
""",
u"""
merged r5976
""",
u"""
merge -r5936:5974 of trunk
""",
u"""
refactor
""",
u"""
fix _sort not always using the node's id as its key
fixes #1380

""",
u"""
merge r5939 from trunk

""",
u"""
merged -r 5869:5936 of trunk, including dialect changes re: extract()

    """,
u"""
explicitly gc_collect weakref tests
fixes #1382

""",
u"""
merge r5895 from trunk
""",
u"""
fix mssql cursor closed issue on reflection
""",
u"""
pass cache to _prepare_reflection_args
""",
u"""
cache _prepare_reflection_args
""",
u"""
removed attrs key from get_columns return value
""",
u"""
removed unecessary oracle specific logic
""",
u"""
moved reflecttable to inspector for mssql
""",
u"""
removed the connection_memoize stuff.
""",
u"""
raise NoSuchTableError in reflecttable
""",
u"""
Corrected mysql import for CLIENT_FLAGS. Added commented out memoize decorators that will not work without a ProxyConnection.
""",
u"""
Corrected mysql version info check.
""",
u"""
moved reflecttable to inspector for postgresql, oracle, sqlite and mysql
""",
u"""
Corrected exception references in Postgres dialect.
""",
u"""
standardized tests on test_schema and test_schema_2.
""",
u"""
Fixed function call counts for 2.5 / 2.6
""",
u"""
Typo in docstring
""",
u"""
Whitespace normalization, adjust some docstrings to reST/Sphinx conventions
""",
u"""
Reverting property workaround
""",
u"""
Migrated gc.collect hack to testlib.compat
""",
u"""
Patch-o
""",
u"""
Updated $py.class ignores
""",
u"""
And added this one
""",
u"""
Adding missing sqlite portion of alowry's patch from r5881
""",
u"""
Special gc.collect() tickling for Jython patch from pjenvey
""",
u"""
a myriad of close_first calls to get sql.alltests to run

""",
u"""
the return of --mockpool, mocking you and your crappy code that doesn't clean up after itself

""",
u"""
Minor changes to adodbapi.
""",
u"""
Corrected MSSQL support for 0.6.
""",
u"""
a pared down ext.compiler with minimal boilerplate.

""",
u"""
revert back to the 0.5 way of calling DBAPIError.instance(), but add the tback as the 3rd argument.  didn't realize this
usage.  sorry empty !

""",
u"""
Fixed up the tests for the new style exception instance_cls.
""",
u"""
Corrections to 0.6 to fix mssql problems.
""",
u"""
merged -r5841:5869 of trunk, including a local information_schema.py for MSSQL

""",
u"""
Set the set in __builtins__ check to Py2-only, set is always available in Py3
I believe some other test may be overriding __builtins__ to be a dict instead of a module only on Py3, but this is the easiest fix.


""",
u"""
Removed __builtin__ and buffer hack for MySQLdb for Py3

""",
u"""
updated documentation
""",
u"""
changed file() to open() for better portability

""",
u"""
minor updates to documentation strings
""",
u"""
moved tests in test/reflection.py into test/engine/reflection.py
""",
u"""
refactored reflecttable
""",
u"""
- merged -r5797:5841 of trunk, including ported changes to MSSQL, Postgres
- got server_version_info attribute on sqlite, postgres, needs work

""",
u"""
reflection fully implemented for mysql
""",
u"""
fixed pkey for include_columns and fkey options
""",
u"""
applied Michael's patch to fix issue with CREATE TABLE parser state
""",
u"""
refactored mysql to separtate parsing from reflecting
""",
u"""
moved get_table_names
""",
u"""
added check for get_default_schema_name implementation
""",
u"""
added **kw to base BaseDialect reflection method sigs
""",
u"""
added reflection methods
""",
u"""
dialects can subclass Inspector
""",
u"""
removed redundant methods from Inspector
""",
u"""
using util.decorator and adding *kw to reflection method signatures
""",
u"""
updates for latest 0.6 of sphinx

""",
u"""
moving to simpler cache technique
""",
u"""
refactored. tests/dialects/sqlite and tests/engine/reflection pass
""",
u"""
reflection methods not use decorator for caching
""",
u"""
finished oracle - all tests pass
""",
u"""
- merged -r5727:5797 of trunk
- newest pg8000 handles unicode statements correctly.

""",
u"""
normalized reflection arguments
""",
u"""
essential refactoring complete - tests pass
""",
u"""
added more methods for convenience
""",
u"""
make sure inputs are unicode when binding to unicode
""",
u"""
refactored mssql for reflection (tests pass/fail same)
    """,
u"""
set info_cache class
""",
u"""
fixed view support
""",
u"""
revised to use PGInfoCache
""",
u"""
added DefaultInfoCache
""",
u"""
added order_by='foreign_key' option to help with dependency checking
""",
u"""
added reflection (inspector) and tests
""",
u"""
additional reflection methods
""",
u"""
completed refactoring of reflecttable
""",
u"""
factored out column reflection from reflecttable
""",
u"""
most orm tests are passing in 3k with pysqlite.  collections the biggest area left.

""",
u"""
some lists to iterators

""",
u"""
select.py passes in 3k

""",
u"""
test/base/alltests passes in 3k

""",
u"""
most folks dont put "./lib/" in their PYTHONPATH.   so replace with the same approach as that of util.

""",
u"""
Switched ext compiler test to use sqlite.
""",
u"""
Get the callable import right.
""",
u"""
Callable must be defined before path magic occurs.
""",
u"""
Resolved merge conflict.
""",
u"""
Couple more corrections to get mssql tests to pass.
""",
u"""
py3king

""",
u"""
2to3 wrapper which includes a preprocessor

""",
u"""
test fixes

""",
u"""
Fixed up some of the mssql dialect tests for date handling.
""",
u"""
correct subclassing

""",
u"""
jek's name change

""",
u"""
doc

""",
u"""
- dialect.type_descriptor() becomes a classmethod
- TypeEngine caches types in impl_dict per dialect class
[ticket:1299]

""",
u"""
A couple of cleanup items to remove pdb and correct dialect name on informix.
""",
u"""
mssql type fixes....
""",
u"""
Corrections to MSSQL Date/Time types; generalized server_version_info to a create_engine() pre-step
""",
u"""
0.6 development branch

""",
u"""
hand-merged pg/mssql changes from trunk -r5699:5727

""",
u"""
merged -r5699:5727 of trunk

""",
u"""
One more mssql dialect test fix.
""",
u"""
Working through dialect changes.
""",
u"""
A couple of fixes for the mssql dialect to correct restructuring / renaming.
""",
u"""
caps adjust

""",
u"""
some import fixes

""",
u"""
- mssql dialects are in place, not fully tested

""",
u"""
- pg uses generic Biginteger now
- fix to _is_excluded() function

""",
u"""
a little guide on how im thinking about types

""",
u"""
remove pyc

""",
u"""
- moved all the dialects over to their final positions
- structured maxdb, sybase, informix dialects.  obviously no testing has been done.

""",
u"""
merged -r5676:5699 of trunk

""",
u"""
import cleanup

""",
u"""
- oracle support, includes fix for #994

""",
u"""
pg8000 handling unicode fine now

""",
u"""
convert_unicode by default clears up the issue for now

""",
u"""
more mysql+pyodbc fixes

""",
u"""
merge -r5673:5675 of trunk

""",
u"""
more test fixup, type correction

""",
u"""
the most epic dialect of all.  the MYSQL DIALECT.  didn't port the dialect test over yet.

""",
u"""
our likely approach towards documentation of generic driver + dbapi driver

""",
u"""
merge -r5658:5665 from trunk

""",
u"""
first merge from the hg repo.  may need cleanup/refreshing

""",
u"""
break out dialects and drivers

""",
u"""
prefer this methods

""",
u"""
- Tightened up **kw on ColumnProperty and its front-end functions.

""",
u"""
happy new year

""",
u"""
oh, its UNION ordering that's changing

""",
u"""
more comparator tweaks

""",
u"""
Ensure RowTuple names are correct by adding "key" to QueryableAttribute.

""",
u"""
suspect the InstrumentedSet/set comparison is failing for some reason

""",
u"""
*more* sqlite appeasement

""",
u"""
mysql/pg sensitive fixes

""",
u"""
don't INSERT a blank row if no rows passed. (breaks all the tests for SQLite on the buildbot....)

""",
u"""
NotSupportedError is a DBAPI wrapper which takes four args and is expected to originate from the DBAPI layer.
Moved those error throws to CompileError/InvalidRequestError.

""",
u"""
added an order by 

""",
u"""
- Concrete inheriting mappers now instrument attributes which are inherited from the superclass, but are not defined for the concrete mapper itself, with an InstrumentedAttribute that issues a descriptive error when accessed.  [ticket:1237]
- Added a new `relation()` keyword `back_populates`.  This allows configuation of backreferences using explicit relations. [ticket:781]  This is required when creating bidirectional relations between a hierarchy of concrete mappers and another class. [ticket:1237]
- Test coverage added for `relation()` objects specified on concrete mappers. [ticket:1237]
- A short documentation example added for bidirectional relations specified on concrete mappers. [ticket:1237]
- Mappers now instrument class attributes upon construction with the final InstrumentedAttribute object which remains persistent.  The `_CompileOnAttr`/`__getattribute__()` methodology has been removed.  The net effect is that Column-based mapped class attributes can now be used fully at the class level without invoking a mapper compilation operation, greatly simplifying typical usage patterns within declarative. [ticket:1269] 
- Index now accepts column-oriented InstrumentedAttributes (i.e. column-based mapped class attributes) as column arguments.  [ticket:1214]
- Broke up attributes.register_attribute into two separate functions register_descriptor and register_attribute_impl.    The first assembles an InstrumentedAttribute or Proxy descriptor, the second assembles the AttributeImpl inside the InstrumentedAttribute.  register_attribute remains for outside compatibility.  The argument lists have been simplified.
- Removed class_manager argument from all but MutableScalarAttributeImpl (the branch had removed class_ as well but this has been reverted locally to support the serializer extension).
- Mapper's previous construction of _CompileOnAttr now moves to a new MapperProperty.instrument_class() method which is called on all MapperProperty objects at the moment the mapper receives them. All MapperProperty objects now call attributes.register_descriptor within that method to assemble an InstrumentedAttribute object directly.  
- InstrumentedAttribute now receives the "property" attribute from the given PropComparator.  The guesswork within the constructor is removed, and allows "property" to serve as a mapper compilation trigger.
- RelationProperty.Comparator now triggers compilation of its parent mapper within a util.memoized_property accessor for the "property" attribute, which is used instead of "prop" (we can probably remove "prop").
- ColumnProperty and similar handle most of their initialization in their __init__ method since they must function fully at the class level before mappers are compiled.
- SynonymProperty and ComparableProperty move their class instrumentation logic to the new instrument_class() method.
- LoaderStrategy objects now add their state to existing InstrumentedAttributes using attributes.register_attribute_impl.  Both column and relation-based loaders instrument in the same way now, with a unique InstrumentedAttribute *and* a unique AttributeImpl for each class in the hierarchy.  attribute.parententity should now be correct in all cases.
- Removed unitofwork.register_attribute, and simpified the _register_attribute methods into a single function in strategies.py.  unitofwork exports the UOWEventHandler extension directly.
- To accomodate the multiple AttributeImpls across a class hierarchy, the sethasparent() method now uses an optional "parent_token" attribute to identify the "parent".  AbstractRelationLoader sends the MapperProperty along to serve as this token.  If the token isn't present (which is only the case in the attributes unit tests), the AttributeImpl is used instead, which is essentially the same as the old behavior.
- Added new ConcreteInheritedProperty MapperProperty.  This is invoked for concrete mappers within _adapt_inherited_property() to accomodate concrete mappers which inherit unhandled attributes from the base class, and basically raises an exception upon access.  [ticket:1237]
- attributes.register_attribute and register_descriptor will now re-instrument an attribute unconditionally without checking for a previous attribute.  Not sure if this is controversial. It's needed so that ConcreteInheritedProperty instrumentation can be overridden by an incoming legit MapperProperty without any complexity.
- Added new UninstrumentedColumnLoader LoaderStrategy.  This is used by the polymorphic_on argument when the given column is not represented within the mapped selectable, as is typical with a concrete scenario which maps to a polymorphic union.  It does not configure class instrumentation, keeping polymorphic_on from getting caught up in the new concrete attribute-checking logic.
- RelationProperty now records its "backref" attributes using a set assigned to `_reverse_property` instead of a scalar.  The `back_populates` keyword allows any number of properties to be involved in a single bidirectional relation.  Changes were needed to RelationProperty.merge(), DependencyProcessor to accomodate for the new multiple nature of this attribute.
- Generalized the methodology used by ManyToManyDP to check for "did the other dependency already handle this direction", building on the `_reverse_property` collection.
- post_update logic within dependency.py moves to use the same methodology as ManyToManyDP so that "did the other dependency do this already" checks are made to be specific to the two dependent instances.
- Caught that RelationProperty.merge() was writing to instance.__dict__ directly (!) - repaired to talk to instance_state.dict.
- Removed needless eager loading example from concrete mapper docs.
- Added test for [ticket:965].
- Added the usual Node class/nodes table to orm/_fixtures.py, but haven't used it for anything yet.   We can potentially update test/orm/query.py to use this fixture.
- Other test/documentation cleanup.


""",
u"""
clarified docs on foreign key cascades, mapper extension methods during delete() and update() methods

""",
u"""
query.delete(False) is not so bad

""",
u"""
Added the missing keywords from MySQL 4.1 so they get escaped properly.

""",
u"""
typo

""",
u"""
Formatting fixups
""",
u"""
doh its 0.5.0

""",
u"""
move memusage to the isolation chamber

""",
u"""
- removed 2.3 compat stuff
- updated MANIFEST for the newer build

""",
u"""
next release is 0.5.0

""",
u"""
- query.join() raises an error when the target of the join
doesn't match the property-based attribute - while it's 
unlikely anyone is doing this, the SQLAlchemy author was
guilty of this particular loosey-goosey behavior.


""",
u"""
Forgot to sqash a commit. Follow up on mssql dates refactoring.
""",
u"""
mssql date / time refactor.
- Added new MSSmallDateTime, MSDateTime2, MSDateTimeOffset, MSTime types
- Refactored the Date/Time types. The smalldatetime data type no longer
  truncates to a date only, and will now be mapped to the MSSmallDateTime
  type. Closes #1254.
  """,
u"""
made the "you passed a non-aliased selectable" warning scarier.  scarier !

""",
u"""
- property.of_type() is now recognized on a single-table
inheriting target, when used in the context of 
prop.of_type(..).any()/has(), as well as 
query.join(prop.of_type(...)).


""",
u"""
if at first you don't succeed, fail, fail again

""",
u"""
assume table.schema, not None, when constraint reflection has no explicit schema.  unit test TBD.

""",
u"""
- Generalized the IdentityManagedState._instance_dict() callable
to the IdentityMap class so that Weak/StrongInstanceDict both
have the same behavior wrt the state referencing the map
- Fixed bug when using weak_instance_map=False where modified
events would not be intercepted for a flush(). [ticket:1272]


""",
u"""
Corrected a few docs and didn't realize we put pyodbc first in the search list.
""",
u"""
docstrings for the hated fold_equivalents argument/function

""",
u"""
added teardown_instance() to complement setup_instance().  
Based on the instance/class agnostic behavior of ClassManager, this might be the best we can 
do regarding [ticket:860]

""",
u"""
- query.order_by() accepts None which will remove any pending
order_by state from the query, as well as cancel out any
mapper/relation configured ordering. This is primarily useful 
for overriding the ordering specified on a dynamic_loader().
[ticket:1079]


""",
u"""
added the significant test for #1247

""",
u"""
Corrected an issue on mssql where Numerics would not accept an int.
""",
u"""
added order_by test coverage as per [ticket:1218]

""",
u"""
one more typo

""",
u"""
fixed critical errors in assocationproxy docs while we wait for the all new and improved version

""",
u"""
- Fixed bug which was preventing out params of certain types
from being received; thanks a ton to huddlej at wwu.edu !
[ticket:1265]


""",
u"""
identified the SQLite changes which affect default reflection

""",
u"""
Added a note about mssql compatibility levels.
""",
u"""
send a NASA probe to the buildbot

""",
u"""
Flagged two versioning tests as failing on MSSQL. The flush occurs even though
there should be a concurrency issue.

I cheated and marked these as FIXME. With this commit all MSSQL tests pass
now. The work of correcting the ``fails_on`` tests begins.
""",
u"""
sqlite tests run fine locally but the buildbot seems to have an issue. Perhaps this will work.
""",
u"""
Some of the ordering fixes messed up MySQL. This should work better. Better testing next time.
""",
u"""
Modified DefaultTest in order to get passage on mssql and still test the right stuff.
""",
u"""
Excluded another failing test from the mssql dialect.

MSSQL doesn't allow ON UPDATE for self-referential keys. The tree of cascading
referential actions must only have one path to a particular table on the
cascading referential actions tree.
""",
u"""
- Fixed some deep "column correspondence" issues which could
impact a Query made against a selectable containing
multiple versions of the same table, as well as 
unions and similar which contained the same table columns
in different column positions at different levels.
[ticket:1268]


""",
u"""
A couple of ordering fixes for the tests.
""",
u"""
sqlite reflection now stores the actual DefaultClause value for the column.
""",
u"""
- mysql, postgres: "%" signs in text() constructs are automatically escaped to "%%".
Because of the backwards incompatible nature of this change, 
a warning is emitted if '%%' is detected in the string.  [ticket:1267]


""",
u"""
Swap out text_as_varchar on the mssql dialect for the Types tests.
""",
u"""
Marked a couple of unicode schema tests as failing on mssql.
""",
u"""
found some more _Function->Function

""",
u"""
- sqlalchemy.sql.expression.Function is now a public
class.  It can be subclassed to provide user-defined
SQL functions in an imperative style, including
with pre-established behaviors.  The postgis.py
example illustrates one usage of this.


""",
u"""
Marked mssql test as failing since it cannot update identity columns.
""",
u"""
Mapped char_length to the LEN() function for mssql.
""",
u"""
Corrected a UOW DefaultTest for mssql because it requires the identity column setup.
""",
u"""
Added ability to use subselects within INSERTS on mssql.
""",
u"""
Specialized trigger tests to accomodate mssql syntax.
""",
u"""
Added note for mssql about using snapshot isolation in order to get multiple
connection session tests to pass.
""",
u"""
Turned off the implicit transaction behavior of MSSQL.

This corrects the savepoint tests.
""",
u"""
- Custom comparator classes used in conjunction with 
column_property(), relation() etc. can define 
new comparison methods on the Comparator, which will
become available via __getattr__() on the 
InstrumentedAttribute.   In the case of synonym()
or comparable_property(), attributes are resolved first
on the user-defined descriptor, then on the user-defined
comparator.


""",
u"""
Modified UOW so that a Row Switch scenario will not attempt to update the Primary Key.
""",
u"""
Cleanup of r5556. Makes the description_encoding less public since this is a
workaround for the pyodbc dbapi.
""",
u"""
emacs
""",
u"""
yes ive been watching the IRC channel.  restored setup_instance() to ClassManager and added coverage for mapper's usage of it.


""",
u"""
- added an extremely basic illustration of a PostGIS
integration to the examples folder.


""",
u"""
Modifications to the mssql dialect in order to to pass through unicode in the pyodbc dialect.
""",
u"""
Added a new description_encoding attribute on the dialect.

This is used for encoding the column name when processing the metadata. This
usually defaults to utf-8.
""",
u"""
A few 2.3 cleanup items.
""",
u"""
Added in MSGenericBinary to the mssql dialect tests.
""",
u"""
- added another usage recipe for contains_eager()
- some typos

""",
u"""
  - Added OracleNVarchar type, produces NVARCHAR2, and also
      subclasses Unicode so that convert_unicode=True by default.
      NVARCHAR2 reflects into this type automatically so
      these columns pass unicode on a reflected table with no explicit
      convert_unicode=True flags.  [ticket:1233]


      """,
    u"""
- Can pass mapped attributes and column objects as keys
to query.update({}).  [ticket:1262]

- Mapped attributes passed to the values() of an 
expression level insert() or update() will use the 
keys of the mapped columns, not that of the mapped 
attribute.


""",
u"""
Added in a new MSGenericBinary type.

This maps to the Binary type so it can implement the specialized behavior of
treating length specified types as fixed-width Binary types and non-length
types as an unbound variable length Binary type.
""",
u"""
- RowProxy objects can be used in place of dictionary arguments 
sent to connection.execute() and friends.  [ticket:935]


""",
u"""
- Fixed shard_id argument on ShardedSession.execute().
[ticket:1072]


""",
u"""
Corrected reflection issue in mssql where include_columns doesn't include the PK.
""",
u"""
On MSSQL if a field is part of the primary_key then it should not allow NULLS.
""",
u"""
MSSQL refactoring of BINARY type and addition of MSVarBinary and MSImage.

- Added in new types: MSVarBinary and MSImage
- Modified MSBinary to now return BINARY instead of IMAGE. This is a
  backwards incompatible change. Closes #1249.
  """,
u"""
- added a full exercising test for all of #946, #947, #948, #949

""",
u"""
- Added a mutex for the initial pool creation when
using pool.manage(dbapi).  This prevents a minor 
case of "dogpile" behavior which would otherwise
occur upon a heavy load startup.  [ticket:799]


""",
u"""
- Added ScopedSession.is_active accessor. [ticket:976]


""",
u"""
- NullPool supports reconnect on failure behavior.
[ticket:1094]


""",
u"""
- Reflected foreign keys will properly locate 
their referenced column, even if the column
was given a "key" attribute different from
the reflected name.  This is achieved via a 
new flag on ForeignKey/ForeignKeyConstraint 
called "link_to_name", if True means the given 
name is the referred-to column's name, not its 
assigned key.
[ticket:650]
- removed column types from sqlite doc, we 
aren't going to list out "implementation" types
since they aren't significant and are less present
in 0.6
- mysql will report on missing reflected foreign
key targets in the same way as other dialects
(we can improve that to be immediate within
reflecttable(), but it should be within
ForeignKeyConstraint()).
- postgres dialect can reflect table with
an include_columns list that doesn't include 
one or more primary key columns


""",
u"""
fix imports for index reflection unit test

""",
u"""
Fixed bugs in sqlalchemy documentation. Closes #1263.
""",
u"""
- Exceptions raised during compile_mappers() are now
preserved to provide "sticky behavior" - if a hasattr()
call on a pre-compiled mapped attribute triggers a failing 
compile and suppresses the exception, subsequent compilation 
is blocked and the exception will be reiterated on the 
next compile() call.  This issue occurs frequently
when using declarative.


""",
u"""
use new anonymize style for the public _anonymize as well

""",
u"""
Added MSSQL support for introspecting the default schema name for the logged in user. Thanks Randall Smith. Fixes #1258.
""",
u"""
silly negative ID numbers on linux...

""",
u"""
- Added Index reflection support to Postgres, using a
great patch we long neglected, submitted by 
Ken Kuhlman. [ticket:714]


""",
u"""
Merge branch 'collation'
""",
u"""
- Columns can again contain percent signs within their
names. [ticket:1256]


""",
u"""
Major refactoring of the MSSQL dialect. Thanks zzzeek.
Includes simplifying the IDENTITY handling and the exception handling. Also
includes a cleanup of the connection string handling for pyodbc to favor
the DSN syntax.
""",
u"""
also check for primaryjoin/secondaryjoin that equates to False, [ticket:1087]

""",
u"""
- CHANGES update
- added slightly more preemptive message for bad remote_side

""",
u"""
- Fixed mysql bug in exception raise when FK columns not present
during reflection. [ticket:1241]


""",
u"""
fix unittest import

""",
u"""
Pulled callable into testlib because path fixup is not available at the point we need it.
""",
u"""
Corrected ColumnsTest for mssql's new explicit nullability behavior.
""",
u"""
removed the "create_execution_context()" method from dialects and replaced
with a more succinct "dialect.execution_ctx_cls" member

""",
u"""
more platform neutral way of getting at 'buffer'

""",
u"""
missed an ordering on a set.   attempting to nail down linux-specific buildbot errors

""",
u"""
and try again

""",
u"""
2.4 doesnt have hashlib....

""",
u"""
*most* py3k warnings are resolved, with the exception of the various __setslice__ related warnings
I don't really know how to get rid of

""",
u"""
merge the test/ directory from -r5438:5439 of py3k_warnings branch.  this gives
us a 2.5-frozen copy of unittest so we're insulated from unittest changes.

""",
u"""
merged -r5299:5438 of py3k warnings branch.  this fixes some sqlite py2.6 testing issues,
and also addresses a significant chunk of py3k deprecations.  It's mainly 
expicit __hash__ methods.  Additionally, most usage of sets/dicts to store columns uses
util-based placeholder names.

""",
u"""
dynamic_loader() accepts query_class= to mix in user Query subclasses.
""",
u"""
Association proxies no longer cloak themselves at the class level.
""",
u"""
- Query() can be passed a "composite" attribute
as a column expression and it will be expanded.
Somewhat related to [ticket:1253].
- Query() is a little more robust when passed
various column expressions such as strings,
clauselists, text() constructs (which may mean
it just raises an error more nicely).
- select() can accept a ClauseList as a column
in the same way as a Table or other selectable
and the interior expressions will be used as
column elements. [ticket:1253]
- removed erroneous FooTest from test/orm/query

-This line, and those below, will be ignored--

M    test/orm/query.py
M    test/orm/mapper.py
M    test/sql/select.py
M    lib/sqlalchemy/orm/query.py
M    lib/sqlalchemy/sql/expression.py
M    CHANGES

""",
u"""
document ConnectionProxy

""",
u"""
- _execute_clauseelement() goes back to being 
a private method.  Subclassing Connection
is not needed now that ConnectionProxy 
is available.
- tightened the interface for the various _execute_XXX()
methods to reduce ambiguity
- __distill_params() no longer creates artificial [{}] entry,
blank dict is no longer passed through to do_execute()
in any case unless explicitly sent from the outside 
as in connection.execute("somestring"), {})
- fixed a few old sql.query tests which were doing that
- removed needless do_execute() from mysql dialect
- fixed charset param not properly being sent to 
_compat_fetchone() in mysql


""",
u"""
- sqlite types
- fixed targeting for sqlalchemy.types

""",
u"""
- Fixed bug where many-to-many relation() with
viewonly=True would not correctly reference the
link between secondary->remote.


""",
u"""
- added sphinx handler to allow __init__ methods through
- sqlite module documentation
- some corrections to pool docs
- the example in URL.translate_connect_args() never made any sense anyway so removed it

""",
u"""
polymorphic_fetch is deprecated. Mark it so in the documentation.

""",
u"""
ok we need find_packages.  fine.

""",
u"""
corrections

""",
u"""
removed dependencies on setuptools.  distutils will be used if setuptools is not 
present.

""",
u"""
Corrected output on docs and a missing {stop} that prevented python results from displaying in the docs.
""",
u"""
Support for three levels of column nullability: NULL, NOT NULL, and the database's configured default.

The default Column configuration (nullable=True) will now generate NULL in the DDL. Previously no specification was emitted and the database default would take effect (usually NULL, but not always).  To explicitly request the database default, configure columns with nullable=None and no specification will be emitted in DDL. Fixes #1243.
""",
u"""
Modified fails_on testing decorator to take a reason for the failure.

This should assist with helping to document the reasons for testing failures.
Currently unspecified failures are defaulted to 'FIXME: unknown'.
""",
u"""
Corrected and verified a few more mssql tests.
""",
u"""
Broke out a specific values test and indicated that it fails on mssql due to duplicate columns in the order by clause.
""",
u"""
- turn __visit_name__ into an explicit member.
[ticket:1244]

""",
u"""
Index entries for thread safety.
""",
u"""
And now for the CHANGES.
""",
u"""
Corrected problem with bindparams not working properly with Query.delete and Query.update. Thanks zzzeek. Fixes #1242.
""",
u"""
We don't need two of these.
""",
u"""
Access doesn't support savepoints or two-phase commit.
""",
u"""
Implemented experimental savepoint support in mssql. There are still some failing savepoint related tests.
""",
u"""
fix circular import

""",
u"""
- Connection.invalidate() checks for closed status 
to avoid attribute errors. [ticket:1246]


""",
u"""
- PickleType now favors == comparison by default,
if the incoming object (such as a dict) implements
__eq__().  If the object does not implement 
__eq__() and mutable=True, a deprecation warning
is raised.


""",
u"""
- fixed string-based "remote_side", "order_by" and 
others not propagating correctly when used in 
backref().


""",
u"""
- VERSION moves just as a string in __version__
- added modified sphinx.sty with plain Verbatim section
- link to pdf doc in site

""",
u"""
- first() works as expected with Query.from_statement().


""",
u"""
- reworked the "SQL assertion" code to something more flexible and based off of ConnectionProxy.  upcoming changes to dependency.py
will make use of the enhanced flexibility.

""",
u"""
dont use names to find Annotated subclasses

""",
u"""
- restored the previous API Reference structure
- bumped latex TOC structure, the PDF looks great
- but we need to fix the translate_connect_args docstring bug to really have PDF

""",
u"""
fix typos

""",
u"""
- removed redundant declarative docs
- cleanup of metadata/foreignkey docs

""",
u"""
further fix that docstring


""",
u"""
fixed invalid docstring example

""",
u"""
- restored the main search form
- fixed search highlighting
- the url docstring works again from a ReST perspective, still not PDF

""",
u"""
- moved index.rst around to have the API docs right there, no "Main Documentation" chapter which is fairly needless.  this all allows PDF to have a decent TOC on the side with only two levels (can we change that ?)
- added LatexFormatter.
- PDF wont work until issue with the docstirng in url.py/URL.translate_connect_args is fixed.

""",
u"""
worked schema into sections

""",
u"""
- convert __init__ and :members: to be compatible with autoclass_content='both'

""",
u"""
fix typos


""",
u"""
documented onupdate, partially documented server_onupdate

""",
u"""
- re-documented Table and Column constructors, fixed case sensitivity description [ticket:1231]
- turned on autoclass_content="both".  Need to specify __init__ docstring with
  a newline after the.
- other docs

""",
u"""
Adjusted basis for refs.
""",
u"""
- removed creepy exec call for now
- removed unnecessary isinstance() from class_mapper()
- removed unnecessary and py3k incompatible "dictionary sort" from association table delete

""",
u"""
need to use absolutes for these, otherwise its dictionary ordering roulette

""",
u"""
- postgres docstring
- insert/update/delete are documented generatively
- values({}) is no longer deprecated, thus enabling
unicode/Columns as keys

""",
u"""
Enabled sphinx doctests.
""",
u"""
remove old files

""",
u"""
- merged -r5338:5429 of sphinx branch.
- Documentation has been converted to Sphinx.
In particular, the generated API documentation
has been constructed into a full blown 
"API Reference" section which organizes 
editorial documentation combined with 
generated docstrings.   Cross linking between
sections and API docs are vastly improved,
a javascript-powered search feature is
provided, and a full index of all
classes, functions and members is provided.


""",
u"""
- union() and union_all() will not whack 
any order_by() that has been applied to the 
select()s inside.  If you union() a 
select() with order_by() (presumably to support
LIMIT/OFFSET), you should also call self_group() 
on it to apply parenthesis.


""",
u"""
- Adjusted the format of create_xid() to repair
two-phase commit.   We now have field reports
of Oracle two-phase commit working properly
with this change.


""",
u"""
- Query.with_polymorphic() now accepts a third
argument "discriminator" which will replace
the value of mapper.polymorphic_on for that
query.  Mappers themselves no longer require
polymorphic_on to be set, even if the mapper
has a polymorphic_identity.   When not set,
the mapper will load non-polymorphically 
by default. Together, these two features allow 
a non-polymorphic concrete inheritance setup 
to use polymorphic loading on a per-query basis,
since concrete setups are prone to many
issues when used polymorphically in all cases.


""",
u"""
- Two fixes to help prevent out-of-band columns from
being rendered in polymorphic_union inheritance
scenarios (which then causes extra tables to be
rendered in the FROM clause causing cartesian 
products): 
- improvements to "column adaption" for
  a->b->c inheritance situations to better
  locate columns that are related to one
  another via multiple levels of indirection,
  rather than rendering the non-adapted
  column.
- the "polymorphic discriminator" column is
  only rendered for the actual mapper being
  queried against. The column won't be
  "pulled in" from a subclass or superclass
  mapper since it's not needed.


    """,
u"""
- Using the same ForeignKey object repeatedly
raises an error instead of silently failing
later. [ticket:1238]


""",
u"""
- Fixed bug introduced in 0.5rc4 involving eager 
loading not functioning for properties which were
added to a mapper post-compile using 
add_property() or equivalent.


""",
u"""
Modified the docstring for Session.add() with lots of help.
""",
u"""
made Session.merge cascades not trigger autoflush

""",
u"""
- Improved mapper() check for non-class classes.
[ticket:1236]


""",
u"""
propagate docstrings for column/fk collections

""",
u"""
- fixed "double iter()" call causing bus errors
in shard API, removed errant result.close()
left over from the 0.4 version. [ticket:1099]
[ticket:1228]


""",
u"""
Refactored the entity setup code in Query so that it is not duplicated in several places.
""",
u"""
A few more order_by statements added to the tests in order to please msql when using offsets.
""",
u"""
- Duplicate items in a list-based collection will
be maintained when issuing INSERTs to
a "secondary" table in a many-to-many relation.
Assuming the m2m table has a unique or primary key 
constraint on it, this will raise the expected 
constraint violation instead of silently
dropping the duplicate entries. Note that the 
old behavior remains for a one-to-many relation
since collection entries in that case
don't result in INSERT statements and SQLA doesn't
manually police collections. [ticket:1232]


""",
u"""
deprecated CompositeProperty 'comparator' which is now
named 'comparator_factory'.

""",
u"""
one more select_table...

""",
u"""
- comparator_factory is accepted by all MapperProperty constructors. [ticket:1149]
- added other unit tests as per [ticket:1149]
- rewrote most of the "joined table inheritance" documentation section, removed badly out of
date "polymorphic_fetch" and "select_table" arguments.
- "select_table" raises a deprecation warning.  converted unit tests to not use it.
- removed all references to "ORDER BY table.oid" from mapping docs.
- renamed PropertyLoader to RelationProperty.  Old symbol remains.
- renamed ColumnProperty.ColumnComparator to ColumnProperty.Comparator.  Old symbol remains.


""",
u"""
- Extra checks added to ensure explicit 
primaryjoin/secondaryjoin are ClauseElement 
instances, to prevent more confusing errors later 
on.


""",
u"""
- Tickets [ticket:1200].

- Added note about create_session() defaults.

- Added section about metadata.reflect().

- Updated `TypeDecorator` section.

- Rewrote the "threadlocal" strategy section of 
the docs due to recent confusion over this 
feature.

- ordered the init arguments in the docs for sessionmaker().

- other edits

""",
u"""
prevent extra nested li items from becoming tiny

""",
u"""
- Fixed the import weirdness in sqlalchemy.sql
to not export __names__ [ticket:1215].


""",
u"""
- Comparison of many-to-one relation to NULL is
properly converted to IS NOT NULL based on not_().


""",
u"""
- Added NotImplementedError for params() method
on Insert/Update/Delete constructs.  These items
currently don't support this functionality, which
also would be a little misleading compared to
values().


""",
u"""
- the "passive" flag on session.is_modified()
is correctly propagated to the attribute manager.


""",
u"""
r5281 knocked down callcounts in 2.5..

""",
u"""
- Query.select_from(), from_statement() ensure
that the given argument is a FromClause,
or Text/Select/Union, respectively.

- Query.add_column() can accept FromClause objects
in the same manner as session.query() can.


""",
u"""
- bump, this may become 0.5.0
- Calling alias.execute() in conjunction with
server_side_cursors won't raise AttributeError.


""",
u"""
notes on tuning


""",
u"""
- switched session.save() to session.add() throughout declarative test
- Fixed PendingDeprecationWarning involving order_by
parameter on relation(). [ticket:1226]
- Unit tests still filter pending deprecation warnings but have a commented-out
line to temporarily disable this behavior.  Tests need to be fully converted
before we can turn this on.

""",
u"""
Pulled out values test that uses boolean evaluation in the SELECT in order to appropriately flag it as not supported on mssql. I sure hope I didn't jack things up for other dialects. Cleaned up a comment and removed some commented pdb statements.
""",
u"""
Fixed a problem with the casting of a zero length type to a varchar. It now correctly adjusts the CAST accordingly.
""",
u"""
Fixed up a lot of missing order_by statements in the tests when using offset. A lot of dialects don't really require order_by although you'll get unpredictable results. mssql does require order_by with an offset, so this fixes problems with that dialect.
""",
u"""
The str(query) output is also correct on the mssql dialect.
""",
u"""
- Rearranged the `load_dialect_impl()` method in 
`TypeDecorator` such that it will take effect
even if the user-defined `TypeDecorator` uses
another `TypeDecorator` as its impl.


""",
u"""
- Can now use a custom "inherit_condition" in 
__mapper_args__ when using declarative.


""",
u"""
Corrected mssql schema named subqueries from not properly aliasing the columns. Fixes #973.
""",
u"""
Doing my part-time editorial duties. Normalized session references and fixed lots of small spelling and grammar issues.
""",
u"""
remove errant pdb.set_trace()

    """,
u"""
- Adjustments to the enhanced garbage collection on 
InstanceState to better guard against errors due 
to lost state.


""",
u"""
Quashed import sets deprecation warning on 2.6.. not wild about this but it seems like it will be ok. [ticket:1209]
""",
u"""
- converted some more attributes to @memoized_property in expressions
- flattened an unnecessary KeyError in identity.py
- memoized the default list of mapper properties queried in MapperEntity.setup_context

""",
u"""
- Restored "active rowcount" fetch before ResultProxy
autocloses the cursor.  This was removed in 0.5rc3.


""",
u"""
- Restored NotImplementedError on Cls.relation.in_()
[ticket:1140] [ticket:1221]


""",
u"""
Handle the mssql port properly. If we're using the SQL Server driver then use the correct host,port syntax, otherwise use the Port= parameter in the connection string. Fixes #1192.
""",
u"""
Flagged another transaction test as causing mssql to hang. Need to look into these.
""",
u"""
Corrected issue with decimal e notation that broke regular decimal tests for mssql.
""",
u"""
If there's a zero offset with mssql just ignore it.
""",
u"""
Corrected problem in access dialect that was still referring to the old column.foreign_key property.
""",
u"""
flattened _get_from_objects() into a descriptor/class-bound attribute

""",
u"""
- Removed the 'properties' attribute of the 
Connection object, Connection.info should be used.
- Method consoliation in Connection, ExecutionContext

""",
u"""
- Query.count() has been enhanced to do the "right
thing" in a wider variety of cases. It can now
count multiple-entity queries, as well as
column-based queries. Note that this means if you
say query(A, B).count() without any joining
criterion, it's going to count the cartesian
product of A*B. Any query which is against
column-based entities will automatically issue
"SELECT count(1) FROM (SELECT...)" so that the
real rowcount is returned, meaning a query such as
query(func.count(A.name)).count() will return a value of
one, since that query would return one row.


""",
u"""
Corrected problems with Access dialect. Corrected issue with reflection due to missing Currency type. Functions didn't return the value. JOINS must be specified as LEFT OUTER JOIN or INNER JOIN. Fixes #1017.
""",
u"""
Global propigate -> propagate change to correct spelling. Additionally found a couple of insures that should be ensure.
""",
u"""
Corrected problems with reflection on mssql when dealing with schemas. Fixes #1217.
""",
u"""
usage docstring for pool listener

""",
u"""
- Query.count() and Query.get() return a more informative
error message when executed against multiple entities.
[ticket:1220]


""",
u"""
removed setup_instance() from the public API
of ClassManager, and made it a private method on 
_ClassInstrumentationAdapter.  ClassManager's approach 
handles the default task with fewer function calls which chops off
a few hundred calls from the pertinent profile tests.

""",
u"""
Fixed E notation problem in mssql. Closes #1216.
""",
u"""
Corrected a lot of mssql limit / offset issues. Also ensured that mssql uses the IN / NOT IN syntax when using a binary expression with a subquery.
""",
u"""
docstring updates

""",
u"""
docstring fix

""",
u"""
- added serializer docs to plugins.txt
- CHANGES formatting

""",
u"""
- Fixed bug preventing declarative-bound "column" objects 
from being used in column_mapped_collection().  [ticket:1174]


""",
u"""
formatting

""",
u"""
- zoomark adjustments
- changelog has separate category for 'features'

""",
u"""
avoid some often unnecessary method calls.   i think we might have squeezed all we're going to squeeze out of compiler at this point.

""",
u"""
the @memoized_property fairy pays a visit

""",
u"""
- Repaired the table.tometadata() method so that a passed-in
schema argument is propigated to ForeignKey constructs.


""",
u"""
- Fixed bug in Query involving order_by() in conjunction with 
multiple aliases of the same class (will add tests in 
[ticket:1218])
- Added a new extension sqlalchemy.ext.serializer.  Provides
Serializer/Deserializer "classes" which mirror Pickle/Unpickle,
as well as dumps() and loads().  This serializer implements
an "external object" pickler which keeps key context-sensitive
objects, including engines, sessions, metadata, Tables/Columns,
and mappers, outside of the pickle stream, and can later 
restore the pickle using any engine/metadata/session provider.   
This is used not for pickling regular object instances, which are 
pickleable without any special logic, but for pickling expression
objects and full Query objects, such that all mapper/engine/session
dependencies can be restored at unpickle time.


""",
u"""
add two new hooks for bulk operations to SessionExtension:

* after_bulk_delete

* after_bulk_update


""",
u"""
- Fixed bug in composite types which prevented a primary-key
composite type from being mutated [ticket:1213].


""",
u"""
- Dialects can now generate label names of adjustable length.
Pass in the argument "label_length=<value>" to create_engine()
to adjust how many characters max will be present in dynamically
generated column labels, i.e. "somecolumn AS somelabel".  Any 
value less than 6 will result in a label of minimal size,
consiting of an underscore and a numeric counter.
The compiler uses the value of dialect.max_identifier_length
as a default. [ticket:1211]
- removed ANON_NAME regular expression, using string patterns now
- _generated_label() unicode subclass is used to indicate generated names 
which are subject to truncation

""",
u"""
Tiny fix to test setup logic.
""",
u"""
- Simplified the check for ResultProxy "autoclose without results"
to be based solely on presence of cursor.description.   
All the regexp-based guessing about statements returning rows 
has been removed [ticket:1212].


""",
u"""
- added 'EXPLAIN' to the list of 'returns rows', but this 
issue will be addressed more fully by [ticket:1212].

""",
u"""
Added a label for pg.
""",
u"""
- Fixed bug when using multiple query.join() with an aliased-bound
descriptor which would lose the left alias.


""",
u"""
- Improved the behavior of aliased() objects such that they more
accurately adapt the expressions generated, which helps 
particularly with self-referential comparisons. [ticket:1171]

- Fixed bug involving primaryjoin/secondaryjoin conditions
constructed from class-bound attributes (as often occurs 
when using declarative), which later would be inappropriately 
aliased by Query, particularly with the various EXISTS
based comparators.


""",
u"""
update call count

""",
u"""
Added tests for Query.scalar(), .value() [ticket:1163]
""",
u"""
Fixed assoc proxy examples [ticket:1191]
""",
u"""
revert r5220 inadvertently committed to trunk

""",
u"""
progress so far

""",
u"""
Corrected some ordering issues with tests.
""",
u"""
- mapper naming/organization cleanup
- gave into peer pressure and removed all __names
- inlined polymorphic_iterator()
- moved methods into categories based on configuration, inspection, persistence, row processing.
a more extreme change would be to make separate mixin classes for these or similar.

""",
u"""
pep8 stuff

""",
u"""
- util.flatten_iterator() func doesn't interpret strings with
__iter__() methods as iterators, such as in pypy [ticket:1077].


""",
u"""
the recent change to garbage collection of InstanceState meant that
the deferred lambda: created by lazy_clause would get a state with
no dict.  creates strong reference to the object now.

""",
u"""
Added documentation for the MetaData.sorted_tables() method.
""",
u"""
Corrected method documentation for MetaData.drop_all().
""",
u"""
allow repr to leave stuff as unicode.  I can't think of any reason for the old behavior except that I didn't understand unicode when I wrote it.  Not that I claim to fully understand it now.  fixes #1136
""",
u"""
Accept USING as a prefix or postfix modifer when reflecting keys.  [ticket:1117]
""",
u"""
Corrects an import error when using echo_uow. Fixes #1205.
""",
u"""
fix #821
""",
u"""
- added some abstraction to the attributes.History object
- Repaired support for "passive-deletes" on a many-to-one
relation() with "delete" cascade. [ticket:1183]


""",
u"""
Updated UOWEventHandler so that it uses session.add() instead of session.save_or_update(). Fixes #1208.
""",
u"""
Corrected typo in Types docs.
""",
u"""
Mysql no longer expects include_columns to be specified in lowercase. Fixes #1206.
""",
u"""
Fixed mysql FK reflection for the edge case where a Table has expicitly provided a schema= that matches the connection's default schema.

""",
u"""
r/m wildcard imports.  fixes #1195
""",
u"""
- InstanceState object now removes circular references to 
itself upon disposal to keep it outside of cyclic garbage
collection.


""",
u"""
- moved _FigureVisitName into visitiors.VisitorType, added Visitor base class to reduce dependencies
- implemented _generative decorator for select/update/insert/delete constructs
- other minutiae

""",
u"""
call drop # 2

""",
u"""
call drop

""",
u"""
- When using Query.join() with an explicit clause for the 
ON clause, the clause will be aliased in terms of the left
side of the join, allowing scenarios like query(Source).
from_self().join((Dest, Source.id==Dest.source_id)) to work
properly.


""",
u"""
small fix

""",
u"""
a couple of refinements

""",
u"""
remove erroneous comments

""",
u"""
two more cache examples

""",
u"""
auto_convert_lobs=False honored by OracleBinary, OracleText types
[ticket:1178]

""",
u"""
- fixed some oracle unit tests in test/sql/
- wrote a docstring for oracle dialect, needs formatting perhaps
- made FIRST_ROWS optimization optional based on optimize_limits=True, [ticket:536]

""",
u"""
2.4 callcounts of course go up for no apparent reason

""",
u"""
- CompileTests run without the DBAPI being used
- added stack logic back to visit_compound(), pared down is_subquery

""",
u"""
call count pinata party

""",
u"""
Demonstrate mssql url examples for the database engine documentation. Closes #1198.
""",
u"""
Included documentation about the defaults for create_session() and how they differ from sessionmaker(). Closes #1197.
""",
u"""
Corrected case in mssql where binary expression has bind parameters on both sides.
""",
u"""
- Added more granularity to internal attribute access, such 
that cascade and flush operations will not initialize
unloaded attributes and collections, leaving them intact for
a lazy-load later on.  Backref events still initialize 
attrbutes and collections for pending instances.
[ticket:1202]


""",
u"""
add lengths to cols

""",
u"""
- polymorphic_union() function respects the "key" of each 
Column if they differ from the column's name.


""",
u"""
- added NoReferencedColumnError, common base class of NoReferenceError
- relation() won't hide unrelated ForeignKey errors inside of
the "please specify primaryjoin" message when determining
join condition.


""",
u"""
Corrected missing declaration in the mssql dialect test.
""",
u"""
Corrected the is_subquery() check based on recent changes. Excluded the test_in_filtering_advanced test for mssql.
""",
u"""
Slightly changed behavior of IN operator for comparing to empty collections. Now results in inequality comparison against self. More portable, but breaks with stored procedures that aren't pure functions.

""",
u"""
Corrected profiling expected call count down to 42 for the test_insert test.
""",
u"""
Modifications to allow the backends to control the behavior of an empty insert.  If supports_empty_insert is True then the backend specifically supports the 'insert into t1 () values ()' syntax.  If supports_default_values is True then the backend supports the 'insert into t1 default values' syntax.  If both are false then the backend has no support for empty inserts at all and an exception gets raised. Changes here are careful to not change current behavior except where the current behavior was failing to begin with.
""",
u"""
- Improved weakref identity map memory management to no longer 
require mutexing, resurrects garbage collected instance
on a lazy basis for an InstanceState with pending changes.


""",
u"""
Verified that Subqueries are not allowed in VALUES. mssql supports a SELECT syntax but only as the source of all inserts.
(cherry picked from commit 4516db6b322fb1feaa04915f09b8b4fabd6b9735)
    """,
u"""
Cleaned up the create_connect_args so that it makes no expectations about keys. Fixes 1193. Added server version info into mssql pyodbc dialect.
""",
u"""
tiny tiny speed improvements....

""",
u"""
call count still goes to 131 for 2.4 despite the removal of ~12 lines from visit_select()

    """,
u"""
- 0.5.0rc3, doh
- The internal notion of an "OID" or "ROWID" column has been
removed.  It's basically not used by any dialect, and the
possibility of its usage with psycopg2's cursor.lastrowid
is basically gone now that INSERT..RETURNING is available.

- Removed "default_order_by()" method on all FromClause
objects.
- profile/compile/select test is 8 function calls over on buildbot 2.4 for some reason, will adjust after checking
the results of this commit

""",
u"""
oracle doesnt seem to like CLOB in unions....

""",
u"""
- "not equals" comparisons of simple many-to-one relation
to an instance will not drop into an EXISTS clause
and will compare foreign key columns instead.

- removed not-really-working use cases of comparing 
a collection to an iterable.  Use contains() to test
for collection membership.

- Further simplified SELECT compilation and its relationship
to result row processing.

- Direct execution of a union() construct will properly set up
result-row processing. [ticket:1194]


""",
u"""
Moved r5164's @lazy_property to @memoized_property, updated existing @memoize consumers.
""",
u"""
Cache polymorphic_iterator in UOWTask; substantial savings for polymorphism-heavy workloads.
""",
u"""
Unless I'm missing something mssql doesn't support and / or within column selects. Even using the case when syntax it's not possible to test truth in this manner.
""",
u"""
- String's (and Unicode's, UnicodeText's, etc.) convert_unicode 
logic disabled in the sqlite dialect, to adjust for pysqlite 
2.5.0's new requirement that only Python unicode objects are 
accepted;
http://itsystementwicklung.de/pipermail/list-pysqlite/2008-March/000018.html


""",
u"""
reduce cruft related to serializable loaders

""",
u"""
a much easier way to ArgSingleton

""",
u"""
Removed the visit_function stuff in mssql dialect. Added some tests for the function overrides. Fixed up the test_select in the sql/defaults.py tests which was a mess.
""",
u"""
Correction of mssql schema reflection in reflectable. Still a problem since the assumed default is dbo, whereas it could be modified by the connection.  Allows SchemaTest.test_select to pass now.
""",
u"""
indicated that test_empty_insert fails on mssql since pyodbc returns a -1 always for the result.rowcount.
""",
u"""
Corrected docstring for Query.one. Fixes #1190.
""",
u"""
- Oracle will detect string-based statements which contain
      comments at the front before a SELECT as SELECT statements.
      [ticket:1187]


      """,
    u"""
Added in sqlite3 DBAPI to the SQLite dbengine docs. This along with a wiki edit on Database Features should close #1145.
""",
u"""
Documented synonym_for and comparable_using in the main docstring for declarative. Fixes #1144.
""",
u"""
Corrected docs for declarative synonym incorrectly referring to instruments instead of descriptor.
""",
u"""
fixed test for #1175

""",
u"""
- fix outerjoin, add order_by for DB variance

""",
u"""
Change in #1165 tests to prevent MySQL from choking on a varchar without a length.
""",
u"""
Corrects issue where engine.execute raised exception when given empty list. Fixes #1175.
""",
u"""
- using contains_eager() against an alias combined with an overall query alias repaired - the
contains_eager adapter wraps the query adapter, not vice versa.  Test coverage added.
- contains_eager() will now add columns into the "primary" column collection within Query._compile_context(), instead
of the "secondary" collection.  This allows those columns to get wrapped within the subquery generated
by limit/offset in conjunction with an ORM-generated eager join.  
Eager strategy also picks up on context.adapter in this case to deliver the columns during result load. 
contains_eager() is now compatible with the subquery generated by a regular eager load
with limit/offset. [ticket:1180]


""",
u"""
- added a few more assertions for [ticket:1165]
- removed non-2.5 partial.keywords, partial.name, etc., not sure what those are getting us here

""",
u"""
Didnt think about <2.5. When will I learn.
""",
u"""
Allowed column types to be callables. Fixes #1165.
""",
u"""
- Adjustment to Session's post-flush accounting of newly
"clean" objects to better protect against operating on
objects as they're asynchronously gc'ed. [ticket:1182]


""",
u"""
- identity_map._mutable_attrs is a plain dict since we manage weakref removal explicitly
- call list() around iteration of _mutable_attrs to guard against async gc.collect() while check_modified() is running

""",
u"""
the @property / __slots__ fairy pays a visit

""",
u"""
Issue a better error message when someone decides to meddle with the active transaction from within a context manager.

""",
u"""
Fixed session.transaction.commit() on a autocommit=False session not starting a new transaction.
Moved starting a new transaction in case of previous closing into SessionTransaction.

""",
u"""
- session.execute() will execute a Sequence object passed to
  it (regression from 0.4).
- Removed the "raiseerror" keyword argument from object_mapper()
  and class_mapper().  These functions raise in all cases
  if the given class/instance is not mapped.
- Refined ExtensionCarrier to be itself a dict, removed 
'methods' accessor
- moved identity_key tests to test/orm/utils.py
- some docstrings

""",
u"""
- Fixed up slices on Query (i.e. query[x:y]) to work properly
for zero length slices, slices with None on either end.
[ticket:1177]


""",
u"""
Tidy.
""",
u"""
fixed custom TypeEngine example

""",
u"""
Fixed mysql TEMPORARY table reflection.
""",
u"""
- Fixed shared state bug interfering with ScopedSession.mapper's
  ability to apply default __init__ implementations on object
  subclasses.


  """,
u"""
re-enabled memusage and connect tests.
""",
u"""
Added query_cls= override to scoped_session's query_property

""",
u"""
- fixed RLock-related bug in mapper which could deadlock
upon reentrant mapper compile() calls, something that
occurs when using declarative constructs inside of
ForeignKey objects.


""",
u"""
random cleanup

""",
u"""
genericized the relationship between bind_processor() and _bind_processor() a little more

""",
u"""
- Overhauled SQLite date/time bind/result processing
to use regular expressions and format strings, rather
than strptime/strftime, to generically support
pre-1900 dates, dates with microseconds.  [ticket:968]


""",
u"""
the wisdom of SQLite accepting strings for columns with the INT type....priceless

""",
u"""
fix up element sorting in declarative

""",
u"""
Get a bit more speed into the new _sort_states function. It's probably possible
to get even more speed by getting rid of the decorator and call the method
directly, but it makes for slightly less readable code so I won't do it since I
don't know whether this code is speed-critical or not.


""",
u"""
- Fixed bug involving read/write relation()s that 
contain literal or other non-column expressions 
within their primaryjoin condition equated
to a foreign key column.
- fixed UnmappedColumnError exception raise to not assume it was passed a column

""",
u"""
un-stupified insert/update/delete sorting

""",
u"""
more failing cases

""",
u"""
"nested sets" example.  needs work.

""",
u"""
- "non-batch" mode in mapper(), a feature which allows
mapper extension methods to be called as each instance
is updated/inserted, now honors the insert order
of the objects given. 
- added some tests, some commented out, involving [ticket:1171]

""",
u"""
- version bump
- turned properties in sql/expressions.py to @property
- column.in_(someselect) can now be used as 
a columns-clause expression without the subquery
bleeding into the FROM clause [ticket:1074]


""",
u"""
added gc.collect() for pypy/jython compat, [ticket:1076]

""",
u"""
- annual unitofwork cleanup
- moved conversion of cyclical sort to UOWTask structure to be non-recursive
- reduced some verbosity
- rationale for the "tree" sort clarified
- would love to flatten all of uow topological sorting, sorting within mapper._save_obj() into a single sort someday

""",
u"""
- 0.5.0rc1
- removed unneeded grouping from BooleanClauseList, generated needless parens

""",
u"""
- Added scalar() and value() methods to Query, each return a
single scalar value.  scalar() takes no arguments and is
roughly equivalent to first()[0], value()
takes a single column expression and is roughly equivalent to
values(expr).next()[0].


""",
u"""
Note to self: save buffers before committing.
""",
u"""
Added Query.scalar() sugar method, eases migration from old query.sum() methods.  Needs tests.
""",
u"""
- the function func.utc_timestamp() compiles to UTC_TIMESTAMP, without
the parenthesis, which seem to get in the way when using in 
conjunction with executemany().


""",
u"""
return type of exists() is boolean, duh

""",
u"""
- Bind params now subclass ColumnElement which allows them to be
selectable by orm.query (they already had most ColumnElement
semantics).

- Added select_from() method to exists() construct, which becomes
more and more compatible with a regular select().

- Bind parameters/literals given a True/False value will detect
their type as Boolean


""",
u"""
Fix bug with MSSQL reflecting and schemas
""",
u"""
- The exists() construct won't "export" its contained list 
of elements as FROM clauses, allowing them to be used more
effectively in the columns clause of a SELECT.

- and_() and or_() now generate a ColumnElement, allowing
boolean expressions as result columns, i.e.
select([and_(1, 0)]).  [ticket:798]



""",
u"""
reverted inheritance tweak which fails tests on non-sqlite

""",
u"""
- Added func.min(), func.max(), func.sum() as "generic functions",
which basically allows for their return type to be determined
automatically.  Helps with dates on SQLite, decimal types, 
others. [ticket:1160]

- added decimal.Decimal as an "auto-detect" type; bind parameters
and generic functions will set their type to Numeric when a 
Decimal is used.


""",
u"""
- Removed conflicting `contains()` operator from 
`InstrumentedAttribute` which didn't accept `escape` kwaarg
[ticket:1153].


""",
u"""
- Dropped 0.3-compatibility for user defined types
(convert_result_value, convert_bind_param).


""",
u"""
- query.order_by().get() silently drops the "ORDER BY" from 
the query issued by GET but does not raise an exception.


""",
u"""
- rearranged delete() so that the object is attached before
cascades fire off [ticket:5058]
- after_attach() only fires if the object was not previously attached

""",
u"""
synchronize inherited does not need to be called for the full mapper hierarchy

""",
u"""
- Fixed exception throw which would occur when string-based
primaryjoin condition was used in conjunction with backref.


""",
u"""
allow the no_criterion call in _get() to copy the method name thorugh

""",
u"""
- Fixed bug whereby mapper couldn't initialize if a composite
primary key referenced another table that was not defined
yet [ticket:1161]


""",
u"""
 added BFILE to reflected type names [ticket:1121]


 """,
u"""
correct extra space in SQL assertions

""",
u"""
 - has_sequence() now takes the current "schema" argument into
      account [ticket:1155]


      """,
    u"""
 - limit/offset no longer uses ROW NUMBER OVER to limit rows,
      and instead uses subqueries in conjunction with a special
      Oracle optimization comment.  Allows LIMIT/OFFSET to work
      in conjunction with DISTINCT. [ticket:536]


      """,
    u"""
Make Query.update and Query.delete return the amount of rows matched

""",
u"""
correction

""",
u"""
- column_property(), composite_property(), and relation() now 
accept a single or list of AttributeExtensions using the 
"extension" keyword argument.
- Added a Validator AttributeExtension, as well as a 
@validates decorator which is used in a similar fashion
as @reconstructor, and marks a method as validating
one or more mapped attributes.
- removed validate_attributes example, the new methodology replaces it

""",
u"""
- AttributeListener has been refined such that the event
is fired before the mutation actually occurs.  Addtionally,
the append() and set() methods must now return the given value,
which is used as the value to be used in the mutation operation.
This allows creation of validating AttributeListeners which
raise before the action actually occurs, and which can change
the given value into something else before its used.
A new example "validate_attributes.py" shows one such recipe
for doing this.   AttributeListener helper functions are
also on the way.


""",
u"""
- Fixed custom instrumentation bug whereby get_instance_dict()
was not called for newly constructed instances not loaded
by the ORM.


""",
u"""
- broke pool tests out into QueuePoolTest/SingletonThreadPoolTest
- added test for r5061/r5062 [ticket:1157]

""",
u"""
recheck the dirty list if extensions are present

""",
u"""
- The "extension" argument to Session and others can now
optionally be a list, supporting events sent to multiple
SessionExtension instances.  Session places SessionExtensions
in Session.extensions.


""",
u"""
- add an example illustrating attribute event reception.

""",
u"""
check extensions each time; user-defined code will be appending to "extensions" after the AttributeImpl has been constructed

""",
u"""
- starargs_as_list was not actually issuing SAPendingDeprecationWarning, fixed
- implemented code cleanup from [ticket:1152] but not including using the decorators module

""",
u"""
- Fixed bug whereby deferred() columns with a group in conjunction
with an otherwise unrelated synonym() would produce 
an AttributeError during deferred load.


""",
u"""
Corrected typo in the mapper docs. Fixes #1159.

""",
u"""
Type processors get a dialect, not an engine...
""",
u"""
ugh...try again

""",
u"""
critical fix to r5028 repairs SingleThreadPool to return a connection in case one had been removed via cleanup()

    """,
u"""
- expire/fetch strategies are now default for Query.update/Query.delete.
- added API docs for Query.update/Query.delete

""",
u"""
- Fixed bug whereby changing a primary key attribute on an 
entity where the attribute's previous value had been expired 
would produce an error upon flush(). [ticket:1151]


""",
u"""
- Session.delete() adds the given object to the session if 
not already present.  This was a regression bug from 0.4
[ticket:1150]


""",
u"""
- Added MSMediumInteger type [ticket:1146].


""",
u"""
- logging scale-back; the echo_uow flag on Session is deprecated, and unit of work logging is now
class level like all the other logging.
- trimmed back the logging API, centralized class_logger() as the single point of configuration for 
logging, removed per-instance logging checks from ORM.
- Engine and Pool logging remain at the instance level.  The modulus of "instance ids" has been upped
to 65535.  I'd like to remove the modulus altogether but I do see a couple of users each month
calling create_engine() on a per-request basis, an incorrect practice but I'd rather their applications 
don't just run out of memory.

""",
u"""
- The 'length' argument to all Numeric types has been renamed
to 'scale'.  'length' is deprecated and is still accepted
with a warning. [ticket:827]
- The 'length' argument to MSInteger, MSBigInteger, MSTinyInteger,
MSSmallInteger and MSYear has been renamed to 'display_width'.
[ticket:827]
- mysql._Numeric now consumes 'unsigned' and 'zerofill' from 
the given kw, so that the same kw can be passed along to Numeric
and allow the 'length' deprecation logic to still take effect
- added testlib.engines.all_dialects() to return a dialect for
every db module
- informix added to sqlalchemy.databases.__all__.  Since other 
"experimental" dbs like access and sybase are there, informix
should be as well.


""",
u"""
- fixed tearDown to reverse sorted table list

""",
u"""
- attributes now has an "active_history" flag.  This flag indicates that when new value is set or the existing value is deleted, we absolutely need the previous value to be present, including if it requires hitting a lazy loader.  Since somewhere around 0.4 we had not been loading the previous value as a performance optimization.
- the flag is set by a ColumnLoader which contains a primary key column.  This allows the mapper to have an accurate record of a primary key column when _save_obj() performs an UPDATE.
- the definition of who gets "active_history" may be expanded to include ForeignKey and any columns participating in a primaryjoin/seconddary join, so that lazyloaders can execute correctly on an expired object with pending changes to those attributes.
- expire-on-commit is why this is becoming a more important issue as of late
- fixes [ticket:1151], but unit tests, CHANGES note is pending

""",
u"""
- column_property() and synonym() both accept comparator_factory argument, allowing
custom comparison functionality
- made the mapper's checks for user-based descriptors when defining synonym or comparable property
stronger, such that a synonym can be used with declarative without having a user-based descriptor

""",
u"""
- Another old-style mixin fix and an explicit mapper() test for it.

""",
u"""
- Fix occurences of Class.c.column_name
- Fix a few typos/mistakes
- removed trailing whitespaces
- tried to achieve a more consistent syntax for spaces in properties
  declaration

  """,
u"""
- fixed a bug in declarative test which was looking for old version of history
- Added "sorted_tables" accessor to MetaData, which returns
Table objects sorted in order of dependency as a list.
This deprecates the MetaData.table_iterator() method.
The "reverse=False" keyword argument has also been
removed from util.sort_tables(); use the Python
'reversed' function to reverse the results.
[ticket:1033]


""",
u"""
catch AttributeError in case thread local storage was not configured

""",
u"""
attributes.get_history now reports some zero-length slots as the empty tuple rather than an empty list. nice speed boost and memory reduction.

""",
u"""
hack tweak: exc.NO_STATE is a tuple.
""",
u"""
more ORM @decorator fliparoo

""",
u"""
- The before_flush() hook on SessionExtension takes place
before the list of new/dirty/deleted is calculated for the
final time, allowing routines within before_flush() to
further change the state of the Session before the flush 
proceeds.   [ticket:1128]

- Reentrant calls to flush() raise an error.  This also
serves as a rudimentary, but not foolproof, check against 
concurrent calls to Session.flush().


""",
u"""
temporary check for unmapped class, until [ticket:1142] is resolved

""",
u"""
- fixed primary key update for many-to-many collections
where the collection had not been loaded yet
[ticket:1127]


""",
u"""
- class.someprop.in_() raises NotImplementedError pending
the implementation of "in_" for relation [ticket:1140]


""",
u"""
Applied .append(x, **kw) removal patch from [ticket:1124] and general cleanup.

""",
u"""
- Mock engines take on the .name of their dialect. [ticket:1123]

  Slightly backward incompatible: the .name is a read-only property.
  The test suite was assigning .name = 'mock'; this no longer works.


  """,
u"""
- Don't choke when instrumenting a class with an old-style mixin. [ticket:1078]
""",
u"""
removing this example until further notice (append_result() not an easy road to travel)

    """,
u"""
- Ignore old-style classes when building inheritance graphs. [ticket:1078]

""",
u"""
Re-use func_defaults when generating wrapper functions. [ticket:1139]

""",
u"""
- Renamed on_reconstitute to @reconstructor and reconstruct_instance
- Moved @reconstructor hooking to mapper
- Expanded reconstructor tests, docs

""",
u"""
Tidy.
""",
u"""
Ignore egg stuff.
""",
u"""
adjust counts for 2.4 based on buildbot observation, remove 2.3 counts

""",
u"""
dont rely upon AttributeError to test for None

""",
u"""
- with 2.3 support dropped, 
all usage of thread.get_ident() is removed, and replaced
with threading.local() usage.  this allows potentially
faster and safer thread local access.

""",
u"""
added import for interfaces, otherwise tsa.interfaces is undef if the test is run standalone

""",
u"""
- joins along a relation() from a mapped
class to a mapped subclass, where the mapped
subclass is configured with single table
inheritance, will include an 
IN clause which limits the subtypes of the
joined class to those requsted, within the
ON clause of the join.  This takes effect for 
eager load joins as well as query.join().    
Note that in some scenarios the IN clause will 
appear in the WHERE clause of the query 
as well since this discrimination has multiple
trigger points.


""",
u"""
- Improved the behavior of query.join()
when joining to joined-table inheritance
subclasses, using explicit join criteria
(i.e. not on a relation).


""",
u"""
added info on named tuples

""",
u"""
- When generating __init__, use a copy of the func_defaults, not a repr of them.

""",
u"""
added col with no name example

""",
u"""
- The composite() property type now supports
a __set_composite_values__() method on the composite
class which is required if the class represents
state using attribute names other than the 
column's keynames; default-generated values now
get populated properly upon flush.  Also,
composites with attributes set to None compare
correctly.  [ticket:1132]


""",
u"""
merged r5018 from 0.4 branch, but using contextual_connect() (will fix in 0.4 too)

    """,
u"""
comment

""",
u"""
- cleaned up the attributes scan for reconstitute hooks
- added more careful check for "_should_exclude", guard against possible heisenbug activity

""",
u"""
added unit tests for [ticket:1024]

""",
u"""
added missing **kwargs

""",
u"""
even better...

""",
u"""
- Fixed @on_reconsitute hook for subclasses 
which inherit from a base class.
[ticket:1129]


""",
u"""
- Improved the determination of the FROM clause
when placing SQL expressions in the query()
list of entities.  In particular scalar subqueries
should not "leak" their inner FROM objects out
into the enclosing query.


""",
u"""
- Temporarily rolled back the "ORDER BY" enhancement
from [ticket:1068].  This feature is on hold 
pending further development.


""",
u"""
- The RowTuple object returned by Query(*cols) now
features keynames which prefer mapped attribute 
names over column keys, column keys over 
column names, i.e. 
Query(Class.foo, Class.bar) will have names
"foo" and "bar" even if those are not the names
of the underlying Column objects.  Direct 
Column objects such as Query(table.c.col) will
return the "key" attribute of the Column.


""",
u"""
slightly more user-friendly repr method for CascadeOptions


""",
u"""
Corrected problem in docstring.

""",
u"""
- fixed endless loop bug which could occur
within a mapper's deferred load of 
inherited attributes.
- declarative initialization of Columns adjusted so that
non-renamed columns initialize in the same way as a non
declarative mapper.   This allows an inheriting mapper
to set up its same-named "id" columns in particular 
such that the parent "id" column is favored over the child
column, reducing database round trips when this value
is requested.


""",
u"""
Typo
""",
u"""
some doc stuff

""",
u"""
removed redundant check to _enable_transaction_accounting

""",
u"""
- compiler visit_label() checks a flag "within_order_by" and will render its own name
and not its contained expression, if the dialect reports true for supports_simple_order_by_label.
the flag is not propagated forwards, meant to closely mimic the syntax Postgres expects which is
that only a simple name can be in the ORDER BY, not a more complex expression or function call
with the label name embedded (mysql and sqlite support more complex expressions).

This further sets the standard for propigation of **kwargs within compiler, that we can't just send 
**kwargs along blindly to each XXX.process() call; whenever a **kwarg needs to propagate through, 
most methods will have to be aware of it and know when they should send it on forward and when not.
This was actually already the case with result_map as well.

The supports_simple_order_by dialect flag defaults to True but is conservatively explicitly set to
False on all dialects except SQLite/MySQL/Postgres to start.

[ticket:1068]

""",
u"""
descriptive error message raised when string-based relation() expressions inadvertently mistake a PropertyLoader for a ColumnLoader property

""",
u"""
- renamed autoexpire to expire_on_commit
- renamed SessionTransaction autoflush to reentrant_flush to more clearly state its purpose
- added _enable_transaction_accounting, flag for Mike Bernson which disables the whole 0.5 transaction state management; the system depends on expiry on rollback in order to function.

""",
u"""
a correction to the recent should_exclude change.  should_exclude is a little mixed
up as to when it honors "column_prefix" and when it doesn't, depending on whether or not
the prop is coming from a column name or from an inherited class.  Will need more testing
to uncover potential issues here.

""",
u"""
- The "entity_name" feature of SQLAlchemy mappers
has been removed.  For rationale, see
http://groups.google.com/group/sqlalchemy/browse_thread/thread/9e23a0641a88b96d?hl=en


""",
u"""
- Refactored declarative_base() as a thin wrapper over type()
- The supplied __init__ is now optional
- The name of the generated class can be specified
- Accepts multiple bases 

""",
u"""
- declarative.declarative_base():
  takes a 'metaclass' arg, defaulting to DeclarativeMeta
  renamed 'engine' arg to 'bind', backward compat
  documented

    """,
u"""
make ProxyImpl a top-level class (this makes it importable by FormAlchemy, making reverse-engineering synonyms a bit easier)
    """,
u"""
further refinement to the inheritance "descriptor" detection such that
local columns will still override superclass descriptors.

""",
u"""
test case to disprove [ticket:1126]

""",
u"""
added MutableType, Concatenable to __all__

""",
u"""
- Fixed bug whereby the "unsaved, pending instance" 
FlushError raised for a pending orphan would not take
superclass mappers into account when generating 
the list of relations responsible for the error.


""",
u"""
relation.order_by requires _literal_as_column conversion as well

""",
u"""
typo

""",
u"""
Corrects reflecttable in firebird database. Closes #1119.

""",
u"""
Raised an error when sqlite version does not support default values.  Addresses #909 in a purposeful way.

""",
u"""
added dummy column to correct results on sqlite

""",
u"""
- func.count() with no argument emits COUNT(*)

    """,
u"""
Corrected problem with detecting closed connections.  Fixed issues in reflecttable for reflecting the mssql tables. Removed unicode reflection test from mssql. Need to investigate this further.

""",
u"""
allow SQLA-defaults on table columns that are excluded in the mapper

""",
u"""
- more accurate changelog message
- generalized the descriptor detection to any object with a __get__ attribute

""",
u"""
- An inheriting class can now override an attribute
inherited from the base class with a plain descriptor, 
or exclude an inherited attribute via the 
include_properties/exclude_properties collections.


""",
u"""
- A critical fix to dynamic relations allows the 
"modified" history to be properly cleared after
a flush().


""",
u"""
- Some improvements to the _CompileOnAttr mechanism which
should reduce the probability of "Attribute x was 
not replaced during compile" warnings. (this generally
applies to SQLA hackers, like Elixir devs).


""",
u"""
- Class-bound attributes sent as arguments to 
relation()'s remote_side and foreign_keys parameters 
are now accepted, allowing them to be used with declarative.


""",
u"""
- reverted r4955, that was wrong.  The backref responsible for the operation is the one where the "cascade" option should take effect.
- can use None as a value for cascade.
- documented cascade options in docstring, [ticket:1064]

""",
u"""
Corrected a couple of lingering transactional=True statements in the docs.

""",
u"""
zoomarks have gone up as a result of r4936, possibly others.  not clear why

""",
u"""
- save-update and delete-orphan cascade event handler 
now considers the cascade rules of the event initiator only, not the local
attribute.  This way the cascade of the initiator controls the behavior
regardless of backref events.

""",
u"""
- Fixed a series of potential race conditions in 
Session whereby asynchronous GC could remove unmodified,
no longer referenced items from the session as they were 
present in a list of items to be processed, typically 
during session.expunge_all() and dependent methods.


""",
u"""
- MapperProperty gets its .key attribute assigned early, in _compile_property.
MapperProperty compilation is detected using a "_compiled" flag.
- A mapper which inherits from another, when inheriting
the columns of its inherited mapper, will use any
reassigned property names specified in that inheriting
mapper.  Previously, if "Base" had reassigned "base_id"
to the name "id", "SubBase(Base)" would still get 
an attribute called "base_id".   This could be worked
around by explicitly stating the column in each
submapper as well but this is fairly unworkable
and also impossible when using declarative [ticket:1111].


""",
u"""
added a new test illustrating a particular inheritance bug.  will add ticket

""",
u"""
- mysql.MSEnum value literals now automatically quoted when used in a CREATE.
  The change is backward compatible. Slight expansion of patch from catlee.
  Thanks! [ticket:1110]

  """,
u"""
- Spiffed up the deprecated decorators & @flipped 'em up top

""",
u"""
Removed deprecated get_version_info, use server_version_info
""",
u"""
- Overhauled _generative and starargs decorators and flipped to 2.4 @syntax

""",
u"""
- Fixed some over-long ReST lines & general formatting touchups
""",
u"""
Completed engine_descriptors() removal (started in r4900)
    """,
u"""
- Moved to 2.4+ import syntax (w/ some experimental merge-friendly formatting)
    """,
u"""
Whitespace tweaks suggested by pep8.py
""",
u"""
- Removed the last of the 2.3 dict compat & some formatting tweaks.
""",
u"""
- Always use native threading.local (or the native dummy version)
    """,
u"""
- Always use native itemgetter & attrgetter
""",
u"""
- Always use native deque
""",
u"""
- Removed 2.3 Decimal compat

""",
u"""
- Dropped `reversed` emulation

""",
u"""
- Removed 2.3 set emulations/enhancements.
  (sets.Set-based collections & DB-API returns still work.)

    """,
u"""
And thus ends support for Python 2.3.

""",
u"""
- Fixed a couple lingering exceptions->exc usages
- Some import tidying

""",
u"""
- Fixed bug when calling select([literal('foo')])
or select([bindparam('foo')]).


""",
u"""
- Added a new SessionExtension hook called after_attach().
This is called at the point of attachment for objects
via add(), add_all(), delete(), and merge().


""",
u"""
Fix reflection where the table name has a duplicate name in a different schema
""",
u"""
- The "allow_column_override" flag from mapper() has
been removed.  This flag is virtually always misunderstood.
Its specific functionality is available via the 
include_properties/exclude_properties mapper arguments.


""",
u"""
fix adjacency list examples

""",
u"""
2.4 support !

""",
u"""
possible fix for MS-SQL version of match() test, but the real solution here may be to have the correct default paramstyle set up on the MS-SQL dialect.

""",
u"""
bump

""",
u"""
Fixed up some very annoying lengthy lines.

""",
u"""
Reverted CHANGES change. Not necessary for this type of fix.

""",
u"""
Added notation about MSSmallDate fix into CHANGES.

(cherry picked from commit 461ee7e08bb2a6f7b10b1c9f1348cc29bfecacbb)

    """,
u"""
added a passing test for [ticket:1105]

""",
u"""
And more
""",
u"""
Typo
""",
u"""
Fixed messed up __init__ in MSSmallDate. Fixes #1040.

""",
u"""
Added new basic match() operator that performs a full-text search. Supported on PostgreSQL, SQLite, MySQL, MS-SQL, and Oracle backends.

""",
u"""
typo

""",
u"""
typo

""",
u"""
Let doc font sizes adapt to browser prefs (experimental)
    """,
u"""
Added default support to OrderedDict.pop [ticket:585]
""",
u"""
Flag beta docs with a big red capsule
""",
u"""
- Declarative supports a __table_args__ class variable, which
is either a dictionary, or tuple of the form
(arg1, arg2, ..., {kwarg1:value, ...}) which contains positional
+ kw arguments to be passed to the Table constructor. 
[ticket:1096]


""",
u"""
    - Unicode, UnicodeText types now set "assert_unicode" and
      "convert_unicode" by default, but accept overriding
      **kwargs for these values.


      """,
    u"""
- SQLite Date, DateTime, and Time types only accept Python
datetime objects now, not strings.  If you'd like to format
dates as strings yourself with SQLite, use a String type.
If you'd like them to return datetime objects anyway despite 
their accepting strings as input, make a TypeDecorator around 
String - SQLA doesn't encourage this pattern.


""",
u"""
Fixed borked testlib due to r4901.

""",
u"""
Refactored the mock_engine in the tests so it's not duplicated in several places. Closes #1098

""",
u"""
- re-fixed the fix to the prefixes fix
- removed ancient descriptor() functions from dialects; replaced with Dialect.name
- removed similarly ancient sys.modules silliness in Engine.name

""",
u"""
- session.refresh() raises an informative error message if
the list of attributes does not include any column-based
attributes.

- query() raises an informative error message if no columns
or mappers are specified.

- lazy loaders now trigger autoflush before proceeding.  This
allows expire() of a collection or scalar relation to 
function properly in the context of autoflush.

- whitespace fix to new Table prefixes option

""",
u"""
commented out bus erroring section for now pending [ticket:1099] resolution

""",
u"""
Added prefixes option to  that accepts a list of string to insert after CREATE in the CREATE TABLE statement. Closes #1075.

""",
u"""
Corrected grammar on session documents. Closes #1097.

""",
u"""
update poly_assoc examples for 0.4+ syntax

""",
u"""
Fixed typo where plugins docs were referencing synonyn_for instead of synonym_for.  Closes #1029

""",
u"""
Added PGCidr type to postgres. Closes #1092

(cherry picked from commit 2394a6bb6c5f77afd448640ce03cf6fda0335a23)

    """,
u"""
Corrected a reference to alt_schema_2 and fixed a docstring indentation for Table.

""",
u"""
merge r4889, SQLite Float type, from 0.4 branch

""",
u"""
Corrected docstring for Pool class to show that the default value for use_threadlocal is False. closes #1095.

""",
u"""
simplified _get_colspec

""",
u"""
Ugh, learning to use git-svn, [4884] was not supposed to go upstream. Reverting.

""",
u"""
Session.bind gets used as a default even when table/mapper specific binds are defined.

""",
u"""
query update and delete need to autoflush

""",
u"""
0.5

""",
u"""
removed fairly pointless test which relied on PK generation artifacts

""",
u"""
- consider args[0] as self when introspecting def(*args): ... [ticket:1091]
                                                               """,
                                                            u"""
- fixed up vertical.py
- Fixed query.join() when used in conjunction with a
columns-only clause and an SQL-expression 
ON clause in the join.


                      """,
                    u"""
- Modified SQLite's representation of "microseconds" to 
match the output of str(somedatetime), i.e. in that the
microseconds are represented as fractional seconds in
string format.  [ticket:1090]
- implemented a __legacy_microseconds__ flag on DateTimeMixin which can
be used per-class or per-type instances to get the old behavior, for
compatibility with existing SQLite databases encoded by a previous 
version of SQLAlchemy.
- will implement the reverse legacy behavior in 0.4.

""",
u"""
use normal ScopedSession, with autoflush, instead of custom one
""",
u"""
`session.Query().iterate_instances()` has been renamed to just `instances()`. The old `instances()` method returning a list instead of an iterator no longer
exists. If you were relying on that behavior, you should use `list(your_query.instances())`.


""",
u"""
- Repaired `__str__()` method on Query. [ticket:1066]


""",
u"""
- Fixed explicit, self-referential joins between two 
joined-table inheritance mappers when using 
query.join(cls, aliased=True).  [ticket:1082]


""",
u"""
fixed the quote() call within dropper.visit_index()

    """,
u"""
merged r4870 from 0.4 branch, index name truncation, [ticket:820]

""",
u"""
- merged r4868, disallow overly long names from create/drop, from 0.4 branch, [ticket:571]

""",
u"""
- fixed some concrete inheritance ramifications regarding r4866
- added explicit test coverage for r4866 with joined table inheritance

""",
u"""
- implemented [ticket:887], refresh readonly props upon save
- moved up "eager_defaults" active refresh step (this is an option used by just one user pretty much)
to be per-instance instead of per-table
- fixed table defs from previous deferred attributes enhancement
- CompositeColumnLoader equality comparison fixed for a/b == None; I suspect the composite capability in SA 
needs a lot more work than this

""",
u"""
- In addition to expired attributes, deferred attributes
also load if their data is present in the result set
[ticket:870]


""",
u"""
better comment

""",
u"""
- Oops, convert @decorator to 2.3 syntax and strengthen raw_append test.
""",
u"""
- Added is_active flag to Sessions to detect when 
a transaction is in progress [ticket:976].  This
flag is always True with a "transactional" 
(in 0.5 a non-"autocommit") Session.



""",
u"""
test coverage for server side statement detection

""",
u"""
merged r4857, postgres server_side_cursors fix, from 0.4 branch

""",
u"""
remove old test

""",
u"""
updated verbiage for 0.5beta1 release

""",
u"""
- Don't insist on locals() mutability [ticket:1073]
""",
u"""
will call this beta1 (same as 0.4 version did)

    """,
u"""
- merged r4841 from 0.4 branch (enable_typechecks lockdown)

    """,
u"""
restored a "distinct" setting that got whacked

""",
u"""
docstrings for instances()/iterate_instances()

    """,
u"""
- Query.UpdateDeleteTest.test_delete_fallback fails on mysql due to subquery in DELETE; not sure how to do this exact operation in MySQL
- added query_cls keyword argument to sessionmaker(); allows user-defined Query subclasses to be generated by query().
- added @attributes.on_reconstitute decorator, MapperExtension.on_reconstitute, both receieve 'on_load' attribute event allowing
non-__init__ dependent instance initialization routines.
- push memusage to the top to avoid pointless heisenbugs
- renamed '_foostate'/'_fooclass_manager' to '_sa_instance_state'/'_sa_class_manager'
- removed legacy instance ORM state accessors
- query._get() will use _remove_newly_deleted instead of expunge() on ObjectDeleted, so that transaction rollback
restores the previous state
- removed MapperExtension.get(); replaced by a user-defined Query subclass
- removed needless **kwargs from query.get()
- removed Session.get(cls, id); this is redundant against Session.query(cls).get(id)
- removed Query.load() and Session.load(); the use case for this method has never been clear, and the same functionality is available in more explicit ways

""",
u"""
merged merge fix from r4834/rel_0_4 branch

""",
u"""
make Query._clone() class-agnostic

""",
u"""
illustrates a simple Query "hook" to implement query caching.

""",
u"""
- removed query.min()/max()/sum()/avg().  these should be called using column arguments or values in conjunction with func.
- fixed [ticket:1008], count() works with single table inheritance
- changed the relationship of InstrumentedAttribute to class such that each subclass in an inheritance hierarchy gets a unique InstrumentedAttribute per column-oriented attribute, including for the same underlying ColumnProperty.  This allows expressions from subclasses to be annotated accurately so that Query can get a hold of the exact entities to be queried when using column-based expressions.  This repairs various polymorphic scenarios with both single and joined table inheritance.
- still to be determined is what does something like query(Person.name, Engineer.engineer_info) do; currently it's problematic.  Even trickier is query(Person.name, Engineer.engineer_info, Manager.manager_name)

""",
u"""
merged r4829 of rel_0_4, [ticket:1058]

""",
u"""
merged [ticket:1062] fix from 0.4 branch r4827

""",
u"""
- improved the attribute and state accounting performed by query.update() and query.delete()
- added autoflush support to same

""",
u"""
- Lengthless String type
""",
u"""
Add delete and update methods to query

""",
u"""
Not implemenented binary ops also raise UnevaluatableError

""",
u"""
add with_only_columns to Select to allow for removing columns from selects

""",
u"""
Preliminary implementation for the evaluation framework

""",
u"""
- bumped PG's call count on test #6 to 1193 for py2.4; this is due to non-pool-threadlocal nature adding some checkout overhead

""",
u"""
- added "CALL" to Mysql select keywords
- NameError doesn't have "message" in py2.4

""",
u"""
added string argument resolution to relation() in conjunction with declarative for: order_by,
primaryjoin, secondaryjoin, secondary, foreign_keys, and remote_side.

""",
u"""
a comment indicating why we can't raise an error for relation(Foo, uselist=False, order_by=something)

""",
u"""
oracle dialect takes schema name into account when checking for existing tables
of the same name. [ticket:709]

""",
u"""
- PropertyLoader.foreign_keys becomes private
- removed most __foo() defs from properties.py
- complexity reduction in PropertyLoader.do_init()

    """,
u"""
- removed info about _local_remote_pairs from PropertyLoader.__determine_fks
- added order_by(), group_by(), having() to the list of "no offset()/limit()", [ticket:851]

""",
u"""
merged r4809 from rel_0_4, oracle fix

""",
u"""
Removed inlining for list.append.
""",
u"""
- unrolled loops for the simplified Session.get_bind() args
- restored the chunk of test r4806 deleted (!)

    """,
u"""
- globally renamed refresh_instance to refresh_state
- removed 'instance' arg from session.get_bind() and friends, this is not a public API
- renamed 'state' arg on same to '_state'
- fixes [ticket:1055]

""",
u"""
Updated fixmes.
""",
u"""
Updated some todos.
""",
u"""
Removed deprecated Dialect.prexecute_sequences aliasing
""",
u"""
- Fixed ORM orphaning bug with _raw_append method
- Promoted _reorder to reorder
- Now horking docstrings of overloaded methods from list
- Added a doctest

""",
u"""
- Be a little smarter about aliased funcs/methods by ignoring func_name

""",
u"""
- Another namespace cleanup tweak, why not.
""",
u"""
- Docstring fix.
""",
u"""
Duh.
""",
u"""
- Removed deprecated append(val, **kw)
- dict/set/list proxies are now docstring'd like their python counterparts

""",
u"""
- More uses of exc.NO_STATE
""",
u"""
- Centralized 'x is not mapped' reporting into sa.orm.exc.
- Guards are now present on all public Session methods and passing in an
  unmapped hoho anywhere yields helpful exception messages, going to some
  effort to provide hints for debugging situations that would otherwise seem
  hopeless, such as broken user instrumentation or half-pickles.


  """,
u"""
- ...and added bind.py into the orm suite

""",
u"""
- Moved an ORM test out of engine...

""",
u"""
- 2.3 compat.
""",
u"""
Refactor-o fix.
""",
u"""
handle null tablespace_name
""",
u"""
- Fleshed out Session.get_bind(), generating a couple todos: [ticket:1053], [ticket:1054], [ticket:1055]
- Trotted out util.pending_deprecation, replacing some 'TODO: deprecate's
- Big session docstring content edit fiesta
- session.py line length and whitespace non-fiesta


""",
u"""
add CHAR to ischema_names map; some minor cleanup
""",
u"""
- Quick cleanup of defaults.py.  The main DefaultTest is still a mess.

""",
u"""
Split out a couple true autoincrement/identity tests from emulated-with-sequences autoincrement=True tests.

""",
u"""
Formatting.
""",
u"""
- changed char_length() to use a fake, neutral "generic function"
- assert_compile() reports the dialect in use

""",
u"""
- zoomark/zoomark_orm seem to work with pool_threadlocal turned off, [ticket:1050] becomes WORKSFORME
- fixed probably errenous unique=True checkin on unitofwork.py

""",
u"""
- Implemented generic CHAR_LENGTH for sqlite (-> LENGTH())
- Updated .requires for firebird

""",
u"""
Remove some noise from the uow test
""",
u"""
pool_threadlocal is off by default [ticket:1049]

""",
u"""
-removed useless log statement (merge garbage?)
- clarified autocommit mechanism

""",
u"""
put a cleanup handler on the "echo" property to try preventing log garbage in the buildbot

""",
u"""
added ORM version of zoomark, python 2.5 only for starters

""",
u"""
some order by's failing on the buildbot

""",
u"""
- added test for threadlocal not supporting begin_nested()
- removed query.compile(); use explicit query.with_labels().statement instead
- moved statement annotation step upwards from query._compile_context() to outliers from_self()/statement.  speeds zoomark.step_6_editing by 16%

""",
u"""
The column default has been renamed `server_default` in 0.5
""",
u"""
begin() pre-issues a flush() in all cases, better fix for [ticket:1046] and allows rollback to work properly with autocommit=True/begin()

    """,
u"""
dont raise assertions when in autocommit mode [ticket:1046]

""",
u"""
- added some help for a heavily flush-order-dependent test
- quote flag propagates to _Label, [ticket:1045]

""",
u"""
added an assertion to prevent against the use in [ticket:1048]

""",
u"""
auto exists remembers to alias in the case of explicit selectable with of_type(), [ticket:1047]

""",
u"""
a particular test which fails in 0.4

""",
u"""
Don't blat Table.quote= when resolving foreign keys.
""",
u"""
Fix table.delete() arguments
""",
u"""
Followup to [4760]: forward **kwargs on TableClause.delete()
    """,
u"""
Corrected Firebird failure reasons
""",
u"""
Fix typo
""",
u"""
Minor doc fixes
""",
u"""
Correct failure reason
""",
u"""
Augment expression.Delete() with a kwargs, like Insert() and Update()
    """,
u"""
Eep.
""",
u"""
raise NotImplemented for begin_nested()

    """,
u"""
- Removed @unsupported

""",
u"""
Fix fix.
""",
u"""
Query.one() raises either NoResultFound or MultipleResultsFound, [ticket:1034]
""",
u"""
- Adjusted zoomoark
- Added test/orm/defaults.  Ambitiously uses ansi triggers.

""",
u"""
Columns now have default= and server_default=. PassiveDefault fades away.

""",
u"""
fixes for PG, Mysql

""",
u"""
fixed mysql not supported declarations

""",
u"""
Support Firebird 2.0+ RETURNING
""",
u"""
Whitespace
""",
u"""
- renamed query.slice_() to query.slice()
- pulled out DeclarativeMeta.__init__ into its own function, added instrument_declarative() 
which will do the "declarative" thing to any class independent of its lineage (for ctheune)
- added "cls" kwarg to declarative_base() allowing user-defined base class for declarative base [ticket:1042]

""",
u"""
- LIMIT/OFFSET of zero is detected within compiler and is counted
- Query.__getitem__ now returns list/scalar in all cases, not generative (#1035)
- added Query.slice_() which provides the simple "limit/offset from a positive range" operation,
we can rename this to range_()/section()/_something_private_because_users_shouldnt_do_this() as needed

""",
u"""
- fixed propagation of operate() for aliased relation descriptors
- ColumnEntity gets a selectable

""",
u"""
Removed declared_synonym(), pep-8 clean ups.
""",
u"""
Removed: all legacy users migrated.
""",
u"""
- Reworked test/orm/mapper
- Exposed some uncovered (and broken) functionality
- Fixed [ticket:1038]

""",
u"""
Tag PKs with `test_needs_autoincrement` on a few test
""",
u"""
Support for  under Firebird
""",
u"""
Tag some tests that fail under Firebird
""",
u"""
scaled back the equivalents determined in _equivalent_columns to just current polymorphic_union
 behavior, fixes [ticket:1041]

 """,
u"""
- clause adaption hits _raw_columns of a select() (though no ORM tests need this feature currently)
- broke up adapter chaining in eagerload, erroneous "wrapping" in row_decorator.  column_property() subqueries are now affected only by the ORMAdapter for that mapper.  fixes [ticket:1037], and may possibly impact some of [ticket:949]

""",
u"""
Check for the presence of the Firebird generator, when creating/dropping a sequence
""",
u"""
Add another exception case to Firebird' is_disconnect()
""",
u"""
Typo
""",
u"""
Tagged two tests that fail under Firebird
""",
u"""
Use a BLOB when asked for a [VAR]CHAR without a length under Firebird
""",
u"""
Added explicit sequences on a few primary keys and minor fixes wrt Firebird
""",
u"""
tweak

""",
u"""
another approach

""",
u"""
cant reproduce buildbot's memory profiling, random fix attempt

""",
u"""
added blurb on session.rollback()

    """,
u"""
py2.4 seems to have different memory behavior than 2.5, test for both "adjusting down" as well as "flatline"

""",
u"""
- removed all the order by's that no longer apply.
- realized about declarative that foobar: relation("SomeFutureClass") is not very useful for collections since
we can't set "order_by" there.

""",
u"""
correcting dataload profiles for various tests

""",
u"""
bizarre duplicate keyword seems to not raise in py2.5

""",
u"""
merged r4720 from 04 branch for [ticket:1036]

""",
u"""
Fix typo in the ORM tutorial
""",
u"""
Reworked & stripped.
""",
u"""
order by doc

""",
u"""
edits

""",
u"""
removed deprecated plugins docs

""",
u"""
backref() function uses primaryjoin/secondaryjoin of the parent relation() if not otherwise specified, removing the frequently annoying need to specify primaryjoin twice.

""",
u"""
Chipping away at remaining cruft.
""",
u"""
- fixed a fairly critical bug in clause adaption/corresponding column in conjunction with annotations
- implicit order by is removed, modified many tests to explicitly set ordering, probably many more to go
once it hits the buildbot. 

""",
u"""
add target_fullname as a public property for _get_colspec

""",
u"""
Test suite modernization in progress.  Big changes:
 - @unsupported now only accepts a single target and demands a reason
   for not running the test.
 - @exclude also demands an exclusion reason
 - Greatly expanded @testing.requires.<feature>, eliminating many
   decorators in the suite and signficantly easing integration of
   multi-driver support.
 - New ORM test base class, and a featureful base for mapped tests
 - Usage of 'global' for shared setup going away, * imports as well


 """,
u"""
more order bys...

""",
u"""
some tweaks to help MySQL

""",
u"""
- more portable tests for eager/inheritance joins
- bumped 2.4 call count for profile test_select
- don't need initialize_properties() during reentrant compile() call (for now)

""",
u"""
MSText no longer implicitly creates TEXT for string with no length
(this actually allows CAST (foo, VARCHAR) to render too)

    """,
u"""
added query.subquery() as shorthand for query.statement.alias()

    """,
u"""
identified case where pending upon commit() is needed; since attribute rollback functionality is gone its safe to revert to this

""",
u"""
move the definition of sessions public methods closer to the source

""",
u"""
added "add", "add_all", "expire_all" to SS

""",
u"""
tweak

""",
u"""
need delete-orphan

""",
u"""
- warnings about Query invalid operations become InvalidRequestErrors
- __no_criterion() checks for more pre-existing conditions
- helpful note in 0.5 svn readme

""",
u"""
r4695 merged to trunk; trunk now becomes 0.5.  
0.4 development continues at /sqlalchemy/branches/rel_0_4

""",
u"""
doc update on quote

""",
u"""
remove **kwargs from execute(), scalar(), connection(), and get_bind().  document all args, [ticket:1028]

""",
u"""
- backported 0.5's contains_eager() behavior such that rendering of eager clauses are disabled.  workaround here is compatible with 0.5 but not compatible with the little-known "decorator" argument to contains_eager() (which was also removed in 0.5).  Doesn't remove any existing 0.4 functionality.

""",
u"""
- added an example dynamic_dict/dynamic_dict.py, illustrating
a simple way to place dictionary behavior on top of 
a dynamic_loader.


""",
u"""
- Fixed "concatenate tuple" bug which could occur with
Query.order_by() if clause adaption had taken place.
[ticket:1027]


""",
u"""
Query.select() wont call filter() if arg is None

""",
u"""
fix foreign_keys example

""",
u"""
Added missing argument check on CheckConstraint
""",
u"""
- _Label adds itself to the proxy collection so that it works in correspoinding column.  fixes some eager load with column_property bugs.
- this partially fixes some issues in [ticket:1022] but leaving the "unlabeled" fix for 0.5 for now

""",
u"""
- added "after_begin()" hook to Session
- Session.rollback() will rollback on a prepared session

""",
u"""
Tidy.
""",
u"""
Fix typo
""",
u"""
Adjusted inplace-binops on set-based collections and association proxies to
more closely follow builtin (2.4+) set semantics.  Formerly any set duck-type
was accepted, now only types or subtypes of set, frozenset or the collection
type itself are accepted.


""",
u"""
failing case

""",
u"""
Fixed duplicate append event emission on repeated instrumented set.add() operations.
""",
u"""
Update for r4643
""",
u"""
Renamed rollback_returned to reset_on_return.  Future, dialect-aware pools can do better than rollback for this function.
""",
u"""
    - same as [ticket:1019] but repaired the non-labeled use case
      [ticket:1022]


      """,
    u"""
    - added "rollback_returned" option to Pool which will 
      disable the rollback() issued when connections are 
      returned.  This flag is only safe to use with a database
      which does not support transactions (i.e. MySQL/MyISAM).


      """,
    u"""
  - Column.copy() respects the value of "autoincrement",
      fixes usage with Migrate [ticket:1021]


      """,
    u"""
- fixes to the "exists" function involving inheritance (any(), has(),
~contains()); the full target join will be rendered into the
EXISTS clause for relations that link to subclasses.


""",
u"""
- The collection instrumentation sweep now skips over descriptors that raise AttributeError.
""",
u"""
- fixed reentrant mapper compile hang when 
a declared attribute is used within ForeignKey, 
ie. ForeignKey(MyOtherClass.someattribute)


    """,
u"""
- Backported attribute sweep removal (instrumentation) and r4493 from 0.5
""",
u"""
one-off workaround for mssql + odbc options, user patch
""",
u"""
- an unfortunate naming conflict
- needed sql import on and()

    """,
u"""
- factored out the logic used by Join to create its join condition
- With declarative, joined table inheritance mappers use a slightly relaxed
function to create the "inherit condition" to the parent
table, so that other foreign keys to not-yet-declared 
Table objects don't trigger an error.


""",
u"""
added some reference tests for the any() situation

""",
u"""
- Fix 2.3 regression from 4598
""",
u"""
- added a feature to eager loading whereby subqueries set
as column_property() with explicit label names (which is not
necessary, btw) will have the label anonymized when
the instance is part of the eager join, to prevent
conflicts with a subquery or column of the same name 
on the parent object.  [ticket:1019]


""",
u"""
And a copy.copy() test for the proxy cache.
""",
u"""
- Refresh the cached proxy if the cache was built for a different instance.
""",
u"""
added multi-level concrete inheritance test (testing with_polymorphic mapper argument)

    """,
u"""
more declarative doc updates

""",
u"""
fix docs for declarative

""",
u"""
Savepoints are supported under Firebird
""",
u"""
fix order by for MySQL environment

""",
u"""
- improved behavior of text() expressions when used as 
FROM clauses, such as select().select_from(text("sometext"))
[ticket:1014]
- removed _TextFromClause; _TextClause just adds necessary FromClause descriptors
at the class level


""",
u"""
- refined mapper._save_obj() which was unnecessarily calling
__ne__() on scalar values during flush [ticket:1015]


""",
u"""
Expanded --noncomparable to cover all comparision ops
""",
u"""
typo

""",
u"""
Update docstring [ticket:873]
""",
u"""
Explicit test of .autoflush(False) to avoid issues with save_on_init=True [ticket:869]
""",
u"""
flush(objects=[]) is a no-op [ticket:928]
""",
u"""
    - fixed Class.collection==None for m2m relationships
      [ticket:4213]


      """,
    u"""
- restored usage of append_result() extension method for primary 
query rows, when the extension is present and only a single-
entity result is being returned.


""",
u"""
Added 'odbc_options' keyword to the MSSQL dialect. Allows a partial ODBC connection string to be passed through to the connection string generator.
""",
u"""
- Support for COLLATE: collate(expr, col) and expr.collate(col)
    """,
u"""
- simplified __create_lazy_clause to make better usage of the new local/remote pairs collection
- corrected the direction of local/remote pairs for manytoone
- added new tests which demonstrate lazyloading working when the bind param is embedded inside of a SQL function,
when _local_remote_pairs argument is used; fixes the viewonly version of [ticket:610]
- removed needless kwargs check from visitors.traverse

""",
u"""
added info about _local_remote_pairs to error message

""",
u"""
- added experimental relation() flag to help with primaryjoins
across functions, etc., _local_remote_pairs=[tuples].  
This complements a complex primaryjoin condition allowing 
you to provide the individual column pairs which comprise
the relation's local and remote sides.


""",
u"""
Pass connection to get_default_schema_name
""",
u"""
Firebird 2 has a SUBSTRING() builtin, expose it thru a function
""",
u"""
- re-established viewonly relation() configurations that
join across multiple tables.


""",
u"""
Add a new 'odbc_autotranslate' engine/dburi kwd parm to the MSSQL pyodbc dialect; string kwd contents will be passed through to ODBC connection string.
[ticket:1005]
""",
u"""
remove monetdb typo
""",
u"""
refactor of default_paramstyle, use paramstyle argument on Dialect to change
""",
u"""
- Avoid cProfile on 2.4 (available via lsprof?)
    """,
u"""
remove unneeded compile assertion test, doesn't work on MySQL

""",
u"""
*headslap* those mutators cant mutate the collections except for never-generated selectables; its not worth it

""",
u"""
- removed ancient assertion that mapped selectables require
"alias names" - the mapper creates its own alias now if
none is present.  Though in this case you need to use 
the class, not the mapped selectable, as the source of
column attributes - so a warning is still issued.


""",
u"""
some fk fixes for PG

""",
u"""
- merged -r4458:4466 of query_columns branch
- this branch changes query.values() to immediately return an iterator, adds a new "aliased" construct which will be the primary method to get at aliased columns when using values()
- tentative ORM versions of _join and _outerjoin are not yet public, would like to integrate with Query better (work continues in the branch)
- lots of fixes to expressions regarding cloning and correlation.  Some apparent ORM bug-workarounds removed.
- to fix a recursion issue with anonymous identifiers, bind parameters generated against columns now just use the name of the column instead of the tablename_columnname label (plus the unique integer counter).  this way expensive recursive schemes aren't needed for the anon identifier logic.   This, as usual, impacted a ton of compiler unit tests which needed a search-n-replace for the new bind names.

""",
u"""
refined "local_remote_pairs" a bit to account for the same columns repeated multiple times

""",
u"""
- Pool listeners may now be specified as a duck-type of PoolListener or a dict of callables, your choice.


""",
u"""
factored down exportable_columns/flatten_cols/proxy_column/oid_etc_yada down to a single, streamlined "_populate_column_collection" method called for all selectables

""",
u"""
fixed union() bug whereby oid_column would not be available if no oid_column in embedded selects

""",
u"""
bump

""",
u"""
Yep.
""",
u"""
- ReST fixes
- reverted strange jeklike symbol syntax

""",
u"""
- changed the name to "local/remote pairs"
- added closing ' to symbol str()  (I'm assuming it's supposed to be that way)

""",
u"""
- merged sync_simplify branch
- The methodology behind "primaryjoin"/"secondaryjoin" has
been refactored.  Behavior should be slightly more
intelligent, primarily in terms of error messages which
have been pared down to be more readable.  In a slight
number of scenarios it can better resolve the correct 
foreign key than before.
- moved collections unit test from relationships.py to collection.py
- PropertyLoader now has "synchronize_pairs" and "equated_pairs" 
collections which allow easy access to the source/destination
parent/child relation between columns (might change names)
- factored out ClauseSynchronizer (finally)
- added many more tests for priamryjoin/secondaryjoin 
error checks


""",
u"""
- microcleanup
""",
u"""
- Experimental: prefer cProfile over hotspot for 2.5+
- The latest skirmish in the battle against zoomark and sanity:
  3rd party code is factored out in the function call count canary tests

  """,
u"""
A couple of usage examples for the case statement

""",
u"""
- case() interprets the "THEN" expressions
as values by default, meaning case([(x==y, "foo")]) will
interpret "foo" as a bound value, not a SQL expression.
use text(expr) for literal SQL expressions in this case.
For the criterion itself, these may be literal strings
only if the "value" keyword is present, otherwise SA
will force explicit usage of either text() or literal().


""",
u"""
some cleanup, some method privating, some pep8, fixed up _col_aggregate and merged
its functionality with _count()

    """,
u"""
The case() function now also takes a dictionary as its whens parameter. But beware that it doesn't escape literals, use the literal construct for that.

""",
u"""
- Added some convenience descriptors to Query: 
query.statement returns the full SELECT construct,
query.whereclause returns just the WHERE part of the
SELECT construct.


""",
u"""
Added a new 'max_identifier_length' keyword to the mssql_pyodbc dialect 
""",
u"""
Cascade traversal algorithm converted from recursive to iterative to support deep object graphs.

""",
u"""
- Got PG server side cursors back into shape, added fixed
unit tests as part of the default test suite.  Added
better uniqueness to the cursor ID [ticket:1001]
- update().values() and insert().values() take keyword 
arguments.


""",
u"""
- Re-tuned call counts for 2.3 through 2.5.
""",
u"""
- Run profiling tests first.
""",
u"""
fixed OracleRaw type adaptation [ticket:902]

""",
u"""
some fixes to the MS-SQL aliasing so that result_map is properly populated

""",
u"""
doh

""",
u"""
some test fixup for oracle

""",
u"""
reduced 2.4 callcounts...

""",
u"""
slight function call reduction

""",
u"""
- Assorted flakes.
""",
u"""
- Revamped the Connection memoize decorator a bit, moved to engine
- MySQL character set caching is more aggressive but will invalidate the cache if a SET is issued.
- MySQL connection memos are namespaced: info[('mysql', 'server_variable')]

""",
u"""
- More 2.4 generator squashing.
""",
u"""
continue attempting to get proper count for pybot on 2.5, ensure order_by for oracle query

""",
u"""
- added verbose activity to profiling.function_call_count
- simplified oracle non-ansi join generation, removed hooks from base compiler
- removed join() call from _label generation, fixed repeat label gen

""",
u"""
- More zzzeek enablement.
""",
u"""
- Squashed 2.4 generators.
""",
u"""
added an order by to fix potential mysql test failure

""",
u"""
seems like the recent itertools add to select()._get_display_froms() adds overhead in 2.4?  not sure why

""",
u"""
fix up some unit tests

""",
u"""
- merge() may actually work now, though we've heard that before...
- merge() uses the priamry key attributes on the object if _instance_key not present.  so merging works for instances that dont have an instnace_key, will still issue UPDATE for existing rows.
- improved collection behavior for merge() - will remove elements from a destination collection that are not in the source.
- fixed naive set-mutation issue in Select._get_display_froms
- simplified fixtures.Base a bit

""",
u"""
- Tighten up r4399 _set_iterable docs
""",
u"""
- Light collections refactor, added public collections.bulk_replace.
- Collection attribs gain some private load-from-iterable flexiblity.


""",
u"""
weird, old cruft

""",
u"""
- removed redundant get_history() method
- the little bit at the bottom of _sort_circular_dependencies is absolutely covered by test/orm/cycles.py !  removing it breaks the test as run on PG.

""",
u"""
C-u 66 C-x f M-q
""",
u"""
MSSQL adjustments to pyodbc connection string building
""",
u"""
Add a new 'driver' keyword to the MSSQL pyodbc Dialect.
Refresh items that were recently reverted by another checkin
""",
u"""
- reverted previous "strings instead of tuples" change due to more specific test results showing tuples faster
- changed cache decorator call on default_schema_name call to a connection.info specific one

""",
u"""
*whistle*
""",
u"""
- Removed cache decorator.
""",
u"""
some cache decorator calls...

""",
u"""
using concatenated strings as keys in generated_ids collection; they hash slightly faster than tuples

""",
u"""
- schema-qualified tables now will place the schemaname
ahead of the tablename in all column expressions as well
as when generating column labels.  This prevents cross-
schema name collisions in all cases [ticket:999]
- the "use_schema" argument to compiler.visit_column() is removed.  It uses
schema in all cases now.
- added a new test to the PG dialect to test roundtrip insert/update/delete/select
statements with full schema qualification

""",
u"""
MSSQL fixes for tickets 979, 916, 884
""",
u"""
- added _from_self()
- changelog authoring

""",
u"""
- rearranged LoaderStrategies a bit 
- removed awareness of "dynamic" from attributes and replaced with "impl_class"
- moved DynaLoader into dynamic.py
- removed create_strategy() method from StrategizedProperty; they set up
'strategy_class' so that StrategizedProperty treats the default the same
as the optional loaders

""",
u"""
turned starargs conversion to a decorator, per jek's advice. select().order_by()/group_by() already take *args.

""",
u"""
- Added PendingDeprecationWarning support
- Deprecation decorator is now a real decorator

""",
u"""
- declarative_base() takes optional kwarg "mapper", which 
is any callable/class/method that produces a mapper,
such as declarative_base(mapper=scopedsession.mapper).
This property can also be set on individual declarative
classes using the "__mapper_cls__" property.


""",
u"""
- merged with_polymorphic branch, which was merged with query_columns branch
- removes everything to do with select_table, which remains as a keyword argument synonymous with 
with_polymorphic=('*', select_table).
- all "polymorphic" selectables find their way to Query by way of _set_select_from() now, so that
all joins/aliasing/eager loads/etc. is handled consistently.  Mapper has methods for producing 
polymorphic selectables so that Query and eagerloaders alike can get to them.
- row aliasing simplified, so that they don't need to nest.  they only need the source selectable
and adapt to whatever incoming columns they get.
- Query is more egalitarian about mappers/columns now.  Still has a strong sense of "entity zero",
but also introduces new unpublished/experimental _values() method which sets up a columns-only query.
- Query.order_by() and Query.group_by() take *args now (also still take a list, will likely deprecate
in 0.5).  May want to do this for select() as well.
- the existing "check for False discriminiator" "fix" was not working completely, added coverage
- orphan detection was broken when the target object was a subclass of the mapper with the orphaned
relation, fixed that too.

""",
u"""
- can now allow selects which correlate all FROM clauses
and have no FROM themselves.  These are typically
used in a scalar context, i.e. SELECT x, (SELECT x WHERE y)
FROM table.  Requires explicit correlate() call.


""",
u"""
- Notes for r4338

""",
u"""
- fixed SQL function truncation of trailing underscores
[ticket:996]


""",
u"""
- Added generic func.random (non-standard SQL)

    """,
u"""
a few more tweaks

""",
u"""
removed AbstractClauseProcessor, merged its copy-and-visit behavior into ClauseVisitor

""",
u"""
- already-compiled mappers will still trigger compiles of
 other uncompiled mappers when used [ticket:995]


 """,
u"""
added nicer error message to dependent class not found

""",
u"""
 - the "owner" keyword on Table is now deprecated, and is
      exactly synonymous with the "schema" keyword.  Tables
      can now be reflected with alternate "owner" attributes,
      explicitly stated on the Table object or not using
      "schema".

    - all of the "magic" searching for synonyms, DBLINKs etc.
      during table reflection
      are disabled by default unless you specify
      "oracle_resolve_synonyms=True" on the Table object.
      Resolving synonyms necessarily leads to some messy
      guessing which we'd rather leave off by default.
      When the flag is set, tables and related tables
      will be resolved against synonyms in all cases, meaning
      if a synonym exists for a particular table, reflection
      will use it when reflecting related tables.  This is
      stickier behavior than before which is why it's
      off by default.


      """,
    u"""
- inheritance in declarative can be disabled when sending
"inherits=None" to __mapper_args__.


""",
u"""
reverted r4315 - a basic test works the way it was and fails with this change

""",
u"""
- made some fixes to the "from_joinpoint" argument to
query.join() so that if the previous join was aliased
and this one isn't, the join still happens successfully.


""",
u"""
- adjusted the definition of "self-referential" to be
any two mappers with a common parent (this affects
whether or not aliased=True is required when joining
with Query).
      


""",
u"""
Undoing patch #994, for now; more testing needed.  Sorry.  Also modifying test for query equivalence to account for underscoring of bind variables.
""",
u"""
adding zzzeek's patch from ticket #994, which fixed virtually all remaining broken unit tests in the Oracle module
""",
u"""
bugfix: preserving remote_owner during reflecttable setup of referential integrity
""",
u"""
added a runtime-incrementing counter for default primary keys to testlib/schema for Oracle
""",
u"""
added escape kw arg to contains(), startswith(), endswith(), [ticket:791]

""",
u"""
- like() and ilike() take an optional keyword argument 
"escape=<somestring>", which is set as the escape character
using the syntax "x LIKE y ESCAPE '<somestring>'"
[ticket:993]


""",
u"""
- symbols now depickle properly
- fixed some symbol __new__ abuse

""",
u"""
typo

""",
u"""
test not supported on sqlite

""",
u"""
some fixup to one-to-many delete cascade

""",
u"""
- fixed/added coverage for various cascade scenarios
- added coverage for some extra cases in dynamic relations
- removed some unused methods from unitofwork

""",
u"""
- added support for declarative deferred(Column(...))
- changed "instrument" argument on synonym() to "descriptor", for consistency with comparable_proeprty()

""",
u"""
- Column._set_parent will complete the key==name contract for instances constructed anonymously
""",
u"""
- reST fixes
""",
u"""
mapper double checks that columns in _compile_property are in the _cols_by_table collection

""",
u"""
- Start coverage for Class.prop = Column(), promote nameless Columns
""",
u"""
- Declarative will complete setup for Columns lacking names, allows
  a more DRY syntax.

    class Foo(Base):
        __tablename__ = 'foos'
        id = Column(Integer, primary_key=True)

        """,
    u"""
- fixed order_by calculation in Query to properly alias
mapper-config'ed order_by when using select_from()


""",
u"""
- 'name' is no longer a require constructor argument for Column().  It (and .key) may now be deferred until the Column is added to a Table.

""",
u"""
- Declarative gains @synonym_for and @comparable_using decorators

""",
u"""
- Added comparable_property(), adds query Comparator behavior to regular, unmanaged Python properties
- Some aspects of MapperProperty initialization are streteched pretty thin now
  and need a refactor; will proceed with these on the user_defined_state branch

  """,
u"""
- trailing whitespace...
""",
u"""
- DEFAULT VALUES again.
""",
u"""
- fixed "cascade delete" operation of dynamic relations,
which had only been implemented for foreign-key nulling
behavior in 0.4.2 and not actual cascading deletes
[ticket:895]


""",
u"""
fix datatypes #2

""",
u"""
fix insert() to have values (supports buildbot's SQLite)

""",
u"""
- Fixed descriminator col type for poly test
""",
u"""
Issue a warning when a declarative detects a likely trailing comma: foo = Column(foo),
      """,
    u"""
- the "synonym" function is now directly usable with 
"declarative".  Pass in the decorated property using 
the "instrument" keyword argument, e.g.:
somekey = synonym('_somekey', instrument=property(g, s))
- declared_synonym deprecated

""",
u"""
Session.execute can now find binds from metadata

""",
u"""
- fixed bug which was preventing synonym() attributes
from being used with inheritance


""",
u"""
typo


""",
u"""
- fixed missing import [ticket:989]
""",
u"""
add relate(), entity() methods
""",
u"""
- fixed/covered case when using a False value as a 
polymorphic discriminator


""",
u"""
- when attributes are expired on a pending instance, an 
error will not be raised when the "refresh" action 
is triggered and returns no result


""",
u"""
- Retroactive textmate damage control
""",
u"""
Bump.
""",
u"""
more edits

""",
u"""
fix a typo....

""",
u"""
(Whoops,)
    """,
u"""
- Take broken mysql 4.1 column defaulting into account.
""",
u"""
- Don't create implicit DDL column defaults
""",
u"""
- increased assert_tabels_equal failure verbosity
""",
u"""
filled in some of the types documentation

""",
u"""
updated SQL output, fixed String/Text type

""",
u"""
reflection tests require foreign key reflection support

""",
u"""
- fix expunging of orphans with more than one parent
- move flush error for orphans from Mapper to UnitOfWork 

""",
u"""
remove redundant test_rekey() test method

""",
u"""
- Test autoload with a FK override
""",
u"""
- Added a primaryjoin= test
""",
u"""
eh, that __autoload_with__ idea was half baked.
""",
u"""
- Added __autoload__ = True for declarative
- declarative Base.__init__ is pickier about its kwargs

""",
u"""
removed the "__main__" code from below

""",
u"""
- a new super-small "declarative" extension has been added,
which allows Table and mapper() configuration to take place
inline underneath a class declaration.  This extension differs
from ActiveMapper and Elixir in that it does not redefine
any SQLAlchemy semantics at all; literal Column, Table
and relation() constructs are used to define the class 
behavior and table definition.


""",
u"""
- relation() can accept a callable for its first argument,
which returns the class to be related.  This is in place
to assist declarative packages to define relations without
classes yet being in place.


""",
u"""
- dynamic_loader() / lazy="dynamic" now accepts and uses
the order_by parameter in the same way in which it works
with relation().


""",
u"""
added sanity test for order_by

""",
u"""
Added support for vendor-extended INSERT syntax like INSERT DELAYED INTO
""",
u"""
weed whacking is not Nones

""",
u"""
- moved property._is_self_referential() to be more generalized; returns True for any mapper.isa() relationship between parent and child, and indicates that aliasing should be used for any join/correlation across the relation.  allows joins/any()/has() to work with inherited mappers referencing the parent etc.
- the original _is_self_referential() is now _refers_to_parent_table() and is only used during "direction" calculation to indicate the relation is from a single table to itself

""",
u"""
corrected assert_raises to be consistent with existing assertRaises() unittest method

""",
u"""
- added assert_raises() to TestBase class
- session.refresh() and session.expire() raise an error when 
called on instances which are not persistent within the session
- session._validate_persistent() properly raises an error for false check

""",
u"""
check the isinsert/isupdate flags before calling __process_defaults

""",
u"""
- adjusted generative.py test for revised error message
- mapper with non_primary asserts primary mapper already created
- added any()/instance compare test to query

""",
u"""
Import fixup & trailing whitespace
""",
u"""
- Synonyms riding on top of existing descriptors are now full proxies
  to those descriptors.

  """,
u"""
- constraint constructor docstring fiesta
""",
u"""
- More docs for r4223
""",
u"""
- Tweaked error messaging for unbound DDL().execute()
    """,
u"""
- Gave DDL() statements the same .bind treatment as the DML ones in r4220

""",
u"""
- whitespace/docstring/linewrap freakout

""",
u"""
- Updated exception messaging for r4220

""",
u"""
- added "bind" keyword argument to insert(), update(), delete();
.bind property is settable on those as well as select().


""",
u"""
unit test for mutable PGArray, thanks to AlexB !!!

""",
u"""
check for None

""",
u"""
- postgres PGArray is a "mutable" type by default;
when used with the ORM, mutable-style equality/
copy-on-write techniques are used to test for changes.


""",
u"""
fixed negated self-referential m2m contains(), [ticket:987]

""",
u"""
- fixed bug which was preventing UNIONS from being cloneable,
[ticket:986]


""",
u"""
fix markdown bug

""",
u"""
- repaired behavior of == and != operators at the relation()
level when compared against NULL for one-to-one and other 
relations [ticket:985]


""",
u"""
(very) minor speed optimization to ResultProxy fetchall & fetchmany methods

""",
u"""
added dispose() for StaticPool

""",
u"""
fix maddening ReST bug

""",
u"""
document with_polymorphic()

    """,
u"""
- Raise a friendly error when assigning an unmapped something (like a string) to a scalar-object attribute
""",
u"""
- state.commit() and state.commit_all() now reconcile the current dict against expired_attributes
and unset the expired flag for those attributes.  This is partially so that attributes are not 
needlessly marked as expired after a two-phase inheritance load.
- fixed bug which was introduced in 0.4.3, whereby loading an
already-persistent instance mapped with joined table inheritance
would trigger a useless "secondary" load from its joined 
table, when using the default "select" polymorphic_fetch.  
This was due to attributes being marked as expired
during its first load and not getting unmarked from the 
previous "secondary" load.  Attributes are now unexpired
based on presence in __dict__ after any load or commit
operation succeeds.


""",
u"""
add note about global metadata removed [ticket:983]

""",
u"""
- fixed bug whereby session.expire() attributes were not
loading on an polymorphically-mapped instance mapped 
by a select_table mapper.

- added query.with_polymorphic() - specifies a list
of classes which descend from the base class, which will
be added to the FROM clause of the query.  Allows subclasses
to be used within filter() criterion as well as eagerly loads
the attributes of those subclasses.

- deprecated Query methods apply_sum(), apply_max(), apply_min(),
apply_avg().  Better methodologies are coming....


""",
u"""
- setting the relation()-level order by to a column in the
many-to-many "secondary" table will now work with eager 
loading, previously the "order by" wasn't aliased against
the secondary table's alias.


""",
u"""
some cleanup of TypeDecorator, moved PickleType / Interval to the newer style for readability

""",
u"""
- postgres TIMESTAMP renders correctly [ticket:981]


""",
u"""
- implemented two-phase API for "threadlocal" engine, 
via engine.begin_twophase(), engine.prepare()
[ticket:936]


""",
u"""
- added exception wrapping/reconnect support to result set 
fetching.  Reconnect works for those databases that 
raise a catchable data error during results 
(i.e. doesn't work on MySQL) [ticket:978]


""",
u"""
silliness reduction

""",
u"""
- Invalid SQLite connection URLs now raise an error.
""",
u"""
C-u 66 C-x f M-q
""",
u"""
- the value of a bindparam() can be a callable, in which 
case it's evaluated at statement execution time to
get the value.
- expressions used in filter(), filter_by() and others,
when they make usage of a clause generated from a
relation using the identity of a child object
(e.g. filter(Parent.child==<somechild>)), evaluate
the actual primary key value of <somechild> at 
execution time so that the autoflush step of the
Query can complete, thereby populating the PK value
of <somechild> in the case that <somechild> was
pending.
- cleanup of attributes.get_committed_value() to never return
the NO_VALUE value; evaluates to None

""",
u"""
- Converted MAGICCOOKIE=object() to a little symbol implementation to ease object inspection and debugging

""",
u"""
er, ok, dont do that (reversed last change).  PG relies upon _register_clean for
new PK switch even if no SQL is emitted.

""",
u"""
dont treat "listonly" objects as newly clean

""",
u"""
- preventive code against a potential lost-reference 
bug in flush()


    """,
u"""
- added a new "higher level" operator called "of_type()" - 
used in join() as well as with any() and has(), qualifies
the subclass which will be used in filter criterion, 
e.g.: 

query.filter(Company.employees.of_type(Engineer).
  any(Engineer.name=='foo')), 

query.join(Company.employees.of_type(Engineer)).
  filter(Engineer.name=='foo')


  """,
u"""
- fixed potential generative bug when the same Query was
used to generate multiple Query objects using join().


""",
u"""
- can again create aliases of selects against textual
FROM clauses, [ticket:975]


""",
u"""
- modernized cascade.py tests
- your cries have been heard:  removing a pending item
from an attribute or collection with delete-orphan 
expunges the item from the session; no FlushError is raised.  
Note that if you session.save()'ed the pending item 
explicitly, the attribute/collection removal still knocks 
it out.


""",
u"""
get basic compilation working for [ticket:972]

""",
u"""
- any(), has(), contains(), attribute level == and != now
work properly with self-referential relations - the clause
inside the EXISTS is aliased on the "remote" side to
distinguish it from the parent table.


""",
u"""
- remove some old cruft
- deprecate ancient engine_descriptors() method

""",
u"""
Bump.
""",
u"""
fixing recent schema.py changes to work with oracle 'owner' attribute

""",
u"""
- comment typo
""",
u"""
- Made testlib's --unhashable and r3935's set changes play nice
- A bonus overhead reduction for IdentitySet instances

""",
u"""
- Corrected __eq__ pragma drift.
""",
u"""
Restore 2.3 compat for the sharding test
""",
u"""
fixed (still uncovered) incorrect variable name...

""",
u"""
- Fixed a couple pyflakes, cleaned up imports & whitespace
""",
u"""
MSSQL now compiles func.now() to CURRENT_TIMESTAMP
""",
u"""
- fixed bug in result proxy where anonymously generated
column labels would not be accessible using their straight
string name


""",
u"""
Added EXEC to MSSQL _is_select regexp; should now detect row-returning stored procedures
Added experimental implementation of limit/offset using row_number()
    """,
u"""
a TODO comment

""",
u"""
0.4.3 edits
""",
u"""
- fixed bug introduced in r4070 where union() and other compound selects would not get 
an OID column if it only contained one selectable element, due to missing return in _proxy_column()
- visit_column() calls itself to render a primary key col being used as the interpretation of the oid col instead of relying upon broken partial logic

""",
u"""
add pk cols to assocaition table

""",
u"""
- Added two new vertical dict mapping examples.
""",
u"""
- added expire_all() method to Session.  Calls expire()
for all persistent instances.  This is handy in conjunction
with .....

- instances which have been partially or fully expired
will have their expired attributes populated during a regular
Query operation which affects those objects, preventing
a needless second SQL statement for each instance.


""",
u"""
- Fixed .get(<int>) of a String PK (exposed by pg 8.3)
    """,
u"""
- updated the naming scheme of the base test classes in test/testlib/testing.py; 
tests extend from either TestBase or ORMTest, using additional mixins for 
special assertion methods as needed

""",
u"""
- Table columns and constraints can be overridden on a 
an existing table (such as a table that was already
reflected) using the 'useexisting=True' flag, which now
takes into account the arguments passed along with it.
- fixed one element of [ticket:910]
- refactored reflection test

""",
u"""
- Better error messaging on failed collection bulk-assignments
""",
u"""
- Note about future CollectionAttributeImp.collection_intrface removal + whitespace cleanup.
""",
u"""
- Determine the basic collection interface dynamically when adapting a collection to an interable

""",
u"""
added info on foreign_keys attribute

""",
u"""
- lazy loader can now handle a join condition where the "bound"
column (i.e. the one that gets the parent id sent as a bind
parameter) appears more than once in the join condition.
Specifically this allows the common task of a relation()
which contains a parent-correlated subquery, such as "select
only the most recent child item". [ticket:946]
- col_is_part_of_mappings made more strict, seems to be OK
with tests
- memusage will dump out the size list in an assertion fail

""",
u"""
heisenbug in aisle 3

(when db.dispose is called in unitofwork test with sqlite, the first test that runs in memusage grows by two gc'ed objects on every iteration; then the problem vanishes.  doesnt matter what test runs in memusage.  doing a dispose() in memusage solves the problem also.  screwing wiht the mechanics of engine.dispose() only fix it when both the pool.dispose() *and* the pool.ressurect() are disabled.  its just a subtle python/pysqlite bug afaict)

""",
u"""
- added generative where(<criterion>) method to delete() 
and update() constructs which return a new object with
criterion joined to existing criterion via AND, just
like select().where().
- compile assertions use assertEquals()

    """,
u"""
- Added deferrability support to constraints

""",
u"""
- psycopg2 can raise un-str()able exceptions; don't croak when trying to log them

""",
u"""
Fix: deletes with schemas on MSSQL 2000 [ticket:967]
""",
u"""
test for session close efficiency

""",
u"""
Fix some mssql unit tests
""",
u"""
Strip schema from access tables
""",
u"""
Avoid using common keywords as field names: the test executes literal selects
""",
u"""
check for unicode first before encoding

""",
u"""
unit-of-work flush didn't close the failed transaction when the session was not in a transaction and commiting the transaction failed.

""",
u"""
- Some more reST docstring corrections
""",
u"""
- clean up the print version of the docs a bit [ticket:745]
""",
u"""
- A few quick docstring typo fixes, including [ticket:766]
""",
u"""
C-u 66 C-x f M-q
""",
u"""
ChangeLog for r4115
""",
u"""
- Enabled schema support on SQLite, added the temporary table namespace to table name reflection
- TODO: add sqlite to the standard alternate schema tests. a little tricky, because unlike CREATE SCHEMA, an ATTACH DATABASE won't survive a pool dispose...

""",
u"""
- doc edits- thanks asmodai! [ticket:906]

""",
u"""
better that it doesn't get a scalar loader callable

""",
u"""
expire with synonyms [ticket:964]

""",
u"""
- Autodetect mysql's ANSI_QUOTES mode, sometimes. [ticket:845]
  The dialect needs a hook run on first pool connect to detect this most of
  the time, and a refactor with Dialect-per-Connection to get it right all of
  the time. (It's a connection-session scoped setting with dialect-modifying
  behavior)

  """,
u"""
hmmm.
""",
u"""
- Added free-form `DDL` statements, can be executed standalone or tied to the DDL create/drop lifecycle of Tables and MetaData. [ticket:903]
- Added DDL event hooks, triggers callables before and after create / drop.

""",
u"""
*more* tweaks to avoid DEFAULT VALUES on sqlite

""",
u"""
lock in replacing '%' with '%%'

""",
u"""
- add dummy column to appease older SQLite verisons in unicode.py
- add test "escape_literal_column" comiler method to start addressing literal '%' character

""",
u"""
- ColumnDefault callables can now be any kind of compliant callable, previously only actual functions were allowed.

""",
u"""
forcibly clean out _sessions, _mapper_registry at test start to eliminate leftovers from other unit tests (from other test scripts) still stored in memory

""",
u"""
add some extra assertions to ensure all mappers are gone after clear_mappers() (for [ticket:963])

    """,
u"""
- fixed reflection of Time columns on sqlite

""",
u"""
- some consolidation of tests in select.py, moved
other tests to more specific modules
- added "now()" as a generic function; on SQLite and 
Oracle compiles as "CURRENT_TIMESTAMP"; "now()"
on all others [ticket:943]

""",
u"""
- Workaround for datetime quirk, LHS comparisons to SA expressions now work.
""",
u"""
- Friendlier exception messages for unbound, implicit execution
- Implicit binding failures now raise UnboundExecutionError

""",
u"""
- added "autocommit=True" kwarg to select() and text(),
as well as generative autocommit() method on select(); 
for statements which modify the database through some 
user-defined means other than the usual INSERT/UPDATE/
DELETE etc., this flag will enable "autocommit" behavior
during execution if no transaction is in progress 
[ticket:915]


""",
u"""
- implemented RowProxy.__ne__ [ticket:945], thanks knutroy
- test coverage for same

""",
u"""
- the startswith(), endswith(), and contains() operators
now concatenate the wildcard operator with the given
operand in SQL, i.e. "'%' || <bindparam>" in all cases,
accept text('something') operands properly [ticket:962]

- cast() accepts text('something') and other non-literal
operands properly [ticket:962]



""",
u"""
escapedefaultstest passes on everything

""",
u"""
moved default escaping test to its own test so oracle gets it

""",
u"""
- Oracle and others properly encode SQL used for defaults
like sequences, etc., even if no unicode idents are used
since identifier preparer may return a cached unicode
identifier.


""",
u"""
docstring fix

""",
u"""
- next release will be 0.4.3
- fixed merge() collection-doubling bug when merging 
transient entities with backref'ed collections.
[ticket:961]
- merge(dont_load=True) does not accept transient 
entities, this is in continuation with the fact that
merge(dont_load=True) does not accept any "dirty" 
objects either.


""",
u"""
- "Passive defaults" and other "inline" defaults can now
be loaded during a flush() call if needed; in particular,
this allows constructing relations() where a foreign key
column references a server-side-generated, non-primary-key
column. [ticket:954]


""",
u"""
- Added a simple @future test marker.
""",
u"""
- Fixed little think-o in fails_if
""",
u"""
- Fixed bug in polymorphic inheritance where incorrect
exception is raised when base polymorphic_on
column does not correspond to any columns within 
the local selectable of an inheriting mapper more 
than one level deep


""",
u"""
encourage usage of union() and other composites as module-level

""",
u"""
- added standalone "query" class attribute generated
by a scoped_session.  This provides MyClass.query
without using Session.mapper.  Use via:

MyClass.query = Session.query_property()


    """,
u"""
- Ignore jython debris

""",
u"""
- Flipped join order of __radd__ on association proxied lists.
""",
u"""
- IdentitySet binops no longer accept plain sets.
""",
u"""
A little clarity tweak to r4093
""",
u"""
Corrected behavior of get_cls_kwargs and friends

""",
u"""
added an intro for the code sample so that its not construed as a "synopsis"

""",
u"""
- query.join() can also accept tuples of attribute
name/some selectable as arguments.  This allows
construction of joins *from* subclasses of a 
polymorphic relation, i.e.:

query(Company).\
join(
  [('employees', people.join(engineer)), Engineer.name]
)


""",
u"""
Added notes about 2.3 improvements
""",
u"""
Edits
""",
u"""
whups, args in wrong order

""",
u"""
more descriptive error message for m2m concurrency error

""",
u"""
more capability added to reduce_columns

""",
u"""
- Migrated zoomark to profiling.function_call_count(), tightened up the numbers.  Is there variation by platform too?  Buildbots will tell...
""",
u"""
rein in r3840 find and replace rampage
""",
u"""
- 2.3 fixup part three: 100% on postgres, mysql
""",
u"""
- Removed some test bogosity
""",
u"""
- Cover 2.3 Decimal fallback

""",
u"""
- 2.3 fixup, part two: 100% passing for sqlite
  - added 2.4-style binops to util.Set on 2.3
  - OrderedSets pickle on 2.3
  - more lib/sqlalchemy set vs Set corrections
  - fixed InstrumentedSet.discard for 2.3
  - set, sorted compatibility for test suite
- added testing.fails_if decorator


""",
u"""
clean up a little close() silliness

""",
u"""
factor create_row_adapter into sql.util.row_adapter

""",
u"""
further clarification on transaction state

""",
u"""
fix rollback behavior with transaction context manager and failed two phase transactions

""",
u"""
example of using try-catch to do transaction commit/rollback was wrong in the docs

""",
u"""
- parent transactions weren't started on the connection when adding a connection to a nested session transaction.
- session.transaction now always refers to the innermost active transaction, even when commit/rollback are called directly on the session transaction object.
- when preparing a two-phase transaction fails on one connection all the connections are rolled back.
- two phase transactions can now be prepared.
- session.close() didn't close all transactions when nested transactions were used.
- rollback() previously erroneously set the current transaction directly to the parent of the transaction that could be rolled back to.
- autoflush for commit() wasn't flushing for simple subtransactions.

""",
u"""
- Restored 2.3 compat. in lib/sqlalchemy
- Part one of test suite fixes to run on 2.3
  Lots of failures still around sets; sets.Set differs from __builtin__.set
  particularly in the binops. We depend on set extensively now and may need to
  provide a corrected sets.Set subclass on 2.3.

  """,
u"""
- Added source transformation framework for non-2.4 parser implementations
- test/clone.py can create and update (transformed) copies of the test suite
- Added Python 2.4 decorator -> 2.3 source transform

""",
u"""
- Oracle assembles the correct columns in the result set
  column mapping when generating a LIMIT/OFFSET subquery,
  allows columns to map properly to result sets even
  if long-name truncation kicks in [ticket:941]


  """,
u"""
- some expression fixup:
- the '.c.' attribute on a selectable now gets an
entry for every column expression in its columns
clause; previously, "unnamed" columns like functions
and CASE statements weren't getting put there.  Now
they will, using their full string representation
if no 'name' is available.  
- The anonymous 'label' generated for otherwise
unlabeled functions and expressions now propagates 
outwards at compile time for expressions like 
select([select([func.foo()])])
- a CompositeSelect, i.e. any union(), union_all(),
intersect(), etc. now asserts that each selectable
contains the same number of columns.  This conforms
to the corresponding SQL requirement.
- building on the above ideas, CompositeSelects
now build up their ".c." collection based on
the names present in the first selectable only;
corresponding_column() now works fully for all 
embedded selectables.


""",
u"""
check for session is none, [ticket:940]

""",
u"""
Updated bit about coverage.py
""",
u"""
- dynamic relations, when referenced, create a strong
reference to the parent object so that the query
still has a parent to call against even if the 
parent is only created (and otherwise dereferenced)
within the scope of a single expression [ticket:938]


""",
u"""
- default the root logger level only if unset

""",
u"""
maintain the ordering of the given collection of columns when reducing so that primary key collections remain 
ordered the same as in the mapped table

""",
u"""
avoid unnecessary mapper.extension copy

""",
u"""
finally, a really straightforward reduce() method which reduces cols
to the minimal set for every test case I can come up with, and 
now replaces all the cruft in Mapper._compile_pks() as well as 
Join.__init_primary_key().  mappers can now handle aliased selects
and figure out the correct PKs pretty well [ticket:933]

""",
u"""
- select_table mapper turns straight join into aliased select + custom PK, to allow
joins onto select_table mappers
- starting a generalized reduce_columns func

""",
u"""
added more (failing) tests to query, will need to fix [ticket:932] [ticket:933]

""",
u"""
- query.join() can now accept class-mapped attributes
as arguments, which can be used in place or in any
combination with strings.  In particular this allows 
construction of joins to subclasses on a polymorphic 
relation, i.e. 
query(Company).join(['employees', Engineer.name]), 
etc.


""",
u"""
- applying some refined versions of the ideas in the smarter_polymorphic
branch
- slowly moving Query towards a central "aliasing" paradigm which merges
the aliasing of polymorphic mappers to aliasing against arbitrary select_from(),
to the eventual goal of polymorphic mappers which can also eagerload other
relations
- supports many more join() scenarios involving polymorphic mappers in
most configurations
- PropertyAliasedClauses doesn't need "path", EagerLoader doesn't need to
guess about "towrap"

""",
u"""
- _get_equivalents() converted into a lazy-initializing property; Query was calling it
for polymorphic loads which is really expensive
- surrogate_mapper adapts the given order_by, so that order_by can be against the mapped
table and is usable for sub-mappers as well.  Query properly calls select_mapper.order_by.

""",
u"""
- testbase is gone, replaced by testenv
- Importing testenv has no side effects- explicit functions provide similar behavior to the old immediate behavior of testbase
- testing.db has the configured db
- Fixed up the perf/* scripts


                      """,
                    u"""
- Undeclared SAWarnings are now fatal to tests as well.
- Fixed typo that was killing runs of individual named tests.

""",
u"""
fixed NOT ILIKE

""",
u"""
- added "ilike()" operator to column operations. 
compiles to ILIKE on postgres, lower(x) LIKE lower(y)
on all others [ticket:727]


""",
u"""
Reverted to False Firebird's supports_sane_rowcount
Slipped in: even if it seems it could be set to True, I'm still testing the rowcount affair
""",
u"""
Try to reflect also the Sequence on the PK under Firebird
""",
u"""
- Warnings are now issued as SAWarning instead of RuntimeWarning; util.warn() wraps this up.
- SADeprecationWarning has moved to exceptions. An alias remains in logging until 0.5.

""",
u"""
Include column name in length-less String warning (more [ticket:912])

""",
u"""
- unit test for r4048

""",
u"""
- added a mapper() flag "eager_defaults"; when set to
True, defaults that are generated during an INSERT
or UPDATE operation are post-fetched immediately, 
instead of being deferred until later.  This mimics
the old 0.3 behavior.


""",
u"""
- added extra fk override test
- proper error message is raised when trying to 
access expired instance attributes with no session
present


""",
u"""
Recognize another Firebird exception in dialect.is_disconnect()
""",
u"""
- finally added PGMacAddr type to postgres 
[ticket:580]


""",
u"""
converted tests to use remote_side and foreign_keys.  but...wow these are hard tests..

""",
u"""
Reworked r4042- undeclared deprecation warnings are now *fatal* to tests.  No surprises.

""",
u"""
test suite deprecation rampage
""",
u"""
bump.
""",
u"""
formatting, added UnicodeText

""",
u"""
Silenced deprecation warnings when testing deprecated extensions...

""",
u"""
Added explicit length to more testing String columns.

""",
u"""
re-bump
""",
u"""
Added UnicodeText alias
""",
u"""
- fixed bug with session.dirty when using "mutable scalars" 
(such as PickleTypes)

- added a more descriptive error message when flushing on a 
relation() that has non-locally-mapped columns in its primary or
secondary join condition


""",
u"""
redid the _for_ddl String/Text deprecation warning correctly [ticket:912]

""",
u"""
- fixed bug in union() so that select() statements which don't derive
from FromClause objects can be unioned


""",
u"""
- Text type is properly exported now and does not raise a warning
on DDL create


""",
u"""
Fixed reflection of mysql empty string column defaults.

""",
u"""
bump

""",
u"""
logged [ticket:923] fix

""",
u"""
Fix for ticket [923]
""",
u"""
- fixed an attribute history bug whereby assigning a new collection
to a collection-based attribute which already had pending changes
would generate incorrect history [ticket:922]

- fixed delete-orphan cascade bug whereby setting the same
object twice to a scalar attribute could log it as an orphan
[ticket:925]
- generative select.order_by(None) / group_by(None) was not managing to 
reset order by/group by criterion, fixed [ticket:924]


""",
u"""
- suppressing *all* errors in InstanceState.__cleanup() now.  


""",
u"""
- fixed bug which could occur with polymorphic "union" mapper
which falls back to "deferred" loading of inheriting tables

- the "columns" collection on a mapper/mapped class (i.e. 'c')
is against the mapped table, not the select_table in the 
case of polymorphic "union" loading (this shouldn't be 
noticeable)


""",
u"""
- synonyms can now be created against props that don't exist yet,
which are later added via add_property().  This commonly includes
backrefs. (i.e. you can make synonyms for backrefs without
worrying about the order of operations) [ticket:919]


""",
u"""
- changed name of TEXT to Text since its a "generic" type; TEXT name is
deprecated until 0.5.  The "upgrading" behavior of String to Text 
when no length is present is also deprecated until 0.5; will issue a
warning when used for CREATE TABLE statements (String with no length
for SQL expression purposes is still fine) [ticket:912]


""",
u"""
Added 'function_call_count' assertion decorator.  The full-suite vs. isolated run call count discrepancy needs to be ironed out before this can be applied to zoomark.

""",
u"""
Updates
""",
u"""
Added lots o' info.

""",
u"""
More overloads: fix cascades for += on a list relation, added operator support to association proxied lists.

""",
u"""
bump.
""",
u"""
calling this 0.4.2a

""",
u"""
- fixed fairly critical bug whereby the same instance could be listed
more than once in the unitofwork.new collection; most typically
reproduced when using a combination of inheriting mappers and 
ScopedSession.mapper, as the multiple __init__ calls per instance
could save() the object with distinct _state objects


""",
u"""
Experimental: modestly more informative repr() for some expressions (using .description)

    """,
u"""
Migrated a few in-function 'from x import y' to the 'global x; if x is None' style.

""",
u"""
Refined bulk-assignment aspects of the r3999 in-place collection operator fix. Also? r4000!

""",
u"""
Fixed in-place set mutation operator support [ticket:920]

""",
u"""
Added REPLACE statements to mysql autocommit list.

""",
u"""
func unittest fix

""",
u"""
fix select tests for labeled functions

""",
u"""
add anonymous labels to function calls

""",
u"""
fix not calling the result processor of PGArray subtypes. (a rather embarrasing copypaste error) [ticket:913]

""",
u"""
- added very rudimentary yielding iterator behavior to Query.  Call
query.yield_per(<number of rows>) and evaluate the Query in an 
iterative context; every collection of N rows will be packaged up
and yielded.  Use this method with extreme caution since it does 
not attempt to reconcile eagerly loaded collections across
result batch boundaries, nor will it behave nicely if the same
instance occurs in more than one batch.  This means that an eagerly 
loaded collection will get cleared out if it's referenced in more than
one batch, and in all cases attributes will be overwritten on instances
that occur in more than one batch.


""",
u"""
fix weakref issue seen on one buildbot test

""",
u"""
- further fix to new TypeDecorator, so that subclasses of TypeDecorators work properly
- _handle_dbapi_exception() usage changed so that unwrapped exceptions can be rethrown with the original stack trace

""",
u"""
happy new year

""",
u"""
fix to new TypeDecorator

""",
u"""
fix up oracle handling of LOB/string [ticket:902], slight fixes to defaults.py but we
will need to fix up result-type handling some more

""",
u"""
filter() criterion takes mapper equivalent_columns into account when it adapts to select_table.  more to come in [ticket:917] .

""",
u"""
remove "is None" from boolean tests

""",
u"""
limit scope of try/except

""",
u"""
use long for query runid counter

""",
u"""
- added is_disconnect() support for oracle
- fixed _handle_dbapi_error to detect endless loops, doesn't call rollback/cursor.close 
etc. in case of disconnect

""",
u"""
- mapped classes which extend "object" and do not provide an 
__init__() method will now raise TypeError if non-empty *args 
or **kwargs are present at instance construction time (and are 
not consumed by any extensions such as the scoped_session mapper), 
consistent with the behavior of normal Python classes [ticket:908]


""",
u"""
- fixed Query bug when filter_by() compares a relation against None
[ticket:899]


""",
u"""
- MapperExtension.before_update() and after_update() are now called
symmetrically; previously, an instance that had no modified column
attributes (but had a relation() modification) could be called with 
before_update() but not after_update() [ticket:907]


""",
u"""
- fixed session.refresh() with instance that has custom entity_name 
[ticket:914]


""",
u"""
some rudimentary fixes to get instance-level deferreds/lazy loads to transfer over on merge()

    """,
u"""
cruft ! who knew

""",
u"""
added assertion for expiry's current inability to detect a PK switch in the DB

""",
u"""
- disabled the "populate expired/deferred attributes as we come across them" functionality in mapper._instance(), as its not completed, doesn't properly handle mutable scalar attributes, and has poor test coverage

""",
u"""
mass load wont overwrite modified expired attributes

""",
u"""
broke up various class-level mapper/instance fanfare into class_level_loader; load-time setup_loader just returns a loader object with no checks

""",
u"""
- reworked all lazy/deferred/expired callables to be 
serializable class instances, added pickling tests
- cleaned up "deferred" polymorphic system so that the
mapper handles it entirely
- columns which are missing from a Query's select statement
now get automatically deferred during load.


""",
u"""
- inheriting mappers now inherit the MapperExtensions of their parent
mapper directly, so that all methods for a particular MapperExtension
are called for subclasses as well.  As always, any MapperExtension 
can return either EXT_CONTINUE to continue extension processing
or EXT_STOP to stop processing.  The order of mapper resolution is:
<extensions declared on the classes mapper> <extensions declared on the
classes' parent mapper> <globally declared extensions>.

Note that if you instantiate the same extension class separately 
and then apply it individually for two mappers in the same inheritance 
chain, the extension will be applied twice to the inheriting class,
and each method will be called twice.

To apply a mapper extension explicitly to each inheriting class but
have each method called only once per operation, use the same 
instance of the extension for both mappers.
[ticket:490]


""",
u"""
- sqlite SLDate type will not erroneously render "microseconds" portion 
of a datetime or time object when sent to the DB.


""",
u"""
forgot CHANGES
""",
u"""
Fix for autoload of non-identity PK integer columns [824]
Better datetime checking/conversion for pyodbc adodbapi [842]
Fix for autoloading schema-qualified tables [901]
Convert_unicode support for all dialects [839]
 


""",
u"""
- Re-raise SystemExit et al in _ConnectionRecord.close
- Little code cleanup- decreased verbosity of string formatting.

""",
u"""
- auto-reconnect support improved; a Connection can now automatically
reconnect after its underlying connection is invalidated, without
needing to connect() again from the engine.  This allows an ORM session
bound to a single Connection to not need a reconnect.
Open transactions on the Connection must be rolled back after an invalidation 
of the underlying connection else an error is raised.  Also fixed
bug where disconnect detect was not being called for cursor(), rollback(),
or commit().


""",
u"""
Fix the unpacking of the refered table name under Firebird
This fixes a little glitch introduced in [3959], in case of "implicit FKs"
(that is, {{{ForeignKey("orders")}}}, where the field(s) is missing).
""",
u"""
introductory docstring bonanza

""",
u"""
Apply default cascade rules for firebird self-ref ForeignKeys.

""",
u"""
a little pre-lunch decrufting and cleanup

""",
u"""
Use an explicit ordering in the query
""",
u"""
Add Firebird to the list of DBs that needs explicit sequences
""",
u"""
get most oracle tests in sql working again....

""",
u"""
- cleanup; lambdas removed from properties; properties mirror same-named functions (more like eventual decorator syntax); remove some old methods, factor out some "raiseerr" ugliness to outer lying functions.
- corresponding_column() integrates "require_embedded" flag with other set arithmetic

""",
u"""
- select().as_scalar() will raise an exception if the select does not have
exactly one expression in its columns clause.
- added "helper exception" to select.type access, generic functions raise
the chance of this happening
- a slight behavioral change to attributes is, del'ing an attribute
does *not* cause the lazyloader of that attribute to fire off again;
the "del" makes the effective value of the attribute "None".  To
re-trigger the "loader" for an attribute, use 
session.expire(instance, [attrname]).
- fix ormtutorial for IS NULL

""",
u"""
fixed del history

""",
u"""
after_update called with state.obj()

    """,
u"""
- more fixes to the LIMIT/OFFSET aliasing applied with Query + eagerloads,
in this case when mapped against a select statement [ticket:904]
- _hide_froms logic in expression totally localized to Join class, including search through previous clone sources
- removed "stop_on" from main visitors, not used
- "stop_on" in AbstractClauseProcessor part of constructor, ClauseAdapter sets it up based on given clause
- fixes to is_derived_from() to take previous clone sources into account, Alias takes self + cloned sources into account. this is ultimately what the #904 bug was.

""",
u"""
Fix bad example of Firebird test DB
Use an absolute path rather than a relative one, and the out-of-the-box
sysdba password. This is just to avoid confusing new testers, that should
add a db.firebird entry in their ~/satest.cfg anyway.
""",
u"""
moved hide_froms and aggregate_hide_froms to be only on FromClause

""",
u"""
Revert to use default poolclass under Firebird
This partially reverts [3562] and instead documents the problem suggesting
a possible workaround. For the tests, the occurence of the problem is
largely reduced by using a TCP connection (that is, 'localhost:/some/file.fdb'
instead of '/some/file.fdb')
""",
u"""
Remove some spurious spaces
""",
u"""
Fixed minor reST issue
""",
u"""
Documentation markup and a few typos
""",
u"""
Implemented FBDialect.server_version_info()
    """,
u"""
oof...unicode object still needs to return the value if it just warned...

""",
u"""
oof, history on collections were wrong. fixed byroot_tree test as well

""",
u"""
- simplified _mapper_registry further.  its now just a weakkeydict of mapper->True, stores 
all mappers including non primaries, and is strictly used for the list of "to compile/dispose".
- all global references are now weak referencing.  if you del a mapped class and any dependent classes, 
its mapper and all dependencies fall out of scope.
- attributes.py still had issues which were barely covered by tests.  added way more tests (coverage.py still says 71%, doh)
fixed things, took out unnecessary commit to states.  attribute history is also asserted for ordering.

""",
u"""
added an inheritance test

""",
u"""
Firebird module documentation
""",
u"""
correction...
""",
u"""
try to bang mysql tests to work

""",
u"""
- merged instances_yields branch r3908:3934, minus the "yield" part which remains slightly problematic
- cleanup of mapper._instance, query.instances().  mapper identifies objects which are part of the
current load using a app-unique id on the query context.
- attributes refactor; attributes now mostly use copy-on-modify instead of copy-on-load behavior, 
simplified get_history(), added a new set of tests
- fixes to OrderedSet such that difference(), intersection() and others can accept an iterator
- OrderedIdentitySet passes in OrderedSet to the IdentitySet superclass for usage in difference/intersection/etc. operations so that these methods actually work with ordering behavior.
- query.order_by() takes into account aliased joins, i.e.  query.join('orders', aliased=True).order_by(Order.id)
- cleanup etc.


""",
u"""
- Raise an error when assigning a bogusly keyed dictionary to one of the builtin dict-based collection types [ticket:886]
- Collections gain a @converter framework for flexible validation and adaptation of bulk assignment
- Bogus bulk assignments now raise TypeError instead of exceptions.ArgumentError

""",
u"""
Fixed some __repr__'s attempting to %d their not-yet-assigned primary key ids.

""",
u"""
Firebird does use qmark style params
""",
u"""
Use the external strlen UDF for func.length() under Firebird
""",
u"""
- Removed @testing.supported.  Dialects in development or maintained outside
  the tree can now run the full suite of tests out of the box.
- Migrated most @supported to @fails_on, @fails_on_everything_but, or (last
  resort) @unsupported.  @fails_on revealed a slew of bogus test skippage,
  which was corrected.
- Added @fails_on_everything_but.  Yes, the first usage *was*
  "fails_on_everything_but('postgres')".  How did you guess!
- Migrated @supported in dialect/* to the new test-class attribute __only_on__.
- Test classes can also have __unsupported_on__ and __excluded_on__.


""",
u"""
Disabled some tests with INTERSECT, not handled by Firebird
""",
u"""
Use an external UDF to implement the mod operator under Firebird
""",
u"""
bug fixes

- the call to self.get() in get_committed_state was missing a required parameter, rendered sqlalchemy unusable in certain situations

- fixed a large bug in dynamic_loader() where the query criterion wasn't generated correctly if other relations existed to dynamic_loader's argument
""",
u"""
Some code-level docs for r3916

""",
u"""
implemented many-to-one comparisons to None generate <column> IS NULL, with column on the left side in all cases

""",
u"""
New simple test for Dialect.has_sequence()
""",
u"""
- on mysql, emit inner joins as 'INNER JOIN ... ON' (for version 3.23) 

""",
u"""
Reflect Firebird PassiveDefaults
 - column's default values are properly reflected (also those coming from DOMAINs)
 - implemented .has_sequence()
 - fix type on FK reflection
 """,
u"""
Cosmetic changes to the Firebird reflection queries.
This brings them more consistent with the syntax of the statements generated by SA,
using lowercase field names.
""",
u"""
- eagerload(), lazyload(), eagerload_all() take an optional 
second class-or-mapper argument, which will select the mapper
to apply the option towards.  This can select among other
mappers which were added using add_entity().  

- eagerloading will work with mappers added via add_entity().
  


""",
u"""
- fix to cascades on polymorphic relations, such that cascades
from an object to a polymorphic collection continue cascading 
along the set of attributes specific to each element in the collection.


""",
u"""
comment

""",
u"""
refresh_instance becomes an InstanceState so boolean tests are OK

""",
u"""
- more query tests
- trying to refine some of the adaptation stuff
- query.from_statement() wont allow further generative criterion
- added a warning to columncollection when selectable is formed with
conflicting columns (only in the col export phase)
- some method rearrangement on schema/columncollection....
- property conflicting relation warning doesnt raise for concrete

""",
u"""
- Query.select_from() now replaces all existing FROM criterion with
the given argument; the previous behavior of constructing a list
of FROM clauses was generally not useful as is required 
filter() calls to create join criterion, and new tables introduced
within filter() already add themselves to the FROM clause.  The
new behavior allows not just joins from the main table, but select 
statements as well.  Filter criterion, order bys, eager load
clauses will be "aliased" against the given statement.


""",
u"""
Better reflection of Firebird data types.
Instead of relying on internal numeric code, lookup the associated real
name. This has the extra benefit of properly handling of DOMAINs.
""",
u"""
fix...

""",
u"""
add pydoc for from_statement().

""",
u"""
- added a warning when a relation() is added to an inheriting mapper that is present on a super-mapper; multiple DependencyProcessors are not expected during the flush process
- found an uncovered line in uow, was "covered" by one particular breaking test

""",
u"""
add some updates too

""",
u"""
- added a test for boolean saves/retrieves

""",
u"""
- fix up the fixtures comparator 
- strengthened memory profiling test

""",
u"""
only report true for source change if added + deleted, dont pick up inserts

""",
u"""
mapper uses attributes to get non-cached history

""",
u"""
remove redundant identity map set

""",
u"""
- mutable primary key support is added. primary key columns can be
changed freely, and the identity of the instance will change upon
flush. In addition, update cascades of foreign key referents (primary
key or not) along relations are supported, either in tandem with the
database's ON UPDATE CASCADE (required for DB's like Postgres) or
issued directly by the ORM in the form of UPDATE statements, by setting
the flag "passive_cascades=False".


""",
u"""
- added new methods to TypeDecorator, process_bind_param() and
process_result_value(), which automatically take advantage of the processing
of the underlying type.  Ideal for using with Unicode or Pickletype.
TypeDecorator should now be the primary way to augment the behavior of any
existing type including other TypeDecorator subclasses such as PickleType.


""",
u"""
some updates, remove an old test (really crufty old stuff here)

    """,
u"""
[ticket:888] continued, synonym add_prop

""",
u"""
ok found it

""",
u"""
fixed test which didnt pass along 'allitems' collection to the sort...

""",
u"""
- flush() refactor merged from uow_nontree branch r3871-r3885
- topological.py cleaned up, presents three public facing functions which
return list/tuple based structures, without exposing any internals.  only
the third function returns the "hierarchical" structure.  when results
include "cycles" or "child" items, 2- or 3- tuples are used to represent
results.
- unitofwork uses InstanceState almost exclusively now.  new and deleted lists
are now dicts which ref the actual object to provide a strong ref for the
duration that they're in those lists.  IdentitySet is only used for the public
facing versions of "new" and "deleted".
- unitofwork topological sort no longer uses the "hierarchical" version of the sort
for the base sort, only for the "per-object" secondary sort where it still
helps to group non-dependent operations together and provides expected insert 
order.  the default sort deals with UOWTasks in a straight list and is greatly
simplified.  Tests all pass but need to see if svilen's stuff still works,
one block of code in _sort_cyclical_dependencies() seems to not be needed anywhere 
but i definitely put it there for a reason at some point; if not hopefully we 
can derive more test coverage from that.
- the UOWEventHandler is only applied to object-storing attributes, not 
scalar (i.e. column-based) ones.  cuts out a ton of overhead when setting
non-object based attributes.
- InstanceState also used throughout the flush process, i.e. dependency.py,
mapper.save_obj()/delete_obj(), sync.execute() all expect InstanceState objects
in most cases now.
- mapper/property cascade_iterator() takes InstanceState as its argument,
but still returns lists of object instances so that they are not dereferenced.
- a few tricks needed when dealing with InstanceState, i.e. when loading a list 
of items that are possibly fresh from the DB, you *have* to get the actual objects
into a strong-referencing datastructure else they fall out of scope immediately.
dependency.py caches lists of dependent objects which it loads now (i.e. history
collections).
- AttributeHistory is gone, replaced by a function that returns a 3-tuple of
added, unchanged, deleted.  these collections still reference the object
instances directly for the strong-referencing reasons mentiontioned, but
it uses less IdentitySet logic to generate.


""",
u"""
changed the anonymous numbering scheme to be more appealing
got tests running

""",
u"""
corrected for current output...

""",
u"""
added a mention about `eagerload_all()` [ticket:897]

""",
u"""
mapper.instances() is deprecated

""",
u"""
a little refinement to topological options, more to come

""",
u"""
fix to unique bind params, you *can* use the same unique bindparam multiple times 
in a statement.  the collision check is strictly detecting non-unique's that happen to have
the same name.

""",
u"""
- also with dynamic, implemented correct count() behavior as well
as other helper methods.


""",
u"""
- added "cascade delete" behavior to "dynamic" relations just like
that of regular relations.  if passive_deletes flag (also just added)
is not set, a delete of the parent item will trigger a full load of 
the child items so that they can be deleted or updated accordingly.


""",
u"""
fixed key error when no pks could be located

""",
u"""
- generation of "unique" bind parameters has been simplified to use the same
"unique identifier" mechanisms as everything else.  This doesn't affect
user code, except any code that might have been hardcoded against the generated
names.  Generated bind params now have the form "<paramname>_<num>",
whereas before only the second bind of the same name would have this form.

- bindparam() objects themselves can be used as keys for execute(), i.e.
statement.execute({bind1:'foo', bind2:'bar'})


""",
u"""
warn if query.get() used with existing criterion

""",
u"""
- query.get() and query.load() do not take existing filter or other
criterion into account; these methods *always* look up the given id
in the database or return the current instance from the identity map, 
disregarding any existing filter, join, group_by or other criterion
which has been configured. [ticket:893]


""",
u"""
assert_unicode=True replaced with default of assert_unicode='warn'

""",
u"""
- ordering of cols in pks_by_table and cols_by_table is significant; 
particularly for pks_by_table the ordering is expected to match the ordering
of pk columns in the table for usage in query.get() as well as identity key
generation

""",
u"""
more assertion hints...

""",
u"""
improved assertions, test is failing on the buildbot only (not osx or linux)

    """,
u"""
some more omit schemas for [ticket:890]

""",
u"""
- tables with schemas can still be used in sqlite, firebird,
schema name just gets dropped [ticket:890]


""",
u"""
- fixed wrong varname in session exception throw
- fixed vertical example to just use a scoped session

""",
u"""
- a major behavioral change to collection-based backrefs: they no 
longer trigger lazy loads !  "reverse" adds and removes 
are queued up and are merged with the collection when it is 
actually read from and loaded; but do not trigger a load beforehand.
For users who have noticed this behavior, this should be much more
convenient than using dynamic relations in some cases; for those who 
have not, you might notice your apps using a lot fewer queries than
before in some situations. [ticket:871]


""",
u"""
- basic framework for generic functions, [ticket:615]
- changed the various "literal" generation functions to use an anonymous
bind parameter.  not much changes here except their labels now look 
like ":param_1", ":param_2" instead of ":literal"
- from_obj keyword argument to select() can be a scalar or a list.


""",
u"""
- fixed backref bug where you could not del instance.attr if attr
was None


""",
u"""
- relaxed rules on column_property() expressions having labels; any
ColumnElement is accepted now, as the compiler auto-labels non-labeled
ColumnElements now.  a selectable, like a select() statement, still
requires conversion to ColumnElement via as_scalar() or label().


""",
u"""
typo

""",
u"""
fixed replacement of existing column properties with synonyms, [ticket:888]

""",
u"""
- moved class-level attributes placed by the attributes package into a _class_state
variable attached to the class.
- mappers track themselves primarily using the "mappers" collection on _class_state.
ClassKey is gone and mapper lookup uses regular dict keyed to entity_name; removes
a fair degree of WeakKeyDictionary overhead as well as ClassKey overhead.
- mapper_registry renamed to _mapper_registry; is only consulted by the 
compile_mappers(), mapper.compile() and clear_mappers() functions/methods.

""",
u"""
- several ORM attributes have been removed or made private:
mapper.get_attr_by_column(), mapper.set_attr_by_column(), 
mapper.pks_by_table, mapper.cascade_callable(), 
MapperProperty.cascade_callable(), mapper.canload()
- refinements to mapper PK/table column organization, session cascading, 
some naming convention work

""",
u"""
added test to ensure two conflicting m2m + backrefs raise an error

""",
u"""
remove a little cruft

""",
u"""
- added support for version_id_col in conjunction with inheriting mappers.
version_id_col is typically set on the base mapper in an inheritance
relationship where it takes effect for all inheriting mappers. 
[ticket:883]
- a little rearrangement of save_obj()

    """,
u"""
- adjustment to the previous checkin regarding inheritance to not conflict with globals
- fix to self-referential eager loading such that if the same mapped
instance appears in two or more distinct sets of columns in the same
result set, its eagerly loaded collection will be populated regardless
of whether or not all of the rows contain a set of "eager" columns for
that collection.  this would also show up as a KeyError when fetching
results with join_depth turned on.


""",
u"""
- fixed bug where Query would not apply a subquery to the SQL when LIMIT
was used in conjunction with an inheriting mapper where the eager 
loader was only in the parent mapper.


""",
u"""
cleanup

""",
u"""
fixed unicode-ness for Unicode values

""",
u"""
- fixed bug which could arise when using session.begin_nested() in conjunction
with more than one level deep of enclosing session.begin() statements


""",
u"""
new synonym() behavior, including auto-attribute gen, attribute decoration, 
and auto-column mapping implemented; [ticket:801]

""",
u"""
default value of assert_unicode is None on String, False on create_engine(), and True on Unicode type.

""",
u"""
- column labels in the form "tablename.columname", i.e. with a dot, are now
supported.


""",
u"""
opened up the test for "reflection with convert_unicode=True".  this is since convert_unicode by default has assert_unicode, want to ensure that other dialects (at least oracle) support this (i.e. not unicode schema names themselves, just that they dont sent thru bytestrings to a String).

if maxdb or sybase *should* be able to handle this too though I can't test on this end.

""",
u"""
added None to support zope __provides__, [ticket:882]

""",
u"""
added a test to validate ResultProxy truncation behavior

""",
u"""
un-screw up the attribute manager checkin

""",
u"""
fixed reflection of unicode, [ticket:881]

""",
u"""
AttributeManager class and "cached" state removed....attribute listing
is tracked from _sa_attrs class collection

""",
u"""
Fix: MSSQL set identity_insert and errors [ticket:538]
""",
u"""
- check for NoneType too with unicode....
- fixed ORM tests to have proper unicode

""",
u"""
MSSQL doesn't support subqueries in insert values; disable test
""",
u"""
Fix: test_decimal on MSSQL - use a value that is accurately represented as a float, and make when asdecimal=False, convert Decimal to float
""",
u"""
edits

""",
u"""
Fix: MSSQL concatenate operator is + not || [ticket:879]
""",
u"""
- added new flag to String and create_engine(), assert_unicode=(True|False|None).
When convert_unicode=True, this flag also defaults to `True`, and results in all 
unicode conversion operations raising an exception when a non-unicode bytestring
is passed as a bind parameter.  It is strongly advised that all unicode-aware
applications make proper use of Python unicode objects (i.e. u'hello' and 
not 'hello').


""",
u"""
Avoid doubling quoting of identifier in MSSQL reflection
""",
u"""
Make function a reserved word in MSSQL
""",
u"""
MSSQL/PyODBC no longer has a global set nocount on
""",
u"""
Change to make PyODBC result fetching a bit more reliable
""",
u"""
column.foreign_key -> foreign_keys in MSSQL
""",
u"""
bump for py2.4

""",
u"""
OrderedSet to appease the unit tests....need to find a way to get rid of this

""",
u"""
- named_with_column becomes an attribute
- cleanup within compiler visit_select(), column labeling
- is_select() removed from dialects, replaced with returns_rows_text(), returns_rows_compiled()
- should_autocommit() removed from dialects, replaced with should_autocommit_text() and
should_autocommit_compiled()
- typemap and column_labels collections removed from Compiler, replaced with single "result_map" collection.
- ResultProxy uses more succinct logic in combination with result_map to target columns

""",
u"""
- decruftify old visitors used by orm, convert to functions that
use a common traversal function.
- TranslatingDict is finally gone, thanks to column.proxy_set simpleness...hooray !
- shoved "slice" use case on RowProxy into an exception case.  knocks noticeable time off of large result set operations.

""",
u"""
- all kinds of cleanup, tiny-to-slightly-significant speed improvements

""",
u"""
more changes to merge(dont_load); since we now have a guarantee that 
all merged instances aren't dirty, we can copy the attribues without using
any append/replace events, and therefore don't have any concern of lazy loaders
firing off.  added tests to ensure that '_is_orphan()' doesn't get screwed up,
and also that the 'dirty' list on the new session stays empty, which is an
extra bonus of this approach.


""",
u"""
- some clarifications and fixes to merge(instance, dont_load=True).  
fixed bug where lazy loaders were getting disabled on returned instances.
Also, we currently do not support merging an instance which has uncommitted
changes on it, in the case that dont_load=True is used....this will
now raise an error.  This is due to complexities in merging the 
"committed state" of the given instance to correctly correspond to the
newly copied instance.  Since the use case for dont_load=True is 
caching, the given instances shouldn't have any uncommitted changes on them
anyway.


""",
u"""
Typo fix
""",
u"""
- clarified the error message which occurs when you try to update()
an instance with the same identity key as an instance already present
in the session.
- opened up the recursive checks in session.merge() a little bit

""",
u"""
- fixed endless loop issue when using lazy="dynamic" on both 
sides of a bi-directional relationship [ticket:872]


""",
u"""
add a polymorphic get() test

""",
u"""
doctest fixups

""",
u"""
- added tests for [ticket:768]

""",
u"""
- added op() operator to instrumented attributes; i.e. 
User.name.op('ilike')('%somename%') [ticket:767]


""",
u"""
- MSSQL anonymous labels for selection of functions made deterministic
- propagate correct **kwargs through mssql methods

""",
u"""
repaired FB functions, [ticket:862]

""",
u"""
Tests for mysql casts and a couple adjustments.

""",
u"""
- Clarified use of python's Decimal

""",
u"""
Migrated Connection.properties to Connection.info ('info' is the new standard name for user-writable property collections that came out of [ticket:573]).  'properties' is now an alias, will be removed in 0.5.

""",
u"""
- added a little more checking for garbage-collection dereferences in
InstanceState.__cleanup() to reduce "gc ignored" errors on app
shutdown

""",
u"""
added some ORDER BYs to appease the ever picky postgres

""",
u"""
- PickleType will compare using `==` when set up with mutable=False,
and not the `is` operator.  To use `is` or any other comparator, send
in a custom comparison function using PickleType(comparator=my_custom_comparator).


""",
u"""
test cases were not fully testing contains_eager() with regards to [ticket:777], fixed contains_eager() for more than one level deep

""",
u"""
some wide zoomark ranges...

""",
u"""
cut down a good deal of Join construction overhead

""",
u"""
logging fixes

""",
u"""
fixed both group-deferred attributes and expired attributes to not
blow away changes made on attributes before the load takes place

""",
u"""
- oracle will now reflect "DATE" as an OracleDateTime column, not 
OracleDate

- added awareness of schema name in oracle table_names() function,
fixes metadata.reflect(schema='someschema') [ticket:847]


""",
u"""
removed is_expired() method since the meaning of "expired" is per-attribute now

""",
u"""
oops, print statements...

""",
u"""
typos

""",
u"""
- session.refresh() and session.expire() now support an additional argument
"attribute_names", a list of individual attribute keynames to be refreshed
or expired, allowing partial reloads of attributes on an already-loaded 
instance.
- finally simplified the behavior of deferred attributes, deferred polymorphic
load, session.refresh, session.expire, mapper._postfetch to all use a single
codepath through query._get(), which now supports a list of individual attribute names
to be refreshed.  the *one* exception still remaining is mapper._get_poly_select_loader(),
which may stay that way since its inline with an already processing load operation.
otherwise, query._get() is the single place that all "load this instance's row" operation
proceeds.  
- cleanup all over the place

""",
u"""
fixed further issues with row translation [ticket:868]

""",
u"""
Restored Python 2.3 compatibility (in IdentitySet)

    """,
u"""
modified last commit; the eager loader only undefers columns from the primary mapped table.

""",
u"""
- DeferredColumnLoader checks row for column, if present sends it to
ColumnLoader to create the row processor
- eager loaders ensure deferred foreign key cols are present in the primary list of columns (and secondary...).  because eager loading with LIMIT/OFFSET doesn't re-join to the parent table anymore this is now necessary. [ticket:864]

""",
u"""
Removed some distractions, ala r3770.

""",
u"""
Removed some distractions.

""",
u"""
  - added having() method to Query, applies HAVING to the generated statement
    in the same way as filter() appends to the WHERE clause.


    """,
u"""
More column type __repr__ corrections.

""",
u"""
AbstractType __repr__ robustification.

""",
u"""
Remove usage of deprecated in_ syntax
""",
u"""
- Pool listeners preserved on pool.recreate()
- Docstring rampage

""",
u"""
Removed out of date identity map language (thanks, Jiten)
    """,
u"""
added self referential test

""",
u"""
  - anonymous column expressions are automatically labeled.  
    e.g. select([x* 5]) produces "SELECT x * 5 AS anon_1".
    This allows the labelname to be present in the cursor.description
    which can then be appropriately matched to result-column processing
    rules. (we can't reliably use positional tracking for result-column 
    matches since text() expressions may represent multiple columns).
  
  - operator overloading is now controlled by TypeEngine objects - the 
    one built-in operator overload so far is String types overloading
    '+' to be the string concatenation operator.
    User-defined types can also define their own operator overloading
    by overriding the adapt_operator(self, op) method.
    
  - untyped bind parameters on the right side of a binary expression
    will be assigned the type of the left side of the operation, to better
    enable the appropriate bind parameter processing to take effect
    [ticket:819]
    


    """,
u"""
- mysql float types now do an end run around the base class and respect precision=None and length=None
- Added the mysteriously missing mysql cast support
- Added mysql REAL synonym for schema generation

""",
u"""
more searching for equiv columns

""",
u"""
- fixed error where Query.add_column() would not accept a class-bound
attribute as an argument; Query also raises an error if an invalid
argument was sent to add_column() (at instances() time) [ticket:858]


""",
u"""
- query doesn't throw an error if you use distinct() and an order_by()
containing UnaryExpressions (or other) together [ticket:848]


""",
u"""
a tweak, still requiring test coverage, to add more "foreign key equivalents" to the equivalent_columns collection

""",
u"""
more changes to traverse-and-clone; a particular element will only be cloned once and is
then re-used.  the FROM calculation of a Select normalizes the list of hide_froms against all
previous incarnations of each FROM clause, using a tag attached from cloned clause to
previous.

""",
u"""
- identified some cases where Alias needs to be cloned; but still cant clone
when its an alias of a Table; added some test coverage for one particular 
case from the doctests
- fixed "having" example in doctests, updated eager load example

""",
u"""
updated zoomark test_1a_populate callcounts. if the calls keep being removed like this then soon there will be none left.

""",
u"""
- fixed remainder of [ticket:853]
- bindparam 'shortname' is deprecated
- fixed testing.assert_compile() to actually generate bind param dict before asserting
- added bind param assertions to CRUDTest.test_update

""",
u"""
  - <Engine|Connection>._execute_clauseelement becomes a public method
    Connectable.execute_clauseelement


    """,
u"""
  - fix to compiled bind parameters to not mistakenly populate None
    [ticket:853]


    """,
u"""
fixed the previous TLTransaction checkin

""",
u"""
- fixed the close() method on Transaction when using strategy='threadlocal'


""",
u"""
adjusted "blank out primary key" rule to check for "allow_null_pks" on target mapper.  this was revealed by
recent attributes.py change in r3695 that causes a value of "None" to register as part of the attribute history's
added_items() collection (i.e. since AttributeHistory compares against NO_VALUE instead of None).

""",
u"""
  - fixed very hard-to-reproduce issue where by the FROM clause of Query
    could get polluted by certain generative calls [ticket:852]


    """,
u"""
fixed/added coverage for list extension; [ticket:855]

""",
u"""
Added missing InternalError exception wrapper [ticket:854]

""",
u"""
Create a storage field for arbitrary info on tables/columns; ticket #573
""",
u"""
Added note about EXT_CONTINUE to 3.x -> 4.x migration guide
""",
u"""
Migrated maxdb behavioral assumptions from unsupported to fails_on

""",
u"""
Added testing.fails_on('db') failure-asserter.

""",
u"""
- figured out a way to get previous oracle behavior back.  the ROWID thing
is still a pretty thorny issue.

""",
u"""
- adjustments to oracle ROWID logic...recent oid changes mean we have to 
use "rowid" against the select itself (i.e. its just...'rowid', no table name). 
seems to work OK but not sure if issues will arise
- fixes to oracle bind param stuff to account for recent removal of ClauseParameters object.

""",
u"""
- oid_column proxies more intelligently off of Select, CompoundSelect - fixes platform-affected bugs in missing the correct "oid" column
- locate_all_froms() is expensive; added an attribute-level cache for it
- put a huge warning on all select.append_XXX() methods stating that derived collections like locate_all_froms() may become invalid if
already initialized

""",
u"""
Whitespace cleanup

""",
u"""
- base_columns on ColumnElement becomes a list; as usual, because columns in CompoundSelects
may extend from more than one root column.
- keys_ok argument from corresponding_column() removed.  no more name-based matching of columns anywhere.
- DictDecorator is gone.  all row translators provided by orm.util.create_row_adapter().  Mapper
and contains_alias() cache the adapters on target mapper to avoid re-computation of adapters.
- create_row_adapter() accepts an "equivalent_columns" map as produced by Mapper, so that
row adapters can take join conditions into account (as usual again, to help with the CompoundSelects
produced by polymorphic_union).
- simplified TableSingleton to just provide lookup; moved all initialization into Table.
- the "properties" accessor on Mapper is removed; it now throws an informative
exception explaining the usage of mapper.get_property() and 
mapper.iterate_properties


""",
u"""
- SHOW CREATE TABLE output is slightly different if msyql is in ANSI mode

""",
u"""
- rewrote and simplified the system used to "target" columns across
selectable expressions.  On the SQL side this is represented by the
"corresponding_column()" method. This method is used heavily by the ORM
to "adapt" elements of an expression to similar, aliased expressions,
as well as to target result set columns originally bound to a 
table or selectable to an aliased, "corresponding" expression.  The new
rewrite features completely consistent and accurate behavior.
- the "orig_set" and "distance" elements as well as all associated
fanfare are gone (hooray !)
- columns now have an optional "proxies" list which is a list of all
columns they are a "proxy" for; only CompoundSelect cols proxy more than one column
(just like before).  set operations are used to determine lineage.
- CompoundSelects (i.e. unions) only create one public-facing proxy column per
column name.  primary key collections come out with just one column per embedded 
PK column.
- made the alias used by eager load limited subquery anonymous.


""",
u"""
  - func. objects can be pickled/unpickled [ticket:844]


  """,
u"""
- eager loading with LIMIT/OFFSET applied no longer adds the primary 
table joined to a limited subquery of itself; the eager loads now
join directly to the subquery which also provides the primary table's
columns to the result set.  This eliminates a JOIN from all eager loads
with LIMIT/OFFSET.  [ticket:843]


""",
u"""
- rewritten ClauseAdapter merged from the eager_minus_join branch; this is a much simpler
and "correct" version which will copy all elements exactly once, except for those which were
replaced with target elements.  It also can match a wider variety of target elements including
joins and selects on identity alone.

""",
u"""
Added a profiled benchmark for orm attribute modification & flush

""",
u"""
- Swap operator.eq for lambda x,y: x==y
- Some docstring re-formatting

""",
u"""
Formatting for 0.4.1
""",
u"""
Added some more notes for maxdb
""",
u"""
- Removed equality, truth and hash() testing of mapped instances. Mapped
  classes can now implement arbitrary __eq__ and friends. [ticket:676]

  """,
u"""
- removed "name" attribute from FromClause, Join, Select, CompoundSelect.  its needless
and led to some very strange anonymous label names
- removed what was apparently cruft in some column-targeting code

""",
u"""
added small clarification on single-table inheritance mapper def
""",
u"""
doc updates for save_on_init=False, merge(...dont_save=True)

    """,
u"""
- extra merge test
- merge with dont_load also propagates _state.modified

""",
u"""
- merge() includes a keyword argument "dont_load=True".  setting this flag will cause
the merge operation to not load any data from the database in response to incoming
detached objects, and will accept the incoming detached object as though it were 
already present in that session.  Use this to merge detached objects from external 
caching systems into the session.


""",
u"""
More improvements to testlib's mapper decorator

""",
u"""
Tweaks for assert_unordered_result

""",
u"""
Added AssertMixin.assert_unordered_result

""",
u"""
- session checks more carefully when determining "object X already in another session";
e.g. if you pickle a series of objects and unpickle (i.e. as in a Pylons HTTP session
or similar), they can go into a new session without any conflict
- added stricter checks around session.delete() similar to update()
- shored up some old "validate" stuff in session/uow

""",
u"""
Added rowset() testing helper.
""",
u"""
Fixed truth-evaluation of mapped objects (part of [ticket:676]

        """,
    u"""
- merged factor_down_bindparams branch. 
- removed ClauseParameters object; compiled.params returns a regular dictionary
  now, as well as result.last_inserted_params()/last_updated_params().
- various code trimming, method removals.

""",
u"""
Added command line options to add tripwires for __hash__, __eq__ and __nonzero__ on mapped classes.

""",
u"""
- A more efficient IdentitySet

""",
u"""
- split ScalarInstrumentedAttribute into a "scalar" and an "object" version.  
The "object" version loads the existing value on set/del, fires events,
 and handles trackparent operations; the "scalar" version does not.
- column loaders now use the "scalar" version of InstrumentedAttribute, so that
event handlers etc. don't fire off for regular column attribute operations.
- some adjustments to AttributeHistory to work properly for non-loaded attributes
- deferred column attributes no longer trigger a load operation when the
attribute is assigned to.  in those cases, the newly assigned
value will be present in the flushes' UPDATE statement unconditionally.


""",
u"""
dont call up new session unless save_on_init

""",
u"""
- also added proxying of save_or_update to scoped sessions.
- session.update() raises an error when updating an instance that is already in the session with a different identity
- adjusted zoomarks lower limits so I can get a nice clean run

""",
u"""
added REAL to reflection list

""",
u"""
Added proxying of __contains__ and __iter__ methods for scoped sessions

""",
u"""
Fixup sp_columns call
""",
u"""
Fixed a truncation error when re-assigning a subset of a collection
(obj.relation = obj.relation[1:]) [ticket:834]

""",
u"""
Added util.IdentitySet to support [ticket:676] and [ticket:834]

""",
u"""
Formatting tweaks.

""",
u"""
- Removed unused util.hash()
- Fixed __hash__ for association proxy collections

""",
u"""
- Don't re-save objects in these tests (post r3681)

""",
u"""
- Refinements for maxdb's handling of SERIAL and FIXED columns
- Expanded maxdb's set of paren-less functions

""",
u"""
- Added the NUMERIC sql type alias

""",
u"""
- fix to "row switch" behavior, i.e. when an INSERT/DELETE is combined into a
  single UPDATE; many-to-many relations on the parent object update properly. 
  [ticket:841]
- it's an error to session.save() an object which is already persistent
  [ticket:840]
- changed a bunch of repr(obj) calls in session.py exceptions to use mapperutil.instance_str() 

    """,
u"""
- restored MapperExtension functionality for [ticket:829], added test coverage
- changed naming convention in mapper.py tests to test_<testname>

""",
u"""
- fixed INSERT statements w.r.t. primary key columns that have SQL-expression
  based default generators on them; SQL expression executes inline as normal
  but will not trigger a "postfetch" condition for the column, for those DB's
  who provide it via cursor.lastrowid


  """,
u"""
- fixed expression translation of text() clauses; this repairs various
  ORM scenarios where literal text is used for SQL expressions


  """,
u"""
- a little cleanup to deferred inheritance loading

""",
u"""
- merged path_based_options branch
- behavior of query.options() is now fully based on paths, i.e. an option
  such as eagerload_all('x.y.z.y.x') will apply eagerloading to only
  those paths, i.e. and not 'x.y.x'; eagerload('children.children') applies
  only to exactly two-levels deep, etc. [ticket:777]
- removes old compiler()/schemagenerator()/schemadropper() methods from mysql dialect

""",
u"""
- inlined a couple of context variables
- PG two phase was calling text() without the correct bind param format, previous compiler checkin revealed issue

""",
u"""
- removed regular expression step from most statement compilations.
  also fixes [ticket:833]
- inlining on PG with_returning() call
- extra options added for profiling

""",
u"""
clear MapperStub ArgSingletons on clear_mappers() too...

""",
u"""
- fixed eager calc endless loop, introduced by r3646?  this issue should have been present before 3646 though.

""",
u"""
- fixed clear_mappers() behavior to better clean up after itself


""",
u"""
Make access dao detecting more reliable #828
""",
u"""
remove unused method

""",
u"""
- removed needless 'continue'


""",
u"""
- refactored _compile_properties/_compile_property, removed redundant code.
still a little squirrely but much less complex.
- improved behavior of add_property() etc., fixed [ticket:831] involving
  synonym/deferred


  """,
u"""
- de-cruftified backref configuration code, backrefs which step on existing
  properties now raise an error [ticket:832]


  """,
u"""
A --db alias for max.
""",
u"""
- Added initial version of MaxDB dialect.
- All optional test Sequences are now optional=True

""",
u"""
Fixed assert_sql_count exception logic.

""",
u"""
Updated for r3655.
""",
u"""
Added support for dialects that have both sequences and autoincrementing PKs.

""",
u"""
- The post_exec() hook now gets invoked before autocommit fires.

""",
u"""
Changed some columns from TEXT to VARCHAR for sapdb.

""",
u"""
- Now guarding against broken DB-APIs when wrapping their exceptions.
- Added an explicit test for exception wrapping.

""",
u"""
- sqlite will reflect "DECIMAL" as a numeric column


""",
u"""
exception message, [ticket:826]

""",
u"""
bumped sqlite version for empty insert test to 3.4

""",
u"""
- the whole OperationContext/QueryContext/SelectionContext thing greatly scaled back;
all MapperOptions process the Query and that's it, one very simpliied QueryContext object gets passed
around at query.compile() and query.instances() time
- slight optimization to MapperExtension allowing the mapper to check for the presence of an extended method, takes 3000 calls off of masseagerload.py test (only a slight increase in speed though)
- attempting to centralize the notion of a "path" along mappers/properties, need to define what that is better.  heading towards [ticket:777]...

""",
u"""
Excluding older sqlite versions from the new insert tests.  Currently conservative- 2.8 definitely fails, 3.3 works.  The 3.0 and 3.1 binaries from sqlite.org segfault for me so the version check should be revisited when possible.

""",
u"""
- Added contains operator (which generate a "LIKE %<other>%" clause).

- Added test coverage for endswith operator


""",
u"""
Fixed empty (zero column) sqlite inserts, allowing inserts on
autoincrementing single column tables.

""",
u"""
- added test coverage for unknown type reflection, fixed
  sqlite/mysql handling of type reflection for unknown types


  """,
u"""
typos, PassiveDefault likes "text()" otherwise the argument is a literal

""",
u"""
Bump!
""",
u"""
put a little note at the top directing users to the more *exciting* changes

""",
u"""
Update for 0.4.0
""",
u"""
typo

""",
u"""
- removed __len__ from "dynamic" collection as it would require issuing
  a SQL "count()" operation, thus forcing all list evaluations to issue
  redundant SQL [ticket:818]


  """,
u"""
Included 0.3.11 changelog
""",
u"""
Make ActiveMapper support viewonly property
""",
u"""
- Added support for UPDATE with LIMIT on mysql.
- Added mysql dialect tests for SET columns and the in_ operator.

""",
u"""
change the in_ API to accept a sequence or a selectable [ticket:750]

""",
u"""
- string-based query param parsing/config file parser understands
  wider range of string values for booleans [ticket:817]


  """,
u"""
Typo fix (thanks Ben!)
    """,
u"""
- Fixed SQL compiler's awareness of top-level column labels as used
  in result-set processing; nested selects which contain the same column 
  names don't affect the result or conflict with result-column metadata.

- query.get() and related functions (like many-to-one lazyloading)
  use compile-time-aliased bind parameter names, to prevent
  name conflicts with bind parameters that already exist in the 
  mapped selectable.


  """,
u"""
Fixed a couple of typos & hardened against future similar errors.

""",
u"""
- inline optimizations added to locate_dirty() which can greatly speed up
  repeated calls to flush(), as occurs with autoflush=True [ticket:816]


  """,
u"""
fix typo in examples

""",
u"""
- much more query verbiage
- contains() operator doesn't need to generate negation criterion unless
many-to-many

""",
u"""
documenting PropComparator behavior in orm tutorial

""",
u"""
- PG reflection, upon seeing the default schema name being used explicitly
  as the "schema" argument in a Table, will assume that this is the the 
  user's desired convention, and will explicitly set the "schema" argument
  in foreign-key-related reflected tables, thus making them match only
  with Table constructors that also use the explicit "schema" argument
  (even though its the default schema).  
  In other words, SA assumes the user is being consistent in this usage.


  """,
u"""
Restored unicode foreign key tests for [ticket:729].

""",
u"""
 - backref remove object operation doesn't fail if the other-side
collection doesn't contain the item, supports noload collections
[ticket:813]



""",
u"""
Added a missing @supported.
""",
u"""
- attempted to add a test for #622 / #751, but cant reproduce the failing condition
- fixed major oracle bug introduced by r3561, since colnames come back as unicode now,
need to encode keys in setinputsizes() step

""",
u"""
Added test for DBAPIError exception wrapping.

""",
u"""
Adjusted zoomark ranges for 2.4 and 2.5.

""",
u"""
Moved author comment preventing python 2.3 from importing the module...

""",
u"""
Snipped another generator expression.

""",
u"""
Converted errant generator expression.

""",
u"""
Assorted unused imports from pyflakes, docstring tweaks, formatting. 

""",
u"""
Winnowed __all__ for 'import * from sqlalchemy.engine'

""",
u"""
Unused imports.
""",
u"""
set svn:eol-style native


""",
u"""
Fixed reference bug in Connect, switched docstring format

""",
u"""
Removed a tab.

""",
u"""
- sybase cleanups: unused imports, adjusted docstrings, trailing whitespace
- added sybase dialect test
- added sybase and access to generated docs

""",
u"""
Fix ActiveMapper unit tests
""",
u"""
A few fixes to the access dialect
""",
u"""
Make ActiveMapper use scoped_session instead of SessionContext
""",
u"""
Fix broken update/delete queries on MSSQL when tables have a schema
""",
u"""
More ORDER BY, now with use_labels.

""",
u"""
- Added small DESC exercise to test_order_by.

""",
u"""
firebird: Fixed reflection for Integer and Numeric (after introducing Float column type). Need to review 'column_func' from reflecttable() and write some unit tests...
""",
u"""
Firebird: added Float and Time types (FBFloat and FBTime). Fixed BLOB SUB_TYPE for TEXT and Binary types.
Firebird's string types are tested in testtypes.py



""",
u"""
Added query coverage for ORDER BY over regular, aliased and DISTINCT columns.

""",
u"""
- sqlite housekeeping- added dialect test & moved tests there, pruned the dialect's reserved words.

""",
u"""
applied patch for pymssql 30-char limit 
""",
u"""
- Expanded JoinTest further, exercising joins the ORM depends on explicitly
  in the 'sql' tests.

  """,
u"""
- Fixed oracle 'use_ansi'-via-engine-url handling, added support for 'mode=sysdba' et al.

""",
u"""
similar type optimization for the Interval type


""",
u"""
Made the PickleType slightly faster.


""",
u"""
make two-phase transactions work a bit better by letting psycopg do whatever it does for implicit 
transaction starts

""",
u"""
changelog

""",
u"""
- initial sybase support checkin, [ticket:785]

""",
u"""
- fixed Oracle non-ansi join syntax

""",
u"""
- Expanded insert speed test to cover execute as well as executemany

""",
u"""
- Cleaned up visit_insert a bit, inserts are ~3% faster now.

""",
u"""
- a better fix for [ticket:810]. The cause was two phase commit/rollback not opening a new transaction as the dbapi implementations do.

""",
u"""
- fix multiple consequent two phase transactions not working with postgres. For some reason implicit transactions are not enough. [ticket:810]
- add an option to scoped session mapper extension to not automatically save new objects to session.

""",
u"""
Firebird now uses dialect.preparer to format sequences names.
UnicodeTest (reflection.py) runs ok now.
""",
u"""
- Expanded the outer join tests, now covering a situation that looked like it would be wonky in oracle.

""",
u"""
- Loosened up test_cant_execute_join for oracle (probably) + bonus typo fix
- Some docstring formatting waiting for pg to finish the tests...  waiting...

""",
u"""
- Added some outerjoin() execution exercises to the query tests.

""",
u"""
- No longer using reserved-ish column names in MutableTypesTest.

""",
u"""
- Actually fixed that testcascade issue.  And friends- looks like a cut-n-paste-o.

""",
u"""
- Fixed bogus testcascade, also made fixture sequences optional.

""",
u"""
- Squashed assumption of transparent type coercion support in defaults test

""",
u"""
- Rewrote autoincrement tests: added new scenarios, changed the orm fetchid to explicit test of last_row_ids(), and now testing transactional/autocommit modes separately to help catch any subtle issues that may exist due to assumed cursor state during post_exec().


""",
u"""
- Tweaked unordered select tests to not be sensitive to result set order, also split apart some tests (aliases) that sapdb has problems with.

""",
u"""
- fix to anonymous label generation of long table/column names [ticket:806]


""",
u"""
Firebird dialect now uses SingletonThreadPool as its poolclass.
(this fixes all "unsuccessful metadata update\n  object XXXXX is in use" test errors)

Minor fixes in tests
""",
u"""
- oracle does not implicitly convert to unicode for non-typed result
  sets (i.e. when no TypeEngine/String/Unicode type is even being used;
  previously it was detecting DBAPI types and converting regardless).
  should fix [ticket:800]
- fixed oracle out_parameters, likely broke in beta6
- fixed oracle _normalize_case for encoded names, gets unicode reflection test to work
- a few extra tests tweaked/unsupported for oracle 

""",
u"""
a typo on postgres returning test version check - change <8.4 -> <8.2

""",
u"""
- null foreign key on a m2o doesn't trigger a lazyload [ticket:803]
- slight simpliication to mapper.populate_instance()
- lamenting the different codepaths between query._get() and DeferredLoader.lazyload()
- query._get() uses all()[0] for single-row load to avoid complexity of first() (same as LazyLoader)

    """,
u"""
- fixed sqlite reflection of BOOL/BOOLEAN [ticket:808]


""",
u"""
- Sequences gain a basic dialect-specific kwargs bucket, like Tables.

""",
u"""
Adjusted reserved word reflection test for oracle-style identifier dialects.  But probably the CheckConstraint part of this test should just be removed, as it's testing a non-extant feature.

""",
u"""
- Fixed convert_result_value/bind_param compatibility for types without processors.

""",
u"""
Firebird now passes all tests from /test/engine/reflection.py (except UnicodeTest).

 * FBDialect now mimics OracleDialect, regarding case-sensitivity of TABLE and COLUMN names
 * FBDialect.table_names() doesn't bring system tables (ticket #796)
 * FB now reflects Column's nullable property correctly.

 """,
u"""
- move PG RETURNING tests to postgres dialect test
- added server_version_info() support for PG dialect
- exclude PG versions < 8.4 for RETURNING tests

""",
u"""
Made the regexp detecting the returning token more readable and fixed a couple of corner cases

""",
u"""
add support for returning results from inserts and updates for postgresql 8.2+. [ticket:797]

""",
u"""
- Tweaked the sql.text date test

""",
u"""
- Unraveled DateTest, removed bogus coverage omission for MySQL TIME types

""",
u"""
removed unused _fold_identifier_case method

""",
u"""
Some fixes on reflection tests (firebird):

 * firebird doesn't support create table tablename (columnname type NULL)" syntax (only NOT NULL)
 * firebird doesn't support schemas

 """,
u"""
- The no-arg ResultProxy._row_processor() is now the class attribute
  `_process_row`.
- Further tiny cleanups in RoxProxy.

""",
u"""
- Removed duplicate RowProxy.__len__ definition and some range(0, 1) lint

""",
u"""
- ident passed to id_chooser in shard.py always a list

""",
u"""
Make the postgres_where attribute to Index private to postgres module by using a kwargs attribute on the Index.

""",
u"""
- fixed three- and multi-level select and deferred inheritance
  loading (i.e. abc inheritance with no select_table), [ticket:795]


  """,
u"""
- added partial index support for postgres
- fixed create and drop methods on MockConnection

""",
u"""
- more docstrings
- Selectable is only used as a marker for FromClause (probably should be
removed/both classes merged)

""",
u"""
- doc updates.  generated sql docs are against sql.expression now.
- added SessionExtension docs.
- removed old sqlconstruction doc.
- changed 'copy_collections' flag in Select to '_copy_collections'; its
not really "public".

""",
u"""
firebird doesn't support sane rowcount.
""",
u"""
- Explicitly close connections in the FOR UPDATE tests.
- Minor housekeeping.

""",
u"""
Dropped the leading '__' from generated savepoint names, '_' isn't universally allowed as an initial character for identifiers.

""",
u"""
bump to beta7, but might become 0.4.0

""",
u"""
- The IdentifierPreprarer's _requires_quotes test is now regex based.
  Any out-of-tree dialects that provide custom sets of legal_characters
  or illegal_initial_characters will need to move to regexes or override
  _requires_quotes.

  """,
u"""
zoomark adjustment for the pybot...

""",
u"""
test coverage has been added...

""",
u"""
- adjust server side logic to work with standalone default execution
- a little bit of inlining of same

""",
u"""
- some docstrings for select()
- fixed tutorial doctests to adjust for execution changes, session being weak-referencing
(reloads objects more frequently which get u'' applied to their __repr__())

""",
u"""
Changed MySQL dialect to use the older LIMIT <offset>, <limit> syntax instead
of LIMIT <l> OFFSET <o> for folks using 3.23. ([ticket:794], thanks for the
patch!)

""",
u"""
Avoid tickling the MySQL-python 1.2.2 executemany parsing bug on a couple tests.

""",
u"""
add micro-doc for sequence standalone execution

""",
u"""
- added "FETCH" to the keywords detected by Postgres to indicate a result-row holding 
  statement (i.e. in addition to "SELECT").


  """,
u"""
Formatting tweaks
""",
u"""
fix comment

""",
u"""
- created a link between QueryContext and SelectionContext; the attribute
dictionary of QueryContext is now passed to SelectionContext inside
of Query.instances(), allowing messages to be passed between the two stages.
- removed the recent "exact match" behavior of Alias objects, they're back to
their usual behavior.
- tightened up the relationship between the Query's generation
  of "eager load" aliases, and Query.instances() which actually grabs the
  eagerly loaded rows.  If the aliases were not specifically generated for
  that statement by EagerLoader, the EagerLoader will not take effect
  when the rows are fetched.  This prevents columns from being grabbed accidentally 
  as being part of an eager load when they were not meant for such, which can happen
  with textual SQL as well as some inheritance situations.  It's particularly important
  since the "anonymous aliasing" of columns uses simple integer counts now to generate
  labels.


  """,
u"""
Tightened up time measurement.
""",
u"""
- the behavior of String/Unicode types regarding that they auto-convert
  to TEXT/CLOB when no length is present now occurs *only* for an exact type
  of String or Unicode with no arguments.  If you use VARCHAR or NCHAR 
  (subclasses of String/Unicode) with no length, they will be interpreted
  by the dialect as VARCHAR/NCHAR; no "magic" conversion happens there.
  This is less surprising behavior and in particular this helps Oracle keep 
  string-based bind parameters as VARCHARs and not CLOBs [ticket:793].  


  """,
u"""
- columns from Alias objects, when used to target result-row columns, must match exactly
  to the label used in the generated statement.  This is so searching for columns in a 
  result row which match aliases won't accidentally match non-aliased columns.
  fixes errors which can arise in eager loading scenarios.


  """,
u"""
- added session.is_modified(obj) method; performs the same "history" comparison operation
  as occurs within a flush operation; setting include_collections=False gives the same
  result as is used when the flush determines whether or not to issue an UPDATE for the
  instance's row.


  """,
u"""
added test coverage for r3512

""",
u"""
found an errant 2-tuple...

""",
u"""
fixed session extension bug [ticket:757]

""",
u"""
fixed firebird visit_alias [ticket:779]

""",
u"""
Added.
""",
u"""
- added "schema" argument to Sequence; use this with Postgres /Oracle when the sequence is
  located in an alternate schema.  Implements part of [ticket:584], should fix [ticket:761].


  """,
u"""
- merged sa_entity branch.  the big change here is the attributes system 
deals primarily with the InstanceState and almost never with the instrumented object
directly.  This reduces lookups and complexity since we need the state for just about
everything, now its the one place for everything internally.
we also merged the new weak referencing identity map, which will go out in beta6 and
we'll see how that goes !

""",
u"""
- added 'comparator' keyword argument to PickleType.  By default, "mutable"
  PickleType does a "deep compare" of objects using their dumps() representation.  
  But this doesn't work for dictionaries.  Pickled objects which provide an 
  adequate __eq__() implementation can be set up with "PickleType(comparator=operator.eq)"
  [ticket:560]


  """,
u"""
Don't use unicode with pyodbc on UCS-4 platforms [ticket:787]
""",
u"""
oops, forgot to commit CHANGES

""",
u"""
add sqlite reserved words list

""",
u"""
Yet more formatting updates
""",
u"""
Formatting tweaks.

""",
u"""
- added 'passive_deletes="all"' flag to relation(), disables all
  nulling-out of foreign key attributes during a flush where the parent 
  object is deleted.
  
- fix to FK compile fix from yesterday

""",
u"""
[ticket:728] foreign key checks for existing reflected FK and replaces itself

""",
u"""
Tweaked changelog
""",
u"""
- adjusted operator precedence of NOT to match '==' and others, so that 
  ~(x <operator> y) produces NOT (x <op> y), which is better compatible with MySQL.
   [ticket:764].  this doesn't apply to "~(x==y)" as it does in 0.3 since ~(x==y)
   compiles to "x != y", but still applies to operators like BETWEEN.


   """,
u"""
added assertion case for [ticket:764]

""",
u"""
[ticket:768] dont assume join criterion consists only of column objects

""",
u"""
- fixes to ShardedSession to work with deferred columns [ticket:771].

- user-defined shard_chooser() function must accept "clause=None"
  argument; this is the ClauseElement passed to session.execute(statement)
  and can be used to determine correct shard id (since execute() doesn't
  take an instance) 


  """,
u"""
Removed DefaultDialect.ischema and information_schema's ISchema (which incidentally had a 'toengine' in it...)


""",
u"""
- merged the unit test for the column_prefix fix that was established in the 0.3
trunk in r2795.  the actual "fix" part of it I just happened to spot manually 
the other day and fixed without testing (forgot what the original failure condition was) in r3449.

""",
u"""
Fixed repr() of mysql floats [ticket:775]
Added repr testing to mysql dialect

""",
u"""
Added 'collection_iter', like 'iter', for anything that implements the @collection.iterator or __iter__ interface.

""",
u"""
Doc updates.

""",
u"""
Updated ignores.
""",
u"""
mysql SETs and ENUMs now unescape embedded quotes before storage in .enums and .values.  An ancient bug.

""",
u"""
associationproxy relies upon a "sweep" through the attributes at the class level,
restored the equivalent functionality from previous releases

""",
u"""
- column defaults and onupdates, executing inline,  will add parenthesis
  for subqueries and other parenthesis-requiring expressions

  """,
u"""
do the cheaper check first....

""",
u"""
Fixed reflection of the empty string for mysql enums.

""",
u"""
merged current entity_management brach r3457-r3462.  cleans up
'_state' mamangement in attributes, moves __init__() instrumntation into attributes.py,
and reduces method call overhead by removing '_state' property.
future enhancements may include _state maintaining a weakref to the instance and a 
strong ref to its __dict__ so that garbage-collected instances can get added to 'dirty',
when weak-referenced identity map is used.

""",
u"""
Small change in ActiveMapper to make it work with Python 2.3
""",
u"""
remove unused method

""",
u"""
buildbot reported a lower number for test 1a...

""",
u"""
- took out method calls for oid_column
- reduced complexity of parameter handling during execution; __distill_params does all
parameter munging, executioncontext.parameters always holds a list of parameter structures
(lists, tuples, or dicts).

""",
u"""
Set supports_sane_multi_rowcount for MSSQL
""",
u"""
- removed "parameters" argument from clauseelement.compile(), replaced with
  "column_keys".  the parameters sent to execute() only interact with the 
  insert/update statement compilation process in terms of the column names 
  present but not the values for those columns.
  produces more consistent execute/executemany behavior, simplifies things a 
  bit internally.


  """,
u"""
- various cruft removal and optimizations to load process.
removes about 15K method calls from masseagerload.py test.

""",
u"""
Minor fixes to MSSQL reflection
""",
u"""
- mapper compilation has been reorganized such that most compilation
  occurs upon mapper construction.  this allows us to have fewer
  calls to mapper.compile() and also to allow class-based properties
  to force a compilation (i.e. User.addresses == 7 will compile all
  mappers; this is [ticket:758]).  The only caveat here is that 
  an inheriting mapper now looks for its inherited mapper upon construction;
  so mappers within inheritance relationships need to be constructed in
  inheritance order (which should be the normal case anyway).


  """,
u"""
lowered value, fewer calls on pybot ?

""",
u"""
entity refs

""",
u"""
edits

""",
u"""
added zoomark profile

""",
u"""
adjusting firebird, obviously needs someone to test

""",
u"""
fix to oracle sequence exec

""",
u"""
sequence pre-executes dont create an ExecutionContext, use straight cursor

""",
u"""
factored out uses_sequences_for_inserts() into 
preexecute_sequence dialect attribute

""",
u"""
- got all examples working
- inline default execution occurs for *all* non-PK columns
unconditionally - preexecute only for non-executemany PK cols on
PG, Oracle, etc.
- new default docs

""",
u"""
whats a big commit without some errant print statements ? :)

""",
u"""
- merged inline inserts branch
- all executemany() style calls put all sequences and SQL defaults inline into a single SQL statement 
and don't do any pre-execution
- regular Insert and Update objects can have inline=True, forcing all executions to be inlined.
- no last_inserted_ids(), lastrow_has_defaults() available with inline execution
- calculation of pre/post execute pushed into compiler; DefaultExecutionContext greatly simplified
- fixed postgres reflection of primary key columns with no sequence/default generator, sets autoincrement=False
- fixed postgres executemany() behavior regarding sequences present, not present, passivedefaults, etc.
- all tests pass for sqlite, mysql, postgres; oracle tests pass as well as they did previously including all
insert/update/default functionality

""",
u"""
update on pool status

""",
u"""
- fixed bugs in determining proper sync clauses from custom inherit
  conditions [ticket:769]


  """,
u"""
remove() should issue a close() on existing session

""",
u"""
Extended 'engine_from_config' coercion for QueuePool size / overflow. [ticket:763]
Added a set of coercion tests.

""",
u"""
engine.url cleanups [ticket:742]
- translate_connect_args can now take kw args or the classic list
- in-tree dialects updated to supply their overrides as keywords
- tweaked url parsing in the spirit of the #742 patch, more or less
 

""",
u"""
Fix for scoped_session's `mapper(extension=<scalar>)` [ticket:760]

""",
u"""
Catch-up entries for b5.

""",
u"""
- Restored reflection for mysql VIEWs [ticket:748]
- Fixed anonymous pk reflection for mysql 5.1
- Tested table and view reflection against the 'sakila' database from
  MySQL AB on 3.23 - 6.0. (with some schema adjustments, obviously)
  Maybe this will go into the SA test suite someday.
- Tweaked mysql server version tuplification, now also splitting on hyphens
- Light janitorial

""",
u"""
Fixed OrderedProperties pickling [ticket:762]

""",
u"""
Fixed signature for orm's BETWEEN operator.

""",
u"""
fix typos in assoc_proxy doc

""",
u"""
Expand custom assocproxy getter/setter support to scalar proxies

""",
u"""
Allow custom getter/setters to be specified for a standard AssociationProxy

""",
u"""
Fix for reflecting mysql keys that have USING

""",
u"""
bump

""",
u"""
- ugh  ! beta4 is double logging....fixed that....
- added test/fixed eager aliasizing for self-referential m2m relations

""",
u"""
changeset about connection pool

""",
u"""
restored WeakValueDict for threadlocal connections + profiler test, addressing
[ticket:754]

""",
u"""
- a "collection-holding" InstrumentedAttribute is now identified
by the presence of a "get_collection" method.
- added "get_collection" to DynamicCollectionAttribute so its 
treated as a collection.

""",
u"""
- tightened down the screws on logging a little bit

""",
u"""
- added **modifiers to _get_from_objects
- fixed up PG distinct flag

""",
u"""
- restored engine.echo flag
- changelog

""",
u"""
Adjusted ColumnDefault default function fitness check to only insure that a given function had no more than one non-defaulted positional arg.

""",
u"""
Housekeeping.

""",
u"""
Added a test for the SELECT DISTINCT ON postgresqlism.
Test currently fails due to two problems in postgres.py, but I'm leaving
it uncorrected for now as its not clear what the original intent was
for lists.

""",
u"""
Deleting an entity having a dynamic loader with cascade="all" has some issues at the moment.

""",
u"""
Association example updates, round two.

""",
u"""
basic 0.4 update

""",
u"""
For sqlite NUMERIC, send Decimal bind values as strings instead of converting to floats.

""",
u"""
fixed imports

""",
u"""
-removed echo_property() function, moved logging checks to
static variables 

""",
u"""
`from foo import (name, name)` isn't valid syntax for 2.3.  ah well.
omitting modules from sqlalchemy.__all__...

""",
u"""
Updated adjencytree examples

""",
u"""
fixed generative behavior to copy collections, [ticket:752]

""",
u"""
added first profile tests per [ticket:753]

""",
u"""
changing Pool to use weakref callback for auto-cleanup, instead of __del__.
Still leaving the RLock in Queue however since I see no guarantee that the weakref callback
isn't called at an arbitrary time.

""",
u"""
Inlined ClauseParameters.set_parameter (simple assignment) in construct_params
Big drop in function count for inserts (22%) with about a 3% wall clock improvement.

""",
u"""
fixed "SmallInteger"

""",
u"""
- implemented __len__() accessor on RowProxy
- implemented jek's ClauseParameters optimization for named params

""",
u"""
tweak that construct_params optimization, one of the adjustments wasn't needed

""",
u"""
A couple critical path optimizations
(some sql operations faster by nearly 10% wallclock, general orm around 3%)

    """,
u"""
- omitted 'table' and 'column' from 'from sqlalchemy import *'
- also omitted all modules and classes that aren't expicitly public
- omitted 'Smallinteger' (small i), but it's still in schema
- omitted NullType-related items from types.__all__
- patched up a few tests to use sql.table and sql.column, other related.

""",
u"""
added stub/import tests for all dialects
post-refactor fix for access dialect

""",
u"""
fix line ending svn prop
""",
u"""
pool_threadlocal on by default

""",
u"""
removed unnecessary _branch calls

""",
u"""
- method call removal

""",
u"""
- Engine and TLEngine assume "threadlocal" behavior on Pool; both use connect() 
for contextual connection, unique_connection() for non-contextual.
- Pool use_threadlocal defaults to True, can be set to false at create_engine()
level with pool_threadlocal=False
- made all logger statements in pool conditional based on a flag calcualted once.
- chagned WeakValueDictionary() used for "threadlocal" pool to be a regular dict 
referencing weakref objects.  WVD had a lot of overhead, apparently.  *CAUTION* - 
im pretty confident about this change, as the threadlocal dict gets explicitly managed
anyway, tests pass with PG etc., but keep a close eye on this one regardless.

""",
u"""
an early out processing insert/update column parameters was a bit too early.

""",
u"""
light docstring tweaks to the pool
more pedantic DBAPI -> DB-API changes in docstrings 

""",
u"""
CHANGES for r3372

""",
u"""
- Connection.begin() no longer accepts nested=True, a possible source of confusion as two forms of nesting are supported.  SAVEPOINT-style nesting logic is now contained soley in begin_nested().
- Docstring love for the engine package.  More is needed.

""",
u"""
ReST docstring fix

""",
u"""
mssql unit test fixes
""",
u"""
One more change of preparer() to identifier_preparer
""",
u"""
pyflakes mop-up

""",
u"""
Use identifier_preparer instead of preparer()
    """,
u"""
Fix broken imports
""",
u"""
docstring compile fixup

""",
u"""
adding an "already exists" catch for CREATE DOMAIN

""",
u"""
1. Module layout.  sql.py and related move into a package called "sql".
2. compiler names changed to be less verbose, unused classes removed.
3. Methods on Dialect which return compilers, schema generators, identifier preparers
have changed to direct class references, typically on the Dialect class itself
or optionally as attributes on an individual Dialect instance if conditional behavior is needed.
This takes away the need for Dialect subclasses to know how to instantiate these
objects, and also reduces method overhead by one call for each one.
4. as a result of 3., some internal signatures have changed for things like compiler() (now statement_compiler()), preparer(), etc., mostly in that the dialect needs to be passed explicitly as the first argument (since they are just class references now).  The compiler() method on Engine and Connection is now also named statement_compiler(), but as before does not take the dialect as an argument.  

5. changed _process_row function on RowProxy to be a class reference, cuts out 50K method calls from insertspeed.py


""",
u"""
- fixed prefixes= argument to select()
- mysql can now generate DISTINCT or ALL for queries, select(..., distinct='ALL')
- documented 'prefixes' arg to select()
- rearranged doc order for select args to mirror that of a generated statement
- went nutty and fixed wrapping and line length on most docstrings in sql.py 

""",
u"""
- modified SQL operator functions to be module-level operators, allowing
  SQL expressions to be pickleable [ticket:735]

- small adjustment to mapper class.__init__ to allow for Py2.6 object.__init__()
  behavior


  """,
u"""
- Added a "legacy" adapter to types, such that user-defined TypeEngine
  and TypeDecorator classes which define convert_bind_param()/convert_result_value()
  will continue to function.  Also supports calling the super() version of
  those methods.
  


  """,
u"""
add a test for dupe tables in MetaData

""",
u"""
- added close() method to Transaction.  closes out a transaction using rollback
  if it's the outermost transaction, otherwise just ends without affecting
  the outer transaction.

- transactional and non-transactional Session integrates better with bound 
  connection; a close() will ensure that connection transactional state is 
  the same as that which existed on it before being bound to the Session.


  """,
u"""
transactional session rolls back bound connection

""",
u"""
- threadlocal TLConnection, when closes for real, forces parent TLSession
to rollback/dispose of transaction


""",
u"""
update activemapper backrefs for r3340

""",
u"""
dont commandeer warnings into logger

""",
u"""
- turned twophase=True on in test
- TLEngine raises notimplemented for two-phase

""",
u"""
reinstated two_phase test.  currently it passes on PG with and without threadlocal.

""",
u"""
merge changset [3347] into trunk
""",
u"""
- added extra argument con_proxy to ConnectionListener interface checkout/checkin methods
- changed testing connection closer to work on _ConnectionFairy instances, resulting in 
pool checkins, not actual closes
- disabled session two phase test for now, needs work
- added some two-phase support to TLEngine, not tested
- TLTransaction is now a wrapper

""",
u"""
Merge [3345] into trunk. Unit test still TODO
""",
u"""
Disable MSSQL unicode statements on UCS-4 platforms, ticket #731
""",
u"""
- session transaction closing tweak for threadlocal
- connection-rollback decorator only fires on unhandled testing exceptions

""",
u"""
added a testing decorator that mops up wayward connections

""",
u"""
removed ridiculous LOrderedProp object

""",
u"""
revert the _DefaultExtension thing, it added function calls

""",
u"""
- moved test/orm/fixtures.py to testlib
- flattened mapper calls in _instance() to operate directly
through a default MapperExtension
- more tests for ScopedSession, fixed [ticket:746]
- threadlocal engine propagates **kwargs through begin()

    """,
u"""
it's a non-stop formatting fiesta

""",
u"""
formatting fiesta

""",
u"""
Added session.prune(), releases unused objects in strong-ref identity maps.

""",
u"""
- fix to bind param processing such that "False" values (like blank strings)
  still get processed/encoded


  """,
u"""
new changelog with betas

""",
u"""
bump

""",
u"""
needed orm import

""",
u"""
bump

""",
u"""
added remove() coverage....

""",
u"""
add length to str for pk usage

""",
u"""
added support for string date passthru in sqlite

""",
u"""
added 'inherit_foreign_keys' arg to mapper()

""",
u"""
use threading.local if available
speed up ThreadLocal for python 2.3 [ticket:743]
clean in topo (in patch from [ticket:743])

    """,
u"""
fix hasattr typo [ticket:744]

""",
u"""
stopgap, need a general strategy for raising readable exceptions for unicode content

""",
u"""
-removed print statements
- removeld errant classmethod on remove()

    """,
u"""
mass has_key->__contains__ migration, [ticket:738]

""",
u"""
- moved unicode schema ORM tests to unitofwork.py tests.  mostly
is to test mappers so limited DB support (really hard to get these unicode schemas
to work...)
- fixed [ticket:739]

""",
u"""
- cleanup, converted unitofwork.py to standard fixtures

""",
u"""
removed init_attr() call, which has shown to not increase performance

""",
u"""
- merged "fasttypes" branch.  this branch changes the signature
of convert_bind_param() and convert_result_value() to callable-returning
bind_processor() and result_processor() methods.  if no callable is 
returned, no pre/post processing function is called.
- hooks added throughout base/sql/defaults to optimize the calling
of bind param/result processors so that method call overhead is minimized.
special cases added for executemany() scenarios such that unneeded "last row id"
logic doesn't kick in, parameters aren't excessively traversed.
- new performance tests show a combined mass-insert/mass-select test as having 68%
fewer function calls than the same test run against 0.3.  
- general performance improvement of result set iteration is around 10-20%.

""",
u"""
cleanup

""",
u"""
revert previous change; had misunderstood context
""",
u"""
fudge to make SQL asserts work reliably with MSSQL
""",
u"""
Make versioningtest.test_basic only assert when the dbapi support sane_rowcount
""",
u"""
added sqlite/sa "unprofiled" raw time tests

""",
u"""
added full fetching of result columns, cut overall size to 50000

""",
u"""
a mass insert/ select benchmarking test, from
http://pyinsci.blogspot.com/2007/07/fastest-python-database-interface.html

""",
u"""
adjustment to table_names test such that the DB can have extra tables around

""",
u"""
removed assertion for "no tables in db"

""",
u"""
commented out unicode foriegn keys for now, not working on mysql or postgres

""",
u"""
attempt to get SessionTest to close transactions better

""",
u"""
- fixed endless loop
- fixed perf imports in masseagerload

""",
u"""
- base_mapper() becomes a plain attribute
- session.execute() and scalar() can search for a Table with which to bind
from using the given ClauseElement
- session automatically extrapolates tables from mappers with binds,
also uses base_mapper so that inheritance hierarchies bind automatically
- moved ClauseVisitor traversal back to inlined non-recursive


""",
u"""
added engine_from_config() function for helping to create_engine() 
from an .ini style config

""",
u"""
docstirng...

""",
u"""
added scoped session test independent of Session.mapper test

""",
u"""
- a rudimental SessionExtension class has been added, allowing user-defined
  functionality to take place at flush(), commit(), and rollback() boundaries.


  """,
u"""
- generalized a SQLCompileTest out of select.py, installed
into dialect/mssql.py, dialect/oracle.py, sql/generative.py
- fixed oracle issues [ticket:732], [ticket:733], [ticket:734]

""",
u"""
adjusted mysql autoload from a named schema, esp. for windows

""",
u"""
Removed unused imports, other import adjustments per pyflakes

""",
u"""
Centralized some `try: import foo except: import other as foo` imports in util 

""",
u"""
Added more unicode foreign key tests for [ticket:729]

""",
u"""
auto-commit after LOAD DATA INFILE for mysql
caught a couple more uncompiled regexps

""",
u"""
- got is_subquery() working in the case of compound selects, test for ms-sql

""",
u"""
removed ms-sql unsupporteds

""",
u"""
- fixed compiler bug in mssql
- marked as unsupported for mssql all two-phase and nested transcation tests
- marked as unsupported for mssql various transactional/session tests which require two connections looking at uncommitted/external data at the same time (ms-sql cant handle it)
- put better explicit closeout step in unitofwork.py tests to appease ms-sqls hard locking

""",
u"""
Close SQLite databases before deleting file, so the lock is released, important on Windows
""",
u"""
MSSQL: disable new 0.4 tests that cause hangs
""",
u"""
edits

""",
u"""
- scoped_session docs
- added remove() method to scoped_session

""",
u"""
Fix missing import of 'operator'
""",
u"""
added "should_commit()" hook to ExecutionContext.  dialects can override with specific tests

""",
u"""
Bump.
""",
u"""
typos

""",
u"""
added a brief migration guide

""",
u"""
two tests which assumed autoincrement=False for integer PK columns now require it 
to be explicit due to r3255.

""",
u"""
Docs.

""",
u"""
Allow auto_increment on any pk column, not just the first.

""",
u"""
Added an exception hierarchy shadowing DB-API exc types
No more generic SQLErrors wrappers- the shadow type matching the DB-API error is raised. [ticket:706]
SQLError is now (also) DBAPIError.
DBAPIError and subtype constructors will refuse to wrap a SystemExit or KeyboardInterrupt, returningthe original interrupt exception instead of a new instance. [ticket:689]
Added a passthroughs for SE/KI exceptions in a couple except-and-discard situations


""",
u"""
inlined encoding of result column names

""",
u"""
- precompiled regexp for anonymous labels
- has_key()->__contains__()

    """,
u"""
Bake the version number into the source during packaging.

""",
u"""
- removed _calculate_correlations() methods, removed correlation_stack, select_stack;
all are merged into a single stack thats all within ansicompiler.  clause visiting cut down
significantly.

""",
u"""
  - case_sensitive=(True|False) setting removed from schema items, since
    checking this state added a lot of method call overhead and there was
    no decent reason to ever set it to False.  Table and column names which are 
    all lower case will be treated as case-insenstive (yes we adjust for 
    Oracle's UPPERCASE style too).
        


    """,
u"""
attempting to get oracle XID to work.  not there yet.

""",
u"""
by popular demand, mysql reflection is now a single round-trip and uses a parse of SHOW CREATE TABLE ddl [ticket:612]
the ANSI_QUOTES mode is now supported
halfway there for auto_increment on secondary columns [ticket:649]
indexes are now reflected [ticket:663]

""",
u"""
repaired oracle savepoint implementation

""",
u"""
- oracle reflection of case-sensitive names all fixed up
- other unit tests corrected for oracle

""",
u"""
#725 add query arg to id_chooser()

""",
u"""
Correct docstring.

""",
u"""
--dropfirst option added, defaults to False.  pre-drops tables when set to True, reportedly mis-behaves on Oracle, MS-SQL.

""",
u"""
- fixes to PG unicode table/sequence reflection/create/drops

""",
u"""
- merged mapper has_pks fix from r3239 0.3 branch

""",
u"""
formatting tweaks

""",
u"""
moved old plugins to "deprecated" subheading, took out SessionContext/assignmapper docs (references 0.3 docs)

""",
u"""
Allow '$' in bind param detection [ticket:719], added test suite & fixed an edge case

""",
u"""
removed unused method from last checkin

""",
u"""
some edits

""",
u"""
- decoupled all ColumnElements from also being Selectables.  this means
that anything which is a column expression does not have a "c" or a
"columns" attribute.  Also works for select().as_scalar(); _ScalarSelect
is a columnelement, so you can't say select().as_scalar().c.foo, which is 
a pretty confusing mistake to make.  in the case of _ScalarSelect made
an explicit raise if you try to access 'c'.

""",
u"""
Added 'unformat_identifiers', produces a list of unquoted identifiers from an identifier or a fully qualified identifier string.

""",
u"""
- added 'object_session' as classlevel method to Session
- moved 'identity_key' to be a classmethod on Session
- some docstrings
- merged r3229 from 0.3 branch to unconditonally quote schemaname in PG-reflected default
- name fixes in dynamic unit test

""",
u"""
restore clipping value for YEAR DDL

""",
u"""
session docs, CHANGES updates

""",
u"""
edits

""",
u"""
added section on SQL-embedded attributes

""",
u"""
tweak

""",
u"""
new session doc

""",
u"""
warning: may not be true.  (GIS types)

    """,
u"""
^C ^C ^C! (revert r3218 in pooling.txt)

    """,
u"""
Added `set_types` to util, a tuple of available set implementations.
Added BIT and SET ([ticket:674])- all mysql data types are now covered!
Fix for YEAR DDL generation, also no longer a concatenable type.
Expanded docs for some mysql column esoterica.

""",
u"""
- fix mssql compiling explicitly added alias twice
- add is_select to mssql dialect. currently adds only sp_columns, someone familiar with mssql should update this
- update mssql get_default_schema_name api
- remove commented code from Query.filter_by

""",
u"""
merge [3215] into trunk
""",
u"""
Improve utf8 engine handling during test setup and in test suites.

""",
u"""
Addded 're' import

""",
u"""
added missing methods/props to ScopedSession

""",
u"""
fix url for 04 docs
""",
u"""
update SS docs to 0.4
""",
u"""

put implicit examples as part of test suite

""",
u"""
added link to implicit execution section

""",
u"""
added docs on connectionless/implicit

""",
u"""
Added 'SET' to reserved words, plus gratuitous reindenting.

""",
u"""
- moved extension class init around so query() is available

""",
u"""
- migrated 'desc', 'asc', and 'distinct' to be in the Operators framework
- fixes to operator() method signature/calling

""",
u"""
edits

""",
u"""
'condition' misspelled

""",
u"""
added 'asc' and 'desc' to PropComparator....this should be placed at a lower level somehow, such
as real ASC and DESC operators

""",
u"""
- 'comparator' argument to composite() is a class
- added composite types doc, other edits

""",
u"""
- added desc() and asc() directly to CompareMixin

""",
u"""
- docs
- added some convenience functions to selects, clauseelements
- fixed distinct()

    """,
u"""
edits

""",
u"""
clean up some dead code in Query.filter_by

""",
u"""
edits

""",
u"""
generated markup fixes

""",
u"""
- edits
- added "params" to ansisql compiler

""",
u"""
edit

""",
u"""
removing Query from __all__ was a little premature

""",
u"""
- draft sqlexpression tutorial
- added some generative methods to exists()
- got clause adapter to work with join()

    """,
u"""
Add initial version of MS Access support
""",
u"""
work in progress

""",
u"""
docstring stuff

""",
u"""
edits

""",
u"""
a more friendly name

""",
u"""
Added test coverage for freeform collection decorators
Decorators with positional arg specs can be called with named args too...

""",
u"""
edits, css

""",
u"""
eager/lazyloading section


""",
u"""
edits

""",
u"""
edits

""",
u"""
edits

""",
u"""
edit

""",
u"""
doc tweaks

""",
u"""
Pedantic tweak to coltype swappage... 

""",
u"""
Further tweaks for lc strategies
Ensure that the recently added first-class tinyint plays nicely with boolean reflection

""",
u"""
Added explicit Unicode table_names test 

""",
u"""
Revert r3169 and r3148 changes to unicode schema reflection test, will add an explicit engine/reflection test to cover.

""",
u"""
More robust droppage of table detritus, also respect --quiet

""",
u"""
Update for osx

""",
u"""
edits

""",
u"""
- fix for [ticket:712], more unit tests

""",
u"""
inheritance docs

""",
u"""
Rearranged engine initialization, its now easy to make ad-hoc testing engines that preserve all of the --options requested
Promoted the 'utf8 bind' logic for tests needing utf8 connections into testlib
Added a pause before issuing DROPs to rid the testing db of clutter


""",
u"""
- fixed table_names for postgres to return as dialect.encoding-decoded unicode strings

""",
u"""
- added hooks for alternate session classes into sessionmaker
- moved shard example/unittest over to sessionmaker

""",
u"""
- removed enhance_classes from scoped_session, replaced with
scoped_session(...).mapper.  'mapper' essentially does the same 
thing as assign_mapper less verbosely.
- adapted assignmapper unit tests into scoped_session tests

""",
u"""
changed to use class attributes

""",
u"""
small fix for filter() aliasing, upgraded elementtree examples to use 0.4 style queries

""",
u"""
stupid svn:ignore isn't recursive?  who thought THAT was a bright idea? find test lib -type d |grep -v svn |xargs -n 1 svn propset svn:ignore '*.pyc'
""",
u"""
add pyc to svnignore
""",
u"""
switch "if not len(x)" to "if not x"
""",
u"""
edits

""",
u"""
more edits

""",
u"""
edits, html escaping

""",
u"""
Oops.

""",
u"""
only one instance of while len(...)
    """,
u"""
switch (simple) occurences of 'if len(x)' to 'if x': find . -name '*.py' |xargs perl -pi.bak -e 's/if len\((\S+)\):/if $1:/' && find . -name '*.bak' |xargs rm
                                                                                                                    """,
                                                                                                                u"""
add comment, intermediate var for readability
                                             """,
                                            u"""
table_names shouldn't include system tables.  (if user wants that they should poke around in catalog manually.)
                                                                                                               """,
                                                                                                            u"""
- Dialects can be queried for the server version (sqlite and mysql only with this commit)
- Mark everything in a test suite as failed when setUpAll fails.
- Added test coverage for Unicode table names in metadata.reflect()
- @testing.exclude() filters out tests by server version
- Applied exclude to the test suite, MySQL 4.1 passes again (no XA or SAVEPOINT)
- Removed MySQL charset-setting pool hook- charset=utf8&use_unicode=0 works just as well.  (Am I nuts?  I'd swear this didn't work before.)
- Finally migrated some old MySQL-tests into the dialect test module
- Corrected 'commit' and 'rollback' logic (and comment) for ancient MySQL versions lacking transactions entirely
- Deprecated the MySQL get_version_info in favor of server_version_info
- Added a big hunk-o-doc for MySQL.


""",
u"""
docs

""",
u"""
- fixed autoflush with count(), aggregates
- doc formatting bonanza
- delete() section to orm tutorial

""",
u"""
- sessionmaker module is out, replaced with simple function in session.py
- scoping/class instrumenting behavior of sessionmaker moved into new scoping module
which implements scoped_session() (subject to potential name change)
- SessionContext / assignmapper are deprecated, replaced with scoped_session()

    """,
u"""
- added inline UPDATE/INSERT clauses, settable as regular object attributes.
      the clause gets executed inline during a flush().


      """,
    u"""
added values() generative method to Insert/Update

""",
u"""
replaced metaclass/__new__ insanity with a __call__()

    """,
u"""
- used a metaclass trick to get Session.bind / Session.<someprop> to work

""",
u"""
-merged 0.3 pool threadlocal fix from r3139

""",
u"""
- SessionContext and assignmapper are deprecated
- Session function is removed
- all replaced with new sessionmaker() function.  description at:
http://www.sqlalchemy.org/trac/wiki/WhatsNewIn04#create_sessionSessionContextassignmapperDeprecated

""",
u"""
Remove unused mxDateTime
""",
u"""
Stopgap for post- #646 and r3030, wedge in 0.3 Decimals-are-floats behavior for vanilla 2.3 Python.


""",
u"""
Don't set __name__ on py 2.3
""",
u"""
ThreadLocalMetaData ought not .dispose() a Connection
More docstring changes

""",
u"""
Sort methods by __init__, name, __names__
Supply a little default docstring for __init__
Don't document __repr__, __str__, __getstate__, ...

""",
u"""
Make {include,exclude}_properties membership tests ignore column_prefix

""",
u"""
Tweak 'poolclass' default arg processing [ticket:437]

""",
u"""
Added EXT_CONTINUE and EXT_STOP for MapperExtensions; EXT_PASS is a synonym for EXT_CONTINUE.
Repointed docs and examples to EXT_CONTINUE


""",
u"""
Little docstring tweaks

""",
u"""
Expanded docstring docs for pool hooks.

""",
u"""
Ignore __weakref__ methods.  Not sure why they're bubbling up here- a Python 2.5 artifact?

""",
u"""
It's now possible to map only a subset of available selectable columns onto mapper properties [ticket:696].

""",
u"""
Removed trailing slash from sys.path manipulation [ticket:700]

""",
u"""
Tweak ([ticket:673])

    """,
u"""
Promoted format_table_seq from mysql to ansisql.  Formats a fully qualified table reference as a quoted sequence, suitable for '.'.joining or whatever.  [ticket:666]

""",
u"""
Changed __colset__ to __composite_values__ [ticket:692] (sort of)

    """,
u"""
Adjust ignore list for intro.
""",
u"""
- commented out auto-rollback of attributes for now, added [ticket:705] with the recipe
- added "drop_all()" at the start of all unittest runs; see if that helps some of the carwrecks we have

""",
u"""
exec() has always made me a little queasy...

""",
u"""
re-jiggered (yes, thats a technical term) DeprecationWarning into SADeprecationWarning so that we can set the "once" filter across all SQLAlchemy-originating DeprecationWarnings.

""",
u"""
- assurances that context.connection is safe to use by column default functions, helps proposal for [ticket:703]

""",
u"""
tweaks

""",
u"""
intro...

""",
u"""
 - restored old assign_mapper monkey patched query methods but with two differences:
   * added a deprecation warning
   * check if a method with that name already exist in the class
 - more foolproof deprecation warning for scalar kwarg

 """,
u"""
MetaData can now reflect() all tables in the database en-masse thanks to table_names().
table_names changed to accept an explicit connection
ThreadLocalMetaData constructor now takes no arguments. If case_sensitive is needed in a multi-bind context, move it to Table or subclass TLMD to force it.
Banished **kwargs from MetaData
Lots of class doc and docstring improvements around MetaData and TLMD.
Some engine->bind internal naming updates + reorg in schema.
MySQL table_names now return Unicode. (Also, a unicode reflect() unit test is needed.)


    """,
u"""
log-ify warnings module.  get rid of one-per-customer deprecationwarning limit.
""",
u"""
add warnings for deprecated methods and options
""",
u"""
little too happy with the copy/paste there
""",
u"""
crank

""",
u"""
more crankage....

""",
u"""
crankin....

""",
u"""
test for table_names
""",
u"""
docs in progress, new ORM tutorial

""",
u"""
more explicit doc

""",
u"""
doc reorganize; greater emphasis on overview (just like with 0.1), but still with tutorials (TODO).

""",
u"""
- added Session constructor which turns autoflush/transactional on
- Session is used by unitofwork unit test now as well as session.py tests
- fixes to table/schema reflection broken last night
- doc updates
- other unittest fixes

""",
u"""
- removed import of old sqlite module [ticket:654]
- removed sqlite version warning, all tests pass 100% with py2.5's older sqlite lib
- fixed dynamic test for py2.5

""",
u"""
Big MySQL dialect update, mostly efficiency and style.
Added TINYINT [ticket:691]- whoa, how did that one go missing for so long?
Added a charset-fixing pool listener. The driver-level option doesn't help everyone with this one.
New reflector code not quite done and omiited from this commit.


""",
u"""
Finish table_names.

""",
u"""
add table_names() for mysql.  maybe it works.
""",
u"""
r/m information_schema from pg
""",
u"""
engine.table_names()

tested vs sqlite and pg.  mssql should also be ok (uses ischema like pg.)  others are best-guess based on has_table code.
""",
u"""
fixed 'column_literal' to 'literal_column' [ticket:626]

""",
u"""
clearer error for ForeignKey cant locate parent table, [ticket:565]

""",
u"""
fixed pydoc bug in [ticket:564]

""",
u"""
-fixed [ticket:555]
- fixed attribute glitch breaking the build

""",
u"""
- removed auto_close_cursors and disallow_open_cursors arguments from Pool;
reduces overhead as cursors are normally closed by ResultProxy and Connection.


""",
u"""
Added pool hooks for connection creation, check out and check in.

""",
u"""
remove print

""",
u"""
- trimming down redundancy in lazyloader code
- fixups to ORM test fixture code
- fixup to dynamic realtions, test for autoflush session, delete-orphan
- made new dynamic_loader() function to create them
- removed old hasparent() call on AttributeHistory

""",
u"""
Got basic backrefs going with dynamic attributes

""",
u"""
- an experimental feature that combines a Query with an InstrumentedAttribute, to provide
"always live" results in conjunction with mutator capability

""",
u"""
removed LONG_STRING, LONG_BINARY from "binary" types, [ticket:622]

""",
u"""
Added some collections slicing tests that somehow escaped the r3040 commit.

""",
u"""
mention include_columns in docs; see #561

(sorry Mike, I did have a unit test but didn't commit it somehow)
""",
u"""
added distinct positional dictionary arg to query.params(), fixes [ticket:690]

""",
u"""
Fix testing.  Really.

""",
u"""
Fix coverage again- try really hard not to load anything from lib/ until after the coverage hook runs.

""",
u"""
some comments, pragma no cover on some deprecated query methods

""",
u"""
- clarified LoaderStrategy implementations, centralized deferred column loading 
into DeferredColumnLoader (i.e. deferred polymorphic loader)
- added generic deferred_load(instance, props) method, will set up "deferred" or "lazy"
loads across a set of properties.
- mapper post-fetch now uses all deferreds, no more post-selects inside a flush() [ticket:652]

""",
u"""
fixed glitch in Select visit traversal, fixes #693

""",
u"""
Fixed that old inconsistency (person VS employee) in the joined-table inheritance docs


""",
u"""
added an order by attempting to get buildbot 100%

""",
u"""
- merged ants' derived attributes example from 0.4 branch
- disabled PG schema test for now (want to see the buildbot succeed)

    """,
u"""
merging 0.4 branch to trunk.  see CHANGES for details.  0.3 moves to maintenance branch in branches/rel_0_3.

""",
u"""
  - added a check for joining from A->B using join(), along two
      different m2m tables.  this raises an error in 0.3 but is
      possible in 0.4 when aliases are used. [ticket:687]


      """,
    u"""
mssql: indexes are now quoted when dropping from reflected tables [ticket:684]
""",
u"""
mssql: added support for TIME type (simulated via DATETIME col) [ticket:679]
""",
u"""
edits

""",
u"""
edits

""",
u"""
postgres cant do this particular test b.c. the default "public" schema is taken
as a blank "schema" argument on Table

""",
u"""
hopefully resolved all the PG deadlocks occuring here

""",
u"""
Merged lower case caching, fetching from r2955
Be sure to close rows fetched in reflection (if not autoclosed)
Fixed bind test, needed transactional storage engine for mysql



""",
u"""
further adjustment to pool.get

""",
u"""
assert timeout is 3 seconds, not 2

""",
u"""
- a new mutex that was added in 0.3.9 causes the pool_timeout
feature to fail during a race condition; threads would 
raise TimeoutError immediately with no delay if many threads 
push the pool into overflow at the same time.  this issue has been
fixed.


""",
u"""
Merged reference fixes from r2986

""",
u"""
Better quoting of identifiers when manipulating schemas
Merged from r2981

""",
u"""
info on db-specific types

""",
u"""
- merged some more of the SessionTransaction connection-bound checks from 0.4
- _BinaryExpression.compare() checks for a base set of "commutative" operators and checks for itself in reverse if so
- added ORM-based unit test for the above, fixes [ticket:664]

""",
u"""
 - foreign key specs can have any chararcter in their identifiers
     [ticket:667]


     """,
    u"""
Properly escape table names when reflecting for mssql and sqlite [ticket:653]
""",
u"""
bind/connectable compat, allow .bind = None
fix import for DBAPIError raise

""",
u"""
Minor cleanups.
""",
u"""
Be specfic when detecting "no table" exceptions.
""",
u"""
- Added basic schema reflection coverage to main tests
- Fix stupid mysql typo (#662)
- Merged mysql osx/multibyte has_table from 0.4 (r2943)

    """,
u"""
- fixed max identifier length on postgres (63) [ticket:571]
- fixed doc typo ("in_" operator)
- misc indent stuff


""",
u"""
- fixes for connection bound sessions, connection-bound compiled objects via metadata

""",
u"""
fixes

""",
u"""
fixes

""",
u"""
spelling error

""",
u"""
- fixed "ambiguous column" result detection, when dupe col names exist
in a result [ticket:657]


""",
u"""
updated interval type for [ticket:595]

""",
u"""
- added friendlier error checking for query.get() with too-short pk
- more docs

""",
u"""
removed prints

""",
u"""
- more docs
- got from_statement() to actually work with query, tests were not covering
- added auto-labeling of anonymous columns sent to add_column(), tests

""",
u"""
- more docs
- some more query tests
- removed warnings from testbase to appease the buildbots

""",
u"""
- columns can be overridden in a reflected table with a "key" 
attribute different than the column's name, including for primary key
columns [ticket:650]
- more docs

""",
u"""
- fixed unicode conversion in Oracle TEXT type

""",
u"""
- converts cx_oracle datetime objects to Python datetime.datetime when
Python 2.3 used [ticket:542]


""",
u"""
- mod operator '%' produces MOD [ticket:624]


""",
u"""
- more docs
- query will unique tupled results
- fixed [ticket:605] which is for psycopg1 anyway...

""",
u"""
more query methods, overhauliung docs for forwards 0.4 method

""",
u"""
- test module turns warnings into exceptions so they can be tested for
- the two mapper PK tests should actually warn on the id column collision
- reverted abc_inheritance back to normal

""",
u"""
- improved ability to get the "correct" and most minimal set of primary key 
  columns from a join, equating foreign keys and otherwise equated columns.
  this is also mostly to help inheritance scenarios formulate the best 
  choice of primary key columns.  [ticket:185]
- added 'bind' argument to Sequence.create()/drop(), ColumnDefault.execute()


""",
u"""
changed password field length to 15 to fix [ticket:656]

""",
u"""
rearrange sqlite dialect initialization to be able to warn about pysqlite1 being too old. fixes #654

""",
u"""
Fix setup for standalone sequence test
""",
u"""
Refinement for r2890, column names should remain unicode.

""",
u"""
Swap imports order, removed trailing whitespace from varchar test data

""",
u"""
- a warning is issued by Mapper when two primary key columns of the
same name are munged into a single attribute.  this happens frequently
when mapping to joins (or inheritance). 


""",
u"""
- composite primary key is represented as a non-keyed set to allow for 
composite keys consisting of cols with the same name; occurs within a
Join.  helps inheritance scenarios formulate correct PK.
- ticket #185 reopened.  still need to get Join to produce a minmal PK for fk'ed columns

""",
u"""
- Keep reflected strings in the connection encoding, not unicode.  For now.

""",
u"""
- the various "engine" arguments, such as "engine", "connectable",
"engine_or_url", "bind_to", etc. are all present, but deprecated.
they all get replaced by the single term "bind".  you also
set the "bind" of MetaData using 
metadata.bind = <engine or connection>.  this is part of 0.4
forwards compatibility where "bind" is the only keyword.
[ticket:631]


""",
u"""
Correct error message for concurrent delete exceptions, fixes #586

""",
u"""
dont cache reflected domains, lookup each time

""",
u"""
- converted mapper.py unit test to 0.4's four separate mapper.py, query.py, eager_relations.py, lazy_relations.py.
tests 0.4 forwards compatibility for [ticket:631]
- fixed "reset_joinpoint()" in query to actually work, when the same table appears in two join()s it reuses that
same table as a joinpoint the way 0.4 does.

""",
u"""
- Patch up MySQL reflection issues with old server versions, alpha drivers,
  quoting, and connection encoding.

  """,
u"""
mssql: preliminary support for using scope_identity() with pyodbc
""",
u"""
mssql now able to reflect start and increment values for identity columns
""",
u"""
further refinements to the previous session.expunge() fix

""",
u"""
fixed small expunge() bug where object might not be present in session

""",
u"""
changed "_source_column" to simpler "_distance"

""",
u"""
more "column targeting" enhancements..columns have a "depth" from their ultimate source column so that corresponding_column() can find the column that is "closest" (i.e. fewest levels of proxying) to the requested column

""",
u"""
Fix port option handling for mssql/pyodbc [ticket:634]
""",
u"""
- ForeignKey to a table in a schema thats not the default schema
requires the schema to be explicit; i.e. ForeignKey('alt_schema.users.id')
- the fix in "schema" above fixes postgres reflection of foreign keys from an
alt-schema table to a public schema table


""",
u"""
discourage usage of always_refresh

""",
u"""
edits

""",
u"""
oh wow, confused "implicit" with "connectionless"

""",
u"""
edits

""",
u"""
more edits

""",
u"""
fixes

""",
u"""
- rewrote dbengine doc
- some changes to metadata doc, no Bound/Dynamic metadata mentioned
- fixed --file flag in genhtml.py

""",
u"""
Tweak docs, very minor DMD compatability tweak

""",
u"""
- Deprecated DynamicMetaData- use ThreadLocalMetaData or MetaData instead
- Deprecated BoundMetaData- use MetaData instead
- Removed DMD and BMD from documentation

""",
u"""
- replaced calls for mapper.props in Query with mapper.get_property(),
which resolves synonyms.  fixes [ticket:598] for join/join_to/join_via/with_parent

""",
u"""
css tweak

""",
u"""
removed superfluous reapplying of options to self

""",
u"""
Merged OrderedDict fixes from r2843 (0.4)

    """,
u"""
improved handling of exceptions upon __init__(): will preserve the stack
trace of the original __init__ exception; errors raised during session.expunge() will be
reported as warnings

""",
u"""
- adjustments to pool locking test to fail on OSX
- restored conditional locking to pool, for all conditions of max_overflow > -1

""",
u"""
added proper cascade for deletes

""",
u"""
- added a mutex to QueuePool's "overflow" calculation to prevent a race 
condition that can bypass max_overflow; merged from 0.4 branch r2736-2738.
also made the locking logic simpler, tried to get the test to create a
failure on OSX (not successful)


    """,
u"""
- MetaData and all SchemaItems are safe to use with pickle.  slow
table reflections can be dumped into a pickled file to be reused later.
Just reconnect the engine to the metadata after unpickling. [ticket:619]


""",
u"""
postgres:
    - added support for reflection of domains [ticket:570]
    - types which are missing during reflection resolve to Null type
      instead of raising an error
    - moved reflection/types/query unit tests specific to postgres to new
      postgres unittest module

      """,
    u"""
eek!  wrong tranasctional command for like, years now....

""",
u"""
added extra session.clear() to enable example to work

""",
u"""
fix to "populate_existing"

""",
u"""
- fix to the "column_prefix" flag so that the mapper does not 
trip over synonyms (and others) that are named after the column's actual
"key" (since, column_prefix means "dont use the key").


""",
u"""
some errors of droppedm mysql connections weren't being caught by the disconnect detecting logic, fixes #625

""",
u"""
better error message for NoSuchColumnError, fix ticket #607

""",
u"""
add missing grouping for compound selects. fixes ticket #623

""",
u"""
fix #624, modulo operator escaping on mysql and postgres
someone should test this with oracle, firebird and sql server also

""",
u"""
fix precedence of between (ticket #621)

    """,
u"""
- fixed precedence of operators so that parenthesis are correctly applied
[ticket:620]
- calling <column>.in_() (i.e. with no arguments) will return 
"CASE WHEN (<column> IS NULL) THEN NULL ELSE 0 END = 1)", so that 
NULL or False is returned in all cases, rather than throwing an error
[ticket:545]


""",
u"""
added test for correlation of scalar subqueries to a JOIN object

""",
u"""
- fixed "where"/"from" criterion of select() to accept a unicode string
in addition to regular string - both convert to text()


    """,
u"""
- added dialect flag "auto_convert_lobs", defaults to True; will cause any
LOB objects detected in a result set to be forced into OracleBinary
so that the LOB is read() automatically, if no typemap was present
(i.e., if a textual execute() was issued).


""",
u"""
- added standalone distinct() function in addition to column.distinct()
[ticket:558]


""",
u"""
- forwards-compatibility with 0.4: added one(), first(), and 
all() to Query
- added selectone_by() to assignmapper


""",
u"""
- added synchronization to the mapper() construction step, to avoid
thread collections when pre-existing mappers are compiling in a 
different thread [ticket:613]


""",
u"""
- fixed very stupid bug when deleting items with many-to-many
uselist=False relations


""",
u"""
orig_set is a Set [ticket:614]

""",
u"""
- finally figured out how to get setuptools version in, available
as sqlalchemy.__version__ [ticket:428]


""",
u"""
- added Interval type to types.py [ticket:595]


""",
u"""
- result.last_inserted_ids() should return a list that is identically
sized to the primary key constraint of the table.  values that were 
"passively" created and not available via cursor.lastrowid will be None.
- sqlite: string PK column inserts dont get overwritten with OID [ticket:603] 


""",
u"""
- datetime fixes: got subsecond TIMESTAMP to work [ticket:604],
added OracleDate which supports types.Date with only year/month/day

""",
u"""
- sqlite better handles datetime/date/time objects mixed and matched
with various Date/Time/DateTime columns


""",
u"""
test case for oracle timestamp adaption

""",
u"""
- Fixed typo blocking some assoc proxy dict assignments, added test

""",
u"""
- Iteration over dict association proxies is now dict-like, not
  InstrumentedList-like (e.g. over keys instead of values).
- Don't tightly bind proxies to source collections (fixes #597)
- Handle slice objects on orderinglist's __setitem__ 

""",
u"""
Multiple MSSQL fixes; see ticket #581
""",
u"""
- MySQL TEXT-derived types weren't respecting convert_unicode, fixes #601
- unicode type test now exercises Unicode() and Unicode(len)

    """,
u"""
added StaticPool, stores just one connection.

""",
u"""
documented eager load fix

""",
u"""
- eager loader calls select_mapper so that poly rulesets get picked up
- changed polymorph example to use a single set of outerjoins

""",
u"""
extra test for corresponding column fix

""",
u"""
- fixed bug where selectable.corresponding_column(selectable.c.col)
would not return selectable.c.col, if the selectable is a join
of a table and another join involving the same table.  messed
up ORM decision making [ticket:593]


""",
u"""
- Rearrange placement of 'fields' (mysql 4.1 reserved word) so that it
  won't accidentally get lost

  """,
u"""
- added 'fields' to reserved words [ticket:590]


""",
u"""
- long-identifier detection fixed to use > rather than >= for 
max ident length [ticket:589]


""",
u"""
pg test wasnt really working with that particular default..its a TODO

""",
u"""
- added filter(), filter_by() to assignmapper


""",
u"""
added reset_joinpoint() feature for query, interim until 0.4

""",
u"""
added interfaces package to orm

""",
u"""
fix running tests on Windows
""",
u"""
include current versions in warning messages.  simplify sqlite_ver test; if a tuple is less than 2,1,3 it is also less than 2,2
""",
u"""
add a couple expository notes to docs; fix a couple rst buglets.  use modern mapper style (i.e., no need to add it to klass as an attribute).
""",
u"""
- Pulling pyformat test for MySQL-python, which fails on 3 driver versions
  (1.2.2b3, 1.2.2c1, 1.2.2)

    """,
u"""
- Emit BOOL rather than BOOLEAN for MySQL booleans in DDL, for old versions
  of MySQL (#583)
- MySQL columns (such as times) with colons in their default values couldn't
  be roundtripped, fixed  (also in Postgres, but not fixed here.)
- BINARY/VARBINARY columns aren't really binary at all on ancient versions
  of MySQL.  The type.Binary(123) passthrough now always makes BLOBs.
  Removed the short-lived MSBaseBinary.
- Added mysql.get_version_info, given a connectable returns a tuple of server
  version info.
- Backed off on the reflection tests for older versions of MySQL, for now.

""",
u"""
0.3.8 version, removed old runhtml script

""",
u"""
- significant speed improvement to ResultProxy, pre-caches
TypeEngine dialect implementations and saves on function calls
per column.  drops the masseagerload test from 80K function calls
to 66K


""",
u"""
- some execution fixes


""",
u"""
some updates

""",
u"""
fix to the backref primary join condition

""",
u"""
added "polymorphic assocaition" example, illustrates how to emulate
Rails' polymorphic associaiton functionality

""",
u"""
fixed two bad __init__ calls

""",
u"""
remove unneeded division

""",
u"""
added hotshot points into unit test, localizes profiling to just the query.select() process.
0.4 branch now has 18% fewer function calls for the same test.

""",
u"""
another object.__init__() call with args....might need to build py2.6 to test this more completely....

""",
u"""
removed ClauseVisitor.__init__(), doesnt work with python trunk

""",
u"""
normalized PG test schema name to "alt_schema"

""",
u"""
- mysql doesnt have + for concatenation, but pg doesnt have concat() (nor does sqlite)
- parameterized masseagerload test

""",
u"""
- Micro-documentation for why we set FOUND_ROWS flag (supports_sane_rowcount)

    """,
u"""
- Coerce 'local_infile' mysql connect argument into an int

""",
u"""
- Nearly all MySQL column types are now supported for declaration and
  reflection. Added NCHAR, NVARCHAR, VARBINARY, TINYBLOB, LONGBLOB, YEAR
- The sqltypes.Binary passthrough now builds a VARBINARY rather than a
  BINARY if given a length
- Refactored the inheritance of some types with respect to sqltypes, and
  especially the binary types
- Lots and lots of docs
- MySQL unit tests now starting to adapt to known problems with alpha/beta
  drivers
- A couple mysql unit test fix-ups and expansions

""",
u"""
- Don't use '+' for sql expr concatenation by default

""",
u"""
- Setup/teardown out test table properly

""",
u"""
- DB connection urls for tests can now be loaded from a configuration file
- Test runs can now --require a particular external package version
- Added some 'coerce' magic to the Oracle connection factory to support use_ansi in the dburl query string

""",
u"""
update

""",
u"""
turned off supports_sane_rowcount until someone wants to fix #370

""",
u"""
CompoundSelect (i.e. UNION etc.) needed self_group() to provide parenthesis

""",
u"""
fix typo

""",
u"""
- improved support for eagerloading of properties off of mappers that are mapped
to select() statements; i.e. eagerloader is better at locating the correct
selectable with which to attach its LEFT OUTER JOIN.
- some fixes to new tests in inheritance5 to work with postgres


""",
u"""
fix to previous logging fix...

""",
u"""
- restored logging of "lazy loading clause" under sa.orm.strategies logger,
got removed in 0.3.7


""",
u"""
restored comparison of 1-element clause list -> ClauseElement, which was broken in [changeset:2620]

""",
u"""
- fixed bug in query.instances() that wouldnt handle more than
on additional mapper or one additional column.


""",
u"""
- removed "no group by's in a select thats part of a UNION"
restriction [ticket:578]


""",
u"""
correct typo

""",
u"""
- the "primary_key" argument to mapper() is propigated to the "polymorphic"
mapper.  primary key columns in this list get normalized to that of the mapper's 
local table.


""",
u"""
- fix to select_by(<propname>=<object instance>) -style joins in conjunction
with many-to-many relationships, bug introduced in r2556 
- the "reverse_direction" flag in _create_lazy_clause works correctly for a many-to-many
relationship (i.e. the reverse is on which clause, not which column in the clause, in the 
case of m2m)

""",
u"""
added test for "assign a list of objects", ensure cascade/persistence functions

""",
u"""
fixed LoggingClauseVisitor

""",
u"""
restored outerjoin test

""",
u"""
- fix to polymorphic query which allows the original polymorphic_union
to be embedded into a correlated subquery [ticket:577]


""",
u"""
- parenthesis are applied to clauses via a new _Grouping construct.
uses operator precedence to more intelligently apply parenthesis
to clauses, provides cleaner nesting of clauses (doesnt mutate
clauses placed in other clauses, i.e. no 'parens' flag)
- added 'modifier' keyword, works like func.<foo> except does not
add parenthesis.  e.g. select([modifier.DISTINCT(...)]) etc.

""",
u"""
- _Label propigates "_hide_froms()" so that scalar selects
behave more properly with regards to FROM clause #574 


""",
u"""
propigated detach() and invalidate() methods to Connection.

""",
u"""
- Connections can be detached from their pool, closing on dereference instead of returning to the pool for reuse

""",
u"""
- set max identifier length to 31

""",
u"""
- fix to long name generation when using oid_column as an order by
(oids used heavily in mapper queries)


    """,
u"""
- session.get() and session.load() propigate **kwargs through to query


""",
u"""
- many-to-many relationships properly set the type of bind params
for delete operations on the association table
- many-to-many relationships check that the number of rows deleted
from the association table by a delete operation matches the expected 
results


""",
u"""
- shored up DBAPI descriptions
- added link to select() docs in sqlconstruction

""",
u"""
clarifying some cascade-based unit tests, adding a little more coverage,
and trying to remove unneeded parts of dependency.py cascades.
also de-emphasizing the whole session.flush([oneobject]) thing since i dont really
agree it should be supported

""",
u"""
- "delete-orphan" no longer implies "delete". ongoing effort to 
separate the behavior of these two operations.


""",
u"""
- _Label class overrides compare_self to return its ultimate object.
meaning, if you say someexpr.label('foo') == 5, it produces
the correct "someexpr == 5".


""",
u"""
Oops, Python 2.5 ternary operator snuck in.
""",
u"""
- Test assoc proxy lazy loads, fixed __set__ race on single scalar assocs

""",
u"""
- New association proxy implementation, implementing complete proxies to list, dict and set-based relation collections (and scalar relations).  Extensive tests.
- Added util.duck_type_collection

""",
u"""
- Aliasizer removed.  hooray !
- ClauseVisitor has handy chain() method.

""",
u"""
- added sqlalchemy.ext.orderinglist, a custom list class that synchronizes an object attribute with that object's position in the list

""",
u"""
- Use Python 2.5's built-in ElementTree if possible

""",
u"""
- Expanded on the MySQL ENUM 'strict' documentation a little bit.
- Oops, clean up after enum unitttest.

""",
u"""
- MySQL ENUM types can now optionally ensure that values are within the
  enum's allowed range on insert and update, with strict=True
- Added new 'dialect' category of unit tests, and migrated MySQL-specific
  dialect tests there.
- Noted the max identifier length in the MySQL dialect (the max alias length,
  actually)

""",
u"""
Removed an unneeded and troublesome subquery test.

""",
u"""
some notes on a labeling issue that arises when label truncation doesnt match col truncation

""",
u"""
- allow MySQL column-level CHARACTER SET and COLLATE, plus shortcuts like
  ASCII, UNICODE, and BINARY.  support NATIONAL.
- added MySQL-specific reserved words
- added tests for MySQL numeric and string column DDL generation
- various minor cleanups, also tweak regex to not break emacs syntax hilighting


""",
u"""
- applied YAGNI to supports_autoclose_results (this issue would be handled by BufferedColumnResultProxy)
- the docstrings, they do not end

""",
u"""
 - small fix to SelectResultsExt to not bypass itself during
      select().


      """,
    u"""
- docstring improvements in query
- added support for __getitem__ on OrderedSet

""",
u"""
0.3.7...

""",
u"""
- adapted gaetan's eager load adaption code for non-mapped column properties

""",
u"""
- restored old "column_property()" ORM function (used to be called
"column()") to force any column expression to be added as a property
on a mapper, particularly those that aren't present in the mapped
selectable.  this allows "scalar expressions" of any kind to be
added as relations (though they have issues with eager loads).


""",
u"""
- the label() method on ColumnElement will properly propigate the
TypeEngine of the base element out to the label, including a label()
created from a scalar=True select() statement.


""",
u"""
added orig_set colleciton to Select when its declared as a scalar, to allow
corresponding_column() to return a result

""",
u"""
- fix to using distinct() or distinct=True in combination with 
join() and similar


""",
u"""
- mysql uses "DESCRIBE [<schemaname>].<tablename>", catching exceptions
if table doesnt exist, in order to determine if a table exists.
this supports unicode table names as well as schema names. tested
with MySQL5 but should work with 4.1 series as well. (#557)


    """,
u"""
- mssql: replace "select @@identity" with "select @@scope_identity". Should help avoid returning wrong ID when insert triggers are used. Also add unit test (thanks paj)
- mssql: if no db-api module specified, probe in the order [pyodbc, pymssql, adodbapi]
""",
u"""
document the 'echo' property

""",
u"""
- added 'url' attribute to Engine
- added docstring to 'echo' attribute

""",
u"""
docstring tweaks

""",
u"""
- CSS change to regular font for docstrings now that we use docutils for formatting
- dynamicmetadata clarification

""",
u"""
- fixed textual select elements that got broke the other day
- docstring work

""",
u"""
sentence clarify

""",
u"""
- support for inline hyperlinks between HTML-generated docstrings
- docstrings for all sql package functions including cross linking.

""",
u"""
extra tests that unneeded UPDATEs dont occur

""",
u"""
removed unneeded closure function

""",
u"""
removed 'unjoined_table', synonymous with local_table

""",
u"""
- the usual adjustments to relationships between inheriting mappers,
in this case establishing relation()s to subclass mappers where
the join conditions come from the superclass' table
- specifically, places where PropertyLoader limits its search to mapper.local_table had to be expanded
to search separately within mapper.mapped_table as well.  in the case of determining primary/secondaryjoin, it starts more specifically first with local table then out to mapped table if not found.  in the case of determining direction, it starts more generally with mapped table, then if ambiguous direction, goes to the local tables.

""",
u"""
correct typo-equivalent mistakes in some comments/docstrings

""",
u"""
- Fully specify ordering for ordered union test comparison

""",
u"""
restored functionality to not issue DELETE for instances that have no _identity_key

""",
u"""
decruftify UOW some more....uowdumper always prints out based on
polymorphic collections

""",
u"""
- generative test doesnt apply to mysql, others
- refactoring to unitofwork.py.  low-hanging cruft 
removed, UOWTask structure simplified particuularly with the 
per-instance sort phase, most methods docstring'ed extensively.
this is a merge from the 'uowsimplify' branch.  (only slightly simpler, tho)
- mapper delete_obj works across multiple mappers to be consistent
with the operation of save_obj

""",
u"""
some extra tests for synonyms to relation()s

""",
u"""
- _with_parent_criterion generalized into _with_lazy_criterion
- _create_lazy_clause now includes a 'reverse_direction' flag to generate lazy criterion
in from parent->child or vice versa
- changed join_by() in query to use the "reverse" _create_lazy_clause for instance comparisons
so conditions like AND can work [ticket:554]

""",
u"""
fixed casing of SET clause

""",
u"""
- Always propagate constructor exceptions in mapped clases (applied patch in #528)

    """,
u"""
- added generative versions of aggregates, i.e. sum(), avg(), etc.
to query. used via query.apply_max(), apply_sum(), etc. 
#552


""",
u"""
revert CSS tweak

""",
u"""
#553 propigate index on copied columns

""",
u"""
some formatting/indentation stuff

""",
u"""
wrap __name__ settings in a try/except for 2.3 compat

""",
u"""
    - assign_mapper names methods according to their keys (i.e. __name__)
      #551


    """,
u"""
- added a col label to help sqlite with order by

""",
u"""
- primary key determination within Join maintains table PK ordering

""",
u"""
- fix to case() construct to propigate the type of the first
WHEN condition as the return type of the case statement
- various unit test tweaks to get oracle working

""",
u"""
added an order_by

""",
u"""
- Fire delrecord events when items are discard()ed from a set-backed
  InstrumentedList, just like remove().

  """,
u"""
dont use assignmapper.flush()

    """,
u"""
- big fix to AssociationProxy so that multiple AssociationProxy
  objects can be associated with a single association collection. 


  """,
u"""
- support for SSL arguments given as inline within URL query string,
prefixed with "ssl_", courtesy terjeros@gmail.com.


""",
u"""
fix for dbapi() method to be classmethod #546

""",
u"""
a rudimental reconnect/pool auto-dispose test.  not super-comprehensive but better
than nothing, will close #516

""",
u"""
- informix support added !  courtesy James Zhang
- tweak to oracle default execution code to use local connection for compilation
- tweak to connection.execute_text() to generate None for parameters when no params sent


""",
u"""
- converted logger.warn() to warnings.warn()
- implemented #302

""",
u"""
non-db identifier length raised arbitrarily high

""",
u"""
more comprehensive query docs

""",
u"""
rewrite....

""",
u"""
- some docstrings
- some more test scenarios for raw bind params

""",
u"""
- Promoted mysql's dburl query string helper to util + fixed
- Coercing sqlite connect args provided in query string to their expected type
  (e.g. 'timeout' as float, fixes #544)
- Coerce mysql's client_flag to int too

""",
u"""
support positional parameters at the execute level even for DBs where we dont expect positional

""",
u"""
unit test with just one param

""",
u"""
some changelog

""",
u"""
- merged in the combined patch for #474, #475, #476 (attached to #476) and a new set of tests

""",
u"""
- fixed issue where slice assignment on relation properties truncates the relation (#529)
- fix for #530, don't require collection classes to respond to len requests

""",
u"""
- tweak to restore Python 2.3 compatability

""",
u"""
some docstrings

""",
u"""
- the "where" criterion of an update() and delete() now correlates
embedded select() statements against the table being updated or
deleted.  this works the same as nested select() statement
correlation, and can be disabled via the correlate=False flag on 
the embedded select().


""",
u"""
- fixed critical issue when, after options(eagerload()) is used,
the mapper would then always apply query "wrapping" behavior
for all subsequent LIMIT/OFFSET/DISTINCT queries, even if no
eager loading was applied on those subsequent queries.


""",
u"""
added "is_disconnect()" for firebird

""",
u"""
- making progress with session.merge() as well as combining its
usage with entity_name [ticket:543]


""",
u"""
note about elixir

""",
u"""
slight cleanup for #498

""",
u"""
- the dialects within sqlalchemy.databases become a setuptools
entry points. loading the built-in database dialects works the
same as always, but if none found will fall back to trying
pkg_resources to load an external module [ticket:521]


""",
u"""
docs/examples for new with_parent() feature

""",
u"""
- added query.with_parent(someinstance) method.  searches for
target instance using lazy join criterion from parent instance.
takes optional string "property" to isolate the desired relation.
also adds static Query.query_from_parent(instance, property)
version. [ticket:541]


""",
u"""
added "recreate()" argument to connection pool classes
this method is called when the invalidate() occurs for a disconnect condition,
so that the entire pool is recreated, thereby avoiding repeat errors on
remaining connections in the pool.
dispose() called as well (also fixed up) but cant guarantee all connections closed.

""",
u"""
- removed meaningless entity_name argument from session.delete()
- session.merge() propigates given entity_name to locate that mapper if the given object
is transient (and therefore has no entity_name)
- some fixes to MockEngine which still is mostly useless for most cases.
- unitofwork test used incorrect session.delete() signature

""",
u"""
- got unicode schemas to work with postgres
- unicode schema with mysql slightly improved, still cant do has_table
- got reflection of unicode schemas working with sqlite, pg, mysql

""",
u"""
more docstrings stuff

""",
u"""
added ansisql docs to output, moved exceptions to a more reasonable location

""",
u"""
didnt need that method...

""",
u"""
some docstrings to provide more detail in the sql package

""",
u"""
- small fix to allow successive compiles of the same SELECT object
which features LIMIT/OFFSET.  oracle dialect needs to modify
the object to have ROW_NUMBER OVER and wasn't performing 
the full series of steps on successive compiles.

""",
u"""
[ticket:534] get dictionary append() method properly

""",
u"""
- the "mini" column labels generated when using subqueries, which
are to work around glitchy SQLite behavior that doesnt understand
"foo.id" as equivalent to "id", are now only generated in the case 
that those named columns are selected from (part of [ticket:513])
- MS-SQL better detects when a query is a subquery and knows not to
generate ORDER BY phrases for those [ticket:513]


""",
u"""
- fix to many-to-many relationships targeting polymorphic mappers
[ticket:533]


""",
u"""
will be 0.3.7

""",
u"""
- some cleanup of reflection unit tests
- removed silly behavior where sqlite would reflect UNIQUE indexes
as part of the primary key (?!)
- added __contains__ support to ColumnCollection; contains_column() method should be removed

""",
u"""
explicit zero was failing for float cols
""",
u"""
- slight tweak to raw execute() change to also support tuples,
not just lists [ticket:523]


""",
u"""
for #516, moved the "disconnect check" step out of pool and back into base.py.  dialects have  
is_disconnect() method now.  simpler design which also puts control of the ultimate "execute" call back into the hands of the dialects.

""",
u"""
- merged the patch from #516 + fixes
- improves the framework for auto-invalidation of connections that have
lost their underlying database - the error catching/invalidate
step is totally moved to the connection pool. 
- added better condition checking for do_rollback() and do_commit() including
SQLError excepetion wrapping

""",
u"""
- merged the "execcontext" branch, refactors engine/dialect codepaths
- much more functionality moved into ExecutionContext, which impacted
the API used by dialects to some degree
- ResultProxy and subclasses now designed sanely
- merged patch for #522, Unicode subclasses String directly, 
MSNVarchar implements for MS-SQL, removed MSUnicode.
- String moves its "VARCHAR"/"TEXT" switchy thing into 
"get_search_list()" function, which VARCHAR and CHAR can override
to not return TEXT in any case (didnt do the latter yet)
- implements server side cursors for postgres, unit tests, #514
- includes overhaul of dbapi import strategy #480, all dbapi
importing happens in dialect method "dbapi()", is only called
inside of create_engine() for default and threadlocal strategies.
Dialect subclasses have a datamember "dbapi" referencing the loaded 
module which may be None.
- added "mock" engine strategy, doesnt require DBAPI module and 
gives you a "Connecition" which just sends all executes to a callable.
can be used to create string output of create_all()/drop_all().


""",
u"""
latest #214 fixups

""",
u"""
- query strings in unicode URLs get keys encoded to ascii
for **kwargs compat

""",
u"""
thank you, SVN, for being completely idiotic and non-intutive. rolling back incorrect checkin to trunk

""",
u"""
current progress with exec branch

""",
u"""
- corresponding to label/bindparam name generataion, eager loaders 
generate deterministic names for the aliases they create using 
md5 hashes.


""",
u"""
added example for expressions in updates

""",
u"""
ordering adjustments

""",
u"""
added keys() to ColumnParameters, needed for setbindparamsizes traversal 

""",
u"""
- sending None as an argument to func.<something> will produce
an argument of NULL


""",
u"""
unit test fix, same child object was being attached to two parents in a one-to-many which produced inconsistent results

""",
u"""
better explicit PK insert checking
""",
u"""
Change to ParameterClause object change
New syntax for adodbapi connection string with port


""",
u"""
error raised if trying to auto-join on a self referential

""",
u"""
added "supports_unicode_statements()" step to dialect/execute_raw so that DB's like oracle can opt out of unicode statement strings

""",
u"""
- column label and bind param "truncation" also generate 
deterministic names now, based on their ordering within the 
full statement being compiled.  this means the same statement
will produce the same string across application restarts and
allowing DB query plan caching to work better.
- cleanup to sql.ClauseParameters since it was just falling
apart, API made more explicit
- many unit test tweaks to adjust for bind params not being 
"pre" truncated, changes to ClauseParameters

""",
u"""
added label truncation for bind param names which was lost in the previous related commit.
added more tests plus test for column targeting with text() clause.

""",
u"""
added LONG->OracleText reflection mapping [ticket:393]

""",
u"""
some more docstring patches for [ticket:214]

""",
u"""
- fix for fetchmany() "size" argument being positional in most
dbapis [ticket:505]


""",
u"""
- fixes [ticket:185], join object determines primary key and removes 
columns that are FK's to other columns in the primary key collection.
- removed workaround code from query.py get()
- removed obsolete inheritance test from mapper
- added new get() test to inheritance.py for this particular issue
- ColumnCollection has nicer string method


""",
u"""
- some logging cleanup
- added 'encodedname' prop to a few ClauseElements to aid logging

""",
u"""
- preliminary support for unicode table and column names added.


""",
u"""
msssql: more unit tests now pass
""",
u"""
- improved/fixed custom collection classes when giving it "set"/
"sets.Set" classes or subclasses (was still looking for append()
methods on them during lazy loads)
- moved CustomCollectionsTest from unitofwork to relationships
- added more custom collections test to attributes module


""",
u"""
- column labels are now generated in the compilation phase, which
means their lengths are dialect-dependent.  So on oracle a label
that gets truncated to 30 chars will go out to 63 characters
on postgres.  Also, the true labelname is always attached as the
accessor on the parent Selectable so theres no need to be aware
of the genrerated label names [ticket:512].
- ResultProxy column targeting is greatly simplified, and relies
upon the ANSICompiler's column_labels map to translate the built-in
label on a _ColumnClause (which is now considered to be a unique
identifier of that column) to the label which was generated at compile
time. 
- still need to put a baseline of ColumnClause targeting for 
ResultProxy objects that originated from a textual query.


""",
u"""
cleanup continued

""",
u"""
various cleanup, docs and things, getting ready for 0.3.6

""",
u"""
documenting generative methods on query

""",
u"""
- MetaData can bind to an engine either via "url" or "engine" kwargs
to constructor, or by using connect() method.  BoundMetaData is 
identical to MetaData except engine_or_url param is required.
DynamicMetaData is the same and provides thread-local connections 
be default.


""",
u"""
dan's latest patch for session.identity_key()

""",
u"""
- CLOB type descends from TEXT so it goes to the dialect correctly
- oracle CLOB has result value LOB handling

""",
u"""
- added explicit MSTimeStamp type which takes effect when using 
types.TIMESTAMP.


""",
u"""
- slightly better support for bind params as column clauses, either
via bindparam() or via literal(), i.e. select([literal('foo')])
- removed "table" argument from column().  this does not add the column
to the table anyway so was misleading.
- Select _exportable_columns() only exports Selectable instances
- Select uses _exportable_columns() when searching for engines
instead of _raw_columns for similar reasons (non selectables have no engine)
- _BindParamClause no longer has a _make_proxy().  its not a ColumnElement.
- _Label detects underlying column element and will generate its own
column()._make_proxy() if the element is not a ColumnElement.  this
allows a Label to be declared for nearly anything and it can export
itself as a column on a containing Selectable.


""",
u"""
contextual_connection()  -> contextual_connect() [ticket:515]

""",
u"""
the "tack on the leftover tasks at the end" step of the "circular dependency sort"
makes a copy of those tasks with the circular_parent marked.  this way the tasks
do not iterate through their child items polymorphically, which is necessary because
the "circular sort" stores individual subclass tasks separately (i.e. saving/deleting
should not traverse polymorhically for those tasks)

""",
u"""
- many-to-many table will be properly handled even for operations that
occur on the "backref" side of the operation [ticket:249]


""",
u"""
mssql: now passes still more unit tests, [ticket:481]
""",
u"""
- added db modules to genned docstrings
- had to tweak out latest MS-SQL module change.  cant do ImportErrors right now until module
importing is moved to the connection phase across all dialects.
- took out "his" from url docstrings
- postgres doesnt do an import * 

""",
u"""
- check for tables in the primaryjoin/secondaryjoin that arent parent of parent/child mappers. 
dont include those clauses when looking for foreign_keys (which also takes care of remote_side).
if those cols are present in foreign_keys, lazyloader makes binds out of them and tries to 
target those columns on the mapper, raising either the "conflicting column" error if they have the same
name, or the "cant find column on mapping" if it has a unique name.  added tests for both.


""",
u"""
mssql: cleanup of module importing code; specifiable DB-API module; more explicit ordering of module preferences. [ticket:480]
""",
u"""
mssql: optionally use VARCHAR(max) instead of TEXT. [ticket:509]
""",
u"""
- flush fixes on self-referential relationships that contain references
to other instances outside of the cyclical chain, when the initial
self-referential objects are not actually part of the flush


""",
u"""
css tag 

""",
u"""
integrated docutils formatting into generated documentation;
restructuredtext fixes throughout docstrings

""",
u"""
merged mako doc generation branch

""",
u"""
- added a catchall **kwargs to MSString, to help reflection of 
obscure types (like "varchar() binary" in MS 4.0)


""",
u"""
"alltests" runners call testbase.main(), which takes an optional suite,
so that exit code is propigated

""",
u"""
literals in PassiveDefault require text()

    """,
u"""
MSSQL now passes still more unit tests [ticket:481]
Fix to null FLOAT fields in mssql-trusted.patch
MSSQL: LIMIT with OFFSET now raises an error
MSSQL: can now specify Windows authorization
MSSQL: ignores seconds on DATE columns (DATE fix, part 1)
    """,
u"""
fix CASE statement when else_ is zero
""",
u"""
- eager loading will not "aliasize" "order by" clauses that were placed 
in the select statement by something other than the eager loader
itself, to fix possibility of dupe columns as illustrated in
[ticket:495].  however, this means you have to be more careful with
the columns placed in the "order by" of Query.select(), that you have
explicitly named them in your criterion (i.e. you cant rely on the
eager loader adding them in for you)

- query._join_to (which powers join, join_via, etc) properly takes
secondary table into account when constructing joins

""",
u"""
- added a handy multi-use "identity_key()" method to Session, allowing
the generation of identity keys for primary key values, instances,
and rows, courtesy Daniel Miller


""",
u"""
some docs

""",
u"""
some formatting

""",
u"""
- for hackers, refactored the "visitor" system of ClauseElement and
SchemaItem so that the traversal of items is controlled by the 
ClauseVisitor itself, using the method visitor.traverse(item).
accept_visitor() methods can still be called directly but will
not do any traversal of child items.  ClauseElement/SchemaItem now 
have a configurable get_children() method to return the collection
of child elements for each parent object. This allows the full
traversal of items to be clear and unambiguous (as well as loggable),
with an easy method of limiting a traversal (just pass flags which
are picked up by appropriate get_children() methods). [ticket:501]
- accept_schema_visitor() methods removed, replaced with
get_children(schema_visitor=True)
- various docstring/changelog cleanup/reformatting

""",
u"""
- oracle:
    - got binary working for any size input !  cx_oracle works fine,
      it was my fault as BINARY was being passed and not BLOB for
      setinputsizes (also unit tests werent even setting input sizes).
    - auto_setinputsizes defaults to True for Oracle, fixed cases where
      it improperly propigated bad types.


      """,
    u"""
- Query has add_entity() and add_column() generative methods.  these
will add the given mapper/class or ColumnElement to the query at compile
time, and apply them to the instances method.  the user is responsible
for constructing reasonable join conditions (otherwise you can get
full cartesian products).  result set is the list of tuples, non-uniqued.
- fixed multi-mapper instances() to pad out shorter results with None so
zip() gets everything

""",
u"""
- the full featureset of the SelectResults extension has been merged
into a new set of methods available off of Query.  These methods
all provide "generative" behavior, whereby the Query is copied
and a new one returned with additional criterion added.  
The new methods include:

  filter() - applies select criterion to the query
  filter_by() - applies "by"-style criterion to the query
  avg() - return the avg() function on the given column
  join() - join to a property (or across a list of properties)
  outerjoin() - like join() but uses LEFT OUTER JOIN
  limit()/offset() - apply LIMIT/OFFSET
  range-based access which applies limit/offset:  
     session.query(Foo)[3:5]
  distinct() - apply DISTINCT
  list() - evaluate the criterion and return results
  
no incompatible changes have been made to Query's API and no methods
have been deprecated.  Existing methods like select(), select_by(),
get(), get_by() all execute the query at once and return results
like they always did.  join_to()/join_via() are still there although
the generative join()/outerjoin() methods are easier to use.

- the return value for multiple mappers used with instances() now returns
a cartesian product of the requested list of mappers, represented
as a list of tuples.  this corresponds to the documented behavior.
So that instances match up properly, the "uniquing" is disabled when 
this feature is used.
- strings and columns can also be sent to the *args of instances() where
those exact result columns will be part of the result tuples.
- query() method is added by assignmapper.  this helps with 
navigating to all the new generative methods on Query.


""",
u"""
cleanup of reversed

""",
u"""
- fixed usage of 2.4-only "reversed" in topological.py [ticket:506]

""",
u"""
- fixed use_alter flag on ForeignKeyConstraint [ticket:503]


""",
u"""
- options() method on SelectResults now implemented "generatively"
like the rest of the SelectResults methods [ticket:472]


""",
u"""
need an "alias()" on map to a select

""",
u"""
decorated ImportError thrown when the <database>:// module isnt found

""",
u"""
added "enable_typechecks=True" flag on relation so the new type check from #500 can be disabled, since people are going to want to disable it.

""",
u"""
- added concept of 'require_embedded' to corresponding_column.
requires that the target column be present in a sub-element of the
target selectable.
- embedded logic above more appropriate for ClauseAdapter functionality
since its trying to "pull up" clauses that represent columns within
a larger union up to the level of the union itself.
- the "direction" test against the "foreign_keys" collection apparently
works for an exact "column 'x' is present in the collection", no proxy
relationships needed.  fixes the case of relating a selectable/alias
to one of its underlying tables, probably fixes other scenarios

""",
u"""
- put an aggressive check for "flushing object A with a collection
of B's, but you put a C in the collection" error condition - 
**even if C is a subclass of B**, unless B's mapper loads polymorphically.
Otherwise, the collection will later load a "B" which should be a "C"
(since its not polymorphic) which breaks in bi-directional relationships
(i.e. C has its A, but A's backref will lazyload it as a different 
instance of type "B") [ticket:500]


""",
u"""
dont continue remote table if warning

""",
u"""
"modernized" polymorph test, name change to "test_roundtrip"

""",
u"""
- bindparam() names are now repeatable!  specify two
distinct bindparam()s with the same name in a single statement,
and the key will be shared.  proper positional/named args translate
at compile time.  for the old behavior of "aliasing" bind parameters
with conflicting names, specify "unique=True" - this option is
still used internally for all the auto-genererated (value-based) 
     bind parameters.    

     """,
    u"""
cleanup; removed "separate foreign key" tests, polymorphic joined-table inheritance requires the same pk col name across tables;
added additional polymorphic load assertions

""",
u"""
- added "fold_equivalents" argument to Join.select(), which removes
'duplicate' columns from the resulting column clause that are known to be 
equivalent based on the join condition.  this is of great usage when 
constructing subqueries of joins which Postgres complains about if 
duplicate column names are present.
- added support to polymorphic stuff for more than one "equivalent column",
when trying to target columns in the polymorphic union; this applies
to multi-leveled inheritance
- put above-two concepts together to get the abc_inheritance tests to work
with postgres

""",
u"""
- use_labels flag on select() wont auto-create labels for literal text
column elements, since we can make no assumptions about the text. to
create labels for literal columns, you can say "somecol AS somelabel",
or use literal_column("somecol").label("somelabel")
- quoting wont occur for literal columns when they are "proxied" into the
column collection for their selectable (is_literal flag is propigated)


    """,
u"""
added a unit test for nested session transactions

""",
u"""
a generating testcase that tests a three-level inheritance chain (A->B->C) and all one-to-many and many-to-one relationships between 
all distinct A,B,C.  still needs support for foreign key to parent table not the same col as the pk col

""",
u"""
this test works with both one to many and many to one, but i think its intended to be one-to-many

""",
u"""
- fixed function execution with explicit connections, when you dont 
explicitly say "select()" off the function, i.e. 
conn.execute(func.dosomething())


    """,
u"""
migrated (most) docstrings to pep-257 format, docstring generator using straight <pre> + trim() func
for now.  applies most of [ticket:214], compliemnts of Lele Gaifax

""",
u"""
- more fixes to polymorphic relations, involving proper lazy-clause
generation on many-to-one relationships to polymorphic mappers 
[ticket:493]


""",
u"""
fix typo

""",
u"""
- added "refresh-expire" cascade [ticket:492]


""",
u"""
- correlated subqueries work inside of ORDER BY, GROUP BY

""",
u"""
- exists() becomes useable as a standalone selectable, not just in a 
WHERE clause


""",
u"""
- a full select() construct can be passed to query.select() (which
worked anyway), but also query.selectfirst(), query.selectone() which
will be used as is (i.e. no query is compiled). works similarly to
sending the results to instances().


""",
u"""
restored sequence back, needed by PG for the unit test

""",
u"""
- added selectfirst(), selectfirst_by() to assign_mapper [ticket:467]

""",
u"""
added collengths to use varchar instead of TEXT

""",
u"""
- removed deprecated method of specifying custom collections on classes;
you must now use the "collection_class" option. the old way was
beginning to produce conflicts when people used assign_mapper(), which
now patches an "options" method, in conjunction with a relationship
named "options". (relationships take precedence over monkeypatched
assign_mapper methods).


""",
u"""
formatting fix

""",
u"""
formatting/cleanup

""",
u"""
  - eager relation loading bug fixed for eager relation on multiple
  descendant classes [ticket:486]


  """,
u"""
Tested with pymssql 0.8.0
mssql: added query_timeout, fixes for passing auto_insert in dburl
""",
u"""
fix to the fix for [ticket:454], prevent other mappers in a load operation from using the main extension option send to the query (i.e. mappers used for eager loads etc).

""",
u"""
- added "contains_alias()" option for result set mapping to an alias of the mapped table


""",
u"""
  - added "alias" argument to contains_eager().  use it to specify the string name
    or Alias instance of an alias used in the query for the eagerly loaded child items.
    easier to use than "decorator"


    """,
u"""
- moved SynonymProperty to interfaces, since its more generalized and synonym-aware operations
take place without knowning so much about properties
- mapper options like eagerload(), lazyload(), deferred(), will work for "synonym()" relationships [ticket:485]


""",
u"""
removed not-always-applicable check for "polymorphic_identity"

""",
u"""
- documented foreign_keys argument
- 0.3.5 markers

""",
u"""
reverted unit test change

""",
u"""
- oracle issues a log warning when a related table cant be reflected due to certain
permission errors [ticket:363]


""",
u"""
Completed previously missed patches from tickets 422 and 415
get unit tests to work with pyodbc [ticket:481]
fix blank password on adodbapi [ticket:371]
""",
u"""
- modified patch for [ticket:379] - detecting synonyms, dblinks in reflection.  test passes
except for DBLINK which I cannot get to work on my oracle-xe database.
- probable (also untested) fix for [ticket:363], better error message if we get None back for
remote table information (which is due to rights)

    """,
u"""
- fixes to tometadata() operation to propigate Constraints at column and table level

""",
u"""
- fixed generation of CHECK constraints on columns [ticket:464]

""",
u"""
- extension() query option propigates to Mapper._instance() method so that 
all loading-related methods get called [ticket:454]

""",
u"""
- moved change for [ticket:466] to ansisql, since thats the syntax for all databases.
the change is across all dialects, not just oracle

""",
u"""
added PGInet type [ticket:444]

""",
u"""
- added a Sequence to the unicode test tables to help Oracle
- fixed named PrimaryKeyConstraint generation on oracle [ticket:466] courtesy andrija at gmail

""",
u"""
[ticket:463] fix to OrderedSet

""",
u"""
commented out ImportError for now; will issue new ticket for handling dialect importerrors more effectively

""",
u"""
- fixed oracle list of binary types to check for their presence in the module (such as BFILE not in all versions of cx_Oracle)
- removed oracle-handicap from binary unit test to test [ticket:435] fix, added an extra row containing None 

""",
u"""
- small fix to BoundMetaData to accept unicode or string URLs

""",
u"""
better MSSSQL support for implicit sequences and auto-insert, ticket 415
""",
u"""
Fix Fix for adodbapi bug introduced by ticket 419

""",
u"""
Func rewrite for better unittest compatibility
Simplified transaction handling for pymssql
""",
u"""
dont do RAWTOHEX on None

""",
u"""
- some cleanup to the unitofwork test suite (needs much more)
- fixed relationship deletion error when one-to-many child item is moved to a new 
  parent in a single unit of work [ticket:478]


  """,
u"""
revert old unittest patch for MSSQL
""",
u"""
MSSSQL is now passing unit tests (well, some) thanks to Paul Johnston
""",
u"""
run-time selectable DB-API modules for mssql [ticket:419]
preliminary support for pyodbc
""",
u"""
Fix for ticket 473
""",
u"""
Fix query.get for MSSQL tables with schema specified
""",
u"""
- fixed relationship deletion error where parent/child with a single column as PK/FK 
on the child would raise a "blank out the primary key" error, if manually deleted
or "delete" cascade without "delete-orphan" was used


""",
u"""
- fixed argument passing to straight textual execute() on engine, connection.
can handle *args or a list instance for positional, **kwargs or a dict instance
for named args, or a list of list or dicts to invoke executemany()


    """,
u"""
- fix for very large topological sorts, courtesy ants.aasma at gmail [ticket:423]


""",
u"""
- added support for py2.5 "with" statement with SessionTransaction [ticket:468]

""",
u"""
- added options() method to SelectResults, equivalent to query.options() [ticket:472]

""",
u"""
- implemented foreign_keys argument on relation() [ticket:385]
- PropertyLoader figures out accurate remote_side collection based 
on foreign_keys, legacy foreignkey, primary/secondaryjoin/polymorphic
- reworked lazyloader, sync to work straight off foreign_keys/
remote_side collections

""",
u"""
removed MissingTypeError (think it was an accidental checkin)

    """,
u"""
- added optional __table_opts__ dictionary to ActiveMapper, will send kw options to 
Table objects [ticket:462]

""",
u"""
ticket 298 plus transaction fixes for pymssql
""",
u"""
- added PGInterval type [ticket:460]


""",
u"""
- fixed "remote_side" in testrelationonbaseclass [ticket:461]
- added --reversetop arg to testbase to allow reversing the input collection 
for topological sorts, to better reveal dependency issues

""",
u"""
- added PrefetchingResultProxy support to pre-fetch LOB columns when they are 
known to be present, fixes [ticket:435]

""",
u"""
- added distinct() method to SelectResults.  generally should only make a difference
  when using count().


  """,
u"""
nested query will always use order_by even if distinct is present, added test case to back it up

""",
u"""
make sure auto-reflection of remote tables working too...

""",
u"""
- added "schema" argument to all has_table() calls, only supported so far by PG
- added basic unit test for PG reflection of tables in an alternate schema

""",
u"""
alternate OrderedSet implementation courtesy sdobrev

""",
u"""
added 'ascii' as default encoding in case getdefaultlocale()[1] comes up with None (see [ticket:457])

""",
u"""
added mockdbapi to mysql dialect create to better help unit tests pass

""",
u"""
polymorphic union uses the literal_column function for its "textual" column

""",
u"""
- added literal_column() to specify a column clause that should not undergo any quoting
- straight text sent to select() added as literal_column
- fix for issue in [ticket:450]

""",
u"""
OK nevermind that last commit, rolling the quoting fix back

""",
u"""
- more quoting fixes for [ticket:450]...quoting more aggressive (but still skips already-quoted literals)
- got mysql to have "format" as default paramstyle even if mysql module not available, allows unit tests
to pass in non-mysql system for [ticket:457].  all the dialects should be changed to pass in their usual
paramstyle.

""",
u"""
- sequences on a non-pk column will properly fire off on INSERT for PG/oracle


""",
u"""
unit test for "cant execute"

""",
u"""
- added a "supports_execution()" method to ClauseElement, so that individual
kinds of clauses can express if they are appropriate for executing...such as, 
you can execute a "select", but not a "Table" or a "Join".


""",
u"""
removed extra _find_cycles call

""",
u"""
added unit test for previous checked in lazy fix

""",
u"""
- clear_mappers() just blows away all of ArgSingleton for now
- lazy clause goes against parent.mapped_table instead of parent.local_table, 
helps it to recognize self-referential condition between a descendant joined-table-inheritance mapper

""",
u"""
- the "polymorphic_primaryjoin" again goes against the parent's non-polymorphic local table.  
lazy load clause evaluation is plenty solid enough to handle it this time.  
- the join_to() method on PropertyLoader takes the parent mapper as an argument and alisiazes
the primaryjoin against that mapper's selectable, so that the same primary join can be used against
the base mapper, any inheriting mapper, etc., whether or not it uses a polymorphic union (although
needs to be tested against alternate polymorphic unions added on subclasses).  fixes [ticket:448]

""",
u"""
- improved support for complex queries embedded into "where" criterion
 for query.select() [ticket:449]
- contains_eager('foo') automatically implies eagerload('foo')
- query.options() can take a combiantion MapperOptions and tuples of MapperOptions,
so that functions can return groups
- refactoring to Aliasizer and ClauseAdapter so that they share a common base methodology,
which addresses all sql.ColumnElements instead of just schema.Column.  common list-processing
methods added.
- query.compile and eagerloader._aliasize_orderby make usage of improved list processing on
above.
- query.compile, within the "nested select generate" step processes the order_by clause using 
the ClauseAdapter instead of Aliasizer since there is only one "target"


""",
u"""
added types to genned docs

""",
u"""
clarification to detached state

""",
u"""
- fix to deferred so that load operation doesnt mistakenly occur when only
PK col attributes are set

""",
u"""
further work on insuring clear_mappers() really works.  assignmapper identified
as a much trickier thing to clean out.  added a unit test so that if any new collections get introduced
we are still testing.

""",
u"""
- fixed bug where cascade operations incorrectly included deleted collection
items in the cascade [ticket:445]

""",
u"""
doc

""",
u"""
updated docs for delete()

    """,
u"""
reset managed attributes on mapped classes when clear_mappers called

""",
u"""
empty out ClassKey registry when clear_mappers() is called

""",
u"""
fixes to quoting on "fake" column when used off its table

""",
u"""
removed erroneous "lazy"

""",
u"""
removed various print statements

""",
u"""
added regexp search for "schema" in sequence reflection for [ticket:442], courtesy david.mugnai@spacespa.it

""",
u"""
merged the polymorphic relationship refactoring branch in.  i want to go further on that branch and introduce the foreign_keys argument, and further centralize the "intelligence" about the joins and selectables into PropertyLoader so that lazyloader/sync can be simplified, but the current branch goes pretty far.
  - relations keep track of "polymorphic_primaryjoin", "polymorphic_secondaryjoin" which it derives from the plain primaryjoin/secondaryjoin.
  - lazy/eagerloaders work from those polymorphic join objects.
  - the join exported by PropertyLoader to Query/SelectResults is the polymorphic join, so that join_to/etc work properly.
  - Query builds itself against the base Mapper again, not the "polymorphic" mapper.  uses the "polymorphic" version
 only as appropriate.  this helps join_by/join_to/etc to work with polymorphic mappers.
  - Query will also adapt incoming WHERE criterion to the polymorphic mapper, i.e. the "people" table becomes the "person_join" automatically.
  - quoting has been modified since labels made out of non-case-sensitive columns could themselves require quoting..so case_sensitive defaults to True if not otherwise specified (used to be based on the identifier itself).
  - the test harness gets an ORMTest base class and a bunch of the ORM unit tests are using it now, decreases a lot of redundancy.

  """,
u"""
fixed "eager=True"

""",
u"""
- added a standardized test harness for ORM tests
- added three-level mapping test.  needed some massaging for postgres

""",
u"""
- fix for multi-level polymorphic mappers

""",
u"""
- eager relation to an inheriting mapper wont fail if no rows returned for
the relationship.

""",
u"""
added a close() to the single SQL execute, useful for testing pool behavior with the ORM

""",
u"""
removed print line

""",
u"""
pool_size was there already of course :-|
""",
u"""
r/m unused import
""",
u"""
add pool_size to "list of all standard options"
""",
u"""
- fix to reflection on older DB's that might return array() type for 
"show variables like" statements

""",
u"""
- calling corresponding_column with keys_ok matches columns on name, not key, since
the name is meaningful with regards to SQL relationships, the key is not
- adjustments to the recent polymorphic relationship refactorings, specifically
for many-to-one relationships to polymorphic unions that did not contain the 
base table [ticket:439].  the lazy/eager clause adaption to the selectable
will match up on straight column names (i.e. its a more liberal policy)
- lazy loader will not attempt to adapt the clause to the selectable if 
loads_polymorphic is not enabled, since the more liberal policy of adapting 
columns fails for more elaborate join conditions
- will have to see if ppl want to do complex joins with polymorphic relations...
may have to add "polymorphic_primaryjoin" in that case as a last resort (would make
working around these issues a snap, tho...)

""",
u"""
added unit tests illustrating current workaround for assignmapper method name/collection class collision

""",
u"""
raise exception if invalid collection class used

""",
u"""
changeset

""",
u"""
oracle can conditionally decide if it wants to say "use rowid" in a select statement.
needs to be tweaked vs. when ROW NUMBER OVER ORDER BY is being used, but currently
fixes [ticket:436]

""",
u"""
note support for LIMIT in firebird and mssql
""",
u"""
formatting

""",
u"""
test patches from [ticket:422]

""",
u"""
- *slight* support for binary, but still need to figure out how to insert reasonably large
values (over 4K).  requires auto_setinputsizes=True sent to create_engine(), rows must
be fully fetched individually, etc.


""",
u"""
attempting to get oracle binary working

""",
u"""
0.3.4

""",
u"""
- added support for column "key" attribute to be useable in row[<key>]/row.<key>

""",
u"""
justify text
""",
u"""
add example of joining to labeled table
""",
u"""
split out SelectableClassType from TableClassType, so we don't have to do an isinstance check for each dml op
""",
u"""
relationships no longer compile against the "selectable" mapper (i.e. the polymorphic mapper).  join conditions, foreign keys etc. are configured against the actual mappers used in the relationship in all cases.  the lazy and eager loaders in turn "adapt" their lazy/eager clauses to that of the "selectable" mapper if one is present.  this is because the join conditions between the mapper's base tables are *far* easier to work with and detect direction etc. compared to an enormous polymorphic union; dealing with the polymorphic union is pushed further out into select query construction.

""",
u"""
added "instances" to assign_mapper funcs  [ticket:433]

""",
u"""
added a session transaction test

""",
u"""
oops, change from yesterday fails the zblog tests...now i understand !

""",
u"""
better error message from [ticket:429]

""",
u"""
added merge unit test from [ticket:430]

""",
u"""
added recursion check to merge

""",
u"""
selectby -> select_by
""",
u"""
docs:  [ticket:345], [ticket:356], [ticket:48], [ticket:403], [ticket:394],
cleanup/completion of keyword arg documentation for create_engine(), mapper(), and
relation()

    """,
u"""
- mysql table create options work on a generic passthru now, i.e. Table(..., mysql_engine='InnoDB',
mysql_collate="latin1_german2_ci", mysql_auto_increment="5", mysql_<somearg>...), 
helps [ticket:418]

""",
u"""
- added "validate=False" argument to assign_mapper, if True will insure that only mapped
attributes are named [ticket:426]

""",
u"""
starting to refactor adaptation of inherited properties out of the MapperProperty and into the mapper for now

""",
u"""
- tightened down conditions used to locate "relation direction", associating
  the "foreignkey" of the relationship with the "primaryjoin".  the column match now
  must be exact, not just "corresponding".  this enables self-referential relationships on a
  polymorphic mapper.
  - a little bit of improvement to the concept of a "concrete" inheritance mapping, though that concept
  is not well fleshed out yet (added test case to support concrete mappers on top of a polymorphic base).

  """,
u"""
removed

""",
u"""
- fix to "proxy=True" behavior on synonym()

""",
u"""
- trailing underscores are trimmed from func.<xxx> calls, such as func.if_()

    """,
u"""
- changed "BooleanExpression" to subclass from "BinaryExpression", so that boolean
expressions can also follow column-clause behaviors (i.e. label(), etc).
- query.select() had to become more picky about what it considers to be a full "selectable"
and what it considers to be a fragment that represents a WHERE criterion - looks for the presence
of a FromClause now (which is still pretty liberal, since i originally intended the check to be
for select() only).  the previous exception-catch method also added a little stack tracing 
overhead anyway.

""",
u"""
- fixed bug where delete-orphan basically didn't work with many-to-many relationships [ticket:427],
backref presence generally hid the symptom

""",
u"""
added testcase for upcoming ticket

""",
u"""
- another fix to subquery correlation so that a subquery which has only one FROM
element will *not* correlate that single element, since at least one FROM element is 
required in a query.

""",
u"""
has_table wasnt handling case-sensitive table names

""",
u"""
 - some deeper error checking when compiling relations, to detect an ambiguous "primaryjoin"
 in the case that both sides of the relationship have foreign key references in the primary
 join condition

 """,
u"""
removed unnecessary value grab

""",
u"""
tweaks

""",
u"""
updates, verbiage

""",
u"""
- fix to the initial checkfirst for tables to take current schema into account [ticket:424]

""",
u"""
document "Accessing the Session"
""",
u"""
added testcase to ensure that type gets propigated from scalar subquery to its label

""",
u"""
added "options" to exported query API

""",
u"""
verbiage updates, this is a work-in-progress (WIP)

    """,
u"""
- added optional constructor to sql.ColumnCollection
- mapper sets its "primary_key" attribute to be the ultimately decided primary_key column collection post-compilation
- added compare() method to MapperProperty, defines a comparison operation of the columns represented by the property to some value
- all the above combines into today's controversial feature: saying query.select_by(somerelationname=someinstance) will create the join of the primary key columns represented by "somerelationname"'s mapper to the actual primary key in "someinstance".
- docs for the above

""",
u"""
- trying to redefine a reflected primary key column as non-primary key raises an error

""",
u"""
[ticket:398]

""",
u"""
- default cascade is "save-update, merge"
- added another merge unit test

""",
u"""
- postgres cursor option is now server_side_cursors=False; some users get bad results using them
so theyre off by default
- type system slightly modified to support TypeDecorators that can be overridden by the dialect
- added an NVarchar type to mssql (produces NVARCHAR), also MSUnicode which provides Unicode-translation
for the NVarchar regardless of dialect convert_unicode setting.


""",
u"""
- basic idea of "session.merge()" actually implemented.  needs more testing.

""",
u"""
more insure->ensure.  this is going to be a hard habit to break...

""",
u"""
- mysql is inconsistent with what kinds of quotes it uses in foreign keys during a
  SHOW CREATE TABLE, reflection updated to accomodate for all three styles [ticket:420]


  """,
u"""
  - added "fetchmany()" support to ResultProxy

  """,
u"""
- postgres no longer uses client-side cursors, uses more efficient server side
  cursors via apparently undocumented psycopg2 behavior recently discovered on the
  mailing list.  disable it via create_engine('postgres://', client_side_cursors=True)

  """,
u"""
add test for max_order non_primary mapper from the list today
""",
u"""
- the "op()" function is now treated as an "operation", rather than a "comparison".
  the difference is, an operation produces a BinaryExpression from which further operations
  can occur whereas comparison produces the more restrictive BooleanExpression


  """,
u"""
brief mention of defer, undefer
""",
u"""
added SVN link to setup.py description

""",
u"""
typo fix (thanks Paul J)
    """,
u"""
- added a mutex to the mapper compilation step.  ive been reluctant to add any kind
of threading anything to SA but this is one spot that its its really needed since mappers
are typically "global", and while their state does not change during normal operation, the 
initial compilation step does modify internal state significantly, and this step usually
occurs not at module-level initialization time (unless you call compile()) but at first-request 
time
- added "compile_mappers()" function as a shortcut to compiling all mappers


""",
u"""
tweak to support reflecting eqlite columns that didnt specify a type

""",
u"""
- added an error message if you actually try to modify primary key values on an entity
and then flush it.

""",
u"""
copyright update

""",
u"""
- default "timezone" setting is now False.  this corresponds to Python's datetime
behavior as well as Postgres' timestamp/time types (which is the only timezone-sensitive
dialect at the moment) [ticket:414]

""",
u"""
- fix to post_update to insure rows are updated even for non insert/delete scenarios 
[ticket:413]

""",
u"""
Removed "burned-in" schema name of "dbo". Suggested by janezj
""",
u"""
Patch from Paul Johnston that refactors adodbapi vs. pymssql a bit, fixes broken COMMITS in adodbapi
""",
u"""
- Firebird fix to autoload multifield foreign keys [ticket:409]
- Firebird NUMERIC type properly handles a type without precision [ticket:409]

""",
u"""
- order of constraint creation puts primary key first before all other constraints;
required for firebird, not a bad idea for others [ticket:408]

""",
u"""
- fixed bug in mapper refresh/expire whereby eager loaders didnt properly re-populate
item lists [ticket:407]

""",
u"""
- added "none" to the list of cascades, although im not sure if we should really allow "none" since it currently doesnt do anything (what should it do, cancel out the other cascades?)

""",
u"""
- invalid options sent to 'cascade' string will raise an exception [ticket:406]

""",
u"""
- global "insure"->"ensure" change.  in US english "insure" is actually
largely interchangeable with "ensure" (so says the dictionary), so I'm not 
completely illiterate, but its definitely sub-optimal to "ensure" which is
non-ambiguous.


""",
u"""
- speed enhancements to ORM object instantiation, eager loading of rows

""",
u"""
- fix to correlation of subqueries when the column list of the select statement
is constructed with individual calls to append_column(); this fixes an ORM
bug whereby nested select statements were not getting correlated with the
main select generated by the Query object.


""",
u"""
- fixes to postgres reflection to better handle when schema names are present;
thanks to jason (at) ncsmags.com [ticket:402]

""",
u"""
- fix to MapperExtension create_instance so that entity_name properly associated
with new instance

""",
u"""
reversing last commit
""",
u"""
added missing ref to between in sql.py __all__
""",
u"""
- added "BIGSERIAL" support for postgres table with PGBigInteger/autoincrement

""",
u"""
PGBigInteger subclasses PGInteger so it gets used

""",
u"""
edits

""",
u"""
formatting

""",
u"""
fixed the raise for mysql to re-raise the error

""",
u"""
fix to the fix for [ticket:396] plus a unit test

""",
u"""
added additional unit test to test that commit errors are detected, rollback occurs in an except:

""",
u"""
added InnoDB for mysql so that all tranactional tests pass for mysql

""",
u"""
- patch that makes MySQL rowcount work correctly! [ticket:396]

""",
u"""
- fixed QueuePool bug whereby its better able to reconnect to a database
that was not reachable, also fixed dispose() method


""",
u"""
new collections example

""",
u"""
- fixes to passive_deletes flag, lazy=None (noload) flag
- added example/docs for dealing with large collections
- added object_session() method to sqlalchemy namespace


""",
u"""
- string-based FROM clauses fixed, i.e. select(..., from_obj=["sometext"])

""",
u"""
added style for page control

""",
u"""
moved page control links

""",
u"""
would help to have the files all checked in....

""",
u"""
removing references to 0.2 series from docs
upgrade version number to 0.3.2

""",
u"""
clarify docs for query.instances() [ticket:386]

""",
u"""
docstring fix for [ticket:381]

""",
u"""
- MySQL bool type fix: [ticket:307]

""",
u"""
added SmallInteger to __all__ list (now we have both SmallInteger/Smallinteger.....)

    """,
u"""
- added onupdate and ondelete keyword arguments to ForeignKey; propigate
to underlying ForeignKeyConstraint if present.  (dont propigate in the
other direction, however)
- patched attribute speed enhancement [ticket:389] courtesy Sebastien Lelong

""",
u"""
- support for None as precision/length in numeric types for postgres, sqlite, mysql
- postgres reflection fixes: [ticket:349] [ticket:382]

""",
u"""
- unit test for strong refs
- unit test to test [ticket:354]

""",
u"""
- identity map in Session is by default *no longer weak referencing*.
to have it be weak referencing, use create_session(weak_identity_map=True)
- some fixes to OrderedProperties

""",
u"""
pickle example for dmiller

""",
u"""
fix in OrderedProperties to allow pickling

""",
u"""
cursors needs to be weak key

""",
u"""
docs/examples/unittests for remote_side

""",
u"""
 the pool fix is more important

 """,
u"""
assign_mapper note

""",
u"""
- fix to connection pool _close() to properly clean up, fixes
MySQL synchronization errors [ticket:387]

""",
u"""
- MySQL detects errors 2006 (server has gone away) and 2014
(commands out of sync) and invalidates the connection on which it occured.


""",
u"""
moved _impl_dict to an external weakref so that TypeEngine objects can be pickled

""",
u"""
got a rudimentary one-page display going

""",
u"""
doc adjust for "dirty" list behavior

""",
u"""
made backrefs aware of "post_update" and "viewonly" so it doesnt have to be explicitly propigated; also backrefs shouldnt fire off in a post_update situation.

""",
u"""
fixed up some debug logging to be conditional, adds speed.  made some
attribute-related lambdas more direct.

""",
u"""
removed useless line

""",
u"""
added 'remote_side' functionality  to lazy clause generation

""",
u"""
- added "remote_side" argument to relation(), used only with self-referential
mappers to force the direction of the parent/child relationship.  replaces
the usage of the "foreignkey" parameter for "switching" the direction;
while "foreignkey" can still be used to "switch" the direction of a parent/
child relationship, this usage is deprecated; "foreignkey" should always
indicate the actual foreign key columns from now on.


""",
u"""
added mass eagerloading profile, debug log in EagerLoader conditional based on flag

""",
u"""
added conditional flag to debug log statements in mapper so that string formats dont occur
updated massload test to work with 0.3

""",
u"""
- improved support for disabling save-update cascade via cascade="none" etc.

""",
u"""
- sending a selectable to an IN no longer creates a "union" out of multiple
selects; only one selectable to an IN is allowed now (make a union yourself
if union is needed; explicit better than implicit, dont guess, etc.)


""",
u"""
- fix to session.update() to preserve "dirty" status of incoming object

""",
u"""
oops, KeyError fix for [ticket:380]

""",
u"""
fixed has_key exception to be KeyError [ticket:380]

""",
u"""
- added extra check to "stop" cascading on save/update/save-update if
an instance is detected to be already in the session.

""",
u"""
added label() function to Select class, useable only with select
that has scalar=True

""",
u"""
removed old function

""",
u"""
- made kwargs parsing to Table strict; removed various obsoluete "redefine=True" kw's from the unit tests
- documented instance variables in ANSICompiler
- fixed [ticket:120], adds "inline_params" set to ANSICompiler which DefaultDialect picks up on when 
determining defaults.  added unittests to query.py
- additionally fixed up the behavior of the "values" parameter on _Insert/_Update
- more cleanup to sql/Select - more succinct organization of FROM clauses, removed silly _process_from_dict 
methods and JoinMarker object


""",
u"""
some clenaup on the "correlation" API on the _Select class

""",
u"""
- cleanup on some instance vars in Select (is_scalar, is_subquery, _froms is __froms, removed unused 'nowait', '_text', etc)
- cleaned up __repr__ on Column, AbstractTypeEngine
- added standalone intersect(_all), except(_all) functions, unit tests illustrating nesting patterns [ticket:247]

""",
u"""
added mapper return value to assign_mapper

""",
u"""
fix to oracle types test, added RAW type [ticket:378]

""",
u"""
fix to previous checkin

""",
u"""
[ticket:373]

""",
u"""
[ticket:366]

""",
u"""
[ticket:374] [ticket:377] [ticket:375], small fix to mutable types unit test

""",
u"""
copyright date....

""",
u"""
added extra pickle unittest to insure update occurs/doesnt occur appropriately

""",
u"""
reflect from table.fullname for schema support

""",
u"""
its that time

""",
u"""
tweaks to get module functions links to work

""",
u"""
edits

""",
u"""
one of those non-2.3 generators got in there...

""",
u"""
edits

""",
u"""
- create_engine() reworked to be strict about incoming **kwargs.  all keyword
arguments must be consumed by one of the dialect, connection pool, and engine
constructors, else a TypeError is thrown which describes the full set of
invalid kwargs in relation to the selected dialect/pool/engine configuration.

""",
u"""
further refactoring of topological sort for clarity

""",
u"""
more fixes to topological sort with regards to cycles, fixes [ticket:365]

""",
u"""
patched **kwargs enhancement for [ticket:361]

""",
u"""
fix to query.count to use mapper-defined primary key cols instead of those of the table

""",
u"""
- "delete-orphan" for a certain type can be set on more than one parent class;
the instance is an "orphan" only if its not attached to *any* of those parents
- better check for endless recursion in eagerloader.process_row

""",
u"""
create_args->connect_args

""",
u"""
fix: auto_identity_insert was not working with non-list insert parms
""",
u"""
removed 'redefine' from docstring

""",
u"""
- fix to subtle condition in topological sort where a node could appear twice,
for [ticket:362]

""",
u"""
- improvement to single table inheritance to load full hierarchies beneath 
the target class

""",
u"""
- added an assertion within the "cascade" step of ORM relationships to check
that the class of object attached to a parent object is appropriate
(i.e. if A.items stores B objects, raise an error if a C is appended to A.items)
- new extension sqlalchemy.ext.associationproxy, provides transparent "association object"
mappings.  new example examples/association/proxied_association.py illustrates.
- some example cleanup

""",
u"""
ExtensionOption needed to extend from MapperOption

""",
u"""
- implemented from_obj argument for query.count, improves count function
on selectresults [ticket:325]


""",
u"""
some example cleanup

""",
u"""
added graphing example

""",
u"""
link to SqlSoup docs on the wiki
""",
u"""
- fixed bug in circular dependency sorting at flush time; if object A
contained a cyclical many-to-one relationship to object B, and object B
was just attached to object A, *but* object B itself wasnt changed,
the many-to-one synchronize of B's primary key attribute to A's foreign key
attribute wouldnt occur.  [ticket:360]


""",
u"""
- fixed bug where eagerload() (nor lazyload()) option didn't properly
instruct the Query whether or not to use "nesting" when producing a
LIMIT query.


""",
u"""
- fixed direct execution of Compiled objects

""",
u"""
raise InvalidRequest when asked to perform DDL on non-Tables
""",
u"""
smarter name generation (handles self-referencing Select); new example of using Soup.map
""",
u"""
figured out how a Select can be in its own _froms list, changed assertion to just a continue

""",
u"""
- fix to postgres sequence quoting when using schemas

""",
u"""
fixed binary types test to use two binary files specifically for testing, instead of 
attempting to grab .pyc files

""",
u"""
further fixes to sqlite booleans, weren't working as defaults

""",
u"""
added assertion to check that mappers only inherit from a mapper with the same "primary/non-primary" setting

""",
u"""
added system return code to base runtest

""",
u"""
converted imports to absolute

""",
u"""
add join explanation for myisam
""",
u"""
- MySQL catches exception on "describe" and reports as NoSuchTableError

""",
u"""
oops, removed pool debugging code

""",
u"""
- SingletonConnectionPool must use the "threadlocal" pooling behavior
- the "delete" cascade will load in all child objects, if they were not
loaded already.  this can be turned off (i.e. the old behavior) by setting
passive_deletes=True on a relation().


""",
u"""
- some new Pool utility classes, updated docs
- "use_threadlocal" on Pool defaults to False (same as create_engine)


""",
u"""
log connection closes

""",
u"""
- eager query generation adjustment, [ticket:355]

""",
u"""
fixed the example, because my brain goes blank when i work on that page,
and fixed exceptions raised in sync.py

""",
u"""
association mappings are now simpler, updated docs

""",
u"""
expired instances will get mapper extension's populate_instance behavior when reloaded, if present

""",
u"""
fully reST-ify doctests
""",
u"""
set global 'sqlalchemy' log level to ERROR so it is insulated from other logging configs [ticket:353]

""",
u"""
integrated coverage.py into unittest suite

""",
u"""
"circular mapping" is out, SA figures that stuff out for you

""",
u"""
fixed some imports, transaction hanging open

""",
u"""
added string length to avoid LOB col type in oracle

""",
u"""
updating the cycles test

""",
u"""
updates to oracle
added more ordering to schema collections for better predictability

""",
u"""
misc

""",
u"""
docstring

""",
u"""
.

""",
u"""
more on non-threadsafeness

""",
u"""
docs about objects not being threadsafe

""",
u"""
renamed Column/ColumnClause "hidden" to "_is_oid"

""",
u"""
added __getattr__() proxy to TypeDecorator

""",
u"""
- attributes module and test suite moves underneath 'orm' package
- fixed table comparison example in metadata.txt
- docstrings all over the place
- renamed mapper _getattrbycolumn/_setattrbycolumn to get_attr_by_column,set_attr_by_column
- removed frommapper parameter from populate_instance().  the two operations can be performed separately
- fix to examples/adjacencytree/byroot_tree.py to fire off lazy loaders upon load, to reduce query calling
- added get(), get_by(), load() to MapperExtension
- re-implemented ExtensionOption (called by extension() function)
- redid _ExtensionCarrier to function dynamically based on __getattribute__
- added logging to attributes package, indicating the execution of a lazy callable
- going to close [ticket:329]

""",
u"""
- docstring on polymorphic_mapping
- applied Simon Wittber's ActiveMapper version_id_col patch for [ticket:348]

""",
u"""
re-implemented extension option

""",
u"""
tweak for Table.create() not having a return value

""",
u"""
ugh, restored brackets

""",
u"""
docstrings

""",
u"""
took out unused formatting

""",
u"""
take those 2.4 generators out....

""",
u"""
merge of new documentation generation system

""",
u"""
some docstring stuff

""",
u"""
fixed pg reflection of timezones

""",
u"""
got linking of classes to work.  but what a mess the doc code is now.

""",
u"""
more doc

""",
u"""
dev

""",
u"""
fix for sqlite refection of names with weird quotes around them in the DDL which seem to hang around

""",
u"""
- cleanup to the last commit
- added contains_eager() MapperOption, used in conjunction with
instances() to specify properties that should be eagerly loaded
from the result set, using their plain column names by default, or translated
given an custom row-translation function. [ticket:347].


""",
u"""
progress on [ticket:329]

""",
u"""
various huge fixes from [ticket:330], thanks to Lele Gaifax

""",
u"""
fixed __repr__ style to be inline with python style guide [ticket:341]

""",
u"""
- [ticket:346], session closing the connection on flush
- added unicode assertion for sqlite

""",
u"""
if type is None it will be propigated from a ForeignKey

""",
u"""
typo

""",
u"""
synonym does not create the proxying behavior unless the flag 'proxy=True' is set up

""",
u"""
restored "synonym" property

""",
u"""
lazy clause generation can handle comparisons of column-containing expressions such as functions, within a limited scope

""",
u"""
ok, TableClause should be public

""",
u"""
reorganizing classnames a bit, flagging "private" classes in the sql package, 
getting the generated docs to look a little nicer.
fixes to extensions, sqlsoup etc. to be compatible with recent API tweaks

""",
u"""
latest markdown, added "bold link" style to doc generator

""",
u"""
- added "column_prefix=None" argument to mapper; prepends the
given string (typically '_') to column-based attributes automatically
set up from the mapper's Table


""",
u"""
quote function names

""",
u"""
strings and unicodes are compared via == rather than 'is'.
TypeDecorator uses underlying impl for mutator/comparison functions by default

""",
u"""
docstrings etc

""",
u"""
apparently re.S makes things go b00m

""",
u"""
tweaks...

""",
u"""
de-cruftification

""",
u"""
doc tweaks

""",
u"""
dev

""",
u"""
doc stuff regarding engine strategies

""",
u"""
- ForeignKey(Constraint) supports "use_alter=True", to create/drop a foreign key
via ALTER.  this allows circular foreign key relationships to be set up.


""",
u"""
fixup of the tutorial, doc tester with the new logging stuff

""",
u"""
- a fair amount of cleanup to the schema package, removal of ambiguous
methods, methods that are no longer needed.  slightly more constrained
useage, greater emphasis on explicitness.
- table_iterator signature fixup, includes fix for [ticket:288]
- the "primary_key" attribute of Table and other selectables becomes
a setlike ColumnCollection object; is no longer ordered or numerically
indexed.  a comparison clause between two pks that are derived from the 
same underlying tables (i.e. such as two Alias objects) can be generated 
via table1.primary_key==table2.primary_key
- append_item() methods removed from Table and Column; preferably
construct Table/Column/related objects inline, but if needed use 
append_column(), append_foreign_key(), append_constraint(), etc.
- table.create() no longer returns the Table object, instead has no
return value.  the usual case is that tables are created via metadata,
which is preferable since it will handle table dependencies.
- added UniqueConstraint (goes at Table level), CheckConstraint
(goes at Table or Column level) fixes [ticket:217]
- index=False/unique=True on Column now creates a UniqueConstraint,
index=True/unique=False creates a plain Index, 
index=True/unique=True on Column creates a unique Index.  'index'
and 'unique' keyword arguments to column are now boolean only; for
explcit names and groupings of indexes or unique constraints, use the
UniqueConstraint/Index constructs explicitly.
- relationship of Metadata/Table/SchemaGenerator/Dropper has been
improved so that the schemavisitor receives the metadata object
for greater control over groupings of creates/drops.
- added "use_alter" argument to ForeignKey, ForeignKeyConstraint, 
but it doesnt do anything yet.  will utilize new generator/dropper
behavior to implement. 


""",
u"""
a simplification to syncrule generation, which also allows more flexible configuration
of which columns are to be involved in the synchronization via foreignkey property.
foreignkey param is a little more important now and should have its role clarified
particularly for self-referential mappers.

""",
u"""
make OrderedDict consructor, update more dict-like
""",
u"""
- remove spurious semicomma from Firebird SQL statement (Lele Gaifax)

    """,
u"""
- sync checks destination column for primary key status, will not set it to None in that case
- dependency non-passively loads child items for many-to-one post update check

""",
u"""
added 'ntext' reflected type

""",
u"""
some cleanup submitted by Lele Galifax

""",
u"""
added docstrings for url, added to compiled documentation

""",
u"""
some logging tweaks....its a little squirrely

""",
u"""
oops, double row echo removed

""",
u"""
added debug-level row echoing to RowProxy (moved from ResultProxy)

    """,
u"""
  - ResultProxy.fetchall() internally uses DBAPI fetchall() for better efficiency,
    added to mapper iteration as well (courtesy Michael Twomey)


    """,
u"""
- fixes to Date/Time (SLDate/SLTime) types; works as good as postgres
  now [ticket:335]

  """,
u"""
_sort_tables uses local tables [ticket:322]

""",
u"""
added PGBigInteger type

""",
u"""
remove unused set

""",
u"""
dont create dependency processor if viewonly=True

""",
u"""
logging of syncrules

""",
u"""
more adjustments to #321

""",
u"""
add table name to save_obj log

""",
u"""
row-switch test should be per-instance, not per table per instance

""",
u"""
added correct insert ordering

""",
u"""
- mapper.save_obj() now functions across all mappers in its polymorphic
series, UOWTask calls mapper appropriately in this manner
- polymorphic mappers (i.e. using inheritance) now produces INSERT
statements in order of tables across all inherited classes
[ticket:321]


""",
u"""
more fixup to self referential composite primary key mappings

""",
u"""
this test works better with session clears in between

""",
u"""
- the "foreign_key" attribute on Column and ColumnElement in general
    is deprecated, in favor of the "foreign_keys" list/set-based attribute,
    which takes into account multiple foreign keys on one column.
    "foreign_key" will return the first element in the "foreign_keys" list/set
    or None if the list is empty.
- added a user test to the relationships test, testing various new things this
change allows

""",
u"""
assorted firebird fixes from Lele Gaifax

""",
u"""
some cleanup

""",
u"""
improved exceptions for closed connections

""",
u"""
fix "no engine found" to raise explicit error, [ticket:326]

""",
u"""
rollback last change until we figure out how to check for engine without exception

""",
u"""
better error message for unconnected DynamicMetaData [ticket:326]

""",
u"""
add compound-where example
""",
u"""
[ticket:324]

""",
u"""
r/m sqlsoup.NoSuchTableError (SA proper takes care of that now)
add sqlsoup.PKNotFoundError

""",
u"""
continued cleanup

""",
u"""
various cleanup etc.

""",
u"""
 - "custom list classes" is now implemented via the "collection_class"
    keyword argument to relation().  the old way still works but is
    deprecated [ticket:212]


    """,
u"""
 - Function objects know what to do in a FROM clause now.  their
    behavior should be the same, except now you can also do things like
    select(['*'], from_obj=[func.my_function()]) to get multiple
    columns from the result, or even use sql.column() constructs to name the
    return columns [ticket:172].  generally only postgres understands the 
    syntax (and possibly oracle).


    """,
u"""
formatting fixup, etc.

""",
u"""
- added auto_setinputsizes=False to oracle dialect.  if true, all executions will get setinputsizes called ahead of time.
- some tweaks to the types unittest for oracle.  oracle types still need lots more work.

""",
u"""
fixed super call

""",
u"""
- removed "extension()" MapperOption
- TypeEngine objects can report on DBAPI types
- added set_input_sizes() to default dialect
- oracle dialect gets Timestamp type added, may need to call
set_input_sizes() to make it work with sub-second resolution [ticket:304]

""",
u"""
- merged loader_strategies branch into trunk.
- this is a wide refactoring to "attribute loader" and "options" architectures.
ColumnProperty and PropertyLoader define their loading behaivor via switchable
"strategies", and MapperOptions no longer use mapper/property copying 
in order to function; they are instead propigated via QueryContext
and SelectionContext objects at query/instnaces time.
All of the copying of mappers and properties that was used to handle
inheritance as well as options() has been removed and the structure
of mappers and properties is much simpler and more clearly laid out.


""",
u"""
- added profiling to massave
- adjusted the formatting for per-instance loggers to limit the number
of loggers that get created in memory.

""",
u"""
adjustment to default timeout

""",
u"""
edits

""",
u"""
further str() on values that may come back as unicode

""",
u"""
[ticket:318] has a user receiving back a unicode from a SHOW CREATE TABLE for some reason

""",
u"""
 - fixed condition that occurred during reflection when a primary key
    column was explciitly overridden, where the PrimaryKeyConstraint would
    get both the reflected and the programmatic column doubled up

    """,
u"""
long changelist, adding some formatting

""",
u"""
- internal refactoring to mapper instances() method to use a 
SelectionContext object to track state during the operation.
SLIGHT API BREAKAGE: the append_result() and populate_instances()
methods on MapperExtension have a slightly different method signature
now as a result of the change; hoping that these methods are not 
in widespread use as of yet.

""",
u"""
- doc edit
- i have no idea what a SynonymProperty was supposed to be for

""",
u"""
- added some dependency logging
- moved the ClauseSynchronizer compile from properties to dependency where its used

""",
u"""
remove print statement

""",
u"""
mass saver for profiling mem usage....

""",
u"""
[ticket:309]

""",
u"""
tweaks for mysql

""",
u"""
fix PK redefinition
""",
u"""
more edits

""",
u"""
rearrangement of docs for [ticket:310]

""",
u"""
raise proper AttributeError

""",
u"""
- more adjustments to the eager load table finder to work with existing mappings
against selects and query-created limit/offset subselects
- added eagertest3 to orm/alltests.py

""",
u"""
the new eagerloading test suite mentioned in the previous commit

""",
u"""
- added test suite to test improved from_obj/join behavior with Query/eagerloading/SelectResults
- EagerLoader looks more carefully for the correct Table/Join/FromClause to bind its outer join onto 
- sqlite boolean datatype converts bind params from python booleans to integer
- took out assertion raise from 'name' property of CompoundSelect

""",
u"""
decruftify

""",
u"""
- pool will auto-close open cursors, or can be configured to raise an error instead
- consolidated scalar() calls into ResultProxy scalar(), fixed ResultProxy scalar() to
apply typing rules
- general de-cruftification of ClauseElement/Compiled (yes i know theres crufty things everywhere)

    """,
u"""
- specifying joins in the from_obj argument of query.select() will
replace the main table of the query, if the table is somewhere within
the given from_obj.  this makes it possible to produce custom joins and
outerjoins in queries without the main table getting added twice.
[ticket:315]
- added join_to and outerjoin_to transformative methods to SelectResults,
to build up join/outerjoin conditions based on property names. also
added select_from to explicitly set from_obj parameter.
- factored "results" arrays from the mapper test suite and into the 
"tables" mapper
- added "viewonly" param to docs

""",
u"""
- added an automatic "row switch" feature to mapping, which will
detect a pending instance/deleted instance pair with the same
identity key and convert the INSERT/DELETE to a single UPDATE
- "association" mappings simplified to take advantage of
automatic "row switch" feature
- fixes [ticket:311]

""",
u"""
NCHAR and NVARCHAR support for MS-SQL. Patch from Kent Johnson
""",
u"""
added "viewonly" flag to allow relations that dont affect flush()

""",
u"""
Simplified MSSQL table reflection code
  added support for multi-column foreign keys
  """,
u"""
fix misspelled func calls
""",
u"""
commented out open cursor check, until resolution of [ticket:312]

""",
u"""
made echo param more doc-friendly

""",
u"""
doc edits, moved object display in uowdumper to be hex, fixed test runner in parseconnect

""",
u"""
- logging is now implemented via standard python "logging" module.
"echo" keyword parameters are still functional but set/unset
log levels for their respective classes/instances.  all logging
can be controlled directly through the Python API by setting
INFO and DEBUG levels for loggers in the "sqlalchemy" namespace.
class-level logging is under "sqlalchemy.<module>.<classname>",
instance-level logging under "sqlalchemy.<module>.<classname>.<hexid>".
Test suite includes "--log-info" and "--log-debug" arguments
which work independently of --verbose/--quiet.  Logging added
to orm to allow tracking of mapper configurations, row iteration
fixes [ticket:229] [ticket:79]

""",
u"""
spelling fix

""",
u"""
onupdate/ondelete fix

""",
u"""
descriptive error message when an executioncontext-requiring call is called off a ResultProxy which was created via literal statement execution and therefore does not have an execution context.

""",
u"""
added MSSQL changes
""",
u"""
Fixes use of port for pymssql
Introduces new auto_indentity_insert option
Fixes bug #261
""",
u"""
added scalar() to ResultProxy

""",
u"""
mutable flag

""",
u"""
- added "mutable" flag to PickleType, set to False to allow old (faster) behavior
- fix attribute unit test
- attributes have explicit flag for "mutable_scalars", propigated by ColumnProperty

""",
u"""
- added "pickleable" module to test suite to have cPickle-compatible
test objects
- added copy_function, compare_function arguments to InstrumentedAttribute
- added MutableType mixin, copy_value/compare_values methods to TypeEngine,
PickleType
- ColumnProperty and DeferredProperty propigate the TypeEngine copy/compare 
methods to the attribute instrumentation
- cleanup of UnitOfWork, removed unused methods
- UnitOfWork "dirty" list is calculated across the total collection of persistent
objects when called, no longer has register_dirty.
- attribute system can still report "modified" status fairly quickly, but does
extra work for InstrumentedAttributes that have detected a "mutable" type where
catching the __set__() event is not enough (i.e. PickleTypes)
- attribute tracking modified to be more intelligent about detecting
changes, particularly with mutable types.  TypeEngine objects now
take a greater role in defining how to compare two scalar instances,
including the addition of a MutableType mixin which is implemented by
PickleType.  unit-of-work now tracks the "dirty" list as an expression
of all persistent objects where the attribute manager detects changes.
The basic issue thats fixed is detecting changes on PickleType 
objects, but also generalizes type handling and "modified" object
checking to be more complete and extensible.


""",
u"""
- connection pool tracks open cursors and raises an error if connection
is returned to pool with cursors still opened.  fixes issues with MySQL, 
others

""",
u"""
- added autoincrement=True to Column; will disable schema generation
of SERIAL/AUTO_INCREMENT/identity seq for postgres/mysql/mssql if
explicitly set to False.  #303

""",
u"""
remove delete-orphan cascade from self referential mappers

""",
u"""
- fixed unfortunate mutating-dictionary glitch from previous checkin
- added "batch=True" flag to mapper; if False, save_obj
will fully save one object at a time including calls
to before_XXXX and after_XXXX

""",
u"""
future log lines

""",
u"""
fix to reset_class_managed to look at noninherited attributes only; an artifact of compilation brought this up

""",
u"""
- fix to deferred group loading

""",
u"""
- ForeignKey reports better error message for column not found
- change in verbiage when join conditions are figured out (and fail)

    """,
u"""
- moved selectresults test from orm to ext package
- renamed objectstore test suite to unitofwork
- added additional "eagerdegrade" tests to mapper, to test fixes from #308

""",
u"""
- adjustments to eager loading so that its "eager chain" is
kept separate from the normal mapper setup, thereby
preventing conflicts with lazy loader operation, fixes 
[ticket:308]


""",
u"""
- BooleanExpression includes new "negate" argument to specify
the appropriate negation operator if one is available.
- calling a negation on an "IN" or "IS" clause will result in
"NOT IN", "IS NOT" (as opposed to NOT (x IN y)). 

""",
u"""
case sensitive function seems to return a string in some cases

""",
u"""
check for mapper or class, raise exception otherwise [ticket:305]

""",
u"""
- post_update behavior improved; does a better job at not
updating too many rows, updates only required columns
[ticket:208]


""",
u"""
no SERIAL for smallinteger columns

""",
u"""
no KeyError if url params not provided

""",
u"""
- added an implicit close() on the cursor in ResultProxy
when the result closes
- added scalar() method to ComposedSQLEngine


""",
u"""
added extract() function to sql dialect

""",
u"""
moved "c.name" to "c.key" for processing defaults since bind params use column key

""",
u"""
- fixed bug where Connection wouldnt lose its Transaction
after commit/rollback

""",
u"""
removed lockmode from get_by

""",
u"""
sqlite doesnt support FOR UPDATE

""",
u"""
ConcurrentModificationExecption

""",
u"""
- implemented "version check" logic in Query/Mapper, used
when version_id_col is in effect and query.with_lockmode()
is used to get() an instance thats already loaded
[ticket:292]

""",
u"""
checks for invalid lockmode argument

""",
u"""
- changed "for_update" parameter to accept False/True/"nowait"
and "read", the latter two of which are interpreted only by
Oracle and Mysql [ticket:292]
- added "lockmode" argument to base Query select/get functions, 
including "with_lockmode" function to get a Query copy that has 
a default locking mode.  Will translate "read"/"update" 
arguments into a for_update argument on the select side.
[ticket:292]


""",
u"""
removed auto-dispose on __del__, produces too much garbage exceptiongs

""",
u"""
fixup to printing of uow

""",
u"""
- more rearrangements of unit-of-work commit scheme to better allow
dependencies within circular flushes to work properly...updated
task traversal/logging implementation

this work is still under construction !  requires more unit tests and
new dumper needs to be finished.

""",
u"""
forgot the tearDown step....

""",
u"""
fixed constructor on bigint

""",
u"""
added link 

""",
u"""
0.2.8..

""",
u"""
- added basic 'zblog' test suite
- better error message for mapper orphan detect


""",
u"""
restored "optimistic" behavior of hasparent.  its generally disastrous without that flag as its impossible to load all lazy loaders, deal with attributes that "noload", etc. just to check for orphan status.

""",
u"""
- unicode fix for startswith()/endswith() [ticket:296]

""",
u"""
update

""",
u"""
further fixes to case sensitive logic

""",
u"""
revised section on quoting, semanticized headings and table of content lists

""",
u"""
- import of py2.5s sqlite3 [ticket:293]

""",
u"""
simplification to quoting to just cache strings per-dialect, added quoting for alias and label names
fixes [ticket:294]

""",
u"""
cleanup/unit test fixes

""",
u"""
- further changes to attributes with regards to "trackparent".  the "commit" operation
now sets a "hasparent" flag for all attributes to all objects.  that way lazy loads
via callables get included in trackparent, and eager loads do as well because the mapper
calls commit() on all objects at load time.  this is a less shaky method than the "optimistic"
thing in the previous commit, but uses more memory and involves more overhead.
- some tweaks/cleanup to unit tests

""",
u"""
futher fix to the "orphan state" idea.  to avoid setting tons of
"hasparent" flags on objects as they are loaded, both from lazy and eager loads,
the "orphan" check now uses an "optimistic" flag to determine the result if no 
"hasparent" flag is found for a particular relationship on an instance. if the
instance has an _instance_key and therefore was loaded from the database, it is
assumed to not be an orphan unless a "False" hasparent flag has been set.  if the
instance does not have an _instance_key and is therefore transient/pending, it is
assumed to be an orphan unless a "True" hasparent flag has been set.

""",
u"""
insure that "parent" pointers are set up on objects that were lazily loaded

""",
u"""
possible fix for [ticket:276].  if mysql detects case-insensitivity, converts
tables to lower case names

""",
u"""
since casing is figured out quasi-automatically when creating table/column/etc, 
removed casing checks within pg reflection

""",
u"""
quoting more or less working with oracle

""",
u"""
fix to from clause in unittest query...somehow this didnt fail on pg 8.0, but fails on 8.1

""",
u"""
defaults and constraints have optional parent

""",
u"""
sequence/default adjustments to allow postgres 8.1 tests to function

""",
u"""
pg formats sequence name, more quote test fixes

""",
u"""
some tweaks to oracle casing...

""",
u"""
- added case_sensitive argument to MetaData, Table, Column, determines
itself automatically based on if a parent schemaitem has a non-None
setting for the flag, or if not, then whether the identifier name is all lower
case or not.  when set to True, quoting is applied to identifiers with mixed or
uppercase identifiers.  quoting is also applied automatically in all cases to
identifiers that are known to be reserved words or contain other non-standard
characters. various database dialects can override all of this behavior, but
currently they are all using the default behavior.  tested with postgres, mysql,
sqlite.  needs more testing with firebird, oracle, ms-sql. part of the ongoing
work with [ticket:155]


""",
u"""
- deregister Table from MetaData when autoload fails; [ticket:289]

""",
u"""
- fix to using query.count() with distinct, **kwargs with SelectResults
count() [ticket:287]

""",
u"""
- changed "invalidate" semantics with pooled connection; will
instruct the underlying connection record to reconnect the next
time its called.  "invalidate" will also automatically be called
if any error is thrown in the underlying call to connection.cursor().
this will hopefully allow the connection pool to reconnect to a
database that had been stopped and started without restarting
the connecting application [ticket:121]


""",
u"""
[ticket:266] constraint name in PrimaryKeyConstraint

""",
u"""
doc bug [ticket:278]

""",
u"""
- added "timezone=True" flag to DateTime and Time types.  postgres
so far will convert this to "TIME[STAMP] (WITH|WITHOUT) TIME ZONE",
so that control over timezone presence is more controllable (psycopg2
returns datetimes with tzinfo's if available, which can create confusion
against datetimes that dont).
[ticket:275]

""",
u"""
added "dev" tag to default setup
some extra README

""",
u"""
fixed inaccuracies regarding "connectable" parameter sent to create/drop

""",
u"""
TODO for oracle

""",
u"""
added limit/offset to union queries

""",
u"""
- cleanup on connection methods + documentation.  custom DBAPI
arguments specified in query string, 'connect_args' argument
to 'create_engine', or custom creation function via 'creator'
function to 'create_engine'.
- added "recycle" argument to Pool, is "pool_recycle" on create_engine,
defaults to 3600 seconds; connections after this age will be closed and
replaced with a new one, to handle db's that automatically close
stale connections [ticket:274]


""",
u"""
[ticket:282]

""",
u"""
the "check for orphans" step will cascade the delete operation to child objects.

""",
u"""
- urls support escaped characters in passwords [ticket:281]

""",
u"""
sqlite dialects can be created without pysqlite installed

""",
u"""
- unit tests updated to run without any pysqlite installed; pool
test uses a mock DBAPI

""",
u"""
working on sequence quoting support....

""",
u"""
postgres reflection uses dialect-wide preparer

""",
u"""
refactoring of ANSIIdentifierPreparer to be one instance per-dialect, simplified caching

""",
u"""
- postgres reflection moved to use pg_schema tables, can be overridden
with use_information_schema=True argument to create_engine
[ticket:60], [ticket:71]
- added natural_case argument to Table, Column, semi-experimental
flag for use with table reflection to help with quoting rules
[ticket:155]


""",
u"""
added a compile check to instances()

    """,
u"""
[ticket:280] statement execution supports using the same BindParam
object more than once in an expression; simplified handling of positional
parameters.  nice job by Bill Noon figuring out the basic idea.


""",
u"""
- unit-of-work does a better check for "orphaned" objects that are
part of a "delete-orphan" cascade, for certain conditions where the
parent isnt available to cascade from.
- it is now invalid to declare a self-referential relationship with
"delete-orphan" (as the abovementioned check would make them impossible
to save)
- improved the check for objects being part of a session when the
unit of work seeks to flush() them as part of a relationship..


""",
u"""
more fixes for [ticket:269], added MSMediumBlob type

""",
u"""
commit should be outside of the try/except; else when commit fails, rollback gets called which is technically invalid (although SA transaction probably lets it slide...this should also possibly be made more strict)

""",
u"""
if a contextual session is established via MapperExtension.get_session
(as it is using the sessioncontext plugin, etc), a lazy load operation
will use that session by default if the parent object is not 
persistent with a session already.


""",
u"""
[ticket:277] check if pg/oracle sequence exists.  checks in all cases before CREATE SEQUENCE/ DROP SEQUENCE

""",
u"""
added "requires_quotes" step, subclasses of ANSIIdentifierPreparer can override

""",
u"""
fixes for threadless python compiles
""",
u"""
- eesh !  the tutorial doctest was broken for quite some time.
- add_property() method on mapper does a "compile all mappers"
step in case the given property references a non-compiled mapper
(as it did in the case of the tutorial !)

    """,
u"""
the latest...

""",
u"""
modifcation to unitofwork to not maintain ordering within the
"new" list or within the UOWTask "objects" list; instead, new objects
are tagged with an ordering identifier as they are registered as new
with the session, and the INSERT statements are then sorted within the 
mapper save_obj.  the INSERT ordering has basically been pushed allthe way 
to the end of the flush cycle. that way the various sorts and 
organizations occuring within UOWTask (particularly the circular task 
sort) dont have to worry about maintaining order (which they werent anyway)

    """,
u"""
fix to __eq__ method in a test object

""",
u"""
improved error message when a backref conflicts with a column-based property

""",
u"""
added MSTinyInteger to MS-SQL [ticket:263]

""",
u"""
fixed construction of order_by with distinct query

""",
u"""
0.2.7 prep

""",
u"""
some fixes to sqlite datetime organization, was improperly reflecting
the "date" type as a "datetime"

""",
u"""
fixes to types so that database-specific types more easily used;
fixes to mysql text types to work with this methodology
[ticket:269]

""",
u"""
[ticket:268]

""",
u"""
refactored ANSIIdentifierPreparer to be visitor based; minimizes escaping operations
and isinstance()/duck-typing calls

""",
u"""
turned off default case-folding rules as they wreak havoc with the current unittests,
temporary isintance() checks in ASNIIdentifierPreparer which will be replaced with visit_ 
methodology

""",
u"""
added docs for ON UPDATE/DELETE, identifier quoting

""",
u"""
 quoting facilities set up so that database-specific quoting can be
turned on for individual table, schema, and column identifiers when
used in all queries/creates/drops.  Enabled via "quote=True" in 
Table or Column, as well as "quote_schema=True" in Table.  Thanks to
Aaron Spike for his excellent efforts.  [ticket:155]

""",
u"""
comment

""",
u"""
[ticket:251]

""",
u"""
removed superfluous **params

""",
u"""
SelectResults will use a subselect, when calling an aggregate (i.e.
max, min, etc.) on a SelectResults that has an ORDER BY clause
[ticket:252]


""",
u"""
reflected 'mediumint' type

""",
u"""
inheritance check uses issubclass() instead of direct __mro__ check
to make sure class A inherits from B, allowing mapper inheritance to more
flexibly correspond to class inheritance [ticket:271]

""",
u"""
added "nowait" flag to Select() [ticket:270]

""",
u"""
fixed ms-sql connect() to work with adodbapi

""",
u"""
moved rollback catch to mysql module...

""",
u"""
fix mysql borkage
""",
u"""
fix mysql borkage
""",
u"""
added __contains__ to OrderedProperties, so that rabbit is not in there

""",
u"""
all create()/drop() calls have a keyword argument of "connectable".
"engine" is deprecated. fixes [ticket:255]

""",
u"""
added an objectstore clear

""",
u"""
fix to lazy loads when mapping to joins

""",
u"""
adjusted __getstate__ on InstrumentedList to further avoid callables getting stuck in there...

""",
u"""
fixed possible error in mysql reflection where certain versions
return an array instead of string for SHOW CREATE TABLE call

""",
u"""
added start of a many-to-many test

""",
u"""
fixed small pickle bug with lazy loaders [ticket:265]

""",
u"""
improvement over previous changeset:
SingletonThreadPool has a size and does a cleanup pass, so that
only a given number of thread-local connections stay around (needed
for sqlite applications that dispose of threads en masse)


""",
u"""
temporary workaround dispose_local() added to SingletonThreadPool
for sqlite applications that dispose of threads en masse


""",
u"""
added reflected 'tinyint' type to MS-SQL [ticket:263]


""",
u"""
fixed mysql reflection of default values to be PassiveDefault

""",
u"""
adjustments to pool stemming from changes made for [ticket:224].
overflow counter should only be decremented if the connection actually
succeeded.  added a test script to attempt testing this.


""",
u"""
oops:  committed the rest of [changeset:1759], removed print in sqlite + restored error check in Join

""",
u"""
- better check for ambiguous join conditions in sql.Join; propigates to a
better error message in PropertyLoader (i.e. relation()/backref()) for when
the join condition can't be reasonably determined.
- sqlite creates ForeignKeyConstraint objects properly upon table
reflection.


""",
u"""
r/m _reset method
""",
u"""
expand explanation of Query methods
""",
u"""
add update method
""",
u"""
fix for when default is zero
""",
u"""
typo fix noticed by R Munn
""",
u"""
doc update
""",
u"""
auto-execute delete stmts
""",
u"""
add mappedtable.delete support
""",
u"""
soup.engine property
""",
u"""
PassiveDefault('?') for autoloaded sqlite defaults

(no complaints on-list so I'm checking this in...  go ahead and revert if I'm stepping on any toes here, Mike)
""",
u"""
custom primary/secondary join conditions in a relation *will* be propigated
to backrefs by default.  specifying a backref() will override this behavior.

""",
u"""
oracle boolean type [ticket:257]

""",
u"""
[ticket:256] propigating url.query arguments to connect() function for all db's

""",
u"""
removed erroneous "on_update" example for PassiveDefault

""",
u"""
fixed anchor tag

""",
u"""
[ticket:254]

""",
u"""
with_labels support
""",
u"""
fix outdated link into SA docs for Query objects
""",
u"""
de-tabbify
""",
u"""
ReST-ify docstring
""",
u"""
small join api change

with_labels stuff doesn't quite work yet -- needs that select(from_obj=[join]) support -- so no doctest
""",
u"""
fixed reflection of foreign keys to autoload the referenced table
if it was not loaded already, affected postgres, mysql, oracle.
fixes the latest in [ticket:105]


""",
u"""
schema support for sqlsoup
""",
u"""
fix doctests by ensuring consistent sort order via __cmp__; add join support
""",
u"""
_selectable interface; allows sqlsoup to pass its classes to Join and have the underlying Table pulled out
""",
u"""
fix doctest integration
""",
u"""
add test for allow_null_pks
""",
u"""
added allow_null_pks option to Mapper, allows rows where some
primary key columns are null (i.e. when mapping to outer joins etc)


    """,
u"""
assignmapper was setting is_primary=True, causing all sorts of mayhem
by not raising an error when redundant mappers were set up, fixed

""",
u"""
fixed [ticket:245]

""",
u"""
patch to inheritance section

""",
u"""
implemented latest patch on [ticket:105], modified to support
new ForeignKeyConstraint upon reflection

""",
u"""
patch for [ticket:105], adding "owner" support to oracle...not tested yet

""",
u"""
added table.exists()

    """,
u"""
added 'checkfirst' argument to table.create()/table.drop()
some 0.2.6 prep

""",
u"""
reduced bind param size in query._get to appease the picky oracle 
[ticket:244]

""",
u"""
mapper compilation work ongoing, someday it'll work....moved
around the initialization of MapperProperty objects to be after
all mappers are created to better handle circular compilations.
do_init() method is called on all properties now which are more
aware of their "inherited" status if so.

eager loads explicitly disallowed on self-referential relationships, or
relationships to an inheriting mapper (which is also self-referential)


    """,
u"""
fix to typing in clause construction which specifically helps
type issues with polymorphic_union (CAST/ColumnClause propigates
its type to proxy columns)


""",
u"""
failing test case re: compilation

""",
u"""
added "synonym()" function, applied to properties to have a
propname the same as another, for the purposes of overriding props
and allowing the original propname to be accessible in select_by().


""",
u"""
remove print statement

""",
u"""
overhaul to MapperExtension so they arent chained via "next"; this breaks all over the place since extensions get copied between mappers etc.  now theyre assembled into a list, of which a single extension can belong to many different lists.

""",
u"""
echo=True

""",
u"""
added __setitem__ to Constraint

""",
u"""
fixed table name in REFERENCES clause to include schema if applicable

""",
u"""
some cleanup on session/uow interaction, check for None
when calling refresh or expire in case object was deleted

""",
u"""
some cascade tweaks

""",
u"""
deferred column load could screw up the connection status in
a flush() under some circumstances, this was fixed

""",
u"""
overhaul to schema, addition of ForeignKeyConstraint/
PrimaryKeyConstraint objects (also UniqueConstraint not
completed yet).  table creation and reflection modified
to be more oriented towards these new table-level objects.
reflection for sqlite/postgres/mysql supports composite 
foreign keys; oracle/mssql/firebird not converted yet.

""",
u"""
ActiveMapper now supports autoloading of column definitions if you supply
a __autoload__ = True attribute in your inner mapping class.  It does not
currently support autoloading relationships.

""",
u"""
$-># for install prompt

""",
u"""
DB connection errors wrapped in DBAPIErrors

""",
u"""
added count/count_by to assignmapper, plus a test in activemapper to try it out

""",
u"""
fixed up boolean datatype for sqlite, mysql, ms-sql

""",
u"""
still having mappers not getting compiled...sigh...

""",
u"""
primary key identifier is a list now, not param list, [ticket:236]

""",
u"""
clarified passivedefault only for INSERT, added brief 'override reflected columns' example

""",
u"""
slightly less lame version function

""",
u"""
sqlite detects version and disables CAST if version < 3.2.3
fixes to unittests, mapper extension to work better with setting/unsetting extensions
objectstore objects get 'session' attribute

""",
u"""
expunge wasnt de-associating the object with a session

""",
u"""
activemapper will use threadlocal mod's objectstore if its installed
both objectstores no longer subclass SessionContext, get at it via .context attribute instead

""",
u"""
adjument to regexp for parsing courtesy Barry Warsaw

""",
u"""
fix to error message for object with mismatched session

""",
u"""
hey ho alphas got to go

""",
u"""
works without backrefs too....

""",
u"""
some refactorings to activemapper, made relationship() class have some polymorphic behavior for initializing its real relation, added support + unittest for self-referential relationship

""",
u"""
added workaround for funny pragma behavior on windows pysqlite
singletonthreadpool has a dispose() method, used by proxy_engine test
to better clean up after itself on windows

""",
u"""
small fix to relation compilation

""",
u"""
0.2.5 

""",
u"""
took out that whole compilation dependency thing.  just need to loop through mapper_registry and compile whatever is not compiled. the "non-reentrant" compile() method, which is a product of the whole compilation dependency tangent, makes this pretty easy.  So it was a pretty roundabout way to go for ultimately a pretty small change to compilation.

""",
u"""
made mapper compilation "check for remaining mappers" compile anything found, guaranteeing everything to be compiled in all cases

""",
u"""
removed debug line

""",
u"""
ordering of UPDATE and DELETE statements within groups is now
in order of primary key values, for more deterministic ordering
after_insert/delete/update mapper extensions now called per object,
not per-object-per-table
fixed import in firebird.py

""",
u"""
fixed hyperlink to adv datamapping

""",
u"""
change exception message

""",
u"""
got MS-SQL support largely working, including reflection, basic types, fair amount of ORM stuff, etc.
'rowcount' label is reseved in MS-SQL and had to change in sql.py count() as well as orm.query

""",
u"""
some adjustments to activemapper's objectstore to be composed against SessionContext
DynamicMetaData checks first for _engine before returning

""",
u"""
fixes to attributes/related so that get_history with passive=True returns no 
AttributeHistory object if an untriggered callable was found (not sure how this used to work
OK....)

""",
u"""
Put back in the foreign-key checking code in process_relationships for 
ActiveMapper.  It looks like it is required by at least one person, so for
now the code will stay in!

""",
u"""
There were two significant changes in this commit:

 * Added implicit primary keys to ActiveMapper.  Now, if you do not speicfy a
   primary key on your objects when declaring them, an Integer primary key
   called `id` will automatically be added to your objects for you.

 * Commented out a large chunk of the process_relationships function that
   should no longer be necessary thanks to some of the deferred mapper
   compilation that was added in SQLAlchemy 0.2.3.  I left it in the code, but
   commented it out just in case this change causes a problem in someone's
   else's code and I can put it back in if needed.

   """,
u"""
added a note about sqlite uris

""",
u"""
removed toengine()  calls

""",
u"""
inserting './lib/' into sys.path since PYTHONPATH no longer straightforward with latest setuptools

""",
u"""
fixed endless loop bug in select_by(), if the traversal hit
two mappers that referenced each other

""",
u"""
firebird patch with support for type_conv

""",
u"""
Updated ActiveMapper to support order_by parameters on all relationships.
Thanks to Charles Duffy for this patch!

""",
u"""
fixes to pool_invalidate [ticket:224]

""",
u"""
new MySQL types: MSEnum, MSTinyText, MSMediumText, MSLongText, etc.
more support for MS-specific length/precision params in numeric types
patch courtesy Mike Bernson


""",
u"""
lazy load bind params properly propigate column type [ticket:225]

""",
u"""
cursor() method on ConnectionFairy allows db-specific extension
arguments to be propigated [ticket:221]

""",
u"""
PG didnt like 'user' for a table name

""",
u"""
dont put SERIAL on a column if it has a ForeignKey

""",
u"""
fixed attribute manager's ability to traverse the full set of managed attributes for a descendant class, + 2 unit tests

""",
u"""
0.2.4...

""",
u"""
migrated Queue.Queue to its own module here, to assure RLock compatibility

""",
u"""
fix to the column properties to better compile the underlying mapper before access

""",
u"""
some doc edits

""",
u"""
fix to timeout

""",
u"""
attempting to fix reentrant condition that can happen with Queue.Queue

""",
u"""
when QueuePool times out it raises a TimeoutError instead of
erroneously making another connection


""",
u"""
fixed bug when specifying explicit module to mysql dialect

""",
u"""
added *extra to mysql string type to consume extra unsupported arguments from reflection

""",
u"""
fixes to inheritance firing off dependency processors correctly + unittest

""",
u"""
identified another TLTransaction scenario, and adjusted TLConnection/TLSession to fix this as well (reverted previous change, and overriding in_transaction() instead)

    """,
u"""
TLConnection insures that it is used to create a transaction via the session when begin() is called, so that it has proper transactional context, + unittests

""",
u"""
still fixing compilation.....dum de dum.....

""",
u"""
removed non py2.3ish parenthesis

""",
u"""
more compilation fixes

""",
u"""
Replaced tab spacing with plain spaces.

""",
u"""
Changed mapper.get_session to compile mapper and thereby create the 
extension chain needed to lookup the current session.

""",
u"""
some cleanup to the new compilation changes

""",
u"""
possible fix to deferred compilation, adds an extra kick in case everything wasnt compiled

""",
u"""
single space for MySQL appeasement

""",
u"""
more development on using eager loads/limit/offset/join_via/order_by at the same time

""",
u"""
when Query does the "nested select" thing, it copies the ORDER BY to be placed on the "outer" select, so that eager loaders modify only the outer one and not the inner one

""",
u"""
added check for conflicting backrefs + unit test
identified unit test where mapper properties must be set up before the surrogate mapper is created

""",
u"""
Added some additional data to exception raised in PropertyLoader,_get_direction when cannot determine the direction to specify exactly which relation failed.
""",
u"""
lazy load and deferred load operations require the parent object
to be in a Session to do the operation; whereas before the operation
would just return a blank list or None, it now raises an exception.

Session.update() is slightly more lenient if the session to which
the given object was formerly attached to was garbage collected;
otherwise still requires you explicitly remove the instance from
the previous Session.


""",
u"""
try/except  around init.__name__ = oldinit.__name__ for py2.3 compat

""",
u"""
cast converted into its own ClauseElement so that it can have an explicit compilation
function in ANSICompiler
MySQLCompiler then skips most CAST calls since it only seems to support the standard syntax for Date
types; other types now a TODO for MySQL
then, polymorphic_union() function now CASTs null()s to the type corresponding to the columns in the UNION,
since postgres doesnt like mixing NULL with integer types
(long road for that .....)

    """,
u"""
if an object fails construction, doesnt get added to the session 

""",
u"""
updates

""",
u"""
unsupported unit test on mysql

""",
u"""
more intelligent "removal" of list items when a list attribute is replaced, doesnt actually "remove" the items from teh replaced list just marks them as "removed" from the parent object for history purposes

""",
u"""
removed historyarray test
ForeignKey is more intelligent about locating the parent table it represents, in the case that
its attached to a CompoundSelect column which has multiple "originals", some of which might not be schema.Columns

""",
u"""
fixed bug where if a many-to-many table mapped as "secondary" had other cols in it, delete operations would try to match up on those columns.  also fixed bug in new attributes if you set a list based attribute to a blank list, properly fires the 'delete' event for the elements of the previous list

""",
u"""
fixed 'port' attribute of URL to be an integer if present [ticket:209]

""",
u"""
some adjustments

""",
u"""
merged attributes rewrite

""",
u"""
if an item attached to a parent is found to be already in the session, then the "save-update" cascade operation doesnt take place.  currently this prevents unncessessary cascading due to backref events, which was a massive speed hit.

""",
u"""
fixed bug where Column with redefined "key" property wasnt getting
type conversion happening in the ResultProxy [ticket:207]

""",
u"""
fixed nested rollbacks

""",
u"""
unit tests for dangling subquery, many-to-many clear-and-resave

""",
u"""
adjustment to better allow textual from clauses

""",
u"""
"parent track" function needed to be more specific to the parent class

""",
u"""
separated standalone between(), column.between(), put literal checking for both, favor column.between()

    """,
u"""
fixed typing for between() operator, [ticket:202]

""",
u"""
fixed module scoping for class_mapper [ticket:201]

""",
u"""
late compilation of mappers.  now you can create mappers in any order, and they will compile their internal state when first used in a query or flush operation (or their props or 'c'/'columns' attributes are used).  includes various cleanups and fixes in support of the change, including some unit test changes, additional unit tests.

""",
u"""
possible fix to cascade_mappers

""",
u"""
fixed [ticket:200]

""",
u"""
Further improved the process_relationships function to handle the ordering of
class definitions better. The function was only looking at relationships, not 
foreign keys, and was making some improper assumptions. The unit tests all 
still pass, and now some of my own code actually works, regardless of the order
that I define the classes in.' 'lib/sqlalchemy/ext/activemapper.py

""",
u"""
fixed bug where tables with schema name werent getting indexed in metadata correctly

""",
u"""
Copy __name__ and __doc__ from oldinit.

""",
u"""
fix to backref when its none for one-to-one

""",
u"""
added "NonExistentTable" exception throw to reflection, courtesy lbruno@republico.estv.ipv.pt, for [ticket:138]

""",
u"""
factored out "inheriting_tasks" member of UOWTask.  all "polymorphic traversal" is done via the polymorphic_tasks() method.

""",
u"""
HashSet is gone, uses set() for most sets in py2.4 or sets.Set.  
ordered set functionality supplied by a subclass of sets.Set

""",
u"""
"foreignkey" property of PropertyLoader is a sets.Set.  removed "foreigntable".
simplified/fixed foreign key location in _find_dependent(), fixes [ticket:151]

""",
u"""
fixed InvalidRequestException -> InvalidRequestError typo
""",
u"""
tweaks 

""",
u"""
0.2.2 prep, added "pickler" option to Pickle type

""",
u"""
force_close...

""",
u"""
more fixes to transaction nesting, interacts better with close() statement

""",
u"""
reorganized unit tests into subdirectories

""",
u"""
improvements/fixes to session cascade iteration,
fixes to entity_name propigation

""",
u"""
added new polymorph test, todos for session/cascade

""",
u"""
dbengine doc: no support for pg1
postgres: if module is none, still use pyformat for some unit tests


""",
u"""
doc for oracle fix

""",
u"""
confirmed that makedsn works with host/port/sid

""",
u"""
restored global_connect() function, default table metadata

""",
u"""
adjustment to datetime

""",
u"""
pool doesnt consume random **kwargs

""",
u"""
cleanup

""",
u"""
- got rudimental "mapping to multiple tables" functionality cleaned up,
more correctly documented

""",
u"""
update

""",
u"""
fixed host connector again, now for [ticket:197]

""",
u"""
switched generator to list comprehension

""",
u"""
create_connect_args can create DSN from host/port, submitted by bernd.dorn@fhv.at for [ticket:192]

""",
u"""
fixes half of [ticket:192], query.load()/get() with a unicode argument was failing to apply type conversion to the bind parameter

""",
u"""
"count" label changed to "rowcount", and default "count" argument is first pk col of the table or the first col if no pks

""",
u"""
implemented query string support in db urls, gets sent to dialect **kwargs, [ticket:196]

""",
u"""
more test adjustments for firebird

""",
u"""
brad clement's 0.2 firebird support !

""",
u"""
some comments...more to come

""",
u"""
inherited synchronization behavior fixed to descend all the way to the base class

""",
u"""
simplification/improvement to circular dependency sort (properly batches now)
mapper accepts add_property calls with columns that are not in its selectable (allows deferreds in, generally more lenient)

    """,
u"""
tweak to join test

""",
u"""
further tweaks to polymorphic loading...getting double polymorphic loaders to work

""",
u"""
further refinement of the polymorphic UOWTask idea.  circular dependency sort has to be pretty much focused on the base mappers
of any inheritance chain, as it now takes part in pretty much any two dependent classes who share the same inherited parent.

""",
u"""
fixed [ticket:188] updated changelog

""",
u"""
polymorphic linked list test, tests polymorphic inheritance with circular refs

""",
u"""
unit-tested product/specline/etc stuff

""",
u"""
more polymorphic adjustments to circular dependency sort

""",
u"""
echo_pool flag fixed
removed incorrect paragraph regarding release modes

""",
u"""
working on [ticket:190], getting circular dependency sort to work with inheriting mappers

""",
u"""
0.2.1 prep

""",
u"""
connection more careful about checking if its closed before operations
small fix to table sort if no tables
unit test tweaks

""",
u"""
added extra info for association object
threadlocal transaction benefits from an explicit close() on the connection besides de-referencing it

""",
u"""
exceptions...

""",
u"""
unit test adjustments to insure weakref status on connecitonfairy

""",
u"""
pool needed weakref
modified auto rollback to only occur when no transaction
more unit tests

""",
u"""
more tlocal trans stuff

""",
u"""
skips blank arguments

""",
u"""
extra tests...

""",
u"""
do-nothing dispose() method in SingletonThreadPool

""",
u"""
would help if commit() worked too...

""",
u"""
TLEngine needed a partial rewrite....

""",
u"""
check for not enough inserted pks to backfill the object

""",
u"""
raises error for bad url

""",
u"""
propigate "pool" argument

""",
u"""
selectresults docs

""",
u"""
it's police....

""",
u"""
formatting etc

""",
u"""
take two

""",
u"""
0.2 prep

""",
u"""
keep verbose false

""",
u"""
latest overhaul to association objects, plus an actual unit test
this change probably fixes [ticket:134]

""",
u"""
doc update

""",
u"""
broke out dumper into a separate module

""",
u"""
doc updates, added 'save' method to assignmapper

""",
u"""
circular dependency sort will not create new UOWTasks/UOWDependencyProcessors mid-stream
further construction on migrating UOWTask to be fully polymorphic

""",
u"""
unitofwork more Set oriented now
MapperProperty now has "localparent" and "parent" attributes, which in the case of
inheritance represent the mapper the property is attached to, and the original mapper it was created on.
the unitofwork now keeps the dependency processors derived from those properties unique so inheritance
structures dont register redundant dependency processors.

""",
u"""
converted sqlsoup, got its doctests working (werent working in 0.1 either....), added doctest hook to testsuite
fix to selectone_by/selectone when zero rows returned

""",
u"""
merged r. morrisons 0.2 update from branch to trunk

""",
u"""
added has_key to RowProxy, + caching of key lookups
fix for mapper translate_row for deferred columns
continuing with the "polymorph-tizing" of the unit of work, dependency processing accesses objects on each target task polymorphically


""",
u"""
uncompleted additional inheritance tests

""",
u"""
some TODOs

""",
u"""
bind parameter conflict in _get() resolved

""",
u"""
pretty major change to inheritance topological sorting - mapper dependencies are calculated
based on their ultimate "base inherited" mapper, UOWTasks organized into recursive inheritance structures based on the inheritance of the mappers.  this allows tasks across a class/mapper inheritance hierarchy to properly interact with other dependency processors and sub-tasks.

""",
u"""
correction to running single named tests

""",
u"""
workaround for get that requires multiple ids in the case of joined table inheritance

""",
u"""
added 0.1.7 changes to changelog
latest sqlsoup from 0.1.7
s. cazzells fixes to assignmapper, threadlocal

""",
u"""
merged 0.2 branch into trunk; 0.1 now in sqlalchemy/branches/rel_0_1

""",
u"""
added explicit check for "==null()" to produce IS NULL, documnted "==None", "==null()", [ticket:187]

""",
u"""
anonymous indexes use column._label to avoid name collisions

""",
u"""
hypothetical (failing) test for primary key selection of joins

""",
u"""
Implemented the changes from ticket 94
""",
u"""
c. martinez' fix to slicing logic

""",
u"""
typo fix

""",
u"""
rick morrison's CASE statement + unit test

""",
u"""
version id...

""",
u"""
title change

""",
u"""
removed .logo style

""",
u"""
extra unicode tests
added 'threaded' keyword argument to oracle.py (pretty important....)

""",
u"""
added pre-compiled docstring support

""",
u"""
added != support for None -> foo IS NOT NULL

""",
u"""
had unicode check improperly placed

""",
u"""
got removed somehow

""",
u"""
added __mod__ type

""",
u"""
fixed a _get_criterion mismatch, cleaned up types + updated types doc

""",
u"""
added from_obj option to select()

    """,
u"""
fixed HAVING/ORDER BY order, 0.1.7 prep

""",
u"""
save_obj/delete_obj need to specify column types to binds for primary key criterion

""",
u"""
foreignkey checks for unicode incoming string

""",
u"""
"order_by" parameter propigated to inheriting mappers
oracle ROW_NUMBER logic uses select.oid_column to get default order by

""",
u"""
gambit's patch to add DISTINCT ON

""",
u"""
added 'supports', 'unsupports' decorators to unittests so that they can all pass on all DBs

""",
u"""
more work on types.  this is the simplest implementation which is a little more manual

""",
u"""
*another* big types change....the old way was still wrong...this way is better (still need to go through it again since i am apparently type-impaired....)

    """,
u"""
fix for [ticket:169], moves the creation of "default" parameters more accurately
where theyre supposed to be

""",
u"""
fix to subquery parens

""",
u"""
the latest and greatest method to keep attributes from growing

""",
u"""
commented out default schema name check

""",
u"""
localtime/localtimestamp dont seem to need the underscore for postgres/mysql, making that default

""",
u"""
added unittest to verify eager loads refresh expired instances

""",
u"""
removed a "swap" from the lazy binary clause. added a test for that condition....

""",
u"""
lazyload clause calculation uses anonymous keynames for the bind parameters, to avoid compilation name conflicts

""",
u"""
Got the unit tests running again, apart from the two that were not working in
the first place.  The changes to process_relationships and to sqlachemy itself
were causing a double 'assign_mapper' call to cause issues.  Now, we basically
defer calling assign_mapper until process_relationships in cases where there
are defined relationships.

Also, I moved ActiveMapper to always use the default engine, as there were a
lot of hacks inside ActiveMapper to allow for engine swapping.  The use of the
default engine and the "global_connect" functionality significantly improves
the usability of ActiveMapper.

ActiveMapper will be getting a bit of a refactor/cleanup at some point in the
nearish future, as it has drifted a bit to complexity with the addition of some
features.  For now, this should do the trick!


""",
u"""
added temporary option "construct_new" to mapper which will cause the mapper to use __new__ to create loaded instances instead of the __init__ method

""",
u"""
some cleanup

""",
u"""
added extend() to historyarrayset

""",
u"""
Updates to ActiveMapper contributed by Gabriel Jacobo.  The main purpose of the
changes is to ensure that relationships are properly detected and built in the
proper order.  This should fix some problems that people were having with
ActiveMapper requiring classes to be declared in a specific order.

""",
u"""
what a strange thing to not be in there....

""",
u"""
fixed up expunge() and the continuing circular refs in attributes, added a unit test for the whole thing

""",
u"""
got circular many-to-many relationships to work

""",
u"""
mapper will verify class inheritance scheme; also will not re-init inherited property, as the improved attribute system seems to handle inheritance OK and allows the property to keep its correct initialization on the parent
exceptions import in query

""",
u"""
added cgi parser for url key/value connect strings, towards [ticket:157]

""",
u"""
fix for [ticket:158] regarding translate row

""",
u"""
added _get_from_obj to TypeClause

""",
u"""
a new batching algorithm for the topological sort

""",
u"""
had to take out the "treeification" of the dependency sort as it doenst really work , added test conditions to the dependency test + the original test that failed

""",
u"""
0.1.6...

""",
u"""
0.1.6 prep

""",
u"""
added a failing unittest for inheriting mappers with add_property

""",
u"""
added patch for mxDateTime support, [ticket:5], courtesy jkakar@kakar.ca

""",
u"""
latest from j. ellis...

""",
u"""
more files moving to .txt format plus enhancements to markdown converter

""",
u"""
Added preliminary support for inheritance.
""",
u"""
install_mod can take strings or module items

""",
u"""
pool argument adjusts for DBProxy/Pool

""",
u"""
a little spring cleaning for the util package, etc

""",
u"""
split up Session into Session/LegacySession, added some new constructor args
created AbstractEngine class which provides base for SQLEngine and will also 
provide base for ConnectionProxy, so SQL binding can be to an engine or specific
connection resource
ClauseElements get using() method which can take AbstractEngines for execution
made more separation between SchemaItems and bound engine

""",
u"""
mapper's querying facilities migrated to new query.Query() object, which can receive session-specific context via the mapper.using() statement.  reuslting object instances will be bound to this session, but query execution still handled by the SQLEngines implicit in the mapper's Table objects.
session now propigates to the unitofwork UOWTransaction object, as well as mapper's save_obj/delete_obj via the UOWTransaction it receives. UOWTransaction explicitly calls the Session for the engine corresponding to each Mapper in the flush operation, although the Session does not yet affect the choice of engines used, and mapper save/delete is still using the Table's implicit SQLEngine.
changed internal unitofwork commit() method to be called flush().
removed all references to 'engine' from mapper module, including adding insert/update specific SQLEngine methods such as last_inserted_ids, last_inserted_params, etc. to the returned ResultProxy so that Mapper need not know which SQLEngine was used for the execute.
changes to unit tests, SelectResults to support the new Query object.

""",
u"""
the __iter__ method on historyarraylist seemed to get broked...hmmmm

""",
u"""
added explicit "session" argument to get(), select_whereclause in mapper, as well as throughout the call-chain for those.  lazy loader honors the "session" of the parent object, + added simple unit test

""",
u"""
this assertion not really needed, esp. if a PickleType is used to take in a list

""",
u"""
added pickle test

""",
u"""
the ultimate "hands off" approach to the object's dictionary of managed attributes

""",
u"""
moves the binding of a TypeEngine object from "schema/statement creation" time into "compilation" time

""",
u"""
factored oid column into a consistent late-bound pattern, fixing [ticket:146]

""",
u"""
Added cast() to allow use of cast(tbl.c.col as Numeric(4,2)) in select and where clauses. Unit tests for same.

""",
u"""
put proper return type

""",
u"""
adjustments to auto-table-aliasing logic (R. Morrison)

    """,
u"""
added a unit test for the "version_id" keyword argument, which passes based on previous changes to Mapper

""",
u"""
update

""",
u"""
added 'entity_name' keyword argument to mapper.  a mapper is now associated with a class via 
the class object as well as the optional entity_name parameter, which is a string defaulting to None.
any number of primary mappers can be created for a class, qualified by the entity name.  instances of those classes
will issue all of their load and save operations through their entity_name-qualified mapper, and maintain separate identity from an otherwise equilvalent object.

""",
u"""
attributes overhaul #2 - attribute manager now tracks class-level initializers strictly through the SmartPropery instances attached to the class, so that attributes retain their natural polymorphic behavior.  naming conventions migrating to "managed_attribute", simplifying codepaths.

""",
u"""
further order_by:  order_by() with no arguments should not affect the current order_by clause (same with group_by)

    """,
u"""
ack, fixes to the order by stuff from last night

""",
u"""
DOH !

""",
u"""
still tryin to clarify....

""",
u"""
added to_selectable() onto ColumnClause to simplify _get_col_by_original

""",
u"""
made order_by/group_by construction a little more simplisitc
fix to mapper extension
CompoundSelect can export all columns now, not sure if theres any advantage there

""",
u"""
added a type to label....

""",
u"""
converted to markdown, added MS-SQL

""",
u"""
merged Rick Morrison / Runar Petursson's MS-SQL module, with adjustments to alias schema-qualified Table objects

""",
u"""
extra sql statements...

""",
u"""
got SQL blocks to work with markdown system, other enhancements
sqlconstruction converted to markdown syntax

""",
u"""
fixed reset_history method when applied to an attribute that had an attribute-level TriggeredAttribute set on it, added unit test.

""",
u"""
fix to oeprator test for new parenthesized rules

""",
u"""
added "parenthesis" check on binary clauses referencing binary clauses, for [ticket:144]

""",
u"""
cleanup of attributes, better naming, added weak reference to base managed attribute to break circular refs, slightly shorter codepaths in some cases. added performance tester

""",
u"""
second assertion

""",
u"""
added unit test for the old commit that was in [changeset:1186].  modified its behavior a bit to not delete private relationships unless they were already marked as deleted at the attribute manipulation level.  got "switching" behavior from one private relationship to another to work, added a unit test for that.

""",
u"""
added for_update flag to Select/CompoundSelect

""",
u"""
adjustments...

""",
u"""
tweak...

""",
u"""
got install_mods to work

""",
u"""
introducing...the mods package ! the SelectResults thing moves as the first mod

""",
u"""
starting to refactor mapper slightly, adding entity_name, version_id_col, allowing keywords in mapper.options()

    """,
u"""
wow, __len__ is a real disaster when combined with list()...turning that off

""",
u"""
Jonas Borgstrom's fantastic SelectRsults patch that adds dynamic list argument support to the mapper.select() methd.  associated unit test tweaks and mapper integration.


""",
u"""
fixed default example

""",
u"""
fixed "DISTINCT" spelling

""",
u"""
d

""",
u"""
tweak to mapper to allow inheritance on the same table.

""",
u"""
backrefs on cyclical relationships were breaking for the "root" node which had None for a parent, due to addition in [changeset:1186] which added a "deletion" traversal for many-to-one relationships.  added unittest.

""",
u"""
0.1.5 prep

""",
u"""
removed..

""",
u"""
added always_refresh flag.  when the mapper loads rows, it will pull objects from the identity map normally, but always blows away their attributes and replaces with those from the database, including changes

""",
u"""
rework to expire() to make it smarter.  when you expire(), history is immediately removed as well as explicit from dirty/deleted lists.  this also changes uow.rollback_object() to remove from those lists, which is strange that it didnt do that before.  anyway the mapper, when selecting and creating instances, asks the uow if this already identity-mapped instance is expired, and if so refreshes it on the fly, saving the need for the re-_get() operation, if some other query happens to touch upon the expired object.  unit test added to confirm this.

""",
u"""
fixed pickle example, its standard anyway....

""",
u"""
column label generation checks for a conflict against a column named the same as the label
comment in mapper

""",
u"""
improved translation of rows when proxying rows from one mapper to another.

""",
u"""
a cool example that illustrates vertical table storage, and objects that automatically configure themselves for this type of storage

""",
u"""
except it fails  a unit test.  OK, make it ia KeyError

""",
u"""
util: the __setitem__ method on historyarraylist was meaningless, surprising nobody noticed that.
types:  added PickleType, its slightly trickier than trivial, so OK now its standard.
attributes: the level of pain if an AttributeError occurs inside a CallableProp, in combination with an object that implements __getattr__,  is too deep for me to put the users through....so convert AttributeErrors to Assertions...
engine: im not a fan of catching universal exceptions and squashing them

""",
u"""
removed circular loop in creating new list elements, fixes a common refresh() condition
added None check in PropertyLoader many-to-one private deletion traversal, fixes byroot_tree (add a unit test for that)

    """,
u"""
removed all "tablename + '_' + columname" code and replaced with column._label, to take 
advantage of column labeling rules
bind param compilation,when it unique-ifys the name of bind params, maintains the length 
of the bind parameter name instead of appending to it

""",
u"""
added *args **kwargs pass-thru to transaction()

    """,
u"""
method add

""",
u"""
added expire/refresh/expunge to assign_mapper

""",
u"""
ah well the overflow doesnt work

""",
u"""
dev

""",
u"""
dev

""",
u"""
doc dev...

""",
u"""
doc dev

""",
u"""
doc devel

""",
u"""
update to types doc
commented out 'tutorial' from docuemnt_base until its complete
float extends numeric type

""",
u"""
ResultProxy has an iterator interface

""",
u"""
got some support for mapping to a select that only selects some of the columns of an underlying table

""",
u"""
added check in SessionTrans.begin() that the underlying unit of work is still the current uow

""",
u"""
added expunge() method to objectstore
correction in attributes reset_history to really reset in all cases
added unit tests testing refresh()/expire() bug that was fixed by reset_history thing

""",
u"""
added overrideable managed_attribute_dict() function which can be changed
to eliminate circular references on objects

""",
u"""
some more tweaks to get more advanced polymorphic stuff to work

""",
u"""
added explicit "convert date types to a string in bind params", since pysqlite1 doesnet seem to do it, operation is synymous with what pysqlite2 does

""",
u"""
added oracle8 test target, sets use_ansi to false
got mapper, objectstore, inheritance unittest working with oracle8, tweaks to join syntax

""",
u"""
another adjustment...

""",
u"""
some adjustments to oracle non-ansi join concatenation, 'row number over' syntax

""",
u"""
added some extra traversal for one-to-many/many-to-one "private" relations to allow single-object commits to cascade into private child objects

""",
u"""
removed print

""",
u"""
fixed oracle's efforts to get an ORDER BY for its ROW NUMBER OVER clause, fixed support for multi-leveled Alias objects to render correctly

""",
u"""
added Mapper class to the docstrings

""",
u"""
added some references to selectfirst

""",
u"""
added "nest_on" option for Session, so nested transactions can occur mostly at the Session level, 
fixes [ticket:113]

""",
u"""
added unit test to test proper construction of lazy clause against inherited mapper

""",
u"""
fixed lazy clause construction to go off...you guessed it...the noninherited table !

""",
u"""
added "name" back to FromClause

""",
u"""
a few changes to attributes.py to allow faster initialization of object attributes on new objects

""",
u"""
a refactoring to the EagerLoaders' _instance method to do a bunch of column arithmetic up front, instead of on each row

""",
u"""
a few tweaks and the polymorph example can also use eager loading

""",
u"""
print remove

""",
u"""
added size limit on test BLOB since mysql has a configured limit of 65535 (at least on my server....)

    """,
u"""
got dilbert to be properly modified....

""",
u"""
added distinct() function to column elements for "DISTINCT <col>"

""",
u"""
got rid of from "ids", using the From object itself as identity now.  improves correlation logic and fixes [ticket:116]

""",
u"""
got clause elements inside INSERTs going...

""",
u"""
der + engine...

""",
u"""
got oracle parenthesized rules for funcs back, fixed copy_container on function

""",
u"""
PropertyLoader will not re-determine direction when initialized a second time, as it is re-initialized as a copy made for an inheriting mapper, and no longer can get to the correct inheriting table.

""",
u"""
rolled back the operationalerror catch...definitely doesnt work right now

""",
u"""
put a try/finally to insure that SQLSession is cleaned out on rollback/commit regardless of issues

""",
u"""
overhaul to SQLSession change from yesterday, needs to use the threadlocal capability of the pool after all

""",
u"""
attempting to catch OperationalErrors and invalidate the connection

""",
u"""
added invalidate() method to connectionfairy, allows the connection to be removed from pooling

""",
u"""
identified more issues with inheritance.  mapper inheritance is more closed-minded about how it creates the join crit
erion as well as the sync rules in inheritance.  syncrules have been tightened up to be smarter about creating a new
SyncRule given lists of tables and a join clause.  properties also checks for relation direction against the "noninherited table" which for the moment makes it a stronger requirement that a relation to a mapper must relate to that mapper's main table, not any tables that it inherits from.

""",
u"""
an import !  eesh

""",
u"""
removed old function generation override, ANSI functions handled by the core now

""",
u"""
edits...

""",
u"""
making the verbiage a little more formal...(its good stuff, just not sure what I want yet)

    """,
u"""
fixed nasty transaction counting bug with new session thing + unit test

""",
u"""
refactor to engine to have a separate SQLSession object.  allows nested transactions.
util.ThreadLocal __hasattr__ method/raise_error param meaningless, removed
renamed old engines test to reflection

""",
u"""
fixes to function/property formatting

""",
u"""
SQLSession.....

""",
u"""
factored objectstore into two packages, one more public facing the other more to be *feared* ! :)


""",
u"""
John Dell'Aquila's patch which fixes [ticket:103] [ticket:105], selecting primary keys properly and using the ALL_* instead of USER_* tables

""",
u"""
expanded and integrated qvx's patch for dotted function names

""",
u"""
reorganized SingletonThreadPool to return distinct connections in the same thread; use_threadlocal behavior is now switchable

""",
u"""
added txt2myt.py to the genhtml/runhtml scripts, added exception if required modules arent found.
edited tutorial.txt, added particles, etc.
added clue that firebird might be supported to dbengine.myt

""",
u"""
J. Ellis' "Simple" ORM module...for Spyce !  (and others...)

""",
u"""
Tutorial draft (not finished) and documentation framework improvements

* a first step to a new documentation framework, using Markdown syntax, with
  some extensions (detailed in txt2myt.py docstrings):
  * `rel:something` for internal links
  * `{@name=something}` to override default header names (used when linking)
  * `{python}` to force code block to use Python syntax highlighting (not
     needed when using examples with `>>>` prompt)
* txt2myt.py -- converter from .txt to .myt
* a draft of tutorial.txt, which uses new syntax
* testdocs.py -- check examples in documentation using doctest (currently only
  in tutorial.txt) 

""",
u"""
added unique_connection() method to engine, connection pool to return a connection
that is not part of the thread-local context or any current transaction

""",
u"""
fixed attributes bug where if an object is committed, its lazy-loaded list got 
blown away if it hadnt been loaded

""",
u"""
formatting...

""",
u"""
removed redundant is_dirty function

""",
u"""
more notes, docs

""",
u"""
tweak

""",
u"""
added scalar subqueries within the column clause of another select

""",
u"""
Fix docstring and exception message in selectone_by
""",
u"""
Minor typo: encode and decode are methods.
""",
u"""
Fix typos, closing #89, #91, #92
""",
u"""
added selectfirst_by/selectone_by, selectone throws  exception if more than one row returned, courtesy J.Ellis

""",
u"""
tweak to get_direction, rolls back a comparison of "foreigntable" to "parent"/"mapper" table to be more constrained.  this change was originally in [changeset:1101] to help out the polymorph example but it now works without it.  the change breaks the Post/Comment relationship in the ZBlog demo since the Post mapper has the comments table inside of it (also with no workaround).

""",
u"""
caveat

""",
u"""
oracle is requiring dictionary params to be in a clean dict, added conversion
some fixes to unit tests

""",
u"""
small tweak to select in order to fix [ticket:112]...the exported columns when doing select on a select() will be the column names, not the keys.  this is with selects that have use_labels=False.  which makes sense since using the "key" and not the name implies a label has to be used.

""",
u"""
tweak to mysql default test

""",
u"""
refactor to Compiled.get_params() to return new ClauseParameters object, a more intelligent bind parameter dictionary that does type conversions late and preserves the unconverted value; used to fix mappers not comparing correct value in post-fetch [ticket:110]
removed pre_exec assertion from oracle/firebird regarding "check for sequence/primary key value"
fix to Unicode type to check for null, fixes [ticket:109]
create_engine() now uses genericized parameters; host/hostname, db/dbname/database, password/passwd, etc. for all engine connections
fix to select([func(column)]) so that it creates a FROM clause to the column's table, fixes [ticket:111]
doc updates for column defaults, indexes, connection pooling, engine params
unit tests for the above bugfixes

""",
u"""
added expire() function + unit test fixes [ticket:95]

""",
u"""
utf-8 encoding is switchable at the engine level, ticket [ticket:101]

""",
u"""
committed patch for MSDouble/tinyint from [ticket:106]

""",
u"""
added exception import

""",
u"""
HistoryArrayList checks internal list as a list or dict to clear it

""",
u"""
overhaul to types system, decoupled base type and engine-specific type into a composed pattern instead of goofy inheritance....gets rid of TypeDecorator (now a no-op) and enables all inhertance

""",
u"""
fixed assocaition example

""",
u"""
added 'noninherited table' prop to mapper indicating the "lead" table, in the case of
inheritance.  relations now create priamry/secondary joins against that lead table.  if you want to create it against
an inherited table, use explicit join conditions.
added 'correlate' argument to CompoundSelect to get polymorph example working again.

""",
u"""
a few tweaks to get table creates/reflection working
table names are always reflected back as having lowercase names

""",
u"""
tweak to engine param..

""",
u"""
added identity() method to mapper, to help get the primary key of an instance.

""",
u"""
added check to relation that will see if the same table is included between the primaryjoin and secondaryjoin, and raises a descriptive exception if so.

""",
u"""
serious overhaul to get eager loads to work inline with an inheriting mapper, when the inheritance/eager loads share the same table.  mapper inheritance will also favor the columns from the child table over those of the parent table when assigning column values to object attributes.  "correlated subqueries" require a flag "correlated=True" if they are in the FROM clause of another SELECT statement, and they want to be correlated.  this flag is set by default when using an "exists" clause.

""",
u"""
took erroneous 'count' off Alias

""",
u"""
took excess visit_func out, handled by ansisql compiler

""",
u"""
comment

""",
u"""
backref() func will also honor lazy=True/False

""",
u"""
added backref() function, allows the creation of a backref where you also send keyword arguments that will be placed on the relation

""",
u"""
checking in patch for column labels limit at 30 chars...what the heck

""",
u"""
patch on index create syntax to fix [ticket:90] so schema name gets included

""",
u"""
fixed bug in eager loading on a many-to-one [ticket:96], added the ticket tests as a unit test eagerload2.
got eagerload1 to be a unit test also.

""",
u"""
sqlite likes OFFSET with LIMIT else its buggy

""",
u"""
a mapper with inheritance will place itself as "dependent" on the inherited mapper; even though this is not usually needed, it allows certain exotic combinations of mapper setups to work (i.e. the one in the polymorph example)

""",
u"""
added new 'polymorphic' example.  still trying to understand it :) .
fixes to relation to enable it to locate "direction" more consistently with inheritance relationships
more tweaks to parenthesizing subqueries, unions, etc.

""",
u"""
more tweak to compoundselect parenthesizing/subquery flag

""",
u"""
selects within a compound clause dont get parenthesis added
fix to ColumnClause

""",
u"""
delete tables in an inheritance rel. requires them in reverse

""",
u"""
added unittest for orm-persisted insert without a postfetch, tweak to engine to only signal postfetch if the passivedefault columns received None/NULL for their parameter (since they dont exec otherwise)

    """,
u"""
got mapper to receive the onupdates after updating an instance (also properly receives defaults on inserts)...

""",
u"""
got column onupdate working
improvement to Function so that they can more easily be called standalone without having to throw them into a select().

""",
u"""
got column defaults to be executeable

""",
u"""
added public-friendly setattr_clean and append_clean

""",
u"""
moved name to 'defaults', going to put more default stuff in

""",
u"""
making sequences, column defaults independently executeable

""",
u"""
removed the dependency of ANSICompiler on SQLEngine.  you can now make ANSICompilers and compile SQL with no engine at all.

""",
u"""
initial table reflection support courtesy Andrija Zaric

""",
u"""
changed default "none" parameters to check positional style

""",
u"""
firebird module initial checkin

""",
u"""
mr. bangerts surprise paragraph rewrite demands strike again 

""",
u"""
rudimentary support for many-to-many relation. Still requires a separately defined intermediate table.
""",
u"""
added util.Logger object with configurable thread/timestamp view

""",
u"""
changed ENGINE to TYPE, for mysql 4 compatibility

""",
u"""
formatting

""",
u"""
its release time

""",
u"""
added objectstore.refresh(), including supporting changes in mapper, attributes, util

""",
u"""
unicode

""",
u"""
module fix

""",
u"""
engine argument on tables optional
test suite uses BaseProxyEngine as a base for the tester engine
documented global proxy engine

""",
u"""
engine property allows polymorphic access to get_engine/set_engine

""",
u"""
got unicode to do None...

""",
u"""
made SchemaEngine more prominent as the base of Table association
BaseProxyEngine descends from SchemaEngine
fixes to sqlite/postgres reflection to use the correct engine for table lookups
Table engine can be none which will default to schema.default_engine (although its
still positional for now, so still needs to be explicit to make room for Columns)
__init__ sets default_engine to be a blank ProxyEngine
fixes to test suite to allow --db proxy.<dbname> to really test proxyengine

""",
u"""
postgres leaves parenthesis off functions only for no-argument ANSI functions according to a list

""",
u"""
Modified mysql to not add AUTOINCREMENT to the first integer primary key if it is also a foreign key.

""",
u"""
added schema support for postgres column defaults, fix for [ticket:88]

""",
u"""
update

""",
u"""
added convert_unicode flag to engine + unittest, does unicode in/out translation on all string/char values when set

""",
u"""
small cleanup courtesy j.ellis

""",
u"""
oid inits at compilation time/when needed again, added a unit test

""",
u"""
added items() method to RowProxy + unittest, courtesy dialtone@divmod.com

""",
u"""
took out that "TypeError" wrapper since it blows away stack traces and confuses users

""",
u"""
fixed an import

""",
u"""
Added code to make foreignkey on ActiveMapper accept a string and create the ForeignKey object on the fly. Also added ability to pass args and kwargs to Column constructor. ActiveMapper columns can have keyword args indexed and unique which will automatically create a index or a unique index. dburi in AutoConnectEngine can be a callable.
""",
u"""
updates

""",
u"""
formatting

""",
u"""
got mapper.using() to work, fixed push/pop mapper, custom session assignments

""",
u"""
doc update for post_update flag

""",
u"""
more work on cycles, fleshed out tests for post_update, fix to the delete phase of a one-to-many post update
closes [ticket:67]

""",
u"""
imported casacde_mappers

""",
u"""
Merge indexes [1047]:[1048] into trunk (for #6)
    """,
u"""
implemented SyncRules for mapper with inheritance relationship, fixes [ticket:81]
TableFinder becomes a list-implementing object (should probably create clauseutils or sqlutils for these little helper visitors)

    """,
u"""
factored out "syncrule" logic to a separate package, so mapper will be able to make use of it as well as properties.  also clarifies the "synchronization" idea

""",
u"""
place _instance_key on object only when objectstore finally register_clean's on it, to make
room for more aggressive "identity map" assertion when modifying objects incoming from a result set

""",
u"""
postgres wraps exec's in SQLError catch

""",
u"""
register_deleted/register_dirty perform pre-check before doing the "validate" operation to cut down on method overhaed

""",
u"""
fixed exception import.  check for objects being present in the identity map occurs not just 
at commit time but also when its logged as "dirty" or "deleted".

""",
u"""
added test to illustrate wacky inhertitance/many-to-many thing

""",
u"""
adjustment to compile synchronizers which allows many-to-many synchronize to work even when one side of the relation has both tables in it (new unittest will be added to inheritance.py to show this...)

    """,
u"""
fixed ticket 72, where a copied clause was using the identical bind param object thereby screwing up a generated statement that included both the original clause and the copied clause, when positional parameters were used

""",
u"""
create() statements return the created object so they can be instantiated and 
create()'ed in one line

""",
u"""
fixed many-to-many example, which was utterly incorrect in many ways

""",
u"""
Refactored ProxyEngine into BaseProxyEngine and ProxyEngine. Also added an AutoConnectProxyEngine to late bind to a particular dburi. I ran the proxy_engine test, however, I don't have postgresql installed so not all tests worked. Also, I don't have an WSGI package installed to run the wsgi tests.


""",
u"""
clauseelement.compile() totally works without an engine

""",
u"""
merged sql_rearrangement branch , refactors sql package to work standalone with 
clause elements including tables and columns, schema package deals with "physical" 
representations

""",
u"""
tentative fix for oracle row_number over syntax

""",
u"""
update

""",
u"""
get() method needs to use the full table, not just the 'primary' table, to get the full list of primary key cols

""",
u"""
fix to silent "recursive" bug in schema getattr that was somehow running only 994 times

""",
u"""
release time

""",
u"""
update

""",
u"""
Function needed compare_type so that its type is set as the type in boolean expressions

""",
u"""
moved iteration of props so that props can set up self-referring backref properties without getting a "list changed during iteration" error

""",
u"""
test commit

""",
u"""
one more test commit

""",
u"""
this is a test commit

""",
u"""
more fix to one-to-one: 'unchanged_items' can be [None] also with one to one so check for this
during delete

""",
u"""
when begin/commit, an exception should still reset the transactional state

""",
u"""
fix to EagerLoad where it late-initializes its eager chain, thereby not getting messed up by late add_property() calls

""",
u"""
when creating lazy clause both sides of each clause must be Column

""",
u"""
working on postupdate idea, refactoring to dependency processing

""",
u"""
merged eager loading overhaul rev 1001:1009
this includes:
sql.Alias object keeps track of the immediate thing it aliased as well
as the ultimate non-aliased (usually a Table) object, so that proxied columns can have
a "parent" attribute
some cleanup to SelectBaseMixin.order_by_clause to allow easier access, needs more cleanup
engine has been making two ResultProxies all this time, added "return_raw" quickie flag to 
disable that
some cleanup to _get_col_by_original so that it also works for oid columns, new eager load stuff
more aggressively aliaseses orderby's so this was needed
EagerLoader now makes "chains" of unique aliased eager loaders in all cases.  no need for
use_alias/selectalias anymore since it aliases every time.
properly detects recursive eager loads and terminates them with a lazyloader, instead of
raising an exception.  totally simplified setup() and init() is more straightforward and has
a single codepath now instead of two or three.

""",
u"""
made 'assign_mapper' doc more explicit
added doc for overriding properties

""",
u"""
none check for pg1 date/time values

""",
u"""
some comments, changed SmartProperty to be smarter, UOW
version has "property" accessor which returns MapperProperty at 
the class level

""",
u"""
doc

""",
u"""
some docstrings etc

""",
u"""
exceptions added
postgres last_inserted_ids will raise an error unless OID's are turned on
(INSERT with PK defaults + no OIDs wont fail unless this method is called)

    """,
u"""
exception package added, support throughout

""",
u"""
onetoone

""",
u"""
converted to a unittest

""",
u"""
test only for postgres

""",
u"""
beginning of a row cycle test

""",
u"""
updating

""",
u"""
added hooks for engines to add stuff to SELECT, etc.

""",
u"""
base begin method returns transaciton object

""",
u"""
ongoing

""",
u"""
added new style of begin/commit which returns a tranactional object

""",
u"""
added indexes to schema/ansisql/engine
slightly different index syntax for mysql
fixed mysql Time type to convert from a timedelta to time
tweaks to date unit tests for mysql

""",
u"""
comment verbiage

""",
u"""
postgres needs to explicitly pre-execute PassiveDefaults on primary key columns, test added

""",
u"""
modified query that uses JOIN keyword explicitly.  a user gets much better performance with it (though I dont)

    """,
u"""
bind params upon insert are totally column "name" based, so in process_defaults set newly acquired parameter by name also

""",
u"""
added an assertion to insure that a column is only attached to one table

""",
u"""
Modified objectstore to look for primary key param values by column name not key name. Added test for same.

""",
u"""
tweak to get tables to show up

""",
u"""
added another multi-pk test

""",
u"""
fix to types test, postgres time types descend from Time type

""",
u"""
got inheritance into alltest

""",
u"""
ok now they worked...

""",
u"""
inheritance test
tweaking to try to get alltests to work, unsuccessful

""",
u"""
Join object wasnt exporting foreign keys correctly
compile_synchronizers in PropertyLoader needed to take into account the full list of tables for each mapper when looking for synchronization rules, not just primary table

""",
u"""
comment

""",
u"""
the list-based foreign key doenst seem to work quite right, rolling it back

""",
u"""
bind_to fix

""",
u"""
0.1.0

""",
u"""
fixed FLOAT type

""",
u"""
fix

""",
u"""
tweaks for order_by

""",
u"""
tweak to oracle limit/offset to not put ora_rn in the select list

""",
u"""
fixes mostly to get the important unit tests to run for Oracle, boxesw without wsgi_utils

""",
u"""
oracle likes to use VARCHAR isntead of CLOB so put limits on String

""",
u"""
tweak

""",
u"""
docstring...

""",
u"""
latest reorgnanization of the objectstore, the Session is a simpler object that just maintains begin/commit state

""",
u"""
lazy load column fix courtesy raul garcia garcia

""",
u"""
fix to string concatenation operator courtesy Marko Mikulicic

""",
u"""
added import for pysqlite1

""",
u"""
tweak to TableImpl/ColumnImpl with the way they get their attribute

""",
u"""
some updates to UOW, fixes to all those relation() calls

""",
u"""
added 'post_update' attribute to PropertyLoader, means to defer processing of this property until after the object has been saved, and then to re-sync and force an update.  used to break otherwise intra-row cycles.  added for "many-to-one" so far.

""",
u"""
more refactoring to session/UOW scope management...under construction !

""",
u"""
some tweaks to options, use_alias, live removed

""",
u"""
assertion

""",
u"""
'column' function (make a ColumnClause) is more useful from sql module, removed 'column' (make a ColumnProperty) from __init__

""",
u"""
cleanup and organization of code mostly in properties, making SyncRules clearer,
also "foreignkey" property can be a list, particularly for a self-referential table with a multi-column join condition

""",
u"""
slight glitch when the same clause is compiled repeatedly and contains redundant bind parameters...this fix prevents the binds from stepping on each other....

""",
u"""
some comments for default test

""",
u"""
more hammering of defaults.  ORM will properly execute defaults and post-fetch rows that contain passive defaults

""",
u"""
integrating Jonathan LaCour's declarative layer

""",
u"""
tableimpl and columnimpl proxy to actual impl objects per engine

""",
u"""
streamlined engine.schemagenerator and engine.schemadropper methodology
added support for creating PassiveDefault (i.e. regular DEFAULT) on table columns
postgres can reflect default values via information_schema
added unittests for PassiveDefault values getting created, inserted, coming back in result sets

""",
u"""
crazy postgres and its foreign key constraints

""",
u"""
fixes to TypeDecorator, including A. Houghton's patch

""",
u"""
beefed up type adaptation methodology, got Unicode to do encode/decode + test case

""",
u"""
fix to manytomany

""",
u"""
put assertion in to check for secondary table if secondaryjoin explicit

""",
u"""
added before_update/after_update

""",
u"""
objectstore refactored to have more flexible scopes for UnitOfWork
central access point is now a Session object which maintains different
kinds of scopes for collections of one or more UnitOfWork objects
individual object instances get bound to a specific Session

""",
u"""
commented out print statement

""",
u"""
somewhat of an overhaul, got alltests to work again

""",
u"""
derefences connection pool upon dispose()

    """,
u"""
deprecated "selectalias" argument on eager loader, do use_alias=True
"eager alias" flag will propigate to child eager loaders so the full query comes 
out OK.  mappers/properties have overhauled "copy" methodology.  mappers 
are no longer "singleton" and no longer have elaborate "hash_key" methods - there
is a primary mapper associated with a class which is done via direct dictionary 
relationship, and the options() method on mapper does its own lighter-weight caching
of created mappers.  the unitofwork does extra work with the mappers it receives
to insure its dealing with "the primary" mapper, so that properties can be more liberal 
about which mapper they reference (i.e. not the primary one).
options() works better but still could use a looking-at to see that
its not wasteful.  simplified mapper() method in __init__.


""",
u"""
took out print statement

""",
u"""
trying to get mappers to support having versions against different tables for the same class,
that dont affect the original class mapper and create objects with the correct identity key
support in EagerLoader to better handle "selectalias" when the eager mapper hits another eager mapper, etc

""",
u"""
took mysql foriegn key thing out

""",
u"""
foreign key reflection !!!!!

""",
u"""
moved stylesheets into section_wrapper so that autohandler can be more easily replaced
(when used on the site)

    """,
u"""
added 'engine' to convert_result_value/convert_bind_param

""",
u"""
added cascade_mappers function.  somewhat experimental !

""",
u"""
docs

""",
u"""
added between(), column.label()

    """,
u"""
table supports per-engine-type options, ansisql allows engines
to add a "post table create" string
mysql gets mysql_engine argument
InnoDB set as default in engines test


""",
u"""
added is_dirty method at module level and within UnitOfWork

""",
u"""
__init__ monkeypatch looks for __init__ in the class' dict rather than via getattr(), to bypass inheritance lookups


""",
u"""
writes foreign keys as individual FOREIGN KEY objects, syntax seems to work better

""",
u"""
got oracle LIMIT/OFFSET to use row_number() syntax
sql: ColumnClause will use the given name when proxying itself (used for the "ora_rn" label)
ansisql: When adding on ORDER_BY, GROUP_BY, etc. clauses, if there is no string for the column list,
then dont add the clause (this allows oracle to strip out the ORDER BY)
Oracle is modifying the select statement, which is not ideal - should fix that

""",
u"""
more Sequences needed for oracle

""",
u"""
ordering of queries can be different based on platform dictionary ordering

""",
u"""
now lets do that properly

""",
u"""
error message if pysqlite2 couldnt be imported

""",
u"""
needed optional sequence for oracle support

""",
u"""
dont mask engine compilation error

""",
u"""
Provisional fix for #51, very slightly adapted from the patch posted in the ticket. Tests added to verify fix.


""",
u"""
started PassiveDefault, which is a "database-side" default.  mapper will go
fetch the most recently inserted row if a table has PassiveDefault's set on it

""",
u"""
columns can be specified to override those from autoload=True

""",
u"""
is_unicode propigated into String subclasses

""",
u"""
added BETWEEN, courtesy Rick Morrison.  go Rick !

""",
u"""
fixes involving when child object from list items is None - onetoone must pass, objectstore.testbackwardsmanipulations with postgres passes

""",
u"""
added ISchema object to engine/information_schema, provides somewhat generic information_schema access for db's that support it, i.e. postgres, mysql 5

""",
u"""
a future unit-test for testing one-to-one relationships

""",
u"""
one-to-one support:
rolled the BackrefExtensions into a single GenericBackrefExtension to handle
all combinations of list/nonlist properties (such as one-to-one)
tweak to properties.py which may receive "None" as "added_items()", in the case of a scalar property
instead of a list
PropHistory masquerades as a List on the setattr/append delattr/remove side to make one-to-one's automatically
work

""",
u"""
added DATE, TIME, SMALLINT to __all__

""",
u"""
Rick Morrison's patch adding Smallint, Date, and Time support !

""",
u"""
beginnings of a "multilple relations to the same table" test

""",
u"""
verbiage edits

""",
u"""
attempting to get MTOBackrefExtension to handle many-to-one, one-to-one equally

""",
u"""
fixed set() to not re-set the same value

""",
u"""
switched objectstore begin/commit behavior to do "reentrant counter"

""",
u"""
deprecated relation(class, table)
changed unit tests/examples to not do it

""",
u"""
self->compare_self()

    """,
u"""
added doc for ProxyEngine

""",
u"""
unit tests for proxy engine

""",
u"""
init

""",
u"""
might add scalar() to select which does limit=1

""",
u"""
new ProxyEngine dispatches to multiple engines; contributed by jason pellerin

""",
u"""
unit tests for merged cylical code

""",
u"""
merged new cyclical dependency code
EagerRelation gets a fix w/ regards to selectalias

""",
u"""
moved dict init to setattr for auto-__init__ thing

""",
u"""
dev on uow docs

""",
u"""
merged fix that insures unrealized connections dont fill up the pool

""",
u"""
fixed code error

""",
u"""
added to trunk

""",
u"""
Tabs to spaces

""",
u"""
Reworked RowProxy to restore column order preservation and to remove some dictionary-like behaviour that was unnecessary and caused breakage in existing code. Added tests for column preservation.

""",
u"""
Added __len__ to RowProxy to allow len(r) and test for same.

""",
u"""
RowProxy changes - added keys(), used keys() to add more dictionary-like behaviour (values(), iteritems(), iterkeys(), etc). Made parent and row private. Modified tests that used RowProxy.row to use values().

""",
u"""
took out print statement

""",
u"""
topological sort can detect cycles, and assemble them into a "big node" with all 
the nodes in the cycle aggregated into one node

""",
u"""
working on representing longer circular relationships

""",
u"""
2nd scalar fix

""",
u"""
scalar() returns None if no rows

""",
u"""
starting uow doc....

""",
u"""
converted LEFT,RIGHT, CENTER to more reasonable names

""",
u"""
task dump checks for None

""",
u"""
refactoring to allow column.label() to work in selects, etc.
fixed superfluous codeline in ForeignKey

""",
u"""
test for inheritance, tests objectstore post_exec works fully

""",
u"""
refactoring of objectstore to handle cleaning up after itself with less
instruction from properties/mapper
objectstore gets an assertion for appending a deleted item
mapper has fix for inheritance
mapper selectone() etc. set "limit=1"

""",
u"""
ai more reasonable hash_key that works across serializations
might want to get the DB password out of it tho....

""",
u"""
added __repr__ to HashSet 

""",
u"""
fix to inheritance example

""",
u"""
Added column accessor to RowProxy, tests and note in documentation for same.

""",
u"""
adds a traversed list to the list of things to clean up

""",
u"""
postgres checks for string/int port ID, converts to int for pg2 and string for pg1

""",
u"""
order_by and group_by being output in wrong order. Added tests for same.

""",
u"""
added some echo arguments for uow, pool, propigated from the engine

""",
u"""
adjustment to dependencies+childtasks attached to circular task - they go 
on just the lead task instead of each per-object task.
more tweaks to dumper output

""",
u"""
rewrote objectstore logging

""",
u"""
comment out dump, reverse check for self-ref task/delete-matchup

""",
u"""
when breaking a circular task into child tasks, propigate the child tasks and the non-self-referring dependencies of the lead task to each child task...else they dont happen !

""",
u"""
formatting?

""",
u"""
some docstrings

""",
u"""
unset attributes on an object instance just return None instead of raising attributeerror

""",
u"""
added explicit bind parameters and column type maps to text type
text type also parses :<string> into bind param objects
bind parameters convert their incoming type using engine.type_descriptor() methods
types.adapt_type() adjusted to not do extra work with incoming types, since the bind
param change will cause it to be called a lot more
added tests to new text type stuff, bind params, fixed some type tests
added basic docs for using text with binde params

""",
u"""
implemented better hash_key on select allowing proper comparisons, implemented
hash_key on all clause objects
added hash_key test to select
util gets extra threadlocal functions and the recursionstack object

""",
u"""
tabbing fix

""",
u"""
more whitespace

""",
u"""
whitespace wrangling

""",
u"""
fix

""",
u"""
dispose() added to pool/engine to allow engines to fall out of scope

""",
u"""
changes to support docs in IE, adds a lot of whitespace....

""",
u"""
Formatting fix.

""",
u"""
Fixed problem in Column.copy(), _make_proxy() with nullable and hidden not being reflected into new Column. Added test for same. Removed reference to non-existant columns test from list of tests in alltests.

""",
u"""
assign_mapper will create a default __init__ method if one doesnt exist

""",
u"""
fullname for table used when generating REFERENCES

""",
u"""
column arguments converted to integer

""",
u"""
mysql table introspection uses 'describe' to work with 3/4/5
no foreign key introspection available, sorry !

""",
u"""
on foreign key default schema is that of the parent column

""",
u"""
tests mapper column/property check

""",
u"""
checks for relations that override columns and raises an error if override_columns_ok not set

""",
u"""
 r818@lightspeed:  robert | 2006-01-12 18:32:38 +1100
 Added class name to the TypeError string to make it easier to find constructor problems when mapper is constructing complex mappings

 """,
u"""
id key uses hash_key off of table now that its a short string

""",
u"""
indent fix

""",
u"""
fixes

""",
u"""
does pydoc for properties too

""",
u"""
 r815@lightspeed:  robert | 2006-01-11 10:15:14 +1100
 Replaced use of repr() with custom identifiers in identity related areas to improve performance

 """,
u"""
tabs->spaces !  (also relies upon '2' being present in version id)

""",
u"""
identity map->weakvaluedictionary

""",
u"""
 r810@lightspeed:  robert | 2006-01-10 11:49:18 +1100
 Added check for __version__ to determine if pyscopg is v1 or v2

 """,
u"""
ColumnClause needed optional foreign_key parameter

""",
u"""
typos

""",
u"""
added some __repr__ functionality

""",
u"""
sqlite/postgres reflection will properly add foreign keys
added append_item() method to column to work similarly to table.append_item(), used to
append foreign keys to the column (required in mysql)
appending new foreign keys will properly replace the old one, so explicitly appending
foreign keys to tables will replace those loaded via table reflection (instead of doubling them up)


    """,
u"""
added count func to mapper

""",
u"""
added count() to table, from objects

""",
u"""
added the README to the description

""",
u"""
key/value params on execute() are based off the from objects, not the select list

""",
u"""
mit license

""",
u"""
removed 'primarytable'  keyword argument

""",
u"""
small adjust after mapper/sql overhaul

""",
u"""
remove method on HashSet

""",
u"""
added 'import_instance' to properly deal with out-of-imap objects,
added assertion upon commit that all mapped objects are properly present in the identity map

""",
u"""
modified 'primarytable' idea and 'inheritance' to work better with improved relational
algrebra stuff

""",
u"""
unit tests to test column/pk/fk exports on relational objects

""",
u"""
moved 'float' test into types test, renamed typetest to overrride test

""",
u"""
misc commenty type stuff

""",
u"""
improvements to relational algrebra of Alias, Select, Join objects, so that they
all report their column lists, primary key, foreign key lists consistently
and so that ForeignKey objects can line up tables against relational objects

""",
u"""
testing backref/lazyload uses mapper.get()

    """,
u"""
mapper - pks_by_table should store keys in order even tho we dont have a failure case
lazyloader can lazyload using mapper.get() if it is appropriate, saves a lot of queries
a few more assertions in properties in prep for relations against select statement mappers
mapper get() clause is determined upfront to avoid re-generating it

""",
u"""
added compare function to the more basic expression objects
adding priamry_key/foreign_keys to selects, alias etc to increase their useability for relating them to tables
improved _get_col_by_original to double-check the column it finds

""",
u"""
better exception catch

""",
u"""
added support for foreign keys to work across schemas

""",
u"""
outerjoin onclause is optional

""",
u"""
edits

""",
u"""
copyright->2005,2006

""",
u"""
cleanup to mapper/relation order_by parameter to be more consistently picked up
down the chain of engine->mapper->select()
documented mapperoption methods


""",
u"""
added binary unit tests
moved datetest to the types module

""",
u"""
type objects pass engine around to get a hold of DBAPI type objects
added dbapi.Binary creation to base BinaryType
fixed MySQL binary type
adjustment to Join._match_primaries to work better with self-referential table


""",
u"""
remove debugging code

""",
u"""
trying to get pg1 date type to work, unsuccessful

""",
u"""
moved tables into examples so basic_tree could be simplified

""",
u"""
new options, new examples

""",
u"""
column.label is now a function; fix byroot example, add 'default_label' accessor to columnimpl

""",
u"""
broke apart deafult ordering into oid or primary key.  a DB that has no oids will have a None oid_column attribute.

""",
u"""
order by oid -> order by *default_order_by() when called by mapper layer.
- one layer of abstraction between the "oid" and default ordering

""",
u"""
rowid->oid

""",
u"""
changed mysql TIMESTAMP->DATETIME
fixed up date unit test
RowProxy __iter__ properly routes columns through type processing

""",
u"""
factoring out mysql's rowid stuff since its down in the base engine class now

""",
u"""
rowid_column becomes more like the "order by column".  'default_ordering' flag sent to create_engine enables whether or not the rowid_column on a Table will be None or not.  mappers/relations will by default use the rowid_column for ordering if its not None, else theres no default ordering.  
still should better define 'default_ordering'/'rowid_column' relationship since its a little kludgy.

""",
u"""
postgres oids say byebye by default, putting hooks in for engines to determine column defaults externally to it having a 'default' property, beefed up unittests to support inserts with/without defaults (will fix oracle unit tests too)


""",
u"""
docdev

""",
u"""
added a hook in for 'binary operator', so sqlite can exchange
'+' for '||' for a binary clause on a string

""",
u"""
shuffling to allow standard 'types' module in
bindparam allows class-based type in
added 'op' to comparemixin to allow custom operators

""",
u"""
fix to ansisql when it tries to determine param-based select clause that its
only on a column-type object
engine has settable 'paramstyle' attribute 

""",
u"""
license switch

""",
u"""
datetime introspection adjustment
license switch

""",
u"""
some doc changes
license move

""",
u"""
changes related to mapping against arbitrary selects, selects with labels or functions:

testfunction has a more complete test (needs an assert tho);
added new labels, synonymous with column key, to "select" statements that are subqueries with use_labels=False, since SQLite wants them - 
this also impacts the names of the columns attached to the select object in the case that the key and name dont match, since
it is now the key, not the name;
aliases generate random names if name is None (need some way to make them more predictable to help plan caching);
select statements have a rowid column of None, since there isnt really a "rowid"...at least cant figure out what it would be yet;
mapper creates an alias if given a select to map against, since Postgres wants it;
mapper checks if it has pks for a given table before saving/deleting, skips it otherwise;
mapper will not try to order by rowid if table doesnt have a rowid (since select statements dont have rowids...)


""",
u"""
some adjustments

""",
u"""
roadmap->trailmap

""",
u"""
roadmap->trailmap

""",
u"""
reworking concept of column lists, "FromObject", "Selectable";
support for types to be propigated into boolean expressions;
new label() function/method to make any column/literal/function/bind param
into a "foo AS bar" clause, better support in ansisql for this concept;
trying to get column list on a select() object to be Column and ColumnClause
objects equally, working on mappers that map to those select() objects


""",
u"""
adjustments for oracle sequences

""",
u"""
catching up oracle to current, some tweaks to unittests to work better with oracle,
allow different ordering of expected statements.
unittests still dont work completely with oracle due to sequence columns in INSERT statements

""",
u"""
url change

""",
u"""
updates for assignmapper, inherit_condition not required

""",
u"""
doc updates

""",
u"""
moved _match_primaries from properties to sql.join, so its generalized to all SQL

""",
u"""
removed assignmapper

""",
u"""
select_by/get_by get SQL clauses as well
public-facing columns on the mapper populated based on given properties first,
then table columns

""",
u"""
comments re: partial ordering, association dependencies
license for topological

""",
u"""
association object dependency glitches

""",
u"""
arg fix in create_engine

""",
u"""
the 'column' function is optional to point a property to a column when constructing a mapper
can also be specified as a list to indicate overlap
mapper columns come from its table, no need to add from given columns

""",
u"""
ColumnProperty -> column

""",
u"""
docstrings

""",
u"""
mapper, when updating, only SET's those columns that have changed.
this also allows "deferred" column properties to remain untouched by a save operation
if they werent affected.

""",
u"""
added defer and undefer mapper options

""",
u"""
remove debugging/comments

""",
u"""
refactor/cleanup to mapper options methodology to allow for incoming defer/undefer options
mapper/relations are stricter about class attributes and primary mapper - is_primary flag
on relations fixed (wasnt working before). new primary mappers clear off old class attributes, 
secondary mappers insure that their property was set up by the primary; otherwise secondary
mappers can add behavior to properties that are unmanaged by the primary mapper
added "group" option to deferred loaders so a group of properties can be loaded at once
mapper adds the "oid" column to the select list if "distinct" is set to true and its 
using the default "order by oid" ordering (mysql benefits from ansisql fix to only print out unique
columns in the select list since its oid is the same as the pk column)
fixed unittests to comply with stricter primary mapper rules

""",
u"""
move execute parameter processing from sql.ClauseElement to engine.execute_compiled
testbase gets "assert_sql_count" method, moves execution wrapping to pre_exec to accomodate engine change
move _get_colparams from Insert/Update to ansisql since it applies to compilation
ansisql also insures that select list for columns is unique, helps the mapper with the "distinct" keyword
docstrings/cleanup


""",
u"""
deferred property, checks for NULL primary key components and returns None

""",
u"""
added 'deferred' keyword, allowing deferred loading of a particular column

""",
u"""
added "late WHERE" compilation to SELECT, adds where criterion based on extra bind parameters specified
at compilation/execution time

""",
u"""
fix to parameter thing in insert
added unicodetype to __all__ for types

""",
u"""
added assign_mapper

""",
u"""
more complete commit when object list is specified

""",
u"""
fix to engine echo, random rundocs 

""",
u"""
in_ clause uses bind params, for typing etc.

""",
u"""
typemap needs lower case keys since result set metadata is not always case-sensitive (like in oracle)

""",
u"""
need to do before_insert before populating the insert row

""",
u"""
fix to oracle function select, users table in test should be non-sequence

""",
u"""
put an assertion in default test

""",
]


