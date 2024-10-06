print("Amount Due: 50")
price = int(50)
coin = int()
while price > 0:
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        price = price - coin
        if price < 0:
            print("Change owed:", price * -1)
            break
        print("Amount Due:", price)
    else:
        print("50")





