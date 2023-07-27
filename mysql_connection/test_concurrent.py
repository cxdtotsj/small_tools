# -*- coding: utf-8 -*-
# @Data : 2021-03-25

import mysql.connector
from multiprocessing import Process
import threading

'''
Python并发测试 UPDATE

threading 是线程，因为GIL的存在，在python中不是实际的并发

Process 是进程，在python中是实际的并发

'''

info = {
    "host": '192.168.250.221',
    "port": 3323,
    "user": 'cxd',
    "password": '123456',
    "db": "temp_db"
}


def update_data(data):

    try:
        cnx = mysql.connector.connect(**info, autocommit=True)
        cursor = cnx.cursor()
        for i in range(data[0], data[1]):
            # print(i)
            sql_1 = f'SELECT MED_LIST_CODG FROM trt_serv_b LIMIT {i}, 1'
            sql = f'''UPDATE test_dead SET j='GGGG' WHERE id={i};'''
            cursor.execute(sql)
    except Exception as e:
        print(e)

def main():
    ths = []
    for i in range(1,1000000,10000):
        p = Process(target=update_data, args=((i, i+500),))
        ths.append(p)
    for p in ths:
        p.start()
    for p in ths:
        p.join()
    

if __name__ == '__main__':
    main()
