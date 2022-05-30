import MetaTrader5 as mt5
import time

import threading
import timeit


def login(user_login,user_server,user_password):
    if not mt5.initialize(login=int(user_login), server=str(user_server), password=str(user_password)):
        print("initialize() failed, error code =", mt5.last_error())
        quit()
    else:
        print("User account connected")

# print("Choose quantity orders")
# orders = int(input())

def getTradeAllowed():
    terminal_info=mt5.terminal_info()._asdict()
    trade_allowed=terminal_info["trade_allowed"]
    return trade_allowed

def waitTradeAllowed():
    while getTradeAllowed()==False:
        if getTradeAllowed():
            print("Automatic trade ON")
        else:
            print("Please allow automatic trade")
            time.sleep(5)
    print("Automatic trade ON")

def setSymbol(user_symbol):
    symbol = str(user_symbol)
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        mt5.shutdown()
        quit()
    else:
        print(symbol, "is setted")
        return symbol

def sendOrder(req):
    mt5.order_send(req)

login(5555,"176.124.191.229:443","vswo5egr")
user_symbol_in="EURUSD.beta"
waitTradeAllowed()

request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": user_symbol_in,
        "volume": 0.05,
        "type": mt5.ORDER_TYPE_BUY,
        "price": 1.17878,
        "sl": 1.16878,
        "tp": 1.17908,
        "magic": 234000,
        "comment": ""
    }
def order(n=100):
    for i in range(n):
        sendOrder(request)


print(timeit.timeit(order,number=1))
