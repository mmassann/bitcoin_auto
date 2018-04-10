import requests
import json
import numpy as np
import pandas as pd

one_m = []
five_m = []
if __name__ == "__main__":
    #ローソク足の時間を指定
    periods = ["60","900"]

    #クエリパラメータを指定
    query = {"periods":','.join(periods)}

    #ローソク足取得
    res = json.loads(requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params=query).text)["result"]

    #表示
    for period in periods:
        print("period = "+period)
        row = res[period]
        length = len(row)
        if period == "60":
            for column in row[:length-4:-1]:
                one_m.append(column[4])
                print(one_m)
        if period == "900":
            for column in row[:length-4:-1]:
                five_m.append(column[4])
                print(five_m)

    x = np.linspace(1, len(one_m), len(one_m))
    a,b = np.polyfit(x, one_m, 1)
    print(a)
    c,d = np.polyfit(x, five_m, 1)
    print(c)
