import json


def write_json(file, data):
    """
    Write JSON file
    """

    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
