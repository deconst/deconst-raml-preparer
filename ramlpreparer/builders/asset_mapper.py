#! usr/bin/env python3

import os
import re
import shutil
from bs4 import BeautifulSoup

# DONE: Step 1: Take the assets and copy them over.
# NOTE: Look at envelopes with
# http://localhost:9000/content/https%3A%2F%2Fgithub.com%2F<org>%2F<repo>
#     %2F<permalink>
# from the integrated deconst.
# DONE: Step 2: Find all assets in the HTML.
# src_asset_dir = './tests/src/assets/'
# dest_asset_dir = './tests/dest/assets/'  # os.getenv('ASSET_DIR')


def map_the_assets(src_asset_dir, dest_asset_dir, docname=None, html_doc_path=None, html_source=None):
    '''
    Given an HTML file, take all image assets and remap for deconst.
    '''
    if not docname:
        docname = 'test.html'
    if html_doc_path:
        the_path = os.path.join(os.getcwd(), html_doc_path)
        with open(the_path, 'r') as html_doc_sample:
            soup = BeautifulSoup(html_doc_sample, 'html.parser')
    elif html_source:
        soup = BeautifulSoup(html_source, 'html.parser')
    else:
        raise ValueError(
            'You need to send this some HTML. Use either a path or a source file.')
    changed_envelope = {}
    element1 = str(soup)
    element2 = 0
    for img in soup.find_all('img'):
        tag_string = str(img)
        begin_offset = element1.index(tag_string)
        src_offset = tag_string.index('src="')
        # To get the end of the tag: end_offset = len(tag_string) +
        # begin_offset
        final_offset = len('src="') + src_offset + begin_offset
        n = img['src']
        img['src'] = element2
        changed_envelope[n] = final_offset
        element2 += 1
    listed_env = list(changed_envelope)
    # Step 3: Map all assets in the HTML to the location in the asset
    # directory.
    # DONE: Replace pseudocode.
    for key in listed_env:
        path_to_key = src_asset_dir + key
        new_path = dest_asset_dir + key
        # potential BUG: What if the same image is used twice in the doc (or
        # reused in another doc)?
        shutil.copy(path_to_key, dest_asset_dir)
        changed_envelope[new_path] = changed_envelope.pop(key)
    # DONE: Step 4: Replace the asset in the HTML with the single-character
    # placeholder.
    # the_new_path = os.path.join(
    #     os.getcwd(), 'tests', 'dest', 'asset_test.html')
    # with open(the_new_path, 'a') as cleaned_file:
    #     cleaned_file.write(str(soup))
    # with open(the_new_path, 'r') as cleaned_file:
        # final_html = BeautifulSoup(cleaned_file, 'html.parser')
    final_body = str(soup.body)[6:-7]
    return final_body, changed_envelope
