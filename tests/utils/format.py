from thenewboston.utils.format import format_address


def test_format_address():
    ip_address = '127.0.0.1'
    port = '80'
    protocol = 'http'
    assert f'{protocol}://{ip_address}:{port}' == format_address(ip_address=ip_address, port=port, protocol=protocol)
    assert f'{protocol}://{ip_address}' == format_address(ip_address=ip_address, port='', protocol=protocol)
