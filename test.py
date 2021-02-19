from pprint import pprint as pp
import Actions.Actions as Actions
# TODO get 3 orderbooks over 30 to 45 seconds and average the numbers for much more accurate results

print("\n=======================")
# pp()
Actions.getOrderBooks("KECCAK", 10)
print("=======================")
