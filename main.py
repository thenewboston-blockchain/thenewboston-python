from nodes.bank import Bank
from nodes.validator import Validator
from utils.display import display_bank, display_validator


def display_nodes(bank, validator):
    """
    Display nodes
    """

    display_bank(bank)
    display_validator(validator)


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

    tx = {
        'amount': 54,
        'balance_key': '960297be66dbdc83615a1a91ca515ae1',
        'recipient': 'validator123'
    }
    response = _validator.create_bank_registration(
        bank=_bank,
        signature='4234',
        tx=tx,
        verifying_key_hex='3123'
    )
    print(response)
