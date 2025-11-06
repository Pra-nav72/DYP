"""Simple prime number utilities and a tiny CLI.

Usage:
  python O7prime.py            # prompts for a number
  python O7prime.py 17         # checks 17 and lists primes up to 17

Functions:
  is_prime(n) -> bool
  primes_upto(n) -> list[int]
"""

from __future__ import annotations

import math
import sys
from typing import List


def is_prime(n: int) -> bool:
    """Return True if n is prime. Handles n < 2 correctly.

    Uses trial division up to the integer square root with a small
    optimization to skip even numbers.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_upto(n: int) -> List[int]:
    """Return a list of all prime numbers <= n using the sieve of Eratosthenes.

    This is efficient for moderate n (e.g., up to a few million). For very
    large n specialized segmented sieves are recommended.
    """
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            step = p
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i, isprime in enumerate(sieve) if isprime]


def _print_check_and_list(n: int) -> None:
    print(f"Number: {n}")
    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
    primes = primes_upto(n)
    print(f"Primes up to {n} ({len(primes)} found):")
    print(primes)


def main(argv: list[str] | None = None) -> int:
    """Small CLI: if an integer arg is given, use it; otherwise prompt the user.

    Returns 0 on success, non-zero on input error.
    """
    args = argv if argv is not None else sys.argv[1:]
    if not args:
        try:
            s = input("Enter a positive integer (or 'q' to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if s.lower() == "q":
            return 0
        try:
            n = int(s)
        except ValueError:
            print("Invalid integer input")
            return 2
        _print_check_and_list(n)
        return 0

    # If an argument was provided, try to parse the first one as an int
    try:
        n = int(args[0])
    except ValueError:
        print("Usage: python O7prime.py [N]")
        return 2
    _print_check_and_list(n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
