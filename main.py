import pandas as pd
import poloniex
import time

# 自作モジュール
import modules.extraction as ex
import modules.split as sp

# データの取り込み-DataFrame(minutes=5, days=100, type_value='close')
df = ex.data_extraction()

print(df)