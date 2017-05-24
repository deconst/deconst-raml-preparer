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
    end_offset = len(tag_string) + begin_offset
    n = (begin_offset, end_offset, img['src'])
    print(n)
    asset_offset_envelope[n] = [tag_string]
    img['src'] = element2
    changed_envelope[element2] = [img]
    element2 += 1

print(asset_offset_envelope)
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
