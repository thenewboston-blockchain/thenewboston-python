import os

from playground.config import SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import post
from thenewboston.utils.signed_requests import generate_signed_request

"""
Creates a signed connection request that is used by the client to send to the target node
POST /connection_requests
"""


def run(send_to_node=False):
    """
    Generate signed connection request
    """

    # Signed request
    sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'cv_nid'))
    signed_request = generate_signed_request(
        data={
            'ip_address': '138.68.233.185',
            'port': None,
            'protocol': 'http'
        },
        nid_signing_key=sk
    )

    if send_to_node:
        send_request_to_node(signed_request, live_pv=True)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'connection-request.json'),
        signed_request
    )


def send_request_to_node(signed_request, live_pv=False):
    """
    Send connection request to node
    """

    if live_pv:
        node_address = format_address(
            ip_address='64.225.47.205',
            port=None,
            protocol='http'
        )
    else:
        node_address = format_address(
            ip_address='192.168.1.75',
            port=8000,
            protocol='http'
        )

    url = f'{node_address}/connection_requests'
    results = post(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)


if __name__ == '__main__':
    run(send_to_node=True)
