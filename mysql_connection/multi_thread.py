# -*- coding: utf-8 -*-
# @Data : 2021-06-19

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
    "host": '192.168.210.132',
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

cnx = mysql.connector.connect(**info_hotdb, autocommit=True)
cur = cnx.cursor()

PSN_CLCT_DETL_IDs = []
PSN_NOs = []

with open('./data.txt', 'r', encoding='utf-8') as fp:
    for i in fp.readlines():
        x = i.split('#')
        PSN_NOs.append(x[0].strip())
        PSN_CLCT_DETL_IDs.append(x[1].strip())

def insert_data(data):


    for _ in range(data[0], data[1]):
        cnx_01 = mysql.connector.connect(**info_hotdb, autocommit=True)
        cnx_02 = mysql.connector.connect(**info_mysql, autocommit=True)
        rd_int_10 = random.randint(1, 999999999)
        index_2 = random.randint(0, 1)
        index_3 = random.randint(0, 2)
        index_4 = random.randint(0, 3)
        index_5 = random.randint(0, 4)
        index_7 = random.randint(0, 6)
        index_17 = random.randint(0, 16)
        # aaz223s = ('200000000000020878','200000000000019162','200000000000020831','200000000000014287','200000000000016457','200000000000015745','200000000000016431','200000000000019171','200000000000019219','200000000000019097','200000000000019071','200000000000020189','200000000000019095','200000000000018813','200000000000020887','200000000000020825','200000000000019261' )
        # aaz223 = aaz223s[index_17]
        aaz223 = random.randint(1, 99999999999999)
        aac001 = random.randint(1, 9999)
        aae001s = ['2019', '2020', '2021']
        aae001 = aae001s[index_3]
        aae002s = ['01', '02', '03', '04']
        aae002 = aae002s[index_4]
        aaz615 = random.randint(1000000, 99999999)
        aaa115s = ['10', '36', '21', '37', '38', '39', '40']
        aaa115 = aaa115s[index_7]
        aab001 = random.randint(1, 99)

        aae792s = ['01', '02', '06', '07', '03', '08', '04']
        aae792 = aae792s[0]
        # aae792 = aae792s[index_7]
        aae341s = ['个人', '中央', '区', '市', '县']

        aae341 = aae341s[index_5]
        aab191s = ['202001', '202002', '202003', '202004', '202005']
        aab191 = aab191s[index_5]
        aaz686 = rd_int_10
        aae202 = rd_int_10
        aic020s = ['200挡', '300挡', '400挡']
        aic020 = aic020s[index_3]
        aae022 = 1000
        aae078s = ['0', '1']
        aae078 = aae078s[index_2]
        aae738 = aae078s[index_2]
        aaz159 = rd_int_10
        aae859 = '20210102'
        aab034 = rd_int_10
        aae741s = [1, 2, 4, 9]
        aae741 = aae741s[index_4]
        baa072s = [1, 2]
        baa072 = baa072s[index_2]
        aae665 = aae078s[index_2]
        aae860 = 'cxd'
        aae011 = 'cxd'
        aaz692 = rd_int_10
        aae036 = aae859
        sql = '''SELECT aac001,aae001,aae002,aaz615,aaa115,aab001 FROM bc43 WHERE aaz223 IN ('200000000000020878','200000000000019162','200000000000020831','200000000000014287','200000000000016457','200000000000015745','200000000000016431','200000000000019171','200000000000019219','200000000000019097','200000000000019071','200000000000020189','200000000000019095','200000000000018813','200000000000020887','200000000000020825','200000000000019261' );'''
        cursor = cnx_01.cursor()
        cursor.execute(sql)
        sql_data = cursor.fetchall()
        values = sql_data[index_17]
        print(values)
        aac001,aae001,aae002,aaz615,aaa115,aab001 = values
        # sql = (f'''INSERT INTO `bc43` 
        # (aaz223, aaz686, aac001, aab001, aae002, aae001, aae202, aaa115, aic020, aae341, aae022, aab191, aae078, aaz615, aae738, aae792, aaz159, aae859, aab034, aae741, baa072, aae665, aae860, aae011, aaz692, aae036) 
        # VALUES 
        # ({aaz223}, {aaz686}, {aac001}, '{aab001}', {aae002}, {aae001}, {aae202}, {aaa115}, '{aic020}', '{aae341}', {aae022}, {aab191}, {aae078}, {aaz615}, {aae738}, '{aae792}', {aaz159}, '{aae859}', {aab034}, {aae741}, {baa072}, {aae665}, '{aae860}', '{aae011}', {aaz692}, '{aae036}');''')
        sql = (f'''INSERT INTO `bc43` 
        (aaz223, aaz686, aac001, aab001, aae002, aae001, aae202, aaa115, aic020, aae341, aae022, aab191, aae078, aaz615, aae738, aae792, aaz159, aae859, aab034, aae741, baa072, aae665, aae860, aae011, aaz692, aae036) 
        VALUES 
        ({aaz223}, {aaz686}, {aac001}, '{aab001}', {aae002}, {aae001}, {aae202}, {aaa115}, '{aic020}', '{aae341}', {aae022}, {aab191}, {aae078}, {aaz615}, {aae738}, '{aae792}', {aaz159}, '{aae859}', {aab034}, {aae741}, {baa072}, {aae665}, '{aae860}', '{aae011}', {aaz692}, '{aae036}');''')

        try:
            # print(f'hotdb: {sql}')
            cursor_01 = cnx_01.cursor()
            cursor_01.execute(sql)
        except Exception as e:
            print(f'hotdb: {e}')
        try:
            # print(f'mysql: {sql}')
            cursor_02 = cnx_02.cursor()
            cursor_02.execute(sql)
        except Exception as e:
            print(f'mysql: {e}')
            
def main():
    ths = []
    # length = len(PSN_NOs)
    num = 8
    # 插入真实数据
    for i in range(0,num):
        p = Process(target=insert_data, args=([1, 10],))
        ths.append(p)
    for p in ths:
        p.start()
    for p in ths:
        p.join()


if __name__ == '__main__':
    main()