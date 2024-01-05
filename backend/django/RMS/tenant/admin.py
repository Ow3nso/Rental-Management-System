# ----- 3rd Party Libraries -----
from django.contrib import admin

# ----- In-Built Libraries -----
from .models import Tenant

# ----- Model Registration -----
admin.site.register(Tenant)