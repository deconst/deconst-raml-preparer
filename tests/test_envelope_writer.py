#!/usr/bin/env python3

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

from ramlpreparer.builders.envelope_writer import make_it_html
from ramlpreparer.builders.envelope_writer import parsing_html
from ramlpreparer.builders.envelope_writer import make_json
from ramlpreparer.builders.envelope_writer import write_out
from ramlpreparer.builders.envelope_writer import Envelope_RAML

# Initialize the raml2html package.
starter_call = path.join(os.getcwd(), 'ramlpreparer',
                         'scripts', 'npminstall.sh')
subprocess.call(starter_call, shell=True)


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
            os.getcwd(), 'tests', 'src', 'test_html.html')
        test_case_1 = make_it_html(raml_location, html_location)
        self.assertTrue(filecmp.cmp(html_location, expected_html_file),
                        'These two files are not equal.')

    @unittest.skip("no clue how to fail this one")
    def test_make_it_html_fail(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    @mock.patch.dict('os.environ', {'CONTENT_ROOT': 'test-root',
                                    'CONTENT_ID_BASE': 'test-base',
                                    'ENVELOPE_DIR': 'test-envelope',
                                    'ASSET_DIR': 'test-asset',
                                    'git_root': 'test-root'})
    def test_parsing_html_pass(self):
        '''
        Question?
        '''
        the_html = path.join(os.getcwd(), 'tests', 'src', 'test_html.html')
        parsed_html = parsing_html(the_html, page_title='fake_title')
        expected_result = {
            body: '<div class="container"><div class="row"><div class="col-m' +
            'd-9" role="main"><div class="page-header"><h1 id="topTitle">Ins' +
            'tagram API Sample RAML File API documentationversion v1</h1><p>' +
            'https://api.instagram.com/{version}</p><p>A sample RAML spec us' +
            'ing Instagram\'s API</p><ul><li><strong>version</strong>: <em>r' +
            'equired (v1)</em></li></ul><h2 id="test_chapter"><a href="#test' +
            '_chapter">test chapter</a></h2><p>Nothing here.</p><h2 id="auth' +
            'entication"><a href="#authentication">Authentication</a></h2><p' +
            '>testing documentation</p></div><div><div><h2 id="p__shortcode_' +
            '_media">/p/{shortcode}/media</h2></div><div><div><div><div><h4>' +
            '<a href="#panel_p__shortcode__media"><span class="parent"></spa' +
            'n>/p/{shortcode}/media</a> <span class="methods"><a href="#p__s' +
            'hortcode__media_get"><span class="badge badge_get">get <span cl' +
            'ass="glyphicon glyphicon-lock" title="Authentication required">' +
            '</span></span></a></span></h4></div><div id="panel_p__shortcode' +
            '__media"><div><div class="list-group"><div class="list-group-it' +
            'em"><span class="badge badge_get">get <span class="glyphicon gl' +
            'yphicon-lock" title="Authentication required"></span></span><di' +
            'v class="method_description"><p>Given a short link, issues a re' +
            'direct to that media&#39;s JPG file.</p></div><div class="clear' +
            'fix"></div></div></div></div></div><div id="p__shortcode__media' +
            '_get"><div><div><div><h4 id="myModalLabel"><span class="badge b' +
            'adge_get">get <span class="glyphicon glyphicon-lock" title="Aut' +
            'hentication required"></span></span> <span class="parent"></spa' +
            'n>/p/{shortcode}/media</h4></div><div><div class="alert alert-i' +
            'nfo"><p>Given a short link, issues a redirect to that media&#39' +
            ';s JPG file.</p></div><div class="alert alert-warning"><span cl' +
            'ass="glyphicon glyphicon-lock" title="Authentication required">' +
            '</span> Secured by <b></b></div><ul><li><a href="#p__shortcode_' +
            '_media_get_request" data-toggle="tab">Request</a></li><li><a hr' +
            'ef="#p__shortcode__media_get_response">Response</a></li><li><a ' +
            'href="#p__shortcode__media_get_securedby">Security</a></li></ul' +
            '><div><div id="p__shortcode__media_get_request"><h3>URI Paramet' +
            'ers</h3><ul><li><strong>shortcode</strong>: <em>required (strin' +
            'g)</em></li></ul><h3>Query Parameters</h3><ul><li><strong>size<' +
            '/strong>: <em>required (one of t,, m,, l - default: m)</em></li' +
            '></ul></div><div id="p__shortcode__media_get_response"><h2>HTTP' +
            ' status code 302</h2><h3>Body</h3><p><strong>Media type</strong' +
            '>: text/html</p><p><strong>Type</strong>: object</p><p><strong>' +
            'Example</strong>:</p><div class="examples"><pre><code>HTTP/1.1 ' +
            '302 FOUND Location: http://distillery.s3.amazonaws.com/media/20' +
            '10/10/02/7e4051fdcf1d45ab9bc1fba2582c0c6b_6.jpg</code></pre></d' +
            'iv></div><div id="p__shortcode__media_get_securedby"><h1>Secure' +
            'd by</h1></div></div></div></div></div></div></div></div></div>' +
            '</div></div></div></div>',
            title: "Instagram API Sample RAML File API documentation",
            toc: '<ul><li><a href="#InstagramAPISampleRAMLFileAPIdocumentati' +
                 'onversionv1">Instagram API Sample RAML File API documentat' +
                 'ion version v1</a><ul><li><a href="#test_chapter">test cha' +
                 'pter</a></li><li><a href="#authentication">Authentication<' +
                 '/a></li><li><a href="#/p/{shortcode}/media">/p/{shortcode}' +
                 '/media</a><ul><li><a href="#/p/{shortcode}/mediaget">/p/{s' +
                 'hortcode}/media get</a></li><li><a href="#get/p/{shortcode' +
                 '}/media">get/p/{shortcode}/media</a></li></ul><ul><li><a h' +
                 'ref="#URIParameters">URI Parameters</a></li><li><a href="#' +
                 'QueryParameters">Query Parameters</a></li></ul></li><li><a' +
                 ' href="#HTTPstatuscode302">HTTP status code 302</a><ul><li' +
                 '><a href="#Body">Body</a></li></ul></li></ul></li><li><a h' +
                 'ref="#Securedby">Secured by</a></li></ul>'}
        self.assertEqual(parsed_html, expected_result)

    @unittest.skip("feature not ready")
    def test_parsing_html_fail(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_make_json_pass(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_make_json_fail(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_write_out_pass(self):
        '''
        Question?
        '''
        pass

    @unittest.skip("feature not ready")
    def test_write_out_fail(self):
        '''
        Question?
        '''
        pass


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
        fake_deconst['githubUrl'] = 'https://github.com/deconst/fake-repo/'
        fake_deconst['envelope_dir'] = 'fake_envelope_dir'
        self.envelope = Envelope_RAML('<body><p>testing</p></body>',
                                      originalFile='test',
                                      docname='test_docname',
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
                                      github_edit_url=fake_deconst['githubUrl'])
        return self.envelope

    def tearDown(self):
        self.config_class = None

    def test_serialization_path_pass(self):
        '''
        Does the correct serialization path appear from this class method?
        '''
        expected_serialization_path = 'fake_envelope_dir/https%3A%2F%2Fgithub.com%2Fdeconst%2Ffake-repo%2Ftest.raml.json'
        actual_serialization_path = self.envelope.serialization_path()
        self.assertEqual(expected_serialization_path,
                         actual_serialization_path)

    @unittest.skip("feature not ready")
    def test_serialization_path_fail(self):
        '''
        Question?
        '''

    def test__populate_meta_pass(self):
        '''
        Does the class method pass the metadata to each per page metadata key?
        '''
        expected_meta_result = {
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            "someKey": "someValue",
            "preferGithubIssues": True,
            'randomkey': 'random'}
        self.envelope._populate_meta()
        actual_meta_result = self.envelope.meta
        self.assertEqual(expected_meta_result, actual_meta_result)

    @unittest.skip("feature not ready")
    def test__populate_meta_fail(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_git_pass(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_git_fail(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_asset_offsets_pass(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_asset_offsets_fail(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_content_id_pass(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_content_id_fail(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_deconst_config_pass(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_deconst_config_fail(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_docname_pass(self):
        '''
        Question?
        '''

    @unittest.skip("feature not ready")
    def test__populate_docname_fail(self):
        '''
        Question?
        '''


if __name__ == '__main__':
    unittest.main()
