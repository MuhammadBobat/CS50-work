import sys
import requests
import json

try:
    n = sys.argv[1]
    if n.isdigit() == True or "." in n:
        n = float(n)
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        value = response.json()
        c_bitcoin = value["bpi"]["USD"]["rate_float"]
        amount = c_bitcoin * n
        print(f"${amount:,.4f}")


    else:
        sys.exit("Command-line is not a number")
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

except requests.RequestException:
    print()





response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")