

# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#pip install binance
#pip install python-binance
#pip install pandas
#pip install ta
#pip install aiohttp
#pip install numpy
import pandas as pd
from binance.client import Client

klinesT =Client().get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1HOUR,
                                        "01 January 2021")
df = pd.DataFrame(klinesT,columns=['timestamp','open','high','low','close','volume','close_time','quote_av','trades','tb_base_av','tb_quote_av','ignore'])
print()
del df['ignore']
del df['quote_av']
del df['tb_base_av']
del df['tb_quote_av']
del df['trades']
del df['close_time']
import bot3
print(df)
from time import time, sleep
while True:
    sleep(60 - time() % 60)

    print(time())