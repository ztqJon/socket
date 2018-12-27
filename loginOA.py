import requests
import bs4
import time
#登陆体育部OA网站
#登陆所需要的Url
loginUrl = 'http://tyb.nju.edu.cn:8089/'
loginRequestUrl = 'http://tyb.nju.edu.cn:8089/student/studentFrame.jsp'
loginHostUrl = 'tyb.nju.edu.cn:8089'
loginRefererUrl = 'http://tyb.nju.edu.cn:8089/index.jsp'
loginFinishUrl = 'http://tyb.nju.edu.cn:8089/student/studentFrame.jsp'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
#登陆用户信息
UserName = '171180526'
passwd = 'As991215'

requestData = {
        #向服务器post的data信息
        'openType': '911',
        'loginflag': '0',
        'loginType': '0',
        'userName': UserName,
        'passwd': passwd,
}

Headers = {
        #向服务器post的headers信息
        'Host': loginHostUrl,
        'Referer': loginRefererUrl,
        'User-Agent': userAgent
}

#向网站提交信息
loginSession = requests.Session()
loginSession.get(loginUrl, headers=Headers, allow_redirects = False)
loginSession.post(loginRequestUrl, data = requestData, headers = Headers)

#解析登陆后才可以访问的网站
time.sleep(3)
test = loginSession.get(loginFinishUrl, headers = Headers)
print(test.text)
soup = bs4.BeautifulSoup(test.text, 'lxml')
print(soup.text)
try:
    title = soup.find('title').text
except:
    title = '登录失败'
print(title)

