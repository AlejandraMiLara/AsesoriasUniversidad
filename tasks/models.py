from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    matricula = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(null=True, blank=True, default=0)
