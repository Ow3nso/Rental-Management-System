# ----- 3rd Party Libraries -----
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# ----- In-Built Libraries -----
from .models import Tenant
from .serializers import TenantSerializer

# ----- CPU Endpoints -----
class TenantViews(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
