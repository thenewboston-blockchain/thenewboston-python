import json
from hashlib import sha3_256 as sha3

from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey, VerifyKey
from os import path

import json
from hashlib import sha3_256 as sha3
from thenewboston.utils.files import write_json


def create_account():
    """
    Create a new account
    Return signing_key, account_number
    """

    signing_key = SigningKey.generate()
    account_number = signing_key.verify_key
    return signing_key, account_number


def encode_account_number(account_number):
    """
    Return the hexadecimal representation of the binary account number data
    """

    if not isinstance(account_number, VerifyKey):
        raise RuntimeError('account_number must be of type nacl.signing.VerifyKey')

    return account_number.encode(encoder=HexEncoder).decode('utf-8')


def generate_balance_lock(tx):
    """
    Generate a balance lock from a Tx
    """

    return sha3(json.dumps(tx, sort_keys=True).encode('utf-8')).digest().hex()


def generate_block(*, payments, signing_key, account_number):
    """
    Generate block
    """

    # balance_lock = get_balance_lock_from_balance_sheet(account_number)
    balance_lock = '123'

    txs = []

    for payment in payments:
        tx = {
            'amount': payment['amount'],
            'balance_key': balance_lock,
            'recipient': payment['recipient']
        }
        balance_lock = generate_balance_lock(tx)
        txs.append(tx)

    message = json.dumps(txs, sort_keys=True).encode('utf-8')
    signature = generate_signature(message, signing_key)
    block = {
        'account_number': encode_account_number(account_number),
        'signature': signature.hex(),
        'txs': txs
    }
    return block


def generate_signature(message, signing_key):
    """
    Sign message using signing key and return signature
    """

    return signing_key.sign(message).signature


def get_account_number(signing_key):
    """
    Return the account number from the signing key
    """

    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')

    return signing_key.verify_key


def read_signing_key_file(file):
    """
    Read signing key from file
    """

    with open(file, 'rb') as f:
        return SigningKey(f.read(), encoder=HexEncoder)


def write_signing_key_file(signing_key, file):
    """
    Save signing key to file
    """

    if path.exists(file):
        raise RuntimeError(f'{file} already exists')

    with open(file, 'wb') as f:
        f.write(signing_key.encode(encoder=HexEncoder))


if __name__ == '__main__':
    # _signing_key, _account_number = create_account()
    # write_signing_key_file(_signing_key, 'hello')

    _signing_key = read_signing_key_file('hello')
    _account_number = get_account_number(_signing_key)

    _payments = [
        {
            'amount': 10,
            'recipient': 'c6b14782902ee6eaa7bc86d843149e08f45dfd7e7fbc085e9aafd2e86d5e314b',
        },
        {
            'amount': 5,
            'recipient': '8b8b8815a45c7f1f2740f77a3b5d85e9c26fc400ec67e7a58114f996237e40d6',
        },
        {
            'amount': 15,
            'recipient': 'e245723754548550f4892bfc583e5c8bd749bebe1b54d362590d51e520185555',
        }
    ]

    _block = generate_block(
        payments=_payments,
        signing_key=_signing_key,
        account_number=_account_number
    )

    print(_block)
    write_json('block.json', _block)
