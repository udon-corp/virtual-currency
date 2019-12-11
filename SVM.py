import poloniex
import time
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

polo = poloniex.Poloniex()

# 5分(300s)間隔で100日分のデータを取得
chart_data = polo.returnChartData('USDT_BTC', period=300, start=time.time()-polo.DAY*100, end=time.time())

df = pd.DataFrame(chart_data)
#APIからString型として受け取るため、float型に変換
data = df['close'].astype(float)

# x:入力データ, t:ラベル
x, t = [], []
data_count = len(data)

# 窓関数の枠
win_6h = 2*6*6
win_1h = 2*6

# 6h分に平均化
MA_6h = pd.Series.rolling(df['close'], win_6h).mean()
# 1h分に平均化
MA_1h = pd.Series.rolling(df['close'], win_1h).mean()

# 上昇率（降下率）を比較
for i in range(win_6h-1, data_count-1):
    rate_for_MA_6h = data[i] / MA_6h[i] - 1
    rate_for_MA_1h = data[i] / MA_1h[i] - 1
    rate_for_before_5_minutes = data[i] / data[i-1] - 1

    _x = [data[i], rate_for_MA_6h * 25, rate_for_MA_1h * 50, rate_for_before_5_minutes * 100]

    _t = 1 if data[i] <= data[i+1] else 0
    x.append(_x)
    t.append(_t)
    
# 75%を訓練用、25%を検証用
N_train = int((data_count - win_6h) * 0.75)
x_train, x_test = x[:N_train], x[N_train:]
t_train, t_test = t[:N_train], t[N_train:]

# 以下、学習

from sklearn import svm
# 線形サポートベクターマシンを準備
clf = svm.LinearSVC()
# 訓練データを使ってモデルの学習
clf.fit(x_train, t_train)

# 予測値
predicted = clf.predict(x_test)

result = []
for n in range(len(t_test)):
    _result = True if t_test[n] == list(predicted)[n] else False
    result.append(_result)
    
matched_count = len(['matched!!!' for n in result if n==True])
matched_percent = matched_count / len(predicted)

print(matched_percent)


# グラフの表示
plt.rcParams['figure.figsize'] = 15, 6
plt.title("BCH_Chart")
plt.xlabel("date")
plt.ylabel("price")
plt.grid(True)

#プロット
plt.plot(data)
plt.show()
