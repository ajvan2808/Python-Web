from Shop.thu_vien.xl_chung import *

@app.route('/shop-page')
def shop_page():

	return render_template('Shop/shop.html')