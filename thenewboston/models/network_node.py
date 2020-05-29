from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.network import MIN_POINT_VALUE, PROTOCOL_CHOICES, VERIFY_KEY_LENGTH
from thenewboston.utils.validators import validate_is_real_number


class NetworkNode(models.Model):
    account_number = models.CharField(max_length=VERIFY_KEY_LENGTH)
    ip_address = models.GenericIPAddressField(unique=True)
    network_identifier = models.CharField(max_length=VERIFY_KEY_LENGTH, unique=True)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    protocol = models.CharField(choices=PROTOCOL_CHOICES, max_length=5)
    version = models.CharField(max_length=32)

    # Fees
    default_transaction_fee = models.DecimalField(
        decimal_places=16,
        default=MIN_POINT_VALUE,
        max_digits=32,
        validators=[
            MinValueValidator(MIN_POINT_VALUE),
            validate_is_real_number
        ]
    )
    registration_fee = models.DecimalField(
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
