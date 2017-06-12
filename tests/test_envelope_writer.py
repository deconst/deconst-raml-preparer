#!/usr/bin/env python3

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
starter_call = path.join(os.getcwd(), 'ramlpreparer',
                         'scripts', 'npminstall.sh')
subprocess.call(starter_call, shell=True)


class EnvelopeWriterTestCase(unittest.TestCase):
    '''
    Tests for the envelope_writer methods
    '''

    def test_make_it_html_pass(self):
        '''
        Question?
        '''
        test_case_1 = make_it_html(
            './src/small_test.raml', './dest/test_case_1.html')
        pass
        # self.assertEqual()

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


class Envelope_RAMLTestCase(unittest.TestCase):
    '''
    Tests for class methods in the Envelope_RAML class
    '''

    def setUp(self):
        '''
        Instantiate the class.
        '''
        self.envelope = Envelope_RAML('<body><p>testing</p></body>')

    def tearDown(self):
        pass

    def test_serialization_path_pass(self):
        '''
        Question?
        '''
        pass

    def test_serialization_path_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_meta_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_meta_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_git_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_git_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_unsearchable_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_unsearchable_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_layout_key_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_layout_key_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_categories_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_categories_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_asset_offsets_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_asset_offsets_fail(self):
        '''
        Question?
        '''
        pass

    def test_populate_content_id_pass(self):
        '''
        Question?
        '''
        pass

    def test_populate_content_id_fail(self):
        '''
        Question?
        '''
        pass

    def test_override_title_pass(self):
        '''
        Question?
        '''
        pass

    def test_override_title_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
