import os

from playground.config import BANK_NID_ACCOUNT_NUMBER, SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import patch
from thenewboston.utils.signed_requests import generate_signed_request

"""
Update trust for a bank
PATCH /banks/<node_identifier>
"""


def run(send_to_node=False):
    """
    Generate signed PATCH request
    """

    # Signed request
    sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bank_nid'))

    payload = {
        'trust': 76.26
    }

    target_nid = BANK_NID_ACCOUNT_NUMBER

    signed_request = generate_signed_request(
        data=payload,
        nid_signing_key=sk
    )

    if send_to_node:
        send_request_to_node(signed_request, target_nid)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'bank-patch-request.json'),
        signed_request
    )


def send_request_to_node(signed_request, target_nid):
    """
    Send request to node
    """

    node_address = format_address(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    url = f'{node_address}/banks/{target_nid}'
    results = patch(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'bank-patch-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_node=True)
