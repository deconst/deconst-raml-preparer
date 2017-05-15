#! usr/bin/env python

from bs4 import BeautifulSoup
import json
import subprocess

import .asset_mapper
import .common
import .tocbuilder
import .raml2html

# Initialize the raml2html package.
starter_call = '../scripts/npminstall.sh'
subprocess.call(starter_call)


class Envelope_RAML:
    '''
    A class for metadata envelopes.
    '''

    def __init__(self, body, docname=None, title=None, author=None, toc=None,
                 publish_date=None, categories=None, unsearchable=None,
                 content_id=None, layout_key=None, meta=None,
                 asset_offsets=None, next=None, previous=None, addenda=None,
                 deconst_config=None, per_page_meta=None):
        '''
        Initiate as a dictionary.
        '''
        the_envelope = {
            'body': self.body,
            'docname': self.docname,
            'title': self.title,
            'toc': self.toc,
            # NOTE: Not sure if any of these following ones will be used.
            'author': self.author,  # Doubt this appears in the RAML spec.
            'publish_date': self.publish_date,  # Ditto
            'categories': self.categories,  # Ditto
            'unsearchable': self.unsearchable,  # From deconst, or Sphinx?
            # TODO: Get these next ones figured out (from the Sphinx preparer)
            'content_id': self.content_id,
            'layout_key': self.layout_key,
            'meta': self.meta,
            'asset_offsets': self.asset_offsets,
            'next': self.next,
            'previous': self.previous,
            'addenda': self.addenda,
            'deconst_config': self.deconst_config,
            'per_page_meta': self.per_page_meta
        }
        return the_envelope

    # TODO: Figure out if this is actually necessary. It looks like the
    # Sphinx preparer is essentially creating it's own builder, which may
    # need this method to generate the JSON.
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

    def _populate_layout_key(self):
        '''
        Derive the "layout_key" from per-page or repository-wide configuration.
        '''
        default_layout = self.config.deconst_default_layout
        self.layout_key = self.per_page_meta.get(
            'deconstlayout', default_layout)

    def _populate_categories(self):
        '''
        Unify global and per-page categories.
        '''
        page_cats = self.per_page_meta.get('deconstcategories')
        global_cats = self.config.deconst_categories
        if page_cats is not None or global_cats is not None:
            cats = set()
            if page_cats is not None:
                cats.update(re.split("\s*,\s*", page_cats))
            cats.update(global_cats or [])
            self.categories = list(cats)

    def _populate_asset_offsets(self):
        '''
        Read stored asset offsets from the docwriter.
        '''
        self.asset_offsets = self.visitor.calculate_offsets()

    def _populate_content_id(self):
        '''
        Derive this envelope's content ID.
        '''
        self.content_id = derive_content_id(self.deconst_config, self.docname)

    def _override_title(self):
        '''
        Override the envelope's title if requested by page metadata.
        '''
        if 'deconsttitle' in self.per_page_meta:
            self.title = self.per_page_meta['deconsttitle']


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

# QUESTION: Does each page's envelope need to get placed separately? Currently,
# it's written to put each envelope inside of a larger envelope...
# TODO: Write each envelope to a new file in ENVELOPE_DIR.
# TODO: Review the code from the Sphinx preparer if anything should be copied.
