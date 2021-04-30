from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, create_engine, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Lop(Base):
	__tablename__ = 'Lop'
	Ma_so = Column(String(50), nullable=False,primary_key=True)
	Ten = Column(String(200), nullable=False)

	def __str__ (self):
		return self.Ten

class Hoc_sinh(Base):
	__tablename__ = 'Hoc_sinh'
	Ma_so = Column(String(50), nullable=False, primary_key=True)
	Ho_ten = Column(String(200), nullable=False)
	Ten_dang_nhap = Column(String(200), nullable=False)
	Mat_khau = Column(String(50), nullable=False)
	Ma_so_Lop = Column(String(50), ForeignKey('Lop.Ma_so'), nullable=False)
	Email = Column(String(100), nullable=True)
	Phone = Column(String(50), nullable=True)
	lop = relationship(Lop, backref='hoc_sinh')

	def __str__(self):
		return self.Ho_ten


class Giao_vien(Base):
	__tablename__ = 'Giao_vien'
	Ma_so = Column(String(50), nullable=False, primary_key=True)
	Ho_ten = Column(String(200), nullable=False)
	Ten_dang_nhap = Column(String(200), nullable=False)
	Mat_khau = Column(String(50), nullable=False)

	def __str__(self):
		return self.Ho_ten

class Giang_day(Base):
	__tablename__ = 'Giang_day'
	id = Column(Integer, nullable=False, primary_key=True)
	Ma_so_Lop = Column(String(50), ForeignKey('Lop.Ma_so'), nullable=False)
	Ma_so_Giao_vien = Column(String(50), ForeignKey('Giao_vien.Ma_so'), nullable=False)
	lop = relationship (Lop, backref='giang_day')
	giao_vien = relationship(Giao_vien, backref='giang_day')

	def __str__(self):
		return self.id

class Nhan_xet(Base):
	__tablename__ = 'Nhan_xet'
	id = Column(Integer, nullable=False, primary_key=True)
	Noi_dung = Column(String(None), nullable=False)
	Diem_so = Column(Float(), nullable=True)
	Ma_so_Hoc_sinh = Column(String(50), ForeignKey('Hoc_sinh.Ma_so'), nullable=False)
	hoc_sinh = relationship(Hoc_sinh, backref='nhan_xet')

engine = create_engine('sqlite:///data/ql_truong_tieu_hoc.db')
Base.metadata.create_all(engine)
print('OK')
