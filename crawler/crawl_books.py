#-*- coding: UTF-8 -*-
import re
# import urllib2 as request
import urllib.request as request
import sys
import os
import time
import random

# 定义初始类型页面地址
baseUrl = "https://www.liukuquanshu.com/b/14695mdcs_syjxj/"
outputFile = "14695.txt"
begin = 1
end = 3000


chapters = []


class chapterInfo:
	chapterName = ''
	chapterUrl = ''

	def __init__(self, name, url):
		self.chapterName = name
		self.chapterUrl = url


'''
获取指定url返回信息
'''
userAgent = ["Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Monzilla/4.0", "FireFox/6.01", "Nokia7110/1.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"]
def GetRequestFromServer(url, headers = {}, data = None):
	try:
		time.sleep(1)
		userAgentIndex = random.randrange(0, len(userAgent))
		# headers = {"User-Agent": userAgent[userAgentIndex],  
        #    "Host":"www.java1234.com"}
		req = request.Request(url = url, headers = headers, data = data)
		content = request.urlopen(req, timeout = 10).read()
		# print(url + "成功")
		return content
	except Exception as e:
		print(url + "异常")
		print(e)

def SaveFile(filepath, content, editModel):
	fs = open(filepath, editModel)
	fs.write(content)
	fs.close()

def GetChapterContentAndSave(filepath, chapterInfo):
    try:
        chapterUrl = baseUrl + chapterInfo.chapterUrl
        chapterContent = ''
        
        getContent = False
        retryIndex = 0
        while(not getContent and retryIndex < 3):
            try:
                chapterContent = GetRequestFromServer(chapterUrl).decode('gbk')
                getContent = True
            except Exception as e:
                retryIndex = retryIndex + 1
                print(chapterInfo.chapterName + "第" + str(retryIndex) + "次爬取失败")


        if(chapterContent == '' or chapterContent == None):
            return


        box_box = re.findall('<div class="box_box">([\s\S]*?)</div>', chapterContent)
        content = re.findall('</script>([\s\S]*?)<script type="text/javascript">', box_box[0])
        content = re.sub(r'<br /><br />', '\r\n', content[0])

        filepath = filepath + '_' + str(begin) + '_' + str(end)
        fs = open(filepath, 'a+')
        fs.write('\r\n\r\n=====')
        fs.write(chapterInfo.chapterName)
        fs.write('=====\r\n')
        fs.write(content)
        fs.close()
        print(chapterInfo.chapterName + "    爬取完成")
    except Exception as e:
        print(e)






try:
    begin = 1
    end = 3000
    if(len(sys.argv) > 2):
        begin = int(sys.argv[1])
        end = int(sys.argv[2])



    chapterTree = GetRequestFromServer(baseUrl).decode('gbk')
    chapterListStr = re.findall('<div class="list_box">(([\s\S]*?)*?)</div>', chapterTree)
    chapterList = re.findall('<a href="(.*?)">(.*?)</a>', chapterListStr[0][0])

    index = 0
    for url, name in chapterList:
        index = index + 1

        if(index < begin):
            continue

        if(index > end):
            break

        chapters.append(chapterInfo(name, url))

    for item in chapters:
        GetChapterContentAndSave(outputFile, item)
        
except Exception as e:
	print(e)





