# ----- 3rd Party Libraries -----
from flask import request
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource
from fastapi.encoders import jsonable_encoder
from fastapi import status

# ----- In-Built Libraries -----
from tenant.models import Tenant
from tenant.schemas import TenantModel, TenantResponse
from tenant.database import sessionmaker, engine

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

# ----- CPU endpoints -----
class TenantView(MethodResource):
    # post endpoint 
    @use_kwargs(TenantModel)
    @marshal_with(TenantResponse)
    def post(self, status_code=status.HTTP_201_CREATED, **kwargs):
        data:TenantResponse = request.json()

        try:
            # add data
            new_tenant = Tenant(**data)

            # commit
            session.add(new_tenant)
            session.commit()

            # response
            return jsonable_encoder(data), status_code
        except Exception as e:
            session.rollback()
            raise e

    # get endpoint
    @use_kwargs(TenantModel)
    @marshal_with(TenantResponse)
    def get(self, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # pagination
            offset, limit, next_offset, previous_offset = Paginate.pagination() 

            tenant = session.query(Tenant).offset(offset).limit(limit).all()

            #url to next and previous pages
            next_page_url = f'tenent?limit={str(limit)}&offset={str(next_offset)}' 
            previous_page_url = f'tenant?limit={str(limit)}&offset={str(previous_offset)}'

            #response to be returned
            response = {
                "tenant":jsonable_encoder(tenant),
                "next_page_url":next_page_url,
                "previous_page_url":previous_page_url,
                "offset": offset,
                "limit": limit,
                "has_more_records": len(tenant) == limit,
            }

            return response, status_code

        # error handling
        except Exception as e:
            session.rollback()
            raise e


class TenantDetail(MethodResource, Resource):
    # put endpoint
    @use_kwargs(TenantModel)
    @marshal_with(TenantResponse)
    def put(self, id:int, status_code=status.HTTP_200_OK, **kwargs):
        try:
            # get object
            tenant = session.query(Tenant).get(id)
            data = request.json

            # iterate and update
            for key, value in data.items():
                setattr(tenant, key, value)

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
            tenant = session.query(Tenant).get(id)

            # response
            return jsonable_encoder(tenant), status_code
        
        # error handling
        except Exception as e:
            session.roolback()
            raise e