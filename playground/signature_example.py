import os

from playground.config import SIGNING_KEY_DIR
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.signatures import generate_signature
from thenewboston.utils.tools import sort_and_encode


def run():
    """
    Run main script
    """

    payload = {
        "balance_key": "6cb8f4fe23c57a1c169e5a193c59ad9f21bbe5a54d69c44a4522f4644bf5b2a2",
        "txs": [
            {
                "amount": 5.5,
                "recipient": "484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc"
            },
            {
                "amount": 1,
                "recipient": "5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8"
            },
            {
                "amount": 4,
                "recipient": "ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314"
            }
        ]
    }
    print(sort_and_encode(payload))
    signing_key = read_signing_key_file(os.path.join(SIGNING_KEY_DIR, 'sample'))
    signature = generate_signature(
        message=sort_and_encode(payload),
        signing_key=signing_key
    )
    print(signature)


if __name__ == '__main__':
    run()
