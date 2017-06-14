#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Modified from the Sphinx preparer's common.py
# TODO: Update with the correct info vs copy-pasta
'''
Some minor set-up stuff
'''

import os
import subprocess
import json
# import glob
from os import path
from pathlib import Path

from ramlpreparer.config import Configuration


def init_builder(test=False):
    '''
    deconst config initialization
    '''
    # Search the tree with os.walk and an if statement
    git_root = subprocess.Popen(
        ['git', 'rev-parse', '--show-toplevel'],
        stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    if test:
        for (dirpath, dirnames, filenames) in os.walk(git_root):
            for filename in filenames:
                if filename.endswith('_deconst.json'):
                    for dirname in dirnames:
                        actual_path = str(Path(dirname).parents[0])[:-2]
                        path_name = path.join(dirpath, actual_path, filename)
        if path_name:
            with open(path_name, 'r') as deconst_file:
                deconst_config = json.load(deconst_file)
        else:
            print("There's no _deconst.json file in this repo at " +
                  str(git_root) + ". Add one!")
            deconst_config = None
    else:
        deconst_config = Configuration(os.environ)
        for (dirpath, dirnames, filenames) in os.walk(git_root):
            for filename in filenames:
                if filename.endswith('_deconst.json'):
                    for dirname in dirnames:
                        actual_path = str(Path(dirname).parents[0])[:-2]
                        path_name = path.join(dirpath, actual_path, filename)
        if path_name:
            with open(path_name, 'r') as deconst_file:
                deconst_config.apply_file(deconst_file)
        else:
            print("There's no _deconst.json file in this repo at " +
                  str(git_root) + ". Add one!")
            deconst_config = None
    return deconst_config


def derive_content_id(deconst_config, docname):
    '''
    Consistently generate content IDs from document names.
    '''

    dirname, basename = path.split(docname)
    if basename == 'index':
        content_id_suffix = dirname
    else:
        content_id_suffix = docname

    content_id = path.join(deconst_config['contentIDBase'], content_id_suffix)
    if content_id.endswith('/'):
        content_id = content_id[:-1]

    return content_id
