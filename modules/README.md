# modulesの中身
## extraction.py
### data_extraction DataFrame(minutes=5, days=100, type_money='USDT_BCH')

poloniexでデータを引っ張っきて、データフレームに格納。
#### 引数
minutes: 何分間隔のデータか。   
days: 何日分か。多分1年までしか無理。  
kind_money: 持ってくる仮想通貨の種類。->[一覧](https://docs.poloniex.com/#currencies)

#### 戻り値
取ってきたデータ。pandasのDataFrameで。

## preprocessing
