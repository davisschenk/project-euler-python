def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(multiples):
    ans = multiples[0]

    for i in multiples:
        ans = ((i * ans) / (gcd(i, ans)))

    return ans
