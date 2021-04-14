from flask import request, render_template, Markup, url_for, redirect, session, flash
import json 
from CoffeeShop import app 

# Tạo biến chung cho đường dẫn
thu_muc_san_pham = 'CoffeeShop/du_lieu/san_pham/'  # đường dẫn chung cho nhiều file sp khác nhau
tap_tin_nguoi_dung = 'CoffeeShop/du_lieu/Nguoi_dung/Nguoi_dung.json' 
url_dang_xuat = '/dang-xuat'
thu_muc_y_kien = 'CoffeeShop/du_lieu/y_kien/'	# tạo đường dẫn chung cho thư mục ý kiến và thành viên đăng ký
thu_muc_thanh_vien = 'CoffeeShop/du_lieu/nguoi_dung/'


# Tạo hàm xử lý file json
def doc_file_json(duong_dan):
	f = open(duong_dan, encoding='UTF-8')
	du_lieu = json.load(f)
	f.close()
	return du_lieu

def ghi_file_json(duong_dan, noi_dung):
	f = open(duong_dan, 'w', encoding='UTF-8')
	json.dump(noi_dung, f, ensure_ascii=False, indent=4)
	f.close()
	return True 
