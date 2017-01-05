#!usr/bin/python
# -*- coding: utf-8 -*-
'''
Creadted on 2016-12-23
@author: zhangqing
使用python爬取csdn个人博客的访问量
'''
import urllib2
import re

#当前博客列表页号
page_num = 1
#不是最后列表的一页
notLast = 1

account = raw_input('输入csdn的登录账号：')

while notLast:
    #首页地址
    baseUrl = 'http://blog.csdn.net/' + account
    #连接页号，组成爬取的页面网址
    myUrl = baseUrl + '/artical/list/' + str(page_num)

    #伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}

    #构造请求
    req = urllib2.Request(myUrl, headers = headers)
    #访问页面
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()

    #在页面中查找是否存在'尾页'这一个标签来判断是否为最后一页
    notLast = re.findall('尾页', myPage, re.S)

    print '----------------------第%d页------------------' %(page_num)

    #利用正则表达式来获取博客的标题
    title = re.findall('(http://blog.csdn.net/xingjiarong/artical/details/.*?)',myPage,re.S)
    
    titleList = []
    for items in title:
        titleList.append(str(items).lstrip().rstrip())

    #利用正则表达式获取博客的访问量
    view = re.findall('阅读\((http://blog.csdn.net/xiaojiarong/artical/details/.*?)\)', myPage, re.S)

    viewList = []
    for items in view:
        viewList.append(str(items).lstrip().rstrip())

    #将结果输出
    for n in range(len(titleList)):
        print '访问量：%s 标题：%s' %(viewList[n], titleList[n])

    #页号加1
    page_num = page_num + 1
