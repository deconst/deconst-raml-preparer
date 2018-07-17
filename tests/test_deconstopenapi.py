#!/usr/bin/env python3
# From https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md
'''
test_deconstopenapi
----------------------------------
Tests for `deconstopenapi` module.
'''

import unittest
import subprocess
import sys
import os
import json
from unittest import mock
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.deconstopenapi import enveloper
from openapipreparer.deconstopenapi import submit
from openapipreparer.deconstopenapi import find_all
from openapipreparer.config import Configuration


class DeconstOPENAPITestCase(unittest.TestCase):
    '''
    Tests for the deconstraml methods
    '''

    def test_enveloper_pass(self):
        '''
        Does the enveloper link things together properly?
        '''
        self.maxDiff = None
        raml_location = path.join(
            os.getcwd(), 'tests', 'src', 'openapi.json')
        html_location = path.join(
            os.getcwd(), 'tests', 'dest')
        actual_result = enveloper(raml_location, html_location)
        expected_result = {
            "body": '<div class="container"><div class="row"><div class="col-md-9" role="main"><div class="page-header"><h1 id="topTitle">Instagram API Sample RAML File API documentation version v1</h1><p>https://api.instagram.com/{version}</p><p>A sample RAML spec using Instagram\'s API</p><ul><li><strong>version</strong>: <em>required (v1)</em></li></ul><h2 id="test_chapter"><a href="#test_chapter">test chapter</a></h2><p>Nothing here.</p><h2 id="authentication"><a href="#authentication">Authentication</a></h2><p>testing documentation</p></div><div><div><h2 id="p__shortcode__media">/p/{shortcode}/media</h2></div><div><div><div><div><h4><a href="#panel_p__shortcode__media"><span class="parent"></span>/p/{shortcode}/media</a> <span class="methods"><a href="#p__shortcode__media_get"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span></a></span></h4></div><div id="panel_p__shortcode__media"><div><div class="list-group"><div class="list-group-item"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span><div class="method_description"><p>Given a short link, issues a redirect to that media\'s JPG file.</p></div><div class="clearfix"></div></div></div></div></div><div id="p__shortcode__media_get"><div><div><div><h4 id="myModalLabel"><span class="badge badge_get">get <span class="glyphicon glyphicon-lock" title="Authentication required"></span></span> <span class="parent"></span>/p/{shortcode}/media</h4></div><div><div class="alert alert-info"><p>Given a short link, issues a redirect to that media\'s JPG file.</p></div><div class="alert alert-warning"><span class="glyphicon glyphicon-lock" title="Authentication required"></span> Secured by <b></b></div><ul><li><a data-toggle="tab" href="#p__shortcode__media_get_request">Request</a></li><li><a href="#p__shortcode__media_get_response">Response</a></li><li><a href="#p__shortcode__media_get_securedby">Security</a></li></ul><div><div id="p__shortcode__media_get_request"><h3>URI Parameters</h3><ul><li><strong>shortcode</strong>: <em>required (string)</em></li></ul><h3>Query Parameters</h3><ul><li><strong>size</strong>: <em>required (one of t,, m,, l - default: m)</em></li></ul></div><div id="p__shortcode__media_get_response"><h2>HTTP status code 302</h2><h3>Body</h3><p><strong>Media type</strong>: text/html</p><p><strong>Type</strong>: object</p><p><strong>Example</strong>:</p><div class="examples"><pre><code>HTTP/1.1 302 FOUND\nLocation: http://distillery.s3.amazonaws.com/media/2010/10/02/7e4051fdcf1d45ab9bc1fba2582c0c6b_6.jpg\n</code></pre></div></div><div id="p__shortcode__media_get_securedby"><h2>Secured by</h2></div></div></div></div></div></div></div></div></div></div></div></div></div>',
            "docname": str(html_location),
            "title": "Instagram API Sample RAML File API documentation",
            "toc": '<ul><li><a href="#test_chapter">test chapter</a></li><li><a href="#authentication">Authentication</a></li><li><a href="#p__shortcode__media">/p/{shortcode}/media</a></li><ul><li><a href="#p__shortcode__media-get-">/p/{shortcode}/media get </a></li></ul><ul><li><a href="#myModalLabel">get  /p/{shortcode}/media</a></li></ul><ul><li><a href="#URIParameters">URI Parameters</a></li><li><a href="#QueryParameters">Query Parameters</a></li></ul><li><a href="#HTTPstatuscode302">HTTP status code 302</a></li><ul><li><a href="#Body">Body</a></li></ul><li><a href="#Securedby">Secured by</a></li></ul>',
            'unsearchable': None,
            'content_id': str(html_location),
            'meta': {'github_edit_url': 'https://github.com/deconst/fake-repo/edit/master/tests/dest/test_make_it.html',
                     'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
                     'preferGithubIssues': True,
                     'someKey': 'someValue'},
            'asset_offsets': {},
            'addenda': None,
            'per_page_meta': {}}
        print(actual_result)
        self.assertEqual(actual_result, expected_result)

    def test_submit_pass(self):
        '''
        Does the submit method pass the json properly?
        '''
        config = Configuration(os.environ)
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
        dest_path = submit(the_envelope_passed)
        with open(dest_path, 'r') as written_file:
            actual_file = json.load(written_file)
        fake_json_envelope = os.path.join(
            os.getcwd(), 'tests', 'src', 'input_file_writeout.json')
        with open(fake_json_envelope, 'r') as fake_envelope:
            expected_json_output = json.load(fake_envelope)
        self.assertEqual(actual_file, expected_json_output)

    def test_find_all_pass(self):
        '''
        Does the find_all method really find all the RAML it can?
        '''
        config_file = Configuration(os.environ)
        actual_list = find_all(config_file)
        expected_list = [os.path.join(
            os.getcwd(), 'tests', 'src', 'small_test.raml')]
        self.assertEqual(actual_list, expected_list)


if __name__ == '__main__':
    unittest.main()
