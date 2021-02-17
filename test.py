import requests
from datetime import datetime


class Algo:
    def __init__(self, title, displayMiningFactor, displayMarketFactor, minimalOrderAmount,
                 minSpeedLimit, maxSpeedLimit, priceDownStep, minimalPoolDifficulty, port):
        self.title = title
        self.displayMiningFactor = displayMiningFactor
        self.displayMarketFactor = displayMarketFactor
        self.minimalOrderAmount = minimalOrderAmount
        self.minSpeedLimit = minSpeedLimit
        self.maxSpeedLimit = maxSpeedLimit
        self.priceDownStep = priceDownStep
        self.minimalPoolDifficulty = minimalPoolDifficulty
        self.port = port


r = requests.get("https://api2.nicehash.com/api/v2/time")
timeStamp = datetime.fromtimestamp(r.json()['serverTime'] / 1000)

r = requests.get("https://api2.nicehash.com/main/api/v2/mining/algorithms")

algosInfo = []
for algoData in r.json()['miningAlgorithms']:
    print(f"{algoData}\n")
    title = algoData['title']
    displayMiningFactor = algoData['displayMiningFactor']
    displayMarketFactor = algoData['displayMarketFactor']
    minimalOrderAmount = algoData['minimalOrderAmount']
    minSpeedLimit = algoData['minSpeedLimit']
    maxSpeedLimit = algoData['maxSpeedLimit']
    priceDownStep = algoData['priceDownStep']
    minimalPoolDifficulty = algoData['minimalPoolDifficulty']
    port = algoData['port']
    algosInfo.append(Algo())
