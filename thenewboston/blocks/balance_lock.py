from hashlib import sha3_256 as sha3

from thenewboston.utils.tools import sort_and_encode


def generate_balance_lock(*, tx):
    """
    Generate a balance lock from a Tx
    """

    return sha3(sort_and_encode(tx)).digest().hex()
