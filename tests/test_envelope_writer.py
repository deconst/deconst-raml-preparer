#!/usr/bin/env python

'''
test_envelope_writer
----------------------------------
Tests for `envelope_writer` module.
'''

import unittest
import subprocess
import sys
import os
import json
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

from ramlpreparer.builders.envelope_writer import make_it_html
from ramlpreparer.builders.envelope_writer import parsing_html
from ramlpreparer.builders.envelope_writer import make_json
from ramlpreparer.builders.envelope_writer import write_out
from ramlpreparer.builders.envelope_writer import Envelope_RAML

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class EnvelopeWriterTestCase(unittest.TestCase):
    '''
    Tests for the envelope_writer methods
    '''

    def test_make_it_html_pass(self):
        '''
        Question?
        '''
        pass

    def test_make_it_html_fail(self):
        '''
        Question?
        '''
        pass

    def test_parsing_html_pass(self):
        '''
        Question?
        '''
        pass

    def test_parsing_html_fail(self):
        '''
        Question?
        '''
        pass

    def test_make_json_pass(self):
        '''
        Question?
        '''
        pass

    def test_make_json_fail(self):
        '''
        Question?
        '''
        pass

    def test_write_out_pass(self):
        '''
        Question?
        '''
        pass

    def test_write_out_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
