# ----- 3rd Party Libraries -----
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# ----- In-Built Libraries -----
from .models import Property
from .serializers import PropertySerializer

# ----- CPU endpoints -----
class PropertyView(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer