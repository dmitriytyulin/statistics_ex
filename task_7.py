from statistics import mean


def _range(x):
    _R = [0 for _ in range(len(x))]
    for i in range(len(x)):
        _x = sorted(x)
        r = []
        for k in range(len(_x)):
            if _x[i] == _x[k]:
                r.append(k + 1)
        rr = mean(r)
        indexes = [index for index in range(len(x)) if x[index] == _x[i]]
        for index in indexes:
            _R[index] = rr
    return _R


X = [70, 72, 75, 72, 72, 76, 77]
Y = [33, 35, 38, 32, 33, 38, 38]
n = len(X) if len(X) == len(Y) else None

R_X = _range(X)
R_Y = _range(Y)

print(R_X)
print(R_Y)

R_X_R_Y = [R_X[i] - R_Y[i] for i in range(len(R_X))]
R_X_R_Y_2 = [el ** 2 for el in R_X_R_Y]

print(R_X_R_Y)
print(R_X_R_Y_2)
print(sum(R_X_R_Y_2))

r_s = 1 - ((6 * sum(R_X_R_Y_2)) / (n * (n ** 2 - 1)))

print()
print("result:")
print(r_s)
