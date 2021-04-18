from thu_vien.xl_model import *
from sqlalchemy.orm import sessionmaker
import json
import os 

# Build internal functions
def doc_file_json(duong_dan):
	f = open(duong_dan, encoding='utf-8-sig')
	noi_dung = json.load(f)
	f.close()
	return noi_dung

def doc_du_lieu(thu_muc):
	danh_sach = []
	for tap_tin in os.listdir(thu_muc):
		duong_dan = thu_muc + tap_tin
		noi_dung = doc_file_json(duong_dan)
		danh_sach.append(noi_dung)
	return danh_sach


# Kết nối đến CSDL
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()

# Đọc Lớp học và ghi vào CSDL 
''' 
lop: dict trong json
lop_hoc: đối tượng
Lop: class trong xl_model
'''


thu_muc_lop_hoc = 'du_lieu/Lop_hoc/'
danh_sach_lop = doc_du_lieu(thu_muc_lop_hoc)
for lop in danh_sach_lop:
	lop_hoc = Lop(Ma_so=lop['Ma_so'], Ten=lop['Ten'])
	session_sqlalchemy.add(lop_hoc)
	session_sqlalchemy.commit()
else:
	print('Done!')



# Đọc và ghi dữ liệu Giao_vien

thu_muc_gv = 'du_lieu/Giao_vien/'
danh_sach_gv = doc_du_lieu(thu_muc_gv)
for gv in danh_sach_gv:
	giao_vien = Giao_vien(Ma_so=gv['Ma_so'], Ho_ten=gv['Ho_ten'],
							Ten_dang_nhap=gv['Ten_dang_nhap'], Mat_khau=gv['Mat_khau'])
	session_sqlalchemy.add(giao_vien)
	session_sqlalchemy.commit()
else:
	print('Done!')

thu_muc_hs = 'du_lieu/Hoc_sinh/'
danh_sach_hs = doc_du_lieu(thu_muc_hs)
for hs in danh_sach_hs:
	hoc_sinh = Hoc_sinh(Ma_so=hs['Ma_so'], Ho_ten=hs['Ho_ten'],
						Ten_dang_nhap=hs['Ten_dang_nhap'],
						Mat_khau=hs['Mat_khau'],
						Ma_so_Lop=hs['Ma_so_Lop_hoc'],
						Email='',
						Phone='')
	session_sqlalchemy.add(hoc_sinh)
	session_sqlalchemy.commit()
else:
	print('Done!')

# Xoá học sinh theo lớp 
# ds = session_sqlalchemy.query(Hoc_sinh).filter(Hoc_sinh.Ma_so_Lop == 'LH_2').all()
# for dong in ds:
# 	session_sqlalchemy.delete(dong)
# 	session_sqlalchemy.commit()
