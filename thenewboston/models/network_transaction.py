from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.utils.validators import validate_is_real_number


class NetworkTransaction(models.Model):
    amount = models.DecimalField(
        decimal_places=16,
        default=0,
        max_digits=32,
        validators=[
            MinValueValidator(0),
            validate_is_real_number
        ]
    )
    balance_key = models.CharField(max_length=64, unique=True)
    recipient = models.CharField(max_length=64)
    sender = models.CharField(max_length=64)
    signature = models.CharField(max_length=128)

    class Meta:
        abstract = True
