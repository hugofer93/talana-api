from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, EmailField

from talana.apps.core.managers import UserManager


class User(AbstractUser):
    """Custom User model inherits from AbstractUser"""
    email = EmailField(unique=True)
    is_verified = BooleanField(default=False)
    is_winner = BooleanField(default=False)

    objects = UserManager()
