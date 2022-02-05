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

html = urlopen('https://www.boannews.com')
#html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs=BeautifulSoup(html,'html.parser')

#/media/, /security_contents/, /securityworld/로 시작되는 링크만 가져오기 위해 정규표현식 사용
for link in bs.findAll('a', href=re.compile('^(/media/|/security_contents/|/securityworld/)(.)*$')):
    #attrs는 속성 값 모두 출력함
    #a 태그를 다 가져와버림 -> #<a class="mw-jump-link" href="#searchInput">Jump to search</a>
    #거기서 href라는 문자열이 있으면
    if 'href' in link.attrs:
        #속성 값 빼고 href 아래에 있는 그 경로만 출력해버림
        print(link.attrs['href'])