from mysql.connector import connect

conn = connect(
	host = 'localhost',
	port = '8889',
	user = 'root',
	passwd = 'root',
	database = 'testdb'
)

chuoi_sql = 'DELETE FROM ql_lop_hoc WHERE Ho_ten = "IU" '
cursor = conn.cursor()
cursor.execute(chuoi_sql)
conn.commit()
print('OK')

conn.close()