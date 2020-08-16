import jaydebeapi

jdbc_url = "jdbc:mysql://192.168.220.102:3323/ja_test?useCursorFetch=true"
user = "cxd"
pwd = "123456"
driver = "com.mysql.jdbc.Driver"
jar_file = './mysql-connector-java-5.1.47.jar'
sql = "select * from t_sharding;"

conn = jaydebeapi.connect(driver, jdbc_url, [user, pwd], jar_file)
# curs = conn.cursor()
curs = conn.jconn.
curs.execute(sql)
result = curs.fetchall()
print(result)
curs.close()
conn.close()