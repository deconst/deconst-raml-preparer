#! /usr/bin/env python3

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
            new_file = open(output_html, 'x')
            new_file.close()
        except FileExistsError:
            pass
        with open(output_html, 'r') as output_file:
            scripting = os.path.join(
                os.getcwd(),
                'ramlpreparer',
                'scripts',
                'ramlconvert.sh'
            )
            nunjucks_path = os.path.join(
                os.getcwd(),
                'ramlpreparer',
                'nunjucks',
                'index.nunjucks'
            )
            htmlifyit = subprocess.call([
                scripting,
                file_raml,
                output_html,
                nunjucks_path
            ])
            apiraw = str(output_file.read())
        return apiraw


# Typical define as needed system
if __name__ == '__main__':
    # BUG: Slice isn't working here. [1:] returns an error.
    raml2html(sys.argv[1], sys.argv[2])
