# factorial calculation

def factorial(n):
    if (n ==1 or n == 0):
        return 1
    return n * factorial(n-1)

print(factorial(10))

def fib(n):
    if n == 1 :
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

print(fib(4))
