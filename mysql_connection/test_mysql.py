# -*- coding: utf-8 -*-
# @Data : 2021-08-11

import time
import mysql.connector
import mysql.connector.pooling
import pymysql

import pymysql

mysql_config = {
    'user': 'cxd',
    'password': 'cxd123456',
    'host': '192.168.250.10',
    'port': 3323,
    'database': ''
}

mysql_source = {
    'user': 'hotdb_datasource',
    'password': 'hotdb_datasource',
    'host': '192.168.250.239',
    'port': 3200,
    'database': ''
}

conn = pymysql.connect(**mysql_config)
cursor = conn.cursor()

conn.select_db('SETLCENT_DB')
for i in range(10101, 10300):
    sql = f'''INSERT INTO noclr_fund_sbit_d VALUES ('AA{i}', '888841', 'H37020200{str(i).zfill(3)}', '1');'''
    cursor.execute(sql)
conn.commit()


# conn.select_db('SETLCENT_DB')
# for i in range(3001, 4000):
#     sql = f'''INSERT INTO `noclr_setl_d` VALUES ('AA{i}', 'H37020200{str(i).zfill(3)}', '2022-12-1', '2022-12-2', '2023-01-03 00:00:00', '11', '0', 'H37020200129', '1', '1');'''
#     cursor.execute(sql)
# conn.commit()

# conn.select_db('HIBIZ_DB')
# for i in range(1, 4000):
#     sql = f'''INSERT INTO med_grp_rlts_d VALUES (0, 'H37020200129', '1', 'H37020200129');'''
#     cursor.execute(sql)
# conn.commit()
