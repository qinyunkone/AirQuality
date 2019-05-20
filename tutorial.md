
什么是爬虫？请求网站并提取数据的自动化程序。

# urllib

[官方文档](https://docs.python.org/zh-cn/3.6/library/urllib.html)

## Request

request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

### urlopen

urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)


```python
from urllib import request

url = 'http://httpbin.org/get'
req = request.Request(url)                   # 发送请求
# print(type(req))                             # urllib.request.Request
response = request.urlopen(req)              # 返回响应
# print(type(response))                        # http.client.HTTPResponse
# print(type(response.read()))                 # bytes
# print(type(response.read().decode('utf8')))  # str
print(response.read().decode('utf8'))        # 源代码
```

    {
      "args": {}, 
      "headers": {
        "Accept-Encoding": "identity", 
        "Host": "httpbin.org", 
        "User-Agent": "Python-urllib/3.6"
      }, 
      "origin": "35.190.180.154, 35.190.180.154", 
      "url": "https://httpbin.org/get"
    }
    
    

### urlencode

urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)


```python
from urllib import request, parse

url = 'http://httpbin.org/post'
data = bytes(parse.urlencode({'hello': 'world'}), encoding='utf8')
headers = {
    'user-agent': 'my-browser'
}

req = request.Request(url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
# print(data)
# print(response.read().decode('utf8'))
```

## Response


```python
from urllib import request, parse

url = 'http://httpbin.org/post'
data = bytes(parse.urlencode({'hello': 'world'}), encoding='utf8')
headers = {
    'User-Agent': 'my-browser'
}

req = request.Request(url, data=data, headers=headers, method='POST')
response = request.urlopen(req)

# print(data)
# print(response.status)
print(response.read().decode('utf8'))
```

    {
      "args": {}, 
      "data": "", 
      "files": {}, 
      "form": {
        "hello": "world"
      }, 
      "headers": {
        "Accept-Encoding": "identity", 
        "Content-Length": "11", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "my-browser"
      }, 
      "json": null, 
      "origin": "35.190.180.154, 35.190.180.154", 
      "url": "https://httpbin.org/post"
    }
    
    

# requests

[中文文档](http://docs.python-requests.org/zh_CN/latest/index.html)

## 简单使用

### 基本 get 请求

requests.get(url, params=None, **kwargs)


```python
import requests

url = 'http://httpbin.org/get'
r = requests.get(url)

# print(type(r))          #requests.models.Response
# print(type(r.content))  #bytes
# print(r.content)        #HTTP响应内容的二进制形式
# print(type(r.text))     #str
print(r.text)           #HTTP响应内容的字符串形式
```

    {
      "args": {}, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.21.0"
      }, 
      "origin": "35.190.180.154, 35.190.180.154", 
      "url": "https://httpbin.org/get"
    }
    
    

### 传递参数和请求头


```python
import requests

url = 'http://httpbin.org/get'
params = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, params=params, headers=headers)
print(r.text)
```

    {
      "args": {
        "key1": "value1", 
        "key2": "value2"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "my-app/0.0.1"
      }, 
      "origin": "35.190.180.154, 35.190.180.154", 
      "url": "https://httpbin.org/get?key1=value1&key2=value2"
    }
    
    

### 常用方法


```python
import requests

url = 'http://httpbin.org/get'
params = {'key1': 'value1', 'key2': 'value2'}
headers = {
    'user-agent': 'my-app/0.0.1'
}

r = requests.get(url, params=params, headers=headers)

# print(r.url)              # http://httpbin.org/get?key1=value1&key2=value2
# print(r.status_code)      #状态码
# print(r.headers)          #响应头
# print(r.request.headers)  #请求头
# print(r.cookies)          #cookie
```

### 解析json


