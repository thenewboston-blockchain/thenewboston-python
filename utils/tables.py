from prettytable import PrettyTable


def display_list(*, list_items, excluded=None):
    """
    Display formatted table of list items
    """

    if not list_items:
        return

    pt = PrettyTable()
    list_headers = get_list_headers(list_items)
    list_headers = [i for i in list_headers if i not in excluded] if excluded else list_headers
    pt.field_names = list_headers

    for item in list_items:
        pt.add_row([item.get(i) for i in list_headers])

    print(pt)


def get_list_headers(list_items):
    """
    Get headers from a list of dictionaries
    """

    first_item = list_items[0]
    return first_item.keys()
