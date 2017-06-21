# -*- coding: utf-8 -*-

# Modified from the Sphinx preparer's __init__.py file

import os
import sys

from pip import pip
import ramlpreparer.deconstraml as deconstraml
from ramlpreparer.config import Configuration

__author__ = 'Laura Santamaria'
__email__ = 'laura.santamaria@rackspace.com'
__version__ = '0.1.0'


def main(directory=False):

    config = Configuration(os.environ)

    if config.content_root:
        if directory and directory != config.content_root:
            print("Warning: Overriding CONTENT_ROOT [{}] with argument [{}].".format(
                config.content_root, directory))
        else:
            os.chdir(config.content_root)
    elif directory:
        os.chdir(directory)

    if os.path.exists("_deconst.json"):
        with open("_deconst.json", "r", encoding="utf-8") as cf:
            config.apply_file(cf)

    # Ensure that the envelope and asset directories exist.
    os.makedirs(config.envelope_dir, exist_ok=True)
    os.makedirs(config.asset_dir, exist_ok=True)

    # Install pip requirements when possible.
    install_requirements()

    the_list = deconstraml.find_all(config)
    for path_name in the_list:
        file_name = os.path.basename(path_name)
        html_name = file_name.replace('raml', 'html')
        base_location = path.join(config.envelope_dir, 'temp', html_name)
        each_envelope = deconstraml.enveloper(path_name, base_location)
        deconstraml.submit(each_envelope)
    # shutil.rmtree(os.chdir(os.path.join(config.envelope_dir, 'temp', '')))

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
    pip.main(['install'] + dependencies)


if __name__ == '__main__':
    main()
