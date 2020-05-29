from thenewboston.blocks.balance_lock import generate_balance_lock
from thenewboston.blocks.signatures import verify_signature
from thenewboston.utils.tools import sort_and_encode


def validate_block(*, balance_lock, block):
    """
    Validate block:
    - Tx formatting
    - Tx chaining
    - signature
    """

    validate_block_format(block)

    account_number = block['account_number']
    signature = block['signature']
    txs = block['txs']

    if not txs:
        raise RuntimeError('No Txs to verify')

    validate_block_transaction_chain(
        balance_lock=balance_lock,
        txs=txs
    )
    verify_signature(
        message=sort_and_encode(txs),
        signature=signature,
        verify_key=account_number
    )

    return account_number, txs


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


def validate_block_transaction_chain(*, balance_lock, txs):
    """
    Validate that a block:
    - has Txs
    - does not contain any Txs with amounts <= 0
    - has Txs properly chained
    """

    if not txs:
        raise RuntimeError('No Txs to verify')

    if [tx for tx in txs if tx['amount'] <= 0]:
        raise RuntimeError('Invalid Tx amount')

    unlocked_tx = next((tx for tx in txs if tx['balance_key'] == balance_lock), None)

    if not unlocked_tx:
        raise RuntimeError(f'Block must contain Tx with balance_key matching balance_lock {balance_lock}')

    unlocked_tx_counter = 0

    while unlocked_tx:
        unlocked_tx_counter += 1
        balance_lock = generate_balance_lock(tx=unlocked_tx)
        unlocked_tx = next((tx for tx in txs if tx['balance_key'] == balance_lock), None)

    if unlocked_tx_counter != len(txs):
        raise RuntimeError(f'Invalid block, unlocked {unlocked_tx_counter}/{len(txs)} Txs')
