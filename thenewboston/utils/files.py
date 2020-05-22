import json


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
