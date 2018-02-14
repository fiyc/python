import re
import urllib.request as request

baseUrl = 'http://manhua.dmzj.com/xlzm'
chapterUrls = set('')
picUrls = set('')



def GetUrlContent(url):
	try:
		content = request.urlopen(url).read()
		temp = content.decode("utf-8")
		return temp
	except Exception as e:
		print(e)
		input()	
		return ''

def GetChapterUrl():
	try:
		url = baseUrl
		content = GetUrlContent(url)
		urlList = re.findall('<a title="修罗之门*" href="(.*?)">', content, re.S)
		fp = open('catroon\\chapterUrls.txt', 'a')
		for detailUrl in urlList:
			temp = baseUrl + detailUrl
			chapterUrls.add(temp)
			fp.write(temp+'\n')

		fp.close()
	except Exception as e:
		print(e)
		input()	


def run():
	try:
		#获取所有章节地址
		GetChapterUrl()

		#遍历每个章节
		chapterList = list(chapterUrls)
		chapterList.sort()
		for chapterUrl in chapterList:
			content = GetUrlContent(chapterUrl)
			#获取当前章节图片数
			pagePart = re.findall('<select name="select" id="page_select" onchange="select_page()">(.*?)</select>', content, re.S)[0]
			pageNum = re.findall('>第(.*?)页</option>', pagePart, re.S)
			largePage = int(len(pageNum))	
			print(chapterUrl + " : " + str(largePage))
			#遍历每一页
			for index in range(1, largePage + 1):
				tempUrl = chapterUrl + '#@page=' + str(index)
				print(tempUrl)
				detailContent = GetUrlContent(tempUrl)
					

				print(detailContent)
				picUrlPart = re.findall('<div id="center_box"(.*?)</div>', detailContent, re.S)[0]
				picUrl = re.findall('<img src="(.*?)" name', picUrlPart, re.S)[0]
				picUrls.add(picUrl)


			#将图片地址存入文件
			fp = open('catroon\\picUrls.txt', 'a')
			for item in picUrls:
				fp.write(item+'\n')
			fp.close()
	except Exception as e:
		print(e)
		input()
	



run()