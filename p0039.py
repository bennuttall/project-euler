from math import sqrt
from operator import itemgetter

results = {p: 0 for p in range(1001)}

for a in range(1, 1000):
    for b in range(1, a+1):
        c = sqrt(a**2 + b**2)
        if c % 1 == 0:
            c = int(c)
            p = a + b + c
            if p <= 1000:
                results[p] += 1

max_p = max(results.items(), key=itemgetter(1))[0]

print(max_p) # 840
