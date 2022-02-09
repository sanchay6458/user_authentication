from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    Address = models.CharField(null=True, blank=True, max_length=300)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/')

# Create your models here.
