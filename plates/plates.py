def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0:2].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for char in s:
        if char == " " or char == "." or char == "!" or char == "?":
            return False
        if char.isdigit():
            index = s.index(char)
            if s[index:].isdigit():
                return True
            else:
                return False
    return True

if __name__ == "__main__":
    main()