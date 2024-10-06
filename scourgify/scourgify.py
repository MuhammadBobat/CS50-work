import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a csv file")

before_file = sys.argv[1]
after_file = sys.argv[2]
new = []

try:
    before_file = open(before_file, "r")
    reader = csv.DictReader(before_file)
    for row in reader:
        surname, forename = row["name"].split(",")
        new.append({"first":forename.lstrip(),"last":surname,"house":row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {before_file}")

after_file = open(after_file, "w")
writer = csv.DictWriter(after_file, fieldnames=["first","last","house"])
writer.writerow({"first": "first", "last": "last", "house": "house"})
for line in new:
    writer.writerow({
        "first":line["first"],"last":line["last"],"house":line["house"]
    })
