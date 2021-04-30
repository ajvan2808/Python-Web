from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Float, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class LoaiHoa(Base):
	__tablename__ = 'LoaiHoa'
	Ma_loai = Column(Integer, primary_key=True)
	Ten_loai = Column(String(100), nullable=False)

	def __str__(self):
		return self.Ten_loai

class Hoa(Base):
	__tablename__= 'Hoa'
	Ma_hoa = Column(Integer, nullable=False, primary_key=True)
	Ma_loai_hoa = Column(Integer, ForeignKey('LoaiHoa.Ma_loai'))
	Ten_hoa = Column(String(100), nullable=False)
	Don_gia = Column(Integer)
	Hinh_anh = Column(String(200))
	Mo_ta = Column(String(200))
	loaihoa = relationship(LoaiHoa, backref='hoa')

	def __str__(self):
		return self.Ten_hoa

class KhachHang(Base):
	__tablename__ = 'KhachHang'
	Ma_khach_hang = Column(Integer, nullable=False, primary_key=True)
	Ten_dang_nhap = Column(String(200), nullable=False)
	Mat_khau = Column(String(100), nullable=False)
	Ho_ten = Column(String(200), nullable=False)
	Dia_chi = Column(String(200), nullable=False)
	Dien_thoai = Column(String(50), nullable=True)
	Email = Column(String(50), nullable=True)

	def __str__(self):
		return self.Ho_ten

engine = create_engine("mysql+pymysql://root:root@localhost:8889/qlbanhoa")
Base.metadata.create_all(engine)
print('OK')