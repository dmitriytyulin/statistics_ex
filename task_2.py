from math import sqrt

x = [67, 69, 64, 66, 67, 68, 67, 68, 69, 61, 60, 71, 71, 65, 61, 65, 71, 68, 68, 64]

x_mid = 0
for i in range(len(x)):
    x_mid += x[i]
x_mid /= len(x)

D = 0
for i in range(len(x)):
    D += (x[i] - x_mid) ** 2
D /= len(x)

s = sqrt(D)

V = (s / x_mid) * 100

m_x = s / sqrt(len(x))

print(x_mid)
print(D)
print(s)
print(V)
print(m_x)
