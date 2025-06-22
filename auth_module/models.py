from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(null=True, blank=True, max_length=20)
    password = models.CharField(max_length=150)
    is_email_verified = models.BooleanField(default=False)
