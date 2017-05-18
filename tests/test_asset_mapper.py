#!/usr/bin/env python

'''
test_asset_mapper
----------------------------------
Tests for `asset_mapper` module.
'''

import unittest
import subprocess
import sys
import os
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

# from ramlpreparer.builders.asset_mapper import name

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class AssetMapperTestCase(unittest.TestCase):
    '''
    Tests for the asset_mapper methods
    '''

    def test_assetmapper1_pass(self):
        '''
        Question?
        '''
        pass

    def test_assetmapper1_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
