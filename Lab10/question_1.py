def eratosthenes(n: int) -> int:
    """

    :param n:
    :return:
    """
    if n <= 0:
        print("Enter a positive integer.")
        return

    # 0 and 1 are not primes. 2 is prime.
    # Total number of entries is n + 1, so n + 1 - 2 = n - 1
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:  # Number is prime

            # Sieve the multiples of i
            for j in range(i * 2, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]


print(eratosthenes(30))
