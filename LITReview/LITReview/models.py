from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    # Your UserFollows model definition goes here

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )
