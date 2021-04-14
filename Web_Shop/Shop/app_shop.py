from Shop.thu_vien.xl_chung import *

@app.route('/shop-page')
def shop_page():

	return render_template('Shop/shop.html')

@app.route('/single-product')
def single_product():

	return render_template('Product/single_product.html')

@app.route('/cart')
def _cart():

	return render_template('Cart/cart.html')

@app.route('/checkout')
def _checkout():

	return render_template('Checkout/checkout.html')