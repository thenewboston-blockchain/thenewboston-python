from nacl.encoding import HexEncoder
from nacl.signing import SigningKey, VerifyKey


def encode_verify_key(*, verify_key):
    """
    Return the hexadecimal representation of the binary account number data
    """

    if not isinstance(verify_key, VerifyKey):
        raise RuntimeError('verify_key must be of type nacl.signing.VerifyKey')

    return verify_key.encode(encoder=HexEncoder).decode('utf-8')


def get_verify_key(*, signing_key):
    """
    Return the verify key from the signing key
    """

    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')

    return signing_key.verify_key
