from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):  # Corregir aquí
    user = models.OneToOneField(User, on_delete=models.CASCADE)

