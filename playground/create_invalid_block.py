import os

from playground.config import PV_NID_ACCOUNT_NUMBER, SIGNED_REQUESTS_DIR, SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.utils.files import write_json
from thenewboston.utils.format import format_address
from thenewboston.utils.network import post
from thenewboston.utils.signed_requests import generate_signed_request

"""
Create invalid block
POST /invalid_blocks
"""


def run(send_to_bank=False):
    """
    Generate invalid block
    """

    # Signed request
    sk = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'cv_nid'))
    signed_request = generate_signed_request(
        data={
            'block': {
                'account_number': '0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb',
                'message': {
                    'balance_key': 'ce51f0d9facaa7d3e69657429dd3f961ce70077a8efb53dcda508c7c0a19d2e3',
                    'txs': [
                        {
                            'amount': 12.5,
                            'recipient': '484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc'
                        },
                        {
                            'amount': 1,
                            'recipient': '5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8'
                        },
                        {
                            'amount': 4,
                            'recipient': 'ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314'
                        }
                    ]
                },
                'signature': 'ee5a2f2a2f5261c1b633e08dd61182fd0db5604c853ebd8498f6f28ce8e2ccbbc38093918610ea88a7ad47c7f3192ed955d9d1529e7e390013e43f25a5915c0f'
            },
            'block_identifier': '65ae26192dfb9ec41f88c6d582b374a9b42ab58833e1612452d7a8f685dcd4d5',
            'primary_validator_node_identifier': PV_NID_ACCOUNT_NUMBER
        },
        nid_signing_key=sk
    )

    if send_to_bank:
        send_request_to_bank(signed_request)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'invalid-block-request.json'),
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
    url = f'{node_address}/invalid_blocks'
    results = post(url=url, body=signed_request)

    if isinstance(results, dict):
        for k, v in results.items():
            print(f'{k}: {v}')

    print(results)

    write_json(
        os.path.join(SIGNED_REQUESTS_DIR, 'invalid-block-response.json'),
        results
    )


if __name__ == '__main__':
    run(send_to_bank=True)
