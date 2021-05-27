import pyupbit
import pandas
import datetime
import time
from Trade import buy, sell
from RSI import rsi
from apikey import upbit

# 이용할 코인 리스트
coinlist = ["KRW-ETC", "KRW-BCH", "KRW-EOS"] # Coin ticker 추가
lower28 = []
higher72 = []
# initiate
for i in range(len(coinlist)):
    lower28.append(False)
    higher72.append(False)

# RSI에 따른 매매 작업
while(True): # 사용시 True로
    for i in range(len(coinlist)):
        data = pyupbit.get_ohlcv(ticker=coinlist[i], interval="minute3")
        now_rsi = rsi(data, 14).iloc[-1]
        if now_rsi <= 28 and lower28[i] == False: 
            lower28[i] = True
            print("코인명: ", coinlist[i])
            buy(coinlist[i])
        elif now_rsi >= 72 and higher72[i] == False:
            print("코인명: ", coinlist[i])
            sell(coinlist[i])
            higher72[i] = True
        elif now_rsi >= 45 and now_rsi <= 55:
            lower28[i] = False
            higher72[i] = False
    time.sleep(0.5)

