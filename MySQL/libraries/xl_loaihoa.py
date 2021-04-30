from libraries.xl_model_MySQL import *
from sqlalchemy.orm import sessionmaker

# KẾT NỐI CSDL
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()

def doc_danh_sach_loai_hoa():
	ds_loai_hoa = session_sqlalchemy.query(LoaiHoa).all()
	list_loai_hoa = []
	for loai_hoa in ds_loai_hoa:
		dict_loai_hoa = {
			'Ma_loai': loai_hoa.Ma_loai,
			'Ten_loai': loai_hoa.Ten_loai
		}
		list_loai_hoa.append(dict_loai_hoa)

	return list_loai_hoa