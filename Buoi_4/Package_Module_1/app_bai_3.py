from flask import render_template, request, Markup
from Package_Module_1.thu_vien.xl_tt import *
from Package_Module_1 import app
import os 

@app.route('/so-lan-dang-nhap', methods=['GET', 'POST'])
def so_lan_dang_nhap():
	chuoi_kq = ''
	if request.form.get('TenDangNhap'):
		ten_dang_nhap = request.form.get('TenDangNhap').strip() 	# cắt bỏ khoẳng trắng nêú người nhập lỡ thêm
		mat_khau = request.form.get('MatKhau').strip()

		duong_dan = 'Package_Module_1/du_lieu/NV_2.json'
		du_lieu = doc_file_json(duong_dan)
		if ten_dang_nhap == du_lieu['Ten_dang_nhap'] and mat_khau == du_lieu['Mat_khau']:
			du_lieu['So_lan_Dang_nhap'] += 1
			ghi_file_json(duong_dan, du_lieu)

			chuoi_kq = '<p> Xin chào ' + du_lieu['Ten_dang_nhap']  + '<p>'
			chuoi_kq += '<p> Bạn đã đăng nhập ' + str(du_lieu['So_lan_Dang_nhap']) + ' lần.</p>'
		else:
			chuoi_kq = 'Đăng nhập thất bại!'
	return render_template('Bai_3/Bai_3_1.html', kq_output = Markup(chuoi_kq))

@app.route('/nhap-don-gia-tivi', methods=['GET', 'POST'])
def don_gia_ban_tivi():
	chuoi_kq = ''
	don_gia_ban = ''
	# duong_dan = 'Package_Module_1/du_lieu/TIVI_1.json'
	# du_lieu = doc_file_json(duong_dan)			# để hiện giá cũ trước khi nhập giá mới trong placeholder
	# don_gia_ban = du_lieu['Don_gia_Ban']

	if request.form.get('DonGiaBan'):
		don_gia_ban = eval(request.form.get('DonGiaBan'))
		duong_dan = 'Package_Module_1/du_lieu/TIVI_1.json'
		du_lieu = doc_file_json(duong_dan)
		du_lieu['Don_gia_Ban'] = don_gia_ban

		kq = ghi_file_json(duong_dan, du_lieu)
		if kq:
			chuoi_kq = 'Đã cập nhật giá bán Tivi là ' + "{:,}".format(int(du_lieu['Don_gia_Ban'])).replace(',', '.')
		else:
			chuoi_kq = 'Cập nhật không thành công.'
	return render_template('Bai_3/Bai_3_2.html', kq_output=chuoi_kq, DonGiaBan = don_gia_ban)

@app.route('/tinh-diem-xet-tuyen', methods=['GET', 'POST'])
def tinh_diem_xet_tuyen():
	chuoi_kq = ''
	so_bao_danh = ''
	if request.form.get('SoBaoDanh'):
		so_bao_danh = request.form.get('SoBaoDanh')
		duong_dan = 'Package_Module_1/du_lieu/' + so_bao_danh + '.json'

		# kiểm tra nếu đường dẫn có tồn tại trong hệ thống 
		if os.path.exists(duong_dan):
			du_lieu = doc_file_json(duong_dan)
			
			cmnd = str(request.form.get('CMND'))			# số cmnd nhập vào là int nên cần chuyển thành str cho cùng định dạng với cmnd trong json
			if (du_lieu['CMND']) == cmnd:
				chuoi_kq = '<p> Họ tên thí sinh: ' + du_lieu['Ho_ten'] + '</p>'
				chuoi_kq += '<p> Toán: ' + str(du_lieu['Toan']) + '</p>'
				chuoi_kq += '<p> Văn: ' + str(du_lieu['Van']) + '</p>'
				chuoi_kq += '<p> Anh: ' + str(du_lieu['Anh']) + '</p>'
			else: 
			 	chuoi_kq = 'Số CMND không chính xác.'
		else:
			chuoi_kq = 'Không tìm thấy số báo danh.'
	return render_template('Bai_3/Bai_3_3.html', kq_output=Markup(chuoi_kq), SoBaoDanh= so_bao_danh)
