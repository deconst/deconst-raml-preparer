#! usr/bin/env python3

import os
import re
import shutil
from bs4 import BeautifulSoup


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
    for key in listed_env:
        path_to_key = src_asset_dir + key
        new_path = dest_asset_dir + key
        # potential BUG: What if the same image is used twice in the doc (or
        # reused in another doc)?
        # print("TEST")
        # print(path_to_key)
        # print(dest_asset_dir)
        shutil.copy(path_to_key, dest_asset_dir)
        changed_envelope[new_path] = changed_envelope.pop(key)
    final_body = str(soup.body)[6:-7]
    return final_body, changed_envelope
