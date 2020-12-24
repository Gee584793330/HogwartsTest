import urllib.request

response: object= urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())

import math
ma
