# coding=utf-8
import requests
import re
from xml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#定义爬虫
class spider(object):
    def __init__(self): #构造函数
        print '开始爬取内容！！！'

    #获取网页源代码的函数——getsource
    def getsource(self, url):
        html = requests.get(url)
        return html.text
    
    #用来产生不同页数的连接的函数——changepage
    def changpage(self,url,total_page):
        now_page = int(re.search('index_(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page + 1):
            link = re.sub('index_\d+','index_%s'%i, url, re.S)
            page_group.append(link)
        return page_group

    #用来爬取一个网络图篇的函数——getpic
    def getpic(self, source):
        selector = etree.HTML(source)
        pic_url = selector.xpath('//ul[@class="ali"]/li/div/a/img/@src')
        return pic_url

    #用来保存结果到pic文件夹中的函数——savepic
    def savepic(self, pic_url):
        picname = re.findall('(\d+)', link, re.S)
        picnamestr = ''.join(picname)
        i = 0
        for each in pic_url:
            print 'now downloading:' + each
            pic = request.get(each)
            fp = open('pic\\' + picnamestr + '-' + str(i) + '.jpg', 'wb')
            fp.write(pic.content)
            fp.close()
            i += 1
            
    #ppic 集合类的方法
    def ppic(self, link):
        print '正在处理页面：'+link
        html = picspider.getsource(link)
        pic_url = picspider.getpic(html)
        picspider.savepic(pic.url)

time1 = time.time()
if __name__ == '__main__':
    url = 'http://www.ivsky.com/tupian/ziranfengguang/index_1.html'
    picspider = spider()
    all_links = picspider.changepage(url, 3)
    for link in all_links:
        picspider.ppic(link)
time2 = time.time
print '耗时：' + str(time2 - time1)

print 'zhangqing'
