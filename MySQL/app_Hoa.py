from flask import Flask, request, render_template
from libraries.xl_hoa import *
from libraries.xl_loaihoa import *

app = Flask(__name__)

@app.route('/')
def index():
	ds_hoa = doc_danh_sach_hoa()
	ds_loai_hoa = doc_danh_sach_loai_hoa()

	return render_template('index.html', DSHoa = ds_hoa, DSLoaiHoa=ds_loai_hoa)

@app.route('/loai-hoa/<int:ma_loai_hoa>')
def loai_hoa(ma_loai_hoa):
	ds_hoa = doc_danh_sach_hoa(ma_loai_hoa)
	ds_loai_hoa = doc_danh_sach_loai_hoa()

	return render_template('index.html', DSHoa = ds_hoa, DSLoaiHoa=ds_loai_hoa)

if __name__ =='__main__':
	app.run(debug=True)