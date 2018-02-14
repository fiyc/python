import sys
if sys.version_info < (3, 0):
	import urllib2 as request
else:
	import urllib.request as request
	


DEFAULT_HEADER = {"Accept-Encoding": "gzip, deflate, sdch", 
					"Accept-Language":"zh-CN,zh;q=0.8", 
					"Connection":"keep-alive", 
					"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}



def GetRequestFromServer(url, headers = {}, data = None):
	req = request.Request(url = url, headers = headers, data = data)
	content = request.urlopen(req).read()
	return content



