import os

from playground.config import (
    BANK_ACCOUNT_NUMBER,
    BANK_TX_FEE,
    BLOCKS_DIR,
    BUCKY_ACCOUNT_NUMBER,
    PV_ACCOUNT_NUMBER,
    PV_TX_FEE,
    SIGNING_KEY_DIR
)
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.verify_keys.verify_key import get_verify_key


def run():
    """
    Create block used for:
    - POST /blocks
    """

    signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bucky'))
    account_number = get_verify_key(signing_key=signing_key)
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
            'amount': 2.5,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock='8db1bd4404eadce824b8f7af2461976e1fde8ebd7a279a2ccec2614479ede338',
        signing_key=signing_key,
        transactions=transactions
    )

    print(block)

    write_json(
        os.path.join(BLOCKS_DIR, 'upw.json'),
        block
    )


if __name__ == '__main__':
    run()
