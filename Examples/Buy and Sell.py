# 매매 기능 함수 코드
# 현재 잔고 or 보유 수량에 따라 매매할 비욜 직접 조정
# 함수 인자에 코인 ticker 넣으면 매매 작업 수행
# res 변수에 매매 결과 저장. 추후 엑셀에 기록

import pyupbit
import pandas
import datetime
import time

# 시장가 매수 함수
def buy(coin):
    money = upbit.get_balance("KRW")
    if money < 20000 :
        res = upbit.buy_market_order(coin, money)
    elif money < 50000:
        res = upbit.buy_market_order(coin, money*0.4)
    elif money < 100000 :
        res = upbit.buy_market_order(coin, money*0.3)
    else :
        res = upbit.buy_market_order(coin, money*0.2)
    return

# 시장가 매도 함수
def sell(coin):
    amount = upbit.get_balance(coin)
    cur_price = pyupbit.get_current_price(coin)
    total = amount * cur_price
    if total < 20000 :
        res = upbit.sell_market_order(coin, amount)
    elif total < 50000:
        res = upbit.sell_market_order(coin, amount*0.4)
    elif total < 100000:
        res = upbit.sell_market_order(coin, amount*0.3)        
    else :
        res = upbit.sell_market_order(coin, amount*0.2)
    return


# RSI에 따른 매매 작업
while(1):
    for i in range(len(coinlist)):
        data = pyupbit.get_ohlcv(ticker=coinlist[i], interval="minute3")
        now_rsi = rsi(data, 14).iloc[-1]
       # print("코인명: ", coinlist[i])
       # print("현재시간: ", datetime.datetime.now())
       # print("RSI :", now_rsi)
       # print()
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

