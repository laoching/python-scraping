import ssl
from urllib.request import urlopen
ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen('https://pythonscraping.com/pages/page1.html')
print(html.read())