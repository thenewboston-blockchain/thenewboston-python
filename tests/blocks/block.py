from tests.helpers import random_encoded_account_number
from thenewboston.accounts.manage import create_account
from thenewboston.blocks.block import generate_block
from thenewboston.blocks.signatures import verify_signature
from thenewboston.constants.network import SIGNATURE_LENGTH
from thenewboston.verify_keys.verify_key import encode_verify_key
from thenewboston.utils.tools import sort_and_encode


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

    # Verify that signature is valid and the message has not been modified 
    verify_signature(
        message=sort_and_encode(block['message']),
        signature=block['signature'],
        verify_key=block['account_number']
    )
    # nacl.exceptions.BadSignatureError – This is raised if the signature is invalid
