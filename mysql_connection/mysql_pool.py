# -*- coding: utf-8 -*-
# @Data : 2021-01-20

'''
mysql-connector 连接池

'''

import mysql.connector
import mysql.connector.pooling

import pymysql

mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': '192.168.220.137',
    'port': 2553,
    'database': 'jwytest'
}

# conn = mysql.connector.connect(**mysql_config, autocommit=True)
conn = pymysql.connect(**mysql_config, autocommit=True)
cursor = conn.cursor()

# sql = rf'''CREATE TABLE `t_global` /* hotdb:020503 SHARD BY global on datanode '1154,1155,1156' */ (id int not null auto_increment primary key, a int(10)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''

# cursor.executemany(''''insert into t01 values (null,1,1.1,1.1,curdate(),now(),now(),now(),2016,'a','a','a','a','1','1','a'),(null,1,1.2,1.1,curdate(),now(),now(),now(),2016,'b',NULL,'a','a','1','1','b');''')

# sql = '''/*!hotdb:dnid=all*/show tables;'''

# cursor.execute('show create table join_a_jwy;')
# print(cursor.fetchone())
# cursor.execute('''select * from join_a_jwy limit 2;''')
# data = cursor.fetchall()
# print(cursor.description)
# print(data)

a = None
b = 200
c = 'Z'
d = '二'
e = 'now()'

sql = f'''SELECT {a}, {b}, '{c}', '{d}', {e}'''

cursor.execute(sql)
print(cursor.fetchone())

# for i in range(5):
#     cursor = conn.cursor()
#     sql = '''select a.news_id, a.match_accum_wht as matching,  b.indu_code as code, b.indu_name as code_name from dws_news_indu_wht a  left join (     select distinct indu_code, indu_name     from dim_indu_ingr      where status = 1 and indu_std_code = 'sw1' )  b on a.indu_code = b.indu_code where a.status = 1 and a.news_id in ('206BF76F-4E71-4850-8A73-1455A1A75294');'''
#     cursor.execute(sql)
#     print(len(cursor.fetchall()))
#     cursor.close()
#     conn.reset_session()

# pool = mysql.connector.pooling.MySQLConnectionPool(pool_name='my_pool', pool_size=3, pool_reset_session=True, **mysql_config)

# for i in range(10):
#     cnx = pool.get_connection()
#     cursor = cnx.cursor()
#     sql = '''select a.news_id, a.match_accum_wht as matching,  b.indu_code as code, b.indu_name as code_name from dws_news_indu_wht a  left join (     select distinct indu_code, indu_name     from dim_indu_ingr      where status = 1 and indu_std_code = 'sw1' )  b on a.indu_code = b.indu_code where a.status = 1 and a.news_id in ('206BF76F-4E71-4850-8A73-1455A1A75294');'''
#     cursor.execute(sql)
#     print(len(cursor.fetchall()))
#     cursor.close()
#     cnx.close()




