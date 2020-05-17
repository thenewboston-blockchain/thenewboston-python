from nodes.bank import Bank
from nodes.validator import Validator
from utils.display import display_bank, display_validator

if __name__ == '__main__':
    print()
    _bank = Bank(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    display_bank(_bank)

    print()
    _validator = Validator(
        ip_address='127.0.0.1',
        port=8001,
        protocol='http'
    )
    display_validator(_validator)
