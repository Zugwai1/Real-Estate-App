from django.db import models
from NewToUk.shared.models.base_model import BaseModel
from auth_app.models import User, Address


class Property(BaseModel):
    name = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT, blank=False, null=False)
    description = models.TextField(null=True)


class Image(BaseModel):
    property = models.ForeignKey(to="Property", on_delete=models.CASCADE)
    image = models.FilePathField()


class Review(BaseModel):
    value = models.IntegerField()
    property = models.OneToOneField(to=Property, on_delete=models.CASCADE)
