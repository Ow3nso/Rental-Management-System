#seeting up database for storage of data
#import modules
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#create engine with postgres account
engine =  create_engine(
    'postgresql://postgres:Nyamburi@localhost/Rental_mgt_sys',
                        echo=True
)

Base = declarative_base()
Session = sessionmaker()