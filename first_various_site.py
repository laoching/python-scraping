from bs4 import BeautifulSoup
import requests

#보안 연결을 우회하는 코드임, 인증을 우회하는 것이기 때문에 믿을 수 있는 사이트에만 하자
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    #사이트에 GET 요청
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.select('div.StoryBodyCompanionColumn div p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class', 'post-body'})
    return Content(url, title, body)

url = '''
https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/
'''
content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}'.format(content.url))
print(content.body)

url = '''
https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html
'''
content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}'.format(content.url))
print(content.body)