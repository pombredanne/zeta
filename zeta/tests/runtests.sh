# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_analytics
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_cache
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_datefmt
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_gviz
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_helpers
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_mailclient
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_pms
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_vcs
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_view
nosetests -v -s -x --with-pylon=../../test.ini zetalib.test_ztext

nosetests -v -s -x --with-pylon=../../test.ini zetacore.test_core
nosetests -v -s -x --with-pylon=../../test.ini zetacore.test_perm
nosetests -v -s -x --with-pylon=../../test.ini zetacore.test_user

nosetests -v -s -x --with-pylon=../../test.ini components.test_attachforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_attach
nosetests -v -s -x --with-pylon=../../test.ini components.test_license
nosetests -v -s -x --with-pylon=../../test.ini components.test_licforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_permforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_projectforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_project
nosetests -v -s -x --with-pylon=../../test.ini components.test_revforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_review
nosetests -v -s -x --with-pylon=../../test.ini components.test_systemforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_system
nosetests -v -s -x --with-pylon=../../test.ini components.test_tag
nosetests -v -s -x --with-pylon=../../test.ini components.test_ticketforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_ticket
nosetests -v -s -x --with-pylon=../../test.ini components.test_userforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_vcsforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_vcs
nosetests -v -s -x --with-pylon=../../test.ini components.test_vote
nosetests -v -s -x --with-pylon=../../test.ini components.test_wikiforms
nosetests -v -s -x --with-pylon=../../test.ini components.test_wiki
nosetests -v -s -x --with-pylon=../../test.ini components.test_xinterface
nosetests -v -s -x --with-pylon=../../test.ini components.test_xsearch
nosetests -v -s -x --with-pylon=../../test.ini components.test_zmail
