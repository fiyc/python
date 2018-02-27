import re
import urllib.request as request

baseUrl = 'http://www.1kkk.com/'
bookTitle = 'manhua1328'
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
		url = baseUrl + bookTitle
		content = GetUrlContent(url)
		liListContent = re.findall('<ul class="sy_nr1 cplist_ullg">(.*?)</ul>', content, re.S)[1]
		urlList = re.findall('<a href="(.*?)" class="tg"', liListContent, re.S)
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
			pagePart = re.findall('<font class="zf40">(.*?)</font>', content, re.S)[0]
			pageNum = re.findall('<span>(.*?)</span>', pagePart, re.S)[0]
			largePage = int(pageNum)	
			print(chapterUrl + " : " + str(largePage))
			#遍历每一页
			for index in range(1, largePage + 1):
				detailContent = ''
				if index == 1:
					detailContent = content
				else:
					tempUrl = chapterUrl + '#ipg' + str(index)
					print(tempUrl)
					detailContent = GetUrlContent(tempUrl)

				print(detailContent)
				picUrl = re.findall('<img id="cpimg" src="(.*?)"', detailContent, re.S)[0]
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