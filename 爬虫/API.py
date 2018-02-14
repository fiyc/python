# -*- coding: utf-8 -*-
import sys
import urllib
import urllib.request as request
import json

url = 'http://apis.baidu.com/txapi/mvtp/meinv?num=10'
#url = 'http://apis.baidu.com/dajuncloud/goddess/goddesses?tuid=3'

req = request.Request(url)

req.add_header("apikey", "3c3f3c0b49822486cbc5ed425fbf4b1f")

resp = request.urlopen(req)
content = resp.read()
content = bytes.decode(content)
print(content)
data = json.loads(bytes.decode(content))
fb = open("result.xml", 'ab')
for item in data["newslist"]:
	title = "title: %s" % item["title"]
	description = "description: %s" % item["description"]
	webUrl = "url: %s" % item["url"]
	picUrl = "picUrl: %s" % item["picUrl"]
	writeContent = "%s \n %s \n %s \n %s \n \n \n" % (title, description, webUrl, picUrl)
	fb.write(str.encode(writeContent))
fb.close()
# fb = open("result.xml", 'wb')
# fb.write(content)
# fb.close()

