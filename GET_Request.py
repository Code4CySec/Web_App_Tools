#!/bin/bash/env python3

# HTTP GET Request

import urllib.parse
import urllib.request

url = 'http://Target URL Here'
with urllib.request.urlopen(url) as response:  # GET
    content = response.read()

print(content)