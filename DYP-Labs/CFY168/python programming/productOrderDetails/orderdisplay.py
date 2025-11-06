def display_order(order, total, discount):
    print("-------- ORDER SUMMARY --------")
    print(f"Product Name  : {order['product_name']}")
    print(f"Quantity      : {order['quantity']}")
    print(f"Price/Unit    : ₹{order['price_per_unit']}")
    print(f"Discount      : ₹{discount:.2f}")
    print(f"Total Amount  : ₹{total:.2f}")
    print("\n✅ Order placed successfully! Thank you for shopping.")
