# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

rm -rf defenv/public/captcha/*
touch defenv/public/captcha/readme
rm -rf defenv/log/*
touch defenv/log/application.log
rm -rf defenv/data/*
rm -rf `find ./ -name "*.pyc"`;
rm -rf build/
rm -rf dist/
rm -rf zeta.egg-info/
rm -rf `find ./defenv/staticfiles/ -name "*.html"`
