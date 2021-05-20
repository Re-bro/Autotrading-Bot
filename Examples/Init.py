# 초기에 설정할 정보들
# 매매에 이용될 코인 목록 or 기타 초깃값 설정
# 매매 전략과는 상관x

import pyupbit
import pandas
import datetime
import time

# API Key
access = "USER ACCESS KEY"
secret = "USER SECRET KEY"
upbit = pyupbit.Upbit(access, secret)

# 이용할 코인 리스트
coinlist = [] # Coin ticker 추가
coinnum = {}
lower28 = []
higher70 = []

# initiate
for i in range(len(coinlist)):
    coinnum[coinlist[i]] = i
    lower28.append(False)
    higher70.append(False)
