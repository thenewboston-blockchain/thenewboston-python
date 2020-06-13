from thenewboston.blocks.signatures import verify_signature
from thenewboston.utils.tools import sort_and_encode


def validate_block(*, block):
    """
    Validate block:
    - formatting
    - signature
    """

    validate_block_format(block)
    verify_signature(
        message=sort_and_encode(block['message']),
        signature=block['signature'],
        verify_key=block['account_number']
    )
    return block


def validate_block_format(block):
    """
    Validate that block is properly formatted
    """

    account_number = block.get('account_number')
    message = block.get('message')
    signature = block.get('signature')

    if not isinstance(account_number, str):
        raise TypeError('Block must include account_number of type str')

    if not isinstance(message, dict):
        raise TypeError('Block must include message of type dict')

    balance_key = message.get('balance_key')
    txs = message.get('txs')

    if not isinstance(balance_key, str):
        raise TypeError('message must include balance_key of type str')

    if not isinstance(txs, list):
        raise TypeError('message must include list of txs')

    if not isinstance(signature, str):
        raise TypeError('Block must include signature of type str')
