from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profil_picture = models.ImageField(default='defpic.jpg')

