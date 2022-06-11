from django.db import models


class BaseModel(models.Model):
    """Abstract Model for all models to Inherit from"""

    id = models.UUIDField("Models id", primary_key=True, null=False, blank=False)
    date_created = models.DateTimeField("Date created", auto_now_add=True, blank=False, null=False)
    date_modified = models.DateTimeField("Date modified", auto_now=True, blank=False, null=False)

    class Meta:
        abstract = True
