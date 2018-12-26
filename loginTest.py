import requests
import bs4
import os
from PIL import Image
from http import cookiejar
#使用图片库PTL
#构造登录需要提交的内容
#设置登录请求头并建立一个session
loginUrl = 'http://elite.nju.edu.cn/jiaowu/'
loginDoUrl = "http://elite.nju.edu.cn/jiaowu/login.do"
loginReferer = "http://elite.nju.edu.cn/jiaowu/exit.do"
head = {'Referer': loginReferer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;rv:58.0) Gecko/20100101 Firefox/58.0'}
loginSession = requests.session()
loginHtml = loginSession.get(loginUrl, headers=head)
loginSession.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')

def createPostContent(Url):
    #创建需要post的data
    #使用lxml的html解析器
    startSoup = bs4.BeautifulSoup(loginHtml.text, 'lxml')

    # 找到验证码图片地址
    Source = startSoup.find('img', attrs={'id': 'ValidateImg'})['src']

    # 下载验证码图片
    pic = requests.get(
        Url + Source).content
    with open('validateImg.png', 'wb') as f:
        f.write(pic)

    # 打开验证码图片
    image = Image.open('{}/ValidateImg.png'.format(os.getcwd()))
    image.show()

    # 构造需要提交的参数列表
    Data = {'userName': input("学号："), 'password': input("密码："),
            'returnUrl': 'null','ValidateCode': input('请输入图片中的验证码：')
            }

    return Data


# 登录教务系统
def login(url, Data):
    # 通过session进行请求提交
    loginSession.post(url, data=Data, headers = head)
    print(loginSession.cookies)
    return loginSession


#教务网地址
data = createPostContent(loginUrl)
#获取登录数据
print(data)
# 模拟登录教务系统
LoginSession = login(loginDoUrl, data)
test = LoginSession.get(loginDoUrl)
#获取登录后页面信息
soup = bs4.BeautifulSoup(test.text, 'lxml')
print(soup.text)
#获取学生姓名，验证登录成功与否
try:
    name = soup.find('div', attrs={'id': 'UserInfo'}).text
except:
    name = '登录失败'
print(name)