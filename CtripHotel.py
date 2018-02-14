# -*- coding: utf-8 -*-
try:
	import yifLibrary.HttpHelper as HttpHelper
	import yifLibrary.IOHelper as IOHelper


	url = "http://hotels.ctrip.com/international/996628.html"
	htmlResult = HttpHelper.GetRequestFromServer(url)
	print(type(htmlResult))
	IOHelper.SaveFile("cTrip.html", htmlResult, 'wb')
except Exception as e:
	print e

input()

