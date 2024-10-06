import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM)? to (\d{1,2}):?(\d{2})? (AM|PM)?$", s)
    if matches:
        #Declare variables
        hour = int(matches.group(1))
        end_hour = int(matches.group(4))

        #Check ValueError
        if matches.group(2):
            mins = matches.group(2)
            if int(mins) >= 60:
                raise ValueError
        if matches.group(5):
            end_mins = matches.group(5)
            if int(end_mins) >= 60:
                raise ValueError

        #Starting time
        if matches.group(3) == "AM" and hour == 12:
            hour = 0
        if matches.group(3) == "PM" and hour != 12:
            hour = hour + 12
        if matches.group(2) == None:
            start_time = f"{hour:02}:00"
        else:
            start_time = f"{hour:02}:{mins}"

        #Ending time
        if matches.group(6) == "AM" and end_hour == 12:
            end_hour = 0
        if matches.group(6) == "PM" and end_hour != 12:
            end_hour = end_hour + 12
        if matches.group(5) == None:
            end_time = f"{end_hour:02}:00"
        else:
            end_time = f"{end_hour:02}:{end_mins}"

        #Printing time
        return f"{start_time} to {end_time}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()