#! /usr/bin/env python

import os
import subprocess

scripting = '../scripts/ramlconvert.sh'
htmlifyit = subprocess.call(scripting)
api_html = open('../../tests/tester-raw.html') # os.getenv('htmlifyit')
apiraw = str(api_html.read())
api_html.close()

print(apiraw)
