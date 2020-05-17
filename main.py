from nodes.bank import Bank
from utils.tables import display_item, display_list


def display_bank(bank):
    """
    Display bank details
    """

    config = bank.get_config()
    display_item(config, title='Config')

    bank_registration_list = bank.get_bank_registration_list()
    display_list(
        bank_registration_list,
        title='Bank Registrations'
    )

    bank_transaction_list = bank.get_bank_transaction_list()
    display_list(
        bank_transaction_list,
        excluded=['created_date', 'modified_date'],
        title='Bank Transactions'
    )

    bank_list = bank.get_bank_list()
    display_list(
        bank_list,
        title='Banks'
    )

    member_list = bank.get_member_list()
    display_list(
        member_list,
        excluded=['created_date', 'modified_date'],
        title='Members'
    )

    member_registration_list = bank.get_member_registration_list()
    display_list(
        member_registration_list,
        excluded=['created_date', 'modified_date'],
        title='Member Registrations'
    )

    self_transaction_fee_tier_list = bank.get_self_transaction_fee_tier_list()
    display_list(
        self_transaction_fee_tier_list,
        ascending=False,
        order_by='trust',
        title='Self Transaction Fee Tiers'
    )

    validator_list = bank.get_validator_list()
    display_list(
        validator_list,
        title='Validators'
    )

    validator_transaction_fee_tier_list = bank.get_validator_transaction_fee_tier_list()
    display_list(
        validator_transaction_fee_tier_list,
        title='Validator Transaction Fee Tiers'
    )


if __name__ == '__main__':
    _bank = Bank(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )
    display_bank(_bank)
