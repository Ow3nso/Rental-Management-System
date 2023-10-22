#perform databse operations
from database import Base, engine
from models import House

Base.metadata.create_all(bind=engine)