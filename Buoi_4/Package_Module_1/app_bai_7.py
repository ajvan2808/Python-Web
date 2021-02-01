from flask import render_template, request, Markup
from Package_Module_1.thu_vien.xl_tivi_1 import *
from Package_Module_1.thu_vien.xl_tt import *
from Package_Module_1.thu_vien.xl_cuoc_goi import *
from Package_Module_1 import app
from datetime import datetime
import os 


@app.route('/thong-tin-phieu-ban', methods=['GET','POST'])
def thong_tin_phieu_ban():
	duong_dan = 'Package_Module_1/du_lieu/TIVI_10.json'
	if os.path.exists(duong_dan):
		du_lieu = doc_file_json(duong_dan)

		# khởi tạo object 
		tivi = mytivi2(du_lieu['Ten'], du_lieu['Ma_so'], du_lieu['Ky_hieu'], du_lieu['Don_gia_Ban'],
						du_lieu['Don_gia_Nhap'], du_lieu['So_luong_Ton'],du_lieu['Danh_sach_Phieu_Ban'],
						du_lieu['Danh_sach_Phieu_Nhap'])
		tivi.Don_gia_Ban = '{:,}'.format(tivi.Don_gia_Ban)  # phải gán biến mới run được 
		str(tivi.So_luong_Ton)   # không cần gán biến vaxn run ????? 

	return render_template('Bai_7/Bai_7_1.html', Tivi=tivi, DuLieu=du_lieu)

@app.route('/ghi-cuoc-goi', methods=['GET', 'POST'])
def ghi_cuoc_goi_taxi():
	chuoi_kq = ''
	if request.form.get('NoiDi'):
		noi_di = request.form.get('NoiDi')
		noi_den = request.form.get('NoiDen')
		thoi_gian_goi = datetime.now()

		# khởi tạo đối tương 
		cuoc_goi = taxicall(noi_di, noi_den, thoi_gian_goi.strftime('%Y-%m-%d %H:%M:%S'))

		ten_file = thoi_gian_goi.strftime('%Y%m%d%H%M%S') + '.json'
		duong_dan = 'Package_Module_1/du_lieu/cuoc_goi/' + ten_file 
		kq = ghi_file_json(duong_dan, cuoc_goi.__dict__) # cuoc_goi dang là object cần chuyển về dict 

		if kq:
			chuoi_kq = 'Gọi Taxi thành công.'
		else: 
			chuoi_kq = 'Gọi Taxi không thành công.'
	
	return render_template('Bai_7/Bai_7_2.html', Chuoi_KQ = chuoi_kq)
		
# Không thể dùng jinja để output kết quả bằng if vì kq là Boolean và jinja nhận vào chuỗi kq = '' đầu tiên
# mà chuỗi rỗng là True nên html luôn hiện ra <p> Không thành công </p> 
# {% if KQ %}
# 	<p> Gọi thành công </p>
# {% else %}
# 	<p>Không thành công </p> 

@app.route('/danh-sach-cuoc-goi', methods=['GET', 'POST'])
def danh_sach_cuoc_goi():
	thu_muc_cuoc_goi = 'Package_Module_1/du_lieu/cuoc_goi/' 
	ds_cuoc_goi = [] 					# tạo list trong để add các dict từ json và output ra ngoài
	ngay_hien_tai = datetime.now()

	for ten_cuoc_goi in os.listdir(thu_muc_cuoc_goi):	# ten_cuoc_goi là 1 file bất kỳ trong list directories
		duong_dan = thu_muc_cuoc_goi + ten_cuoc_goi
		du_lieu = doc_file_json(duong_dan)

		#ds_cuoc_goi.append(du_lieu)			-->  ghi tất cả vào list đã tạo
		
		# HOẶC chỉ lấy theo ngày hiện hành
		if du_lieu['Thoi_gian'].split()[0] == ngay_hien_tai.strftime('%Y-%m-%d'):
			ds_cuoc_goi.append(du_lieu)

# tách Thoi_gian trong theo khg trắng và lấy p.t ở index 0

	return render_template('Bai_7/Bai_7_3.html', DS_Cuoc_Goi=ds_cuoc_goi)