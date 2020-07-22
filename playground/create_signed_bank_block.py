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
from thenewboston.blocks.signatures import generate_signature
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import post
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key


def run(send_to_pv=False):
    """
    Create block used for:
    - POST /bank_blocks
    - Bank > PV
    """

    treasury_signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'treasury'))
    account_number = get_verify_key(signing_key=treasury_signing_key)

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
            'amount': 1.0,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
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
        'node_identifier': bank_nid,
        'signature': generate_signature(message=message, signing_key=bank_nid_sk)
    }

    write_json(
        os.path.join(BLOCKS_DIR, 'bank-blocks-request.json'),
        signed_block
    )

    if send_to_pv:
        send_request_to_pv(signed_block)


def send_request_to_pv(signed_request):
    """
    Send request to PV
    """

    node_address = format_address(
        ip_address='64.225.47.205',
        port=None,
        protocol='http'
    )
    url = f'{node_address}/bank_blocks'
    results = post(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)

    write_json(
        os.path.join(BLOCKS_DIR, 'bank-blocks-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_pv=True)
