# https://dodona.be/nl/courses/4195/series/46779/activities/546000908


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
