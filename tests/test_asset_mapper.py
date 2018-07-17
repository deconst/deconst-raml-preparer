#!/usr/bin/env python3

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

from openapipreparer.builders.asset_mapper import map_the_assets


class AssetMapperTestCase(unittest.TestCase):
    '''
    Tests for the asset_mapper methods
    '''

    def test_map_the_assets_asset_offset_pass(self):
        '''
        Does the mapper successfully map the new path?
        '''
        tool_time12_path = path.join(
            os.getcwd(), 'tests', 'dest', 'assets', 'tool_time12.jpg')
        tool_time_path = path.join(
            os.getcwd(), 'tests', 'dest', 'assets', 'tool_time.jpg')
        expected_version = {tool_time12_path: 3980, tool_time_path: 663}
        source_assets = path.join(os.getcwd(), 'tests', 'src', 'assets', '')
        dest_assets = path.join(os.getcwd(), 'tests', 'dest', 'assets', '')
        x, mapped_version = map_the_assets(
            source_assets, dest_assets, html_doc_path='tests/src/tester-raw.html')
        print(expected_version)
        print(mapped_version)
        self.assertEqual(expected_version, mapped_version)


if __name__ == '__main__':
    unittest.main()
