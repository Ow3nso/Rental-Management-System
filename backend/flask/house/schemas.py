# ----- 3rd Party Libraries -----
from marshmallow import Schema, fields

# ----- In-Built Libraries -----
from .models import House

# ----- Schemas -----
class HouseModel(Schema):
    house_number = fields.String(required=True)
    type = fields.String(required=True)
    rent = fields.Float(required=True)
    vacant = fields.Boolean(default=False)
    property = fields.Integer(required=True)

class HouseResponse(Schema):
    house_number = fields.String(required=True)
    type = fields.String(required=True)
    rent = fields.Float(required=True)
    vacant = fields.Boolean(default=False)
    property = fields.Integer(required=True)