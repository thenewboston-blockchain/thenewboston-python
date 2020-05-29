from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.network import BALANCE_LOCK_LENGTH, MIN_POINT_VALUE, VERIFY_KEY_LENGTH
from thenewboston.utils.validators import validate_is_real_number


class NetworkTransaction(models.Model):
    amount = models.DecimalField(
        decimal_places=16,
        default=MIN_POINT_VALUE,
        max_digits=32,
        validators=[
            MinValueValidator(MIN_POINT_VALUE),
            validate_is_real_number
        ]
    )
    balance_key = models.CharField(max_length=BALANCE_LOCK_LENGTH, unique=True)
    recipient = models.CharField(max_length=VERIFY_KEY_LENGTH)

    class Meta:
        abstract = True
