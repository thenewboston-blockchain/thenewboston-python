import os

from playground.config import SIGNING_KEY_DIR
from thenewboston.accounts.key_files import create_account_and_save_signing_key_file, read_signing_key_file
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key


def run():
    """
    Create new account and save signing key
    """

    file_path = os.path.join(SIGNING_KEY_DIR, 'cv_nid')
    create_account_and_save_signing_key_file(file=file_path)

    signing_key = read_signing_key_file(file_path)
    verify_key = get_verify_key(signing_key=signing_key)
    verify_key = encode_verify_key(verify_key=verify_key)

    print(f'verify_key: {verify_key}')


if __name__ == '__main__':
    run()
