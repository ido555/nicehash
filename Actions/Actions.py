from Enums.ApiURIs import ApiURIs
from Enums.OrderType import OrderType
from Models.Algo import Algo
from Models.OrderBook import OrderBook
from Models.Order import Order
import requests
from datetime import datetime


def getServerTime():
    r = requests.get("https://api2.nicehash.com/api/v2/time")
    return datetime.fromtimestamp(r.json()['serverTime'] / 1000)


def getOrderBooks(algorithm, size):
    """ recommended size (orders amount per page) is above 1000"""
    headers = {'algorithm': algorithm, 'size': size}
    r = requests.get(ApiURIs.hashPowerOrderBook.value, headers)

    orderBooks = []
    date = getServerTime()
    data = r.json()['stats']
    for orderBook in data.values():
        tempOrderBook = OrderBook(algorithm, date)
        for order in orderBook.get('orders'):
            orderType = OrderType[order.get('type')]
            price = order.get('price')
            limit = order.get('limit')
            rigsCount = order.get('rigsCount')
            isAlive = order.get('alive')
            orderId = order.get('id')
            tempOrderBook.addOrder(Order(orderType, price, limit, rigsCount, isAlive, orderId))
        orderBooks.append(tempOrderBook)
    return orderBooks


def getAlgosInfo():
    r = requests.get(ApiURIs.serverTime.value)
    date = datetime.fromtimestamp(r.json()['serverTime'] / 1000)
    algosInfo = []
    r = requests.get(ApiURIs.miningAlgosInfo.value)
    for algoInfo in r.json()['miningAlgorithms']:
        title = algoInfo['title']
        algorithm = algoInfo['algorithm']
        displayMiningFactor = algoInfo['displayMiningFactor']
        displayMarketFactor = algoInfo['displayMarketFactor']
        minimalOrderAmount = algoInfo['minimalOrderAmount']
        minSpeedLimit = algoInfo['minSpeedLimit']
        maxSpeedLimit = algoInfo['maxSpeedLimit']
        priceDownStep = algoInfo['priceDownStep']
        minimalPoolDifficulty = algoInfo['minimalPoolDifficulty']
        port = algoInfo['port']
        infoDate = date
        algosInfo.append(
            Algo(title, algorithm, displayMiningFactor, displayMarketFactor, minimalOrderAmount, minSpeedLimit,
                 maxSpeedLimit, priceDownStep, minimalPoolDifficulty, port, infoDate))

    return algosInfo
