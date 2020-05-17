import json
from urllib.request import Request, urlopen


def fetch(*, url, headers):
    """
    Download data from URL and return as Python object
    """

    try:
        request = Request(url)

        for k, v in headers.items():
            request.add_header(k, v)

        response = urlopen(request)
        results = json.loads(response.read())
        return results
    except Exception as e:
        print(e, url)
        return None
