from tests.helpers import random_encoded_account_number

from thenewboston.accounts.manage import create_account
from thenewboston.blocks.block import generate_block
from thenewboston.constants.network import BANK, PRIMARY_VALIDATOR
from thenewboston.serializers.network_block import NetworkBlockSerializer
from thenewboston.verify_keys.verify_key import encode_verify_key


def test_network_block_serializer():
    signing_key, account_number = create_account()
    encoded_account_number = encode_verify_key(verify_key=account_number)

    transactions = [
        {
            'amount': 1,
            'fee': BANK,
            'recipient': random_encoded_account_number(),
        },
        {
            'amount': 1,
            'fee': PRIMARY_VALIDATOR,
            'recipient': random_encoded_account_number(),
        },
        {
            'amount': 5,
            'memo': 'Hello there I am 123 years old',
            'recipient': random_encoded_account_number(),
        }
    ]

    block = generate_block(
        account_number=account_number,
        balance_lock=encoded_account_number,
        signing_key=signing_key,
        transactions=transactions
    )

    serializer = NetworkBlockSerializer(data=block)
    assert serializer.is_valid()
