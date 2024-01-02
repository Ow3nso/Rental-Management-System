# ----- In-built Libraries -----
from property.database import engine, Base
from property.models import Property

# ----- migrations -----
Base.metadata.create_all(bind=engine)