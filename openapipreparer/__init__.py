# -*- coding: utf-8 -*-

# Modified from the Sphinx preparer's __init__.py file and RAML preparer's __init__.py

import os
import sys
import re

try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

from pprint import pprint

DECONST_FILE = "_deconst.json"

sys.path.insert(0, os.getcwd())

from openapipreparer.deconstopenapi import enveloper, submit, find_all
from openapipreparer.config import Configuration

__author__ = 'Laura Santamaria, Madhusudan Sridharan'
__email__ = 'laura.santamaria@rackspace.com, madhu.sridharan@rackspace.com'
__version__ = '0.1.0'


def main(directory=False):

    config = Configuration(os.environ)

    if config.content_root:
        if directory and directory != config.content_root:
            print("Warning: Overriding CONTENT_ROOT [{}] with argument [{}].".format(
                config.content_root, directory))
        else:
            os.chdir(config.content_root)
            # print(os.getcwd())
    elif directory:
        os.chdir(directory)
        # print(os.getcwd())

    if os.path.exists(DECONST_FILE):
        config.apply_file(DECONST_FILE)

    # Ensure that the envelope and asset directories exist.
    os.makedirs(config.envelope_dir, exist_ok=True)
    os.makedirs(config.asset_dir, exist_ok=True)

    # Install pip requirements when possible.
    install_requirements()

    the_list = find_all(config)
    for path_name in the_list:
        file_name = os.path.basename(path_name)
        # html_name = file_name.replace('json', 'html')
        # base_location = os.path.join(config.envelope_dir, html_name)
        
        each_envelope = enveloper(path_name, config.envelope_dir)
        submit(each_envelope)
    # TODO: Clear out intermediate .html in envelope dir
    # regex_clear = re.compile('.*(\.html)$')
    # directoryname = os.path.join(config.envelope_dir, 'temp', '')
    # for anyfile in directoryname:
    #     if re.search(regex_clear, anyfile):
    #         os.remove(os.path.join(directoryname, anyfile))

# TODO: Implement some sort of nice exit status. I'm thinking of using
# try/except...

    # status = deconstraml.build_all(config)
    # if status != 0:
    #     sys.exit(status)

    # reasons = config.missing_values()
    # if reasons:
    #     print("Not preparing content because:", file=sys.stderr)
    #     print(file=sys.stderr)
    #     for reason in reasons:
    #         print(" * " + reason, file=sys.stderr)
    #     print(file=sys.stderr)
    #     sys.exit(1)


def install_requirements():
    """
    Install non-colliding dependencies from a "requirements.txt" file found at
    the content root.
    """

    reqfile = None
    if os.path.exists('deconst-requirements.txt'):
        reqfile = 'deconst-requirements.txt'
    elif os.path.exists('requirements.txt'):
        reqfile = 'requirements.txt'
    else:
        return

    dependencies = []

    with open(reqfile, 'r', encoding='utf-8') as rf:
        for line in rf:
            if line.startswith('#'):
                continue

            stripped = line.strip()
            if not stripped:
                continue

            dependencies.append(stripped)

    print("Installing dependencies from {}: {}.".format(
        reqfile, ', '.join(dependencies)))
    pipmain(['install'] + dependencies)


if __name__ == '__main__':
    main()
