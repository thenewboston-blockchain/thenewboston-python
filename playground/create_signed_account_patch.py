import os

from playground.config import SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR, TREASURY_ACCOUNT_NUMBER
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import patch
from thenewboston.utils.signed_requests import generate_signed_request

"""
Update trust for a account
PATCH /account/<account_number>
"""


def run(send_to_node=False):
    """
    Generate signed PATCH request
    """

    # Signed request
    sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bank_nid'))

    payload = {
        'trust': 99.98
    }

    signed_request = generate_signed_request(
        data=payload,
        nid_signing_key=sk
    )

    if send_to_node:
        send_request_to_node(signed_request)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'account-patch-request.json'),
        signed_request
    )


def send_request_to_node(signed_request):
    """
    Send request to node
    """

    node_address = format_address(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    url = f'{node_address}/accounts/{TREASURY_ACCOUNT_NUMBER}'
    results = patch(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'account-patch-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_node=True)
