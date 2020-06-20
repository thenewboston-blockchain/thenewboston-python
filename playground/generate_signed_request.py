from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.blocks.signatures import generate_signature
from thenewboston.constants.network import ACCEPTED
from thenewboston.utils.files import write_json
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key

# Bank
BANK_ACCOUNT_NUMBER = '5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8'

# Validator
VALIDATOR_ACCOUNT_NUMBER = 'ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314'
VALIDATOR_NID = '3afdf37573f1a511def0bd85553404b7091a76bcd79cdcebba1310527b167521'
VALIDATOR_REGISTRATION_FEE = 16


def generate_signed_create_bank_registration_request():
    """
    Generate signed create bank registration request
    """

    bank_signing_key = read_signing_key_file('signing_keys/bank_signing_key_file')
    bank_account_number_verify_key = get_verify_key(signing_key=bank_signing_key)

    # Payment block (for validator registration fees)
    block = generate_block(
        account_number=bank_account_number_verify_key,
        balance_lock=BANK_ACCOUNT_NUMBER,
        signing_key=bank_signing_key,
        transactions=[
            {
                'amount': VALIDATOR_REGISTRATION_FEE,
                'recipient': VALIDATOR_ACCOUNT_NUMBER,
            },
        ]
    )

    message = {
        'block': block,
        'validator_network_identifier': VALIDATOR_NID
    }

    # Signed request
    bank_nid_signing_key = read_signing_key_file('signing_keys/bank_nid_signing_key_file')
    bank_network_identifier = get_verify_key(signing_key=bank_nid_signing_key)
    signature = generate_signature(
        message=sort_and_encode(message),
        signing_key=bank_nid_signing_key
    )
    signed_request = {
        'message': message,
        'network_identifier': encode_verify_key(verify_key=bank_network_identifier),
        'signature': signature
    }

    write_json('bank-signed-request.json', signed_request)


def generate_signed_update_bank_registration_request():
    """
    Generate signed update bank registration request
    """

    signing_key = read_signing_key_file('signing_keys/validator_nid_signing_key_file')
    network_identifier = get_verify_key(signing_key=signing_key)

    message = {
        'status': ACCEPTED
    }

    signature = generate_signature(
        message=sort_and_encode(message),
        signing_key=signing_key
    )

    signed_request = {
        'message': message,
        'network_identifier': encode_verify_key(verify_key=network_identifier),
        'signature': signature
    }

    write_json('validator-signed-request.json', signed_request)


if __name__ == '__main__':
    generate_signed_create_bank_registration_request()
    # generate_signed_update_bank_registration_request()
