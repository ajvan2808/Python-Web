from Shop.thu_vien.xl_chung import *

@app.route('/')
def index():

	return render_template('index/trang_chinh.html')