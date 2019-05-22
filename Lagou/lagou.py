import requests
from urllib.parse import urlencode, quote
from fake_useragent import UserAgent
import math
import time
from random import randint
import pandas as pd


def get_json(url, param, kd, kd_parse, referer, pn):
    # 设置头部信息
    ua = UserAgent()
    header = {
            'User-Agent':ua.random,
            'Referer':referer,
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With':'XMLHttpRequest'
            }
    data = {
            'first': 'true',
            'pn':pn,
            'kd':kd
            }
    # 获取包含职位信息的json对象
    req = requests.post(url, headers = header, data = data)
    json = req.json()
    return json


def get_page_num(count):
    # 获取最大抓取页数
    pages = math.ceil(count/15)
    if pages > 30:
        return 30
    else:
        return pages

def get_page_info(jobs_list):
    # 对职位信息进行解析,返回列表
    page_info_list = []
    for i in jobs_list:
        job_info = []
        job_info.append(i['companyFullName'])
        job_info.append(i['companyShortName'])
        job_info.append(i['companySize'])
        job_info.append(i['financeStage'])
        job_info.append(i['district'])
        job_info.append(i['positionName'])
        job_info.append(i['workYear'])
        job_info.append(i['education'])
        job_info.append(i['salary'])
        job_info.append(i['positionAdvantage'])
        page_info_list.append(job_info)
    return page_info_list

def main(keyword, city='',gx=''):
    '''keyword 搜索关键词；
       city默认全国，还可以设置为'北京'，'上海'，'杭州'，'广州'，'深圳'，'成都'，'武汉'，'江苏'等城市；
       gx(工作性质)默认不限，可设置为'应届'or'实习'；
       '''
    # 中文转换为ASCII
    kd = keyword
    kd_parse = quote(kd)
    
    if not (gx or city):
        params = ''
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=1'
        referer = 'https://www.lagou.com/jobs/list_%E9%87%8F%E5%8C%96?isSchoolJob=1'
    elif (gx and not city):
        params = urlencode({'gx':gx})
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&' + params +'&needAddtionalResult=false&isSchoolJob=1'
        referer = 'https://www.lagou.com/jobs/list_{}?px=default&'.format(kd_parse) + params + 'isSchoolJob=1'
    elif (city and not gx):
        params = urlencode({'city':city})
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&' + params +'&needAddtionalResult=false&isSchoolJob=1'
        referer = 'https://www.lagou.com/jobs/list_{}?px=default&isSchoolJob=1&'.format(kd_parse) + params
    else:
        params = urlencode({'gx':gx, 'city':city})
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&' + params +'&needAddtionalResult=false&isSchoolJob=1'
        referer = 'https://www.lagou.com/jobs/list_{}?px=default'.format(kd_parse) + urlencode({'gx':gx}) + '&isSchoolJob=1&' + urlencode({'city':city})

                
    # 获取职位总数和总页数
    page_1 = get_json(url, kd=kd, kd_parse=kd_parse, param=params, referer=referer, pn=1)
    total_count = page_1['content']['positionResult']['totalCount']
    pagenum = get_page_num(total_count)
    print('职位总数:{},页数:{}'.format(total_count,pagenum))
    
    total_info = []
    for i in range(1,pagenum+1):
        # 对每个网页读取JSON, 获取每页数据
        page = get_json(url, kd=kd, kd_parse=kd_parse, param=params, referer=referer, pn=i)
        jobs_list = page['content']['positionResult']['result']
        page_info = get_page_info(jobs_list)
        total_info += page_info
        # 每次抓取完成后,暂停一会,防止被服务器拉黑
        time.sleep(randint(20,30))
        print('已经抓取第{}页, 职位总数:{}'.format(i, len(total_info)))
    #将总数据转化为DataFrame再输出
    df = pd.DataFrame(data = total_info, columns = ['公司全名','公司简称','公司规模','融资阶段','区域','职位名称','工作经验','学历要求','工资','职位福利'])
    df.to_csv('lagou_jobs.csv', index=False, encoding='utf-8')
    print('已保存为csv文件.')

if __name__== "__main__":
    main('金融', city='武汉', gx='实习')
