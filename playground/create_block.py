import os

from playground.config import (
    BANK_ACCOUNT_NUMBER,
    BANK_TX_FEE,
    BUCKY_ACCOUNT_NUMBER,
    SIGNING_KEY_DIR,
    VALIDATOR_ACCOUNT_NUMBER,
    VALIDATOR_TX_FEE
)
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.balance_lock import generate_balance_lock
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import post
from thenewboston.verify_keys.verify_key import get_verify_key


def run(send_to_bank=False):
    """
    Create block used for:
    - POST /blocks
    """

    signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'treasury'))
    account_number = get_verify_key(signing_key=signing_key)

    balance_lock = 'e7e8a1af9e9531f866161ef48f3df0e99507b16ab09ec747d18b0c8f884386e8'
    transactions = [
        {
            'amount': BANK_TX_FEE,
            'recipient': BANK_ACCOUNT_NUMBER,
        },
        {
            'amount': VALIDATOR_TX_FEE,
            'recipient': VALIDATOR_ACCOUNT_NUMBER,
        },
        {
            'amount': 4.125,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock=balance_lock,
        signing_key=signing_key,
        transactions=transactions
    )

    if send_to_bank:
        send_block_to_bank(block)

    write_json('blocks/block.json', block)


def send_block_to_bank(block):
    """
    Send block to bank
    """

    next_balance_lock = generate_balance_lock(message=block['message'])
    print(f'\nNext balance lock will be: {next_balance_lock}\n')

    bank_address = format_address(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    url = f'{bank_address}/blocks'
    results = post(url=url, body=block)

    for k, v in results.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    run(send_to_bank=False)