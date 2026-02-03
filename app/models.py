from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    zip_code = Column(String)
    status = Column(String)
    price = Column(Float)
    bed = Column(Float)
    bath = Column(Float)
    acre_lot = Column(Float)
    house_size = Column(Float)