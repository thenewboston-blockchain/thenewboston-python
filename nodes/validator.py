from nodes.node import Node
from utils.network import post


class Validator(Node):

    def __init__(self, *, ip_address, port, protocol):
        super().__init__(ip_address=ip_address, port=port, protocol=protocol)

    def create_bank_registration(self, *, bank, signature, tx, verifying_key_hex):
        """
        Create bank registration
        """

        body = {
            'ip_address': bank.ip_address,
            'port': bank.port,
            'protocol': bank.protocol,
            'signature': signature,
            'txs': [tx],
            'verifying_key_hex': verifying_key_hex
        }
        url = f'{self.address}/bank_registrations'
        results = post(url=url, body=body)
        return results
