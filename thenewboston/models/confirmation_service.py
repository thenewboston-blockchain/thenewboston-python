from uuid import uuid4

from django.db import models

from thenewboston.models.created_modified import CreatedModified


class ConfirmationService(CreatedModified):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    end = models.DateTimeField()
    start = models.DateTimeField()

    class Meta:
        abstract = True
