#! /usr/bin/env python3

import os
import sys
import subprocess
from sys import argv

def openapi2html(file_openapi, output_html):
    '''
    Converts OpenAPI files to HTML using the OpenAPI JAR. Expects
    two arguments:
    -   the path to a OpenAPI json file for input
    -   the path to an HTML file for output. This file does not need to be
        created first as the script will create it as needed.
    '''
    script_path = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.dirname(os.path.realpath(script_path))
    ## Note: We do need lot of additional json files. so, make sure that input file name doesn't
    ## start with '_', for our case we are using openapi.json.
    if not file_openapi.lower().endswith('.json'):
        raise TypeError("This isn't json! Pass a JSON file to this method.")
    else:
        try:
            output_html_new_file = os.path.join(output_html, "index.html")
            
            new_file = open(output_html_new_file, 'x')
            new_file.close()
        except FileExistsError:
            pass
        with open(output_html_new_file, 'r') as output_file:
            scripting = os.path.join(
                script_path,
                'scripts',
                'openapiconverter.sh'
            )
            nunjucks_path = os.path.join(
                script_path,
                'nunjucks',
                'index.nunjucks'
            )
            htmlifyit = subprocess.call([
                scripting,
                file_openapi,
                output_html,
                nunjucks_path
            ])
            apiraw = str(output_file.read())
        return apiraw

# Typical define as needed system
if __name__ == '__main__':
    # BUG: Slice isn't working here. [1:] returns an error.
    openapi2html(sys.argv[1], sys.argv[2])
