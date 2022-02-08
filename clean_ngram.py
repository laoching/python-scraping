from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

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
	output=[]
	for i in range(len(content)-n+1):
		output.append(content[i:i+n])
	return output

def getNgrams(content, n):
	content = cleanInput(content)
	ngrams=[]
	for sentence in content:
		ngrams.extend(getNgramsFromSentence(sentence, n))
	return(ngrams)

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is :'+str(len(ngrams)))