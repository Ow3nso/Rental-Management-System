# ----- 3rd Party Libraries -----
import os
from dotenv import load_dotenv

# ----- Database Configuration -----
load_dotenv()
PSQL_STR = os.getenv('DATABASE_URL')