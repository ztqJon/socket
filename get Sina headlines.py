# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import urllib
#download sina headlines from the websites
#get HTML source code 

#use agent
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

#Analysis of HTML source code
def html_parser(html, target):
    #下载100以内的新闻标题
    a = 0
    soup = BeautifulSoup(html, 'html.parser')
    for each in soup.select('.news-item'):
        if each.select('h2'):
            print('发布时间:', each.select('.time')[0].text,end=' ')
            print('标题:', each.select('h2')[0].text)
        if (a == 100):
            break
        a += 1

#Execution of main program
url = 'http://news.sina.com.cn/china/'
target = 'a'
html_parser(html_create(url), target)
