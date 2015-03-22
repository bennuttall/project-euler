from euler import is_prime
from itertools import permutations

primes = [n for n in range(1000, 10000) if is_prime(n)]

for a in primes:
    perms = [int(''.join(p)) for p in permutations(str(a))]
    b = a + 3330
    if b in perms and b in primes:
        c = b + 3330
        if c in perms and c in primes:
            if a != 1487:
                print("%s%s%s" % (a, b, c)) # 296962999629
