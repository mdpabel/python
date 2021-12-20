# https://codingbat.com/prob/p107010

def first_half(str):
    n = int(len(str) / 2)

    if len(str) % 2 == 1:
        n = n + 1

    return str[:n]
