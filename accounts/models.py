from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    )
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)