# Insert models here
from django.db import models


class Client(models.Model):
    """Client model"""
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=12, db_index=True)
    contact_name = models.CharField(max_length=128, null=True, blank=True)
    # If multiple address can move this to a new model.
    street_name = models.CharField(max_length=256, null=True, blank=True)
    suburb = models.CharField(max_length=256, null=True, blank=True, db_index=True)
    postcode = models.CharField(max_length=6, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
