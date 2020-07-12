from django.core.validators import MinValueValidator
from django.db import models

from thenewboston.constants.network import ACCOUNT_FILE_HASH_LENGTH, BLOCK_IDENTIFIER_LENGTH, MIN_POINT_VALUE
from thenewboston.models.network_node import NetworkNode
from thenewboston.utils.validators import validate_is_real_number


class NetworkValidator(NetworkNode):
    root_account_file = models.URLField(max_length=1024)
    root_account_file_hash = models.CharField(max_length=ACCOUNT_FILE_HASH_LENGTH)
    seed_block_identifier = models.CharField(blank=True, max_length=BLOCK_IDENTIFIER_LENGTH)

    # Confirmation rate (used by confirmation validators only)
    daily_confirmation_rate = models.DecimalField(
        blank=True,
        decimal_places=16,
        max_digits=32,
        null=True,
        validators=[
            MinValueValidator(MIN_POINT_VALUE),
            validate_is_real_number
        ]
    )

    class Meta:
        abstract = True
