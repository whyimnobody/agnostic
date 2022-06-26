# source: https://adriennedomingus.com/blog/soft-deletion-in-django
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def active(self):
        return self.filter(deleted_at=None)

    def deleted(self):
        return self.exclude(deleted_at=None)
