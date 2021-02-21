from enum import Enum


class NicehashURIs(Enum):
    __baseURL = "https://api2.nicehash.com/"
    hashPowerOrderBook = __baseURL + "main/api/v2/hashpower/orderBook"
    miningAlgosInfo = __baseURL + "main/api/v2/mining/algorithms"
    serverTime = __baseURL + "api/v2/time"


class WhattomineURIs(Enum):
    __baseURL = "https://whattomine.com/"
    coins = __baseURL + "calculators.json"
    """Coin URI format: coins/ID_NUMBER.json"""
    coin = __baseURL + "coins/"
    serverTime = __baseURL + "api/v2/time"
