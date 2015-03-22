from euler import is_prime
from itertools import permutations

def find_prime_pandigitals(upper_limit):
    digits = range(1, upper_limit + 1)
    pandigitals = [int(''.join(str(digit) for digit in n)) for n in permutations(digits)]
    prime_pandigitals = [n for n in pandigitals if is_prime(n)]
    return prime_pandigitals

for n in range(8, 1, -1):
    prime_pandigitals = find_prime_pandigitals(n)
    if prime_pandigitals:
        print(max(prime_pandigitals))
        break

# 7652413
