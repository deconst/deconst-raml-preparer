#! /bin/sh

file_raml=$1
output_html=$2
raml2html $file_raml > $output_html --template ../../tests/nunjucks/index.nunjucks
