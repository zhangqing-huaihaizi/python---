# coding=utf-8
'''
项目名称：每天一个python程序之保存激活码到MySQL
创建时间：2017-01-11
作者：zhangqing
联系方式：
'''
import mysql.connector as conn

def activationCode2sql():
    #打开数据库连接
    db = conn.connect(user='root',passwd='root',host='localhost',database='words')
    cur = db.cursor()
    #使用execute()方法执行SQL
    cur.execute("drop table if exists activationCode")
    cur.execute("create table activationCode (id int auto_increment primary key, code varchar(10))")
    f = open('activationCode.txt')
    for line in f.readlines():
        cur.execute("insert into activationCode(code) values('%s')",line.strip())
    f.close()
    cur.close()


if __name__ == '__main__':
    activationCode2sql()
