from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

#보안 연결을 우회하는 코드임, 인증을 우회하는 것이기 때문에 믿을 수 있는 사이트에만 하자
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context




#문장을 단어로 구분함
def cleanSentence(sentence):
	sentence = sentence.split(' ')
	#공백, 구두점 제거(파이썬에서 구두점: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
	sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
	#한 글자로 이루어진 단어 제거(1과 a를 제외한 나머지들)
	sentence = [word for word in sentence if len(word) > 1 or (word.lower() == 'a' or word.lower() == 'i')]
	return sentence

def cleanInput(content):
	content = content.upper()
	#공백, [12]같은 인용 표시 지움
	content = re.sub('\n|[[\d+\]]', ' ', content)
	#인코딩 방식을 UTF-8로 바꿔서 이스케이프 문자 지움
	content = bytes(content, 'UTF-8')
	#ascii를 디코딩하고 에러는 무시
	content = content.decode('ascii', 'ignore')
	#.뒤에 공백이 있으면 그 문장은 끝난 것으로 판단
	sentences = content.split('. ')
	return [cleanSentence(sentence) for sentence in sentences]

def getNgramsFromSentence(content, n):
	#2-그램으로 출력하는 부분
	output=[]
	for i in range(len(content)-n+1):
		output.append(content[i:i+n])
	return output

def getNgrams(content, n):
	#깔끔한 리스트를 content에 넣음
	content = cleanInput(content)
	#Counter 클래스를 사용하면 대상 데이터에 있는 2-그램의 개수를 세서 딕셔너리 형태로 반환함
	ngrams = Counter()
	ngrams_list = []
	for sentence in content:
		newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentence(sentence, n)]
		#이건 왜 있는지 모르겠음
		#ngrams_list.extend(newNgrams)
		#ngrams 딕셔너리를 업데이트함
		ngrams.update(newNgrams)
	return(ngrams)



html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is :'+str(len(ngrams)))

