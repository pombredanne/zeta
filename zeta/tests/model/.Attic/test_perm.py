from   __future__            import with_statement
import unittest

from   pylons                import config
from   sqlalchemy.exceptions import IntegrityError, InvalidRequestError

from   zeta.model            import meta
from   zeta.model.tables     import System, PermissionName, PermissionGroup
from   zeta.lib.error        import ZetaPermNameError, ZetaNamelenError, \
                                    ZetaPermGroupError


# TODO :
#   1. Verify, verify_permnames() and verify_permgroups() functions

def _add_obj( msession, obj ) :
    with msession.begin() :
        msession.add( obj )

def _del_obj( msession, obj ) :
    with msession.begin() :
        msession.delete( obj )

class TestPermissions( unittest.TestCase ) :
    def test_invalid_permname( self ) :
        self.assertRaises( ZetaPermNameError, PermissionName, '' )
        self.assertRaises( ZetaPermNameError, PermissionName, '_' )
        self.assertRaises( ZetaPermNameError, PermissionName, 'perm_name_' )
        self.assertRaises( ZetaPermNameError, PermissionName, '_perm_name' )
        self.assertRaises( ZetaNamelenError, PermissionName, 
                           'perm_123456789123456789123456789123456789' )

    def test_invalid_permgroup( self ) :
        self.assertRaises( ZetaPermGroupError, PermissionGroup, '' )
        self.assertRaises( ZetaNamelenError, PermissionGroup, 'gr' )
        self.assertRaises( ZetaNamelenError, PermissionGroup, 
                           'permgroup_123456789123456789123456789' )

    def test_duplicate_permname( self ) :
        msession   = meta.Session()
        perm_obj1 = PermissionName( 'perm10_name1' )
        perm_obj2 = PermissionName( 'PERM10_NAME1' )
        with msession.begin() :
            msession.add( perm_obj1 )
        self.assertRaises( IntegrityError, _add_obj, msession, perm_obj2 )
        with msession.begin() :
            msession.delete( perm_obj1 )
        self.assertRaises( InvalidRequestError, _del_obj, msession, perm_obj2 )

    def test_duplicate_permgroup( self ) :
        msession   = meta.Session()
        perm_obj1 = PermissionGroup( 'GROUP10' )
        perm_obj2 = PermissionGroup( 'group10' )
        with msession.begin() :
            msession.add( perm_obj1 )
        self.assertRaises( IntegrityError, _add_obj, msession, perm_obj2 )
        with msession.begin() :
            msession.delete( perm_obj1 )
        self.assertRaises( InvalidRequestError, _del_obj, msession, perm_obj2 )

    def test_verify_permname( self ) :
        pass

    def test_verify_permname( self ) :
        pass
