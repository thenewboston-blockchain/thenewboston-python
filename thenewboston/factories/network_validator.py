from factory import Faker

from .network_node import NetworkNodeFactory
from ..constants.network import ACCOUNT_FILE_HASH_LENGTH, BLOCK_IDENTIFIER_LENGTH
from ..models.network_validator import NetworkValidator


class NetworkValidatorFactory(NetworkNodeFactory):
    daily_confirmation_rate = Faker('pyint')
    root_account_file = Faker('url')
    root_account_file_hash = Faker('text', max_nb_chars=ACCOUNT_FILE_HASH_LENGTH)
    seed_block_identifier = Faker('text', max_nb_chars=BLOCK_IDENTIFIER_LENGTH)

    class Meta:
        model = NetworkValidator
        abstract = True
