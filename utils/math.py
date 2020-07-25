from functools import reduce
from typing import List, Iterator, Set


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(multiples: List[int]) -> float:
    ans = multiples[0]

    for i in multiples:
        ans = ((i * ans) / (gcd(i, ans)))

    return ans


def product(arr: Iterator[int]) -> int:
    value = 1

    for num in arr:
        value *= num

    return value


def factors(n: int) -> Set[int]:
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def get_digits(n: int) -> Iterator[int]:
    while n:
        n, d = divmod(n, 10)
        yield d


def get_first_digit(n: int) -> int:
    while n >= 10:
        n //= 10

    return int(n)
