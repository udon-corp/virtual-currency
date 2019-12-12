import pandas as pd
import poloniex
import time

def data_extraction(minutes=5, days=100, kind_money='USDT_BCH'):

    # poloniexのAPI準備
    polo = poloniex.Poloniex()

    # period[分]間隔でdays日分読み込む
    chart_data = polo.returnChartData(kind_money, period=minutes*60, start=time.time()-polo.DAY*days, end=time.time())

    # pandasにデータの取り込み
    df = pd.DataFrame(chart_data)
    
    return df