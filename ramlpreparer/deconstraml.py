#! /usr/bin/env python3

# Written for Python 3.x by Laura A Santamaria for deconst, an end-to-end
# documentation delivery system.

'''
Use the RAML2HTML JavaScript library to convert .raml files to JSON envelopes
to pass to the deconst submitter module.
'''

import sys
import os
import re
import shutil
import urllib.parse
# import requests
from pathlib import Path

sys.path.insert(0, os.getcwd())

import ramlpreparer.builders.envelope_writer as envelope_writer
from ramlpreparer.config import Configuration


config = Configuration(os.environ)

def enveloper(the_raml, the_location):
    '''
    Use the RAML2HTML JavaScript library to generate HTML, and then wrap the
    submission in the deconst envelope schema.
    '''
    the_html = envelope_writer.make_it_html(the_raml, the_location)
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
    Finds and builds all RAML in the directory given in the config files.
    '''
    listed_raml = []
    excluded_filepath = set(['node_modules'])
    # for (dirpath, dirnames, filenames) in os.walk(config.git_root, topdown=True):
    for (dirpath, dirnames, filenames) in os.walk(config.content_root, topdown=True):
        dirnames[:] = [
            dirname for dirname in dirnames if dirname not in excluded_filepath]
        for filename in filenames:
            if filename.endswith('.raml'):
                path_name = os.path.join(dirpath, filename)
                listed_raml.append(path_name)
    return listed_raml
