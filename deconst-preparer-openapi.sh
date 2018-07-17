#!/bin/bash
set -x
set -euo pipefail

CONTENT_ROOT=${1:-$(pwd)}

exec docker run \
  --rm=true \
  -e CONTENT_ID_BASE=${CONTENT_ID_BASE:-} \
  -e ENVELOPE_DIR=${ENVELOPE_DIR:-} \
  -e ASSET_DIR=${ASSET_DIR:-} \
  -e VERBOSE=${VERBOSE:-} \
  -e CONTENT_ROOT=/usr/content-repo \
  -v ${CONTENT_ROOT}:/usr/content-repo \
  deconstopenapiprepare
#  quay.io/deconst/preparer-raml ## to be used when it's all set
