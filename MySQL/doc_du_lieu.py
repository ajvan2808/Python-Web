import mysql.connector 
from mysql.connector import connect

# Kết nối đến CSDL
conn = connect(
	host = 'localhost',
	user = 'root',
	port = '8889',
	passwd = 'root',
	database = 'testdb'
)
# nhớ khai báo port 

#print('Done')

# Thực hiện ĐỌC DỮ LIỆU
chuoi_sql = 'SELECT * FROM ql_lop_hoc'
cursor = conn.cursor()
cursor.execute(chuoi_sql)
kq = cursor.fetchall()
for lines in kq:
	print(lines)

conn.close()