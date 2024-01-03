# ----- 3rd Party Libraries -----
from flask import request
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource
from fastapi.encoders import jsonable_encoder
from fastapi import status

# ----- In-Built Libraries -----
from property.models import Property
from property.schemas import PropertyModel, PropertyResponse
from property.database import sessionmaker, engine

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
class PropertyView(MethodResource, Resource):
    # post endpoint 
    @use_kwargs(PropertyModel)
    @marshal_with(PropertyResponse)
    def post(self, status_code=status.HTTP_201_CREATED, **kwargs):
        data:PropertyResponse = request.json()

        try:
            # add data
            new_property = Property(**data)

            # commit
            session.add(new_property)
            session.commit()

            # response
            return jsonable_encoder(data), status_code
        except Exception as e:
            session.rollback()
            raise e

    # get endpoint
    @use_kwargs(PropertyModel)
    @marshal_with(PropertyResponse)
    def get(self, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # pagination
            offset, limit, next_offset, previous_offset = Paginate.pagination() 

            property = session.query(Property).offset(offset).limit(limit).all()

            #url to next and previous pages
            next_page_url = f'property?limit={str(limit)}&offset={str(next_offset)}' 
            previous_page_url = f'property?limit={str(limit)}&offset={str(previous_offset)}'

            #response to be returned
            response = {
                "property":jsonable_encoder(property),
                "next_page_url":next_page_url,
                "previous_page_url":previous_page_url,
                "offset": offset,
                "limit": limit,
                "has_more_records": len(property) == limit,
            }

            return response, status_code

        # error handling
        except Exception as e:
            session.rollback()
            raise e


class PropertyDetail(MethodResource, Resource):
    # put endpoint
    @use_kwargs(PropertyModel)
    @marshal_with(PropertyResponse)
    def put(self, id:int, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # get object
            property = session.query(Property).get(id)
            data = request.json

            # iterate and update
            for key, value in data.items():
                setattr(property, key, value)

            # commit
            session.commit()

            # response
            return jsonable_encoder(data), status_code
        
        # error handling
        except Exception as e:
            session.rollback()
            raise e
    
    # get specific object
    def get(self, id:int, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # get object
            property = session.query(Property).get(id)

            # response
            return jsonable_encoder(property), status_code
        
        # error handling
        except Exception as e:
            session.roolback()
            raise e