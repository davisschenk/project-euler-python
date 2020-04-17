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

