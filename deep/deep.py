question = input("What's the answer to the Great Question of Life...?")
if question.strip() == "42":
    print("Yes")
elif question.lower() == "forty-two":
    print("Yes")
elif question.lower() == "forty two":
    print("Yes")
else:
    print("No")
