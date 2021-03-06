import pyupbit
import pandas
import datetime
import time
from Trade import buy, sell
from RSI import rsi
from apikey import upbit
from write_xlsx import write_regularly

# 이용할 코인 리스트
coinlist = ["KRW-XRP", "KRW-ETH", "KRW-ETC", "KRW-BCH", "KRW-EOS", "KRW-OMG"] # Coin ticker 추가
lower27 = []
higher73 = []
# initiate
for i in range(len(coinlist)):
    lower27.append(False)
    higher73.append(False)

recordtime = [] # 4시간마다 기록
for i in range(6):
    recordtime.append(False)

# RSI에 따른 매매 작업
while(True): # 사용시 True로
    hour = str(datetime.datetime.now()).split(' ')[1].split('.')[0].split(':')[0]
    hour = int(hour)
    if hour % 4 == 1 and recordtime[hour // 4] == False:
        for i in range(6):
            recordtime[i] = False
        recordtime[hour//4] = True
        write_regularly(coinlist)

    for i in range(len(coinlist)):
        data = pyupbit.get_ohlcv(ticker=coinlist[i], interval="minute3")
        now_rsi = rsi(data, 14).iloc[-1]
        if now_rsi <= 27 and lower27[i] == False: 
            lower27[i] = True
            print("코인명: ", coinlist[i])
            buy(coinlist[i])
        elif now_rsi >= 73 and higher73[i] == False:
            print("코인명: ", coinlist[i])
            sell(coinlist[i])
            higher73[i] = True
        elif now_rsi >= 45 and now_rsi <= 55:
            lower27[i] = False
            higher73[i] = False
    time.sleep(0.5)

