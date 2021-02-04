#!/usr/bin/python
# encoding:utf-8

'''
使用mysql-connector-python操作MYSQL数据库
'''

# 需要依赖mysql客户端： pip install mysql-connector-python

import os, sys, string
import mysql.connector
import sys
import random
from uuid import uuid1
sys.setdefaultencoding('utf-8')


def main():
    # connect to mysql
    try:
        conn = mysql.connector.connect(host='10.201.*.*', user='root', passwd='root', db='dbname')
    except Exception as e:
        print(e)
        sys.exit()


    # get cursor
    cursor = conn.cursor()
    # create table
    dropSql='drop table product'
    createSql = 'create table if not exists product(Prd_name varchar(128) primary key, Count int(4))'
    cursor.execute(dropSql)
    cursor.execute(createSql)

    # insert one data
    sql = "insert into product(Prd_name, Count) values('%s', %d)" % ("ATG", 200)

    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)

        # insert some datas
    sql = "insert into product(Prd_name, Count) values(%s, %s)"
    val = (("PPS", 400), ("暗恋我", 150), ("你好测试1", 25))

    try:
        cursor.executemany(sql, val)
    except Exception as e:
        print(e)

    conn.commit()
        # quary data
    sql = "select * from product"
    cursor.execute(sql)
    alldata = cursor.fetchall()
    # print data
    if alldata:
        for rec in alldata:
            print(rec[0], rec[1])

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
    print("\nIt's OK")


    cnx01 = mysql.connector.connect(user='cxd', passwd='123456', host='192.168.220.102', port=3323, database='hotdb_test')
    cursor = cnx01.cursor()

    sql = '''insert into dwd_news_content (news_id, content, status) values (%s, %s, %s) on duplicate key update content = values(content), status = values(status)''' 

    vals = []
    status = [0, 1, 2]


    for i in range(9999):
        ud = uuid1()
        rd = random.randint(0,2)
        val = [str(ud), f'abc{i}', status[rd]]
        vals.append(val)

    print(len(vals))

    for i in range(2):
        try:
            cursor.executemany(sql, vals)
        except Exception as e:
            print(e)
        cnx01.commit()