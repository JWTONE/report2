from django.db import models
from django.conf import settings

like_products = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )