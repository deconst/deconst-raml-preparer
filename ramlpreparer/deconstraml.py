#! /usr/bin/env python

# Written for Python 3.x by Laura A Santamaria for deconst, an end-to-end
# documentation delivery system.

import sys
import os
import re
import urllib.parse
import requests
#from deconstraml.builder import DeconstJSONBuilder
# from <<<raml builder>>>> import <<<<modules>>>>>

import envelope_writer

# Get the RAML


def enveloper(self, the_raml):
    '''
    Use the RAML2HTML JavaScript library to generate HTML, and then wrap the
    submission in the deconst envelope schema.
    '''
    the_html = envelope_writer.make_it_html(the_raml)
    the_envelope = envelope_writer.parsing_html(the_html)
    return the_envelope


# Sumbit to the submitter
def submit(___):
    '''
    Pass the envelopes to the submitter.
    '''
    pass


# Run me!
if __name__ == "__main__":
    print("This module was called directly.")
    pass
