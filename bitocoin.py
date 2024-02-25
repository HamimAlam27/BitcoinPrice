import requests
import json
import time

def main():
    print(crypto()

def crypto():
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    res = res.json()
    return(res["bpi"]["USD"]["rate_float"])

if __name__ == "__main__":
    while True:
        main()
        print("wait....")
        time.sleep(10)

