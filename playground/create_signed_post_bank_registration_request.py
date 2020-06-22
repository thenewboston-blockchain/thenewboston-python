import os

from playground.config import (
    BANK_ACCOUNT_NUMBER,
    SIGNED_REQUESTS_DIR,
    SIGNING_KEY_DIR,
    VALIDATOR_ACCOUNT_NUMBER,
    VALIDATOR_NID_ACCOUNT_NUMBER,
    VALIDATOR_REGISTRATION_FEE
)
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.utils.signed_requests import generate_signed_request
from thenewboston.verify_keys.verify_key import get_verify_key


def run():
    """
    Generate signed create bank registration request
    """

    bank_signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bank'))
    bank_account_number = get_verify_key(signing_key=bank_signing_key)

    # Payment block (for validator registration fees)
    block = generate_block(
        account_number=bank_account_number,
        balance_lock=BANK_ACCOUNT_NUMBER,
        signing_key=bank_signing_key,
        transactions=[
            {
                'amount': VALIDATOR_REGISTRATION_FEE,
                'recipient': VALIDATOR_ACCOUNT_NUMBER,
            },
        ]
    )

    # Signed request
    bank_nid_signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bank_nid'))
    signed_request = generate_signed_request(
        data={
            'block': block,
            'validator_node_identifier': VALIDATOR_NID_ACCOUNT_NUMBER
        },
        nid_signing_key=bank_nid_signing_key
    )
    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'signed-post-bank-registration-request.json'),
        signed_request
    )


if __name__ == '__main__':
    run()
