# -*- coding: utf-8 -*-
import pybitflyer
import time

#初期化
midprice = 0
before_midprice = 0
pos = 0 # Long : 1, Short : -1, No position : 0
public_api = pybitflyer.API()
api = pybitflyer.API(api_key="[]", api_secret="[]")
#中間価格の初期化
midprice = before_midprice =  public_api.board(product_code = "FX_BTC_JPY")["mid_price"]
#注文用のメソッド
def placeOrder(side):
    size = 0.001 # 枚数
    api.sendchildorder(product_code = "FX_BTC_JPY",child_order_type = "MARKET",side = side , size = size)


#メインループ
while True:
    time.sleep(20)
    #現在の中間価格を取得
    midprice = public_api.board(product_code = "FX_BTC_JPY")["mid_price"]

    #決済注文
    if pos == 1:
        print("Close Long position")
        placeOrder("SELL")
        pos = 0
        continue
    elif pos == -1:
        print("Close Short position")
        placeOrder("BUY")
        pos = 0
        continue

    #1分前より価格が高く、ノーポジの時
    if midprice - before_midprice > 0 and pos == 0:
            print("Long Entry")
            placeOrder("BUY") #ロングエントリー
            pos = 1#現在のポジションを更新

    #1分前より価格が低く、ノーポジの時
    if before_midprice - midprice > 0 and pos == 0:
            print("Short Entry")
            placeOrder("SELL") #ショートエントリー
            pos =-1 #現在のポジションを更新

    before_midprice = midprice # 価格をシフト
