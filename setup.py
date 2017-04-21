#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Get rid of the copy-pasta...

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

# TODO: implement changelog
#with open('HISTORY.rst') as history_file:
#    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

#setup(
#    name='deconst-raml-preparer',
#    version='0.1.0',
#    description="Build RAML-based documentation to JSON and jam it in the cloud",
#    long_description=readme + '\n\n' + history,
#    author="Laura Santamaria",
#    author_email='laura.santamaria@rackspace.com',
#    url='https://github.com/nimbinatus/deconst-raml-preparer',
#    packages=[
#        'ramlpreparer',
#    ],
#    package_dir={'ramlpreparer':
#                 'deconst-raml-preparer'},
#    include_package_data=True,
#    install_requires=requirements,
#    license="Apache",
#    zip_safe=False,
#    keywords=[
#        'deconst',
#        'deconst-raml-preparer',
#    ],
#    classifiers=[
#        'Development Status :: 2 - Pre-Alpha',
#        'Intended Audience :: Developers',
#        'License :: OSI Approved :: BSD License',
#        'Natural Language :: English',
#        "Programming Language :: Python :: 2",
#        'Programming Language :: Python :: 2.7',
#        'Programming Language :: Python :: 3',
#        'Programming Language :: Python :: 3.6',
#    ],
#    test_suite='tests',
#    tests_require=test_requirements
#)
