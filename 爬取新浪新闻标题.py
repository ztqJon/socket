# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import urllib
#从新浪网上下载新闻标题
#获取html源码

#使用代理
'''
proxy_support = urllib.request.ProxyHandler({'http':'121.232.146.207'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
'''
def html_create(url):
    head = {}#设置请求头 修改User-Agent
    head['Referer'] = url
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;rv:58.0) Gecko/20100101 Firefox/58.0'
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

#解析html源码
def html_parser(html, target):
    #下载100以内的新闻标题
    a = 0
    soup = BeautifulSoup(html, 'html.parser')
    for each in soup.select('.news-item'):
        if each.select('h2'):
            print('发布时间:', each.select('.time')[0].text,end=' ')
            print('标题:', each.select('h2')[0].text)
        if (a == 1000000000000):
            break
        a += 1

#执行主程序
url = 'http://news.sina.com.cn/china/'
target = 'a'
html_parser(html_create(url), target)
