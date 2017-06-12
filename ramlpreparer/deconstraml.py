#! /usr/bin/env python

# Written for Python 3.x by Laura A Santamaria for deconst, an end-to-end
# documentation delivery system.

'''
Use the RAML2HTML JavaScript library to convert .raml files to JSON envelopes
to pass to the deconst submitter module.
'''

import sys
import os
import re
import urllib.parse
import requests
import ramlpreparer.envelope_writer as envelope_writer


def enveloper(self, the_raml):
    '''
    Use the RAML2HTML JavaScript library to generate HTML, and then wrap the
    submission in the deconst envelope schema.
    '''
    the_html = envelope_writer.make_it_html(the_raml)
    the_envelope = envelope_writer.parsing_html(the_html)
    return the_envelope


# Sumbit to the submitter
def submit(self, the_envelope):
    '''
    Pass the envelopes to the submitter.
    '''
    the_json = envelope_writer.make_json(the_envelope)
    # TODO: What's the submission variable?
    final_submit = envelope_writer.write_out(SUBMISSION)


# Run me!
if __name__ == "__main__":
    print("This module was called directly.")
    pass
