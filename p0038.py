from euler import concatenated_product

def find_pandigital_concatenated_products(pandigital_size, upper_limit):
    for a in range(2, upper_limit + 1):
        n = 1
        digits = set()
        while len(digits) < pandigital_size:
            p = a * n
            p_digits = [digit for digit in str(p)]
            p_digits_set = set(p_digits)

            if len(p_digits) > len(p_digits_set):
               break
            if any(digit in digits for digit in p_digits):
                break
            if '0' in p_digits:
                break

            for digit in p_digits:
                digits.add(digit)
            if len(digits) == pandigital_size:
                cp = concatenated_product(a, n)
                yield int(cp)
            n += 1

results = find_pandigital_concatenated_products(9, 10000)

print(max(results)) # 932718654
