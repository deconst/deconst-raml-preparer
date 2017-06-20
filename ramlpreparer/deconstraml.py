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
import requests
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


# Sumbit to the submitter
def submit(the_envelope):
    '''
    Pass the envelopes to the submitter.
    '''
    # DONE: What's the submission variable?
    final_base = str(the_envelope['content_id']) + '.json'
    submission = os.path.join(config.envelope_dir, final_base)
    final_submit = envelope_writer.write_out(
        the_envelope, file_path=submission)
    return submission


# Run me!
if __name__ == "__main__":
    temp_base = str(the_envelope['content_id']) + '.html'
    base_location = os.path.join(config.envelope_dir, 'temp', temp_base)
    for (dirpath, dirnames, filenames) in os.walk(config.git_root):
        for filename in filenames:
            if filename.endswith('.raml'):
                for dirname in dirnames:
                    actual_path = str(Path(dirname).parents[0])[:-2]
                    path_name = path.join(dirpath, actual_path, filename)
                    each_envelope = enveloper(path_name, base_location)
                    submit(each_envelope)
    shutil.rmtree(os.chdir(os.path.join(config.envelope_dir, 'temp', '')))
