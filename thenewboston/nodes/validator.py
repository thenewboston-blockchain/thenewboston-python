from thenewboston.nodes.node import Node
from thenewboston.utils.blocks import validate_block
from thenewboston.utils.network import post


class Validator(Node):

    def __init__(self, *, ip_address, port, protocol):
        super().__init__(ip_address=ip_address, port=port, protocol=protocol)

    def create_bank_registration(self, *, bank, block):
        """
        Create bank registration
        """

        validate_block(block)

        body = {
            **block,
            'ip_address': bank.ip_address,
            'port': bank.port,
            'protocol': bank.protocol,
        }

        url = f'{self.address}/bank_registrations'
        results = post(url=url, body=body)
        return results
