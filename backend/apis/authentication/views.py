import psycopg2

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from .database import Session, engine
from .schemas import UserModel,LoginModel

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

session = Session(bind=engine)

@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user:UserModel):

    db_email = session.query(User).filter(User.email==user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that email already exists"
        )

    db_nationalid = session.query(User).filter(User.national_id==user.national_id).first()
    if db_nationalid is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that ID number already exists"
        )

    try:    
        new_user = User(
            fullname = user.fullname,
            email = user.email,
            phonenumber = user.phonenumber,
            national_id = user.national_id,
            occupied_in = user.occupied_in,
            password = generate_password_hash(user.password),
            date_join = user.date_join,
            date_exit = user.date_exit,
            is_staff = user.is_staff,
            is_active = user.is_active
        )
        session.add(new_user)
        session.commit()
        response = {
            "fullname":user.fullname,
            "email":user.email,
            "phonenumber":user.phonenumber,
            "national_id":user.national_id,
            "occupied_in":user.occupied_in,
            "password":user.password,
            "date_join":user.date_join,
            "date_exit":user.date_exit,
            "is_staff":user.is_staff,
            "is_active":user.is_active
        }
        return jsonable_encoder(response)
    except (Exception,psycopg2.errors.UndefinedTable) as UndefinedTable:
            session.rollback()
            raise UndefinedTable

@auth_router.get("/signup", status_code=status.HTTP_200_OK)
async def get_all_tenants():
    tenants =  session.query(User).all()
    return jsonable_encoder(tenants)

@auth_router.post("/login", status_code=200)
async def loginuser(user:LoginModel, Authorize:AuthJWT=Depends()):
    db_user=session.query(User).filter(User.email==user.email).first()
    if db_user and check_password_hash(db_user.password, user.password):
        access_token = Authorize.create_access_token(subject=db_user.email)
        refresh_token = Authorize.create_refresh_token(subject=db_user.email)

        response={
            "access":access_token,
            "refresh":refresh_token
        }
        return jsonable_encoder(response)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Username or password"
        )

@auth_router.get("refresh")
async def refresh_token(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please provide a refresh token"
        )
    
    current_user = Authorize.get_jwt_identity()
    access_token = Authorize.create_access_token(subject=current_user)
    return jsonable_encoder({"access":access_token})
    