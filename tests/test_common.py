#!/usr/bin/env python

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

# from ramlpreparer.builders.common import name

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class CommonTestCase(unittest.TestCase):
    '''
    Tests for the common methods
    '''

    def test_common1_pass(self):
        '''
        Question?
        '''
        pass

    def test_common1_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
