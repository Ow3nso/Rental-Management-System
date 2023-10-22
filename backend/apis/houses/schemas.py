from typing import Optional
from pydantic import BaseModel

class HouseModel(BaseModel):
    id:int
    house_number:str="A41"
    house_type:Optional[str]="Bungalow"
    rent:int=20000
    status:Optional[str]="Vacant"
    apartment:Optional[int]="Balozi Apartment"

    class Config:
        orm_model = True
        