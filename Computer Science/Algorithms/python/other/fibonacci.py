#!/usr/bin/python3

# define a function that returns the nth fibonacci number,
# where the index of the first number is 0

def fib(n: int) -> int:
    if n < 2:  #base case
        return n
    return fib(n-2) + fib(n - 1)

if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
