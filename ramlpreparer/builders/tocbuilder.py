#! /usr/bin/env python

from bs4 import BeautifulSoup
import re

# TODO: Test with real RAML2HTML output
# TODO: Pythonify this
# TODO: Hook up with the rest of the system
# NOTE: It might be better to move this into another file for cleanliness.

def parseIt(html_doc):
    '''
    Parses an HTML doc for headings to add to a table of contents.
    '''
    soup = BeautifulSoup(html_doc, 'html.parser')
    toc_gen =[]
    current_h2 = []
    current_h3 = ["<ul>"]
    begstr = "<li><a href=\"#"
    endstr = "</a></li>"
    body_tag = soup.body
    regex101 = re.compile('h[1,2,3]')
    cleared_tags = body_tag.findAll(regex101)
    for tag in cleared_tags:
        if tag.name == 'h1':
            try:
                tag_link = str(tag['id'])
            except KeyError:
                tag_string = tag.string
                tag_link = tag_string.replace(" ","")
            toc_gen.append(begstr+tag_link+"\">"+tag.string+endstr)
        elif tag.name == 'h2':
            try:
                tag_link = tag['id']
            except KeyError:
                tag_string = tag.string
                tag_link = tag_string.replace(" ","")
            current_h2.append(begstr+tag_link+"\">"+tag.string+endstr)
            try:
                sibs = tag.find_next_sibling(regex101)
                if sibs.name != 'h2':
                    toc_gen.append(current_h2)
                    current_h2 = []
                else:
                    continue
            except:
                toc_gen.append(current_h2)
        elif tag.name == 'h3':
            try:
                tag_link = tag['id']
            except KeyError:
                tag_string = tag.string
                tag_link = tag_string.replace(" ","")
            current_h3.append(begstr+tag_link+"\">"+tag.string+endstr)
            try:
                sibs = tag.find_next_sibling(regex101)
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
