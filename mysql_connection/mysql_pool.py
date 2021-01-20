# -*- coding: utf-8 -*-
# @Data : 2021-01-20

'''
mysql-connector 连接池

'''

import mysql.connector
import mysql.connector.pooling

mysql_config = {
    'user': 'cxd',
    'password': '123456',
    'host': '192.168.220.102',
    'port': 3323,
    'database': 'hotdb_test'
}

pool = mysql.connector.pooling.MySQLConnectionPool(pool_name='my_pool', pool_size=3, pool_reset_session=True, **mysql_config)

for i in range(10):
    cnx = pool.get_connection()
    cursor = cnx.cursor()
    cursor.execute('''SELECT * FROM a;''')
    print(cursor.fetchall())
    cursor.close()
    cnx.close()
