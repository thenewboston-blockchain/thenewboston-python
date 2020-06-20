import os

from playground.config import SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.constants.network import ACCEPTED
from thenewboston.utils.files import write_json
from thenewboston.utils.signed_requests import generate_signed_request


def run():
    """
    Generate signed update bank registration request
    """

    signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'validator_nid'))
    signed_request = generate_signed_request(
        data={
            'status': ACCEPTED
        },
        nid_signing_key=signing_key
    )
    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'signed-patch-bank-registration-request.json'),
        signed_request
    )


if __name__ == '__main__':
    run()
