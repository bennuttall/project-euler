d = ''
n = 0
product = 1

powers_of_ten = list(reversed([10**i for i in range(8)]))

next_power = powers_of_ten.pop()

while powers_of_ten:
    n += 1
    d += str(n)
    if len(d) >= next_power:
        product *= int(d[next_power - 1])
        next_power = powers_of_ten.pop()

print(product) # 210
