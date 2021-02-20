from pprint import pprint as pp
import Actions.Actions as actions
import jsonpickle
from Enums.OrderType import OrderType
from Models.Order import Order
import random
import json
# TODO get 3 orderbooks over 30 to 45 seconds and average the numbers for much more accurate results

# str = 'STANDARD'
# orderType = OrderType(str)
# print(orderType)
# print("\n=======================")
# actions.getOrderBooks("SHA256", 1)
for orderBook in actions.getOrderBooks("DAGGERHASHIMOTO", 1000):
    print("=====================================\n")
    print(orderBook.marketRegion)
    for order in orderBook.getCheapestOrders():
        print(order.__repr__())
    print("=====================================\n")


# print("=======================")

# orders = []
# for i in range(0, 20):
#     orderType = OrderType.STANDARD
#     price = round(random.uniform(0.5, 5), 11)
#     limit = round(random.uniform(0.01, 1), 2)
#     rigsCount = random.randint(1, 40)
#     isAlive = True
#     orderId = i
#     orders.append(Order(orderType, price, limit, rigsCount, isAlive, orderId))
#
#
#

# pp(orders[2].__dict__)