# ----- 3rd Party Libraries -----
from marshmallow import fields, Schema

# ----- Schemas -----
class PropertyModel(Schema):
    name =  fields.String(required=True)
    type = fields.String(required=True)
    country = fields.String(required=True)
    town = fields.String(required=True)
    area = fields.String(required=True)
    landlord = fields.String(required=True)

class PropertyResponse(Schema):
    name =  fields.String(required=True)
    type = fields.String(required=True)
    country = fields.String(required=True)
    town = fields.String(required=True)
    area = fields.String(required=True)
    landlord = fields.String(required=True)