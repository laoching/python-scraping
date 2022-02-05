from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#보안 연결을 우회하는 코드임, 인증을 우회하는 것이기 때문에 믿을 수 있는 사이트에만 하자
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

pages=set()
def getLinks(pageUrl):
    global pages
    #보안뉴스 메인 도메인만 써놓고 pageUrl 변수에 경로를 받아온다.
    html = urlopen('https://www.boannews.com{}'.format(pageUrl))
    #html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
    bs=BeautifulSoup(html,'html.parser')
    #a 태그 안에 href가 /media/, /security_contents/, /securityworld/ 문자열로 시작하는 것을 찾아서 link 변수에 넣음
    for link in bs.findAll('a',href=re.compile('^(/media/|/security_contents/,/securityworld/)')):
        #link 변수를 속성까지 다 불러와서 href가 있으면
        if 'href' in link.attrs:
            #위에서 발견한 것이 pages 안에 없으면 (중복 탐색을 방지하기 위함)
            if link.attrs['href'] not in pages:
                #새 페이지를 발견
                newPage = link.attrs['href']
                #발견한 새 페이지를 출력
                print(newPage)
                #pages에 발견한 페이지를 추가함
                pages.add(newPage)
                #함수를 재귀적으로 호출한다
                getLinks(newPage)

getLinks('')

