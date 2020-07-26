import os

from playground.config import CV_NID_ACCOUNT_NUMBER, SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import post
from thenewboston.utils.signed_requests import generate_signed_request

"""
Bank request asking a confirmation validator to upgrade to a primary validator
POST /upgrade_request
"""


def run(send_to_cv=False):
    """
    Bank asking a confirmation validator to upgrade to a primary validator
    """

    # Signed request
    sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'bank_nid'))

    new_pv_data = {
        'validator_node_identifier': CV_NID_ACCOUNT_NUMBER
    }

    signed_request = generate_signed_request(
        data=new_pv_data,
        nid_signing_key=sk
    )

    if send_to_cv:
        send_request_to_cv(signed_request)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'upgrade-request-request.json'),
        signed_request
    )


def send_request_to_cv(signed_request):
    """
    Send request to CV
    """

    node_address = format_address(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    url = f'{node_address}/upgrade_request'
    results = post(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'upgrade-request-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_cv=True)
