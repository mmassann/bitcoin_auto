import pybitflyer
import json

public_api = pybitflyer.API()
bitFlyer_keys = json.load(open('bitFlyer_keys.json', 'r'))
api = pybitflyer.API(api_key=bitFlyer_keys['key'], api_secret=bitFlyer_keys['secret'])

getposition = api.getpositions(product_code = "FX_BTC_JPY")
if getposition == []:
    print("None")
else:
    print("IN")

midprice = public_api.board(product_code = "FX_BTC_JPY")["mid_price"]
print(midprice)
