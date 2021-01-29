from flask import render_template, request, Markup
from Package_Module_1.thu_vien.xl_tt import *
from Package_Module_1.thu_vien.xl_tt_tivi import *
import os
from Package_Module_1 import app


@app.route('/xuat-thong-tin-tivi', methods=['GET', 'POST'])
def xuat_thong_tin_tv():
	ma_tivi = ''
	chuoi_kq = ''

	if request.form.get('MaTV'):
		ma_tivi = request.form.get('MaTV')

		# tạo đường dẫn tới từng file json để đọc file
		duong_dan = 'Package_Module_1/du_lieu/' + ma_tivi + '.json'
		if os.path.exists(duong_dan):
			du_lieu = doc_file_json(duong_dan)

			# Khởi tạo object và gán giá trị trong du_lieu cho tham số của object 
			tivi = mytivi(du_lieu['Ten'], du_lieu['Ma_so'], du_lieu['Ky_hieu'], du_lieu['Don_gia_Ban'], du_lieu['Don_gia_Nhap'],
						 	du_lieu['So_luong_Ton'], du_lieu['Danh_sach_Phieu_Ban'], du_lieu['Danh_sach_Phieu_Nhap'],
							du_lieu['Nhom_Tivi'])
			
			DonGiaBan = '{:,.1f}'.format(tivi.Don_gia_Ban)
			SoLuongTon = str(tivi.So_luong_ton)
			
			chuoi_kq = '<p> Tên: ' + tivi.Ten + '</p>'
			chuoi_kq += '<p> Giá: ' + DonGiaBan + '</p>'
			chuoi_kq += '<p> Số lượng còn: ' + SoLuongTon + '</p>'
			chuoi_kq += '<img src="/static/' + tivi.Ma_TV + '.png" class="img-fluid" alt="' + tivi.Ma_TV + '.png">'  # trả về hình ảnh tivi dynamically

		else:
			chuoi_kq = 'Không có sản phẩm cần tìm.'
	
	return render_template('Bai_6/Bai_6_1.html', MaTV= ma_tivi, Chuoi_KQ=Markup(chuoi_kq))

@app.route('/tinh-tien-ban-tivi', methods=['GET', 'POST'])
def tinh_tien_ban_tivi():
	chuoi_kq = ''

	duong_dan = 'Package_Module_1/du_lieu/TIVI_1.json'
	du_lieu = doc_file_json(duong_dan)
	tivi = mytivi(du_lieu['Ten'], du_lieu['Ma_so'], du_lieu['Ky_hieu'], du_lieu['Don_gia_Ban'],du_lieu['Don_gia_Nhap'],
					du_lieu['So_luong_Ton']) 

	if request.form.get('SoLuong'):
		so_luong = int(request.form.get('SoLuong'))
		if so_luong > tivi.So_luong_ton:
			chuoi_kq = 'Số lượng hàng còn ' + str(tivi.So_luong_ton)
		else:
			tong_don_gia = tivi.Don_gia_Ban * so_luong
			chuoi_kq = 'Tổng tiền = {:,.1f}'.format(tong_don_gia) 	# nếu chỉ .f nghĩa là tách tất cả các đơn vị bằng dấu chấm -->

	return render_template('Bai_6/Bai_6_2.html', Chuoi_KQ=chuoi_kq, Tivi=tivi)

@app.route('/nhap-thong-tin-tivi-moi', methods=['GET','POST'])
def nhap_thong_tin_tivi_moi():
	chuoi_kq = ''
	ten = ''
	ma_so = ''
	ky_hieu = ''
	don_gia_ban = ''
	don_gia_nhap = ''
	so_luong_ton = ''

	if request.form.get('Ten'):
		ten = request.form.get('Ten')
		ma_so = request.form.get('MaSo')
		ky_hieu = request.form.get('KyHieu')
		don_gia_ban = request.form.get('DonGiaBan')
		don_gia_nhap = request.form.get('DonGiaNhap')
		so_luong_ton = request.form.get('SoLuongTon')

		duong_dan = 'Package_Module_1/du_lieu/' + ma_so + '.json'
		tivi = mytivi(ten, ma_so, ky_hieu, don_gia_ban, don_gia_nhap, so_luong_ton)
		kq = ghi_file_json(duong_dan, tivi.__dict__) # tivi đang là object cần chuyển đổi về dict 
		
		if kq:
			chuoi_kq = 'Cập nhật hàng mới thành công.'
		else:
			chuoi_kq = 'Cập nhật thông tin không thành công.'

	return render_template('Bai_6/Bai_6_3.html', Chuoi_KQ=chuoi_kq,MaSo=ma_so,KyHieu=ky_hieu,
							DonGiaBan=don_gia_ban, DonGiaNhap=don_gia_nhap, SoLuongTon=so_luong_ton)
	
	# Cần khai báo biến, gán biến html mới có thể giữ kết quả user nhập vẫn hiện trên input sau khi submit