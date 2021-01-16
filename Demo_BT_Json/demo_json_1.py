import json

# Kết nối đến tập tin json
f = open('QLCT_1.json', encoding='utf-8')
du_lieu = json.load(f)          # mở ra tập tin là định dạng dict
f.close()

# Hiển thị thông tin công ty
cong_ty = du_lieu['CONG_TY'][0]     # Gọi và Gán giá trị đầu index 0 (là 1 dict) của CONG TY (là 1 list) trong file json du_lieu
print("Tên công ty:", cong_ty['Ten'])       # Gọi phần tử 'Ten'nằm trong dict của 1 list trong phần tử Cong Ty
print("Địa chỉ:", cong_ty['Dia_chi'])

# Tổng số nhân viên
don_vi = du_lieu['DON_VI']  # gọi DON_VI trong json
tong_nv = 0
for dv in don_vi:           # dv là phần tử bất kỳ trong don_vi 
    tong_nv += int(dv['So_Nhan_vien'])          # So_Nhan_vien trong don vi là str nên cần chuyển thành int
print("Tổng số nhân viên:", tong_nv)

# Thống kê nhân viên theo đơn vị
print('--- Thống kê nhân viên theo đơn vị ---')
stt = 0
for dv in don_vi:
    stt += 1
    print(stt, '/ Tên đơn vị:', dv['Ten'])
    print('\t- Số nhân viên:', dv['So_Nhan_vien'])
    print('\t- Tỷ lệ', dv['Ty_le'], '%')