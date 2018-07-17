#!/usr/bin/env python3

'''
test_common
----------------------------------
Tests for `common` module.
'''

import unittest
import subprocess
import sys
import os
import json
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.builders.common import init_builder
from openapipreparer.builders.common import derive_content_id


class CommonTestCase(unittest.TestCase):
    '''
    Tests for the common methods
    '''

    def test_init_builder_pass(self):
        '''
        Does the init_builder method parse a full deconst file correctly?
        '''
        deconst_config = init_builder()
        actual_result = {}
        actual_result['contentIDBase'] = deconst_config.content_id_base
        actual_result['githubUrl'] = deconst_config.github_url
        actual_result['meta'] = deconst_config.meta
        expected_result = {
            "contentIDBase": "https://github.com/deconst/fake-repo/",
            "githubUrl": "https://github.com/deconst/fake-repo/",
            "meta": {
                "github_issues_url": "https://github.com/deconst/fake-repo/issues",
                "someKey": "someValue", "preferGithubIssues": True}}
        self.assertEqual(actual_result, expected_result)

    def test_derive_content_id_pass(self):
        '''
        Does this method get a content id?
        '''
        deconst_path = path.join(os.getcwd(), 'tests', 'src', '_deconst.json')
        with open(deconst_path, 'r') as deconst_file:
            deconst_config = json.load(deconst_file)
        expected_content_id = 'https://github.com/deconst/fake-repo/docname_test'
        actual_content_id = derive_content_id(
            deconst_config, "docname_test", test=True)
        self.assertEqual(actual_content_id, expected_content_id)


if __name__ == '__main__':
    unittest.main()
