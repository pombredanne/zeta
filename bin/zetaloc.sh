#! /usr/bin/env bash

echo -n 'Python     ...'; wc `find ~/dev/zeta/zeta -name "*.py" | grep -v sampledata` |  grep total
echo -n 'templates  ...'; wc `find ~/dev/zeta/zeta/templates-dojo/ -name "*.html"` | grep total
echo -n 'javascript ...'; wc ~/dev/zeta/defenv/public/zhighcharts.js ~/dev/zeta/defenv/public/zdojo/*.js | grep total
echo -n 'zwiki      ...' ; wc `find ~/dev/zwiki/zwiki -name "*.py"` | grep total
