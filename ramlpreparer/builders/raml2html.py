#! /usr/bin/env python

import os
import sys
import subprocess
from sys import argv


def raml2html(file_raml, output_html):
    '''
    Converts RAML files to HTML using the raml2html JavaScript library. Expects
    two arguments:
    -   the path to a RAML file for input
    -   the path to an HTML file for output. This file does not need to be
        created first as the script will create it as needed.
    '''
    if not file_raml.lower().endswith('.raml'):
        raise TypeError("This isn't RAML! Pass a RAML file to this method.")
    else:
        try:
            output_file = open(output_html, 'r')
        except FileNotFoundError:
            output_file = open(output_html, 'w')  # TODO: Switch to with open()
            output_file.close()
            output_file = open(output_html, 'r')  # TODO: Fix the messiness
        scripting = os.path.join(
            os.getcwd(), 'ramlpreparer', 'scripts', 'ramlconvert.sh')
        nunjucks_path = os.path.join(
            os.getcwd(), 'ramlpreparer', 'nunjucks', 'index.nunjucks')
        htmlifyit = subprocess.call(
            [scripting, file_raml, output_html, nunjucks_path])
        apiraw = str(output_file.read())
        output_file.close()
        return apiraw


# Typical define as needed system
if __name__ == '__main__':
    starter_call = os.path.join(
        os.getcwd(), 'ramlpreparer', 'scripts', 'npminstall.sh')
    subprocess.call(starter_call, shell=True)
    # print(sys.argv[0])
    # print(sys.argv[1])
    # print(sys.argv[2])
    # BUG: Slice isn't working here. [1:] returns an error.
    raml2html(sys.argv[1], sys.argv[2])
