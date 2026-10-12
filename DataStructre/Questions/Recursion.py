# factorial calculation

def factorial(n):
    if (n ==1 or n == 0):
        return 1
    return n * factorial(n-1)

print(factorial(10))
def febseq(n):
        def fib(n):
            if n == 1 :
                return 1
            if n == 0:
               return 0

            x = fib(n-1) + fib(n-2)
            return x

        for i in range(n+1):

         print(fib(i) , end=" ")


febseq(4)