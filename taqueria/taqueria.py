menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
price = float()

while True:
    try:
        item = input("Item:").title()
        if item in menu:
            price = price + menu[item]
            rounded_price = "{:.2f}".format(price)
            print(f"Total: ${rounded_price}")

    except EOFError:   #if they are finished...
        print()
        break

