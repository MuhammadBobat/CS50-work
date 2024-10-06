def main():
    greeting = input("Greeting:").strip()
    money = value(greeting)
    print(f"${money})

def value(greeting):
    if greeting.lower().startswith("h") == True:
        if greeting.lower().startswith("hello") == True:
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()