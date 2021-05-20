import pyupbit
import time
import datetime

# 'interval'초 마다 비트코인 가격 가져오기
interval = 1
while False: # 사용시 True로
    now = str(datetime.datetime.now()).split('.')
    cur_price = pyupbit.get_current_price("KRW-BTC")
    print(now[0], "현재가 :", cur_price)
    time.sleep(interval)
