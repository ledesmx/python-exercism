"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    dictionary = {}
    for item in items:
        if dictionary.get(item):
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    
    return dictionary


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    new_inventory = dict(inventory)
    for item in items:
        if new_inventory.get(item):
            new_inventory[item] += 1
        else:
            new_inventory[item] = 1
    
    return new_inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    new_inventory = dict(inventory)
    for item in items:
        if new_inventory.get(item) and new_inventory.get(item) > 0:
            new_inventory[item] -= 1
    
    return new_inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    new_inventory = dict(inventory)
    new_inventory.pop(item, "")
    return new_inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    inventory_list = []
    for key, value in inventory.items():
        if value == 0:
            continue
        inventory_list.append((key, value))
    return inventory_list
