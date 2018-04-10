#!python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import numpy as np
import pybitflyer
import json

before_Side = 0
position = 0
public_api = pybitflyer.API()
bitFlyer_keys = json.load(open('bitFlyer_keys.json', 'r'))
api = pybitflyer.API(api_key=bitFlyer_keys['key'], api_secret=bitFlyer_keys['secret'])

def placeOrder(side):
    api.sendchildorder(product_code = "FX_BTC_JPY",child_order_type = "MARKET",side = side , size = 1)

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
		pos = bv - sv

		driver.quit()
		return pos

while True:
	INAGO = Inago()
	Side = INAGO.inago()
	judge = abs(Side)
	Side = np.sign(Side)
	health = public_api.gethealth(product_code = "FX_BTC_JPY")["status"]
	print(health)
	if health == "NORMAL":
		if Side != before_Side:
			before_Side = Side
			if position == 1:
				placeOrder("SELL")
				position = 0
				print("BUYCLOSE")
				continue
			if position == -1:
				placeOrder("BUY")
				position = 0
				print("SELLCLOSE")
				continue

		if judge > 30:
			if Side > 0 and position == 0:
				placeOrder("BUY")
				position = 1
				print("BUY")
			if Side < 0 and position == 0:
				placeOrder("SELL")
				position = -1
				print("SELL")
