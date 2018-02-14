import re
import urllib.request as request

baseurl = "http://www.istartedsomething.com/bingimages/"
picUrlHeader = "http://www.istartedsomething.com/bingimages/cache/"
pageurl = "http://www.istartedsomething.com/bingimages/?m=2&y=2016"
input("begin loop")
picUrls = set('')

def GetMonthlyPic(year, month):
	#print("Begin to get picture urls for " + str(year) + "." + str(month))
	url = baseurl + "?m=" + str(month) + "&y=" + str(year)
	try:
		content = request.urlopen(pageurl).read()
		temp = content.decode("utf-8")

		#picUrlBodys= re.findall('data-original="resize.php?i=(.*?)&w=100"', temp, re.S)
		picUrlBodys= re.findall('img class="lazy" data-original="resize.php\?i=(.*?)&w=100"', temp, re.S)
		for item in picUrlBodys:
			picUrl = picUrlHeader + item
			#picUrl = item
			picUrls.add(picUrl)
	except Exception as e:
		print(e)
		input()


def DownLoadAndSavePic(year, month):
	try:
		headers = {'Accept':'image/webp,*/*;q=0.8', 'Accept-Encoding':'gzip,deflate,sdch', 'Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}
		index = 1
		tempList = list(picUrls)
		for picUrl in tempList:
			print("now downloading: " + picUrl)
			req = request.Request(url = picUrl, headers = headers)
			content = request.urlopen(req).read()
			fp = open('pic\\bingPic\\' + str(year) + "_" + str(month) + "_" + str(index)+'.jpg', 'wb')
			fp.write(content)
			fp.close()
			index += 1
			if index > 20:
				break
	except Exception as e:
		print(e)
	


try:
	year = 2016
	largeMonth = 9
	for mon in range(1, largeMonth + 1):
		picUrls = set('')
		GetMonthlyPic(year, mon)
		print("Get picture url for year: " + str(year) + ", month: " + str(mon) + ", total number: " + str(len(picUrls)))
		DownLoadAndSavePic(year, mon)
		print("download finish..")

	input()
except Exception as e:
	print(e)






















