# -*- coding: utf-8 -*-
# @Data : 2022-08-19

import pymysql
from pymysql.cursors import DictCursor
import time
import mysql.connector

info = {
    'host': '192.168.240.148',
    'port': 3200,
    'user': 'hotdb_datasource',
    'password': 'hotdb_datasource',
    'db': 'test_zy',
    'charset': 'utf8'
}

# for i in range(10):
conn = pymysql.connect(**info)

cursor = conn.cursor()

cursor.execute('''select i,group_concat( i,j order by i,j) as cg,count(*) as a from dml_d_zy  group by i with rollup;''')

print(cursor.fetchall())