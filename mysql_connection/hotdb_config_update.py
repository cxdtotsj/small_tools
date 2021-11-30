'''
SERVER自动化环境升级脚本

升级步骤:
1. 清除257所有表信息，移除自动建表表配置
2. 部署 V258 环境, 导入258配置库
3. 使用同步工具，同步257配置库至258配置库
4. 执行以下脚本方法（修改对应版本号）
'''


import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from mysql_connection.myclinet import DB

ip_146 = '192.168.220.146'
ip_147 = '192.168.220.147'
ip_148 = '192.168.220.148'
ip_149 = '192.168.220.149'
port1 = 3307
port2 = 3308
port3 = 3309
db01 = 'autohotdb258'
db02 = 'autocross258'
db03 = 'auto_vertical_258'
datasource_infos1 = [(ip_146, port1), (ip_146, port2), (ip_146, port3), (ip_147, port1), (ip_147, port2), (ip_147, port3), (ip_148, port1), (ip_149, port2), (ip_149, port3)]
datasource_infos2 = [(ip_146, port2), (ip_146, port3), (ip_147, port2), (ip_147, port3)]
datasource_infos3 = [(ip_149, port2)]
db_info = {
    "host": None,
    "port": None,
    "user": "hotdb_datasource",
    "password": "hotdb_datasource",
    "db": ""
}

server_info = {
    "host": '192.168.220.137',
    "port": 3306,
    "user": "hotdb_config",
    "password": "hotdb_config",
    "db": "autohotdb_258_config"
}

def create_datasource_db():
    '''创建新的存储节点'''
    for dis in datasource_infos1:
        db_info.update({
            'host': dis[0],
            'port': dis[1]
        })
        s = DB(db_info)
        s.executeSQL_no_expection(f'''CREATE DATABASE `{db01}` /*!40100 DEFAULT CHARACTER SET utf8mb4 */''')
    for dis in datasource_infos2:
        db_info.update({
            'host': dis[0],
            'port': dis[1]
        })
        s = DB(db_info)
        s.executeSQL_no_expection(f'''CREATE DATABASE `{db02}` /*!40100 DEFAULT CHARACTER SET utf8mb4 */''')
    for dis in datasource_infos3:
        db_info.update({
            'host': dis[0],
            'port': dis[1]
        })
        s = DB(db_info)
        s.executeSQL_no_expection(f'''CREATE DATABASE `{db03}` /*!40100 DEFAULT CHARACTER SET utf8mb4 */''')

def update_datasource_config():
    '''修改配置库'''

    s = DB(server_info)
    sql_data = s.get_fetchall('''SELECT * FROM hotdb_datasource;''')
    for d in sql_data:
        source_id = d['datasource_id']
        new_name = d['datasource_name'][:-1] + '8'
        new_db_name = d['db_name'][:-1] + '8'
        for t in ('hotdb_datasource', 'hotdb_datasource_running'):
            print(f'''UPDATE {t} SET datasource_name="{new_name}", db_name="{new_db_name}" WHERE id={source_id};''')
            s.executeSQL_no_expection(f'''UPDATE {t} SET datasource_name="{new_name}", db_name="{new_db_name}" WHERE datasource_id={source_id};''')


if __name__ == "__main__":
    update_datasource_config()