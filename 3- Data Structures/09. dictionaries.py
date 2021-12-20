obj = {
    "name": "MD Pabel",
    "id": 111111
}

print(obj)

# Access
print(obj['name'])
print(obj.get("name"))
print(obj.values())
print(obj.keys())
print(obj.items())

# Modify
obj['id'] = 222222
obj.update({'name': 'Md Pabel'})
print(obj)


# ADD
obj['bd'] = 1997

print(obj)

# delete
obj.pop('bd')

if 'user' in obj:
    del obj['user']

print(obj)


# LOOP
for key, value in obj.items():
    print(key, value)


# COPY
# copied = obj.copy()
copied = dict(obj)
obj['test'] = 'test'
print(copied)
print(obj)
