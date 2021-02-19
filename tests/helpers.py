from operator import itemgetter

from thenewboston.accounts.manage import create_account
from thenewboston.utils.tools import sort_and_encode
from thenewboston.verify_keys.verify_key import encode_verify_key


def random_encoded_account_number():
    signing_key, account_number = create_account()
    return encode_verify_key(verify_key=account_number)


def generate_message(encoded_account_number):
    transactions = get_transactions()
    message = {
        'balance_key': encoded_account_number,
        'txs': sorted(transactions, key=itemgetter('recipient'))
    }
    message = sort_and_encode(message)
    return message


def get_transactions():
    transactions = [
        {
            'amount': 1,
            'recipient': random_encoded_account_number(),
        }
    ]
    return transactions
