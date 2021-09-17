from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.TextField(max_length=20, blank=False)
    is_verified = models.BooleanField(default=False)

