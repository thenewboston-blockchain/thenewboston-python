import pytest

from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key


def test_encode_verify_key_raise_exception():
    with pytest.raises(RuntimeError):
        encode_verify_key(verify_key=None)


def test_get_verify_key_raise_exception():
    with pytest.raises(RuntimeError):
        get_verify_key(signing_key=None)
