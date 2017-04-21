#! usr/bin/env python

# TODO: Replace psuedocode with real code

from bs4 import BeautifulSoup

# Take in HTML
originalHTML = array_with_html_pages

# Put into envelope
for each_page in originalHTML:
    htmlpage = each_page
    soupit = BeautifulSoup(htmlpage, 'html.parser')
    create an empty JSON envelope (instance of class)
    write soupit.find(div='col-md-9') to body field in envelope
    write soupit.title.string to title tag
    parse body for headings
    convert headings into layered toc div
    put toc div in toc tag
