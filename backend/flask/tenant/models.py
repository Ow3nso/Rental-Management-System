# ----- 3rd Party Libraries -----
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, BigInteger, DateTime, ForeignKey

# ----- In-BUilt LIbraries -----
from house.models import House
from tenant.database import Base

# ----- Models -----
class Tenant(Base):
    __tablename__ = "tenant"
    id = Column(Integer, primary_key=True)
    name =  Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(BigInteger, nullable=False)
    password = Column(String, nullable=False, default="User@Pass123")
    joined_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    exit_date = Column(DateTime, nullable=True)
    house_id = Column(Integer, ForeignKey(House.id))
    houses = relationship(House, back_populates="houses")

    def __repr__(self):
        return f'<Tenant{self.email} +  {self.house_id}'