# Đổ dữ liệu từ XMl vào db

from xml.dom.minidom import parse
import sqlite3

# Tạo biến dùng chung 
path_csdl = 'du_lieu/ql_nhan_vien.db'

# Khởi tạo kết nối đến csdl 
conn = sqlite3.connect(path_csdl)

# ------ ĐƠN VỊ -------
tai_lieu = parse('files_xml/don_vi.xml')

node_root = tai_lieu.documentElement

# Tạo danh sách Node con
ds_don_vi = node_root.getElementsByTagName('DON_VI')

for don_vi in ds_don_vi:
	_id = don_vi.getAttribute('ID')
	ten = don_vi.getAttribute('Ten')

	chuoi_sql = 'INSERT INTO DonVi VALUES(?,?)'
	conn.execute(chuoi_sql, (_id, ten))
	conn.commit()

# ------ NHÂN VIÊN -------
tai_lieu = parse('files_xml/nhan_vien.xml')

node_root = tai_lieu.documentElement

ds_nhan_vien = node_root.getElementsByTagName('NHAN_VIEN')

for nhan_vien in ds_nhan_vien:
	_id = nhan_vien.getAttribute('ID')
	ho_ten = nhan_vien.getAttribute('Ho_ten')
	gioi_tinh = nhan_vien.getAttribute('Gioi_tinh')
	ngay_sinh = nhan_vien.getAttribute('Ngay_sinh')
	cmnd = nhan_vien.getAttribute('CMND')
	muc_luong = nhan_vien.getAttribute('Muc_luong')
	dia_chi = nhan_vien.getAttribute('Dia_chi')
	id_don_vi = nhan_vien.getAttribute('ID_DON_VI')

	chuoi_sql = 'INSERT INTO NhanVien VALUES(?,?,?,?,?,?,?,?)'

	conn.execute(chuoi_sql, (_id, ho_ten, gioi_tinh, ngay_sinh, cmnd, muc_luong, dia_chi, id_don_vi))
	conn.commit()

conn.close()
