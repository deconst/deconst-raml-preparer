#! /usr/bin/env python

import os
import subprocess

def raml2html(file, output_html):
    scripting = '../scripts/ramlconvert.sh'
    htmlifyit = subprocess.call(scripting)
    api_html = open('output_html') # os.getenv('htmlifyit')
    apiraw = str(api_html.read())
    api_html.close()
    return apiraw
