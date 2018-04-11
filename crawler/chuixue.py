#-*- coding: UTF-8 -*-
import sys
import os
sys.path.append("/Users/yif/Documents/code/python")
import re
from bs4 import BeautifulSoup
import urllib.request as http
import random
import jseval as je
# from library import fiyc_http 

baseUrl='http://www.chuixue.net'
id=26798


def SaveFile(filepath, content, editModel):
	fs = open(filepath, editModel)
	fs.write(content)
	fs.close()

userAgent = ["Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Monzilla/4.0", "FireFox/6.01", "Nokia7110/1.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"]

def request(url, headers, data = None):
	try:
		userAgentIndex = random.randrange(0, len(userAgent))
		headers["User-Agent"] = userAgent[userAgentIndex]
		req = http.Request(url)
		content = http.urlopen(req).read().decode('gbk')
		# content = bytes.decode(content)
		return content
	except Exception as ex:
		print(ex)
		return None





result = request(baseUrl+ '/manhua/' + str(id), {})
print(result)
soup = BeautifulSoup(result)
chapterdiv = soup.findAll(id='play_0')[0]
links = chapterdiv.findAll(name='a')

finaloutput = {}

for item in links:
	detailurl = baseUrl + item.attrs['href']
	title = item.attrs['title']

	if(not re.match(r'^[0-9]{1,3}$', title)):
		continue
		
	# print("开始获取地址: " + detailurl + " 的页面信息...")
	print('begin to get the detail info from url: ' + detailurl)
	detailPage = request(detailurl, {});	

	imagestr = re.findall('photosr(.*?);var maxpages', str(detailPage))

	if(imagestr == None or len(imagestr) <= 0):
		# print('页面为获取到图片地址信息...')
		print('can not get the image info')
		decodeStr = re.findall('packed=(.*?);eval', str(detailPage))
		urls = je.getImageUrls(decodeStr[0])

		for index in range(0, len(urls)):
			indexKey = ''
			if(index > 9):
				indexKey = str(index)
			else:
				indexKey = '0' + str(index)
			key = title + '_' + indexKey
			finaloutput[key] = 'http://img.81txt.com/'+ url[0]
	else:
		urls = imagestr[0].split(';')

		for index in range(0, len(urls)):
			indexKey = ''
			if(index > 9):
				indexKey = str(index)
			else:
				indexKey = '0' + str(index)
			key = title + '_' + indexKey
			url = re.findall('"(.*?)"', urls[index]) 
			finaloutput[key] = 'http://img.81txt.com/'+ url[0]
	

print('All image urls ready...')

headers = {'Accept':'image/webp,*/*;q=0.8', 'Accept-Encoding':'gzip,deflate,sdch', 'Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}
for each in finaloutput:
	image_url = finaloutput[each]	
	image_content = request(image_url, headers)

	# print('开始下载图片: ' + each + ',  地址: ' + image_url)
	print('downloading the image: ' + each + ', url: ' + image_url)

	filePath = '/Users/yif/Downloads/YRZX/' + each + '.jpg'
	SaveFile(filePath, image_content, 'w')




	







