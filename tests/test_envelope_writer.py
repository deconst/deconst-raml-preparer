# !/usr/bin/env python3

'''
test_envelope_writer
----------------------------------
Tests for `envelope_writer` module.
'''

import unittest
import subprocess
import sys
import os
import json
import filecmp
from os import path
from bs4 import BeautifulSoup
from unittest import mock

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.builders.envelope_writer import make_it_html
from openapipreparer.builders.envelope_writer import parsing_html
from openapipreparer.builders.envelope_writer import write_out
from openapipreparer.builders.envelope_writer import Envelope_OPENAPI


class EnvelopeWriterTestCase(unittest.TestCase):
    '''
    Tests for the envelope_writer methods
    '''

    def test_make_it_html_pass(self):
        '''
        Does the method post to the correct file?
        '''
        raml_location = path.join(
            os.getcwd(), 'tests', 'src', 'small_test.raml')
        html_location = path.join(
            os.getcwd(), 'tests', 'dest', 'test_make_it.html')
        expected_html_file = path.join(
            os.getcwd(), 'tests', 'src', 'tested_html.html')
        test_case_1 = make_it_html(raml_location, html_location)
        self.assertTrue(filecmp.cmp(html_location, expected_html_file),
                        'These two files are not equal.')

    def test_parsing_html_pass(self):
        '''
        Question?
        '''
        self.maxDiff = None
        the_html = path.join(os.getcwd(), 'tests', 'src', 'tested_html.html')
        parsed_html = parsing_html(the_html, page_title='fake_title')
        expected_result = {
            "body": '<div class="container"><div class="row"><div class="col-md-9" role="main"><div class="page-header"><h1 id="topTitle">Instagram API Sample RAML File API documentation version v1</h1><p>https://api.instagram.com/{version}</p><p>A sample RAML spec using Instagram\'s API</p><ul><li><strong>version</strong>: <em>required (v1)</em></li></ul><h2 id="test_chapter"><a href="#test_chapter">test chapter</a></h2><p>Nothing here.</p><h2 id="authentication"><a href="#authentication">Authentication</a></h2><p>testing documentation</p></div><div><div><h2 id="p__shortcode__media">/p/{shortcode}/media</h2></div><div><div><div><div><h4><a href="#panel_p__shortcode__media"><span class="parent"></span>/p/{shortcode}/media</a> <span class="methods"><a href="#p__shortcode__media_get"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span></a></span></h4></div><div id="panel_p__shortcode__media"><div><div class="list-group"><div class="list-group-item"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span><div class="method_description"><p>Given a short link, issues a redirect to that media\'s JPG file.</p></div><div class="clearfix"></div></div></div></div></div><div id="p__shortcode__media_get"><div><div><div><h4 id="myModalLabel"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span> <span class="parent"></span>/p/{shortcode}/media</h4></div><div><div class="alert alert-info"><p>Given a short link, issues a redirect to that media\'s JPG file.</p></div><div class="alert alert-warning"><span class="glyphicon glyphicon-lock" title="Authentication required"></span> Secured by <b></b></div><ul><li><a data-toggle="tab" href="#p__shortcode__media_get_request">Request</a></li><li><a href="#p__shortcode__media_get_response">Response</a></li><li><a href="#p__shortcode__media_get_securedby">Security</a></li></ul><div><div id="p__shortcode__media_get_request"><h3>URI Parameters</h3><ul><li><strong>shortcode</strong>: <em>required (string)</em></li></ul><h3>Query Parameters</h3><ul><li><strong>size</strong>: <em>required (one of t,, m,, l - default: m)</em></li></ul></div><div id="p__shortcode__media_get_response"><h2>HTTP status code 302</h2><h3>Body</h3><p><strong>Media type</strong>: text/html</p><p><strong>Type</strong>: object</p><p><strong>Example</strong>:</p><div class="examples"><pre><code>HTTP/1.1 302 FOUND\nLocation: http://distillery.s3.amazonaws.com/media/2010/10/02/7e4051fdcf1d45ab9bc1fba2582c0c6b_6.jpg\n</code></pre></div></div><div id="p__shortcode__media_get_securedby"><h2>Secured by</h2></div></div></div></div></div></div></div></div></div></div></div></div></div>',
            "docname": str(the_html),
            "title": "fake_title",
            "toc": '<ul><li><a href="#test_chapter">test chapter</a></li><li><a href="#authentication">Authentication</a></li><li><a href="#p__shortcode__media">/p/{shortcode}/media</a></li><ul><li><a href="#p__shortcode__media-get-">/p/{shortcode}/media get </a></li></ul><ul><li><a href="#myModalLabel">get  /p/{shortcode}/media</a></li></ul><ul><li><a href="#URIParameters">URI Parameters</a></li><li><a href="#QueryParameters">Query Parameters</a></li></ul><li><a href="#HTTPstatuscode302">HTTP status code 302</a></li><ul><li><a href="#Body">Body</a></li></ul><li><a href="#Securedby">Secured by</a></li></ul>',
            'unsearchable': None,
            'content_id': str(the_html),
            'meta': {'github_edit_url': 'https://github.com/deconst/fake-repo/edit/master/tests/src/tested_html.html',
                     'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
                     'preferGithubIssues': True,
                     'someKey': 'someValue'},
            'asset_offsets': {},
            'addenda': None,
            'per_page_meta': {}}
        self.assertEqual(parsed_html, expected_result)

    def test_write_out_pass(self):
        '''
        Does the file write out properly?
        '''
        self.maxDiff = None
        the_envelope_passed = {
            "body": '<div class="container"><div class="row"><div class="col-md-9" role="main"><div class="page-header"><h1 id="topTitle">Instagram API Sample RAML File API documentation version v1</h1><p>https://api.instagram.com/{version}</p><p>A sample RAML spec using Instagram\'s API</p><ul><li><strong>version</strong>: <em>required (v1)</em></li></ul><h2 id="test_chapter"><a href="#test_chapter">test chapter</a></h2><p>Nothing here.</p><h2 id="authentication"><a href="#authentication">Authentication</a></h2><p>testing documentation</p></div><div><div><h2 id="p__shortcode__media">/p/{shortcode}/media</h2></div><div><div><div><div><h4><a href="#panel_p__shortcode__media"><span class="parent"></span>/p/{shortcode}/media</a> <span class="methods"><a href="#p__shortcode__media_get"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span></a></span></h4></div><div id="panel_p__shortcode__media"><div><div class="list-group"><div class="list-group-item"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span><div class="method_description"><p>Given a short link, issues a redirect to that media\'s JPG file.</p></div><div class="clearfix"></div></div></div></div></div><div id="p__shortcode__media_get"><div><div><div><h4 id="myModalLabel"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span> <span class="parent"></span>/p/{shortcode}/media</h4></div><div><div class="alert alert-info"><p>Given a short link, issues a redirect to that media\'s JPG file.</p></div><div class="alert alert-warning"><span class="glyphicon glyphicon-lock" title="Authentication required"></span> Secured by <b></b></div><ul><li><a data-toggle="tab" href="#p__shortcode__media_get_request">Request</a></li><li><a href="#p__shortcode__media_get_response">Response</a></li><li><a href="#p__shortcode__media_get_securedby">Security</a></li></ul><div><div id="p__shortcode__media_get_request"><h3>URI Parameters</h3><ul><li><strong>shortcode</strong>: <em>required (string)</em></li></ul><h3>Query Parameters</h3><ul><li><strong>size</strong>: <em>required (one of t,, m,, l - default: m)</em></li></ul></div><div id="p__shortcode__media_get_response"><h2>HTTP status code 302</h2><h3>Body</h3><p><strong>Media type</strong>: text/html</p><p><strong>Type</strong>: object</p><p><strong>Example</strong>:</p><div class="examples"><pre><code>HTTP/1.1 302 FOUND\nLocation: http://distillery.s3.amazonaws.com/media/2010/10/02/7e4051fdcf1d45ab9bc1fba2582c0c6b_6.jpg\n</code></pre></div></div><div id="p__shortcode__media_get_securedby"><h2>Secured by</h2></div></div></div></div></div></div></div></div></div></div></div></div></div>',
            "docname": 'fake_docname',
            "title": "fake_title",
            "toc": '<ul><li><a href="#test_chapter">test chapter</a></li><li><a href="#authentication">Authentication</a></li><li><a href="#p__shortcode__media">/p/{shortcode}/media</a></li><ul><li><a href="#p__shortcode__media-get-">/p/{shortcode}/media get </a></li></ul><ul><li><a href="#myModalLabel">get  /p/{shortcode}/media</a></li></ul><ul><li><a href="#URIParameters">URI Parameters</a></li><li><a href="#QueryParameters">Query Parameters</a></li></ul><li><a href="#HTTPstatuscode302">HTTP status code 302</a></li><ul><li><a href="#Body">Body</a></li></ul><li><a href="#Securedby">Secured by</a></li></ul>',
            'unsearchable': "None",
            'content_id': 'fake_content_id',
            'meta': {'github_edit_url': 'https://github.com/deconst/fake-repo/edit/master/tests/src/test_html.html',
                     'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
                     'preferGithubIssues': "True",
                     'someKey': 'someValue'},
            'asset_offsets': {},
            'addenda': "None",
            'per_page_meta': {}}
        dest_path = os.path.join(os.getcwd(), 'tests',
                                 'dest', 'output_file.json')
        write_out(the_envelope_passed, file_path=dest_path)
        with open(dest_path, 'r') as written_file:
            actual_file = json.load(written_file)
        fake_json_envelope = os.path.join(
            os.getcwd(), 'tests', 'src', 'input_file_writeout.json')
        with open(fake_json_envelope, 'r') as fake_envelope:
            expected_json_output = json.load(fake_envelope)
        self.assertEqual(actual_file, expected_json_output)


