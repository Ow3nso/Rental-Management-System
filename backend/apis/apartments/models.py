#import modules
from backend.apis.apartments.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType

#create db tables and column
class Apartment(Base):
    TYPES = (
        ('Apartment','Apartment'),
        ('Bungalow', 'Bungalow'),
        ('Real Estate', 'Real Estate'),
        ('Masionette', 'Massionette'),
        ('Others', 'Others')
    )

    __tablename__= "Apartments"
    id = Column(Integer, primary_key=True)
    name = Column(String(10000))
    type =  Column(ChoiceType(choices=TYPES), default="Apartment")
    country = Column(String(10000))
    town =  Column(String(10000))

    def __repr__(self):
        return f"<Apartment{self.name}"