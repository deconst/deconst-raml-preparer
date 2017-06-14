#!/usr/bin/env python3

'''
test_common
----------------------------------
Tests for `xommon` module.
'''

import unittest
import subprocess
import sys
import os
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

from ramlpreparer.builders.common import init_builder
from ramlpreparer.builders.common import derive_content_id

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class CommonTestCase(unittest.TestCase):
    '''
    Tests for the common methods
    '''

    # @unittest.skip("feature not ready")
    def test_init_builder_pass(self):
        '''
        Does the init_builder method parse a full deconst file correctly?
        '''
        actual_result = init_builder(test=True)
        expected_result = {
            "contentIDBase": "https://github.com/deconst/fake-repo/",
            "githubUrl": "https://github.com/deconst/fake-repo/",
            "meta": {"someKey": "someValue", "preferGithubIssues": True}}
        self.assertEqual(actual_result, expected_result)

    @unittest.skip("feature not ready")
    def test_common1_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
