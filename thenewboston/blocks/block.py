from operator import itemgetter

from thenewboston.blocks.signatures import generate_signature
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key


def generate_block(*, account_number, balance_lock, signing_key, transactions):
    """
    Generate block
    """

    message = {
        'balance_key': balance_lock,
        'txs': sorted(transactions, key=itemgetter('recipient'))
    }

    signature = generate_signature(
        message=sort_and_encode(message),
        signing_key=signing_key
    )

    block = {
        'account_number': encode_verify_key(verify_key=account_number),
        'message': message,
        'signature': signature
    }

    return block
