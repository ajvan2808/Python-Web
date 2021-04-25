import sqlite3

ma_so = input('Mã số: ')
ten = input('Tên: ')

# Kết nối đến CSDL
conn = sqlite3.connect('du_lieu/ql_san_pham.db')

''' Thực hiện thêm dữ liệu vào database
Khi khai báo các giá trị sau VALUES cần khai báo đúng vị trị và số lượng 
tương ứng với các cột đã khai báo trong table
'''
# CÁCH 1 
chuoi_sql = 'INSERT INTO SanPham (Ma_so, Ten, Don_gia, Mo_ta, Danh_muc) VALUES (1, "Bạc Xỉu Đá", 29000, "Nếu Phin Sữa Đá dành cho các bạn đam mê vị đậm đà, thì Bạc Xỉu Đá là một sự lựa chọn nhẹ đô cà phê nhưng vẫn thơm ngon, chất lừ không kém!", "")'
conn.execute(chuoi_sql)
conn.commit()

# CÁCH 2
# chuoi_sql = 'INSERT INTO SanPham (Ma_so, Ten, Don_gia, Mo_ta, Danh_muc) VALUES (null, ?, ?, ?, ?, ?)'
# conn.execute(chuoi_sql, (ma_so, ten, 29000, "Nếu Phin Sữa Đá dành cho các bạn đam mê vị đậm đà, thì Bạc Xỉu Đá là một sự lựa chọn nhẹ đô cà phê nhưng vẫn thơm ngon, chất lừ không kém!", ""))
# conn.commit()

# # CÁCH 3
# chuoi_sql = 'INSERT INTO SanPham (Ma_so, Ten, Don_gia, Mo_ta, Danh_muc) VALUES (?, ?, ?, ?, ?)'
# conn.execute(chuoi_sql, (ma_so, ten, 29000, "Nếu Phin Sữa Đá dành cho các bạn đam mê vị đậm đà, thì Bạc Xỉu Đá là một sự lựa chọn nhẹ đô cà phê nhưng vẫn thơm ngon, chất lừ không kém!", ""))
# conn.commit()

# Ngắt kết nối với database
conn.close()