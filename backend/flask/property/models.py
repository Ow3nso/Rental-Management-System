# ----- 3rd Party Libraries -----
from sqlalchemy import Column, Integer, String

# ----- In-Built Libraries -----
from property.database import Base

# ----- Database table and fields -----
class Property(Base):
    __tablename__ = "property"
    id = Column(Integer, primary_key=True, nullable=False)
    name  = Column(String, nullable=False)
    type =  Column(String, nullable=False)
    country = Column(String, nullable=False)
    town = Column(String, nullable=False)
    landlord = Column(String, nullable=True)

    def __repr__(self):
        return f'<Property {self.name} + {self.landlord}'