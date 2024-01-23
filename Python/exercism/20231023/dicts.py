#%%
"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    dict_inventory = {}
    for item in items:
        if dict_inventory.get(item, 'NULL') == 'NULL':
            dict_inventory[item] = 1
        else:
            dict_inventory[item] = dict_inventory[item]+1
    return dict_inventory



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    dict_inventory = inventory
    for item in items:
        if dict_inventory.get(item, 'NULL') == 'NULL':
            dict_inventory[item] = 1
        else:
            dict_inventory[item] = dict_inventory[item] +1
    return dict_inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    dict_inventory = inventory
    for item in items:
        if dict_inventory.get(item, 'NULL') == 'NULL':
            dict_inventory[item] = 1
        elif dict_inventory.get(item, 'NULL') > 0:
            dict_inventory[item] = dict_inventory[item] -1
    return dict_inventory



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    dict_inventory = inventory
    if dict_inventory.get(item, "NULL") != "NULL":
        dict_inventory.pop(item)
    return dict_inventory



def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_inventory_result = []
    for product, amount in inventory.items():
        if amount > 0:
            list_inventory_result.append((product, amount))
    return list_inventory_result

#%%
#create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
#add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
#decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])

#remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
#remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})