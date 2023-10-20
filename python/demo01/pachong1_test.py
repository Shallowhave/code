from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "https://cq.58.com/ershouche/?PGTID=0d100000-0002-50d1-61e3-68d9a9cd6d8a&ClickID=4"
headers = {'UserAgent': UserAgent().chrome}

req = Request(url=url, headers=headers)
reslut = urlopen(req)
print(reslut.read().decode())
