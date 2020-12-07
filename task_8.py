def delta(item):
    return item[1] - item[0]


def T(item):
    return (delta(item) * 100) / (0.5 * (item[0] + item[1]))


st_kg = [125, 129]
b_kg = [9.1, 8.8]
p_kg = [6.2, 6.4]

st_eg = [130, 138]
b_eg = [9, 8.5]
p_eg = [5.1, 5.5]

print(delta(st_kg))
print(T(st_kg))
print()

print(delta(b_kg))
print(T(b_kg))
print()

print(delta(p_kg))
print(T(p_kg))
print()

print(delta(st_eg))
print(T(st_eg))
print()

print(delta(b_eg))
print(T(b_eg))
print()

print(delta(p_eg))
print(T(p_eg))
print()
