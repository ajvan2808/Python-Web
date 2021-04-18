from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.testing.config import db

# Gán biến 
Base = declarative_base()

# tạo class đối tượng 
class Lop(Base):
	__tablename__ = 'Lop'
	Ma_so = Column(String(50), nullable=False, primary_key=True)
	Ten = Column(String(200), nullable=False)

	def __str__(self):
		return self.Ten

''' 
- Tạo table tên Lop với cột Ma_so giới hạn 50 từ, ko được null và là primary_key 
- def __str__: khi được gọi sẽ trả về là giá trị của cột Ten 
'''

class Hoc_sinh(Base):
	__tablename__ = 'Hoc_sinh'
	Ma_so = Column(String(50), nullable=False, primary_key=True)	# primary_keu đặt cuối cùng 
	Ho_ten = Column(String(200), nullable=False)
	Ten_dang_nhap = Column(String(50), nullable=False)
	Mat_khau = Column(String(50), nullable=False)
	Ma_so_Lop = Column(String(50), ForeignKey('Lop.Ma_so'), nullable=False)
	Email = Column(String(100), nullable=True)
	Phone = Column(String(50), nullable=False)
	lop = relationship(Lop, backref='hoc_sinh')

	def __str__(self):
		return self.Ten_dang_nhap

class Giao_vien(Base):
	__tablename__= 'Giao_vien'
	Ma_so = Column(String(50), nullable=False, primary_key=True)
	Ho_ten = Column(String(200), nullable=False)
	Ten_dang_nhap = Column(String(200), nullable=False)
	Mat_khau = Column(String(50), nullable=False)

	def __str__(self):
		return self.Ho_ten

class Giang_day(Base):
	__tablename__= 'Giang_day'
	id = Column(Integer, primary_key=True,nullable=False, autoincrement=True)
	Ma_so_Lop = Column(String(50), ForeignKey('Lop.Ma_so'), nullable=False)
	Ma_so_Giao_vien = Column(String(50), ForeignKey('Giao_vien.Ma_so'), nullable=False)
	lop = relationship(Lop, backref='giang_day')
	giao_vien = relationship(Giao_vien, backref='giang_day')

class Nhan_xet(Base):
	__tablename__ = 'Nhan_xet'
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	Noi_dung = Column(String(None), nullable=True)
	Diem_so = Column(Float(), nullable=True)
	Ma_so_Hoc_sinh = Column(String(50), ForeignKey('Hoc_sinh.Ma_so'), nullable=False)
	hoc_sinh = relationship(Hoc_sinh, backref='nhan_xet')

engine = create_engine('sqlite:///du_lieu/ql_truong_tieu_hoc.db')	# khởi tạo file 
Base.metadata.create_all(engine)
print('OK')