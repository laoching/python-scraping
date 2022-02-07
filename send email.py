import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


#MIMEText 객체인 msg에는 수신/발신자의 이메일 주소, 본문, 헤더가 드렁있음
#메일을 보내기 위해 기본적으로 SMTP 서버에 접근이 가능해야한다. 이 소스에서는 SMTP 서버를 로컬에서 실행했다는 가정하에 작성했다.
#저 주소에 들어가서 보이는게 NO가 아니라면 크리스마스라는 이메일을 보내주는 기능을 한다.
def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject']=subject
    msg['From']='christmas_alerts@pythonscraping.com'
    mgs['To']='wjdtkdals159@gmail.com'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bs = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bs.find('a', {"id":"answer"}).attrs['title']=="NO"):
    print("It is not christmas yet.")
    time.sleep(3600)
    bs = BeautifulSoup(urlopen("https://isitchristmas.com/"))

sendMail("It's Christmas!",
         "According to http://itischristmas.com, it is Christmas!")