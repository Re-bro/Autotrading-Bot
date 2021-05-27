import pyupbit
import pandas
import datetime
import time
from apikey import upbit

# 시장가 매수 함수
def buy(coin):
    money = upbit.get_balance("KRW")
    if money < 15000 :
        res = upbit.buy_market_order(coin, money)
    elif money < 50000 :
        res = upbit.buy_market_order(coin, 10000)
    elif money < 100000 :
        res = upbit.buy_market_order(coin, 15000)
    else :
        res = upbit.buy_market_order(coin, money*0.15)
    print(res)
    return

# 시장가 매도 함수
def sell(coin):
    amount = upbit.get_balance(coin)
    cur_price = pyupbit.get_current_price(coin)
    total = amount * cur_price
    if total < 15000 :
        res = upbit.sell_market_order(coin, amount)
    elif total < 30000 :
        res = upbit.sell_market_order(coin, amount*0.5)
    elif total < 50000 :
        res = upbit.sell_market_order(coin, amount*0.35)
    elif total < 100000 :
        res = upbit.sell_market_order(coin, amount*0.2)        
    else :
        res = upbit.sell_market_order(coin, amount*0.15)
    print(res)
    return
