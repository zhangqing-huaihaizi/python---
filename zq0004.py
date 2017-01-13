#coding=utf-8
'''
项目名称：任一个英文的纯文本文件，统计其中的单词出现的个数
作者：zhangqing
日期：2017-1-13
联系方式：
'''
import collections, re
import sys

def count_words(inputname):
    print 'now processing:' + inputname + '....'
    f = open(inputname,'r')
    data = f.read()
    dic = collections.defaultdict(lambda: 0)
    #r表示后面单引号中的字符串是原生字符串
    #\W：匹配非字母数字   \d：匹配任意数字
    #将data中的非字母符号或者数字，替换成空格
    data = re.sub(r'[\W\d]', ' ', data)
    data = data.lower()
    datalist = data.split(' ')
    for item in datalist:
        dic[item] += 1
        
    del dic['']
    return dic

if __name__ == '__main__':
    try:
        print sorted(count_words("0004inputfile.txt").items())
    except:
        print 'no input file'
