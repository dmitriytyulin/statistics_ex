from math import sqrt, factorial


def bernulli(__n, __m, __p):
    return (factorial(__n) / (factorial(__m) * factorial(__n - __m))) * __p ** __m * (1 - __p) ** (__n - __m)


P = 0.7
n = 2

distribution = {}
for m in range(n + 1):
    distribution[m] = bernulli(n, m, P)

M_x = 0
for index, value in distribution.items():
    M_x += index * value

D = 0
for index, value in distribution.items():
    D += value * (index - M_x) ** 2

sigma = sqrt(D)

print(distribution)
print(M_x)
print(D)
print(sigma)
