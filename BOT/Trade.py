import pyupbit
import pandas
import datetime
import time
from apikey import upbit
from write_xlsx import write_trade, write_regularly

# 시장가 매수 함수
def buy(coin):
    money = upbit.get_balance("KRW")
    if money < 15000 :
        res = upbit.buy_market_order(coin, money-10)
    elif money < 50000 :
        res = upbit.buy_market_order(coin, 10000)
    elif money < 100000 :
        res = upbit.buy_market_order(coin, 12000)
    else :
        res = upbit.buy_market_order(coin, money*0.1)
    
    if 'error' not in res:
        write_trade(res, 0)
    print(res)
    return

# 시장가 매도 함수
def sell(coin):
    amount = upbit.get_balance(coin)
    cur_price = pyupbit.get_current_price(coin)
    total = amount * cur_price
    prev = upbit.get_balance("KRW")

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
    
    post = upbit.get_balance("KRW")
    if 'error' not in res:
        write_trade(res, post - prev)
    print(res)
    
    return
