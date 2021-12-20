tuple = (1, 2, 3, 4)
print(tuple[0])

one, two, *rest = tuple

print(one, two, rest)

for item in tuple:
    print(item)

t2 = (10, 20)

print(tuple + t2)

print(tuple.count(1))
print(tuple.index(2))

# Swapping Variables

x = 2
y = 3

x, y = y, x

print(x, y)
