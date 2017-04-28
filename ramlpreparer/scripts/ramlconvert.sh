#! /bin/sh

echo $output_html
raml2html $file_raml > $output_html --template ../../tests/nunjucks/index.nunjucks
