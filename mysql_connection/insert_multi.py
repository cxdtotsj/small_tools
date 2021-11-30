import logging
from mysql.connector.pooling import MySQLConnectionPool
from traceback import format_exc
from mysql.connector.errors import InternalError
import json


class MySqlHelper:
    _db_config = {
        'user': 'root',
        'password': 'root',
        'host': '192.168.240.147',
        'port': 3323,
        'database': 'hotdb_test',
    }

    def __init__(self):
        self._cur = None
        self._conn = None

    def __enter__(self):
        self._connect_database()
        return self

    def __exit__(self, _, value, trace):
        if isinstance(value, Exception):
            self._conn.rollback()
            self._close_db()
            raise value
        else:
            self._conn.commit()
            self._close_db()

    def _close_db(self):
        self._conn.close()

    def _connect_database(self):
        try:
            if not hasattr(MySqlHelper, "_cnxp"):
                MySqlHelper._cnxp = MySQLConnectionPool(
                    pool_name="mysql_helper",
                    pool_size=1,
                    host=self._db_config.get("host"),
                    user=self._db_config.get("user"),
                    password=self._db_config.get("password"),
                    database=self._db_config.get("database"),
                    port=self._db_config.get("port"),
                    raise_on_warnings=False,
                    auth_plugin="mysql_native_password",
                    charset="utf8mb4",
                    collation="utf8mb4_general_ci",
                )
            self._conn = MySqlHelper._cnxp.get_connection()
            self._conn.cursor().execute("")
        except Exception:
            logging.error("链接失败!")
            raise

    def exec_query(self, sql_query, param=()):
        if not self._conn:
            self._connect_database()
        try:
            self._cur = self._conn.cursor(dictionary=True)
            self._cur.execute(sql_query, param)
            result = list()
            for row in self._cur:
                result.append(row)
            self._cur.close()
            return result
        except Exception:
            message = "执行异常！执行的语句是%s,参数为%s" % (sql_query, str(param))
            logging.error(message)
            raise

    def exec_batch_query(self, sql, para=()):
        if not self._conn:
            self._connect_database()
        try:
            self._cur = self._conn.cursor(dictionary=True)
            if isinstance(para, list):
                self._cur.executemany(sql, para)
            else:
                self._cur.execute(sql, para)
            count = self._cur.rowcount
            self._cur.close()
            return count
        except Exception:
            message = "执行异常！执行的语句是%s,参数为%s" % (sql, str(para))
            logging.error(message)
            raise

    def exec_no_query(self, sql_query, param=()):
        if not self._conn:
            self._connect_database()
        try:
            self._cur = self._conn.cursor()
            self._cur.execute(sql_query, param)
            self._cur.close()
        except Exception:
            message = "执行异常！执行的语句是%s,参数为%s" % (sql_query, str(param))
            logging.error(message)
            raise

    def exec_prepared_batch_query(self, sql, para=()):
        if not self._conn:
            self._connect_database()
        try:
            # todo: 待处理, 设置prepared=True会导致某些情况下报data too long for column
            # self._cur = self._conn.cursor(prepared=True)
            self._cur = self._conn.cursor()
            if isinstance(para, list):
                for singer in para:
                    self._cur.execute(sql % singer)
            else:
                self._cur.execute(sql, para)
            count = self._cur.rowcount
            self._cur.close()
            return count
        except Exception:
            message = "执行异常！执行的语句是%s,参数为%s" % (sql, str(para))
            logging.error(message)
            raise

    def exec_scalar(self, sql, para=()):
        if not self._conn:
            self._connect_database()
        try:
            self._cur = self._conn.cursor(dictionary=True)
            self._cur.execute(sql, para)
            row = self._cur.fetchone()
            if row:
                result = None
                for cell in row:
                    result = row[cell]
                    break
                self._cur.close()
                return result
            else:
                return None

        except Exception:
            message = "执行异常！执行的语句是%s,参数为%s" % (sql, str(para))
            logging.error(message)
            raise

    def commit(self):
        try:
            if self._conn.unread_result:
                self._conn.commit()
        except InternalError:
            pass
        except Exception:
            message = "执行异常！事务提交失败！"
            logging.error(message)
            logging.error(format_exc())
            if self._conn:
                self._conn.rollback()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    query = """
INSERT INTO hotdb_test.dws_pufd_net_value (pufd_id,nv_date,swanav_post,swanav)
VALUES (%(pufd_id)s,%(nv_date)s,%(swanav_post)s,%(swanav)s)
ON DUPLICATE KEY UPDATE
swanav_post = values(swanav_post),swanav = values(swanav);
    """
    logging.info("SQL语句: {}".format(query))
    # with open("./data", "r", encoding="utf8") as file:
    #     data_list = json.loads(file.read())
    # data_list = data_list[:50]
    # for one in data_list:
    #     if one["swanav_post"] is not None:
    #         one["swanav_post"] = round(float(one["swanav_post"]),8)
    #         one["swanav_post"] = float(one["swanav_post"])
    data_list = [{'pufd_id': 303001, 'nv_date': '20130805', 'swanav_post': '0.9930000097895001803204895257', 'swanav': '0.993000'}]
    logging.info("数据数量: {}".format(len(data_list)))
    logging.info("开始: {}".format(len(data_list)))
    with MySqlHelper() as sql:
        res_count = sql.exec_batch_query(query, data_list)
    logging.info("写入: {}".format(res_count))

