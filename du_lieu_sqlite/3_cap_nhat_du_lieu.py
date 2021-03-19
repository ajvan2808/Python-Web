import sqlite3
# Kết nối đến db
conn = sqlite3.connect('du_lieu/ql_hoc_sinh.db')
# Cập nhật db
chuoi_sql = 'UPDATE HocSinh SET Dia_chi=? WHERE Ma_so_lop=?'
conn.execute(chuoi_sql, ('Hà Nội', 'LH01'))
conn.commit()

conn.close()

''' 
Giả thích câu lệnh cập nhật:
UPDATE bảng HocSinh VỚI Dia_chi = 'Hà Nội' TẠI các cột có Ma_so_lop = 'LH01'
'''