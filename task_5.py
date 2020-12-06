from math import sqrt, fabs

n_x = 8
n_y = 7
x_mid = 28.5
y_mid = 37.5
m_x = 2.1
m_y = 1.5

t_l = fabs(x_mid - y_mid) / sqrt(m_x ** 2 + m_y ** 2)

print(t_l)
