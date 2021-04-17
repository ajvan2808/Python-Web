from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def diem_tb():
	dtb = 5
	return render_template('jinja_demo_1.html', Diem_tb=dtb)

@app.route('/xuat-du-lieu')
def xuat_du_lieu():
	ds_hs = [
        {
            "Ma_so": "HS01",
            "Ho_ten": "Học sinh 1",
            "Dia_chi": "TPHCM"
        },
        {
            "Ma_so": "HS02",
            "Ho_ten": "Học sinh 2",
            "Dia_chi": "Hà Nội"
        }
    ]
	return render_template('jinja_demo_2.html', DSHS=ds_hs)

if __name__ == "__main__":
	app.run(debug=True)
