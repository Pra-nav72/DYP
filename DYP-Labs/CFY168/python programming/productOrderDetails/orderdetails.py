def get_order_details():
    print("--------- Enter Order Details ------------")
    order = {}
    order['product_name'] = input("Enter product name: ")
    order['quantity'] = int(input("Enter quantity: "))
    order['price_per_unit'] = float(input("Enter price per unit: "))
    return order
