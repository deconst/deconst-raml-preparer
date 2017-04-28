#! /usr/bin/env python

import os
import subprocess
# starter_call = '../scripts/npminstall.sh'
# subprocess.call(starter_call)

def raml2html(file_raml, output_html):
    scripting = '../scripts/ramlconvert.sh'
    htmlifyit = subprocess.call([scripting, file_raml, output_html])
    api_html = open(output_html)
    apiraw = str(api_html.read())
    api_html.close()
    return apiraw
