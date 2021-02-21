from tests.helpers import random_encoded_account_number
from thenewboston.transactions.validation import validate_transaction_exists

def test_validate_transaction_exists():
    account = random_encoded_account_number()
    amount = 1
    fee = 1
    error = RuntimeError
    transactions = [
        {
            'amount': amount,
            'fee' : fee,
            'recipient': account,
        },
        {
            'amount': 2,
            'fee' : fee,
            'recipient': account,
        },        
    ]
    try:
        validate_transaction_exists(amount=amount, fee=fee, error=error, recipient=account, txs=transactions)
        validate_transaction_exists(amount=amount+1, fee=fee, error=error, recipient=account, txs=transactions)
        assert True
    except error:
        assert False
    try:
        validate_transaction_exists(amount=amount, fee=3, error=error, recipient=account, txs=transactions)
        validate_transaction_exists(amount=amount, fee=fee, error=error, recipient=random_encoded_account_number(), txs=transactions)
        assert False
    except error:
        assert True