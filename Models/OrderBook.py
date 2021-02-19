from Models.Order import Order
from Enums.OrderType import OrderType


# TODO OPTIMIZATION use a dict in self.orders to index each order by its id and improve performance (in some cases)
#  dict = O(1)
#  list = O(n)

class OrderBook:
    def __init__(self, algorithm, date, marketRegion):
        self.algorithm = algorithm
        self.date = date
        self.marketRegion = marketRegion
        self.__orders = []

    def addOrder(self, order):
        if not isinstance(order, Order):
            raise TypeError("Must use the Order class")
        self.__orders.append(order)

    def getOrders(self):
        return self.__orders

    def deleteOrderById(self, orderId):
        for order in self.__orders:
            if order.orderId == orderId:
                self.__orders.remove(order)

    def deleteDeadOrders(self):
        for order in self.__orders:
            if not order.isAlive:
                self.__orders.remove(order)

    def deleteOrderWithoutRigs(self):
        for order in self.__orders:
            if order.rigsCount < 1:
                self.__orders.remove(order)

    def getOrdersByType(self, orderType):
        if not isinstance(orderType, OrderType):
            raise TypeError("must use OrderType enum class for orderType")
        filteredOrders = [];
        for order in self.__orders:
            if order.orderType == orderType:
                filteredOrders.append(order)
        return filteredOrders
