from urllib import request, error
from fake_useragent import UserAgent
import re
import time


def request_(url):
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.chrome}
        req = request.Request(url, headers=headers)
        return request.urlopen(req).read().decode('utf-8')
    except error as e:
        return e.reason


def parse_(html):
    ol = re.search('<ol class="grid_view">(.*?)</ol>', html, re.S).group(0)
    content = ('<li>.*?<em class="">(\d+)</em>.*?class="hd".*?href="(.*?)".*?class="title">(.*?)</span>.*?' +
               'property="v:average">(.*?)</span>.*?</li>')
    matchlist = re.compile(content, re.S).findall(ol)
    for match in matchlist:
        yield {
            'rank' : match[0],
            'src' : match[1],
            'name' : match[2],
            'score' : match[3]
            }


def main():
    url = 'https://movie.douban.com/top250?start={}'
    for page in range(10):
        start = page*25
        html = request_(url.format(start))
        time.sleep(0.5)
        for match in parse_(html):
            print(match)


if __name__ == '__main__':
    main()
