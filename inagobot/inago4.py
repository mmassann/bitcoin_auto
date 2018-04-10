#!python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import numpy as np
import pybitflyer
import json

bestbid = 0
bestask = 0
midprice = 0
before_Side = 0
position = 0
public_api = pybitflyer.API()
bitFlyer_keys = json.load(open('bitFlyer_keys.json', 'r'))
api = pybitflyer.API(api_key=bitFlyer_keys['key'], api_secret=bitFlyer_keys['secret'])

def placeOrder(side,price):
    api.sendchildorder(product_code = "FX_BTC_JPY",child_order_type = "LIMIT",price = price,side = side, size = 0.01)

class Inago:

	def inago(self):
		pjs_path = 'C:/phantomjs/bin/phantomjs.exe'
		url = "https://inagoflyer.appspot.com/btcmac"
		driver = webdriver.PhantomJS(executable_path=pjs_path)

		driver.get(url)
		print("Connection successful.")

		#fetch and print BuyVol
		for buyvol in driver.find_elements_by_id("buyVolumePerMeasurementTime"):
			bv = float(buyvol.text)
			print("BuyVolume:"+str(bv))
		#fetch and print SellVol
		for sellvol in driver.find_elements_by_id("sellVolumePerMeasurementTime"):
			sv = float(sellvol.text)
			print("SellVolume:"+str(sv))
		pos = np.sign(bv - sv)

		driver.quit()
		return pos
while True:
    INAGO = Inago()
    Side = INAGO.inago()
    midprice = public_api.board(product_code = "FX_BTC_JPY")["mid_price"]
    bestbid = public_api.ticker(product_code = "FX_BTC_JPY")["best_bid"]
    bestask = public_api.ticker(product_code = "FX_BTC_JPY")["best_ask"]
    getposition = api.getpositions(product_code = "FX_BTC_JPY")

    if getposition == []:
        position = 0

    if Side > 0 and position == 0:
        placeOrder("BUY",bestbid)
        placeOrder("SELL",midprice + 500)
        position = 1
        print("BUY")
    if Side < 0 and position == 0:
        placeOrder("SELL",bestask)
        placeOrder("BUY",midprice - 500)
        position = 1
        print("SELL")

    before_Side = Side
