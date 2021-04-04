# Ghi dữ liệu từ CSV vào XML

import csv
from xml.dom.minidom import Document

# Đọc dữ liệu từ csv
f = open('du_lieu/danh_sach_phim.csv', encoding='utf-8')
ds_phim = []
for dong in csv.reader(f):
	phim = {
		"Ten": dong[0],
		"Nam_sx": dong[1],
		"The_loai": dong[2],
		"Dinh_dang": dong[3]
	}
	ds_phim.append(phim)
f.close()

# Ghi dữ liệu từ csv vào xml
# Tạo tài liệu 
tai_lieu = Document()

# Node root (DANH_SACH)
node_root = tai_lieu.createElement('DANH_SACH')
tai_lieu.appendChild(node_root)
node_root.setAttribute('shelf', 'Danh sách phim')	# setAttribute: đặt giá trị cho node root, không nhất thiết lấy key là shelf

# Tạo các node con
for phim in ds_phim:
	# Node cha PHIM
	node_phim = tai_lieu.createElement('PHIM') # khởi tạo thì phải đi từ tai_lieu
	node_root.appendChild(node_phim) # PHIM nằm sau DANH_SACH nên append từ node_root là DANH_SACH
	node_phim.setAttribute('Nam_san_xuat', phim['Nam_sx'])
	node_phim.setAttribute('Ten', phim['Ten'])

	# Node con The_loai
	node_the_loai = tai_lieu.createElement('The_loai')
	node_phim.appendChild(node_the_loai)
	text_node_the_loai = tai_lieu.createTextNode(phim['The_loai']) # nội dung của node con ko thể dùng setAttribute
	node_the_loai.appendChild(text_node_the_loai)

	# Node con Dinh_dang 
	node_dinh_dang = tai_lieu.createElement('Dinh_dang')
	node_phim.appendChild(node_dinh_dang)
	text_node_dinh_dang = tai_lieu.createTextNode(phim['Dinh_dang'])
	node_dinh_dang.appendChild(text_node_dinh_dang)

f = open('files_xml/phim_moi.xml', 'w', encoding='utf-8') # tạo đường dẫn mới là phim_moi.xml 
tai_lieu.writexml(f, newl='\n', addindent='\t') 

# Lệnh ghi và lệnh cấu trúc file của xml khác với json 