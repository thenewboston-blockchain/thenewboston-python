import requests


def fetch(*, url, headers):
    """
    Send a GET request and return response as Python object
    """

    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        print(e, url)
        return None


def post(*, url, body):
    """
    Send a POST request and return response as Python object
    """

    response = requests.post(url, json=body)
    return response.json()
