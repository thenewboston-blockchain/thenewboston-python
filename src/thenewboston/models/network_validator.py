from django.db import models

from thenewboston.constants.network import ACCOUNT_FILE_HASH_LENGTH, BLOCK_IDENTIFIER_LENGTH
from thenewboston.models.network_node import NetworkNode


class NetworkValidator(NetworkNode):
    root_account_file = models.URLField(max_length=1024)
    root_account_file_hash = models.CharField(max_length=ACCOUNT_FILE_HASH_LENGTH)
    seed_block_identifier = models.CharField(blank=True, max_length=BLOCK_IDENTIFIER_LENGTH)

    # Confirmation rate (used by confirmation validators only)
    daily_confirmation_rate = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        abstract = True
