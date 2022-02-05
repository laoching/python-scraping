from urllib.request import urlopen
from bs4 import BeautifulSoup
#정규 표현식을 위한 re 모듈 import
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#re.complie()에 정규 표현식을 써준다.
#../img/gifts/img로 시작하고 .jpg로 끝나는 것들만 다 출력함
#images는 list처럼 이용이 가능함
images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
print(images)
for image in images:
    #src 아래의 것들만 출력해줌
    print(image['src'])
