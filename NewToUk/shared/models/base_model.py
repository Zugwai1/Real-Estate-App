import uuid
from django.db import models


def _get_id():
    return uuid.uuid4()


class BaseModel(models.Model):
    """Abstract Model for all models to Inherit from"""

    id = models.UUIDField("Models id", primary_key=True, null=False, blank=False, default=_get_id())
    date_created = models.DateTimeField("Date created", auto_now_add=True, blank=False, null=False)
    date_modified = models.DateTimeField("Date modified", auto_now=True, blank=False, null=False)

    class Meta:
        abstract = True
