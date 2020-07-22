from playground.config import TREASURY_ACCOUNT_NUMBER
from thenewboston.utils.format import format_address
from thenewboston.utils.network import fetch


def get_account_balance_lock(*, account_number, live_pv=False):
    """
    Return the balance lock for the given account
    """

    if live_pv:
        pv_address = format_address(
            ip_address='64.225.47.205',
            port=None,
            protocol='http'
        )
    else:
        pv_address = format_address(
            ip_address='192.168.1.75',
            port=8000,
            protocol='http'
        )

    url = f'{pv_address}/account_balance_lock/{account_number}'
    results = fetch(url=url, headers={})
    return results['balance_lock']


if __name__ == '__main__':
    get_account_balance_lock(account_number=TREASURY_ACCOUNT_NUMBER)
