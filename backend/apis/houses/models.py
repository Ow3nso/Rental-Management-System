#import modules
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

from backend.apis.houses.database import Base
from backend.apis.apartments.models import Apartment

class House(Base):
    TYPE = (
        ('Bedsitter', 'Bedsitter'),
        ('Single room', 'Single room'),
        ('2 Bedroom', '2 Bedroom'),
        ('3 Bedroom',  '3 Bedroom'),
        ('4 Bedrrom', '4 Bedroom')
    )
    STATUS = (
        ('Vacant', 'Vacant'),
        ('Occupied', 'Occupied')
    )
    __tablename__= 'House'
    id = Column(Integer, primary_key=True)
    house_number = Column(String(1000))
    house_type = Column(ChoiceType(choices=TYPE), default="Bedsitter")
    rent = Column(Integer)
    status = Column(ChoiceType(choices=STATUS), default="Vacant")
    apartment_id  = Column(Integer, ForeignKey(Apartment.id), nullable=True)
    apartment =  relationship(Apartment, back_populates="houses")

    def __repr__(self):
        return f"<House {self.house_number}"