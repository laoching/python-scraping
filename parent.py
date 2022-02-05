from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')

#img1.jpg를 선택함 -> 그 사진의 부모 태그를 선택함 -> 선택한 부모 태그의 윗 태그를 선택함 -> 선택한 태그에서 text를 출력함
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())