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

# conn = mysql.connector.connect(**mysql_config)

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




