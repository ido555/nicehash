class Algo:
    def __init__(self, title, algorithm, displayMiningFactor, displayMarketFactor, minimalOrderAmount,
                 minSpeedLimit, maxSpeedLimit, priceDownStep, minimalPoolDifficulty, port, infoDate):
        self.title = title
        self.algorithm = algorithm
        self.displayMiningFactor = displayMiningFactor
        self.displayMarketFactor = displayMarketFactor
        self.minimalOrderAmount = minimalOrderAmount
        self.minSpeedLimit = minSpeedLimit
        self.maxSpeedLimit = maxSpeedLimit
        self.priceDownStep = priceDownStep
        self.minimalPoolDifficulty = minimalPoolDifficulty
        self.port = port
        self.infoDate = infoDate
