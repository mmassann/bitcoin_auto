import requests
import json

if __name__ == "__main__":
    #ローソク足の時間を指定
    periods = ["60","300"]

    #クエリパラメータを指定
    query = {"periods":','.join(periods)}

    #ローソク足取得
    res = json.loads(requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params=query).text)["result"]

    #表示
    for period in periods:
        print("period = "+period)
        row = res[period]
        length = len(row)
        for column in row[:length-8:-1]:
            print (column)
