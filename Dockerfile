#FROM alpine:latest
FROM openapitools/openapi-generator-online

LABEL maintainer="laura.santamaria@rackspace.com"

RUN apk update && apk add --no-cache python3 git nodejs
# nodejs-npm

RUN python3 -m ensurepip
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip3 install --upgrade pip \
  && pip3 install virtualenv
#RUN npm install --global raml2html

RUN adduser -D -g "" -u 1000 preparer
RUN mkdir -p /preparer /venv /usr/content-repo
RUN chown -R preparer:preparer /preparer /venv
ENV PYTHONPATH /preparer

RUN virtualenv /venv
ENV PATH /venv/bin:${PATH}

COPY ./requirements.txt /preparer/requirements.txt
RUN pip3 install -r /preparer/requirements.txt
COPY . /preparer

VOLUME /usr/content-repo
WORKDIR /preparer
RUN wget http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/3.1.1/openapi-generator-cli-3.1.1.jar -O /preparer/openapi-generator-cli-3.1.1.jar

RUN python3 setup.py install

USER preparer

# TODO: Consider putting the git command logic out here and passing to Python.
# Should be a lot simpler and avoids dependencies (and allows for other VCS
# types as we could abstract this out to code in the repo itself).
CMD ["python3", "-m", "openapipreparer"]
#RUN python3 /preparer/tests/test_asset_mapper.py