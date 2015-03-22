from itertools import product
from euler import is_pandigital

one_four_four = [(a*b, str(a) + str(b) + str(a*b)) for a, b in product(range(1, 10), range(1000, 10000)) if len(str(a*b)) == 4]
two_three_four = [(a*b, str(a) + str(b) + str(a*b)) for a, b in product(range(10, 100), range(100, 1000)) if len(str(a*b)) == 4]

all_products = one_four_four + two_three_four

unique_pandigitals = {product for (product, mmp) in all_products if is_pandigital(mmp, 9)}

print(sum(unique_pandigitals)) # 45228
