from django.db import models

from thenewboston.constants.network import HEAD_HASH_LENGTH
from thenewboston.models.network_node import NetworkNode


class NetworkValidator(NetworkNode):
    head_hash = models.CharField(max_length=HEAD_HASH_LENGTH)
    root_account_file = models.URLField(max_length=1024)
    root_account_file_hash = models.CharField(max_length=HEAD_HASH_LENGTH)
    seed_block_hash = models.CharField(max_length=HEAD_HASH_LENGTH)

    class Meta:
        abstract = True
