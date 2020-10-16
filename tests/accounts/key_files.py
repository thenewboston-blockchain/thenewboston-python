from nacl.signing import SigningKey, VerifyKey

from thenewboston.accounts.key_files import (
    create_account_and_save_signing_key_file,
    read_signing_key_file,
    write_signing_key_file
)
from thenewboston.accounts.manage import create_account


def test_create_account_and_save_signing_key_file(tmpdir):
    file_path = tmpdir.join('signing_key_file')
    signing_key, account_number = create_account_and_save_signing_key_file(file_path)

    assert isinstance(signing_key, SigningKey)
    assert isinstance(account_number, VerifyKey)
    assert signing_key == read_signing_key_file(file_path)


def test_read_signing_key_file(tmpdir):
    file_path = tmpdir.join('signing_key_file')
    signing_key, account_number = create_account_and_save_signing_key_file(file_path)

    assert signing_key == read_signing_key_file(file_path)


def test_write_signing_key_file(tmpdir):
    file_path = tmpdir.join('signing_key_file')
    signing_key, account_number = create_account()
    write_signing_key_file(signing_key, file_path)

    assert signing_key == read_signing_key_file(file_path)
