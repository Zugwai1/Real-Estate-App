from django.db import models

# Create your models here.
from NewToUk.shared.models.base_model import BaseModel
from auth_app.models import User


class Post(BaseModel):
    post = models.TextField()
    reactions = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, blank=False, null=False)


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField()
    replay = models.ForeignKey("self", on_delete=models.CASCADE, related_name="comment")
