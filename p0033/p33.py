from fractions import Fraction
from operator import mul

curious = []

for d in range(10, 100):
    for n in range(10, d - 1):
        shared_digits = {str(digit) for digit in str(n) if digit in str(d)}
        if shared_digits:
            f = Fraction(n, d)
            for digit in shared_digits:
                n2 = int(str(n).replace(digit, '', 1))
                d2 = int(str(d).replace(digit, '', 1))

                if n2 > 0 and d2 > 0 and str(n)[-1] != '0':
                    f2 = Fraction(n2, d2)

                    if f == f2:
                        curious.append(f)

product = reduce(mul, curious, 1)

print(product.denominator)
