list = [1, 2, 4, 2, 1, 5]

set = set(list)

set2 = {1, 2, 5, 8, 9}

print(set)

# union
print(set | set2)
# intersection
print(set & set2)

print(len(set))
set2.add(10)

if 3 in set2:
    set2.remove(3)


print(set2)
