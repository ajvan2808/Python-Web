import sqlite3

# Kết nối đến CSDL
conn = sqlite3.connect('du_lieu/ql_san_pham.db')

# Tạo chuỗi sql , có 2 cách 
''' 
Cách 1: chọn tất cả thông tin từ table 

chuoi_sql = 'SELECT * FROM Hocsinh'
'''
# Cách 2
chuoi_sql = 'SELECT Ma_so, Ten, Don_gia, Mo_ta, Danh_muc FROM SanPham'
cursor = conn.execute(chuoi_sql) 
for dong in cursor:
	print(dong)

# *** Nhớ ngắt kết nối với database ***
conn.close()