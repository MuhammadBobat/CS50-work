import random
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except:
        pass

number = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < number:
                print ("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass