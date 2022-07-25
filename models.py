from decimal import Decimal
from database import Base
from sqlalchemy import Column, String


class Address(Base):
    __tablename__="address"

    id = Column(String(255), primary_key=True, index=True)
    address = Column(String(255),nullable=False)
    api_address = Column(String(255),nullable=False)
    latitude = Column(String(255))
    longitude = Column(String(255))