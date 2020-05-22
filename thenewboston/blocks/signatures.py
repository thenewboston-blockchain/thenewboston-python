from nacl.encoding import HexEncoder
from nacl.signing import VerifyKey


def generate_signature(*, message, signing_key):
    """
    Sign message using signing key and return signature
    """

    return signing_key.sign(message).signature.hex()


def verify_signature(*, account_number, signature, message):
    """
    Verify block signature
    """

    account_number = VerifyKey(account_number.encode('utf-8'), encoder=HexEncoder)
    signature = bytes.fromhex(signature)
    account_number.verify(message, signature)
