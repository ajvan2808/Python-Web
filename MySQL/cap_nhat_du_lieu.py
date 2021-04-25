from mysql.connector import connect 

conn = connect(
	host = 'localhost',
	port = '8889',
	user = 'root',
	passwd = 'root',
	database = 'testdb'
)

chuoi_sql = 'UPDATE ql_lop_hoc SET Lop=%s, Ho_ten=%s WHERE Ma_so=%s'
cursor = conn.cursor()
cursor.execute(chuoi_sql, ('LH_4', 'Lan', 'HS_2'))
conn.commit()
print('Done')

conn.close()