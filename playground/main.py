from thenewboston.accounts.key_files import read_signing_key_file, write_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key
from thenewboston.accounts.manage import create_account

# Bank
BANK_ACCOUNT_NUMBER = '5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8'
BANK_REGISTRATION_FEE = 2
BANK_TX_FEE = 2

# Validator
VALIDATOR_ACCOUNT_NUMBER = 'ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314'
VALIDATOR_TX_FEE = 2

# Users
BUCKY_ACCOUNT_NUMBER = '484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc'


def create_block():
    """
    Create block used for:
    - POST /blocks
    """

    signing_key = read_signing_key_file('treasury_signing_key_file')
    account_number = get_verify_key(signing_key=signing_key)
    balance_lock = '0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb'

    payments = [
        {
            'amount': BANK_TX_FEE,
            'recipient': BANK_ACCOUNT_NUMBER,
        },
        {
            'amount': VALIDATOR_TX_FEE,
            'recipient': VALIDATOR_ACCOUNT_NUMBER,
        },
        {
            'amount': 20,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock=balance_lock,
        payments=payments,
        signing_key=signing_key,
    )
    write_json('valid-block.json', block)


def create_member_registration_block():
    """
    Create block used for:
    - POST /member_registrations
    """

    signing_key = read_signing_key_file('treasury_signing_key_file')
    account_number = get_verify_key(signing_key=signing_key)
    balance_lock = '0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb'

    payments = [
        {
            'amount': BANK_REGISTRATION_FEE,
            'recipient': BANK_ACCOUNT_NUMBER,
        },
        {
            'amount': VALIDATOR_TX_FEE,
            'recipient': VALIDATOR_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock=balance_lock,
        payments=payments,
        signing_key=signing_key,
    )
    block['balance_lock'] = balance_lock
    write_json('member-registration-block.json', block)


if __name__ == '__main__':
    # signing_key, account_number = create_account()
    # write_signing_key_file(signing_key, 'vr1')
    # encoded_account_number = encode_verify_key(verify_key=account_number)
    # print(encoded_account_number)

    create_block()
