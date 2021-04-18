from CoffeeShop.thu_vien.xl_chung import *
from CoffeeShop.thu_vien.xl_sp import *
from CoffeeShop.thu_vien.xl_Nguoi_dung import *
from werkzeug.utils import secure_filename 	# chuyển file sang BIT (hệ nhị phân) để gửi đi


# để tải file, thư mục lên mạng , browser
UPLOAD_FOLDER = app.static_folder
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "gif"])
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# kiểm tra file có hợp lệ hay không 
def allowed_file(filename):
	return "." in filename and filename.split(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Trang dành cho admin quản trị
@app.route('/admin/dang-nhap', methods=['GET', 'POST'])
def admin_dang_nhap():
	chuoi_kq = ''
	if request.form.get('TenDangNhap'):
		ten_dang_nhap = request.form.get('TenDangNhap')
		mat_khau = request.form.get('MatKhau')

		# thực hiện đọc danh sách người dùng
		danh_sach_nguoi_dung = doc_danh_sach_nguoi_dung()

		# thực hiện kiểm tra đăng nhập 
		nguoi_dang_nhap = nguoi_dung_dang_nhap(danh_sach_nguoi_dung, ten_dang_nhap, mat_khau)
		if nguoi_dang_nhap is not None:
			session['session_Admin'] = nguoi_dang_nhap 	# tạo 1 session là dict để lưu thông tin người nhập với key là session_Admin
			return redirect(url_for('admin'))
		else:
			chuoi_kq = 'Lỗi đăng nhập. Vui lòng kiểm tra lại thông tin.'

	# Chuyển hướng sang trang admin nếu người dùng đã đăng nhập 
	if session.get('session_Admin') is not None:
		return redirect(url_for('admin'))

	return render_template('Dang_nhap.html', ChuoiKQ=chuoi_kq)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
	# Chuyển hướng sang trang đăng nhập nếu chưa đăng nhập
	if session.get('session_Admin') is None:
		return redirect(url_for('admin_dang_nhap'))

	# thực hiện tạo biến cho người dùng vừa đăng nhập để hiển thị bên html
	ho_ten_nguoi_dung = session['session_Admin']['Ho_ten']
	nhom_nguoi_dung = session['session_Admin']['Nhom_nguoi_dung']['Ten'] 	# từ file Nguoi_dung.json
	
	# thực hiện đọc danh sách sản phẩm tương tự trang chủ sản phẩm
	danh_sach_san_pham = doc_danh_sach_san_pham()
	danh_sach_san_pham_hien_thi = danh_sach_san_pham	# biến phụ để thực hiện hiẻn thị lọc theo tìm kiếm

	# thực hiện tìm kiếm theo từ khoá 
	tu_khoa = ''
	if request.form.get('TimKiem'):
		tu_khoa = request.form.get('TimKiem')
		danh_sach_san_pham_hien_thi = tra_cuu_san_pham(tu_khoa, danh_sach_san_pham)

	# Xoá sản phẩm 
	chuoi_kq = ''
	if request.form.get('MaSo_Xoa'):
		ma_so_xoa = request.form.get('MaSo_Xoa')
		ten_hinh_xoa = request.form.get('TenHinh_Xoa')

		# xoá đường dẫn sản phẩm 
		duong_dan = thu_muc_san_pham + 'San_pham_' + ma_so_xoa + '.json'
		os.remove(duong_dan)

		# xoá hình sản phẩm, xét trường hợp sản phẩm có hình ảnh và không có hình ảnh 
		if ten_hinh_xoa != '':
			duong_dan_hinh = app.config['UPLOAD_FOLDER'] + '/san-pham/' + ten_hinh_xoa
			os.remove(duong_dan_hinh)
		
		chuoi_kq=''' 
		<div class="alert alert-success" role="alert"> Xoá sản phẩm thành công.
		<a href="/admin" class="alert-link"> Quay lại trang chủ </a>
		</div> 
		'''

		# Load lại danh sách sau khi xoá sản phẩm 
		danh_sach_san_pham = doc_danh_sach_san_pham()
		danh_sach_san_pham_hien_thi = danh_sach_san_pham
	
	# truy xuất
	chuoi_html_thong_tin_nguoi_dung = tao_chuoi_html_thong_tin_nguoi_dung(ho_ten_nguoi_dung, nhom_nguoi_dung, url_dang_xuat)
	chuoi_html_danh_sach_san_pham = tao_chuoi_html_danh_sach_sp_admin(danh_sach_san_pham_hien_thi)

	return render_template('Trang_chu.html', TimKiem=tu_khoa, 
							ChuoiHTMLThongTinNguoiDung=chuoi_html_thong_tin_nguoi_dung,
							ChuoiHTMLDanhSachSanPham=chuoi_html_danh_sach_san_pham,
							Chuoi_KQ=Markup(chuoi_kq))


@app.route('/admin/dang-xuat')
def admin_dang_xuat():
	session.pop('session_Admin', None)
	return redirect(url_for('admin_dang_nhap')) 

# url_for(tên function)

@app.route('/admin/them-san-pham', methods=['GET', 'POST'])
def admin_them_san_pham():
	# Chuyển hướng nếu chưa đăng nhập 
	if session.get('session_Admin') is None:
		return redirect(url_for('admin_dang_nhap'))
	# Đọc và kiểm tra thông tin đăng nhập 
	ho_ten_nguoi_dung = session['session_Admin']['Ho_ten']
	nhom_nguoi_dung = session['session_Admin']['Nhom_nguoi_dung']['Ten']
	
	# Thêm sản phẩm
	# đọc danh sách sản phẩm 
	chuoi_kq = ''
	if request.form.get('Ten'):
		danh_sach_san_pham = doc_danh_sach_san_pham()

		# gán biến 
		ma_so = tim_ma_san_pham_moi_nhat(danh_sach_san_pham) + 1
		ten_san_pham = request.form.get('Ten')
		don_gia_san_pham = int(request.form.get('DonGia'))
		mo_ta = request.form.get('MoTa')
		danh_muc = int(request.form.get('DanhMuc'))
		ten_danh_muc = lay_thong_tin_danh_muc(danh_sach_san_pham)[danh_muc]['Ten']
		mo_ta_danh_muc = lay_thong_tin_danh_muc(danh_sach_san_pham)[danh_muc]['Mo_ta']

		# thực hiện upload hình ảnh 
		# kiểm tra post request có file part hay chưa
		if 'file' not in request.files:
			flash('No file part')
		file = request.files['file']  # ['file'] chính là giá trị của type bên html

		# Trường hợp user không cần upload hình ảnh ngay lúc đó 
		if file.filename == '':
			filename = ''

		# Trường hợp user có upload hình ảnh 
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/san-pham/', filename))
		
		# tạo danh sách sản phẩm 
		san_pham = {
			"Ma_so": ma_so,
			"Ten": ten_san_pham,
			"Don_gia": don_gia_san_pham,
			"Mo_ta": mo_ta,
			"Hinh_anh": filename,
			"Danh_muc": {
				"Ma_so": danh_muc,
				"Ten": ten_danh_muc,
				"Mo_ta": mo_ta_danh_muc
			}, 
			"Danh_sanh_phieu_nhap": [],
			"Danh_sach_phieu_ban": []
		}

		# ghi dữ liệu thành file json trong '/du_lieu'
		duong_dan = thu_muc_san_pham + 'San_pham_' + str(ma_so) + '.json'
		kq = ghi_file_json(duong_dan, san_pham)
		if kq:
			chuoi_kq = ''' 
            <div class="alert alert-success" role="alert"> Thêm sản phẩm thành công 
				<a href="/admin" class="alert-link"> Quay lại trang chủ </a>
			</div>
            '''
		else:
			chuoi_kq = '''
			<div class="alert alert-danger" role="alert"> Thêm sản phẩm không thành công 
				<a href="/admin" class="alert-link"> Quay lại trang chủ </a>
			</div>
			'''
	chuoi_html_thong_tin_nguoi_dung = tao_chuoi_html_thong_tin_nguoi_dung(ho_ten_nguoi_dung, nhom_nguoi_dung, url_dang_xuat)
	return render_template('Them_san_pham.html', 
							ChuoiHTMLThongTinNguoiDung=chuoi_html_thong_tin_nguoi_dung,
							Chuoi_KQ=Markup(chuoi_kq))


@app.route('/admin/cap-nhat-san-pham/<int:ma_so>', methods=['GET', 'POST'])  # lưu ý giá trị dynamic vào link
def admin_cap_nhat_san_pham(ma_so):
	
	if session.get('session_Admin') is None:
		return redirect(url_for('admin_dang_nhap'))

	ho_ten_nguoi_dung = session['session_Admin']['Ho_ten']
	nhom_nguoi_dung = session['session_Admin']['Nhom_nguoi_dung']['Ten']
	
	# thực hiện cập nhật thông tin sản phẩm 
	danh_sach_san_pham = doc_danh_sach_san_pham()
	san_pham_chon = lay_chi_tiet_san_pham(danh_sach_san_pham, ma_so)
	ten_sp = san_pham_chon['Ten']
	don_gia_sp = san_pham_chon['Don_gia']
	mo_ta_sp = san_pham_chon['Mo_ta']

	chuoi_kq = ''
	if request.form.get('Ten'):
		ten_sp = request.form.get('Ten')
		don_gia_sp = int(request.form.get('DonGia'))
		mo_ta_sp = request.form.get('MoTa')

		# đọc file json cũ và ghi thông tin mới đè lên 
		duong_dan = thu_muc_san_pham + 'San_pham_' + str(ma_so) + '.json'
		san_pham = doc_file_json(duong_dan)
		san_pham['Ten'] = ten_sp
		san_pham['Don_gia'] = don_gia_sp
		san_pham['Mo_ta'] = mo_ta_sp

		kq = ghi_file_json(duong_dan, san_pham)
		if kq:
			chuoi_kq = '''
			<div class="alert alert-success role="alert"> Cập nhật thông tin thành công. 
				<a href="/admin" class="alert-link"> Quay lại trang chủ </a>
			</div>
			 '''
		else:
			chuoi_kq = ''' 
			<div class="alert alert-danger role="alert"> Cập nhật thông tin thất bại.
				<a href="/admin" class="alert-link"> Quay lại trang chủ </a>
			</div>
			'''

	chuoi_html_thong_tin_nguoi_dung = tao_chuoi_html_thong_tin_nguoi_dung(ho_ten_nguoi_dung, nhom_nguoi_dung, url_dang_xuat)
	return render_template('Cap_nhat_san_pham.html',
							ChuoiHTMLThongTinNguoiDung=chuoi_html_thong_tin_nguoi_dung,
							Ten=ten_sp, DonGia=don_gia_sp, MoTa=mo_ta_sp,
							Chuoi_KQ=Markup(chuoi_kq))


