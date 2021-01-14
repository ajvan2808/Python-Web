from thu_vien import *

hoc_sinh = {
        "Ma_so": "HS05",
        "Ho_ten": "Họ tên 5",
        "Dia_chi": "TPHCM"
    }

duong_dan = 'buoi_1/ds_hoc_sinh.json'

du_lieu = doc_file_json(duong_dan)  # trả về list

du_lieu.append(hoc_sinh)

ghi_file_json(duong_dan, du_lieu)

# duongdan = 'ds_hoc_sinh.json'
# du_lieu = doc_file_json(duongdan)
# du_lieu.append(hoc_sinh)
# ghi_file_json(duongdan, du_lieu)