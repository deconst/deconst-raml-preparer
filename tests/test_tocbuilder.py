#!/usr/bin/env python3

'''
test_tocbuilder
----------------------------------
Tests for `tocbuilder` module.
'''

import unittest
import subprocess
import sys
import os
import re
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.builders.tocbuilder import tag_it
from openapipreparer.builders.tocbuilder import sibs_it
from openapipreparer.builders.tocbuilder import parse_it
from openapipreparer.builders.tocbuilder import htmlify


class TocBuilderTestCase(unittest.TestCase):
    '''
    Tests for the tocbuilder methods
    '''

    def setUp(self):
        pass

    def tearDown(self):
        soup = None
        tag = None
        html_sample = None
        the_method = None
        the_result = None

    def test_tag_it_if_id_present(self):
        '''
        Does tag_it provide a string when given good input?
        '''
        soup = BeautifulSoup('<h2 id="yep">heading</h2>', 'html.parser')
        tag = soup.h2
        self.assertEqual('yep', tag_it(tag))

    def test_tag_it_if_id_not_present(self):
        '''
        Does tag_it provide a string when given good input without an id field?
        '''
        soup = BeautifulSoup('<h2>yep that is it</h2>', 'html.parser')
        tag = soup.h2
        self.assertEqual('yepthatisit', tag_it(tag))

    def test_sibs_it_has_sib(self):
        '''
        If the tag is followed by a sibling, does it provide the right output?
        '''
        soup = BeautifulSoup('<h4>test</h4><h4>test</h4>', 'html.parser')
        the_method = sibs_it(
            soup.h4, 'h4', ['current_heading_list'], re.compile(
                'h[2,3,4]'), ['toc_builder'])
        self.assertEqual(
            (['toc_builder'], ['current_heading_list'], None, '4'), the_method)

    def test_sibs_h4_followed_by_h3(self):
        '''
        If the h4 tag is followed by an h3 tag, does it provide the right
        output?
        '''
        soup = BeautifulSoup('<h4>test</h4><h3>test</h3>', 'html.parser')
        the_method = sibs_it(
            soup.h4, 'h4', ['current_heading_list'], re.compile(
                'h[2,3,4]'), ['toc_builder'], ['h3 list'])
        self.assertEqual(
            (['toc_builder'], [], ['h3 list', ['current_heading_list']], '3'),
            the_method)

    def test_sibs_h4_followed_by_h2(self):
        '''
        If the h4 tag is followed by an h2 tag, does it provide the right
        output?
        '''
        soup = BeautifulSoup('<h4>test</h4><h2>test</h2>', 'html.parser')
        the_method = sibs_it(
            soup.h4, 'h4', ['current_heading_list'], re.compile(
                'h[2,3,4]'), ['toc_builder'])
        self.assertEqual(
            (['toc_builder', ['current_heading_list']],
             [], None, '2'), the_method)

    def test_parse_it_h2_only(self):
        '''
        Does parse_it work for h2 tags only?
        '''
        self.maxDiff = None
        html_sample = '<body><h2>Heading 1 h2</h2><h2>Heading 2 h2</h2></body>'
        the_result = ['<li><a href="#Heading1h2">Heading 1 h2</a></li>',
                      '<li><a href="#Heading2h2">Heading 2 h2</a></li>']
        the_method = parse_it(html_sample)
        self.assertEqual(the_method, the_result)

