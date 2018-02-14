#-*- coding: UTF-8 -*-
import urllib.request as request
import xml.dom.minidom 

def GetAndSaveResult(url, savePath, isLocal):
	result = ""
	if(isLocal):
		result = "<root><doc><name>Test</name></doc><doc><name>Test</name></doc><doc><name>Test</name></doc><doc><name>Test</name></doc><doc><name>Test</name></doc></root>"
	else:
		result = request.urlopen(url).read()
		print(result)

	result = bytes(result, encoding="utf8")
	fp = open(savePath, 'wb')
	fp.write(result)
	fp.close()
	return result
	
try:
	url = "http://apis.baidu.com/apistore/idservice/id?id=320586199204022950&apikey=3c3f3c0b49822486cbc5ed425fbf4b1f"
	result = GetAndSaveResult(url, 'result.xml', False)
	domTree = xml.dom.minidom.parse('result.xml')

	data = domTree.documentElement
	hotels = data.getElementsByTagName("doc")

	logfp = open("log.txt", 'wb')
	for hotel in hotels:
		#hotelEst = hotel.getElementsByTagName("est")[0]
		hotelName = hotel.getElementsByTagName("name")[0]
		hotelName = "酒店酒店名:  %s \n" % hotelName.firstChild.data
		logfp.write(bytes(hotelName, encoding="utf8"))
		# logfp.write("酒店设施:  %s \n" % hotelEst)
		logfp.write(b"================================== \n")

	logfp.close()
	input()
except Exception as e:
	print(e)
	# logfp = open("log.txt", 'wb')
	# logfp.write(e)
	# logfp.close()
	# input()