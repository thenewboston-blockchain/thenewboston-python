from thenewboston.accounts.key_files import read_signing_key_file, write_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json
from thenewboston.verify_keys.verify_key import encode_verify_key, get_verify_key
from thenewboston.accounts.manage import create_account

if __name__ == '__main__':
    # signing_key, account_number = create_account()
    # write_signing_key_file(signing_key, 'treasury_signing_key_file')

    signing_key = read_signing_key_file('buckys_signing_key_file')
    account_number = get_verify_key(signing_key=signing_key)

    encoded_account_number = encode_verify_key(verify_key=account_number)
    print(encoded_account_number)

    payments = [
        {
            'amount': 2,
            'recipient': 'bank_001',
        },
        {
            'amount': 2,
            'recipient': 'validator_001',
        },
        {
            'amount': 90,
            'recipient': 'min',
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock='684b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbl',
        payments=payments,
        signing_key=signing_key,
    )
    write_json('block-4.json', block)
