def add(a: int, b: int = 5) -> int:
    return a + b


print(add(2, 3))


def mul(*lists):
    res = 1
    for num in lists:
        res *= num
    return res


print(mul(1, 2, 4, 5))


def storeUser(**user):
    print(user)


storeUser(id=1, name="MD Pabel")
