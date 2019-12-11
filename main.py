import pandas as pd

# poloniexのAPI準備
polo = poloniex.Poloniex()

    # period[分]間隔でdays日分読み込む
chart_data = polo.returnChartData('BTC_ETH', period=minutes*60, start=time.time()-polo.DAY*days, end=time.time())

    # pandasにデータの取り込み
df = pd.DataFrame(chart_data)

print(df)
