#! /usr/bin/env python

from bs4 import BeautifulSoup
import re

# TODO: Test with real RAML2HTML output
# TODO: Clean this thing up...
# TODO: Hook up with the rest of the system
# html_doc = """
# <html>
# <head>
# <title>The Dormouse's story</title>
# </head>
# <body>
# <h1>Heading 1</h1>
# <p>randompara</p>
# <h2>Heading 1.1</h2>
# <p>randompara</p>
# <h3>Heading 1.1.1</h3>
# <p>randompara</p>
# <h3>Heading 1.1.2</h3>
# <p>randompara</p>
# <h2>Heading 1.2</h2>
# <p>randompara</p>
# <h2>Heading 1.3</h2>
# <p>randompara</p>
# <h1>Heading 2</h1>
# <p>randompara</p>
# <h2>Heading 2.1</h2>
# <p>randompara</p>
# <h2>Heading 2.2</h2>
# <p>randompara</p>
# </body>
# </html>
# """

def parseIt(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    toc_gen =[]
    current_h2 = []
    current_h3 = ["<ul>"]
    begstr = "<li><a href=\"#"
    endstr = "</a></li>"
    body_tag = soup.body
    regex101 = re.compile('h[1,2,3]')
    cleared_tags = body_tag.findAll(regex101)
    for item in cleared_tags:
        if item.name == 'h1':
            try:
                item_link = item['id']
            except:
                item_link = item.string.replace(" ","")
            toc_gen.append(begstr+item_link+"\">"+item.string+endstr)
        elif item.name == 'h2':
            try:
                item_link = item['id']
            except:
                item_link = item.string.replace(" ","")
            current_h2.append(begstr+item_link+"\">"+item.string+endstr)
            try:
                sibs = item.find_next_sibling(regex101)
                if sibs.name != 'h2':
                    toc_gen.append(current_h2)
                    current_h2 = []
                else:
                    continue
            except:
                toc_gen.append(current_h2)
        elif item.name == 'h3':
            try:
                item_link = item['id']
            except:
                item_link = item.string.replace(" ","")
            current_h3.append(begstr+item_link+"\">"+item.string+endstr)
            try:
                sibs = item.find_next_sibling(regex101)
                if sibs.name != 'h3':
                    current_h3.append("</ul>")
                    toc_gen.append(current_h3)
                    current_h3 = []
                else:
                    continue
            except:
                toc_gen.append(current_h3)
    return toc_gen

def htmlify(toc_list):
    result = ["<ul>"]
    for item in toc_list:
        if isinstance(item, list):
            result.append(htmlify(item))
        else:
            result.append(item)
    result.append("</ul>")
    return result
