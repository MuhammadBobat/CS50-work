def main():
    fraction = input("Fraction:")
    percentage = convert(fraction)
    new_percent = gauge(percentage)
    print(new_percent)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            percentage = float(x / y * 100)
            percentage = round(percentage)
            if percentage <= 100:
                return percentage

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()