# -*- coding: utf-8 -*-
# @Data : 2020-04-21

import pymysql
from pymysql.cursors import DictCursor


info =  {
    "host": "192.168.220.102",
    "port": 3323,
    "user": "root",
    "password": "root",
    "db": ""
}
# ssl = {
#     "ssl": {
#     "ca": r"D:\temp\ca.pem",
#     "cert": r"D:\temp\client-cert.pem",
#     "key": r"D:\temp\client-key.pem"
#     }
# }
client = pymysql.connect(autocommit=True, cursorclass=DictCursor, **info) # , ssl=ssl
cursor = client.cursor()
cursor.execute('status;')
data = cursor.fetchall()
print(data)