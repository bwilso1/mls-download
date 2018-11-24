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
	
	
	
def breakdown(element):
	#https://matrix.brightmls.com/Matrix/Public/PhotoPopup.aspx?tid=9&mtid=1&L=1&key=627224603&n=21&i=0&View=G
	print('not done')
	#<a href="PhotoPopup.aspx?tid=9&amp;mtid=1&amp;L=1&amp;key=627224603&amp;n=21&amp;i=0&amp;View=Y"><img class="IV_Image" src="https://matrixmedia.brightmls.com/mediaserver/GetMedia.ashx?Key=627224603&amp;TableID=9&amp;Type=1&amp;Number=0&amp;Size=6&amp;exk=1c7d269cfbcb629e1378d7c0d12455f5"></a>