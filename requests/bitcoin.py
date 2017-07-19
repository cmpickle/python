import requests

r = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/sell")
sellAmount = r.json()["data"]["amount"]

r2 = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
buyAmount = r2.json()["data"]["amount"]

print("------------------------------------")
print("|  Sell Amount\t  | Buy Amount\t   |")
print("|-----------------|----------------|")
print("|  $" + sellAmount + "\t  | $" + buyAmount + "\t   |")
print("------------------------------------")
