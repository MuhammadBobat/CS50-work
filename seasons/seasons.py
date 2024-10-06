import re
import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    dob = get_date(input("Date of Birth:"))
    day = int(dob[2])
    month = int(dob[1])
    year = int(dob[0])
    current_date = date.today()
    dob = date(year,month,day)
    age = current_date - dob
    minutes = age.days * 24 * 60
    words = p.number_to_words(minutes, andword="").capitalize()
    print(f"{words} minutes")


def get_date(dob):
    if re.search("^....-..-..$", dob):
        dob = dob.split("-")
        return dob
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()