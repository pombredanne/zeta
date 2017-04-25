#! /usr/bin/env bash

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# Zeta built into .egg package, only binary version
python ./setup.py bdist_egg --exclude-source-files

# There should only on egg file under dist/. Otherwise the following loop
# logic will fail
for f in dist/*; do zetaegg=$f; done

root=`pwd`
dir=/tmp/zeta-`date +%h%H:%m:%S`
tarfile=$zetaegg.tar
mkdir -p $dir

# Copy deployzeta.py, zwiki.egg package and zeta.egg package into a temporary
# directory
cp $f $dir
cp bin/deployzeta.py $dir
for f in ../zwiki/dist/*; do zwikiegg=$f; done
cp $zwikiegg $dir

echo "Tarring 'zeta' egg, 'zwiki' egg and 'deployzeta.py' ... "
cd $dir
tar -cf $root/$tarfile ./
cd -
rm -rf $dir

echo "ok"
