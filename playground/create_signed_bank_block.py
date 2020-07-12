import os

from playground.config import (
    BANK_ACCOUNT_NUMBER,
    BANK_TX_FEE,
    BLOCKS_DIR,
    BUCKY_ACCOUNT_NUMBER,
    SIGNING_KEY_DIR,
    PV_ACCOUNT_NUMBER,
    PV_TX_FEE
)
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.blocks.signatures import generate_signature
from thenewboston.utils.files import write_json
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key


def run():
    """
    Create block used for:
    - POST /bank_blocks
    """

    treasury_signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'treasury'))
    treasury_account_number = get_verify_key(signing_key=treasury_signing_key)
    balance_lock = 'c80237a8d230b08f4ca0f31e8943a318ab73ac8ba816d0a49fc367694ece5c6f'
    transactions = [
        {
            'amount': BANK_TX_FEE,
            'recipient': BANK_ACCOUNT_NUMBER,
        },
        {
            'amount': PV_TX_FEE,
            'recipient': PV_ACCOUNT_NUMBER,
        },
        {
            'amount': 4.125,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=treasury_account_number,
        balance_lock=balance_lock,
        signing_key=treasury_signing_key,
        transactions=transactions
    )

    bank_nid_sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bank_nid'))
    bank_nid = get_verify_key(signing_key=bank_nid_sk)
    bank_nid = encode_verify_key(verify_key=bank_nid)
    message = sort_and_encode(block)

    signed_block = {
        'block': block,
        'bank_nid': bank_nid,
        'signature': generate_signature(message=message, signing_key=bank_nid_sk)
    }

    write_json(
        os.path.join(BLOCKS_DIR, 'signed-bank-block.json'),
        signed_block
    )


if __name__ == '__main__':
    run()
