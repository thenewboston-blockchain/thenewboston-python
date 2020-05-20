import json
from hashlib import sha3_256 as sha3

from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey, VerifyKey
from os import path


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
    print(encode_account_number(_account_number))
    print(read_signing_key_file('hello'))
