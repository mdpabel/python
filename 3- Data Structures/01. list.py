basic = [1, 2, 3, 5]
matrix = [[1, 2], [3, 4]]
zeros = [0] * 10
seq = list(range(0, 20, 1))
chars = list("Hello world!")


print(chars)
print(len(chars))

# Accessing Items
print(seq[0])
print(seq[-1])
print(seq[:5])
print(seq[::2])
print(seq[::-1])
print(seq[0:10:2])


# List Unpacking
first, *rest, last = seq
print(first, last, rest)

# Looping over lists
print("====== Looping over lists =======")

letters = ['a', 'b', 'c']

for letter in letters:
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

# ADD and REMOVE
print("====== ADD and REMOVE =======")

letters.append("d")
letters.insert(0, '-')
print(letters)

letters.pop(2)
letters.remove('-')
del letters[1:4]
letters.clear()

print(letters)

#  Finding Items
print("====== Finding =======")
letters = ['x', 'a', 'b', 'c', 'a']
print(letters.index('a'))

if 'd' in letters:
    print(letters.index('d'))

print(letters.count("a"))


# Sort
print("====== SORT =======")
letters.sort(reverse=True)
print(letters)

products = [('laptop', 999), ('pc', 1000), ('mobile', 299)]

products.sort(reverse=True, key=lambda item: item[1])
print(products)
