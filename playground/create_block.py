import os

from playground.config import (
    BANK_ACCOUNT_NUMBER,
    BANK_TX_FEE,
    BLOCKS_DIR,
    BUCKY_ACCOUNT_NUMBER,
    PV_ACCOUNT_NUMBER,
    PV_TX_FEE,
    SIGNING_KEY_DIR,
    TREASURY_ACCOUNT_NUMBER
)
from playground.utils import get_account_balance_lock
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.messages import get_message_hash
from thenewboston.utils.network import post
from thenewboston.verify_keys.verify_key import get_verify_key


def run(send_to_bank=False):
    """
    Create block used for:
    - POST /blocks
    """

    signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'treasury'))
    account_number = get_verify_key(signing_key=signing_key)

    balance_lock = get_account_balance_lock(account_number=TREASURY_ACCOUNT_NUMBER, live_pv=True)
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
            'amount': 5.50,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock=balance_lock,
        signing_key=signing_key,
        transactions=transactions
    )

    write_json(
        os.path.join(BLOCKS_DIR, 'blocks.json'),
        block
    )

    if send_to_bank:
        send_block_to_bank(block)


def send_block_to_bank(block):
    """
    Send block to bank
    """

    next_balance_lock = get_message_hash(message=block['message'])
    print(f'\nNext balance lock will be: {next_balance_lock}\n')

    bank_address = format_address(
        ip_address='167.99.173.247',
        port=None,
        protocol='http'
    )
    url = f'{bank_address}/blocks'
    results = post(url=url, body=block)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    write_json(
        os.path.join(BLOCKS_DIR, 'blocks-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_bank=True)
