# -*- coding: utf-8 -*-
# @Author : chenxiaodong
# @Email  : chenxiaodong@hotdb.cn

import logging
import re
import time
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pymysql
from pymysql.cursors import DictCursor
from collections.abc import Iterable
from warnings import filterwarnings

DATABASES = {
    "hotdb_datasource": {
        "host": "192.168.210.62",
        "port": 3323,
        "user": "root",
        "password": "root",
        "db": "modify_db"
    }
}

filterwarnings("ignore", category=pymysql.Warning)

class DB:

    def __init__(self, connect_key=None,db_name=None):
        """
        :params connection_key: conf.py --> DATABASES
        :params db_name: 物理库名称, 当 connection_key 中无 db_name 时, db_name 必传

        """
        # 如果 connect_key 在 DATABASES 中已维护信息, 则取 DATABASES
        # 如果 connect_key 在 DATABASES 中不存在, 则 connect_key 就是连接信息
        try:
            if isinstance(connect_key, str):
                self.db_config = DATABASES[connect_key]
            else:
                self.db_config = connect_key
        except KeyError:
            logging.exception("数据库配置信息未获取")
        if db_name is not None:
            self.db_config["db"] = db_name
        self._conn = self.connect_db()
        self._cursor = self._conn.cursor()

    def connect_db(self):
        """
        连接MYSQL， 并返回操作游标

        :params config_key: conf.DATABASES 中，需要建立连接的Mysql配置信息
        """
        try:
            conn = pymysql.connect(autocommit=True, cursorclass=DictCursor, **self.db_config)
        except ConnectionError as e:
            logging.exception(f"数据库连接失败: {e}")
        return conn
    
    def get_fetchall(self, sql, is_hint=False, node_ids=None):
        """
        获取全部返回结果
        """
        if is_hint:
            sql = self.select_hint_deal(sql, node_ids)
        self._cursor.execute(sql)
        return self._cursor.fetchall()
        
    def get_fetchmany(self, sql, size=None):
        """
        获取指定的 N 行结果
        """
        self._cursor.execute(sql)
        return self._cursor.fetchmany(size)
    
    def get_fetchone(self, sql, is_hint=False, node_ids=None):
        """
        获取第一个返回结果
        """
        if is_hint:
            sql = self.select_hint_deal(sql, node_ids)
        self._cursor.execute(sql)
        return self._cursor.fetchone()
    
    def get_effect_row(self, sql, is_hint=False, node_ids=None):
        """
        获取返回的行数
        """
        if is_hint:
            sql = self.select_hint_deal(sql, node_ids)
        return self._cursor.execute(sql)

    def update(self, sql):
        """
        执行 UPDATE 语句
        """
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql)
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            logging.exception(f"数据库UPDATE更新失败, SQL: {sql}")
        finally:
            cursor.close()
    
    def insert(self, sql):
        """
        执行 INSERT 语句
        """
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql)
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            logging.exception(f"数据库INSERT插入失败, SQL: {sql}")
        finally:
            cursor.close()

    def insert_manay(self, sql, params=None):
        """
        执行 INSERT 语句
        """
        st = time.time()
        cursor = self._conn.cursor()
        try:
            cursor.executemany(sql, params) if params else cursor.executemany(sql)
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            logging.exception(f"数据库INSERT插入失败, SQL: {sql}")
        finally:
            cursor.close()
        logging.info("数据插入完成.==>> 耗时: {}'s.".format(round(time.time() - st, 3)))


    def delete(self, sql):
        """
        执行 DELETE 语句
        """
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql)
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            logging.exception(f"数据库DELETE删除失败, SQL: {sql}")
        finally:
            cursor.close()

    def exeuteSQL(self, sql):
        """执行SQL语句,报错回滚"""
        try:
            self._cursor.execute(sql)
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            logging.exception(f"数据库操作失败, SQL: {sql}")

    def exeuteSQLs(self, sqls, is_hint=False, node_ids=None):
        """批量执行SQL语句"""
        sqls = self.multi_sql_deal(sqls, is_hint, node_ids)
        for sql in sqls:
            self.exeuteSQL(sql)

    def executeSQL_no_expection(self, sql):
        """执行SQL, 不捕获异常"""

        cursor = self._conn.cursor()
        cursor.execute(sql)
        self._conn.commit()
        cursor.close()


    @staticmethod
    def multi_sql_deal(sqls, is_hint=False, node_ids=None):
        """SQL语句批量处理"""
        
        if isinstance(sqls, str):
            sqls = sqls.split(";")
            sqls = [x.replace('\n', ' ').strip() if '\n' in x else x.strip() for x in sqls]
        if not isinstance(sqls, Iterable):
            raise TypeError("sql type must be Iterable.")
        for sql in sqls:
            if sql == '':
                sqls.remove('')
        if is_hint:
            if isinstance(node_ids, int):
                sqls = [f"/*!hotdb:dnid={node_ids}*/{sql}" for sql in sqls]
            elif isinstance(node_ids, Iterable):
                sqls = [f"/*!hotdb:dnid={dnid}*/{sql}" for dnid in node_ids for sql in sqls]
            else:
                raise RuntimeError(f"Model of HINT, params -> node_ids: {node_ids} params error!")
        return sqls

    @staticmethod
    def select_hint_deal(sql, node_ids):
        """查询语句 SQL hint 处理"""
        if isinstance(node_ids, int):
            sql = f"/*!hotdb:dnid={node_ids}*/{sql}"
        elif isinstance(node_ids, Iterable):
            node_ids = ','.join((str(nid) for nid in node_ids))
            sql = f"/*!hotdb:dnid={node_ids}*/{sql}"
        return sql



    def close_db(self):
        """
        关闭数据库连接
        """
        self._cursor.close()
        self._conn.close()

    def executeSQLFromFile(self, filename):
        with open(filename, 'r', encoding='utf-8') as fd:
            sql_commands = fd.read().split(';')[:-1]
            sql_commands = [x.replace('\n', ' ') if '\n' in x else x for x in sql_commands]
        try:
            for sql in sql_commands:
                self._cursor.execute(sql)
        except Exception:
            self._conn.rollback()
            logging.exception("数据库操作失败, SQL: {sql}")
        finally:
            self._conn.commit()
            self._cursor.close()
        logging.info("SQL批量执行完成.")


if __name__ == '__main__':
    
    db = DB("hotdb_datasource")

    for i in range(10000):
        name = f"ming{i}"
        sql = f'insert into t_modify values (null, "{name}", {i});'
        db.insert(sql)