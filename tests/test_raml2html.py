#!/usr/bin/env python3

'''
test_raml2html
----------------------------------
Tests for `raml2html` module.
'''

import unittest
import subprocess
import sys
import os
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.builders.openapi2html import openapi2html

class OPENAPI2HTMLTestCase(unittest.TestCase):
    '''
    Tests for the OPENAPI2HTML method
    '''

    def test_raml2html_is_html(self):
        '''
        Is the output of openapi2html actually HTML?
        '''
        test_raml = path.join(os.getcwd(), 'tests', 'src', 'openapi.json')
        output_file = path.join(os.getcwd(), 'tests',
                                'dest', 'test_is_html', 'index.html')
        self.assertIn('<html>', openapi2html(test_raml, output_file))

    def test_raml2html_without_raml(self):
        '''
        Does non-RAML input fail?
        '''
        test_not_raml = path.join(os.getcwd(), 'tests', 'src', 'tester.txt')
        output_file = path.join(os.getcwd(), 'tests',
                                'dest', 'test_isnt_html','index.html')
        self.assertRaises(TypeError, openapi2html, [test_not_raml, output_file])


if __name__ == '__main__':
    unittest.main()
