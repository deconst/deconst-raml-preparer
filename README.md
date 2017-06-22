# Deconst RAML Preparer
RAML :point_right: :wrench: :point_right: .json

[![Stability Rating](https://img.shields.io/badge/stability-in%20test-yellow.svg)](https://img.shields.io/badge/stability-in%20test-yellow.svg) [![Build Status](https://travis-ci.org/nimbinatus/deconst-raml-preparer.svg?branch=master)](https://travis-ci.org/nimbinatus/deconst-raml-preparer/)
[![Coverage Status](https://coveralls.io/repos/github/nimbinatus/deconst-raml-preparer/badge.svg)](https://coveralls.io/github/nimbinatus/deconst-raml-preparer?branch=master)

:construction: Work in progress :construction:

The *deconst RAML preparer* builds [RAML 1.0](http://raml.org/) into custom JSON metadata envelopes. It's intended to be used within a CI system to present content to the rest of build pipeline.

This preparer is part of [deconst](https://github.com/deconst), an end-to-end documentation delivery system.

## Testing

Currently, the Docker image needs to be build manually as it is not yet up on quay.io or another Docker image library. Change into your clone of this repo and run the following command to build the image:

```bash
docker build . --no-cache --tag deconstramlpreparer:latest
```

## Running locally

To run the RAML preparer locally, you'll need to install:

*   [Docker](https://docs.docker.com/installation/#installation) for your platform.

Once you have Docker set up, export any desired configuration variables and run `deconst-preparer-sphinx.sh` with the absolute path to any RAML-based content repository.

```bash
./deconst-preparer-raml.sh /absolute/path/to/content-repo
```

## Configuration

### Environment variables

The following values may be present in the environment:

*   `CONTENT_ROOT` is a path containing RAML content to prepare. *Default: $(pwd)*
*   `ENVELOPE_DIR` is the destination directory for metadata envelopes. *Default: $(pwd)/_build/deconst-envelopes/*
*   `ASSET_DIR` is the destination directory for referenced assets. *Default: $(pwd)/_build/deconst-assets/*
*   `CONTENT_ID_BASE` is a prefix that's unique among the content repositories associated with the target deconst instance. Our convention is to use the base URL of the GitHub repository. *Default: Read from _deconst.json*

### Build system

By default, the preparer uses the [raml2html](https://github.com/raml2html) library to generate HTML from RAML and then uses Python to translate those HTML files to JSON envelopes. No configuration options are available outside of the RAML pages themselves at this time.
