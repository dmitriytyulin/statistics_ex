from math import sqrt
from statistics import mean


def s___2(__x):
    __s_2 = 0
    for __index in range(len(__x)):
        __s_2 += (__x[__index] - mean(__x)) ** 2
    __s_2 /= len(__x) - 1
    return __s_2


x = [58, 58, 55, 66, 62]
y = [93, 95, 93, 105, 104]

x_mid = mean(x)
y_mid = mean(y)

print(x_mid)
print(y_mid)

s_x_2 = s___2(x)
s_y_2 = s___2(y)

s_x = sqrt(s_x_2)
s_y = sqrt(s_y_2)

print(s_x_2)
print(s_y_2)
print(s_x)
print(s_y)

r = 0
for i in range(len(x)):
    r += (x[i] - x_mid) * (y[i] - y_mid)
r /= len(x) * s_x * s_y

print()
print(r)
