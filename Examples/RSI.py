# RSI 지표 계산하는 코드 
# ticker에 원하는 암호화폐, interval에 원하는 분/일/시

import pyupbit
import pandas
import time

def rsi(ohlc: pandas.DataFrame, period: int = 14):
    delta = ohlc["close"].diff()
    gains, declines = delta.copy(), delta.copy()
    gains[gains<0] = 0
    declines[declines > 0] = 0

    _gain = gains.ewm(com=(period - 1), min_periods=period).mean()
    _loss = declines.abs().ewm(com=(period-1), min_periods=period).mean()

    RS = _gain/_loss
    return pandas.Series(100 - (100/(1+RS)), name = "RSI")

while True:
    data = pyupbit.get_ohlcv(ticker="KRW-XRP", interval="minute5")
    nrsi = rsi(data, 14).iloc[-1]
    print(nrsi)
    time.sleep(0.5)
