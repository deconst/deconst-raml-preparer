#!/usr/bin/env python

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

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class RAML2HTMLTestCase(unittest.TestCase):
    '''
    Tests for the RAML2HTML method
    '''

    def test_raml2html_is_html(self):
        '''
        Is the output of raml2html actually HTML?
        '''
        test_raml = os.getcwd() + '/tests/tester.raml'
        output_file = os.getcwd() + '/tests/test_is_html.html'
        self.assertIn('<html>', raml2html(test_raml, output_file))


if __name__ == '__main__':
    unittest.main()
