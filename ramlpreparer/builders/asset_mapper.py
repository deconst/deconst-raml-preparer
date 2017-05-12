#! usr/bin/env python

import os

# Take the assets and copy them over.
# Find all assets in the HTML.

the_body = soup.body
asset_offset_envelope = {}

# TODO: Figure out how to find it in the_body so this for loop works to find
# the offset...
for img in the_body:
    n = str(img)
    asset_offset_envelope[n] = [the_body.ascii_lowercase.index('<img')]

# Map all assets in the HTML to the location in the asset directory.
# TODO: Replace pseudocode.
for asset in original_asset_dir:
    copy image to ASSET_DIR
    get path using os.path()
    find the match in the asset_offset_envelope
    append path to list of the match

# TODO: Replace the asset in the HTML with the single-character placehoolder.
