#! /bin/bash

npm install raml2html
raml2html ../../tests/tester.raml > ../../tests/tester-raw.html --template ../../tests/nunjucks/index.nunjucks
