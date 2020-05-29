from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.network import MIN_POINT_VALUE
from thenewboston.utils.validators import validate_is_real_number


class NetworkTransactionFeeTier(models.Model):
    fee = models.DecimalField(
        decimal_places=16,
        default=MIN_POINT_VALUE,
        max_digits=32,
        validators=[
            MinValueValidator(MIN_POINT_VALUE),
            validate_is_real_number
        ]
    )

    class Meta:
        abstract = True
