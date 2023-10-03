#import modules
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

from backend.apis.apartments.database import engine, Session
from backend.apis.apartments.models import Apartment
from backend.apis.apartments.schemas import ApartmentModel

#configure router and decorator
apartment_router = APIRouter(
    prefix="/apartment",
    tags=["apartment"]
)

session = Session(bind=engine)

#post endpoint 
@apartment_router.post("/apartment", status_code=status.HTTP_201_CREATED)
async def add_apartment(apartment:ApartmentModel):
    try:
        new_apartment = Apartment(
            name = apartment.name,
            type = apartment.type,
            country = apartment.country,
            town = apartment.town
        )
        session.add(new_apartment)
        session.commit()
        response = {
            "name":apartment.name,
            "type":apartment.type,
            "country":apartment.country,
            "town":apartment.town
        }
        return jsonable_encoder(response)
    except Exception as e:
        session.rollback()
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request"
        )

#pagination route
@apartment_router.get("/apartment", 
                        status_code=status.HTTP_200_OK,
                    )
async def get_all_apartments():
    try:
        apartments = session.query(Apartment).all()
        return jsonable_encoder(apartments)
    except Exception as e:
        session.rollback()
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request"
        )

#update route
@apartment_router.put("/apartment/{apartment_id}", status_code=status.HTTP_200_OK)
async def update_apartments(id:int, apartment:ApartmentModel):
    try:
        apartment_to_update  = session.query(Apartment).filter(Apartment.id==id).first()

        apartment_to_update.name = apartment.name
        apartment_to_update.type = apartment.type
        apartment_to_update.country = apartment.country
        apartment_to_update.town = apartment.town

        session.commit()

        response = {
            "name":apartment.name,
            "type":apartment.type,
            "country":apartment.country,
            "town":apartment.town
        }
        return jsonable_encoder(response)
    except Exception as e:
        session.rollback()
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request"
        )