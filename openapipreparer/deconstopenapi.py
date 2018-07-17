#! /usr/bin/env python3

# Modified from deconst-raml-prepare for deconst by Madhusudan Sridharan, an end-to-end
# documentation delivery system.

'''
Use the openapi-generator-cli-3.1.1.jar file to convert openapi.json files to JSON envelopes
to pass to the deconst submitter module.
'''

import sys
import os
import re
import shutil
import urllib.parse
from pathlib import Path

sys.path.insert(0, os.getcwd())

import openapipreparer.builders.envelope_writer as envelope_writer
from openapipreparer.config import Configuration


config = Configuration(os.environ)

def enveloper(the_json, the_location):
    '''
    Use the openapi-generator-cli-3.1.1.jar file to generate HTML, and then wrap the
    submission in the deconst envelope schema.
    '''
    the_html = envelope_writer.make_it_html(the_json, the_location)
    the_envelope = envelope_writer.parsing_html(the_html)
    return the_envelope


def submit(the_envelope):
    '''
    Pass the envelopes to the submitter.
    '''
    final_base = str(the_envelope['content_id']) + '.json'
    submission = os.path.join(config.envelope_dir, final_base)
    final_submit = envelope_writer.write_out(
        the_envelope, file_path=submission)
    return submission


def find_all(config):
    '''
    Finds and builds JSON in the directory given in the config files.
    '''
    ## TODO: Since This function does os walk and tries finding the json file, for our scenario we
    ## need openapi.json file to be present unlike the .raml file requirement. so, for the time
    ## being the filename.endswith('openapi.json') constrain is places. should talk to laura and
    ## come up with a concrete solution.
    ## questions to ask: The config checks if the input path is an github repo, since this file is
    ## generated seperately in local, will it be fine?
    ## if not what to do ?
    listed_json = []
    excluded_filepath = set(['node_modules'])
    for (dirpath, dirnames, filenames) in os.walk(config.content_root, topdown=True):
        dirnames[:] = [
            dirname for dirname in dirnames if dirname not in excluded_filepath]
        for filename in filenames:
            if filename == 'openapi.json':
                path_name = os.path.join(dirpath, filename)
                listed_json.append(path_name)
    return listed_json