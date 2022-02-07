from urllib.request import urlopen
from bs4 import BeautifulSoup

#보안 연결을 우회하는 코드임, 인증을 우회하는 것이기 때문에 믿을 수 있는 사이트에만 하자
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
"""
textpage = urlopen('https://www.ietf.org/rfc/fyi-index.txt')
#textpage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')

#utf-8 인코딩 해줘야 정상적으로 모든 문자열 출력이 가능하다
print(str(textpage.read(), 'utf-8'))
"""
html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
#스크래이핑하려는 페이지의 소스를 보면 인코딩 방식이 나와있는데, 이 태그에서 지정한 인코딩 방법을 써서 페이지를 읽는게 좋다.
content = bytes(content, 'UTF-8')
content = content.decode('UTF-8')
print(content)