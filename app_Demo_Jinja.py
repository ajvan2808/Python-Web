from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def vi_du_1():
    dtb = 5
    return render_template('vi_du_1.html', DTB=dtb)



@app.route('/vi-du-2')
def vi_du_2():
    ds_hoc_sinh = [
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

    return render_template('vi_du_2.html', DSHS=ds_hoc_sinh)



if __name__ == '__main__':
    app.run(debug=True, port=5001)