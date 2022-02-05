from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html=urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

#findAll을 사용해서 문서에 조건에 일치하는 문자열을 모두 출력함 
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    #get_text를 사용해서 모든 태그를 지우고 유니코드 텍스트만 들어 있는 문자열 반환
    print(name.get_text())