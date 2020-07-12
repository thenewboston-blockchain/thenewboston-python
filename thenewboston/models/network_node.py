from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from thenewboston.constants.network import MIN_POINT_VALUE, PROTOCOL_CHOICES, VERIFY_KEY_LENGTH
from thenewboston.utils.validators import validate_is_real_number


class NetworkNode(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    account_number = models.CharField(max_length=VERIFY_KEY_LENGTH)
    ip_address = models.GenericIPAddressField(unique=True)
    node_identifier = models.CharField(max_length=VERIFY_KEY_LENGTH, unique=True)
    port = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(65535)
        ]
    )
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

    class Meta:
        abstract = True
