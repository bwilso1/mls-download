import inspect
import requests
from bs4 import BeautifulSoup

def launch(url = None):
	if url:
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html5lib')
		tables = soup.find_all('tr', {'id': 'm_trGallery'})
		tables = tables.find_all('tr', {'class': 'imageRow'})
	
	else:
		print("you need to type a url to start")
		url =  "https://matrix.brightmls.com/Matrix/Public/PhotoPopup.aspx?tid=9&mtid=1&L=1&key=627224603&n=21&i=0&View=G"
	
	
	
def breakdown(element):
	print('someting')
	# https://matrix.brightmls.com/Matrix/Public/
	# PhotoPopup.aspx?tid=9&mtid=1&L=1&key=627224603&n=21&i=0&View=Y
	
	# https://matrix.brightmls.com/Matrix/Public/PhotoPopup.aspx?tid=9&mtid=1&L=1&key=627224603&n=21&i=0&View=Y

def generateLinks(base_url, limit):
	for x in range(0,limit):
		base_url % x
		
def getImageLink(url=None):
	if url is None:
		url = "https://matrix.brightmls.com/Matrix/Public/PhotoPopup.aspx?tid=9&mtid=1&L=1&key=627224603&n=21&i=0&View=Y"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html5lib')
	imgs = soup.find_all('img', {'class' : 'IV_Image'})

	return imgs[0]['src']
		
def savePhoto():
	import urllib
	f = open('00000001.jpg','wb')
	f.write(urllib.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read())
	f.close()
	
	import requests
	f = open('00000001.jpg','wb')
	f.write(requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content)
	f.close()
	
	# this works
	# urllib.request.urlretrieve(getImageLink(), '1.jpg')