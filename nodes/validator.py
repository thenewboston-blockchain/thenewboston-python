from nodes.node import Node
from utils.network import fetch


class Validator(Node):

    def __init__(self, *, ip_address, port, protocol):
        super().__init__(ip_address=ip_address, port=port, protocol=protocol)

    def get_bank_registration_list(self):
        """
        Return a list of bank registrations
        """

        url = f'{self.address}/bank_registrations'
        results = fetch(url=url, headers={})
        return results

    def get_bank_list(self):
        """
        Return a list of banks
        """

        url = f'{self.address}/banks'
        results = fetch(url=url, headers={})
        return results

    def get_self_transaction_fee_tier_list(self):
        """
        Return a list of self transaction fee tiers
        """

        url = f'{self.address}/self_transaction_fee_tiers'
        results = fetch(url=url, headers={})
        return results
