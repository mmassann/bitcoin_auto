#!python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

pjs_path = 'C:/phantomjs/bin/phantomjs.exe'

url = "https://inagoflyer.appspot.com/btcmac"

driver = webdriver.PhantomJS(executable_path=pjs_path)

def main():

	driver.get(url)
	print("Connection successful.")

	#fetch and print BuyVol
	for buyvol in driver.find_elements_by_id("buyVolumePerMeasurementTime"):
		print("BuyVolume:"+buyvol.text)

	#fetch and print SellVol
	for sellvol in driver.find_elements_by_id("sellVolumePerMeasurementTime"):
		print("SellVolume:"+sellvol.text)

	driver.quit()

if __name__ == '__main__':
	main()
