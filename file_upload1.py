import requests

#로그인 패스와 같이 개발자도구 - 네트워크 - 응답이나 페이지 소스에서 폼에 사용되는 전달 파라미터를 파악한다.
#그 다음 폼이 동작하는 곳의 경로를 알아낸다.
#open 함수를 사용하고 업로드 하려는 파일의 경로+이름, rb(바이너리 형태: 여러가지 장점이 있음)
files = {'uploadFile':open('./test.png', 'rb')}
url = 'https://pythonscraping.com/pages/files/processing2.php'
r = requests.post(url, files=files)
print(r.text)

"""
바이너리를 이용했을 때의 장점
- 데이터 처리 및 전송 시 비용이 적게 발생함
- 보통 텍스트에 비해 파싱이 쉬워 데이터 처리 속도가 빠름
- 필요한 데이터 공간도 더 적은 경우가 있음
"""