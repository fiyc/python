#-*- coding: UTF-8 -*-
import sys
import os
sys.path.append("/Users/yif/Documents/code/python")
import re
from bs4 import BeautifulSoup
import urllib.request as http
from urllib.request import urlretrieve
import random
import jseval as je

import time

import json
# from library import fiyc_http

baseUrl = 'http://www.chuixue.net'

comic_args = sys.argv
if (len(comic_args) == 1):
    # os._exit(0)
    id = "7660"
    desc = "绿野仙踪"
else:
    id = comic_args[1]
    desc = str(comic_args[2])
#id=26798 ## 一人之下
#id=26754 ## 食色大陆

print('begin to get ' + desc + ', id: ' + id)


def SaveFile(filepath, content, editModel):
    fs = open(filepath, editModel)
    fs.write(content)
    fs.close()


userAgent = [
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Monzilla/4.0",
    "FireFox/6.01", "Nokia7110/1.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
]


def request(url, headers, data=None):
    try:
        sleeptime = random.randrange(1, 3)
        time.sleep(sleeptime)
        userAgentIndex = random.randrange(0, len(userAgent))
        headers["User-Agent"] = userAgent[userAgentIndex]
        req = http.Request(url)
        content = http.urlopen(req).read()  #.decode('gbk')
        # content = bytes.decode(content)
        return content
    except Exception as ex:
        print(ex)
        return None


result = request(baseUrl + '/manhua/' + str(id), {})
result = result.decode('gbk')
soup = BeautifulSoup(result)
chapterdiv = soup.findAll(id='play_0')[0]
links = chapterdiv.findAll(name='a')

finaloutput = {}

for item in links:
    detailurl = baseUrl + item.attrs['href']
    title = item.attrs['title']

    matchRes = re.search(r'[0-9]{1,3}', title)
    if (not matchRes):
        continue

    begin = matchRes.regs[0][0]
    end = matchRes.regs[0][1]
    title = title[begin:end]

    # if(int(title) < 218):
    # 	break

    # print("开始获取地址: " + detailurl + " 的页面信息...")
    print('begin to get the ' + title + 'detail info from url: ' + detailurl)
    detailPage = request(detailurl, {})
    detailPage = detailPage.decode('gbk')

    imagestr = re.findall('photosr(.*?);var maxpages', str(detailPage))

    if (imagestr == None or len(imagestr) <= 0):
        # print('页面为获取到图片地址信息...')
        # print('can not get the image info')
        decodeStr = re.findall('packed=(.*?);eval', str(detailPage))
        urls = je.getImageUrls(decodeStr[0])

        urls = urls.split(';')

        for index in range(0, len(urls)):
            url = urls[index]

            if (url == ''):
                continue

            indexKey = ''
            if (index > 9):
                indexKey = str(index)
            else:
                indexKey = '0' + str(index)
            key = title + '_' + indexKey
            finaloutput[key] = 'http://img.81txt.com/' + url
    else:
        urls = imagestr[0].split(';')

        for index in range(0, len(urls)):
            indexKey = ''
            if (index > 9):
                indexKey = str(index)
            else:
                indexKey = '0' + str(index)
            key = title + '_' + indexKey
            url = re.findall('"(.*?)"', urls[index])
            finaloutput[key] = 'http://img.81txt.com/' + url[0]

print('All image urls ready...')

outputData = {}
outputData["id"] = id
outputData["name"] = desc
outputData["data"] = finaloutput

outputJson = json.dumps(outputData)
# print(outputJson)
outputPath = '/Users/yif/Documents/code/front-end/comic-book/data-source/' + str(
    id) + '.json'
SaveFile(outputPath, outputJson, 'w')

# headers = {'Accept':'image/webp,*/*;q=0.8', 'Accept-Encoding':'gzip,deflate,sdch', 'Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}
# for each in finaloutput:
# 	try:
# 		image_url = finaloutput[each]
# 		print('downloading the image: ' + each + ', url: ' + image_url)
# 		filePath = '/Users/yif/Downloads/YRZX/' + each + '.jpg'
# 		urlretrieve(image_url, filePath)
# 	except Exception as ex:
# 		print(ex)

# image_content = request(image_url, headers)

# print('开始下载图片: ' + each + ',  地址: ' + image_url)

# SaveFile(filePath, image_content.decode('utf8'), 'w')
