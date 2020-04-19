from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(multiples):
    ans = multiples[0]

    for i in multiples:
        ans = ((i * ans) / (gcd(i, ans)))

    return ans


def product(arr):
    value = 1

    for num in arr:
        value *= num

    return value


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def get_digits(n):
    while n:
        n, d = divmod(n, 10)
        yield d

