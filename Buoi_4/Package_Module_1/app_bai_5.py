from flask import render_template, request, Markup
from Package_Module_1 import app
from Package_Module_1.thu_vien.xl_tt import *
from datetime import datetime
import os 

@app.route('/cap-quyen-dang-nhap', methods=['GET','POST'])
def cap_quyen_dang_nhap():
	chuoi_kq = ''
	cap_quyen = ''
	if request.form.get('QuyenDN'):
		quyen = request.form.get('QuyenDN')
		# Cách 1 theo lệnh if else thông thường 
		# if quyen == '1':
		# 	cap_quyen = 'True'
		# else:
		# 	cap_quyen = 'False'

		# Cách 2: lệnh shorthand 
		cap_quyen = 'True' if quyen == '1' else 'False'

		duong_dan = 'Package_Module_1/du_lieu/NV_2.json'
		du_lieu = doc_file_json(duong_dan)
		du_lieu['Quyen_dang_nhap'] = cap_quyen
		kq = ghi_file_json(duong_dan, du_lieu)
		if kq:
			chuoi_kq = 'Đã kích hoạt quyền đăng nhập.'
		else: 
			chuoi_kq = 'Đã huỷ quyền đăng nhập.'

	return render_template('Bai_5/Bai_5_1.html', Chuoi_KQ=chuoi_kq)

@app.route('/dang-nhap-voi-quyen-dang-nhap', methods=['GET', 'POST'])
def dang_nhap_voi_QDN():
	chuoi_kq = ''
	if request.form.get('TenDangNhap'):
		ten_dang_nhap = request.form.get('TenDangNhap')
		mat_khau = request.form.get('MatKhau')
		duong_dan = 'Package_Module_1/du_lieu/NV_2.json'
		du_lieu = doc_file_json(duong_dan)
		if ten_dang_nhap == du_lieu['Ten_dang_nhap'] and mat_khau == du_lieu['Mat_khau']:
			if du_lieu['Quyen_dang_nhap'] == 'True':
				du_lieu['So_lan_Dang_nhap'] += 1
				ghi_file_json(duong_dan, du_lieu)
				chuoi_kq = '<p> Xin chào ' + du_lieu['Ho_ten'] + '</p>'
				chuoi_kq += '<p> Đây là lần đăng nhập thứ : ' + str(du_lieu['So_lan_Dang_nhap']) + '</p>'
				chuoi_kq += '<p> Ngày đăng nhập gần nhất: ' + du_lieu['Ngay_dang_nhap'] + '</p>'  
				du_lieu['Ngay_dang_nhap'] = datetime.now().strftime('%d-%m-%Y')	 
				ghi_file_json(duong_dan, du_lieu)

			else:
				chuoi_kq = 'Tài khoản đã bị khoá quyền đăng nhập.'
		else:
			chuoi_kq = 'Đăng nhập thất bại. Kiểm tra lại thông tin.'

	return render_template('Bai_5/Bai_5_2.html', Chuoi_KQ=Markup(chuoi_kq))
		
@app.route('/xep-loai-hoc-luc', methods=['GET', 'POST'])
def xep_loai_hoc_luc():
	chuoi_kq = ''
	so_bao_danh = ''
	if request.form.get('SoBD'):
		so_bao_danh = request.form.get('SoBD')
		duong_dan = 'Package_Module_1/du_lieu/' + so_bao_danh + '.json'
		if os.path.exists(duong_dan):
			du_lieu = doc_file_json(duong_dan)

			# xếp loại học lực theo điểm trung bình 
			if du_lieu['Diem_trung_binh'] <5:
				hoc_luc = 'Yếu'
			elif du_lieu['Diem_trung_binh'] < 6.5:
				hoc_luc = 'Trung Bình'
			elif du_lieu['Diem_trung_binh'] < 8:
				hoc_luc = 'Khá'
			else:
				hoc_luc = 'Giỏi'

			chuoi_kq = '<p> Họ tên: ' + du_lieu['Ho_ten'] + '</p>'
			chuoi_kq += '<p> Số CMND: ' + du_lieu['CMND'] + '</p>'
			chuoi_kq += '<p> Lớp: ' + du_lieu['Lop'] + '</p>'
			chuoi_kq += '<p> Điểm trung bình: ' + str(du_lieu['Diem_trung_binh']) + '</p>'
			chuoi_kq += '<p> Xếp loại học lực: ' + hoc_luc + '</p>'

		else:
			chuoi_kq = 'Không tìm thấy mã số ' + so_bao_danh 
	return render_template('Bai_5/Bai_5_3.html', Chuoi_KQ=Markup(chuoi_kq), SoBD=so_bao_danh)

@app.route('/dang-ky-thanh-vien', methods=['GET', 'POST'])
def dang_ky_thanh_vien():
	chuoi_kq = ''
	if request.form.get('HoTen'):
		ho_ten = request.form.get('HoTen')
		email_dn = request.form.get('EmailDN')
		mat_khau = request.form.get('MatKhau')
		xac_nhan_mk = request.form.get('XacNhanMatKhau')
		gioi_tinh = request.form.get('GioiTinh')
		doi_tuong = request.form.get('DoiTuong')
		ngay_dang_ky = datetime.now()  # tên file thành viên sẽ là ngày giờ đăng ký 

		# tạo dict cho đối tượng 
		thanh_vien = {
			"Ho_ten": ho_ten,
			"Email": email_dn,
			"Mat_khau": mat_khau,
			"Gioi_tinh": gioi_tinh,
			"Doi_tuong": doi_tuong
		}

		if mat_khau == xac_nhan_mk:
			# Cách 1: Lưu từng thành viên thành từng file json riêng biệt (quy ước tên là %Y%m%d%H%M%S)
			# duong_dan = 'Package_Module_1/du_lieu/thanh_vien/' + ngay_dang_ky.strftime('%Y%m%d%H%M%S') + '.json'
			# kq = ghi_file_json(duong_dan, thanh_vien)
			# chuoi_kq = 'Đăng ký thành công.'

			# Cách 2: Ghi tất cả vào cùng 1 file json thanh_vien
			duong_dan = 'Package_Module_1/du_lieu/thanh_vien/thanh_vien.json'
			du_lieu = doc_file_json(duong_dan) #--> list
			du_lieu.append(thanh_vien)
			kq = ghi_file_json(duong_dan, du_lieu)
			if kq:
				chuoi_kq = 'Đăng ký thành công'
			else:
				chuoi_kq = 'Đăng ký không thành công. Hệ thống xảy ra lỗi.'
		else:
			chuoi_kq = 'Mật khẩu không trùng khớp.'
	return render_template('Bai_5/Bai_5_4.html', Chuoi_KQ=chuoi_kq)
