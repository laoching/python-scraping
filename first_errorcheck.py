from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getTitle(url):
    try:
        html=urlopen(url)
    #HTTP Error 발생 시 None 반환
    except HTTPError as e:
        return None
    #없는 URL 입력 시 None 반환
    except URLError as e:
        return None
    try:
        bs=BeautifulSoup(html.read(), 'html.parser')
        title=bs.body.h1
    #title에서 존재하지 않는 태그 입력 시 None 반환
    except AttributeError as e:
        return None
    return title

#getTitle 함수에 url 변수로 확인하고자 하는 url 입력
title = getTitle('http://www.pythonscraping.com/pages/page1.html')

#함수 실행 결과가 None이면 설정해놓은 문구 출력
if title == None:
    print('Title could not be found')
else:
    print(title)