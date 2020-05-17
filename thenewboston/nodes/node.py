import ipaddress

from thenewboston.config.constants import PROTOCOL_CHOICES
from thenewboston.utils.format import format_address
from thenewboston.utils.network import fetch


class Node:

    def __init__(self, *, ip_address, port, protocol):
        self.ip_address = ip_address
        self.port = port
        self.protocol = protocol
        self._validate_init()
        self.address = format_address(ip_address=ip_address, port=port, protocol=protocol)

    def _validate_init(self):
        """
        Validate initialization of class
        """

        try:
            ipaddress.ip_address(self.ip_address)
        except ValueError:
            raise RuntimeError('Invalid ip_address')

        if self.port and not isinstance(self.port, int):
            raise RuntimeError('Invalid port, must be integer or None')

        if self.protocol not in PROTOCOL_CHOICES:
            raise RuntimeError(f'Invalid protocol, choices are {PROTOCOL_CHOICES}')

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

    def get_config(self):
        """
        Return config
        """

        url = f'{self.address}/config'
        results = fetch(url=url, headers={})
        return results

    def get_self_transaction_fee_tier_list(self):
        """
        Return a list of self transaction fee tiers
        """

        url = f'{self.address}/self_transaction_fee_tiers'
        results = fetch(url=url, headers={})
        return results
