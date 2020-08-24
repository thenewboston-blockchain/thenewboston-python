from uuid import uuid4

from django.core.validators import MaxValueValidator
from django.db import models

from thenewboston.constants.network import PROTOCOL_CHOICES, VERIFY_KEY_LENGTH


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
    default_transaction_fee = models.PositiveBigIntegerField()

    class Meta:
        abstract = True
