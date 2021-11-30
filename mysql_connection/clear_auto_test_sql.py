# -*- coding: utf-8 -*-
# @Data : 2021-07-31

import mysql.connector
import mysql.connector.pooling
import pymysql

import pymysql

mysql_config = {
    'user': 'zy',
    'password': 'zy',
    'host': '192.168.210.212',
    'port': 3323,
    'database': 'test_ct'
}

conn = pymysql.connect(**mysql_config, autocommit=True)

cursor = conn.cursor()

# # 获取表
cursor.execute('/*!hotdb:dnid=all*/show tables;')
tables = cursor.fetchall()
for t in tables:
    # 删除表
    if 'hotdb_temp' not in t[0]:
        continue
    if t[0] in ('hotdb_heartbeat', 'htp_dp_sync', '_hotdb_xa_log'):
        continue
    try:
        cursor.execute(f'/*!hotdb:dnid=all*/DROP TABLE IF EXISTS `{t[0]}`;')
    except Exception as e:
        print(t[0])
        print(e)
        pass

# for i in range(1, 10):
#     if i in (10, 11):
#         continue
#     sql = f'/*!hotdb:dnid={i}*/show processlist;'
#     cursor.execute(sql)
#     ps = cursor.fetchall()
#     for p in ps:
#         if p[-1] == 'DROP TABLE IF EXISTS hotdb_heartbeat':
#             cursor.execute(f'/*!hotdb:dnid={i}*/kill {p[0]};')