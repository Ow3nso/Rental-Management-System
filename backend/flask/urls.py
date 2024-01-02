# ----- 3rd Party Libraries -----
from flask_restful import Api

# ----- In-Built Libraries -----
from main import app
from flask.property.views import PropertyView, PropertyDetail

api = Api(app)
API = api.add_resource

# ----- register the API -----
urls = [
    API(PropertyView, "/api/property"),
    API(PropertyDetail, "/api/property/<id>"),
    #API(ContactDetail, "/contacts")
]