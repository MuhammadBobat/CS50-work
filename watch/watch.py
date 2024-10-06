import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s.startswith("<iframe"):
        if matches := re.search(r"https?://(?:www\.)?youtube\.(?:com)/embed/(\w+)", s):
            code = matches.group(1)
            return f"https://youtu.be/{code}"







if __name__ == "__main__":
    main()