from flask import Flask, render_template, request, Markup       # để gọi các file nằm trong template, Markup dùng để ẩn html trên trình duyệt 
# import hàm request để gửi thông tin lên server vì có dùng method POST trong html

app = Flask(__name__)       


@app.route('/')     # ten mien chinh dai dien cho trang chu
def index():
    return "Test thử lần 1"

# @app.route('/in-loi-chao')              # đường dẫn tới sub-page được dẫn đến từ trang chủ phía trên 
# def in_loi_chao():
#     return 'Bài 1: In lời chào'

@app.route('/in-loi-chao', methods=['GET','POST'])      # methods trong python có 's'
def in_loi_chao():
    loi_chao = ''
    ho_ten = ''
    if request.form.get('HoTen'):                       # get ten bien là name của input html 
        ho_ten = request.form.get('HoTen')              # gán biến 
        loi_chao = "Hello " + ho_ten
        # print(ho_ten) --> to test after input 
                                                
    return render_template('Bai_1/Bai_1_2.html', loi_chao_output = loi_chao, HoTen = ho_ten)

@app.route('/tinh-toan-don-gian', methods=['GET', 'POST'])
def tinh_toan_don_gian():
    chuoi_kq = ''
    if request.form.get('Sothunhat'):
        so_thu_nhat = eval(request.form.get('Sothunhat'))
        so_thu_hai = eval(request.form.get('Sothuhai'))
        # thực hiện phép tính
        tong = so_thu_nhat + so_thu_hai
        hieu = so_thu_nhat - so_thu_hai
        tich = so_thu_nhat * so_thu_hai
        thuong = so_thu_nhat / so_thu_hai

        # xuất kết quả tính
        chuoi_kq = 'Tổng = ' + str(so_thu_nhat) + '+' + str(so_thu_hai)+ '=' + str(tong) + '<br>'
        chuoi_kq += 'Hiệu = ' + str(so_thu_nhat) + '-' + str(so_thu_hai)+ '=' + str(hieu) + '<br>'
        chuoi_kq += 'Tich = ' + str(so_thu_nhat) + '*' + str(so_thu_hai)+ '=' + str(tich) + '<br>'
        chuoi_kq = 'Thương = ' + str(so_thu_nhat) + '/' + str(so_thu_hai)+ '=' + str(thuong) + '<br>'           
    return render_template('Bai_1/Bai_1_3.html', ket_qua_output = Markup(chuoi_kq))     

if __name__ =='__main__':
    app.run(debug=True)               

# khai báo debug=True --> khi app còn ở chế độ dev, để có thể chỉnh sửa và cập nhật
# app.run(port=5000) --> không nhất thiết khai báo vì mặc định local host của python flask là 127.0.0.1:5000
# copy link local host và paste lên browser để chạy test 