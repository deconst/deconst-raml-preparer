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

from ramlpreparer.config import _normalize
from ramlpreparer.config import Configuration

# Initialize the raml2html package.
starter_call = path.join(os.getcwd(), 'ramlpreparer',
                         'scripts', 'npminstall.sh')
subprocess.call(starter_call, shell=True)


class ConfigTestCase(unittest.TestCase):
    '''
    Tests for the config method
    '''

    @unittest.skip("feature not ready")
    def test__normalize_pass(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test__normalize_fail(self):
        '''
        Question?
        '''
        pass


class ConfigurationTestCase(unittest.TestCase):
    '''
    Tests for class methods in the Configuration class
    '''

    def setUp(self):
        '''
        Instantiate the class.
        '''
        self.config_class = Configuration()

    def tearDown(self):
        pass

    @unittest.skip("feature not ready")
    def test_apply_file_pass(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_apply_file_fail(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test__get_git_root_pass(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test__get_git_root_fail(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_missing_values_pass(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_missing_values_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
