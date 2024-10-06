groceries = {}

while True:
    try:
        item = input().upper()

    except EOFError:
        break

    else:
        if item in groceries:
            groceries[item] = groceries[item] + 1
        else:
            groceries[item] = 1

#print items here
for item in sorted(groceries):
    print(groceries[item], item)