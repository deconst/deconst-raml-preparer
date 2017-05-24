#! usr/bin/env python

import os
import re
from bs4 import BeautifulSoup

# TODO: Step 1: Take the assets and copy them over.


# DONE: Step 2: Find all assets in the HTML.

with open(os.getcwd() + '/tests/tester-raw.html', 'r') as html_doc_sample:
    soup = BeautifulSoup(html_doc_sample, 'html.parser')

asset_offset_envelope = {}
changed_envelope = {}
element1 = str(soup)
element2 = 0

for img in soup.find_all('img'):
    tag_string = str(img)
    begin_offset = element1.index(tag_string)
    src_offset = tag_string.index('src="')
    # To get the end of the tag: end_offset = len(tag_string) + begin_offset
    final_offset = len('src="') + src_offset + begin_offset
    n = (img['src'], final_offset)
    img['src'] = element2
    changed_envelope[n] = [img]
    element2 += 1
    # can I use bs4 to replace the src with the asset URL, or is that
    # happening in the submitter? Do I need the offset of the src where I
    # place the single chara, or the offset of the tag?

print(changed_envelope)

# Step 3: Map all assets in the HTML to the location in the asset directory.
# TODO: Replace pseudocode.
# for asset in original_asset_dir:
#     copy image to ASSET_DIR
#     get path using os.path()
#     find the match in the asset_offset_envelope
#     append path to list of the match

# TODO: Step 4: Replace the asset in the HTML with the single-character
# placehoolder.
