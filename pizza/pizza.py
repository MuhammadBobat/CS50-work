import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a csv file")

table = []

try:
    file = sys.argv[1]
    file = open(file, "r")
    reader = csv.reader(file)
    for row in reader:
        table.append(row)
    print(tabulate(
        table[1:], headers=[table[0][0], "Small", "Large"],tablefmt="grid"
    ))



except FileNotFoundError:
    sys.exit("File does not exist")
