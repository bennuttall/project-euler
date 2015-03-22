from euler import is_prime

primes = [n for n in range(2, 1000000) if is_prime(n)]

longest = 0
longest_count = 0

for i in range(len(primes)):
    s = 0
    count = 0
    for j in range(i, len(primes)):
        if s > primes[-1]:
            break
        count += 1
        s += primes[j]
        if count > longest_count and s in primes:
            longest = s
            longest_count = count

print(longest) # 997651
