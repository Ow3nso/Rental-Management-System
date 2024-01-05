# ----- 3rd Party Libraries -----
from marshmallow import Schema, fields

# ----- Schema -----
class TenantModel(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Integer(required=True)
    password = fields.String(required=False)
    joined_date = fields.DateTime(required=False)
    exit_date = fields.DateTime(required=False)
    house_id = fields.Integer(required=True)

class TenantResponse(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Integer(required=True)
    password = fields.String(required=False)
    joined_date = fields.DateTime(required=False)
    exit_date = fields.DateTime(required=False)
    house_id = fields.Integer(required=True)