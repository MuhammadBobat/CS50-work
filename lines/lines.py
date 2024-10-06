import sys

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

try:
    user_file = sys.argv[1]
    file = open(user_file, "r")
    lines = file.readlines()
    count_lines = int()
    for line in lines:
        line = line.lstrip()
        if line.startswith("#") == False:
            if len(line.strip()) != 0:
                count_lines = count_lines + 1
    print(count_lines)

except FileNotFoundError:
    sys.exit("File does not exist")
    