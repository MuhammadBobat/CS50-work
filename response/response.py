from validator_collection import checkers
email = input("What's your email address?")
is_email = checkers.is_email(email)
if is_email == True:
    print("Valid")
else:
    print("Invalid")