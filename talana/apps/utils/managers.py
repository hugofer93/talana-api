from django.db.models import Manager, QuerySet


class BaseQuerySet(QuerySet):
    """BaseQuerySet for BaseManager."""
    def all_available(self):
        return self.filter(available=True)


class BaseManager(Manager.from_queryset(BaseQuerySet)):
    """BaseManager for BaseModel."""
