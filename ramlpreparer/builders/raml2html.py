#! /usr/bin/env python

import ramlfications
# TODO: Replace psuedocode

api_doc = "/Users/laur0616/testRAMLcase/api.raml"
apiDict = {}
responseDict = {}
resourceList = []
n = 0
x = 0

parsed = ramlfications.parse(api_doc)

apiDict['title'] = parsed.title
apiDict['version'] = parsed.version
apiDict['documentation'] = parsed.documentation
apiDict['baseUri'] = parsed.base_uri

for item in parsed.resources:
    resourceList.append(item)

for item in resourceList:
    apiDict_sub = {}
    apiDict_sub['name'] = item.name
    apiDict_sub['display_name'] = item.display_name
    apiDict_sub['description'] = item.description
    apiDict_sub['methods'] = item.method
    apiDict_sub['URI'] = item.uri_params
    for response in item.responses:
        responseDict_sub = {'response_to':item.name}
        responseDict_sub['response_code'] = response.code
        responseDict_sub['response_method'] = response.method
        responseDict_sub['response_description'] = response.description
        responseDict_sub['response_body'] = response.body
        responseDict[x] = responseDict_sub
        x += 1
    apiDict_sub['responses'] = responseDict
    apiDict[n] = apiDict_sub
    n += 1

readable = '\n'.join(['%s:: %s' % (key, value) for (key, value) in apiDict.items()])
#print(readable)

def htmlIt(item):
    protoHtml = '<div id="%(key1)s" class="section">\n<h2>%(key2)s<a title="Permalink to this headline" href="#%(key3)s" class="headerlink">#</a></h2>\n<div class="code highlight-default"><div class="highlight"><pre>%(key4)s</pre></div></div>\n<p>%(key5)s</p>\n<p>This table shows the possible response codes for this operation:</p>\n<table border="1" class="docutils">\n<colgroup>' % item
    return protoHtml

testDict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}

print(htmlIt(testDict))

#\n<col width="33%">\n<col width="33%">\n<col width="33%">\n</colgroup>\n<thead valign="bottom">\n<tr class="row-odd">\n<th class="head">Response Code</th>\n<th class="head">Name</th>\n<th class="head">Description</th>\n</tr>\n</thead>\n<tbody valign="top">\n<tr class="row-even">\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n<tr class="row-odd">\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n</tbody>\n</table>\n<div id="request" class="section">\n<h3>Request<a title="Permalink to this headline" href="#request-%s" class="headerlink">#</a></h3>\n<p>This table shows the body parameters for the request:</p>\n<table border="1" class="docutils">\n<colgroup>\n<col width="53%">\n<col width="17%">\n<col width="29%">\n</colgroup>\n<thead valign="bottom">\n<tr class="row-odd">\n<th class="head">Name</th>\n<th class="head">Type</th>\n<th class="head">Description</th>\n</tr>\n</thead>\n<tbody valign="top">\n<tr class="row-even">\n<td>%s.<strong>%s</strong></td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n<tr class="row-odd">\n<td>%s.<strong>%s</strong></td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n</tbody>\n</table>\n<p><strong>Example %s: %s request</strong></p>\n<div class="code highlight-default">%s</div>\n</div>\n<div id="response" class="section">\n<h3>Response<a title="Permalink to this headline" href="#response-%s" class="headerlink">#</a></h3>\n<p>This table shows the body parameters for the response:</p>\n<table border="1" class="docutils">\n<colgroup>\n<col width="36%">\n<col width="32%">\n<col width="32%">\n</colgroup>\n<thead valign="bottom">\n<tr class="row-odd">\n<th class="head">Name</th>\n<th class="head">Type</th>\n<th class="head">Description</th>\n</tr>\n</thead>\n<tbody valign="top">\n<tr class="row-even">\n<td><strong>%s</strong></td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n<tr class="row-odd">\n<td>%s.<strong>%s</strong></td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n</tbody>\n</table>\n<p><strong>Example %s: %s response</strong></p>\n<div class="code highlight-default">%s</div>\n</div>\n<div class="code highlight-default">%s</div>\n</div>
