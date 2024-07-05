"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    v_current_cart = current_cart
    for i in items_to_add:
        value = v_current_cart.setdefault(i, "N")
        if value != "N":
            v_aux = v_current_cart[i] + 1
            v_current_cart.update({i: v_aux})
        else:
            v_current_cart.update({i: 1})
    return v_current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    new_cart = {}
    if len(notes) > 0:
        add_item(new_cart, notes)
    return new_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    v_ideas_dict: dict = ideas
    for update in recipe_updates:
        v_ideas_dict.update({update[0]: update[1]})
    return v_ideas_dict


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return sorted(cart.items())


def send_to_store(cart: dict, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    order: dict = cart
    for item in cart:
        aux_order: list = [cart[item]] + aisle_mapping[item]
        order.update({item: aux_order})
    return sorted(order.items(), reverse=True)


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    inventory: dict = store_inventory
    for item in fulfillment_cart:
        aux_inventory_qtd = store_inventory[item][0] - fulfillment_cart[item][0]

        if aux_inventory_qtd == 0:
            inventory.update({item: ["Out of Stock", store_inventory[item][1], store_inventory[item][2]]})
        else:
            inventory.update({item: [aux_inventory_qtd, store_inventory[item][1], store_inventory[item][2]]})
    return inventory



#testes
# cart = add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},('Apple', 'Apple', 'Orange', 'Apple', 'Banana', 'Kiwi', 'Kiwi', 'Tomato'))
# print(cart)
#
# new_cart = read_notes(('Banana','Apple', 'Orange', 'Banana' ))
# print(new_cart)
#
# new_ideias = update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                     'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
# (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
#
# print(new_ideias)
# new_ideias = update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
#                         'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
#                         'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
#                [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
#                             ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
#                             ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})])
# print(new_ideias)
#
# sorted_cart = sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1})
#
# print(sorted_cart)

# order = send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
#                       {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False],
#                        'Milk': ['Aisle 2', True]})
#
# print(order)

inventory = update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
                                    {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]})
print(inventory)
