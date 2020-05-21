def validate_block_format(block):
    """
    Validate that block is properly formatted
    """

    account_number = block.get('account_number')
    signature = block.get('signature')
    txs = block.get('txs')

    if not isinstance(account_number, str):
        raise TypeError('Block must include account_number of type str')

    if not isinstance(signature, str):
        raise TypeError('Block must include signature of type str')

    if not isinstance(txs, list):
        raise TypeError('Block must include list of txs (empty lists are acceptable)')
