# ----- 3rd party libraries -----
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ----- In-Built Libraries -----
from property import PSQL_STR

# ----- Database configuration -----
engine = create_engine(PSQL_STR,
                        echo=True
)

Base = declarative_base()
Session = sessionmaker()