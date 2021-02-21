# https://whattomine.com/calculators.json


# https://whattomine.com/COIN_ID.json?hr=1000&p=0&fee=1&cost=0&hcost=0&commit=Calculate
# hr = hashrate
# p = power in watts
# cost = cost per $/kWh
# fee = fees in %
# hr = hashrate
# hcost = hardware cost
"""
# Metric prefix from high to low:
Exa(hash)
Peta(hash)
Tera
Giga
Mega
Kilo
"""
"""
Nethash vs provided hash rate

when the Nethash is at the GH/s scale or lower the provided hash rate (hr) needs to be 1 order of magnitude lower
examples:
Nethash - GH/s, HR - MH/s
Nethash - MH/s, HR - KH/s


when the Nethash is at the PH/s or TH/s scales the provided hash rate (hr) needs to be 2 orders of magnitude lower
Nethash - PH/s, HR - GH/s
Nethash - TH/s, HR - MH/s
"""