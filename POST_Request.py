#!/bin/bash/env python3

import urllib.parse
import urllib.request

url = 'http://Target URL Here'
info = {'user': 'hacker', 'password': 'password1234'}
data = urllib.parse.urlencode(info).encode() # Data is now of type bytes

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:  # POST
    content = response.read()

print(content)