```python
import requests

url = 'http://httpbin.org/get'
r = requests.get(url)
# print(type(r.json()))  #dict
print(r.json())
```

    {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.21.0'}, 'origin': '35.190.180.154, 35.190.180.154', 'url': 'https://httpbin.org/get'}
    

### 各种请求方式

requests.post('http://httpbin.org/post')

requests.put('http://httpbin.org/put')

requests.delete('http://httpbin.org/delete')

requests.head('http://httpbin.org/get')

requests.options('http://httpbin.org/get')

requests.post(url, data=None, json=None, **kwargs)


```python
import requests

url = 'http://httpbin.org/post'
data = {'key1': 'value1', 'key2': 'value2'}
headers = {
    'User-Agent': 'my-browser'
}
r = requests.post(url, data=data, headers=headers)
print(r.text)
```

    {
      "args": {}, 
      "data": "", 
      "files": {}, 
      "form": {
        "key1": "value1", 
        "key2": "value2"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "23", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "my-browser"
      }, 
      "json": null, 
      "origin": "35.190.180.154, 35.190.180.154", 
      "url": "https://httpbin.org/post"
    }
    
    

## 高级应用

### proxies


```python
import requests
from requests.exceptions import ProxyError

url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://119.101.116.230:9999',
    'https': 'http://119.101.118.26:9999',
}

try:
    r = requests.get(url, proxies=proxies)
    print(r.text)
except ProxyError:
    print('代理失败')
```

    代理失败
    

### cookies


```python
import requests

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.text)
```

    {
      "cookies": {
        "cookies_are": "working"
      }
    }
    
    

### timeout


```python
import requests
from requests.exceptions import Timeout

url = 'http://httpbin.org/get'
try:
    r = requests.get(url, timeout=0.01)
    print(r.status_code)
except Timeout:
    print('Time Out')
```

    Time Out
    

### Session


```python
import requests


#实例化
s = requests.Session()

url = 'http://httpbin.org/get'
#参数
s.params = {'key1': 'value1', 'key2': 'value2'}
#请求头
s.headers = {'user-agent': 'my-app/0.0.1'}
#代理
# s.proxies = {
#     'http': 'http://119.101.116.230:9999',
#     'https': 'http://119.101.118.26:9999',
# }
#cookies
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#认证
s.auth = ('user', 'pass')

r = s.get(url)
print(r.text)
```

    {
      "args": {
        "key1": "value1", 
        "key2": "value2"
      }, 
      "headers": {
        "Accept-Encoding": "identity", 
        "Authorization": "Basic dXNlcjpwYXNz", 
        "Cookie": "sessioncookie=123456789", 
        "Host": "httpbin.org", 
        "User-Agent": "my-app/0.0.1"
      }, 
      "origin": "35.190.180.154, 35.190.180.154", 
      "url": "https://httpbin.org/get?key1=value1&key2=value2"
    }
    
    

# 正则表达式

[正则表达式测试](http://tool.oschina.net/regex)

| 模式| 描述|
|--|-:|
| \w	| 匹配字母数字及下划线 |
| \W	| 匹配非字母数字下划线 |
| \s	| 匹配任意空白字符，等价于 [\t\n\r\f]. |
| \S	| 匹配任意非空字符 |
| \d	| 匹配任意数字，等价于 [0-9] |
| \D	| 匹配任意非数字 |
| \A	| 匹配字符串开始 |
| \Z	| 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串 |
| \z	| 匹配字符串结束 |
| \G	| 匹配最后匹配完成的位置 |
| \n | 匹配一个换行符 |
| \t | 匹配一个制表符 |
| ^	| 匹配字符串的开头 |
| $	| 匹配字符串的末尾。|
| .	| 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。|
| [...]	| 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k' |
| [^...]	| 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。| 
| *	| 匹配0个或多个的表达式。|
| +	| 匹配1个或多个的表达式。|
| ?	| 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式| 
| {n}	| 精确匹配n个前面表达式。|
| {n, m} | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式| 
| a&#124;b | 匹配a或b |
| ( )	| 匹配括号内的表达式，也表示一个组 |

---
|控制标记| 描述 |
|--|:-|
| re.I | 使匹配对大小写不敏感 |
| re.M | 多行匹配，影响 ^ 和 $ |
| re.S | 使 . 匹配包括换行在内的所有字符 |

## re.match

re.match(pattern, string, flags=0)  从字符串的开始位置匹配，返回match对象


```python
import re

content = 'Hello 123 4567 World'
match = re.match('^Hello.*World', content)
print(match)          # <_sre.SRE_Match object; span=(0, 20), match='Hello 123 4567 World'>
print(type(match))    # _sre.SRE_Match
print(match.group())
```

    <_sre.SRE_Match object; span=(0, 20), match='Hello 123 4567 World'>
    <class '_sre.SRE_Match'>
    Hello 123 4567 World
    


```python
import re

content = 'Hello 123 4567 World'
match = re.match('^Hello\s(\d+)\s(\d+)\sWorld$', content)
print(match.group(0))
print(match.group(1))
print(match.group(2))
```

    Hello 123 4567 World
    123
    4567
    

re.match强制从字符串的开始位置匹配


```python
import re

content = 'Extra stings Hello 1234567 World'
match = re.match('Hello.*Demo', content)
print(match)
```

    None
    

## re.search

re.search(pattern, string, flags=0)  搜索匹配的第一个位置，返回match对象

贪婪匹配(.*)


```python
import re

content = 'Extra stings Hello 1234567 World'
match = re.search('Hello (.*) World', content)
print(match)
print(match.group(1))
```

    <_sre.SRE_Match object; span=(13, 32), match='Hello 1234567 World'>
    1234567
    

非贪婪匹配(.*?)


```python
import re

content = 'Extra stings Hello 1234567 World'
match = re.search('Hello (.*?)(\d{6}) World', content)
print(match.group(1))
print(match.group(2))
```

    1
    234567
    

## re.findall

re.findall(pattern, string, flags=0)  以列表形式返回全部匹配的子串


```python
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(type(results))  # list
for result in results:
    print(result[0], result[1], result[2])
```

    <class 'list'>
    /2.mp3 任贤齐 沧海一声笑
    /3.mp3 齐秦 往事随风
    /4.mp3 beyond 光辉岁月
    /5.mp3 陈慧琳 记事本
    /6.mp3 邓丽君 但愿人长久
    

## re.compile

re.compile(pattern, flags=0)


```python
import re

content = 'Extra stings Hello 1234567 World'
pat = re.compile('\d')  # 匹配数字
print(pat)              # re.compile('\\d')
print(type(pat))        # _sre.SRE_Pattern

#pat.sub(repl, string, count=0)  用repl替换string中的匹配对象
res1 = pat.sub('*', content, 5)
print(res1)

#pat.split(string=None, maxsplit=0, *, source=None)  按照匹配结果分割string，返回列表
res2 = pat.split(content)
print(res2)

#pat.finditer(string, flags=0)  返回匹配的可迭代对象
for m in pat.finditer(content):
    print(type(m), m.group())
```

    re.compile('\\d')
    <class '_sre.SRE_Pattern'>
    Extra stings Hello *****67 World
    ['Extra stings Hello ', '', '', '', '', '', '', ' World']
    <class '_sre.SRE_Match'> 1
    <class '_sre.SRE_Match'> 2
    <class '_sre.SRE_Match'> 3
    <class '_sre.SRE_Match'> 4
    <class '_sre.SRE_Match'> 5
    <class '_sre.SRE_Match'> 6
    <class '_sre.SRE_Match'> 7
    

# BeautifulSoup

[中文文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

| 解析器	| 使用方法	| 优势	| 劣势 |
|--| -- |-- |-- |
| Python标准库 |	BeautifulSoup(markup, "html.parser")	| Python的内置标准库、执行速度适中 、文档容错能力强 | Python 2.7.3 or 3.2.2)前的版本中文容错能力差|
| lxml HTML 解析器	| BeautifulSoup(markup, "lxml")	| 速度快、文档容错能力强 | 需要安装C语言库 |
| lxml XML 解析器	| BeautifulSoup(markup, "xml") | 速度快、唯一支持XML的解析器 | 需要安装C语言库 |
| html5lib	| BeautifulSoup(markup, "html5lib")	 | 最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档 | 速度慢、不依赖外部扩展 |

## 简单用法


```python
from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(type(soup))  # bs4.BeautifulSoup
print(soup.prettify())
```

    <class 'bs4.BeautifulSoup'>
    <html>
     <head>
      <title>
       The Dormouse's story
      </title>
     </head>
     <body>
      <p class="title">
       <b>
        The Dormouse's story
       </b>
      </p>
      <p class="story">
       Once upon a time there were three little sisters; and their names were
       <a class="sister" href="http://example.com/elsie" id="link1">
        Elsie
       </a>
       ,
       <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>
       and
       <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>
       ;
        and they lived at the bottom of a well.
      </p>
      <p class="story">
       ...
      </p>
     </body>
    </html>
    

### Tag


```python
print(type(soup.p))  # bs4.element.Tag
print(soup.p)
```

    <class 'bs4.element.Tag'>
    <p class="title"><b>The Dormouse's story</b></p>
    


```python
print(type(soup.p.name), soup.p.name)      #获取名称  str
print(type(soup.p.attrs), soup.p.attrs)    #获取属性  dict
print(type(soup.p.string), soup.p.string)  #获取内容  NavigableString
print(type(soup.p.text), soup.p.text)      #获取内容  str
```

    <class 'str'> p
    <class 'dict'> {'class': ['title']}
    <class 'bs4.element.NavigableString'> The Dormouse's story
    <class 'str'> The Dormouse's story
    

## 遍历文档树


```python
from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
```

### 子节点和后代节点


```python
# tag的 .contents 属性可以将tag的子节点以列表的方式输出
# print(soup.body.contents)

# tag的 .children 生成器,可以对tag的子节点进行循环
for ind, child in enumerate(soup.body.children):
    print(ind, child)

# tag的. descendants 生成器会返回所有的后代节点
# for ind, child in enumerate(soup.body.descendants):
#     print(ind, child)
```

    0 
    
    1 <p class="title"><b>The Dormouse's story</b></p>
    2 
    
    3 <p class="story">Once upon a time there were three little sisters; and their names were
        <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
        <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
    4 
    
    5 <p class="story">...</p>
    6 
    
    

### 父节点和祖先节点


```python
# 通过 .parent 属性来获取某个元素的父节点
print(soup.a.parent)

# 通过 .parents 属性可以递归得到元素的所有祖先节点
# for ind, parent in enumerate(soup.a.parents):
#     print(ind, parent)
```

    <p class="story">Once upon a time there were three little sisters; and their names were
        <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
        <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
    

### 兄弟节点


```python
# 向后遍历
for ind, sibling in enumerate(soup.a.next_siblings):
    print(ind, sibling)

# 向前遍历
for ind, sibling in enumerate(soup.a.previous_siblings):
    print(ind, sibling)
```

    0 ,
        
    1 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    2  and
        
    3 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    4 ;
        and they lived at the bottom of a well.
    0 Once upon a time there were three little sisters; and their names were
        
    

## 搜索文档树


```python
from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story" id="link">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
```

### soup.find(name=None, attrs={}, recursive=True, text=None, **kwargs)

返回第一个匹配对象


```python
print(soup.find('a', class_='sister'))
```

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    

### soup.find_all(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)

以列表形式返回所有的匹配对象


```python
for ind, tag in enumerate(soup.find_all('a', class_='sister')):
    print(ind, tag)
```

    0 <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    1 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    2 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    


```python
# 找到所有属性有3个的标签
for ind, tag in enumerate(soup.find_all(lambda tag: len(tag.attrs)==3)):
    print(ind, tag)
```

    0 <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    1 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    2 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    

### CSS选择器

通过select()直接传入CSS选择器即可完成选择


```python
# 直接选择标签
for tag in soup.select('p a'):
    print(tag)

# 选择class,前面加.
for tag in soup.select('.story .sister'):
    print(tag)

# 选择id,前面加#
for tag in soup.select('#link .sister'):
    print(tag)
```

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    

# PyQuery

## 初始化


```python
from pyquery import PyQuery as pq

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story" id="link">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""

doc = pq(html)
print(type(doc))
```

## CSS选择器

1.直接选择标签

2.选择class,前面加.

3.选择id,前面加#


```python
print(doc('.story a'))
```

## 获取信息


```python
a = doc('.story #link1')
print(a)

# 获取属性
print(a.attr('href'))
print(a.attr.href)

# 获取文本
print(a.text())
```

# selenium

## 初始化浏览器


```python
from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()
```

## 访问页面


```python
browser.get('https://httpbin.org/get')
print(type(browser.page_source))
print(browser.page_source)
browser.close()
```

# Scrapy

[中文文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/index.html)

## 创建新项目


```python
!scrapy startproject myproject
!cd myproject
!scrapy genspider test httpbin.org
```
