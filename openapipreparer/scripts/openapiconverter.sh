#! /bin/sh

file_json=$1
output_html=$2
template_path=$3
## TODO Should try it out with template tag -t.
java -jar /preparer/openapi-generator-cli-3.1.1.jar generate -i $file_json -g html -o $output_html