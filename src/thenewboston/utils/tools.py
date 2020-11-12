import json


def sort_and_encode(dictionary):
    """
    Sort dictionary and return encoded data
    """

    return json.dumps(dictionary, separators=(',', ':'), sort_keys=True).encode('utf-8')
