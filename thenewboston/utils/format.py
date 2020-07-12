def format_address(*, ip_address, port, protocol):
    """
    Format address
    """

    port = f':{port}' if port else ''
    return f'{protocol}://{ip_address}{port}'


def format_node_address(*, node):
    """
    Format address for node
    """

    ip_address = node.ip_address
    port = f':{node.port}' if node.port else ''
    protocol = node.protocol
    return f'{protocol}://{ip_address}{port}'
