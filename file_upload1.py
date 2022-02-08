import requests

files = {'uploadFile':open('./test.png', 'rb')}
url = 'https://pythonscraping.com/pages/files/processing2.php'
r = requests.post(url, files=files)
print(r.text)