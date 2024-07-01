from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class LibraryModel(AbstractUser):
    role=models.CharField(max_length=100)
    place=models.CharField(max_length=100)