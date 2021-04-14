from CoffeeShop.thu_vien.xl_chung import *

def doc_danh_sach_nguoi_dung():   # function không cần tham số vì đã import function đọc file json
	danh_sach_nguoi_dung = doc_file_json(tap_tin_nguoi_dung) 
	return danh_sach_nguoi_dung


def nguoi_dung_dang_nhap(danh_sach_nguoi_dung, ten_dang_nhap, mat_khau):
	nguoi_dang_nhap = list(filter(lambda nguoi_dung: nguoi_dung['Ten_dang_nhap'] == ten_dang_nhap and nguoi_dung['Mat_khau'] == mat_khau,
									danh_sach_nguoi_dung))
	ket_qua = nguoi_dang_nhap[0] if len(nguoi_dang_nhap) ==1 else None

	return ket_qua


def tao_chuoi_html_thong_tin_nguoi_dung(ho_ten, nhom_nguoi_dung, url_dang_xuat):
	chuoi_html = '''
	<p>
		<div class="btn-group">
			<button type="button" class="btn btn-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				<strong> Xin Chào ''' + ho_ten + ''' </strong>
			</button>
			
			<div class="dropdown-menu">
				<a class="dropdown-item" href=" '''+ url_dang_xuat +''' ">Đăng xuất</a>
			</div>
		</div>
	</p>
	<p style="padding-left: 15px;"> '''+ nhom_nguoi_dung +''' </p>'
'''
	return Markup(chuoi_html)