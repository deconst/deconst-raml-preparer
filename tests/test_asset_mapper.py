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

from ramlpreparer.builders.asset_mapper import map_the_assets

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class AssetMapperTestCase(unittest.TestCase):
    '''
    Tests for the asset_mapper methods
    '''

    def test_map_the_assets_asset_offset_pass(self):
        '''
        Does the mapper successfully map the new path?
        '''
        expected_version = {os.getcwd() + '/tests/dest/assets/tool_time12.jpg': 3980,
                            os.getcwd() + '/tests/dest/assets/tool_time.jpg': 663}
        source_assets = os.getcwd() + '/tests/src/assets/'
        dest_assets = os.getcwd() + '/tests/dest/assets/'
        x, mapped_version = map_the_assets(
            '/tests/src/tester-raw.html', source_assets, dest_assets)
        self.assertEqual(expected_version, mapped_version)

    def test_map_the_assets_asset_offset_fail(self):
        '''
        Question?
        '''
        pass


if __name__ == '__main__':
    unittest.main()
