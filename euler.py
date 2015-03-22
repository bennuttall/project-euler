def is_pandigital(number, n):
    """
    Returns True if number is n-digit pandigital, otherwise returns False.

    e.g. 13524 is 5-digit pandigital, 12346 is not.
    """

    digits = ''.join(str(digit) for digit in range(1, n + 1))
    ordered_number = ''.join(sorted(digit for digit in str(number)))
    return ordered_number == digits

assert is_pandigital(192837465, 9)
assert not is_pandigital(199872631, 9)
assert is_pandigital(13542, 5)
assert not is_pandigital(13742, 5)
