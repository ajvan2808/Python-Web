'''
DOM: Document Object Model là nền của XML. 
- Tài liệu XML có cấu trúc thứ bậc của các đơn vị thông tin gọi là node. 
- XML DOM cung cấp 1 API cho phép lập trình viên thêm, chỉnh sửa, hoặc xoá các node trong xml tại bất kỳ điểm nào để tạo ứng dụng 
- Ngoài DOM còn có SAX, tuy nhiên SAX chỉ có thể hỗ trợ dọc dữ liệu ra ngoài, dữ liệu được lưu trong bộ nhớ lưu trữ.
- DOM cho phép thực hiện thao tác 2 chiều và dữ liệu được lưu trong RAM.
'''

# input module
from xml.dom.minidom import parse

# Tài liệu 
tai_lieu = parse('files_xml/phim.xml')

# Node root: đơn vị thông tin gốc 
node_root = tai_lieu.documentElement

# Danh sách các node con 
ds_phim = node_root.getElementsByTagName('PHIM')

# Lấy các phần tử trong danh sách
for phim in ds_phim:
	ten = phim.getAttribute('Ten')
	nam_sx = phim.getAttribute('Nam_san_xuat')

	the_loai = phim.getElementsByTagName('The_loai')[0] # lấy tới <the_loai>
	noi_dung_the_loai = the_loai.childNodes[0].data # the_loai chỉ chứa 1 phần tử là list nên ta lấy từ index 0 

	dinh_dang = phim.getElementsByTagName('Dinh_dang')[0]
	noi_dung_dinh_dang = dinh_dang.childNodes[0].data 

	# truy xuất dữ liệu có sắp xếp 
	print('---- ', ten.upper(), ' ----')
	print('Năm sản xuất: ', nam_sx)
	print('Thể loại: ', noi_dung_the_loai)
	print('Định dạng: ', noi_dung_dinh_dang)
	
	