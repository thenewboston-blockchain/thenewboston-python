import ipaddress

from config.constants import PROTOCOL_CHOICES
from utils.format import format_address
from utils.network import fetch


class Bank:

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

    def get_member_list(self):
        """
        Return a list of members
        """

        url = f'{self.address}/members'
        results = fetch(url=url, headers={})
        return results
