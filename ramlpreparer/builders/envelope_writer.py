#! usr/bin/env python

from bs4 import BeautifulSoup
import tocbuilder
import json
import raml2html
import subprocess
starter_call = '../scripts/npminstall.sh'
subprocess.call(starter_call)

html_list = []
list_of_ramls = ['../../tests/tester.raml', '../../tests/tester.raml']
whole_enchilada = {}
n = 0
that_page = ''


class Envelope_RAML:
    '''
    A class for metadata envelopes.
    '''

    def __init__(self, docname, body, title, author, toc, publish_date,
                 categories, unsearchable):
        self.docname = docname
        self.body = body
        self.title = title
        self.toc = toc
        # NOTE: Not sure if any of these following ones will be used.
        self.author = author
        self.publish_date = publish_date
        self.categories = categories
        self.unsearchable = unsearchable
        # TODO: Get these next ones figured out (from the Sphinx preparer)
        self.content_id = None
        self.layout_key = None
        self.meta = None
        self.asset_offsets = None
        self.next = None
        self.previous = None
        self.addenda = None
        self.builder = builder
        self.deconst_config = deconst_config
        self.per_page_meta = per_page_meta
        self.docwriter = docwriter

    def serialization_path(self):
        """
        Generate the full path at which this envelope should be serialized.
        """

        envelope_filename = urllib.parse.quote(
            self.content_id, safe='') + '.json'
        return path.join(self.deconst_config.envelope_dir, envelope_filename)

    def serialization_payload(self):
        """
        Construct a dict containing the data that should be serialized as part
        of the envelope.
        """

        payload = {'body': self.body}
        if self.title:
            payload['title'] = self.title
        if self.toc:
            payload['toc'] = self.toc

        if self.unsearchable is not None:
            payload['unsearchable'] = self.unsearchable
        if self.layout_key is not None:
            payload['layout_key'] = self.layout_key
        if self.categories is not None:
            payload['categories'] = self.categories
        if self.meta is not None:
            payload['meta'] = self.meta
        if self.asset_offsets is not None:
            payload['asset_offsets'] = self.asset_offsets

        if self.next is not None:
            payload['next'] = self.next
        if self.previous is not None:
            payload['previous'] = self.previous
        if self.addenda is not None:
            payload['addenda'] = self.addenda


# Take in HTML
for raml in list_of_ramls:
    output_html = '../../tests/tester-raw.html'
    originalHTML = raml2html.raml2html(raml, output_html)
    html_list.append(originalHTML)

# Put into envelope
# QUESTION: Does each page's envelope need to get placed separately? Currently,
# it's written to put each envelope inside of a larger envelope...
for page in html_list:
    soupit = BeautifulSoup(page, 'html.parser')
    that_page = tocbuilder.parseIt(page)
    toc_html = tocbuilder.htmlify(that_page)
    whole_envelope = Envelope_RAML(body=soupit.body,
                                   title=soupit.title.string,
                                   toc=toc_html)
    whole_enchilada[n] = whole_envelope
    n += 1

print(whole_enchilada)
# print(json.dumps(whole_enchilada))
# TODO: Write each envelope to a new file in ENVELOPE_DIR.
# TODO: Review the code from the Sphinx preparer if anything should be copied.
