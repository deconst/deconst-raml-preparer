#! usr/bin/env python

from bs4 import BeautifulSoup
import json
import subprocess

import .asset_mapper
import .common
import .tocbuilder
import .raml2html

# Initialize the raml2html package.
starter_call = os.getcwd() + '/ramlpreparer/scripts/npminstall.sh'
subprocess.call(starter_call, shell=True)


class Envelope_RAML:
    '''
    A class for metadata envelopes.
    '''

    def __init__(self, body, docname=None, title=None, toc=None,
                 publish_date=None, unsearchable=None, content_id=None,
                 meta=None, asset_offsets=None, addenda=None,
                 deconst_config=None, per_page_meta=None):
        '''
        Run populations, and initiate dictionary.
        '''
        self._populate_content_id()
        self._populate_meta()
        self._populate_asset_offsets()
        self._populate_unsearchable()
        self._populate_git()

        the_envelope = {
            'body': self.body,  # TODO: Fix the body to show the asset mapper
            'docname': self.docname,  # TODO: Set docname up so the content id and all work
            'title': self.title,
            'toc': self.toc,
            # NOTE: Not sure if any of these following ones will be used.
            # 'publish_date': self.publish_date,  # Ditto
            'unsearchable': self.unsearchable,  # From deconst, or Sphinx?
            # TODO: Get these next ones figured out (from the Sphinx preparer)
            'content_id': self.content_id,
            'meta': self.meta,
            'asset_offsets': self.asset_offsets,
            'addenda': self.addenda,
            'deconst_config': self.deconst_config,
            'per_page_meta': self.per_page_meta
        }
        return the_envelope

    def serialization_path(self):
        '''
        Generate the full path at which this envelope should be serialized.
        '''
        envelope_filename = urllib.parse.quote(
            self.content_id, safe='') + '.json'
        return path.join(self.deconst_config.envelope_dir, envelope_filename)

    def _populate_meta(self):
        '''
        Merge repository-global and per-page metadata into the envelope's
        metadata.
        '''
        self.meta = self.deconst_config.meta.copy()
        self.meta.update(self.per_page_meta)

    def _populate_git(self):
        '''
        Set the github_edit_url property within "meta".
        '''
        if self.deconst_config.git_root and self.deconst_config.github_url:
            full_path = path.join(os.getcwd(),
                                  self.builder.env.srcdir,
                                  self.docname + self.config.source_suffix[0])
            edit_segments = [
                self.deconst_config.github_url,
                'edit',
                self.deconst_config.github_branch,
                path.relpath(full_path, self.env.srcdir)
            ]
            self.meta['github_edit_url'] = (
                '/'.join(segment.strip('/') for segment in edit_segments))

    def _populate_unsearchable(self):
        '''
        Populate "unsearchable" from per-page or repository-wide settings.
        '''
        unsearchable = self.per_page_meta.get(
            'deconstunsearchable', self.config.deconst_default_unsearchable)
        if unsearchable is not None:
            self.unsearchable = unsearchable in ('true', True)

    def _populate_asset_offsets(self):
        '''
        Read stored asset offsets from the asset mapper, and then update the body.
        '''
        self.body, self.asset_offsets = self.asset_offsets.map_the_assets()

    def _populate_content_id(self):
        '''
        Derive this envelope's content ID.
        '''
        self.content_id = common.derive_content_id(
            self.deconst_config, self.docname)


def make_it_html(self, raml, output_html):
    '''
    Takes in the RAML and gives out HTML
    '''
    originalHTML = raml2html.raml2html(raml, output_html)
    return originalHTML


def parsing_html(self, page):
    '''
    Parse the HTML to put it in an envelope.
    '''
    soupit = BeautifulSoup(page, 'html.parser')
    that_page = tocbuilder.parse_it(page)
    toc_html = tocbuilder.htmlify(that_page)
    whole_envelope = Envelope_RAML(body=soupit.body,
                                   title=soupit.title.string,
                                   toc=toc_html)
    return whole_envelope


def make_json(self, envelope):
    '''
    Take in an HTML envelope (a dictionary) and output JSON.
    '''
    the_envelope_please = json.dumps(envelope)
    return the_envelope_please


def write_out(self, jsonfile):
    '''
    Write the JSON to the serialized path.
    '''
    file_path = serialization_path()
    with open(file_path, 'w') as thefile:
        json.dump(jsonfile, thefile)
    return thefile


# QUESTION: Does each page's envelope need to get placed separately? Currently,
# it's written to put each envelope inside of a larger envelope...
# TODO: Write each envelope to a new file in ENVELOPE_DIR.
# TODO: Review the code from the Sphinx preparer if anything should be copied.
