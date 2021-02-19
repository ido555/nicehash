from enum import Enum

baseURL = "https://api2.nicehash.com/"


class ApiURIs(Enum):
    hashPowerOrderBook = baseURL + "main/api/v2/hashpower/orderBook"
    miningAlgosInfo = baseURL + "main/api/v2/mining/algorithms"
    serverTime = baseURL + "api/v2/time"
