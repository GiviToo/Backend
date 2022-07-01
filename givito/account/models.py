from uuid import uuid4
from django.db import models

class User(models.Model):
    uuid = models.CharField(max_length=36, default=uuid4)
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=15, null=True, blank=True, default="")
    email = models.EmailField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    