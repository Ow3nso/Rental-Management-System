from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT

from backend.apis.authentication.views import auth_router
from backend.apis.apartments.views import apartment_router
from backend.apis.authentication.schemas import Settings

app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(apartment_router)

if __name__ == "__main__":
    app.run(debug=True, port=8080)