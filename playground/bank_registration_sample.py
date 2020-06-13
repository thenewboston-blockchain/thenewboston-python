from thenewboston.nodes.bank import Bank
from thenewboston.nodes.validator import Validator
from thenewboston.utils.display import display_bank, display_validator


def display_nodes(bank, validator):
    """
    Display nodes
    """

    display_bank(bank)
    display_validator(validator)


def get_test_block():
    """
    Return test block
    """

    return {
        'txs': [
            {
                'amount': 54,
                'balance_key': '960297be66dbdc83615a1a91ca515ae1',
                'recipient': 'validator123'
            }
        ],
        'signature': '93c4f312326e08b508db1fc6204b98655742554318cab5b73b2b5',
        'verifying_key_hex': 'a30e83483996d83b06ff53d1c022c79420b'
    }


if __name__ == '__main__':
    _bank = Bank(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )

    _validator = Validator(
        ip_address='127.0.0.1',
        port=8001,
        protocol='http'
    )

    response = _validator.create_bank_registration(
        bank=_bank,
        block=get_test_block()
    )
    print(response)
