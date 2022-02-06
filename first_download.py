import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

#로컬의 downloaded 폴더를 다운로드 경로로 지정
downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

#입력받은 URL을 절대경로로 바꿔서 외부 경로로 나가지 않게 함
def getAbsoluteURL(baseUrl, source):
    #startswith(str or tuple) / 반환은 true or false / 지정한 문자열로 시작하는지 검사하는 함수
    #baseurl의 형태에 따라 url에 src 속성에서 주소 값을 넣는 형태가 달라짐
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    else:
        url = '{}/{}'.format(baseUrl, source)
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    #www 지우고
    path = absoluteUrl.replace('www.', '')
    #url 다 지우고
    path = path.replace(baseUrl, '')
    #지정한 디렉토리 + 파일 이름
    path = downloadDirectory+path
    #경로 중 디렉토리 이름만 가져오는 기능 (c:\users\user\abc.txt -> c:\users\user 반환)
    directory = os.path.dirname(path)

    #파일 or 디렉토리 경로가 존재하는지 체크
    if not os.path.exists(directory):
        #체크해서 없으면 그 디렉토리를 만드는 기능
        os.makedirs(directory)
    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
#src 속성이 있는 태그에 연결된 파일들을 list에 저장
#모두 다운로드 받기 위함
downloadList = bs.findAll(src=True)

for download in downloadList:
    #src=~~~ 에서 ~~~만 fileUrl에 저장
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)

#urlretrieve: url로 표시된 객체를 로컬 파일로 복사하는 기능
#urlretrieve(url(다운로드 받을 파일), filename(복사할 파일 위치), reporthook(콜러블), data)
#모든 객체 파일을 로컬의 지정한 폴더에 그 파일 이름 그대로 다운로드
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))