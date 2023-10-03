#import modules
from pydantic import BaseModel
from typing import Optional

#create schema
class ApartmentModel(BaseModel):
    id:Optional[int]
    name:str
    type:Optional[str]
    country:str
    town:str

    class Config:
        orm_model = True
        schema_extra = {
            'example':{
                'name':'Balozi Villas',
                'type':'Bungalow',
                'country':'Kenya',
                'Town':'Nairobi'
            }
        }

