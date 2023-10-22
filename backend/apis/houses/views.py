#import modules
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder

from backend.apis.houses.database import engine, Session
from backend.apis.houses.schemas import HouseModel
from backend.apis.houses.models import House

#configure router and decorator
house_router = APIRouter(
    prefix="/house",
    tags=["house"]
)

session = Session(bind=engine)

#post method endpoint
@house_router.post("/houses", status_code=status.HTTP_201_CREATED)
async def add_house(house:HouseModel):
    try:
        new_house = House(
            house_number=house.house_number,
            house_type = house.house_type,
            rent = house.rent,
            status = house.status,
            apartment = house.apartment
        )
        session.add(new_house)
        session.commit()
        response = {
            "house_number":house.house_number,
            "house_type":house.house_type,
            "rent":house.house_rent,
            "status":house.rent,
            "apartment":house.apartment
        }
        return jsonable_encoder(response)
    except Exception as e:
        session.rollback()
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Bad Request"
                             )

#get route endpoint to get all houses
@house_router.get("/houses", status_code=status.HTTP_200_OK)
async def get_all_houses():
    try:
        houses =  session.query(House).all()
        return jsonable_encoder(houses)
    except Exception as e:
        session.rollback()
        raise e

#update route endpoint
@house_router.put("/houses/{house_id}", status_code=status.HTTP_200_OK)
async def update_house_details(id:int, house:HouseModel):
    try:
        house_to_update =  session.query(House).filter(House.id==id).first()

        house_to_update.house_number = house.house_number
        house_to_update.house_type = house.house_type
        house_to_update.rent = house.rent
        house_to_update.status = house.status
        house_to_update.apartment = house.apartment

        session.commit()

        response = {
            "house_number":house.house_number,
            "house_type":house.house_type,
            "rent":house.house_rent,
            "status":house.rent,
            "apartment":house.apartment
        }
        return jsonable_encoder(response)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Bad  Request"
                             )