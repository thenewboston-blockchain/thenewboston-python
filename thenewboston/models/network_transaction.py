from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.network import MIN_POINT_VALUE, VERIFY_KEY_LENGTH
from thenewboston.utils.validators import validate_is_real_number


class NetworkTransaction(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    amount = models.DecimalField(
        decimal_places=16,
        default=MIN_POINT_VALUE,
        max_digits=32,
        validators=[
            MinValueValidator(MIN_POINT_VALUE),
            validate_is_real_number
        ]
    )
    recipient = models.CharField(max_length=VERIFY_KEY_LENGTH)

    class Meta:
        abstract = True
