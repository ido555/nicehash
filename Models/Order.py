from Enums.OrderType import OrderType


class Order:
    def __init__(self, orderType, price, limit, rigsCount, isAlive, orderId):
        if not isinstance(orderType, OrderType):
            raise TypeError("must use OrderType enum class for orderType")
        self.orderType = orderType
        self.orderId = orderId
        self.price = price
        self.limit = limit
        self.rigsCount = rigsCount
        self.isAlive = isAlive

    def __repr__(self):
        return f"Price: {self.price}, Rigs: {self.rigsCount}, Hash Limit: {self.limit}, Order Type: {self.orderType}"
