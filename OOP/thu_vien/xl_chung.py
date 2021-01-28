'''	Biến đối tượng, lập trình theo hướng đối tượng 
- Khai báo mặc định class, self, (object) có thể khai hoặc không oython vẫn tự hiểu
- Mặc định phải khai báo biến khởi tạo __init__(self, parameter1, para2, para3,...) 
'''


class xl_tivi(object):
	def __init__(self, _Ten, _Ky_hieu, _Don_gia_Nhap, _Don_gia_Ban, _So_luong_ton): 	# --> tham số, giá trị (tượng trưng cho thông tin về đối tượng)
	 
		self.Ten = _Ten
		self.Ky_hieu = _Ky_hieu						# thực hiện bước gán biến cho các giá trị/ tham số 
		self.Don_gia_Nhap = _Don_gia_Nhap
		self.Don_gia_Ban = _Don_gia_Ban
		self.So_luong_ton = _So_luong_ton
