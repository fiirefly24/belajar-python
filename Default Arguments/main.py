# def net_price(list_price, discount=0, tax=0.05): # Set value after arg
#     return list_price * (1-discount)* (1+tax)
# print(net_price(500))
# print(net_price(500, 0.10))

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0,10)