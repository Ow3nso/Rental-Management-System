# ----- 3rd Party Libraries -----
from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    type = models.CharField(max_length=1000, blank=False)
    country = models.CharField(max_length=1000, blank=False)
    town = models.CharField(max_length=1000, blank=False)
    area = models.CharField(max_length=1000, blank=False)
    landlord = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name + self.landlord