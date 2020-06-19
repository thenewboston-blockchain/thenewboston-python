from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.signatures import generate_signature
from thenewboston.constants.network import ACCEPTED
from thenewboston.utils.files import write_json
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key


def generate_signed_create_bank_registration_request():
    """
    Generate signed create bank registration request
    """

    signing_key = read_signing_key_file('bank_nid_signing_key_file')
    network_identifier = get_verify_key(signing_key=signing_key)

    message = {
        'status': ACCEPTED,
        'validator': 'a8101b03-15ad-42fc-8e64-2de24b850e0e'
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

    write_json('bank-signed-request.json', signed_request)


def generate_signed_update_bank_registration_request():
    """
    Generate signed update bank registration request
    """

    signing_key = read_signing_key_file('validator_nid_signing_key_file')
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
