import pybitflyer
import json
import time

# bitFlyer API setting
public_api = pybitflyer.API()
bitFlyer_keys = json.load(open('bitFlyer_keys.json', 'r'))
api = pybitflyer.API(api_key=bitFlyer_keys['key'], api_secret=bitFlyer_keys['secret'])

while True:
    time.sleep(1)
    Ticker = api.ticker(product_code="FX_BTC_JPY")
    print(Ticker["volume_by_product"],Ticker["best_ask"],Ticker["best_bid"])
