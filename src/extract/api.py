import os
import requests


def call(dt='20150101', url_param={}):
    url = gen_url(dt, url_param)
    r = requests.get(url)
    j = r.json()
    br = j['boxOfficeResult']
    boxoffice = br['dailyBoxOfficeList']
    return boxoffice


def gen_url(dt='20150101', url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = key = os.getenv('MOVIE_API_KEY')
    url = f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_param.items():
        url = url + f"&{k}={v}"
    return url