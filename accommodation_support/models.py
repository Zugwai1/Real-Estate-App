from django.db import models

# Create your models here.
from NewToUk.shared.models.BaseModel import BaseModel
from auth_app.models import User, Address


class Property(BaseModel):
    type = models.CharField(max_length=50)
    images = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT, blank=False, null=False)
