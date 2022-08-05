from django.db import models
from NewToUk.shared.models.base_model import BaseModel
from auth_app.models import User, Address


class Property(BaseModel):
    name = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT, blank=False, null=False)
    description = models.TextField(null=True)
    status = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=60, decimal_places=10, null=True)
    number_of_bedrooms = models.IntegerField(null=True)
    number_of_bathrooms = models.IntegerField(null=True)

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Description: {self.description}"


class Image(BaseModel):
    property = models.ForeignKey(to="Property", on_delete=models.CASCADE)
    image = models.FilePathField()


class Review(BaseModel):
    value = models.IntegerField()
    property = models.OneToOneField(to=Property, on_delete=models.CASCADE)
