from flask import render_template, request, Markup
from Package_Module_1 import app
from Package_Module_1.thu_vien.xl_tt import *
import datetime
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
				chuoi_kq = 'Đăng nhập thành công.'
			else:
				chuoi_kq = 'Tài khoản đã bị khoá quyền đăng nhập.'
		else:
			chuoi_kq = 'Đăng nhập thất bại. Kiểm tra lại thông tin.'
	return render_template('Bai_5/Bai_5_2.html', Chuoi_KQ=chuoi_kq)
		
	
	
