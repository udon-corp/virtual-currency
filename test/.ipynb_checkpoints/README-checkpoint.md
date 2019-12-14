# 固定の時系列データでテストする

## save
period=300なら100日分しか取ってこれない。  
100日分取ってきて、連結させる場合のpandasの関数はconcat  
グラフにする時には、昔のやつから連結させないと変な線が入るので注意。  
4年分のデータを4year_data.pklに保存した

## DataFrameのデータをpklから読み込む方法
data = pd.read_pickle(file)