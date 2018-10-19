__author__ = 'Reijer'

memo = {1:1}

def fib(n, m):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        memo[n] = 1
        return memo[n]
    elif n == 2:
        memo[n] = 1
        return memo[n]
    else:
        if not n in memo:
            memo[n] = fib(n-1, m) + fib(n-2, m) - fib(n-m-1, m)
        return memo[n]

def test():
    n = 94
    m = 20
    print fib(n, m)



if __name__ == '__main__':
    test()