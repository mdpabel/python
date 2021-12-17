# Immutable
num = 1

print(id(num))

num += 1

print(id(num))

# Mutable

arr = [1, 2]

print(id(arr))

arr.append(3)

print(id(arr))
