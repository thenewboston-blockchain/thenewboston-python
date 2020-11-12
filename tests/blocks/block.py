from tests.helpers import random_encoded_account_number

from thenewboston.accounts.manage import create_account
from thenewboston.blocks.block import generate_block
from thenewboston.constants.network import SIGNATURE_LENGTH
from thenewboston.verify_keys.verify_key import encode_verify_key


def test_generate_block():
    signing_key, account_number = create_account()
    encoded_account_number = encode_verify_key(verify_key=account_number)

    transactions = [
        {
            'amount': 1,
            'recipient': random_encoded_account_number(),
        },
        {
            'amount': 1,
            'recipient': random_encoded_account_number(),
        },
        {
            'amount': 5,
            'recipient': random_encoded_account_number(),
        }
    ]

    block = generate_block(
        account_number=account_number,
        balance_lock=encoded_account_number,
        signing_key=signing_key,
        transactions=transactions
    )

    assert block['account_number'] == encoded_account_number
    assert block['message']['balance_key'] == encoded_account_number
    assert len(block['message']['txs']) == 3
    assert len(block['signature']) == SIGNATURE_LENGTH
