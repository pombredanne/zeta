# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

echo "........................."
paster request development.ini /pasteradmin/upgradedb
echo "........................."
paster request development.ini /pasteradmin/upgradewiki
echo "........................."
paster request development.ini /pasteradmin/upgradeenv
echo "........................."
paster request development.ini /pasteradmin/staticwiki do=push dir=./defenv/staticfiles
echo "........................."
