from nacl.encoding import HexEncoder
from nacl.signing import SigningKey, VerifyKey


def encode_account_number(*, account_number):
    """
    Return the hexadecimal representation of the binary account number data
    """

    if not isinstance(account_number, VerifyKey):
        raise RuntimeError('account_number must be of type nacl.signing.VerifyKey')

    return account_number.encode(encoder=HexEncoder).decode('utf-8')


def get_account_number(*, signing_key):
    """
    Return the account number from the signing key
    """

    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')

    return signing_key.verify_key
