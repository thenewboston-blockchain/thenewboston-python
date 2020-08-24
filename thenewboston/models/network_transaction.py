from uuid import uuid4

from django.db import models

from thenewboston.constants.network import VERIFY_KEY_LENGTH


class NetworkTransaction(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    amount = models.PositiveBigIntegerField()
    recipient = models.CharField(max_length=VERIFY_KEY_LENGTH)

    class Meta:
        abstract = True
