def validate_block(block):
    """
    Validate that block is properly formatted
    """

    txs = block.get('txs')
    signature = block.get('signature')
    verifying_key_hex = block.get('verifying_key_hex')

    if not isinstance(txs, list):
        raise TypeError('Block must include list of txs (empty lists are acceptable)')

    if not isinstance(signature, str):
        raise TypeError('Block must include signature of type str')

    if not isinstance(verifying_key_hex, str):
        raise TypeError('Block must include verifying_key_hex of type str')
