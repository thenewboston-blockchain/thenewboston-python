from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.models import PROTOCOL_CHOICES
from thenewboston.utils.validators import validate_is_real_number


class NetworkNode(models.Model):
    identifier = models.CharField(max_length=256)
    ip_address = models.GenericIPAddressField(unique=True)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    protocol = models.CharField(choices=PROTOCOL_CHOICES, max_length=5)
    version = models.CharField(max_length=32)

    # Fees
    default_transaction_fee = models.DecimalField(
        decimal_places=16,
        default=0,
        max_digits=32,
        validators=[
            MinValueValidator(0),
            validate_is_real_number
        ]
    )
    registration_fee = models.DecimalField(
        decimal_places=16,
        default=0,
        max_digits=32,
        validators=[
            MinValueValidator(0),
            validate_is_real_number
        ]
    )

    class Meta:
        abstract = True
