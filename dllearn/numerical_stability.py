
base = 1000000000

delta = 0.000001

sum = 0

sum += base

for i in range(1000000):
    sum += delta

print(sum - base)

