import requests

from thenewboston.utils.exceptions import NetworkException


def fetch(*, url, headers):
    """
    Send a GET request and return response as Python object
    """

    response = requests.get(url, headers=headers)
    return validate_response(response)


def patch(*, url, body):
    """
    Send a PATCH request and return response as Python object
    """

    response = requests.patch(url, json=body)
    return validate_response(response)


def post(*, url, body):
    """
    Send a POST request and return response as Python object
    """

    response = requests.post(url, json=body)
    return validate_response(response)


def validate_response(response):
    """
    Validate status code
    Return response as Python object
    """

    data = response.json()

    if response.status_code >= 400:
        err = f'status_code:{response.status_code} - {data}'
        raise NetworkException(err)

    return data
