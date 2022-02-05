from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html=urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

#findAll을 사용해서 문서에 조건(attributes)에 일치하는 문자열을 모두 출력함
#attributes 자리에는 속성으로 이루어진 파이썬 딕셔너리를 받고 그 중 일치하는 태그를 찾음
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    #get_text를 사용해서 모든 태그를 지우고 유니코드 텍스트만 들어 있는 문자열 반환
    print(name.get_text())

#매개변수 중 text라는 변수가 있는데 문서에서 찾고자 하는 문자열을 입력하면
#문서에 해당 문자열이 들어있는 갯수만큼 리스트 형태에 쌓임
#그래서 문자열이 몇개 있는지 확인할 수 있음
List=bs.findAll(text='the prince')
print(List)
#문자열 몇개  있는지 알 수 있는 코드
print(len(List))