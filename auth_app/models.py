from django.contrib.auth.models import AbstractUser
from django.db import models
from NewToUk.shared.models.base_model import BaseModel

# Create your models here.


class Address(BaseModel):
    number_line = models.TextField("Address Number Line")
    street = models.CharField("Address street", max_length=2000, blank=False, null=False)
    city = models.CharField("Address city", max_length=2000, blank=False, null=False)
    state = models.CharField("Address state", max_length=2000, blank=False, null=False)
    country = models.CharField("Address country", max_length=2000, blank=False, null=False)
    postal_code = models.TextField("Postal code")


class User(AbstractUser, BaseModel):
    middle_name = models.CharField("User's Middle name", max_length=50, blank=True, null=True)
    phone_number = models.CharField("User's phone number", max_length=30, blank=False, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    nationality = models.CharField("User's Nationality", max_length=30, blank=False, null=False)
    DOB = models.DateField("User's Date of birth")
