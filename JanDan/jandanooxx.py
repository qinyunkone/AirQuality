import requests
from bs4 import BeautifulSoup
import os
import re
import time


class JanDan():
    '''
    爬取煎蛋网所有图片并保存在文件夹
    '''
    
    
    # url:爬取网址  folder:文件夹名
    def __init__(self, url='http://jandan.net/ooxx/', folder='jandan'):
        self._url = url
        self._folder = folder
    
    
    # 返回网页源代码
    def get_page_source(self, url):
        html = requests.get(url).text
        return html
    
    
    # 返回图片总页数
    def get_pages_num(self):
        html = self.get_page_source(self._url)
        pages_num = BeautifulSoup(html, 'lxml').find('span', class_="current-comment-page").string[1:-1]
        return int(pages_num)
    
    
    # 创建保存图片的文件夹
    def create_folder(self, cwd):
        os.chdir(cwd)
        if not os.path.exists(self._folder):
            os.mkdir(self._folder)
        os.chdir(self._folder)
    
    
    def main(self):
        current_cwd = os.getcwd()
        self.create_folder(current_cwd)
        pages_num = self.get_pages_num()
        print(f'总页数：{pages_num}')
        for i in range(pages_num):
            page = pages_num - i
            print(f'正在爬取第{page}页')
            page_url = self._url + f'page-{page}#comments'
            time.sleep(1)
            page_html = self.get_page_source(page_url)
            page_soup = BeautifulSoup(page_html, 'lxml').find('ol', class_='commentlist')
            for img in page_soup.find_all('img', attrs={'referrerpolicy': 'no-referrer'}):
                img_url = 'http:' + img.attrs['src']
                f_name = img_url.split('/')[-1]
                with open(f_name, 'wb') as f:
                    time.sleep(0.5)
                    img_ = requests.get(img_url).content
                    f.write(img_)
        
        print('图片爬取完毕！')


if __name__ == '__main__':
    jandan = JanDan()
    jandan.main()
