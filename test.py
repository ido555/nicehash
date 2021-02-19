from pprint import pprint as pp
import Actions.Actions as actions
from Enums.OrderType import OrderType

# TODO get 3 orderbooks over 30 to 45 seconds and average the numbers for much more accurate results

# str = 'STANDARD'
# orderType = OrderType(str)
# print(orderType)
# print("\n=======================")
# actions.getOrderBooks("SHA256", 1)
for orderBook in actions.getOrderBooks("SHA256", 10):
    pp(orderBook.__dict__)
# print("=======================")
