# ----- 3rd Party Libraries -----
from rest_framework import serializers

# ----- In-Built Libraries -----
from .models import Property

# ----- Data Serialization -----
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"