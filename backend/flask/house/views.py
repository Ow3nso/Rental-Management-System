# ----- 3rd Party Libraries -----
from flask import request
from flask_apispec import MethodResource, marshal_with, use_kwargs, doc
from flask_restful import Resource
from fastapi.encoders import jsonable_encoder
from fastapi import status

# ----- In-Built Libraries -----
from house.models import House
from house.schemas import HouseResponse, HouseModel
from house.database import sessionmaker, engine

# ----- database config -----
Session = sessionmaker()
session = Session(bind=engine)

# ----- pagination -----
class Paginate:
    @staticmethod
    def pagination():

        #pagination
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 100))
        next_offset = offset + limit
        previous_offset = offset - limit

        return offset, limit, next_offset, previous_offset

# ----- CPU Endpoints -----
class HouseViews(MethodResource, Resource):
    # post endpoint 
    @use_kwargs(HouseModel)
    @marshal_with(HouseResponse)
    def post(self, status_code=status.HTTP_201_CREATED, **kwargs):
        data:HouseResponse = request.json()
        try:
            # new house
            new_house = House(**data)

            # commit
            session.add(new_house)
            session.commit()

            #response
            return jsonable_encoder(data), status_code
        
        #error handling
        except Exception as e:
            session.rollback()
            raise e
    
    # get endpoint
    @use_kwargs(HouseModel)
    @marshal_with(HouseResponse)
    def get(self, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # pagination
            offset, limit, next_offset, previous_offset = Paginate.pagination() 

            house = session.query(House).offset(offset).limit(limit).all()

            #url to next and previous pages
            next_page_url = f'house?limit={str(limit)}&offset={str(next_offset)}' 
            previous_page_url = f'house?limit={str(limit)}&offset={str(previous_offset)}'

            #response to be returned
            response = {
                "property":jsonable_encoder(house),
                "next_page_url":next_page_url,
                "previous_page_url":previous_page_url,
                "offset": offset,
                "limit": limit,
                "has_more_records": len(house) == limit,
            }

            return response, status_code

        # error handling
        except Exception as e:
            session.rollback()
            raise e

class HouseDetail(MethodResource, Resource):

    # put endpoint 
    @use_kwargs(HouseModel)
    @marshal_with(HouseResponse)
    def put(self, id:int, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # get object
            house = session.query(House).get(id)
            data = request.json

            # iterate and update
            for key, value in data.items():
                setattr(house, key, value)

            # commit
            session.commit()

            # response
            return jsonable_encoder(data), status_code
        
        # error handling
        except Exception as e:
            session.rollback()
            raise e
    
    # get object endpoint
    @use_kwargs(HouseModel)
    @marshal_with(HouseResponse)
    def get(self, id:int, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # get object
            house = session.query(House).get(id)

            # response
            return jsonable_encoder(house), status_code
        
        # error handling
        except Exception as e:
            session.roolback()
            raise e