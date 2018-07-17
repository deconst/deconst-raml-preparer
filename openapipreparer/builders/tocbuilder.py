#! /usr/bin/env python3

from bs4 import BeautifulSoup
import re

# NOTE: It might be better to move this into another file for cleanliness.


def tag_it(tag):
    '''
    Set up a tag link.
    '''
    try:
        tag_link = str(tag['id'])
    except KeyError:
        try:
            tag_string = tag.string
            tag_link = tag_string.replace(" ", "")
        except AttributeError:
            complicated_tag = tag.get_text()
            replace1 = complicated_tag.strip('/')
            replace2 = replace1.replace("/{", "__")
            replace3 = replace2.replace("}/", "__")
            replace4 = replace3.replace("/", "__")
            tag_link = replace4.replace(" ", "-")        
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
            return (toc_gen,
                    current_heading_list,
                    prev_list,
                    sib_head_level
                    )
        elif sibs.name != name and head_level > sib_head_level:
            prev_list.append(current_heading_list)
            current_heading_list = []
            return (toc_gen,
                    current_heading_list,
                    prev_list, sib_head_level
                    )
        else:
            return (toc_gen,
                    current_heading_list,
                    prev_list,
                    sib_head_level
                    )
    except AttributeError:
        if head_level != '2':
            toc_gen.append(current_heading_list)
            current_heading_list = []
            return (toc_gen,
                    current_heading_list,
                    prev_list,
                    sib_head_level
                    )
        else:
            return (toc_gen,
                    current_heading_list,
                    prev_list,
                    sib_head_level
                    )


def parse_it(html_doc,
             toc_gen=None,
             current_h2=None,
             current_h3=None,
             current_h4=None,
             begstr="<li><a href=\"#",
             endstr="</a></li>"
             ):
    '''
    Parses an HTML doc for headings to add to a table of contents.

    Note that H1 is reserved for the title of the page in the library. This
    system assumes that there are only three levels for headings, which is
    considered good practice in documentation.
    '''
    if toc_gen is None:
        toc_gen = []
        current_h3 = []
        current_h4 = []
    else:
        toc_gen = None
        current_h2 = None
        current_h3 = None
        current_h4 = None
        toc_gen = []
        current_h3 = []
        current_h4 = []
    soup = BeautifulSoup(html_doc, 'html.parser')
    body_tag = soup.body
    regex101 = re.compile('h[2,3,4]')
    cleared_tags = body_tag.findAll(regex101)
    # print("Test clear tags --> {}".format(cleared_tags))
    for tag in cleared_tags:
        if tag.name == 'h2':
            tag_link = tag_it(tag)
            toc_gen.append(begstr + tag_link + "\">" + tag.string + endstr)
            (toc_gen, current_h2, prev_var, sib) = sibs_it(
                tag,
                tag.name,
                current_h2,
                regex101,
                toc_gen
            )
            if sib != '2':
                pass
            if sib == '0':
                current_h2 = []
                current_h3 = []
                current_h4 = []
                prev_var = []
            else:
                current_h2 = []
                current_h3 = []
                current_h4 = []
                prev_var = []
        elif tag.name == 'h3':
            #print("tag.string_type = {}, tag.string_value = {}".format(type(tag.string), tag.string))
            #print("begstr_type = {}, begstr_value = {}".format(type(begstr), begstr))
            # print("begstr = {}".format(begstr))
            #print("endstr_type = {}, endstr_value = {}".format(type(endstr), endstr))
            # print("endstr = {}".format(endstr))
            tag_link = tag_it(tag)
            #print("tag_link type = {}, tag_link value = {}".format(type(tag_link), tag_link))
            
            ## TODO: Ask Laura about the tag.string because we have lot of tags with empty string,
            ## might be because of templating not sure so will need to make sure of the result.
            ## if that is the case should do it for all the tags here.
            if tag.string:
                #print("final string ==> {}".format(begstr + tag_link + "\">" + tag.string + endstr))
                current_h3.append(begstr + tag_link + "\">" + tag.string + endstr)
            else:
                # print("final string ==> {}".format(begstr + tag_link + "\">" + tag.string + endstr))
                current_h3.append(begstr + tag_link + "\">" + "" + endstr)
            ##TODO: come back here
            
            # except TypeError:
                # print("----EXCEPTION")
                # print("tag.string_type = {}, tag.string_value = {}".format(type(tag.string), tag.string))
                # print("begstr_type = {}, begstr_value = {}".format(type(begstr), begstr))
                # # print("begstr = {}".format(begstr))
                # print("endstr_type = {}, endstr_value = {}".format(type(endstr), endstr))
                # # print("endstr = {}".format(endstr))
                # tag_link = tag_it(tag)
                # print("tag_link type = {}, tag_link value = {}".format(type(tag_link), tag_link))
                # print("------EXCEPTION")
                
            (toc_gen, current_h3, prev_var, sib) = sibs_it(
                tag,
                tag.name,
                current_h3,
                regex101,
                toc_gen,
                current_h2
            )
            if sib == '2':
                current_h3 = current_h2
                toc_gen.append(current_h3)
                current_h3 = []
            if sib == '0':
                current_h2 = []
                current_h3 = []
                current_h4 = []
                prev_var = []
            else:
                pass
        elif tag.name == 'h4':
            tag_link = tag_it(tag)
            try:
                current_h4.append(begstr + tag_link +
                                  "\">" + tag.string + endstr)
            except TypeError:
                current_h4.append(begstr + tag_link +
                                  "\">" + tag.get_text() + endstr)
            (toc_gen, current_h4, prev_var, sib) = sibs_it(
                tag,
                tag.name,
                current_h4,
                regex101,
                toc_gen,
                current_h3
            )
            if sib == '2':
                toc_gen.append(current_h3)
                current_h2 = []
                current_h3 = []
                current_h4 = []
                prev_var = []
            if sib == '0':
                current_h2 = []
                current_h3 = []
                current_h4 = []
                prev_var = []
            else:
                pass
    # print("toc_gen-->{}".format(toc_gen))
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
    html_result = "".join(result)
    return html_result
