import pyupbit
import pandas
import datetime
import time
from Trade import *
from RSI import *

# 이용할 코인 리스트
coinlist = ["KRW-BTC", "KRW-XRP", "KRW-ETC", "KRW-ETH", "KRW-BCH", "KRW-EOS"] # Coin ticker 추가
coinnum = {}
lower28 = []
higher70 = []

# initiate
for i in range(len(coinlist)):
    coinnum[coinlist[i]] = i
    lower28.append(False)
    higher70.append(False)

# RSI에 따른 매매 작업
while(True): # 사용시 True로
    for i in range(len(coinlist)):
        data = pyupbit.get_ohlcv(ticker=coinlist[i], interval="minute3")
        now_rsi = rsi(data, 14).iloc[-1]
        print("코인명: ", coinlist[i])
        print("현재시간: ", datetime.datetime.now())
        print("RSI :", now_rsi)
        print()
        if now_rsi <= 28 : 
            lower28[i] = True
        elif now_rsi >= 33 and lower28[i] == True:
            buy(coinlist[i])
            lower28[i] = False
        elif now_rsi >= 70 and higher70[i] == False:
            sell(coinlist[i])
            higher70 = True
        elif now_rsi <= 60 :
            higher70 = False

