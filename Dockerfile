FROM alpine:latest
LABEL maintainer="laura.santamaria@rackspace.com"

RUN apk update && apk add --no-cache python3 git nodejs nodejs-npm
RUN python3 -m ensurepip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip

RUN adduser -D -g "" -u 1000 preparer
RUN mkdir -p /preparer /venv /usr/content-repo
RUN chown -R preparer:preparer /preparer /venv
ENV PYTHONPATH /preparer

USER preparer

RUN pyvenv /venv
ENV PATH /venv/bin:${PATH}

COPY ./requirements.txt /preparer/requirements.txt
RUN pip install -r /preparer/requirements.txt
COPY . /preparer

VOLUME /usr/content-repo
WORKDIR /usr/content-repo

# TODO: Consider putting the git command logic out here and passing to Python.
# Should be a lot simpler and avoids dependencies (and allows for other VCS
# types as we could abstract this out to code in the repo itself).
CMD ["python", "-m", "ramlpreparer"]
