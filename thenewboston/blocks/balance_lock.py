from hashlib import sha3_256 as sha3

from thenewboston.utils.tools import sort_and_encode


def generate_balance_lock(*, message):
    """
    Generate a balance lock from a message
    """

    return sha3(sort_and_encode(message)).digest().hex()
