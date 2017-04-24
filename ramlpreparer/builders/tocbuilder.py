#! /usr/bin/env python

from bs4 import BeautifulSoup
import re

# TODO: Test with real RAML2HTML output
# TODO: Hook up with the rest of the system
html_doc = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<h1>Heading 1</h1>
<p>randompara</p>
<h2>Heading 1.1</h2>
<p>randompara</p>
<h3>Heading 1.1.1</h3>
<p>randompara</p>
<h3>Heading 1.1.2</h3>
<p>randompara</p>
<h2>Heading 1.2</h2>
<p>randompara</p>
<h2>Heading 1.3</h2>
<p>randompara</p>
<h1>Heading 2</h1>
<p>randompara</p>
<h2>Heading 2.1</h2>
<p>randompara</p>
<h2>Heading 2.2</h2>
<p>randompara</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Intial code attempt with complements to http://stackoverflow.com/a/2515508
# (so I'm not starting from scratch completely)

toc_gen =[]
current_h2 = []
current_h3 = ["<ul>"]
begstr = "<li><a href=\"#"
endstr = "</a></li>"
body_tag = soup.body
regex101 = re.compile('h[1,2,3]')
cleared_tags = body_tag.findAll(regex101)

for child in cleared_tags:
    if child.name == 'h1':
        try:
            child_link = child['id']
        except:
            child_link = child.string.replace(" ","")
            print(child_link)
        toc_gen.append(begstr+child_link+"\">"+child.string+endstr)
    elif child.name == 'h2':
        try:
            child_link = child['id']
        except:
            child_link = child.string.replace(" ","")
            print(child_link)
        current_h2.append(begstr+child_link+"\">"+child.string+endstr)
        try:
            sibs = child.find_next_sibling(regex101)
            if sibs.name != 'h2':
                toc_gen.append(current_h2)
                current_h2 = []
            else:
                continue
        except:
            toc_gen.append(current_h2)
    elif child.name == 'h3':
        try:
            child_link = child['id']
        except:
            child_link = child.string.replace(" ","")
            print(child_link)
        current_h3.append(begstr+child_link+"\">"+child.string+endstr)
        try:
            sibs = child.find_next_sibling(regex101)
            if sibs.name != 'h3':
                current_h3.append("</ul>")
                toc_gen.append(current_h3)
                current_h3 = []
            else:
                continue
        except:
            toc_gen.append(current_h3)

def htmlify(toc_list):
    result = ["<ul>"]
    for item in toc_list:
        if isinstance(item, list):
            result.append(htmlify(item))
        else:
            print("This item is not a list!")
            result.append(item)
    result.append("</ul>")
    return "\n".join(result)

# Table of contents
print(htmlify(toc_gen))
