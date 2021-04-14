from CoffeeShop.thu_vien.xl_chung import *
from CoffeeShop.thu_vien.xl_sp import *
from CoffeeShop.thu_vien.xl_form import *
from datetime import datetime
from flask_wtf.form import Form

# Xử lý hình ảnh 
UPLOAD_FOLDER = app.static_folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
	# Đọc danh sách
	danh_sach_san_pham = doc_danh_sach_san_pham()
	danh_sach_san_pham_hien_thi = danh_sach_san_pham 	# tạo biến phụ cho tìm kiếm 

	# tìm kiếm 
	tu_khoa = ''
	if request.form.get('TimKiem'):
		tu_khoa = request.form.get('TimKiem')
		danh_sach_san_pham_hien_thi = tra_cuu_san_pham(tu_khoa, danh_sach_san_pham)

	# truy xuất
	chuoi_html_danh_sach_san_pham = tao_chuoi_html_danh_sach_sp(danh_sach_san_pham_hien_thi)

	return render_template('Trang_chu.html', ChuoiHTMLDanhSachSanPham=chuoi_html_danh_sach_san_pham, TimKiem=tu_khoa)

@app.route('/dang-ky-thanh-vien', methods=['GET', 'POST'])
def dang_ky_thanh_vien():
	form = FormDangKyThanhVien()
	chuoi_kq = ''

	if form.validate_on_submit():
		# Gán biến 
		ho_ten = request.form.get('HoTen')	# HoTen là biến của class FormDangKyThanhVien 
		ten_dang_nhap = request.form.get('TenDangNhap')
		mat_khau = request.form.get('MatKhau')
		xac_nhan_mk = request.form.get('XacNhanMatKhau')

		# khởi tạo dict đối tượng 
		thanh_vien = {
			"Ho_ten": ho_ten,
			"Ten_dang_nhap": ten_dang_nhap,
			"Mat_khau": mat_khau,
			"Xac_nhan_mat_khau": xac_nhan_mk
		}

		# Lấy ten_dang_nhap làm tên file json 
		ten_file = ten_dang_nhap.split('@')[0]	# Bỏ '@' ở vị trí index tìm thấy đầu tiên 
		duong_dan = thu_muc_thanh_vien + ten_file + '.json'
		kq = ghi_file_json(duong_dan, thanh_vien)
		if kq:
			chuoi_kq = ''' 
			<div class="alert alert-success" role="alert">
			Đăng ký thành công.
			<a href="/" class="alert-link"> Quay lại trang chủ </a>
			</div>
			'''
		else:
			chuoi_kq = ''' 
			<div class="alert alert-danger" role="alert">
			Đăng ký không thành công.
			<a href="/" class="alert-link"> Quay lại trang chủ </a>
			</div>
			'''
	
	return render_template('Dang_ky_thanh_vien.html', Form=form, Chuoi_KQ=Markup(chuoi_kq))

@app.route('/gui-y-kien', methods=['GET', 'POST'])
def Gui_y_kien():
	form = FormGuiYKien()
	chuoi_kq = ''

	if form.validate_on_submit():
		# Gán biến 
		ho_ten = request.form.get('HoTen')
		tieu_de = request.form.get('TieuDe')
		dien_thoai = request.form.get('DienThoai')
		email = request.form.get('Email')
		dia_chi = request.form.get('DiaChi')
		y_kien = request.form.get('YKien')
		ngay_hien_hanh = datetime.now()

		# Lấy hình ảnh được upload về 
		f = form.HinhAnh.data
		ten_hinh = f.filename 
		if ten_hinh != '':
			f.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/y_kien/' + ten_hinh))
		
		# Tạo đối tượng 
		y_kien = {
			"Ho_ten": ho_ten,
			"Tieu_de": tieu_de,
			"Dien_thoai": dien_thoai,
			"Email": email,
			"Dia_chi": dia_chi,
			"Y_kien": y_kien,
			"Ngay_gui": ngay_hien_hanh.strftime('%Y-%m-%d')
		}

		# Ghi dữ liệu 
		ten_file = ngay_hien_hanh.strftime('%Y%m%d%H%M%S')
		duong_dan = thu_muc_y_kien + ten_file + '.json'
		kq = ghi_file_json(duong_dan, y_kien)
		if kq:
			chuoi_kq = ''' 
			<div class="alert alert-success" role="alert">
			Gửi thành công.
			<a href="/" class="alert-link"> Quay lại trang chủ </a>
			</div>
			'''
		else:
			chuoi_kq = ''' 
			<div class="alert alert-danger" role="alert">
			Gửi không thành công.
			<a href="/" class="alert-link"> Quay lại trang chủ </a>
			</div>
			'''
	return render_template('Gui_y_kien.html', Form=form, Chuoi_KQ=Markup(chuoi_kq))