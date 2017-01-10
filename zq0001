# coding=utf-8
__author__='zhangqing'
'''
项目名称：每天一个python程序之随机产生激活码
创建时间：2017-01-10
作者： zhangqing
联系方式：
'''
import string
import random

def ranGeneration():
    f = open('activationCode.txt','w+')
    for i in range(200):
        rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for j in range(10)) + '\n'
        f.write(rand_str)
    f.close()

if __name__ == '__main__':
    ranGeneration()
