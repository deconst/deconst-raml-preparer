#! /bin/sh

file_raml=$1
output_html=$2
template_path=$3
raml2html $file_raml > $output_html --template $template_path
