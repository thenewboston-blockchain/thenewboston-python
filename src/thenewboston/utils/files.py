import json
from hashlib import sha3_256 as sha3

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def get_file_hash(file):
    """
    Return hash value of file
    """

    h = sha3()

    with default_storage.open(file, 'rb') as file:
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
        with default_storage.open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = None

    return data


def write_json(file, data):
    """
    Write JSON file
    """

    try:
        default_storage.delete(file)
    except NotImplementedError:
        pass

    default_storage.save(
        file,
        ContentFile(
            json.dumps(data)
        )
    )
