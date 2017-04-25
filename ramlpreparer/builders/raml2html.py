#! /usr/bin/env python

import ramlfications
# TODO: Replace psuedocode

api_doc = "/Users/laur0616/testRAMLcase/api.raml"
apiDict = {}
resourceList = []
n = 0

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
    apiDict_sub['responses'] = item.responses
    apiDict[n] = apiDict_sub
    n += 1

print(apiDict)

# <div id="title">
#   <h2>display_name</h2>
#   <div class='code'></div>
#   <p>description</p>
#
