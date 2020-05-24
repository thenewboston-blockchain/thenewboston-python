from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.network import ACCOUNT_NUMBER_LENGTH, BALANCE_LOCK_LENGTH, SIGNATURE_LENGTH
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
    balance_key = models.CharField(max_length=BALANCE_LOCK_LENGTH, unique=True)
    recipient = models.CharField(max_length=ACCOUNT_NUMBER_LENGTH)
    sender = models.CharField(max_length=ACCOUNT_NUMBER_LENGTH)
    signature = models.CharField(max_length=SIGNATURE_LENGTH)

    class Meta:
        abstract = True
