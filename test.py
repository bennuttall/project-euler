from euler import *

assert is_pandigital(192837465, 9)
assert not is_pandigital(199872631, 9)
assert is_pandigital(13542)
assert not is_pandigital(13742)

assert concatenated_product(192, 3) == '192384576'
assert concatenated_product(9, 5) == '918273645'
