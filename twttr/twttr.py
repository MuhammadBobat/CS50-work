def main():
    string = input("Input:")
    print(shorten(string))

def shorten(word):
    for n in word:
        if n == "a" or n == "i" or n == "o" or n == "e" or n == "u":
            word = word.replace(n,"")
        elif n == "A" or n == "I" or n == "O" or n == "E" or n == "U":
            word = word.replace(n,"")
    return word

if __name__ == "__main__":
    main()