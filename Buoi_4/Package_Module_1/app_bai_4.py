from flask import render_template, request, Markup
from Package_Module_1 import app
from Package_Module_1.thu_vien.xl_tt import *
import os
from datetime import datetime

@app.route('/ngay-dang-nhap', methods=['GET', 'POST'])
def cap_nhat_ngay_dang_nhap():
	chuoi_kq = ''
	if request.form.get('TenDangNhap'):
		ten_dang_nhap = request.form.get('TenDangNhap')
		mat_khau = request.form.get('MatKhau')
		duong_dan = 'Package_Module_1/du_lieu/NV_2.json'
		du_lieu = doc_file_json(duong_dan)
		# du_lieu['Ngay_dang_nhap'] = ''
		# kq = ghi_file_json(duong_dan, du_lieu)	--> tạo key Ngay_dang_nhap vì dict cũ chưa có, chỉ để tham khảo vì json cần có sẵn, bởi khi run nếu để lệnh key sẽ được tạo thêm lần nữa
		
		# gán biến và chuyển đổi datetime
		if ten_dang_nhap == du_lieu['Ten_dang_nhap'] and mat_khau == du_lieu['Mat_khau']:
			du_lieu['So_lan_Dang_nhap'] += 1
			# du_lieu['Ngay_dang_nhap'] = datetime.now().strftime('%d-%m-%Y') 	#strftime: chuyển từ định dạng datetime sang chuỗi theo date-month-year hoặc ngược lại 
			ghi_file_json(duong_dan, du_lieu)

			chuoi_kq = '<p> Xin chào ' + du_lieu['Ho_ten'] + '</p>'
			chuoi_kq += '<p> Đây là lần đăng nhập thứ : ' + str(du_lieu['So_lan_Dang_nhap']) + '</p>'
			chuoi_kq += '<p> Ngày đăng nhập gần nhất: ' + du_lieu['Ngay_dang_nhap'] + '</p>'  # trả về ngày đăng nhập gần nhất
			du_lieu['Ngay_dang_nhap'] = datetime.now().strftime('%d-%m-%Y')					# override ngày cũ bằng ngày mới 
			ghi_file_json(duong_dan, du_lieu)

		else:
			chuoi_kq = 'Đăng nhập không thành công.'

	return render_template('Bai_4/Bai_4_1.html', kq_output=Markup(chuoi_kq))

@app.route('/tat-toan-so-tiet-kiem', methods=['GET', 'POST'])
def tat_toan_tk():
	chuoi_kq = ''
	so_stk = ''
	if request.form.get('SoSTK'):
		so_stk = request.form.get('SoSTK')
		cmnd = request.form.get('CMND')
		duong_dan = 'Package_Module_1/du_lieu/' + so_stk + '.json'
		if os.path.exists(duong_dan):
			du_lieu = doc_file_json(duong_dan)
			if du_lieu['CMND'] == cmnd:
				# gán biến và thực hiện tính toán
				lai_suat_ngay = du_lieu['Lai_suat_nam']/365/100
				# tính ngày gửi
				ngay_bd_gui = datetime.strptime(du_lieu['Ngay_gui'], '%Y-%m-%d') # chuyển chuổi ngày gửi trong json sang dạng datetime
				ngay_tat_toan = datetime.now() 
				tong_ngay_gui = (ngay_tat_toan - ngay_bd_gui).days
				#tính lãi suát và tổng tiền 
				tien_lai = tong_ngay_gui * lai_suat_ngay * du_lieu['Tien_gui']
				tong_tien = tien_lai + du_lieu['Tien_gui']
				formatted_tong_tien = '{:0,.2f}'.format(tong_tien)
				formatted_tien_lai = '{:0,.2f}'.format(tien_lai)

				# xuất kết quả ra screen 
				chuoi_kq = '<p> Họ tên khách hàng: ' + du_lieu['Ho_ten'] + '</p>'
				chuoi_kq += '<p> Tiền gửi: ' + str('{:,}'.format(du_lieu['Tien_gui'])) + '</p>'
				chuoi_kq += '<p> Ngày bắt đầu: ' + du_lieu['Ngay_gui'] + '</p>'
				chuoi_kq += '<p> Lãi suất: ' + str(du_lieu['Lai_suat_nam']) + '%</p>'
				chuoi_kq += '<p> Thời gian gửi: ' + str(tong_ngay_gui) + '</p>'
				chuoi_kq += '<p> Tiền lãi: ' + formatted_tien_lai + '</p>'
				chuoi_kq += '<p> Tổng tiền : ' + formatted_tong_tien + '</p>'
			else:
				chuoi_kq = 'Mật khẩu không chính xác. Vui lòng nhập lại'
		else:
			chuoi_kq = 'Không có Sổ tiết kiệm này. Vui lòng nhập lại mã số chính xác.'
	return render_template('Bai_4/Bai_4_2.html', kq_output=Markup(chuoi_kq), SoSTK=so_stk)