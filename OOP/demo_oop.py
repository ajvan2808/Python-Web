from thu_vien.xl_chung import *

tivi = xl_tivi("LG OS", "LG OS", 30000000, 45000000, 10)
tivi_1 = xl_tivi("Samsung OLEG", "Samsung OLEG", 40000000, 55000000, 10)
tivi_2 = xl_tivi("Toshiba 14'", "Toshiba 14'", 40000000, 55000000, 9)

print(tivi.Ten)

ds_tivi = [tivi, tivi_1, tivi_2]
for tv in ds_tivi:
	tv = tv.Ten
	print(tv)

