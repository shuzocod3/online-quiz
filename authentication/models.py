from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)