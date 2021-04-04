from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/bar-chart')
def bar_chart():

	return render_template('bar_chart.html')

@app.route('/line-chart')
def line_chart():

	return render_template('line_chart.html')

@app.route('/pie-chart')
def pie_chart():

	return render_template('pie_chart.html')



if __name__=='__main__':
	app.run(debug=True)
