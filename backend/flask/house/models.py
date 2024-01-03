# ----- 3rd Party Libraries -----
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# ----- In-Built Libraries -----
from house.database import Base
from property.models import Property

# ----- Models -----
class House(Base):
    __tablename__="house"
    id = Column(Integer, primary_key=True, nullable=False)
    house_number = Column(String, nullable=False)
    type = Column(String, nullable=False)
    rent = Column(Float, nullable=False)
    vacant = Column(Boolean, default=True, nullable=False)
    property_id = Column(Integer, ForeignKey(Property.id))
    property = relationship(Property, back_populates="houses")

    def __repr__(self):
        return f"<House{self.house_number}"