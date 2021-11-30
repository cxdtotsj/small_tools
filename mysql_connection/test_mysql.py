# -*- coding: utf-8 -*-
# @Data : 2021-08-11

import mysql.connector
import mysql.connector.pooling
import pymysql

import pymysql

mysql_config = {
    'user': 'cxd',
    'password': 'cxd123456',
    'host': '192.168.220.102',
    'port': 3323,
    'database': 'hotdb_test'
}

# server_config = {
#     'user': 'zy',
#     'password': 'zy',
#     'host': '192.168.220.137',
#     'port': 2563,
#     'database': 'test_cxd'
# }

# mysql_config = {
#     'user': 'cara',
#     'password': '123456',
#     'host': '192.168.220.150',
#     'port': 3309,
#     'database': 'test_cxd'
# }

conn = pymysql.connect(**mysql_config, autocommit=True)

cursor = conn.cursor()

for i in range(1, 1000000):
    sql = f'''INSERT INTO `test` VALUES ({i})'''
    cursor.execute(sql)


# sql = '''CREATE TABLE `t_moduleoptset` (`id` int(11) NOT NULL AUTO_INCREMENT,`cid` bigint(20) NOT NULL DEFAULT '0' COMMENT '企业识别码',`modulecode` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '模块code',`viewtype` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '视图类型',`optcode` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '操作类别标识',`optname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '操作中文名',`enoptname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '操作英文名',`optmodulecode` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '操作模块code',`useflag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '&lt;0表示否&gt;是否启用',`iconuri` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '图标',`listoptflag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '列表操作',`listorderno` int(11) NOT NULL DEFAULT '0' COMMENT '列表操作排序',`detailoptflag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '详情操作',`detailorderno` int(11) NOT NULL DEFAULT '0' COMMENT '详情操作排序',`fastoptflag` tinyint(4) NOT NULL DEFAULT '0' COMMENT '快速操作',`fastorderno` int(11) NOT NULL DEFAULT '0' COMMENT '快速操作排序',`targetoptcode` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '操作模块optCode',PRIMARY KEY (`id`),UNIQUE KEY `uniq_moduleoptset` (`cid`,`modulecode`,`viewtype`,`optcode`,`optmodulecode`) USING BTREE) ENGINE=InnoDB AUTO_INCREMENT=3772 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='模块操作设置表';'''

# cursor.execute(sql)
# print(cursor.fetchall())