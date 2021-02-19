from tests.helpers import generate_message

from thenewboston.accounts.manage import create_account
from thenewboston.blocks.signatures import (
    generate_signature, verify_signature
)
from thenewboston.verify_keys.verify_key import encode_verify_key


def test_generate_signature():
    signing_key, account_number = create_account()
    encoded_account_number = encode_verify_key(verify_key=account_number)
    message = generate_message(encoded_account_number)
    signature = generate_signature(message=message, signing_key=signing_key)
    assert verify_signature(message=message, signature=signature, verify_key=encoded_account_number)

# def test_verify_signature():
#     signing_key, account_number = create_account()
#     encoded_account_number = encode_verify_key(verify_key=account_number)
#     message = generate_message(encoded_account_number)
#     signature = generate_signature(message=message, signing_key=signing_key)
#     assert verify_signature(message=message, signature=signature, verify_key=encoded_account_number)
