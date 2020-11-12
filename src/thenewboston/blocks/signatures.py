from nacl.encoding import HexEncoder
from nacl.signing import VerifyKey


def generate_signature(*, message, signing_key):
    """
    Sign message using signing key and return signature
    """

    return signing_key.sign(message).signature.hex()


def verify_signature(*, message, signature, verify_key):
    """
    Verify block signature
    """

    verify_key = VerifyKey(verify_key.encode('utf-8'), encoder=HexEncoder)
    signature = bytes.fromhex(signature)
    verify_key.verify(message, signature)
