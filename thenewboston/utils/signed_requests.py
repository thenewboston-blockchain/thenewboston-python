from thenewboston.blocks.signatures import generate_signature
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key


def generate_signed_requests(*, data, nid_signing_key):
    """
    Generate and return signed request
    """

    network_identifier = get_verify_key(signing_key=nid_signing_key)
    signature = generate_signature(
        message=sort_and_encode(data),
        signing_key=nid_signing_key
    )
    return {
        'message': data,
        'network_identifier': encode_verify_key(verify_key=network_identifier),
        'signature': signature
    }
