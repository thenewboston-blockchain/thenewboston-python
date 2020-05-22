from thenewboston.accounts.account_numbers import encode_account_number, get_account_number
from thenewboston.accounts.key_files import read_signing_key_file
from thenewboston.blocks.block import generate_block
from thenewboston.utils.files import write_json

if __name__ == '__main__':
    # signing_key, account_number = create_account()
    # write_signing_key_file(signing_key, 'buckys_signing_key_file')
    signing_key = read_signing_key_file('buckys_signing_key_file')
    account_number = get_account_number(signing_key=signing_key)

    encoded_account_number = encode_account_number(account_number=account_number)
    print(encoded_account_number)

    payments = [
        {
            'amount': 2,
            'recipient': 'bank_001',
        },
        {
            'amount': 2,
            'recipient': 'validator_001',
        }
    ]
    block = generate_block(
        account_number=account_number,
        balance_lock='484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc',
        payments=payments,
        signing_key=signing_key,
    )

    print(block)
    write_json('block.json', block)
