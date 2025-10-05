#shopping cart using list[]
items= []
prices = []
total = 0

while True:
    item = input("Enter item name(x to quit): ")
    if item.lower() == 'x':
        break
    else:
        items.append(item)
        price = float(input("Enter the price: ₹"))
        prices.append(price)
        total += price
print(items)
print(prices)

print(f"Total Cart cost is ₹{total}")