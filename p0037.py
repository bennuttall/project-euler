from euler import is_prime

def is_left_truncatable_prime(n):
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])):
            return False
    return True

def is_right_truncatable_prime(n):
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[:-i])):
            return False
    return True

def is_truncatable_prime(n):
    return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)

primes = [n for n in range(10, 1000000) if is_prime(n)]

truncatable_primes = [n for n in primes if is_truncatable_prime(n)]

print(sum(truncatable_primes)) # 748317
