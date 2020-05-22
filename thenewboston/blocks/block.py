from thenewboston.accounts.account_numbers import encode_account_number
from thenewboston.blocks.balance_lock import generate_balance_lock
from thenewboston.blocks.signatures import generate_signature
from thenewboston.utils.tools import sort_and_encode


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
        balance_lock = generate_balance_lock(tx=tx)
        txs.append(tx)

    message = sort_and_encode(txs)
    block = {
        'account_number': encode_account_number(account_number=account_number),
        'signature': generate_signature(message=message, signing_key=signing_key),
        'txs': txs
    }
    return block
