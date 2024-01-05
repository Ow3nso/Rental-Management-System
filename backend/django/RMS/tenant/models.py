# ----- 3rd Party Libraries -----
from django.db import models

# ----- In-Built Libraries -----
from house.models import House

# ----- Models -----
class Tenant(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.BigIntegerField(blank=False)
    password = models.CharField(max_length=1000, blank=False, default="User@Pass123")
    joined_date = models.DateTimeField(auto_now_add=True, blank=False)
    exit_date = models.DateTimeField(blank=True)
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.email + self.house_id 