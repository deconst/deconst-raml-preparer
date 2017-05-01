#! /usr/bin/env python

import os
import subprocess
from sys import argv
# starter_call = '../scripts/npminstall.sh'
# subprocess.call(starter_call)

def raml2html(file_raml, output_html):
    '''
    Converts RAML files to HTML using the raml2html JavaScript library. Expects
    two arguments:
    -   the path to a RAML file for input
    -   the path to an HTML file for output. This file does not need to be
        created first as the script will create it as needed.
    '''
    # file_raml, output_html = argv
    try:
        output_file = open(output_html, 'r')
    except FileNotFoundError:
        output_file = open(output_html, 'w')
    scripting = '../scripts/ramlconvert.sh'
    htmlifyit = subprocess.call([scripting, file_raml, output_html])
    api_html = open(output_html)
    apiraw = str(api_html.read())
    api_html.close()
    return apiraw

# Typical define as needed system
if __name__ == '__main__':
    import sys
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    raml2html(sys.argv[1],sys.argv[2])
