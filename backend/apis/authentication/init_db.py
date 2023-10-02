from backend.apis.authentication.database import Base, engine
from backend.apis.authentication.models import User

Base.metadata.create_all(bind=engine)