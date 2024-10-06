variable = input("Variable name:")
for n in variable:
    if n.isupper():
        print("_" + n.lower(), end="")
    else:
        print(n, end="")
print()