#-*- coding: UTF-8 -*-
import sys
import platform
import random
import urllib.request as http

# if (platform.python_version()[0] == '2'):
#     import urllib2 as http
# else:
#     import urllib
#     http = urllib.request


userAgent = ["Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Monzilla/4.0", "FireFox/6.01", "Nokia7110/1.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"]

def request(url, headers, data = None):
    try:
        userAgentIndex = random.randrange(0, len(userAgent))
        headers["User-Agent"] = userAgent[userAgentIndex]
        req = http.Request(url = url, headers = headers, data = data)
        content = http.urlopen(req, timeout = 10).read()
        return content
    except Exception as ex:
        print(ex)
        return None
