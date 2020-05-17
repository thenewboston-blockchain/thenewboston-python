from thenewboston.nodes.node import Node
from thenewboston.utils.network import fetch


class Bank(Node):

    def __init__(self, *, ip_address, port, protocol):
        super().__init__(ip_address=ip_address, port=port, protocol=protocol)

    def get_bank_transaction_list(self):
        """
        Return a list of bank transactions
        """

        url = f'{self.address}/bank_transactions'
        results = fetch(url=url, headers={})
        return results

    def get_member_list(self):
        """
        Return a list of members
        """

        url = f'{self.address}/members'
        results = fetch(url=url, headers={})
        return results

    def get_member_registration_list(self):
        """
        Return a list of member registrations
        """

        url = f'{self.address}/member_registrations'
        results = fetch(url=url, headers={})
        return results

    def get_validator_list(self):
        """
        Return a list of validators
        """

        url = f'{self.address}/validators'
        results = fetch(url=url, headers={})
        return results

    def get_validator_transaction_fee_tier_list(self):
        """
        Return a list of validator transaction fee tiers
        """

        url = f'{self.address}/validator_transaction_fee_tiers'
        results = fetch(url=url, headers={})
        return results
