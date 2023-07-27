# -*- coding: utf-8 -*-
# @Data : 2022-08-24

import pymysql
from pymysql.cursors import DictCursor
import time
import mysql.connector

info = {
    'host': '192.168.250.236',
    'port': 3325,
    'user': 'root',
    'password': 'root',
    'db': ''
}



while True:
    print('3323')
    conn = pymysql.connect(**info, cursorclass=DictCursor)
    conn.autocommit(0)
    cursor = conn.cursor()
    cursor.execute('''select * from backend where `host`in ('192.168.250.239:3200', '192.168.250.240:3200') and `state` in ('borrowed', 'running') and `comment` not in ('latency check', 'heartbeat');''')
    data = cursor.fetchone()
    if data:
        bkid = data['mysqlid']
    else:
        bkid = ''
    conn.close()

    print('SOURCE')
    mysql_info = {
        'host': '192.168.250.239',
        'port': 3200,
        'user': 'hotdb_datasource',
        'password': 'hotdb_datasource',
        'db': ''
    }
    conn_mysql = pymysql.connect(**mysql_info)
    cursor = conn_mysql.cursor()
    if bkid:
        sql = f'kill {bkid};'
        print(sql)
        cursor.execute(sql)
    time.sleep(3)
    conn_mysql.close()