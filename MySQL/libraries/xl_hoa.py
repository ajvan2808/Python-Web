from libraries.xl_model_MySQL import *
from sqlalchemy.orm import sessionmaker

# KẾT NỐI CSDL
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()

def doc_danh_sach_hoa(ma_loai_hoa='all'):
	list_hoa = []

	if ma_loai_hoa == 'all':
		danh_sach_hoa = session_sqlalchemy.query(Hoa).all()
		for hoa in danh_sach_hoa:
			dict_hoa = {
				'Ma_hoa': Hoa.Ma_hoa,
				'Ma_loai_hoa': Hoa.Ma_loai_hoa,
				'Ten_hoa': Hoa.Ten_hoa,
				'Don_gia': Hoa.Don_gia,
				'Hinh_anh': Hoa.Hinh_anh,
				'Mo_ta': Hoa.Mo_ta
			}
			list_hoa.append(dict_hoa)
	else:
		danh_sach_hoa = session_sqlalchemy.query(Hoa).filter(Hoa.Ma_loai_hoa == ma_loai_hoa).all()
		for hoa in danh_sach_hoa:
			dict_hoa = {
			'Ma_hoa': Hoa.Ma_hoa,
			'Ma_loai_hoa': Hoa.Ma_loai_hoa,
			'Ten_hoa': Hoa.Ten_hoa,
			'Don_gia': Hoa.Don_gia,
			'Hinh_anh': Hoa.Hinh_anh,
			'Mo_ta': Hoa.Mo_ta
		}
		list_hoa.append(dict_hoa)
	
	return list_hoa