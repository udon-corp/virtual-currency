# 自作モジュール
import modules.extraction as ex
import modules.split as sp

# データの取り込み-DataFrame(minutes=5, days=100, type_value='close')
df = ex.data_extraction()

# 
x,t = sp.predict_value(df)
rate_SMA()