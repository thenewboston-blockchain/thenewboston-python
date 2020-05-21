import json
from hashlib import sha3_256 as sha3
from os import path

from nacl.encoding import HexEncoder
from nacl.signing import SigningKey, VerifyKey

from thenewboston.utils.blocks import validate_block_format
from thenewboston.utils.files import read_json, write_json

BALANCE_SHEET_JSON = 'balance_sheet.json'


def create_account():
    """
    Create a new account
    Return signing_key, account_number
    """

    signing_key = SigningKey.generate()
    account_number = signing_key.verify_key
    return signing_key, account_number


def create_account_and_save_signing_key_file(file):
    """
    Create a new account
    Save signing key to file
    Return signing_key, account_number
    """

    signing_key, account_number = create_account()
    write_signing_key_file(signing_key, file)
    return signing_key, account_number


def encode_account_number(account_number):
    """
    Return the hexadecimal representation of the binary account number data
    """

    if not isinstance(account_number, VerifyKey):
        raise RuntimeError('account_number must be of type nacl.signing.VerifyKey')

    return account_number.encode(encoder=HexEncoder).decode('utf-8')


def generate_balance_lock(tx):
    """
    Generate a balance lock from a Tx
    """

    return sha3(sort_and_encode(tx)).digest().hex()


def generate_block(*, account_number, balance_lock, payments, signing_key):
    """
    Generate block
    """

    txs = []

    for payment in payments:
        tx = {
            'amount': payment['amount'],
            'balance_key': balance_lock,
            'recipient': payment['recipient']
        }
        balance_lock = generate_balance_lock(tx)
        txs.append(tx)

    message = sort_and_encode(txs)
    signature = generate_signature(message, signing_key)
    block = {
        'account_number': encode_account_number(account_number),
        'signature': signature.hex(),
        'txs': txs
    }
    return block


def generate_signature(message, signing_key):
    """
    Sign message using signing key and return signature
    """

    return signing_key.sign(message).signature


def get_account_number(signing_key):
    """
    Return the account number from the signing key
    """

    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')

    return signing_key.verify_key


def get_balance_lock_from_balance_sheet(account_number):
    """
    Get balance sheet lock
    """

    balance_sheet = read_json(BALANCE_SHEET_JSON)
    return balance_sheet[account_number]['balance_lock']


def read_signing_key_file(file):
    """
    Read signing key from file
    """

    with open(file, 'rb') as f:
        return SigningKey(f.read(), encoder=HexEncoder)


def sort_and_encode(dictionary):
    """
    Sort dictionary and return encoded data
    """

    return json.dumps(dictionary, sort_keys=True).encode('utf-8')


def update_balance_sheet(block):
    """
    Update balance sheet
    """

    account_number, txs = verify_block(block)

    balance_sheet = read_json(BALANCE_SHEET_JSON)
    account_data = balance_sheet[account_number]
    balance_lock = account_data['balance_lock']

    unlocked_tx = next((tx for tx in txs if tx['balance_key'] == balance_lock), None)

    while unlocked_tx:
        amount = unlocked_tx['amount']
        recipient = unlocked_tx['recipient']

        if recipient in balance_sheet:
            balance_sheet[recipient]['balance'] += amount
        else:
            balance_sheet[recipient] = {
                'balance': amount,
                'balance_lock': recipient
            }

        balance_lock = generate_balance_lock(unlocked_tx)
        balance_sheet[account_number]['balance'] -= amount
        balance_sheet[account_number]['balance_lock'] = balance_lock
        unlocked_tx = next((tx for tx in txs if tx['balance_key'] == balance_lock), None)

    write_json(BALANCE_SHEET_JSON, balance_sheet)


def verify_block(block):
    """
    Verify Tx block formatting, data, and signature
    """

    validate_block_format(block)

    account_number = block['account_number']
    signature = block['signature']
    txs = block['txs']

    if not txs:
        raise RuntimeError('No Txs to verify')

    tx_amounts = [tx['amount'] for tx in txs]

    if [tx_amount for tx_amount in tx_amounts if tx_amount <= 0]:
        raise RuntimeError('Invalid Tx amount')

    balance_sheet = read_json(BALANCE_SHEET_JSON)
    account_data = balance_sheet[account_number]
    balance = account_data['balance']
    balance_lock = account_data['balance_lock']

    if balance < sum(tx_amounts):
        raise RuntimeError('Not enough points')

    unlocked_tx = next((tx for tx in txs if tx['balance_key'] == balance_lock), None)

    if not unlocked_tx:
        raise RuntimeError(f'Block must contain Tx with balance_key matching balance_lock {balance_lock}')

    while unlocked_tx:
        balance_lock = generate_balance_lock(unlocked_tx)
        unlocked_tx = next((tx for tx in txs if tx['balance_key'] == balance_lock), None)

    verify_signature(
        account_number=account_number,
        signature=signature,
        message=sort_and_encode(txs)
    )

    return account_number, txs


def verify_signature(*, account_number, signature, message):
    """
    Verify signature
    """

    account_number = VerifyKey(account_number.encode('utf-8'), encoder=HexEncoder)
    signature = bytes.fromhex(signature)
    account_number.verify(message, signature)


def write_signing_key_file(signing_key, file):
    """
    Save signing key to file
    """

    if path.exists(file):
        raise RuntimeError(f'{file} already exists')

    with open(file, 'wb') as f:
        f.write(signing_key.encode(encoder=HexEncoder))


if __name__ == '__main__':
    _signing_key = read_signing_key_file('buckys_signing_key_file')
    _account_number = get_account_number(_signing_key)

    _payments = [
        {
            'amount': 25,
            'recipient': 'c6b14782902ee6eaa7bc86d843149e08f45dfd7e7fbc085e9aafd2e86d5e314b',
        },
        {
            'amount': 15,
            'recipient': '8b8b8815a45c7f1f2740f77a3b5d85e9c26fc400ec67e7a58114f996237e40d6',
        },
        {
            'amount': 10,
            'recipient': 'e245723754548550f4892bfc583e5c8bd749bebe1b54d362590d51e520185555',
        }
    ]

    _block = generate_block(
        account_number=_account_number,
        balance_lock='c0ff32df04f22180baef1c8d6df5b8e2e5441e65c0ccbfd2f6dc3e3d867b35bb',
        payments=_payments,
        signing_key=_signing_key,
    )

    write_json('block.json', _block)
    update_balance_sheet(_block)
