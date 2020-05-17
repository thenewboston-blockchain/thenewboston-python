from nodes.bank import Bank
from utils.tables import display_list

if __name__ == '__main__':
    bank = Bank(
        ip_address='192.168.1.232',
        port=8000,
        protocol='http'
    )

    member_list = bank.get_member_list()
    display_list(
        list_items=member_list,
        excluded=['created_date', 'modified_date']
    )
