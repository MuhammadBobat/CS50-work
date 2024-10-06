def main():
    question = convert(input("What is the time?"))
    if 7 <= question <= 8:
        print("breakfast time")
    elif 12 <= question <= 13:
        print("lunch time")
    elif 18 <= question <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    new_time = (hours + minutes)
    return(new_time)



main()