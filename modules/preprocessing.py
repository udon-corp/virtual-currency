import numpy as np
import pandas as pd

#v_size分の値から次の値を予測する。
def predict_value(df, v_size=30, type_value='close'):

    # APIからString型として受け取るため、float型に変換
    data = df[type_value].astype(float)

    data_len = len(data)    #総データ数

    x, t = [None]*(data_len - v_size), [None]*(data_len - v_size)
    
    #変数とラベルの生成
    for i in range(data_len - v_size):
        x[i] = data[i : i+v_size]    #連続したmax_len個の値
        t[i] = data[i+v_size]    #x_valuの次の値

    #ndarray型に変換し形を直す
    x = np.array(x).reshape(data_len-v_size, v_size, 1)
    t = np.array(t).reshape(data_len-v_size, 1)
    
    return x, t

# 現在~period[時間]の平均を求めた後、乖離率（上昇率/降下率）とラベル(up or down)を求める。
def updown_SMA(df, period=5, type_value='close'):   

    # APIからString型として受け取るため、float型に変換
    data = df[type_value].astype(float)

    period = period*12
    # 移動平均(moving average)を求める
    # ave_periodは平均する区間
    MA = pd.Series.rolling(data, period).mean()

    # データの長さ
    data_count = len(data)

    # データ(x)とラベル(t)の初期化
    x = [None]*(data_count-period)
    t = [None]*(data_count-period)

    for i in range(period-1, data_count-1):
        # period時間の平均の価格からの乖離率を計算
        x[i] = data[i] / MA[i] - 1
        # 出力変数に「0 or 1（下落or上昇）」を準備
        t[i] = 1 if data[i] <= data[i+1] else 0

    return np.array(x), np.array(t)

