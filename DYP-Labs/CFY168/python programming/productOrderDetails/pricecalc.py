def calculate_total(order):
    total = order['quantity'] * order['price_per_unit']
    discount = 0

    if total > 1000:
        discount = total * 0.12
        total -= discount

    return total, discount
