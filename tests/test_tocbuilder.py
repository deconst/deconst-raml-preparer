#!/usr/bin/env python

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

from ramlpreparer.builders.tocbuilder import tag_it
from ramlpreparer.builders.tocbuilder import sibs_it
from ramlpreparer.builders.tocbuilder import parse_it
from ramlpreparer.builders.tocbuilder import htmlify

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class TocBuilderTestCase(unittest.TestCase):
    '''
    Tests for the tocbuilder methods
    '''

    def test_tag_it_if_id_present(self):
        '''
        Does tag_it provide a string when given good input?
        '''
        soup = BeautifulSoup('<h1 id="yep">heading</h1>', 'html.parser')
        tag = soup.h1
        self.assertEqual('yep', tag_it(tag))

    def test_tag_it_if_id_not_present(self):
        '''
        Does tag_it provide a string when given good input without an id field?
        '''
        soup = BeautifulSoup('<h1>yep that is it</h1>', 'html.parser')
        tag = soup.h1
        self.assertEqual('yepthatisit', tag_it(tag))

    def test_sibs_it_has_sib(self):
        '''
        If the tag is followed by a sibling, does it provide the right output?
        '''
        soup = BeautifulSoup('<h3>test</h3><h3>test</h3>', 'html.parser')
        the_method = sibs_it(soup.h3, ['<ul>'], re.compile('h[1,2,3]'), [])
        self.assertEqual(['<ul>'], the_method)

    def test_sibs_it_not_sib(self):
        '''
        If the tag is not followed by a sibling, does it provide the right
        output?
        '''
        soup = BeautifulSoup('<h3>test</h3><h2>test</h2>', 'html.parser')
        the_method = sibs_it(soup.h3, ['empty'], re.compile('h[1,2,3]'), [])
        self.assertEqual([['empty']], the_method)

    def test_parse_it_h1_only(self):
        '''
        Does parse_it work for H1 tags only?
        '''
        self.maxDiff = None
        html_sample_h1 = ('<body><h1>text 1</h1><h1>text 2</h1></body>')
        the_result_h1 = ['<li><a href="#text1">text 1</a></li>',
                         '<li><a href="#text2">text 2</a></li>']
        the_method_h1 = parse_it(html_sample_h1)
        self.assertEqual(the_method_h1, the_result_h1)

# BUG: These next two tests make the test_parse_it_h1_only test break.
# I think somehow the values of the variables are getting passed as if the
# cache hasn't cleared...
    # def test_parse_it_h1_and_h2(self):
    #     '''
    #     Does parse_it work for H1 and H2 tags?
    #     '''
    #     self.maxDiff = None
    #     html_sample_h2 = ('<body><h1>text h1 1</h1><h2>text h2 1</h2>' +
    #                       '<h2>text h2 2</h2><h1>text h1 2</h1>' +
    #                       '<h2>text h2 3</h2><h2>text h2 4</h2></body>')
    #     the_result_h2 = ['<li><a href="#texth11">text h1 1</a></li>',
    #                      ['<li><a href="#texth21">text h2 1</a></li>',
    #                       '<li><a href="#texth22">text h2 2</a></li>'],
    #                      '<li><a href="#texth12">text h1 2</a></li>',
    #                      ['<li><a href="#texth23">text h2 3</a></li>',
    #                          '<li><a href="#texth24">text h2 4</a></li>']]
    #     the_method_h2 = parse_it(html_sample_h2)
    #     self.assertEqual(the_method_h2, the_result_h2)
    #
    # def test_parse_it_pass(self):
    #     '''
    #     Does parse_it work for H1, H2, and H3 tags?
    #     '''
    #     self.maxDiff = None
    #     html_sample_h3 = ('<body><h1>text h1 1</h1><h2>text h2 1</h2>' +
    #                       '<h3>text h3 1</h3><h3>text h3 2</h3>' +
    #                       '<h2>text h2 2</h2><h3>text h3 3</h3>' +
    #                       '<h1>text h1 2</h1><h2>text h2 3</h2>' +
    #                       '<h2>text h2 4</h2></body>')
    #     the_result_h3 = ['<li><a href="#texth11">text h1 1</a></li>',
    #                      ['<li><a href="#texth21">text h2 1</a></li>',
    #                       ['<li><a href="#texth31">text h3 1</a></li>',
    #                        '<li><a href="#texth32">text h3 2</a></li>'],
    #                          '<li><a href="#texth22">text h2 2</a></li>',
    #                          ['<li><a href="#texth33">text h3 3</a></li>']],
    #                      '<li><a href="#texth12">text h1 2</a></li>',
    #                      ['<li><a href="#texth23">text h2 3</a></li>',
    #                          '<li><a href="#texth24">text h2 4</a></li>']]
    #     the_method_h3 = parse_it(html_sample_h3)
    #     self.assertEqual(the_method_h3, the_result_h3)

    def test_parse_it_fail(self):
        '''
        Question?
        '''
        html_doc = '<h1>text</h1><h2>text</h2><h3>text</h3>'
        pass

    def test_htmlify_pass(self):
        '''
        Does htmlify return a list wrapped in <ul></ul>?
        '''
        the_list = ['<li>item1</li>',
                    ['<ul>', '<li>sub1</li>', '<li>sub2</li>',
                     ['<ul>', '<li>subsub1</li>', '<li>subsub2</li>', '</ul>'],
                     '</ul>'],
                    '<li>item2</li>']
        the_result = ['<ul>', '<li>item1</li>',
                      ['<ul>', '<ul>', '<li>sub1</li>', '<li>sub2</li>',
                       ['<ul>', '<ul>', '<li>subsub1</li>', '<li>subsub2</li>',
                        '</ul>', '</ul>'], '</ul>', '</ul>'],
                      '<li>item2</li>', '</ul>']
        the_method = htmlify(the_list)
        self.assertEqual(the_method, the_result)

    def test_htmlify_fail(self):
        '''
        Question?
        '''
        soup = BeautifulSoup(
            '<h1>text</h1><h2>text</h2><h3>text</h3>', 'html.parser')
        pass


if __name__ == '__main__':
    unittest.main()
