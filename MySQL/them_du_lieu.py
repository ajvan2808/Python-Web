import mysql.connector
from mysql.connector import connect

conn = connect(
	host = 'localhost',
	port = '8889',
	user = 'root',
	passwd = 'root',
	database = 'testdb'
)

chuoi_sql = 'INSERT INTO ql_lop_hoc VALUES (%s, %s, %s)'	#MySQL tham số là %s
cursor = conn.cursor()
cursor.execute(chuoi_sql, ('HS_5', 'Sunny', 'LH_3'))
conn.commit()
print('Done')

conn.close()