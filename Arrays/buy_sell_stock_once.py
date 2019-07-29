
from typing import List

def buy_sell_stock_once(A:List[int])->int:

    profit = 0
    minNumber = 9999999

    for i in range(len(A)):
        minNumber = min(minNumber, A[i])
        profit = max(profit, A[i]-minNumber)
    return profit


print(buy_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
print(buy_sell_stock_once([315, 310, 310, 310, 310, 310, 270, 270, 270]))
print(buy_sell_stock_once([0, 315, 275, 295, 260, 270, 290, 230, 255, 315]))