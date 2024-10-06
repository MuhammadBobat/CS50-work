import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_conditions()
    try:
        imagefile = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = ImageOps.fit(imagefile, size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

#ARGV requirements:
def check_conditions():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    split1 = splitext(sys.argv[1])
    split2 = splitext(sys.argv[2])
    if split1[1] not in [".jpg", ".jpeg", ".png"] or split2[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")
    if split1[1] != split2[1]:
        sys.exit("Input and output have different extensions")

main()