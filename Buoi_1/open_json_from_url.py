# Mở file json từ url và truy xuất dữ liệu 

from urllib.request import urlopen
import json


url = urlopen('http://lntpython.laptrinhpython.net:8181/dich-vu-san-pham/chi-tiet')
du_lieu = json.loads(url.read().decode())           #json.loads có s 
# print(du_lieu)
print(len(du_lieu))

# .ljust -> 1 ô chứa bằng 7 khoảng trắng được canh từ trái 

print("STT".ljust(7), "TÊN SẢN PHẨM".ljust(40), "HÌNH SẢN PHẨM".ljust(50), "GIÁ SIZE S".ljust(15), "GIÁ SIZE M".ljust(15))
stt = 0
for san_pham in du_lieu:
    stt += 1
    print(str(stt).ljust(7), san_pham['ten_san_pham'].ljust(40), san_pham['hinh_san_pham'].ljust(50), 
          str(san_pham['gia_size_s']).ljust(15), str(san_pham['gia_size_m']).ljust(15))

# stt, gia_size_s và gia_size_m là int nên cần lưu ý chuyển về str 