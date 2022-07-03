from django.db import models
from auth_app.models import User
from NewToUk.shared.models.base_model import BaseModel


# Create your models here.


class Lawyer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    registration_number = models.CharField("Association or organization registration number", max_length=100,
                                           blank=False, null=False)
    languages = models.CharField("Languages spoken", max_length=1000, blank=False, null=False)
    documents = models.CharField("Documents lawyer uploaded", max_length=10000, blank=True, null=True)


class AppointmentSchedules(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField("Appointment Schedule date")
    time = models.TimeField("Appointment Time")
    isUsed = models.BooleanField("Used to check if the appointment schedule has been used by another user",
                                 default=False)


class Appointment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    schedule = models.ForeignKey(AppointmentSchedules, on_delete=models.CASCADE, blank=False, null=False)
    status = models.CharField("Appointment status e.g Rejected, Scheduled", max_length=20)

