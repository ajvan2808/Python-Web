import sqlite3

conn = sqlite3.connect('du_lieu/ql_hoc_sinh.db')

chuoi_sql = 'DELETE FROM HocSinh WHERE Ma_so=?'
conn.execute(chuoi_sql, ('HS08',))
conn.close()

# Cần có dấu phẩy đằng sau nếu chỉ có 1 phần tử được khai báo
# Do chuỗi khai báo dang ở dạng tuple, trong tuple nếu chỉ có 1 pt cần có dấu ',' đằng sau 