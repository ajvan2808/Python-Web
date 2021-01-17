from flask import render_template, request
from Package_Module_1 import app

@app.route('/')
def index():
	return render_template('index.html')