# FIXED: These next two tests make the test_parse_it_h2_only test break.

    def test_parse_it_h2_and_h3(self):
        '''
        Does parse_it work for h2 and h3 tags?
        '''
        self.maxDiff = None
        html_sample = (
            '<body><h2>Heading 1 h3</h2><h3>Heading 1.1 h3</h3>'
            '<h3>Heading 1.2 h3</h3><h2>Heading 2 h3</h2>'
            '<h3>Heading 2.1 h3</h3><h3>Heading 2.2 h3</h3></body>')
        # BUG: Need to figure out why the double square bracket appears on the
        # first 2nd level here.
        the_result = ['<li><a href="#Heading1h3">Heading 1 h3</a></li>', [
            ['<li><a href="#Heading1.1h3">Heading 1.1 h3</a></li>',
             '<li><a href="#Heading1.2h3">Heading 1.2 h3</a></li>']],
            '<li><a href="#Heading2h3">Heading 2 h3</a></li>', [
                '<li><a href="#Heading2.1h3">Heading 2.1 h3</a></li>',
                '<li><a href="#Heading2.2h3">Heading 2.2 h3</a></li>']]
        the_method = parse_it(html_sample)
        self.assertEqual(the_method, the_result)

    def test_parse_it_pass(self):
        '''
        Does parse_it work for h2, h3, and h4 tags?
        '''
        self.maxDiff = None
        html_sample = (
            '<body><h2>Heading 1 h4</h2><h3>Heading 1.1 h4</h3>'
            '<h4>Heading 1.1.1 h4</h4><h4>Heading 1.1.2 h4</h4>'
            '<h3>Heading 1.2 h4</h3><h4>Heading 1.2.1 h4</h4>'
            '<h2>Heading 2 h4</h2><h3>Heading 2.1 h4</h3>'
            '<h3>Heading 2.2 h4</h3></body>')
        the_result = ['<li><a href="#Heading1h4">Heading 1 h4</a></li>', [
            '<li><a href="#Heading1.1h4">Heading 1.1 h4</a></li>', [
                '<li><a href="#Heading1.1.1h4">Heading 1.1.1 h4</a></li>',
                '<li><a href="#Heading1.1.2h4">Heading 1.1.2 h4</a></li>'],
            '<li><a href="#Heading1.2h4">Heading 1.2 h4</a></li>', [
                '<li><a href="#Heading1.2.1h4">Heading 1.2.1 h4</a></li>']],
            '<li><a href="#Heading2h4">Heading 2 h4</a></li>', [
                '<li><a href="#Heading2.1h4">Heading 2.1 h4</a></li>',
            '<li><a href="#Heading2.2h4">Heading 2.2 h4</a></li>']]
        the_method = parse_it(html_sample)
        self.assertEqual(the_method, the_result)

    def test_parse_it_full_pass(self):
        '''
        Does parse_it work for a full sample?
        '''
        self.maxDiff = None
        html_sample = (
            '<body><h2>Heading 1 h4</h2><p>Random text</p>'
            '<h3>Heading 1.1 h4</h3><p>Random text</p><p>Random text</p>'
            '<h4>Heading 1.1.1 h4</h4><p>Random text</p><p>Random text</p>'
            '<h4>Heading 1.1.2 h4</h4><p>Random text</p>'
            '<h3>Heading 1.2 h4</h3><p>Random text</p><p>Random text</p>'
            '<h4>Heading 1.2.1 h4</h4><p>Random text</p>'
            '<h2>Heading 2 h4</h2><p>Random text</p><p>Random text</p>'
            '<h3>Heading 2.1 h4</h3><p>Random text</p>'
            '<h3>Heading 2.2 h4</h3><p>Random text</p><p>Random text</p>'
            '<p>Random text</p></body>')
        the_result = ['<li><a href="#Heading1h4">Heading 1 h4</a></li>', [
            '<li><a href="#Heading1.1h4">Heading 1.1 h4</a></li>', [
                '<li><a href="#Heading1.1.1h4">Heading 1.1.1 h4</a></li>',
                '<li><a href="#Heading1.1.2h4">Heading 1.1.2 h4</a></li>'],
            '<li><a href="#Heading1.2h4">Heading 1.2 h4</a></li>', [
                '<li><a href="#Heading1.2.1h4">Heading 1.2.1 h4</a></li>']],
            '<li><a href="#Heading2h4">Heading 2 h4</a></li>', [
                '<li><a href="#Heading2.1h4">Heading 2.1 h4</a></li>',
            '<li><a href="#Heading2.2h4">Heading 2.2 h4</a></li>']]
        the_method = parse_it(html_sample)
        self.assertEqual(the_method, the_result)

    def test_htmlify_pass(self):
        '''
        Does htmlify return a list wrapped in <ul></ul>?
        '''
        the_list = ['<li>item1</li>', [
            '<li>sub1</li>', '<li>sub2</li>',
            ['<li>subsub1</li>', '<li>subsub2</li>']],
            '<li>item2</li>']
        the_result = '<ul><li>item1</li><ul><li>sub1</li><li>sub2</li><ul><li>subsub1</li><li>subsub2</li></ul></ul><li>item2</li></ul>'
        the_method = htmlify(the_list)
        self.assertEqual(the_method, the_result)


if __name__ == '__main__':
    unittest.main()
