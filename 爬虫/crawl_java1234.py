#-*- coding: UTF-8 -*-
'''
目标网站: http://www.java1234.com/

描述: 爬取目标网站上的电子书资源

分析:
	1. 电子书栏目分类地址:
		- http://www.java1234.com/a/javabook/javabase/ 65
		- http://www.java1234.com/a/javabook/database/ 66
		- http://www.java1234.com/a/javabook/javaweb/ 67
		- http://www.java1234.com/a/javabook/android/ 68
		- http://www.java1234.com/a/javabook/webbase/ 69
		- http://www.java1234.com/a/javabook/yun/ 115

	2. 进入分类页后为图书列表, 分页信息可以如下标签获取
		<span class="pageinfo">
			“共”
			<strong>xx</strong>
			“页”
			<strong>xx</strong>
			“条”
		</span>

	3. 分页请求地址为
		list_xx_yy.html
		xx为类型, 每一次进入页面后可以从第一页的链接处获取
		yy为页码信息


	4. 图书列表每页数据可以从如下html标签获取, 可获取图书名以及图书详情页
		$("div[class='listbox'] li a[class='title']")

	5. 进入详情页以后, 可以通过关键字"密码"前面的<a>来获取百度云盘链接, 以及后面的文件密码

	6. 该网站资源完全免费, 福利站. 爬取信息时需要控制频率.

'''

import re
import urllib2 as request
import sys
import os
import time
import random

# 定义初始类型页面地址
baseUrl = "http://www.java1234.com"
baseUrlDict = {}
baseUrlDict[65] = "http://www.java1234.com/a/javabook/javabase/"
baseUrlDict[66] = "http://www.java1234.com/a/javabook/database/"
baseUrlDict[67] = "http://www.java1234.com/a/javabook/javaweb/"
baseUrlDict[68] = "http://www.java1234.com/a/javabook/android/"
baseUrlDict[69] = "http://www.java1234.com/a/javabook/webbase/"
baseUrlDict[115] = "http://www.java1234.com/a/javabook/yun/"


bookUrls = {}

finalData = set()
class BookInfo:
	BookName = ''
	BaiduUrl = ''
	Password = ''

	def __init__(self,name,url,passwd):
		self.BookName = name
		self.BaiduUrl = url
		self.Password = passwd

'''
获取指定url返回信息
'''
userAgent = ["Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Monzilla/4.0", "FireFox/6.01", "Nokia7110/1.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"]
def GetRequestFromServer(url, headers = {}, data = None):
	try:
		time.sleep(1)
		userAgentIndex = random.randrange(0, len(userAgent))
		headers = {"User-Agent": userAgent[userAgentIndex],  
           "Host":"www.java1234.com"}
		req = request.Request(url = url, headers = headers, data = data)
		content = request.urlopen(req, timeout = 10).read()
		print(url + "成功")
		return content
	except Exception as e:
		print(url + "异常")
		print(e)

def SaveFile(filepath, content, editModel):
	fs = open(filepath, editModel)
	fs.write(content)
	fs.close()

'''
typeCode: 书籍分类code
baseUrl: 分类列表地址

获取当前类型下所有图书详情页地址信息的字典
'''
def GetBookDetailUrls(typeCode, baseUrl):
	result = {}
	# 列表页第一页信息
	indexContent = GetRequestFromServer(baseUrl);

	if(indexContent == None or indexContent == ""):
		return result

	pageInfoContent = re.findall('<span class="pageinfo">(.*?)</span>', indexContent)
	if(pageInfoContent == None or len(pageInfoContent) == 0):
		return result

	pageInfos = re.findall('<strong>(.*?)</strong>', pageInfoContent[0])


	if(pageInfos == None or len(pageInfos) == 0):
		return result

	totalPage = int(pageInfos[0])

	for index in range(1, totalPage):

		try:
			url = baseUrl + "list_" + str(typeCode) + "_" + str(index) + ".html"

			listPage = GetRequestFromServer(url);
			listDiv = re.findall('<div class="listbox">([\s\S]*?)</div>', listPage)

			if(listDiv == None or len(listDiv) == 0):
				continue

			bookInfos = re.findall('<a href="(.*?)" class="title">(.*?)</a>', listDiv[0]);

			for item in bookInfos:
				book = GetBookDetailInfo(item[1], item[0])

				if(book == None):
					continue

				fileResult = open('books.csv', 'a+')
				dataLine = "%s,%s,%s\n" % (book.BookName, book.BaiduUrl, book.Password)
				fileResult.write(dataLine);
				fileResult.close()
				# result[item[0]] = item[1]

			message = "获取 %s 类型图书 第 %d 页完成" % (str(typeCode), index)
			print(message)

		except Exception as e:
			message = "获取 %s 类型图书 第 %d 页出错" % (str(typeCode), index)
			print(message)



	return result

'''
bookName: 图书名
bookUrl: 图书详情页地址(不带域名)

获取图书的详细信息, 返回一个图书信息实体, 包括图书名, 图书百度云盘下载地址以及提取密码
'''
def GetBookDetailInfo(bookName, bookUrl):
	bookUrl = baseUrl + bookUrl
	pageContent = GetRequestFromServer(bookUrl)


	contentDiv = re.findall('<div class="content">([\s\S]*?)</div>', pageContent)

	if(contentDiv == None or len(contentDiv) == 0):
		return

	temp = re.findall('<strong>[\s\S]*密码[\s\S]*</strong>', contentDiv[0])

	if(temp == None or len(temp) == 0):
		return


	url = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>[\s\S]', temp[0])
	passwd = re.findall('<span style="color:#ff0000;">(.*?)</span>', temp[0])

	if(url == None or len(url) == 0):
		return

	if(passwd == None or len(passwd) == 0):
		return


	return BookInfo(bookName, url[0][0], passwd[0])








try:
	for key, value in baseUrlDict.items():
		currentDict = GetBookDetailUrls(key, value)
		# bookUrls.update(currentDict);

	# fileResult = open('books.csv', 'a+')

	# header = "图书名,百度地址, 密码\n"
	# fileResult.write(header)

	# for key, value in bookUrls.items():
	# 	try:
	# 		book = GetBookDetailInfo(value, key)
	# 		finalData.add(book)
	# 		dataLine = "%s,%s,%s\n" % (book.BookName, book.BaiduUrl, book.Password)
	# 		fileResult.write(dataLine);
	# 		message = "获取图书 %s 详细信息完成" % (book.BookName)
	# 		print(message)
	# 	except Exception as e:
	# 		message = "获取图书 %s 详细信息错误" % (book.BookName)
	# 		print(message)

	# fileResult.close()

except Exception as e:
	print(e)





