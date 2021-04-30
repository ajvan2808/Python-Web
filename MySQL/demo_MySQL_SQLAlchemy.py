from libraries.xl_model_MySQL import *
from sqlalchemy.orm import sessionmaker

# KẾT NỐI ĐẾN CSDL
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()