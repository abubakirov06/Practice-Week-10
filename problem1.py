def receipt_generator(products, cart):
    total = 0
    print()
    for c in cart:
        if c in products:
            print(f'{products[c][0]}: ${products[c][1]:.2f}')
            total += products[c][1]
        else:
            print(f'Item {c} not found.')
    print('--------------------')
    print(f'Grand Total: ${total}\n')

products = {
    "101": ("Milk", 2.50),
    "102": ("Eggs", 3.00),
    "103": ("Bread", 1.75),
    "104": ("Cheese", 4.50),
    "105": ("Apple", 0.50)
}
cart = ["101", "105", "105", "999", "103", "105"]
receipt_generator(products, cart)