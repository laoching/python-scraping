from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')

#next_siblings() 함수는 다음 형제만 가져옴
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)