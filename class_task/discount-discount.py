def discount():
    price = int(input("Please enter your price: \n"))
    discount_price = price * 0.1
    new_price = price - discount_price
    print(f"Your former price is {price} with a 10% discount, you now have {new_price}")


discount()
