from math import sqrt

n = 16
gamma = 0.99
x_mid = 36
s = 2

mu = n - 1

t_gamma = 2.946

print(f"Mu in [{x_mid - t_gamma * s / sqrt(n)}; {x_mid + t_gamma * s / sqrt(n)}]")
