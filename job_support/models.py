from django.db import models

# Create your models here.
from NewToUk.shared.models.base_model import BaseModel
from auth_app.models import User


class JobCategory(BaseModel):
    name = models.CharField("Job category", max_length=50)
    description = models.CharField("Job category description", max_length=500)


class Job(BaseModel):
    title = models.CharField("Job title", max_length=50)
    type = models.CharField("Job Type", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    form = models.JSONField("Application form stored in Json format to dynamically generate the forms")


class JobApplication(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    job = models.OneToOneField(Job, on_delete=models.RESTRICT, blank=False, null=False)
    application = models.JSONField("Job application")
