#! usr/bin/env python

# TODO: Replace psuedocode with real code
# NOTE: Probably not going to be used. envelope_writer.py ended up holding this, really.

# Take in HTML
originalHTML = array_with_html_pages

# Put into envelope
for each_page in originalHTML:
    remove extra classes from the RAML2HTML converter
    create an empty JSON envelope (instance of class)
    write contents of body div tag holding content only to body field
    parse head tag
    put head.title in title tag
    put head.category in category tag?
    parse body for div tag from RAML2HTML holding sidebartoc
    put toc div in toc tag
