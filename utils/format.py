def format_address(*, ip_address, port, protocol):
    """
    Format address
    """

    port = f':{port}' if port else ''
    return f'{protocol}://{ip_address}{port}'
