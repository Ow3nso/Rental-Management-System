# ----- In-built Libraries -----
from house.database import engine, Base
from house.models import House

# ----- migrations -----
Base.metadata.create_all(bind=engine)