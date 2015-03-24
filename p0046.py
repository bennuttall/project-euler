from euler import is_prime

primes = [n for n in range(10000) if is_prime(n)]

doubled_squares = [2*n**2 for n in range(10000)]

composite_numbers = (n for n in range(9, 10001, 2) if not is_prime(n))

for c in composite_numbers:
    solved = False
    for p in (n for n in primes if n < c):
        solution = c - p
        if solution in doubled_squares:
            solved = True
            break
    if not solved:
        print(c) # 5777
        break
