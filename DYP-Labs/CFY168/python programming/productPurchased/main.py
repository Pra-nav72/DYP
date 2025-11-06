from productOrderDetails import orderdetails, pricecalc, orderdisplay

def main():
    order = orderdetails.get_order_details()
    total, discount = pricecalc.calculate_total(order)
    orderdisplay.display_order(order, total, discount)

if __name__ == "__main__":
    main()
