#! /usr/bin/env python

from bs4 import BeautifulSoup
import re

# DONE: Test with real RAML2HTML output
# DONE: Pythonify this
# TODO: Retest after modularizing with real RAML2HTML output.
# DONE: Hook up with the rest of the system
# NOTE: It might be better to move this into another file for cleanliness.


def tag_it(tag):
    '''
    Set up a tag link.
    '''
    try:
        tag_link = str(tag['id'])
    except KeyError:
        tag_string = tag.string
        tag_link = tag_string.replace(" ", "")
    return tag_link


def sibs_it(tag, name, current_heading_list, regex101, toc_gen, prev_list=None):
    '''
    Identify if the next heading is at the same level. If not, close the
    unordered list and start a new one for the heading level. If it is, add
    that item to the current unordered list.
    '''
    sibs = tag.find_next_sibling(regex101)
    head_level = re.findall(r'\d+', name)[0]
    try:
        sib_head_level = re.findall(r'\d+', sibs.name)[0]
    except AttributeError:
        sib_head_level = 0
    try:
        if sibs.name != name and head_level < sib_head_level:
            return (toc_gen, current_heading_list, prev_list, sib_head_level)
        elif sibs.name != name and head_level > sib_head_level:
            prev_list.append(current_heading_list)
            current_heading_list = []
            return (toc_gen, current_heading_list, prev_list, sib_head_level)
        else:
            return (toc_gen, current_heading_list, prev_list, sib_head_level)
    except AttributeError:
        if head_level != '1':
            toc_gen.append(current_heading_list)
            current_heading_list = []
            return (toc_gen, current_heading_list, prev_list, sib_head_level)
        else:
            return (toc_gen, current_heading_list, prev_list, sib_head_level)


def parse_it(html_doc, toc_gen=None, current_h1=None, current_h2=None,
             current_h3=None, begstr="<li><a href=\"#", endstr="</a></li>"):
    '''
    Parses an HTML doc for headings to add to a table of contents.
    '''
    if toc_gen is None:
        toc_gen = []
        # current_h1 = []
        current_h2 = []
        current_h3 = []
    else:
        toc_gen = None
        current_h1 = None
        current_h2 = None
        current_h3 = None
        toc_gen = []
        # current_h1 = []
        current_h2 = []
        current_h3 = []
    soup = BeautifulSoup(html_doc, 'html.parser')
    body_tag = soup.body
    regex101 = re.compile('h[1,2,3]')
    cleared_tags = body_tag.findAll(regex101)
    for tag in cleared_tags:
        if tag.name == 'h1':
            tag_link = tag_it(tag)
            toc_gen.append(begstr + tag_link + "\">" + tag.string + endstr)
            (toc_gen, current_h1, prev_var, sib) = sibs_it(
                tag, tag.name, current_h1, regex101, toc_gen)
            if sib != '1':
                pass
            if sib == '0':
                current_h1 = []
                current_h2 = []
                current_h3 = []
                prev_var = []
            else:
                current_h1 = []
                current_h2 = []
                current_h3 = []
                prev_var = []
        elif tag.name == 'h2':
            tag_link = tag_it(tag)
            current_h2.append(begstr + tag_link + "\">" + tag.string + endstr)
            (toc_gen, current_h2, prev_var, sib) = sibs_it(
                tag, tag.name, current_h2, regex101, toc_gen, current_h1)
            if sib == '1':
                current_h2 = current_h1
                toc_gen.append(current_h2)
                current_h2 = []
            if sib == '0':
                current_h1 = []
                current_h2 = []
                current_h3 = []
                prev_var = []
            else:
                pass
        elif tag.name == 'h3':
            tag_link = tag_it(tag)
            current_h3.append(begstr + tag_link + "\">" + tag.string + endstr)
            (toc_gen, current_h3, prev_var, sib) = sibs_it(
                tag, tag.name, current_h3, regex101, toc_gen, current_h2)
            if sib == '1':
                toc_gen.append(current_h2)
                current_h1 = []
                current_h2 = []
                current_h3 = []
                prev_var = []
            if sib == '0':
                current_h1 = []
                current_h2 = []
                current_h3 = []
                prev_var = []
            else:
                pass
    return toc_gen


def htmlify(toc_list):
    '''
    Put together the TOC pieces to make a full TOC for an HTML document.
    '''
    result = ["<ul>"]
    for item in toc_list:
        if isinstance(item, list):
            result.append(htmlify(item))
        else:
            result.append(item)
    result.append("</ul>")
    return result
