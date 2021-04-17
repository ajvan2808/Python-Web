import json
ds_hoc_sinh_moi = [
    {
        "Ma_so": "HS10",
        "Ho_ten": "Họ tên A",
        "Dia_chi": "TPHCM"
    },
    {
        "Ma_so": "HS12",
        "Ho_ten": "Họ tên B",
        "Dia_chi": "Hà Nội"
    },
    {
        "Ma_so": "HS13",
        "Ho_ten": "Họ tên C",
        "Dia_chi": "Cà Mau"
    }
]

f = open('ds_hoc_sinh_moi.json','w', encoding='utf-8')
json.dump(ds_hoc_sinh_moi, f, indent=4, ensure_ascii=False)
f.close()

# Hoặc f = open('buoi_1/ds_hoc_sinh_moi.json','w', encoding='utf-8') để tạo file ngay trong folder buoi_1