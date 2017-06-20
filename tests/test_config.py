#!/usr/bin/env python3

'''
test_config
----------------------------------
Tests for `config` module.
'''

import unittest
import subprocess
import sys
import os
import json
import io
from unittest import mock
from os import path
from bs4 import BeautifulSoup
from test import support

sys.path.append(path.join(path.dirname(__file__), '..'))

from ramlpreparer.config import _normalize as normalize_it
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

    def test__normalize_pass(self):
        '''
        Does normalize send a good URL with a slash?
        '''
        expected_output = 'https://github.com/'
        actual_output = normalize_it('https://github.com')
        self.assertEqual(expected_output, actual_output)

    def test__normalize_has_slash_pass(self):
        '''
        Does normalize send a good URL with a slash if it already has a slash?
        '''
        expected_output = 'https://github.com/'
        actual_output = normalize_it('https://github.com/')
        self.assertEqual(expected_output, actual_output)

    def test__normalize_not_a_url(self):
        '''
        Does normalize send something as expected when it's not a URL?
        '''
        expected_output = 'random-path/'
        actual_output = normalize_it('random-path')
        self.assertEqual(expected_output, actual_output)

    def test__normalize_not_a_url_with_slash(self):
        '''
        Does normalize send something as expected when it's not a URL but has
        a slash?
        '''
        expected_output = 'random-path/'
        actual_output = normalize_it('random-path/')
        self.assertEqual(expected_output, actual_output)


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

    def test_apply_minimal_file_pass(self):
        '''
        Does the apply_file method correctly parse the deconst json file?
        '''
        deconstjson = path.join(os.getcwd(), 'tests',
                                'src', '_deconst_minimal.json')
        self.config_class.content_id_base = '/random/path/'
        self.config_class.apply_file(deconstjson)
        test_deconst_result = {}
        test_deconst_result['contentIDBase'] = self.config_class.content_id_base
        expected_deconst_result = {}
        expected_deconst_result['contentIDBase'] = '/random/path/'
        self.assertEqual(expected_deconst_result, test_deconst_result)

    def test_apply_minimal_file_check_error_message_pass(self):
        '''
        Does the apply_file method correctly parse the deconst json file?
        '''
        expected_message = ("Using environment variable CONTENT_ID_BASE=" +
                            "[/random/path/] instead of _deconst.json " +
                            "setting [https://github.com/deconst/fake-repo/]" +
                            ".\n")
        deconstjson = path.join(os.getcwd(), 'tests',
                                'src', '_deconst_errorcheck.json')
        self.config_class.content_id_base = '/random/path/'
        with mock.patch('sys.stdout', new_callable=io.StringIO) as object_out:
            self.config_class.apply_file(deconstjson)
            self.assertEqual(expected_message, object_out.getvalue())

    def test__get_git_root_pass(self):
        '''
        Question?
        '''
        actual_git_root = self.config_class._get_git_root()
        expected_git_root = os.getcwd()
        self.assertEqual(actual_git_root, expected_git_root)

    def test_missing_values_pass(self):
        '''
        Does a missing content_id_base raise the correct reason for failure?
        '''
        self.maxDiff = None
        self.config_class.content_id_base = None
        actual_output = self.config_class.missing_values()
        self.assertEqual(
            actual_output, ['CONTENT_ID_BASE is missing. It should be the base URL used to generate IDs for content within this repository.'])


if __name__ == '__main__':
    unittest.main()
