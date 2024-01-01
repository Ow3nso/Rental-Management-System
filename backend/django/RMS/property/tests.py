# ----- 3rd Party Libraries -----
import pytest
from django.test import TestCase

# ----- In-Built Libraries -----
from .models import Property

# -----Create your tests here -----
class Dummy:
    @staticmethod
    def dummydata():
        data = {
            "name":"Yesu Telo Apartments", 
            "type":"Apartment",
            "country":"Kenya",
            "town":"HomaBay",
            "area":"sofia",
            "landlord":"Jeffrey Owen",
        }
        return data
