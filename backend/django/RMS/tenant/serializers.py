# ----- 3rd Party Libraries -----
from rest_framework import serializers

# ----- In-Built Libraries -----
from .models import Tenant

# ----- Model Serializers -----
class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"