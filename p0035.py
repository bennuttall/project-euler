from euler import is_prime

def rotate(n):
    n = str(n)
    cycle = n * 2
    length = len(n)
    for i in range(length):
        yield cycle[i:i+length]

def is_circular_prime(n):
    return all(is_prime(int(''.join(rotation))) for rotation in rotate(n))

#primes = [n for n in range(1, 1000000) if is_prime(n)]

circular_primes = [n for n in range(1, 1000000) if is_prime(n) and is_circular_prime(n)]

print(len(circular_primes)) # 55
