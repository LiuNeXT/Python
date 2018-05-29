#!/usr/bin/env python
# -*- coding: utf-8 -*-


from urllib import request
from bs4 import BeautifulSoup


url = "http://www.baidu.com"
page_info = urllib.request.urlopen(url).read()
page_info = page_info.decode('utf-8')
print(page_info)



#Python中urllib中的request模块提供了模拟浏览器访问的功能，代码如下：
from urllib import request
url = 'http://www.baidu.com'
# page = request.Request(url)
# page.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
print(page_info)

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')

# 以格式化的形式打印html
# print(soup.prettify())
titles = soup.find_all('a', 'title')  # 查找所有a标签中class='title'的语句
# 打印查找到的每一个a标签的string
for title in titles:
    print(title.string)


