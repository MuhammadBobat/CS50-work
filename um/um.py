import re

def main():
    print(count(input("Text: ")))


def count(s):
    number = re.findall(r"\b(u|U)m", s, re.IGNORECASE)
    if number:
        return len(number)


if __name__ == "__main__":
    main()