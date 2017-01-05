#coding=utf-8

import urllib
import re

def downloadPage(url):
    h = urllib.urlopen(url)
    return h.read()

def downloadImg(content):
    pattern = r'href="(.+?\.jpg)" class'
    m = re.compile(pattern)
    urls = re.findall(m, content)

    for i, url in enumerate(urls):
        print url
        urllib.urlretrieve(url, "%s.jpg" % (i, ))

content = downloadPage("http://s5.51cto.com/wyfs02/M00/24/E1/wKiom1NV022R9qJXAABHAu-hyvQ095.jpg")
downloadImg(content)
