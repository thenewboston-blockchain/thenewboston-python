from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from thenewboston.constants.network import MAX_POINT_VALUE, MIN_POINT_VALUE, PROTOCOL_CHOICES, VERIFY_KEY_LENGTH


class NetworkNode(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)  # noqa: A003
    account_number = models.CharField(max_length=VERIFY_KEY_LENGTH)
    ip_address = models.GenericIPAddressField()
    node_identifier = models.CharField(max_length=VERIFY_KEY_LENGTH, unique=True)
    port = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(65535)])
    protocol = models.CharField(choices=PROTOCOL_CHOICES, max_length=5)
    version = models.CharField(max_length=32)

    # Fees
    default_transaction_fee = models.PositiveBigIntegerField(
        default=MIN_POINT_VALUE,
        validators=[
            MaxValueValidator(MAX_POINT_VALUE),
            MinValueValidator(MIN_POINT_VALUE),
        ]
    )

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['ip_address', 'port', 'protocol']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['ip_address', 'port', 'protocol'],
                name='%(app_label)s_%(class)s_unique_ip_port_proto')
        ]
