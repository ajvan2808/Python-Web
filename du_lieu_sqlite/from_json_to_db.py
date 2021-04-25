import sqlite3
import os
import json

thu_muc_san_pham = 'du_lieu/san_pham/'
tap_tin_db = 'du_lieu/ql_san_pham.db'

def doc_file_json(duong_dan):
	f = open(duong_dan, encoding='utf-8')
	du_lieu = json.load(f)
	f.close()
	return du_lieu

def ghi_file_json(duong_dan, noi_dung):
	f = open(duong_dan, 'w', encoding='utf-8')
	json.dump(noi_dung, f, ensure_ascii=False, indent=4)
	f.close()
	return True

def doc_danh_sach_san_pham():
	danh_sach = []
	for tap_tin in os.listdir(thu_muc_san_pham):
		duong_dan = thu_muc_san_pham + tap_tin
		san_pham = doc_file_json(duong_dan)
		danh_sach.append(san_pham)
	return danh_sach

# Truyền dữ liệu từ json vào database

danh_sach_san_pham = doc_danh_sach_san_pham()
conn = sqlite3.connect(tap_tin_db)

# Truyền dữ liệu từ json vào table DanhMuc trước
# Xử lý trùng Danh_muc['Ma_so']

'''
danh_muc_san_pham = {}
for san_pham in danh_sach_san_pham:
	danh_muc = san_pham['Danh_muc']
	ma_so = danh_muc['Ma_so']
	ten = danh_muc['Ten']
	mo_ta = danh_muc['Mo_ta']
	danh_muc_san_pham[ma_so] = [ten, mo_ta] 	# trong dict không có key trùng nhau
	
	# thực hiện truyền data từ json và DanhMuc trong db
for ma_so, gia_tri in danh_muc_san_pham.items():		# lấy từng items dict
	chuoi_sql = 'INSERT INTO DanhMuc VALUES (?, ?, ?)'
 	conn.execute(chuoi_sql, (ma_so, gia_tri[0], gia_tri[1]))
 	conn.commit()
'''

	#thực hiện truyền các data liên quan đến san_pham
for san_pham in danh_sach_san_pham:
	chuoi_sql = 'INSERT INTO SanPham VALUES (?, ?, ?, ?, ?, ?)'
	conn.execute(chuoi_sql, (san_pham['Ma_so'], san_pham['Ten'], san_pham['Don_gia'], san_pham['Mo_ta'],
							san_pham['Hinh_anh'], san_pham['Danh_muc']['Ma_so'])) # trong table SanPham danh_muc được ký hiệu bằng ma_so của DanhMuc
	conn.commit()

conn.close()

# Không thể thực hiện 2 lệnh truyền cùng lúc 
# Cần khai báo giá trị truyền vào đúng thứ tự và số lượng như trong db 