# -*- coding: utf-8 -*-
# @Data : 2021-06-19

import pymysql
import random
import mysql.connector
from multiprocessing import Process
import threading
import string

'''
Python并发测试 UPDATE

threading 是线程，因为GIL的存在，在python中不是实际的并发

Process 是进程，在python中是实际的并发

'''

info_hotdb = {
    "host": '192.168.220.102',
    "port": 3323,
    "user": 'cxd',
    "password": 'cxd123456',
    "db": "hotdb_test"
}

info_mysql = {
    "host": '192.168.220.150',
    "port": '3309',
    "user": 'cara',
    "password": '123456',
    "db": "hotdb_test"
}


PSN_CLCT_DETL_IDs = []
PSN_NOs = []

# with open('./data.txt', 'r', encoding='utf-8') as fp:
#     for i in fp.readlines():
#         x = i.split('#')
#         PSN_NOs.append(x[0].strip())
#         PSN_CLCT_DETL_IDs.append(x[1].strip())

def insert_data():
    cnx_01 = pymysql.connect(**info_hotdb, autocommit=True)
    cursor = cnx_01.cursor()
    while 1:
        # aab001 = '20000' + str(random.randint(111, 999))
        # aae003 = '20220' + str(random.randint(1, 9))
        aab001 = '20000999'
        aae003 = '202202'
        aac001 = str(random.randint(50, 100))
        sql = f'''INSERT INTO ac43 VALUES (0, '{aab001}', '{aae003}', {aac001}, '410', '01');'''
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)

            
def main():
    ths = []
    for i in range(0, 5):
        p = Process(target=insert_data, args=())
        ths.append(p)
    for p in ths:
        p.start()
    for p in ths:
        p.join()


if __name__ == '__main__':
    main()