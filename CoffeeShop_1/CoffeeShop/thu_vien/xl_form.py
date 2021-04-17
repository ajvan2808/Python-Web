from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, FileField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf.file import FileAllowed
from flask_ckeditor import CKEditorField 

# pip install flask_wtf tại terminal 

class FormDangKyThanhVien(FlaskForm):
	HoTen = TextField('Họ tên', [DataRequired()])
	TenDangNhap = TextField('Tên đăng nhập', [DataRequired(), Email('Email không hợp lệ!')])
	MatKhau = PasswordField('Mật khẩu', [DataRequired()])
	XacNhanMatKhau = PasswordField('Xác nhận mật khẩu', [DataRequired(), EqualTo('MatKhau', message='Mật khẩu không trùng khớp!')])
	HinhDaiDien = FileField('Hình đại diện', validators=[FileAllowed(['png', 'jpg', 'gif', 'jpeg'], message='Chỉ được upload hình ảnh')])
	DangKy = SubmitField('Đăng Ký')

class FormGuiYKien(FlaskForm):
	HoTen = TextField('Họ tên', [DataRequired()])
	TieuDe = TextField('Tiêu đề')
	DienThoai = TextField('Số điện thoại', [DataRequired()])
	Email = TextField('Email cá nhân', [DataRequired(), Email('Email không hợp lệ!')])
	DiaChi = TextField('Địa chỉ')
	YKien = TextAreaField('Ý kiến đóng góp', [DataRequired()])
	HinhAnh = FileField('Hình ảnh', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], message='Chỉ được upload file hình ảnh.')])
	GuiYKien = SubmitField('Gửi')