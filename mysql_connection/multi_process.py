# -*- coding: utf-8 -*-
# @Data : 2022-11-07

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from collections.abc import Iterator
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
from typing import Union, Tuple, Callable, Iterator

from conf import PROCESS_NUM
from operation.public import common
from operation.public.common_sql import CommonSQL
from utils import util
from utils.logger import logger


class MultiProcessInsert:
    """批量插入数据"""

    def __init__(self, connect_key: Union[str, dict], total_num: int, signle_num=100, process_num=None, db_info=None) -> None:
        """
        :Args:
         - connect_info: <str> -> exp: from conf import DATABASES KEY | <dict> -> exp: {'host': '', 'port': 3306, 'user': '', 'password': '', db: ''}
         - total_num: 插入的总数据量
         - signle_num: 单个子进程程插入的数据量, 默认为 100
         - process_num: 子进程数, 默认为4
         - db_info: <core.DB> 类构造参数

        """
        self.db_info = {} if db_info is None else db_info
        self.connect_key = connect_key
        self.total_num = total_num
        self.signle_num = signle_num
        self.process_num = process_num
        if process_num is None:
            self.process_num = PROCESS_NUM

    @util.time_consuming
    def table_multi_insert(self, table_name: str, func=None, sqls=None):
        """
        多进程执行

        :Args:
         - table_name: 表名称
         - func: <function> 生成单条INSERT SQL的方法, eg: operation.public.common.insert_sql(table_name) -> str
         - sqls: 默认为None, 表示使用 operation.public.common 下默认的 auto_create 建表, 使用统一的 insert_sql 语句 
        """
        # with Pool(self.process_num) as pool:
        #     for _ in range(int((self.total_num / self.signle_num))):
        #         pool.apply_async(self.table_signle_insert, args=(table_name, func, sqls), error_callback=util.error_callback)
        #     pool.close()
        #     pool.join()
        with ProcessPoolExecutor(max_workers=self.process_num) as executor:
            executor.map(self.table_signle_insert, ((table_name, func, sqls) for _ in range(int((self.total_num / self.signle_num)))), timeout=30)


    # def table_signle_insert(self, table_name: str, func: Union[callable, None], sqls: Union[list, Iterator, None]):
    def table_signle_insert(self, args: Tuple[str, Callable, str]):
        """
        单个进程执行INSERT
        
        :Args:
         - table_name: 表名称
         - func: 生成单条INSERT SQL的方法, eg: operation.public.common.insert_sql(table_name) -> str
         - sqls: 单个进程需要执行的SQL
        """
        table_name, func, sqls = args
        # 如果不传 sqls, 表示使用 operation.public.common 下默认的 auto_create 建表, 使用统一的 insert_sql
        if func is None:
            func = common.insert_sql
        if sqls is None:
            sqls = self.yield_sql(func, table_name)
        if not isinstance(sqls, (list, Iterator)):
            logger.error(f'param <sqls> must be Iterator, now is: {type(sqls)}')
        try:
            db_session = CommonSQL(self.connect_key, autocommit=False, **self.db_info)
            for sql in sqls:
                db_session.insert(sql)
            db_session.commit()
        finally:
            db_session.close_db()
    
    def yield_sql(self, func: Union[Callable, None], table_name: str):
        """
        批量生成单个进程需要执行的SQLs
        
        :Args:
         - func: 随机生成单条INSERT SQL的方法
         - table_name: 表名称
        """
        for _ in range(self.signle_num):
            yield func(table_name)

    def insert_sql(self, table_name):
        return f"insert into {table_name} (id,name,age) values (null, '{util.random_name_en(n=10)}', 1);"

    def thread_pool_callback(self, worker):
        worker_exception = worker.exception()
        if worker_exception:
            logger.exception(f'Thread Exception: {worker_exception}')
            exit(1)


if __name__ == '__main__':
    info = {
        "host": '192.168.250.10',
        "port": 3323,
        "user": 'autotest',
        "password": 'auto123456',
        "db": ""
    }
    multi_insert = MultiProcessInsert(info, 50000, 100, process_num=16, db_info={'db': 'om_test'})
    multi_insert.table_multi_insert('org_modify', multi_insert.insert_sql, None)
