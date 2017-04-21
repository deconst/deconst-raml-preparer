#! /usr/bin/env python

from bs4 import BeautifulSoup

# TODO: Test with real RAML2HTML output
# TODO: Hook up with the rest of the system
html_doc = """
<html><head><title>The Dormouse's story</title></head><body><h1>Heading 1</h1><h2>Heading 1.1</h2><h3>Heading 1.1.1</h3><h3>Heading 1.1.2</h3><h2>Heading 1.2</h2><h2>Heading 1.3</h2><h1>Heading 2</h1><h2>Heading 2.1</h2><h2>Heading 2.2</h2></body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Intial code attempt with complements to http://stackoverflow.com/a/2515508 (so I'm not starting from scratch completely)

toc_gen = []
current_list = toc_gen
previous_tag = None

for heading in soup.findAll(['h2', 'h3', 'h4', 'h5', 'h6']):
    heading_link = heading.string.replace(" ","")

# TODO: Implement for all levels
# TODO: Clean this mess up

    if previous_tag == 'h2' and heading.name == 'h3':
        current_list = []
    elif previous_tag == 'h3' and heading.name == 'h2':
        toc_gen.append(current_list)
        current_list = toc_gen
#    elif previous_tag == 'h3' and heading.name == 'h4':
#        pass

    current_list.append((heading_link, heading.string))

    previous_tag = heading.name

if current_list != toc_gen:
    toc_gen.append(current_list)


def htmlify(toc_list):
    print(toc_list)
    result = ["<ul>"]
    for item in toc_list:
        if isinstance(item, list):
            result.append(htmlify(item))
        else:
            result.append('<li><a href="#%s">%s</a></li>' % item)
    result.append("</ul>")
    return "\n".join(result)

# Table of contents
print(htmlify(toc_gen))
