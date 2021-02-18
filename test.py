import requests
from pprint import pprint as pp
from datetime import datetime
from Models import Algo
# noinspection SpellCheckingInspection
def getAlgos():
    r = requests.get("https://api2.nicehash.com/api/v2/time")
    date = datetime.fromtimestamp(r.json()['serverTime'] / 1000)
    algosInfo = []
    r = requests.get("https://api2.nicehash.com/main/api/v2/mining/algorithms")
    for algoData in r.json()['miningAlgorithms']:
        title = algoData['title']
        displayMiningFactor = algoData['displayMiningFactor']
        displayMarketFactor = algoData['displayMarketFactor']
        minimalOrderAmount = algoData['minimalOrderAmount']
        minSpeedLimit = algoData['minSpeedLimit']
        maxSpeedLimit = algoData['maxSpeedLimit']
        priceDownStep = algoData['priceDownStep']
        minimalPoolDifficulty = algoData['minimalPoolDifficulty']
        port = algoData['port']
        infoDate = date
        algosInfo.append(Algo(title, displayMiningFactor, displayMarketFactor, minimalOrderAmount, minSpeedLimit,
                              maxSpeedLimit, priceDownStep, minimalPoolDifficulty, port, infoDate))

    return algosInfo

def getOrderBook():
    r = requests.get("https://api2.nicehash.com/api/v2/time")
    date = datetime.fromtimestamp(r.json()['serverTime'] / 1000)
    algosInfo = []
    r = requests.get("https://api2.nicehash.com/main/api/v2/hashpower/orderBook")
    for algoData in r.json()['miningAlgorithms']:
        title = algoData['title']
        displayMiningFactor = algoData['displayMiningFactor']
        displayMarketFactor = algoData['displayMarketFactor']
        minimalOrderAmount = algoData['minimalOrderAmount']
        minSpeedLimit = algoData['minSpeedLimit']
        maxSpeedLimit = algoData['maxSpeedLimit']
        priceDownStep = algoData['priceDownStep']
        minimalPoolDifficulty = algoData['minimalPoolDifficulty']
        port = algoData['port']
        infoDate = date
        algosInfo.append(Algo(title, displayMiningFactor, displayMarketFactor, minimalOrderAmount, minSpeedLimit,
                              maxSpeedLimit, priceDownStep, minimalPoolDifficulty, port, infoDate))

    return algosInfo

for i in getAlgos():
    print("\n=======================")
    pp(i.__dict__)
    print("=======================")
