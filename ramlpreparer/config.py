#! usr/bin/env python3

# Modified from the Sphinx preparer's config.py file
# TODO: Clean up copy-pasta.

import json
import os
import subprocess
from os import path


def _normalize(url):
    '''
    Ensure that the argument ends with a trailing slash if it's nonempty.
    '''
    if url and not url.endswith("/"):
        return url + "/"
    else:
        return url


class Configuration:
    '''
    Configuration settings derived from the environment and current git
    branch.
    '''

    def __init__(self, env):
        self.content_root = env.get("CONTENT_ROOT", None)
        if not self.content_root:
            self.content_root = os.getcwd()
        self.content_id_base = _normalize(env.get("CONTENT_ID_BASE"))
        self.envelope_dir = env.get("ENVELOPE_DIR", None)
        if not self.envelope_dir:
            self.envelope_dir = path.join(
                self.content_root, '_build', 'deconst-envelopes')
        self.asset_dir = env.get("ASSET_DIR", None)
        if not self.asset_dir:
            self.asset_dir = path.join(
                self.content_root, '_build', 'deconst-assets')
        self.meta = {}
        self.github_url = ""
        self.github_branch = "master"
        try:
            self.git_root = self._get_git_root(os.getcwd())
        except FileNotFoundError:
            self.git_root = None

    def apply_file(self, f):
        '''
        Parse the contents of an open filehandle as JSON and apply
        recognized settings found there to this configuration.
        Environment variables take precedence over any values found here.
        '''
        with open(f, 'r') as deconst_file:
            doc = json.load(deconst_file)
        if "contentIDBase" in doc:
            if not self.content_id_base:
                self.content_id_base = _normalize(doc["contentIDBase"])
            elif self.content_id_base != _normalize(doc["contentIDBase"]):
                print("Using environment variable CONTENT_ID_BASE=[{}] "
                      "instead of _deconst.json setting [{}]."
                      .format(self.content_id_base, doc["contentIDBase"]))
        if "meta" in doc:
            self.meta = doc["meta"]
        if "githubUrl" in doc:
            self.github_url = doc["githubUrl"]
            self.github_issues_url = '/'.join(
                segment.strip('/') for segment in [doc["githubUrl"], 'issues'])
            self.meta.update({'github_issues_url': self.github_issues_url})
        if "githubBranch" in doc:
            self.github_branch = doc["githubBranch"]
        else:
            self.github_branch = "master"

    def _get_git_root(self, d):
        the_git_root = subprocess.Popen(
            ['git', 'rev-parse', '--show-toplevel'],
            stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
        if not the_git_root:
            raise FileNotFoundError('You\'re not in a git repo.')
            the_git_root = '/fake-root/'
        return the_git_root

    def missing_values(self):
        '''
        Determine whether or not the current build should result in the
        preparation of envelopes. If not, return a list of reasons why it
        won't.
        '''
        reasons = []
        if not self.content_id_base:
            reasons.append("CONTENT_ID_BASE is missing. It should be the base "
                           "URL used to generate IDs for content within this "
                           "repository.")
        return reasons

    @classmethod
    def load(cls, env):
        '''
        Derive the current configuration from the environment.
        '''
        return cls(env)
