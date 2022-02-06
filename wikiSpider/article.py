import scrapy

class ArticleSpider(scrapy.Spider):
    name='article'

    #start_requests: scrapy가 웹사이트를 크롤링할 때 사용하는 request 객체를 생성
    def start_resquests(self):
        urls = [
            'http://en.wikipedia.org/wiki/Python_%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
            'https://www.naver.com'
            'https://www.boannews.com']
        return [scrapy.Request(url=url, callback=self.parse)
                for url in urls]
    #사용자 정의 콜백 함수, callback=self.parse를 사용해 Request 객체로 전달
    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
