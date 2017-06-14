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
from test import support

sys.path.append(path.join(path.dirname(__file__), '..'))

from ramlpreparer.config import _normalize
from ramlpreparer.config import Configuration

# Initialize the raml2html package.
starter_call = path.join(os.getcwd(), 'ramlpreparer',
                         'scripts', 'npminstall.sh')
subprocess.call(starter_call, shell=True)

# Identify where the test files live
env_file = path.join(os.getcwd(), 'ramlpreparer', 'tests', 'src', 'env')
deconstjson = path.join(os.getcwd(), 'ramlpreparer',
                        'tests', 'src', '_deconst.json')


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
        self.config_class = Configuration(os.environ)
        return self.config_class

    def tearDown(self):
        self.config_class = None

    def test_apply_file_pass(self):
        '''
        Does the apply_file method correctly parse the deconst json file?
        '''
        deconstjson = path.join(os.getcwd(), 'tests', 'src', '_deconst.json')
        self.config_class.apply_file(deconstjson)
        test_deconst_result = {}
        test_deconst_result['contentIDBase'] = self.config_class.content_id_base
        test_deconst_result['meta'] = self.config_class.meta
        test_deconst_result['githubUrl'] = self.config_class.github_url
        expected_deconst_result = {}
        expected_deconst_result['contentIDBase'] = 'https://github.com/deconst/fake-repo/'
        expected_deconst_result['meta'] = {
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            "someKey": "someValue",
            "preferGithubIssues": True}
        expected_deconst_result['githubUrl'] = 'https://github.com/deconst/fake-repo/'
        self.assertEqual(expected_deconst_result, test_deconst_result)

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
