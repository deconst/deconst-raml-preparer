#! usr/bin/env python3

from bs4 import BeautifulSoup
import json
import subprocess
import os

import ramlpreparer.builders.asset_mapper as asset_mapper
import ramlpreparer.builders.common as common
import ramlpreparer.builders.tocbuilder as tocbuilder
import ramlpreparer.builders.raml2html as raml2html

# Initialize the raml2html package.
starter_call = os.path.join(
    os.getcwd(), 'ramlpreparer', 'scripts', 'npminstall.sh')
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
        self.title = title
        self._populate_docname()
        self._populate_deconst_config()
        self._populate_content_id()
        self._populate_meta()
        self._populate_asset_offsets()
        self._populate_unsearchable()
        self._populate_git()

        the_envelope = {
            'body': self.body,  # TODO: Fix the body to show the asset mapper
            'docname': self.docname,  # DONE: Set docname up so the content id and all work
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

    def _populate_deconst_config(self):
        '''
        Pull in all the deconst json info
        '''
        self.deconst_config = common.init_builder(os.getcwd())

    def _populate_docname(self):
        '''

        '''
        self.docname = self.title.replace(" ", "")


def make_it_html(raml, output_html):
    '''
    Takes in the RAML and gives out HTML
    '''
    originalHTML = raml2html.raml2html(raml, output_html)
    return originalHTML


def parsing_html(page, page_title=None):
    '''
    Parse the HTML to put it in an envelope. Optional arguments are for
    unittests only.
    '''
    with open(page, 'r') as contents:
        soupit = BeautifulSoup(contents, 'html.parser')
    with open(page, 'r') as contents:
        that_page = tocbuilder.parse_it(contents)
    toc_html = tocbuilder.htmlify(that_page)
    if page_title == None:
        the_title = soupit.title.string
    else:
        the_title = page_title
    whole_envelope = Envelope_RAML(body=soupit.body,
                                   title=the_title,
                                   toc=toc_html)
    return whole_envelope


def make_json(envelope):
    '''
    Take in an HTML envelope (a dictionary) and output JSON.
    '''
    the_envelope_please = json.dumps(envelope)
    return the_envelope_please


def write_out(jsonfile, file_path=None, envelope=None):
    '''
    Write the JSON to the serialized path. If no file_path is provided, the
    original envelope from make_json() is needed to generate a file path. An
    error is raised if you don't have a file path or an envelope.
    '''
    if file_path is None and envelope is None:
        raise ValueError("If you don't have a file path, you need to" +
                         "identify the envelope that the JSON came from so " +
                         "the system can generate a file path for you.")
    elif file_path is None and envelope is not None:
        file_path = envelope.serialization_path()
    else:
        pass
    with open(file_path, 'w') as thefile:
        json.dump(jsonfile, thefile)
    return thefile


# QUESTION: Does each page's envelope need to get placed separately? Currently,
# it's written to put each envelope inside of a larger envelope...
# TODO: Write each envelope to a new file in ENVELOPE_DIR.
# TODO: Review the code from the Sphinx preparer if anything should be copied.
