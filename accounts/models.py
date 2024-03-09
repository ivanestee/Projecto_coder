from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

