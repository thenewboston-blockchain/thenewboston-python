import requests


def fetch(*, url, headers):
    """
    Send a GET request and return response as Python object
    """

    response = requests.get(url, headers=headers)
    return response.json()


def post(*, url, body):
    """
    Send a POST request and return response as Python object
    """

    response = requests.post(url, json=body)
    return response.json()
