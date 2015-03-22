def is_pandigital(number, n=None):
    """
    Returns True if number is n-digit pandigital, otherwise returns False.

    If n is not given, the number's length is used.

    e.g. 13524 is 5-digit pandigital, 12346 is not.
    """

    if n is None:
        n = len(str(number))

    digits = ''.join(str(digit) for digit in range(1, n + 1))
    ordered_number = ''.join(sorted(digit for digit in str(number)))
    return ordered_number == digits

def is_prime(n):
    """
    Returns True if n is prime, otherwise returns False.
    """

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def concatenated_product(n, m):
    """
    Returns the concatenated product of n and each element of (1, 2, ... , m).

    e.g. 192 and (1,2,3) => 192384576

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576
    """

    t = range(1, m+1)
    return ''.join(str(n*i) for i in t)
