from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserModel(BaseModel):
    id:Optional[int]
    fullname: str
    email:str
    phonenumber:int
    national_id:int
    occupied_in:str
    password:str
    date_join:date
    date_exit:date
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_model = True
        schema_extra = {
            'example':{
                "fullname":"John Doe",
                "email":"johndoe@email.com",
                "phonenumber":254707394018,
                "national_id":1234567890,
                "occupied_in":"Baringo",
                "password":"pasword",
                "date_join":"dd-mm-yy",
                "date_exit":"dd-mm-yy",
                "is_staff":False,
                "is_active":True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = 'v1e2abfce860b4277e360486d1425gf91e4799da310febd72b1d31489'

class LoginModel(BaseModel):
    email:str
    password:str