import requests
from bs4 import BeautifulSoup
import lxml
import time


def get_IP(num):
    '''
    爬取代理IP
    '''
    
    
    IP_list = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    
    for i in range(1, num+1):
        url = f'https://www.xicidaili.com/nn/{i}/'
        time.sleep(1)
        req = requests.get(url, headers=header)
        soup = BeautifulSoup(req.text, 'lxml')
        tr_list = soup.find_all('tr')[1:]
        
        for tr in tr_list:
            td_list = tr.find_all('td')
            ip = td_list[1].text
            port = td_list[2].text
            IP_list.append(f'{ip}:{port}')
      
    return IP_list


def test_IP(IP_list):
    '''
    检验IP可用性
    '''
    
    
    IP_pool = []
    url = 'https://www.baidu.com/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    
    for ip in IP_list:
        try:
            pro = {'http': f'http://{ip}', 
                   'https': f'http://{ip}'}
            req = requests.get(url, headers=header, proxies=pro, timeout=5)
            time.sleep(0.5)
        
            if req.status_code == 200:
                IP_pool.append(ip)
                
        except:
            continue

    return IP_pool


if __name__ == '__main__':
    import csv
    
    IP_list = get_IP(3)
    IP_pool = test_IP(IP_list)
    
    with open('proxy_ip.csv', 'w', newline='') as f:
        csv.writer(f).writerow(['ip'])
        
        for ip in IP_pool:
            csv.writer(f).writerow([ip])  #writerow()里是一个可迭代对象

    print('IP池建立完毕')