from flask import Flask, render_template, request, Markup
from Buoi_3.thu_vien.xl_tt import *

app = Flask(__name__)

@app.route('/')
def thong_tin_cty_1():
    duong_dan = 'Buoi_3/du_lieu/Cong_ty.json'
    du_lieu = doc_file_json(duong_dan)

    # xuất dữ liệu từ json ra ngoài, định dạng lại dữ liệu theo html 
    chuoi_kq = '<h4> ' + du_lieu['Ten'] + '</h4>'
    chuoi_kq += '<p> Điện thoại: ' + du_lieu['Dien_thoai'] + '</p>'
    chuoi_kq += '<p> Địa chỉ: ' + du_lieu['Dia_chi'] + '</p>'
    chuoi_kq += '<p> Email: ' + du_lieu['Mail'] + '</p>'

    return render_template('Bai_2/Bai_2_1_a.html', du_lieu_output= Markup(chuoi_kq))

@app.route('/page-1')
def thong_tin_cty_2():
    duong_dan = 'Buoi_3/du_lieu/Cong_ty.json'
    du_lieu = doc_file_json(duong_dan)

    return render_template('Bai_2/Bai_2_1_b.html', TT_cong_ty=du_lieu)

@app.route('/page-2', methods=['GET', 'POST'])
def nhap_ho_ten_1():
    kq = ''
    if request.form.get('HoTen'):
        ho_ten = request.form.get('HoTen')
        ds_ho_ten = {
            "Ho_ten": ho_ten
            }
        # Thực hiện đọc file json
        duong_dan ='Buoi_3/du_lieu/Ho_ten.json'
        du_lieu = ghi_file_json(duong_dan, ds_ho_ten)
        if du_lieu:
            kq = 'Đã ghi tên vào danh sách thành công.'
        else:
            kq = 'Ghi tên không thành công.'

    return render_template('Bai_2/Bai_2_2_a.html', kq_output=kq)

@app.route('/page-2-1', methods=['GET', 'POST'])
def chinh_sua_ho_ten():
    chuoi_kq = ''
    ho_ten = ''
    if request.form.get('HoTen'):
        ho_ten = request.form.get('HoTen')

        # thực hiện đọc file json
        duong_dan = 'Buoi_3/du_lieu/Ho_ten.json'
        du_lieu = doc_file_json(duong_dan)

        # cập nhật key cho json
        du_lieu['Ho_ten'] = ho_ten

        # ghi lại vào json 
        kq = ghi_file_json(duong_dan, du_lieu)
        if kq:
            chuoi_kq = 'Đã cập nhật thành công.'
        else:
            chuoi_kq = 'Cập nhật không thành công.'
    return render_template('Bai_2/Bai_2_2_b.html', chuoi_kq_output=chuoi_kq, HoTen = ho_ten)       # ở đây có khai báo biến ho_ten do có gán key 

@app.route('/page-3', methods=['GET', 'POST'])          # luôn có lệnh methods=['GET', 'POST'] để lấy và trả về thông tin ra html
def dang_nhap():
    kq = ''
    if request.form.get('Username'):
        user_name = request.form.get('Username').strip()            #dùng strip() để loại bỏ kg trắng nếu user lỡ nhập 
        pass_word = request.form.get('Password').strip()

        # tạo đường dẫn đến file json và đọc file
        duong_dan = 'Buoi_3/du_lieu/NV_2.json'
        ds_nv = doc_file_json(duong_dan)

        # xét dữ liệu đầu vô có trùng với dữ liệu trong json hay không 
        if ds_nv['Ten_dang_nhap'] == user_name and ds_nv['Mat_khau'] == pass_word:
             kq = 'Đăng Nhập Thành Công.'
        else:
             kq = 'Mật khẩu hoặc Tên đăng nhập không chính xác!' 

    return render_template('Bai_2/Bai_2_3.html', chuoi_kq_output=kq)

if __name__=='__main__':
    app.run(debug=True)