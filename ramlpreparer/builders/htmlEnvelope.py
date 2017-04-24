#! usr/bin/env python

# TODO: Replace psuedocode with real code

from bs4 import BeautifulSoup
import tocbuilder
import json

# Take in HTML
originalHTML = array_with_html_pages

# Put into envelope
for each_page in originalHTML:
    htmlpage = each_page
    soupit = BeautifulSoup(htmlpage, 'html.parser')
    create an empty JSON envelope (instance of class)
    write soupit.find(div='col-md-9') to body field in envelope
    write soupit.title.string to title tag
    toc_html_envelope = htmlify(each_page)

whole_enchilada = {
                    'body': body_html_envelope
                    'title': title_envelope
                    'author': author_envelope
                    'toc': toc_html_envelope
                    'publish_date': pubdate_envelope
                    'categories': cat_envelope
                    'unsearchable': deconst_json_search_choice
}

print(json.dumps(whole_enchilada))
