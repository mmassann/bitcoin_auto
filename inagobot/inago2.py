#!python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import time

pjs_path = 'C:/phantomjs/bin/phantomjs.exe'

url = "https://inagoflyer.appspot.com/btcmac"

driver = webdriver.PhantomJS(executable_path=pjs_path)

def inago():

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

	driver.quit()

while True:
	inago()
