import itertools
from typing import Iterator


def sieve_of_eratosthenes(limit: int) -> Iterator[int]:
    # We use bytearray because its way faster when multiplying
    sieve = bytearray([True]) * limit
    zero = bytearray([False])

    for p in range(2, int(limit ** 0.5)):
        if sieve[p]:
            # I chose to use slice assignment because its quicker then looping
            sieve[p ** 2:limit:p] = zero * ((limit - p ** 2 - 1) // p + 1)

    sieve[0] = sieve[1] = False

    # This is pretty much equivalent to (i for i, j in zip(range(limit), sieve) if j)
    return itertools.compress(range(limit), sieve)


def simple_is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
