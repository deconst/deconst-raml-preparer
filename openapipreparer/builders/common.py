#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Modified from the Sphinx preparer's common.py
# DONE: Update with the correct info vs copy-pasta
'''
Some minor set-up stuff
'''

import os
import subprocess
import json
# import glob
from os import path
from pathlib import Path

from openapipreparer.config import Configuration
from openapipreparer import DECONST_FILE


def init_builder(test=False):
    '''
    deconst config initialization
    '''
    # Search the tree with os.walk and an if statement
    path_name = ""
    deconst_config = Configuration(os.environ)
    for (dirpath, dirnames, filenames) in os.walk(deconst_config.git_root):
        for filename in filenames:
            if filename.endswith(DECONST_FILE):
                for dirname in dirnames:
                    actual_path = str(Path(dirname).parents[0])[:-2]
                    path_name = path.join(dirpath, actual_path, filename)
    if path_name!="":
        deconst_config.apply_file(path_name)
    else:
        raise FileNotFoundError("There's no _deconst.json file in this repo at " +
                                str(deconst_config.git_root) + ". Add one!")
        deconst_config = None
    return deconst_config


def derive_content_id(deconst_config, docname, test=False):
    '''
    Consistently generate content IDs from document names.
    '''

    dirname, basename = path.split(docname)
    if basename == 'index':
        content_id_suffix = dirname
    else:
        content_id_suffix = docname

    if test == True:
        content_id = path.join(
            deconst_config['contentIDBase'], content_id_suffix)
    else:
        content_id = path.join(
            deconst_config.content_id_base, content_id_suffix)
    if content_id.endswith('/'):
        content_id = content_id[:-1]

    return content_id