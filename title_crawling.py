from bs4 import BeautifulSoup
from urllib.request import urlopen

#지정한 url의 모든 html 코드를 긁어온다.
html=urlopen('https://www.boannews.com/media/t_list.asp')
bs=BeautifulSoup(html,'html.parser')

#긁어온 코드에서 span 태그의 class 이름이 news_txt인 것만 title에 저장한다.
#boanews 홈페이지에서는 기사 제목을 <span class='news_txt'>에 작성해놓음.
title=bs.select('span[class = news_txt]')

#title에는 기사 제목 뿐만 아니라 태그까지 모두 포함되어 있기 때문에 get_text()를 이용해 text만 뽑아준다.
for i in title:
    print(i.get_text())
