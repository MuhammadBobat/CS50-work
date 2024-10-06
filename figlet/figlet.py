import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()


if len(sys.argv) == 3:
    font_type = sys.argv[1]
    font_name = sys.argv[2]

    if font_name not in figlet.getFonts():
        sys.exit("Invalid Usage")

    if font_type == "-f" or font_type == "--font":
        string = input("Input: ")
        figlet.setFont(font=font_name)
        print(figlet.renderText(string))

    else:
        sys.exit("Invalid Usage")
elif len(sys.argv) < 2:
    string = input("Input: ")
    figlet.setFont() == random.choice(figlet.getFonts())
    print(figlet.renderText(string))

else:
    sys.exit("Invalid Usage")