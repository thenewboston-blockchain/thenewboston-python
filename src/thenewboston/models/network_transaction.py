from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from thenewboston.constants.network import MAX_POINT_VALUE, MIN_POINT_VALUE, VERIFY_KEY_LENGTH


class NetworkTransaction(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    amount = models.PositiveBigIntegerField(
        validators=[
            MaxValueValidator(MAX_POINT_VALUE),
            MinValueValidator(MIN_POINT_VALUE),
        ]
    )
    recipient = models.CharField(max_length=VERIFY_KEY_LENGTH)

    class Meta:
        abstract = True
