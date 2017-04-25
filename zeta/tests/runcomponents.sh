#! /usr/bin/env bash

nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_attachforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_attach
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_license
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_licforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_permforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_projectforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_project
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_revforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_review
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_systemforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_system
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_tag
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_ticketforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_ticket
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_userforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_vcsforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_vcs
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_vote
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_wikiforms
nosetests -v -s -x --pdb --pdb-failures --with-pylons=../../test.ini components.test_wiki
