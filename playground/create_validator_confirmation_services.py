import os

from playground.config import SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import post
from thenewboston.utils.signed_requests import generate_signed_request

"""
Create validator confirmation service
POST /validator_confirmation_services
"""


def run(send_to_bank=False):
    """
    Generate validator confirmation service
    """

    # Signed request
    sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'cv_nid'))
    signed_request = generate_signed_request(
        data={
            'end': '2020-07-09T22:10:25Z',
            'start': '2020-08-09T22:10:25Z'
        },
        nid_signing_key=sk
    )

    if send_to_bank:
        send_request_to_bank(signed_request)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'signed-validator-confirmation-services-request.json'),
        signed_request
    )


def send_request_to_bank(signed_request):
    """
    Send request to bank
    """

    node_address = format_address(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    url = f'{node_address}/validator_confirmation_services'
    results = post(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'signed-validator-confirmation-services-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_bank=True)
