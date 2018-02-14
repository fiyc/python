import re
import urllib.request as request

#f = open('source.txt', 'r', encoding='utf-8')
#html = f.read()
#f.close()

picid = '1'
baseurl = "http://www.meineihan.cc/diaosifuli/26313"
page = 16



url = ''
html = ''
for index in range(1, page):
	if index == 1:
		url = baseurl + '.html'
	else:
		url = baseurl + '_' + str(index) + '.html'
	content = request.urlopen(url).read()
	#html = html + str(content)
	fp = open('pic' + picid + '\\' + str(1) + '.txt', 'wb')
	fp.write(content)
	fp.close()
	f = open('pic' + picid + '\\' + str(1) + '.txt', 'r')
	temp = f.read()
	f.close()
	pic_url = re.findall('img src="(.*?)" alt="rosi', temp, re.S)
	for each in pic_url:
		fp = open('pic' + picid + '\\' + str(2) + '.txt', 'a')
		fp.write('<a>'+each+'</a>\n')
		fp.close()

fp = open('pic' + picid + '\\' + str(2) + '.txt', 'r')
urls = fp.read()
fp.close()
pic_urls = re.findall('<a>(.*?)</a>', urls, re.S)

i = 0
headers = {'Accept':'image/webp,*/*;q=0.8', 'Accept-Encoding':'gzip,deflate,sdch', 'Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'}
for each in pic_urls:
	print("now downloading: " + each)
	req = request.Request(url = each, headers = headers)
	content = request.urlopen(req).read()
	#pic = request.urlopen(each)
	fp = open('pic' + picid + '\\' + str(i) + '.jpg', 'wb')
	fp.write(content)
	fp.close()
	i += 1
	if i >= 500:
		break;
print("downloading finish...")
