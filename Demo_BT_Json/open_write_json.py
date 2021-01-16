import json

ds_hoc_sinh = [
    {
        "Ma_so": "HS01",
        "Ho_ten": "Họ tên 1",
        "Dia_chi": "TPHCM"
    },
    {
        "Ma_so": "HS02",
        "Ho_ten": "Họ tên 2",
        "Dia_chi": "Hà Nội"
    },
    {
        "Ma_so": "HS03",
        "Ho_ten": "Họ tên 3",
        "Dia_chi": "Cà Mau"
    }
]


f = open('ds_hoc_sinh.json', 'w', encoding='utf-8')
json.dump(ds_hoc_sinh, f, indent=4, ensure_ascii=False)
f.close()

# Hoặc f = open('ds_hoc_sinh.json','w', encoding='utf-8') để tạo file ngoài folder buoi_1