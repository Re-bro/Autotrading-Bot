# 단일 코인에 대해 RSI 지표 계산하는 코드 
# ticker에 원하는 암호화폐, interval에 원하는 분/일/시
# 매 초마다 현재 RSI값 출력

import pyupbit
import pandas
import datetime
import time

def rsi(ohlc: pandas.DataFrame, period: int = 14):
    delta = ohlc["close"].diff()
    ups, downs = delta.copy(), delta.copy()
    ups[ups < 0] = 0
    downs[downs > 0] = 0

    AU = ups.ewm(com = period-1, min_periods = period).mean()
    AD = downs.abs().ewm(com = period-1, min_periods = period).mean()
    RS = AU/AD

    return pandas.Series(100 - (100/(1 + RS)), name = "RSI")  


while True:
    data = pyupbit.get_ohlcv(ticker="KRW-XRP", interval="minute5")
    now_rsi = rsi(data, 14).iloc[-1]
    print(datetime.datetime.now(), now_rsi)
    time.sleep(1)
