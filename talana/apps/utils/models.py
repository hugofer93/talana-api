from django.db.models import BooleanField, DateTimeField, Model

from talana.apps.utils.managers import BaseManager


class BaseModel(Model):
    """Base Model for project."""
    available = BooleanField(default=True)
    creation_date = DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True
