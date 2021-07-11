#!/usr/bin/python3

''' python has a build-in decorator for memoizing any function  '''

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


if __name__ == "__main__":
    print(fib(5))
    print(fib(50))
