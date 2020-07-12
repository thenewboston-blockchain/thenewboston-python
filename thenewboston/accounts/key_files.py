from os import path

from nacl.encoding import HexEncoder
from nacl.signing import SigningKey

from thenewboston.accounts.manage import create_account


def create_account_and_save_signing_key_file(file):
    """
    Create a new account
    Save signing key to file
    Return signing_key, account_number
    """

    signing_key, account_number = create_account()
    write_signing_key_file(signing_key, file)
    return signing_key, account_number


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

    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')

    if path.exists(file):
        raise RuntimeError(f'{file} already exists')

    with open(file, 'wb') as f:
        f.write(signing_key.encode(encoder=HexEncoder))
