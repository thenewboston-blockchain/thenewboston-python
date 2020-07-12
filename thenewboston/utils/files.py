import json
from hashlib import sha3_256 as sha3


def get_file_hash(file):
    """
    Return hash value of file
    """

    h = sha3()

    with open(file, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()


def read_json(file):
    """
    Read JSON file
    """

    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = None
    return data


def write_json(file, data):
    """
    Write JSON file
    """

    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
