#! usr/bin/env python

# Take the assets and copy them over.
# Find all assets in the HTML.

the_body = soup.body

# TODO: Figure out how to find it in the_body so this for loop works to find
# the offset...
for img in the_body:
    asset[n] = the_body.ascii_lowercase.index('<img')
    n += 1

# Map all assets in the HTML to the location in the asset directory.
