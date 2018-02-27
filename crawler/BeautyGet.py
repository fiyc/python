# -*- coding: utf-8 -*-
import yifLibrary.HttpHelper as HttpHelper
import yifLibrary.IOHelper as IOHelper
import re
import yifLibrary.Model as Model


url = "http://m.xxxiao.com/"
rootPath = "xxxiao"

# 获取首页标题链接集合
htmlResult = HttpHelper.GetRequestFromServer(url)
htmlResult = str(htmlResult, encoding = "utf-8") 
primaryMenuTempStr = re.findall('<ul id="mega-menu-primary" (.*?)</ul>', htmlResult)[0]
primaryMenus = re.findall('<a class="mega-menu-link" href="(.*?)" tabindex="0">(.*?)</a>', primaryMenuTempStr)
primaryMenuLinks = []
for item in primaryMenus:
	if(item[1] == "最新美女" or item[1] == "女神笑了"):
		continue
	itemLink = Model.LinkInfo(item[0], item[1])
	itemLink.Path = rootPath + "\\" + item[1]
	primaryMenuLinks.append(itemLink)

	IOHelper.MakeDir(itemLink.Path)



#遍历标题栏链接，获取每个标题下的图片标题
peopleLinks = []
for item in primaryMenuLinks:
	secondHtmlResult = HttpHelper.GetRequestFromServer(item.Url)
	secondHtmlResult = str(secondHtmlResult, encoding = "utf-8") 
	eachPeoples = re.findall('<h2 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h2>', secondHtmlResult)

	for people in eachPeoples:
		peopleLink = Model.LinkInfo(people[0], people[1])
		peopleLink.Path = item.Path + "\\" + people[1]
		peopleLinks.append(peopleLink)
		IOHelper.MakeDir(peopleLink.Path)


#遍历每个人物下的图片，获取链接信息
picLinks = []
for item in peopleLinks:
	peopleHtmlResult = HttpHelper.GetRequestFromServer(item.Url)
	peopleHtmlResult = str(peopleHtmlResult, encoding = "utf-8") 
	eachPic = re.findall('class="attachment-medium size-medium" alt="" srcset="(.*?)" size', peopleHtmlResult)

	index = 1
	for picUrls in eachPic:
		urls = re.findall('http:(.*?)jpg',picUrls)
		urlContent = urls[len(urls) - 1]
		picUrl = 'http:%sjpg' % urlContent
		picPath = item.Path + "\\" +  str(index) + ".jpg"
		index = index + 1
		picInfo = Model.LinkInfo(picUrl, "")
		picInfo.Path = picPath
		picLinks.append(picInfo)

print("获取所有图片信息成功，开始写入文件...")
fs = open("pics.txt", 'w')
for pic in picLinks:
	message = pic.Url + "|||" + pic.Path + "\n"
	fs.write(message)
fs.close()

print("图片信息写入成功!开始下载图片...")
downloadNum = 1
for pic in picLinks:
	content = HttpHelper.GetRequestFromServer(pic.Url, HttpHelper.DEFAULT_HEADER)
	IOHelper.SaveFile(pic.Path, content, 'wb')
	print("第" + str(downloadNum) + "张下载完成。。")
	downloadNum = downloadNum + 1

print("图片下载完成！")

# print(primaryMenus)
# htmlResult = str(htmlResult, encoding = "utf-8")  
# print(htmlResult)