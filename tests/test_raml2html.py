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

from ramlpreparer.builders.raml2html import raml2html


class RAML2HTMLTestCase(unittest.TestCase):
    '''
    Tests for the RAML2HTML method
    '''

    def test_raml2html_is_html(self):
        '''
        Is the output of raml2html actually HTML?
        '''
        test_raml = path.join(os.getcwd(), 'tests', 'src', 'small_test.raml')
        output_file = path.join(os.getcwd(), 'tests',
                                'dest', 'test_is_html.html')
        self.assertIn('<html>', raml2html(test_raml, output_file))

    def test_raml2html_without_raml(self):
        '''
        Does non-RAML input fail?
        '''
        test_not_raml = path.join(os.getcwd(), 'tests', 'src', 'tester.txt')
        output_file = path.join(os.getcwd(), 'tests',
                                'dest', 'test_isnt_html.html')
        self.assertRaises(TypeError, raml2html, [test_not_raml, output_file])


if __name__ == '__main__':
    unittest.main()
