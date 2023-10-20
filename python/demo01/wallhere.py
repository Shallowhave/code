import requests_html
import fake_useragent


# session = requests_html.HTMLSession()
# headers = {'User-Agent': fake_useragent.UserAgent().chrome}
# url = "https://wallhere.com/"
#
# r = session.get(url=url, headers=headers,verify=False)
# print(r.html.html)
#

class Crawler:

    def __init__(self, url, headers):
        self.session = requests_html.HTMLSession()
        self.url = url
        self.headers = headers


if __name__ == '__main__':
    headers = {'User-Agent': fake_useragent.UserAgent().chrome}
    url = "https://wallhere.com/"
    Crawler(url=url,headers=headers)
