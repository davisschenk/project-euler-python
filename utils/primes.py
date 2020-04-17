import math


def sieve_of_eratosthenes(limit):
    nums = [True] * limit

    for p in range(2, limit):
        if nums[p]:
            for j in range(p ** 2, limit, p):
                nums[j] = False

    return [i for i, v in enumerate(nums) if v][2::]


def simple_is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i ** 2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True
