from pprint import pprint as pp
import Actions.Actions as actions
from Models.OrderBook import htmlifyOrders
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
table = ""
for algo in actions.getAlgosInfo():
    for orderBook in actions.getOrderBooks(algo.algorithm, 1000):
        print(f"added: {algo.algorithm}, from the {orderBook.marketRegion} market region")
        table += htmlifyOrders(orderBook, orderBook.getCheapestOrders(), algo.displayMarketFactor)
        print("=====================================\n")
file = open(r"B:\xampp\htdocs\table.html", "w")

file.write("""
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    </head>
    <body>
    """)

file.write(table)
file.write("</body>")
file.close()

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
