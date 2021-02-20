from Models.Order import Order
from Enums.OrderType import OrderType


# TODO OPTIMIZATION use a dict in self.orders to index each order by its id and improve performance (in some cases)
#  dict = O(1)
#  list = O(n)

# TODO make the delete methods return a list/dict rather than change the self.orders list/dict

class OrderBook:
    def __init__(self, algorithm, date, marketRegion):
        self.algorithm = algorithm
        self.date = date
        self.marketRegion = marketRegion
        self.__orders = []

    def addOrder(self, order):
        if not isinstance(order, Order):
            raise TypeError("Must use the Order class")
        if order.isAlive and order.rigsCount > 0:
            self.__orders.append(order)

    def getOrders(self):
        return self.__orders

    def setOrders(self, orders: list):
        self.__orders = orders

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

    def getCheapestOrders(self):
        """ Get 5 lowest price orders """
        tempOrders = self.__orders
        # TODO bad code from here on, good enough for POC
        for order in tempOrders:
            if not order.isAlive:
                tempOrders.remove(order)
            if order.rigsCount < 1:
                tempOrders.remove(order)

        tempOrders.sort(key=lambda o: o.price, reverse=False)
        cheapestOrders = []
        if len(tempOrders) > 2:
            for i in range(3):
                cheapestOrders.append(tempOrders[i])
        else:
            for i in range(len(tempOrders)):
                cheapestOrders.append(tempOrders[i])
        return cheapestOrders


def htmlifyOrders(orderBook, orders: Order, unitSize: str):
    if not isinstance(orderBook, OrderBook):
        raise TypeError("must use the OrderBook class")
    table = f"""
    <h2>Algo: {orderBook.algorithm}</h2>
    <table class="table">
        <tr>
            <th scope="col">Price</th>
            <th scope="col">Rigs</th>
            <th scope="col">Hash Power Limit in {unitSize}</th>
            <th scope="col">Order Type</th>
            <th scope="col">Region</th>
        </tr>
    """
    for order in orders:
        table += f"""
            <tr scope="row">
                <td>{order.price}</td>
                <td>{order.rigsCount}</td>
                <td>{order.limit}</td>
                <td>{order.orderType.value}</td>
                <td>{orderBook.marketRegion}</td>
            </tr>
        """
    table += "</table>"
    return table
