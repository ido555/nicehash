from Enums.OrderType import OrderType


class Order:
    def __init__(self, orderType, price, limit, rigsCount, isAlive, orderId):
        if not isinstance(orderType, OrderType):
            raise TypeError("must use OrderType enum class for orderType")
        self.orderType = orderType
        self.orderId = orderId
        self.algorithm = price
        self.date = limit
        self.rigsCount = rigsCount
        self.isAlive = isAlive

