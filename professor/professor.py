import random
def main():
    level = get_level()
    score = game(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return x,y

def user_input(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                print("EEE")
                tries = tries + 1
        except:
            print("EEE")
            tries = tries + 1
    print(f"{x} + {y} = {x+y}")

def game(level):
    rounds = 0
    score = 0
    while rounds < 10:
        x, y = generate_integer(level)
        response = user_input(x, y)
        if response == True:
            score = score + 1
        rounds = rounds + 1
    return score

if __name__ == "__main__":
    main()
