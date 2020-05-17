from nodes.node import Node


class Validator(Node):

    def __init__(self, *, ip_address, port, protocol):
        super().__init__(ip_address=ip_address, port=port, protocol=protocol)
