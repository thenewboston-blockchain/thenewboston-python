def validate_transaction_exists(*, amount, error, recipient, txs):
    """
    Check for the existence of a Tx
    """

    tx = next((tx for tx in txs if tx.get('amount') >= amount and tx.get('recipient') == recipient), None)

    if not tx:
        raise error({
            'error_message': 'Tx not found',
            'expected_amount': amount,
            'expected_recipient': recipient
        })
