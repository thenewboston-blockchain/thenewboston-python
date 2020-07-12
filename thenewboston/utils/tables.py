from operator import itemgetter

from prettytable import PrettyTable


def display_item(item, *, excluded=None, title=None):
    """
    Display dictionary in table format
    """

    if not item:
        return

    pt = PrettyTable(header=False)

    excluded = excluded or []
    items = [[k, v] for k, v in item.items() if k not in excluded]

    for item in items:
        pt.add_row(item)

    if title:
        print(title)

    print(f'{pt}\n')


def display_list(list_items, *, ascending=True, excluded=None, order_by=None, title=None):
    """
    Display formatted table of list items
    """

    if not list_items:
        return

    pt = PrettyTable()
    list_headers = get_list_headers(list_items)
    list_headers = [i for i in list_headers if i not in excluded] if excluded else list_headers
    pt.field_names = list_headers

    if order_by:
        list_items = sorted(list_items, key=itemgetter(order_by), reverse=not ascending)

    for item in list_items:
        pt.add_row([item.get(i) for i in list_headers])

    if title:
        print(title)

    print(f'{pt}\n')


def get_list_headers(list_items):
    """
    Get headers from a list of dictionaries
    """

    first_item = list_items[0]
    return first_item.keys()