class Envelope_RAMLTestCase(unittest.TestCase):
    '''
    Tests for class methods in the Envelope_RAML class
    '''

    def setUp(self):
        '''
        Instantiate the class.
        '''
        fake_deconst = {}
        fake_deconst['contentIDBase'] = 'https://github.com/deconst/fake-repo/'
        fake_deconst['meta'] = {
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            "someKey": "someValue",
            "preferGithubIssues": True}
        fake_deconst['github_url'] = 'https://github.com/deconst/fake-repo/'
        fake_deconst['envelope_dir'] = 'fake_envelope_dir'
        fake_deconst['git_root'] = os.getcwd()
        fake_deconst['github_branch'] = 'master'
        fake_deconst['originalAssetDir'] = os.path.join(
            os.getcwd(), 'tests', 'src', 'assets', '')
        original_file = os.path.join(
            os.getcwd(), 'tests', 'src', 'asset_test_html.html')
        self.envelope = Envelope_OPENAPI('openapi.json',
                                      '<body><p>testing</p></body>',
                                      originalFile=original_file,
                                      title='test_title',
                                      toc='<ul><li>test1</li><li>test2</li></ul>',
                                      publish_date='test_date',
                                      unsearchable='derp',
                                      content_id='https://github.com/deconst/fake-repo/test.raml',
                                      meta=fake_deconst['meta'],
                                      asset_offsets='random',
                                      addenda='derpderp',
                                      deconst_config=fake_deconst,
                                      per_page_meta={'randomkey': 'random'},
                                      github_edit_url=fake_deconst['github_url'])
        return self.envelope

    def tearDown(self):
        self.envelope = None

    def test_serialization_path_pass(self):
        '''
        Does the correct serialization path appear from this class method?
        '''
        expected_serialization_path = 'fake_envelope_dir/https%3A%2F%2Fgithub.com%2Fdeconst%2Ffake-repo%2Ftest.raml.json'
        actual_serialization_path = self.envelope.serialization_path()
        self.assertEqual(expected_serialization_path,
                         actual_serialization_path)

    def test__populate_meta_pass(self, testing=True):
        '''
        Does the class method pass the metadata to each per page metadata key?
        '''
        expected_meta_result = {
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            "someKey": "someValue",
            "preferGithubIssues": True,
            'randomkey': 'random'}
        self.envelope._populate_meta(test=testing)
        actual_meta_result = self.envelope.meta
        self.assertEqual(expected_meta_result, actual_meta_result)

    def test__populate_git_pass(self, testing=True):
        '''
        Does the class method pass the correct git url result?
        '''
        expected_git_path = 'https://github.com/deconst/fake-repo/edit/master/tests/src/small_test.raml'
        self.envelope._populate_git(test=testing)
        actual_git_path = self.envelope.meta['github_edit_url']
        self.assertEqual(expected_git_path, actual_git_path)

    def test__populate_content_id_pass(self):
        '''
        Does the content_id populate correctly?
        '''
        expected_content_id = 'https://github.com/deconst/fake-repo/small_test.raml'
        self.envelope._populate_content_id(testing=True)
        actual_content_id = self.envelope.content_id
        self.assertEqual(expected_content_id, actual_content_id)


