from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')

#페이지의 table 중 id가 giftList인 것의 자식들만 출력함
#이걸 쓰려면 페이지의 코드 분석이 필요할듯?
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)