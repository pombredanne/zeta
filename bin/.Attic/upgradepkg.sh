#! /usr/bin/env bash

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# DEPRICATED

# Notes :
#   1. Package `zeta` and `zwiki` and re-install their eggs in the deployment
#      directory

# Usage :
#   upgradepkg <zwiki-srcdir> <zeta-srcdir>

echo ""
echo "Packaging ZWiki ... "
cd $1
bin/cleanzwiki.sh
bin/pkg.sh egg
for f in dist/*; do zwikiegg=$f; done
echo "Upgrading ZWiki to $zwikiegg ..."
cd -
cp $1/dist/$zwikiegg .
easy_install -U $zwikiegg
echo "ok"

echo ""
echo "Packaging Zeta ... "
cd $2
bin/cleanzeta.sh
bin/pkgzeta.sh
for f in dist/*; do zetaegg=$f; done
echo "Upgrading Zeta to $zetaegg ..."
cd -
cp $2/dist/$zetaegg .
easy_install -U $zetaegg
echo "ok"
