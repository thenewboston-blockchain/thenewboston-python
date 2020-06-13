from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.balance_lock import generate_balance_lock
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.verify_keys.verify_key import get_verify_key

# Bank
BANK_ACCOUNT_NUMBER = '5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8'
BANK_REGISTRATION_FEE = 2
BANK_TX_FEE = 1

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
    balance_lock = 'df246a329d6eff183c53f5c2704626e03ca29e00aa55e68e643551f63d10e886'

    transactions = [
        {
            'amount': BANK_TX_FEE,
            'recipient': BANK_ACCOUNT_NUMBER,
        },
        {
            'amount': VALIDATOR_TX_FEE,
            'recipient': VALIDATOR_ACCOUNT_NUMBER,
        },
        {
            'amount': 4.125,
            'recipient': BUCKY_ACCOUNT_NUMBER,
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock=balance_lock,
        signing_key=signing_key,
        transactions=transactions
    )

    next_balance_lock = generate_balance_lock(message=block['message'])
    print(f'Next balance lock will be: {next_balance_lock}')

    write_json('valid-block.json', block)


def create_member_registration_block():
    """
    Create block used for:
    - POST /member_registrations
    """

    signing_key = read_signing_key_file('treasury_signing_key_file')
    account_number = get_verify_key(signing_key=signing_key)
    balance_lock = '0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb'

    transactions = [
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
        signing_key=signing_key,
        transactions=transactions
    )

    next_balance_lock = generate_balance_lock(message=block['message'])
    print(f'Next balance lock will be: {next_balance_lock}')

    write_json('member-registration-block.json', block)


if __name__ == '__main__':
    create_block()
    # create_member_registration_block()
