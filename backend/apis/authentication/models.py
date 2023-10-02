from backend.apis.authentication.database import Base
from sqlalchemy import Column, String, Integer, Boolean, Date


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(10000))
    email = Column(String(10000), unique=True)
    phonenumber =  Column(Integer)
    national_id = Column(Integer, unique=True)
    occupied_in = Column(String(10000))
    password =  Column(String(10000))
    date_join = Column(Date)
    date_exit = Column(Date, nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User {self.email}"