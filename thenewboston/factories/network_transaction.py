from factory import Faker
from factory.django import DjangoModelFactory

from ..constants.network import VERIFY_KEY_LENGTH
from ..models.network_transaction import NetworkTransaction


class NetworkTransactionFactory(DjangoModelFactory):
    amount = Faker('pydecimal', left_digits=16, right_digits=16)
    recipient = Faker('text', max_nb_chars=VERIFY_KEY_LENGTH)

    class Meta:
        model = NetworkTransaction