class Envelope_RAML_deconstjsonTestCase(unittest.TestCase):
    '''
    Tests explicitly for the deconst.json populate method in Envelope_RAML
    '''

    def setUp(self):
        '''
        Instantiate the class.
        '''
        original_file = os.path.join(
            os.getcwd(), 'tests', 'src', 'asset_test_html.html')
        self.envelope = Envelope_RAML('small_test.raml',
                                      '<body><p>testing</p></body>',
                                      originalFile=original_file,
                                      title='test_title',
                                      toc='<ul><li>test1</li><li>test2</li></ul>',
                                      publish_date='test_date',
                                      unsearchable='derp',
                                      content_id='https://github.com/deconst/fake-repo/test.raml',
                                      meta='meta',
                                      asset_offsets='random',
                                      addenda='derpderp',
                                      per_page_meta={'randomkey': 'random'},
                                      github_edit_url='github_url')
        return self.envelope

    def tearDown(self):
        self.envelope = None

    def test__populate_deconst_config_pass(self):
        '''
        Question?
        '''
        expected_deconst_result = {
            "contentIDBase": "https://github.com/deconst/fake-repo/",
            "githubUrl": "https://github.com/deconst/fake-repo/",
            "meta": {
                "github_issues_url": "https://github.com/deconst/fake-repo/issues",
                "someKey": "someValue", "preferGithubIssues": True}}
        self.envelope._populate_deconst_config()
        actual_deconst_result = {}
        actual_deconst_result['contentIDBase'] = self.envelope.deconst_config.content_id_base
        actual_deconst_result['githubUrl'] = self.envelope.deconst_config.github_url
        actual_deconst_result['meta'] = self.envelope.deconst_config.meta
        self.assertEqual(expected_deconst_result, actual_deconst_result)

    @mock.patch.dict('os.environ', {
        'ASSET_DIR': os.path.join(os.getcwd(), 'tests', 'dest', 'assets', '')})
    def test__populate_asset_offsets_pass(self):
        '''
        Do the assets populate correctly?
        '''
        self.maxDiff = None
        expected_body_result = (
            '<p><img alt="test image" src="0"/></p><p><img alt="test image" src="1"/></p>')
        expected_asset_map = {
            os.path.join(os.getcwd(), 'tests', 'dest', 'assets', 'tool_time.jpg'): 58,
            os.path.join(os.getcwd(), 'tests', 'dest', 'assets', 'tool_time12.jpg'): 108}
        self.envelope._populate_asset_offsets(
            original_asset_dir=os.path.join(os.getcwd(), 'tests', 'src', 'assets', ''))
        actual_body_result = self.envelope.body
        actual_asset_map = self.envelope.asset_offsets
        self.assertEqual([expected_body_result, expected_asset_map], [
                         actual_body_result, actual_asset_map])


if __name__ == '__main__':
    unittest.main()
