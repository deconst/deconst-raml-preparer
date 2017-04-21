# Deconst RAML Preparer
RAML :point_right: :wrench: :point_right: .json

:contstruction: Work in progress :construction:

The *deconst RAML preparer* builds [RAML](#) into custom JSON metadata
envelopes. It's intended to be used within a CI system to present content to
the rest of build pipeline.

## Running locally

To run the preparer locally, you'll need to install:

*   [Docker](https://docs.docker.com/installation/#installation) for your
    platform.

Once you have Docker set up, export any desired configuration variables and
run `deconst-preparer-raml.sh` with the absolute path to any RAML-based content
repository.

```bash
./deconst-preparer-raml.sh /absolute/path/to/content-repo
```

### Configuration

#### Environment variables

The following values may be present in the environment:

*   `CONTENT_ROOT` is a path containing RAML content to prepare.
    *Default: $(pwd)*
*   `ENVELOPE_DIR` is the destination directory for metadata envelopes.
    *Default: $(pwd)/_build/deconst-envelopes/*
*   `ASSET_DIR` is the destination directory for referenced assets.
    *Default: $(pwd)/_build/deconst-assets/*
*   `CONTENT_ID_BASE` is a prefix that's unique among the content repositories
    associated with the target deconst instance. Our convention is to use the
    base URL of the GitHub repository. *Default: Read from _deconst.json*
