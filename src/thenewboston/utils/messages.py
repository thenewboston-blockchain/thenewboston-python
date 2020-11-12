from hashlib import sha3_256 as sha3

from thenewboston.utils.tools import sort_and_encode


def get_message_hash(*, message):
    """
    Return has of given message
    """

    return sha3(sort_and_encode(message)).digest().hex()
