from thenewboston.utils.network import fetch, post


def test_fetch():
    url = 'http://54.183.17.224/config'
    body = {'key':'value'}    
    assert post(url=url, body=body) == fetch(url=url, headers=None)