ORDERS = [
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 1
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 2
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 3
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 4
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 5
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 6
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 7
    },
    {
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1,
      "id": 8
    },
    {
      "styleId": 2,
      "sizeId": 3,
      "metalId": 3,
      "id": 9
    },
    {
      "styleId": 3,
      "sizeId": 5,
      "metalId": 5,
      "id": 10
    },
    {
      "styleId": 1,
      "sizeId": 4,
      "metalId": 3,
      "id": 11
    },
    {
      "styleId": 2,
      "sizeId": 3,
      "metalId": 4,
      "id": 12
    },
    {
      "styleId": 3,
      "sizeId": 3,
      "metalId": 3,
      "id": 13
    }
  ]

def get_all_orders():
    return ORDERS

# Function with a single parameter
def get_single_order(id):
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the orderS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the orderS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
