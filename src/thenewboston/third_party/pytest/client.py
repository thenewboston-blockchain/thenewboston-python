from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient


class APIError(Exception):

    def __init__(self, *args, resp, expected):
        super().__init__(*args)
        self.resp = resp
        self.expected = expected


class UserWrapper:

    def __init__(self, user=None):
        self.user = user
        self.client = APIClient()
        self.client.force_authenticate(user)

    def _method(self, method, url, data):
        return getattr(self.client, method)(url, data, format='json')

    @staticmethod
    def check_code(resp, expected):
        if resp.status_code != expected:
            msg = '{} {}'.format(resp.status_code, resp.content)[:1000]
            raise APIError(msg, resp=resp, expected=expected)

    def delete(self, url, data=None):
        return self._method('delete', url, data or {})

    def delete_json(self, *args, expected=HTTP_204_NO_CONTENT, **kwargs):
        response = self.delete(*args, **kwargs)
        self.check_code(response, expected)
        assert not response.content, response.content

    def get(self, url, data=None):
        return self._method('get', url, data or {})

    def get_json(self, *args, expected=HTTP_200_OK, **kwargs):
        response = self.get(*args, **kwargs)
        self.check_code(response, expected)
        return response.json()

    def patch(self, url, data):
        return self._method('patch', url, data)

    def patch_json(self, *args, expected=HTTP_200_OK, **kwargs):
        response = self.patch(*args, **kwargs)
        self.check_code(response, expected)
        return response.json()

    def post(self, url, data):
        return self._method('post', url, data)

    def post_json(self, *args, expected=HTTP_201_CREATED, **kwargs):
        response = self.post(*args, **kwargs)
        self.check_code(response, expected)
        return response.json()

    def put(self, url, data):
        return self._method('put', url, data)

    def put_json(self, *args, expected=HTTP_200_OK, **kwargs):
        response = self.put(*args, **kwargs)
        self.check_code(response, expected)
        return response.json()
