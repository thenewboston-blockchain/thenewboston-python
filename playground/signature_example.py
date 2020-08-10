import os

from playground.config import SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.signatures import generate_signature


def run():
    """
    Run main script
    """

    signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'sample'))
    signature = generate_signature(
        message='Hey'.encode('utf-8'),
        signing_key=signing_key
    )
    print(signature)


if __name__ == '__main__':
    run()
