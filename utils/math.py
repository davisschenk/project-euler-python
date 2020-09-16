from functools import reduce
from typing import Iterator, Set, Iterable


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(multiples: Iterable[int]) -> float:
    multiples = iter(multiples)
    ans = next(multiples)

    for i in multiples:
        ans = i * ans / gcd(i, ans)

    return ans


def product(arr: Iterator[int]) -> int:
    value = 1

    for num in arr:
        value *= num

    return value


def factors(n: int) -> Set[int]:
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def prime_factors(n: int):
    facs = []
    while n % 2 == 0:
        facs.append(2)
        n /= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            facs.append(i)
            n /= i

    if n > 2:
        facs.append(n)

    return facs


def get_digits(n: int) -> Iterator[int]:
    while n:
        n, d = divmod(n, 10)
        yield d


def get_first_digit(n: int) -> int:
    while n >= 10:
        n //= 10

    return int(n)
