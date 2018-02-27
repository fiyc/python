from bs4 import BeautifulSoup
import yifLibrary.HttpHelper as http

def main():
	# url = "http://www.chenyifei.online/blog"

	url = "http://hotels.ctrip.com/international/996628.html"
	html = http.GetRequestFromServer(url)
	soup = BeautifulSoup(html)
	links = soup.findAll(name='a')
	for link in links:
		if link.has_key('href') or str(link['href']).startswith('http'):
			print(link['href'])




if __name__ == "__main__":
	main()