import requests
#보안 연결을 우회하는 코드임, 인증을 우회하는 것이기 때문에 믿을 수 있는 사이트에만 하자
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#전달되는 패킷을 만들려면 파라미터 이름을 정확하게 알고 있어야 한다.
params = {'firstname':'Ryan', 'lastname':'Mitchell'}

#폼이 실제로 동작하는 곳을 알고 있어야 한다. 여기서는 processing.php임
#폼에서 요구하는 파라미터가 firstname, lastname 밖에 없기 때문에 손쉽게 작성할 수 있었음
r = requests.post('https://pythonscraping.com/pages/processing.php', data=params)
print(r.text)
